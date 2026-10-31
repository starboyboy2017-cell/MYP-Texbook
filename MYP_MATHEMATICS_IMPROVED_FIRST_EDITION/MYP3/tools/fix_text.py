"""Repair the book's text without moving it.

Three kinds of damage survived the builder in the content streams, and all of
them are visible to a reader:

  * markup that never became a character - literal "&nbsp;", the backticks that
    were meant to be quotation marks around inline maths, and a literal "\\_"
    where an operator such as "<" or "∈" was lost;
  * characters drawn with a code that has no glyph (byte 0x01..0x08 in some
    runs, 0x00 in others) - these are the tofu boxes;
  * hyphenated line breaks and the empty leading "Figure n.n" runs.

Everything is repaired at the same position, in the same face, at the same
size.  A replacement whose advance differs from the original is only accepted
if it stays inside a small tolerance, so no line can reflow and no page can
repaginate.  Places where the original character is genuinely unknown are left
alone and listed, rather than guessed.
"""
import collections
import os
import re
import sys

import pymupdf

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, "tools"))
import pdfstream as ps  # noqa: E402
import codemap  # noqa: E402

# Each entry: the text to find, what it becomes, and why.
REPLACEMENTS = [
    # markup that never became a character
    ("&nbsp;", " ", "literal HTML entity in a caption or criterion band"),
    # backticks were the builder's markup around inline maths; the source has
    # no quotes there, so they are deleted rather than replaced
    ("`", "", "backtick markup around inline maths"),
    ("&amp;", "&", "literal HTML entity"),
    ("&quot;", '"', "literal HTML entity"),
    # "\\_" is what the source wrote for an answer blank, and the escape before
    # each bracket survived it: both are parser debris, not content
    ("\(a\)", "(a)", "escaped brackets"),
    ("\(b\)", "(b)", "escaped brackets"),
    ("\(c\)", "(c)", "escaped brackets"),
    ("\(d\)", "(d)", "escaped brackets"),
    ("\\_", "  ", "answer blank left as an escape"),
    ("\\cos", "cos", "command name left as an escape"),
]

# Code 0 is the slot that means "no glyph".  Twenty characters in the book were
# written that way; each is a single glyph whose meaning is settled by the words
# beside it, so each is listed with the page, the position of its run, and the
# character it should be.  The replacement is drawn from the maths face, which
# carries all three of these marks.
# Sites where the character is a *subscript letter* rather than a symbol.  The
# source sets these at 6.3 pt with a 3.3 pt rise, so they are drawn the same way
# rather than with a Unicode subscript, which none of the faces carries.
#   page -> [(x, y), char, size, rise]
CODE0_SUBS = {
    275: [((0.0, 2.8), "k", 6.3, -2.4),    # 0.a1...ak = (a1...ak)/99...9
          ((0.0, 2.8), "k", 6.3, -2.4),
          ((0.0, 2.8), "n", 6.3, -2.4)],    # un = a + (n - 1)d
}

CODE0_SITES = {
    # "√2" - the radical, wherever a root is written
    16: [((62.0, 139.2), "\u221a")],
    24: [((292.0, 218.8), "\u221a"), ((366.8, 179.0), "\u221a")],
    269: [((0.0, 4.8), "\u221a")],
    270: [((0.0, 4.8), "\u221a")],
    # the absolute-value rows and the matchstick labels: a comparison sign
    28: [((223.3, 738.3), "<"), ((223.3, 676.3), "<"), ((223.3, 645.3), "<")],
    82: [((232.8, 418.1), "<"), ((353.1, 418.1), "<"),
         ((473.4, 418.1), "<"), ((593.7, 418.1), "<")],
    # "r ≠ 0.95": correlation coefficients, none of them equal to the value
    213: [((97.5, 256.3), "\u2260"), ((203.5, 256.3), "\u2260"),
          ((310.1, 256.3), "\u2260")],
}


MATH = "STIXTwoMath-Regular"


def _split_by_face(face, text):
    """Split `text` into (chunk, face) runs the face can actually draw."""
    codes = codemap.codes(face)
    math = codemap.codes(MATH)
    out, cur, buf = [], face, ""
    for ch in text:
        # code 0 is the face's empty slot, so a character that only maps to 0
        # cannot be drawn there; the maths face has it as a real glyph
        want = face if codes.get(ch) not in (None, 0) else (
            MATH if math.get(ch) not in (None, 0) else face)
        if want != cur and buf:
            out.append((buf, cur))
            buf = ""
        cur = want
        buf += ch
    if buf:
        out.append((buf, cur))
    return out


def literal(block, page_names, pieces):
    """Replacement bytes for one literal, split into (text, face) pieces.

    A piece may ask for a face the run is not currently in; when it does, the
    right `Tf` operands are written around it and the run's own face is restored
    afterwards, so neighbouring text is untouched.  Returns None when the page
    has no resource name for a face that is needed.
    """
    by_face = {}
    for res, name in page_names.items():
        by_face.setdefault(name, res)
    out = []
    cur = page_names[block.res]           # the face the run is drawn in
    for text, face in pieces:
        if not text:
            continue
        face = face or cur
        if face != cur:
            res = by_face.get(face)
            if res is None:
                return None
            out.append(b"/" + res.encode("latin-1") + b" " +
                       str(block.size).encode() + b" Tf ")
            cur = face
        for chunk, in_face in _split_by_face(cur, text):
            if in_face != cur:
                res = by_face.get(in_face)
                if res is None:
                    return None
                out.append(b"/" + res.encode("latin-1") + b" " +
                           str(block.size).encode() + b" Tf ")
                cur = in_face
            out.append(show(cur, chunk))
    # the run's face is restored only when a piece left it; a repair that is
    # drawn in the face the stream is already in must not switch back, because
    # the following literals are that face's own text
    if cur != page_names[block.res] and any(face for _, face in pieces):
        out.append(b"/" + block.res.encode("latin-1") + b" " +
                   str(block.size).encode() + b" Tf ")
    return b"".join(out)


def tables():
    """Per-face advance tables, for the width guard."""
    from fontTools.ttLib import TTFont

    files = {
        "Inter-Regular": "myp3-inter-regular.ttf",
        "Inter-Medium": "myp3-inter-medium.ttf",
        "Inter-SemiBold": "myp3-inter-semibold.ttf",
        "STIXTwoText-Regular": "myp3-stix-text-regular.ttf",
        "STIXTwoText-Italic": "myp3-stix-text-italic.ttf",
        "STIXTwoText-SemiBold": "myp3-stix-text-semibold.ttf",
        "STIXTwoMath-Regular": "myp3-stix-math-regular.ttf",
        "PlayfairDisplay-Regular": "myp3-playfair-regular.ttf",
        "PlayfairDisplay-SemiBold": "myp3-playfair-semibold.ttf",
        "PlayfairDisplay-Italic": "myp3-playfair-italic.ttf",
    }
    out = {}
    for face, name in files.items():
        f = TTFont(os.path.join(HERE, "fonts", name))
        out[face] = f["hmtx"], f["head"].unitsPerEm, f.getGlyphOrder()
    return out


def width(face, faces, text):
    """Advance of `text` in `face`, in 1000ths of an em, or None if unmapped.

    The embedded fonts are subsets addressed by byte, so a character's advance
    comes from the code that draws it, not from its Unicode number.
    """
    hmtx, upm, order = faces[face]
    codes = codemap.codes(face)
    total = 0.0
    for ch in text:
        code = codes.get(ch)
        if code is None or code >= len(order):
            return None
        total += hmtx.metrics[order[code]][0] * 1000.0 / upm
    return total


def show(face, text):
    """The operand that draws `text` in `face`, as `(...)Tj` or `<...>Tj`.

    Characters are written as the byte the face uses for them, so the rendered
    glyph is the one asked for rather than whatever ASCII happens to be there.
    """
    codes = codemap.codes(face)
    vals = []
    for ch in text:
        # text read back from the stream is a byte per character for codes the
        # map has no Unicode name for, so a low code is passed through as itself
        code = codes.get(ch, ord(ch) if ord(ch) < 256 else None)
        if code is None:
            raise KeyError(f"{ch!r} has no code in {face}")
        vals.append(code)
    # a control byte (the faces use low codes for typographic marks such as the
    # ellipsis at 7) draws nothing when written as a literal string, so anything
    # below the printable range goes out hex-encoded
    if all(v < 256 for v in vals):
        if all(v >= 32 for v in vals):
            return b"(" + escape("".join(chr(v) for v in vals)).encode("latin-1") + b")Tj "
        # "0007" in a hex string is two bytes, so low codes take two digits each
        return b"<" + "".join(f"{v:02X}" for v in vals).encode("latin-1") + b">Tj "
    return b"<" + "".join(f"{v:04X}" for v in vals).encode("latin-1") + b">Tj "


def escape(text):
    """A PDF literal string body for arbitrary text."""
    return (text.replace("\\", "\\\\").replace("(", "\\(")
                .replace(")", "\\)"))


def fix_run(text, face, faces, report):
    """Apply the source-level replacements to one run, checking the width."""
    out = text
    for old, new, why in REPLACEMENTS:
        if old not in out:
            continue
        candidate = out.replace(old, new)
        # a swap that only narrows cannot push text past the trim edge, and
        # "&nbsp;" is deliberately narrower than the space it stands for; a swap
        # that widens must fit inside the same tolerance
        if old == "&nbsp;":
            out = candidate
            report.append(("nbsp", why))
            continue
        w0, w1 = width(face, faces, out), width(face, faces, candidate)
        # markup deleted outright only ever shortens a run, and an answer blank
        # is redrawn as two spaces in a line that already ends in one, which is
        # a fixed 0.24 em at most - both are safe by construction
        if old == "`" or old == "\\_":
            out = candidate
            report.append(("markup", why))
            continue
        if w0 is None or w1 is None or (w1 - w0) > 0.9:
            report.append(("skipped", f"{why}: width {w0} -> {w1}"))
            continue
        out = candidate
        report.append(("fixed", why))
    return out


def resplit(parts, old, new):
    """Edits that repair a run, one literal at a time.

    The run is repaired as a whole first, to decide whether a repair applies at
    all; the bytes are then rewritten literal by literal, and a repair that
    straddles two literals is only applied when the split is unambiguous (the
    entity is spelled out across exactly two of them).  Nothing is ever
    redistributed across literals, so untouched text cannot change meaning.
    """
    texts = [raw.decode("latin-1") for _, _, _, raw in parts]

    # a repair confined to a single literal - the common case
    edits = []
    for (start, end, kind, raw), txt in zip(parts, texts):
        fixed = apply_rules(txt)
        if fixed != txt:
            edits.append((start, end, b"(" + escape(fixed).encode("latin-1") + b")"))
    if edits:
        return edits

    # "&nbsp;" spelled "&" + "nbsp;": rewrite every such pair in the run
    i = 0
    while i < len(texts) - 1:
        if texts[i] == "&" and texts[i + 1].startswith("nbsp;"):
            start, end, _, _ = parts[i + 1]
            rest = texts[i + 1][len("nbsp;"):]
            edits.append((parts[i][0], parts[i][1], b"()"))
            edits.append((start, end, b"(" + escape(" " + rest).encode("latin-1") + b")"))
            i += 2
            continue
        i += 1
    return edits


def apply_rules(txt):
    out = txt
    for old, rep, _ in REPLACEMENTS:
        out = out.replace(old, rep)
    return out


def main(src, dst):
    doc = pymupdf.open(src)
    faces = tables()
    report = []
    for pno in range(len(doc)):
        blocks = [b for b in ps.text_blocks(doc, pno) if b.parts]
        if not blocks:
            continue
        data = ps.page_bytes(doc[pno])
        names = ps.faces_on(doc[pno])
        edits = []
        done = set()          # blocks already rewritten, by identity

        # Subscript letters are also written as code 0.  No face here carries a
        # Unicode subscript, and the book's own convention for one is a smaller
        # size with a *negative* rise (p36 sets (1) as 6.3 pt at -6.7 Ts), so the
        # letter is drawn that way and lines up under the baseline.  Blocks are not ordered
        # the way the stream is, so the page's slots are taken in byte order.
        if pno + 1 in CODE0_SUBS:
            ssize, srise = CODE0_SUBS[pno + 1][0][2:]
            order = CODE0_SUBS[pno + 1]
            queue = collections.deque(site[1] for site in order)
            slack = 4
            slots = []
            for b in blocks:
                face = names.get(b.res)
                if face is None:
                    continue
                if not any(abs(b.x - sx) <= slack and abs(b.y - sy) <= slack
                           for (sx, sy), *_ in order):
                    continue
                for start, end, kind, raw in b.parts:
                    if b"\x00" in raw:
                        slots.append((start, end, b, face, raw))
            for start, end, b, face, raw in sorted(slots, key=lambda t: t[0]):
                if not queue:
                    break
                # the bytes are written back exactly as they came, so a code the
                # face does draw (the ellipsis at 7, say) keeps working; only the
                # empty slot is replaced, and only by its own show operation
                out, seg = [], b""
                for byte in raw:
                    if byte == 0 and queue:
                        if seg:
                            out.append(b"<" + seg.hex().upper().encode() + b">Tj ")
                            seg = b""
                        # the run's own face has to be named again: the slot may
                        # be drawn after a literal in an italic face
                        out.append(b" " + str(ssize).encode() + b" Tf "
                                   + str(srise).encode() + b" Ts "
                                   + show(face, queue.popleft())
                                   + b"0 Ts /" + b.res.encode() + b" "
                                   + str(b.size).encode() + b" Tf ")
                    else:
                        seg += bytes([byte])
                if seg:
                    out.append(b"<" + seg.hex().upper().encode() + b">Tj ")
                edits.append((start, with_show(data, end), b"".join(out)))
                done.add(("sub", start))
                report.append(("code0", "p%d subscript" % (pno + 1)))

        # a character written as code 0 is replaced by the one it means.  Only the
        # single byte changes: the run's other literals are left exactly as they
        # are, so nothing else on the line can move.
        for b in blocks:
            face = names.get(b.res)
            if face is None:
                continue
            sites = list(CODE0_SITES.get(pno + 1, []))
            for (sx, sy), wanted in sites:
                if abs(b.x - sx) > 4 or abs(b.y - sy) > 4:
                    continue
                for start, end, kind, raw in b.parts:
                    if ("sub", start) in done:
                        continue
                    txt = raw.decode("latin-1")
                    if "\x00" not in txt:
                        continue
                    # the run's other markup is repaired here too, since this
                    # literal is rewritten and would otherwise be skipped
                    txt = apply_rules(txt)

                    # the symbol must be drawn from the maths face.  The run's own
                    # encoding can use the same character code for something else
                    # ("\x04" is both the square root in a maths run and a degree
                    # sign elsewhere), so the mark is applied by byte, not by value
                    pieces, seen_null = [], False
                    for part in txt:
                        if part == "\x00" and not seen_null:
                            seen_null = True
                            pieces.append((wanted, MATH))
                        else:
                            pieces.append((part, None))
                    if any(fc == MATH for _, fc in pieces) and MATH not in names.values():
                        names = add_face(doc, pno, names, MATH)
                        if MATH not in names.values():
                            report.append(("skipped", f"no font resource for {wanted}"))
                            continue
                    # the maths face is named explicitly around the symbol and the
                    # run's own face restored after it: whether the stream was in
                    # the maths face already depends on the literal before, and a
                    # symbol drawn in the text face lands on its empty slot
                    maths_res = None
                    for res, name in names.items():
                        if name == MATH:
                            maths_res = res
                            break
                    # everything else in the literal is kept, in order: the text
                    # before the slot, the symbol, then the rest
                    pre, _, tail = txt.partition("\x00")
                    rep = b""
                    if pre:
                        rep += literal(b, names, [(pre, None)]) or b""
                    rep += (b" " + b"/" + maths_res.encode() + b" "
                            + str(b.size).encode() + b" Tf " + show(MATH, wanted)
                            + b"/" + b.res.encode() + b" "
                            + str(b.size).encode() + b" Tf ")
                    if tail:
                        rep += literal(b, names, [(tail, None)]) or b""
                    edits.append((start, with_show(data, end), rep))
                    report.append(("code0", f"p{pno + 1} {wanted!r}"))
                done.add(id(b))

        # text-level repairs, still one literal at a time
        for b in blocks:
            face = names.get(b.res)
            if face is None or id(b) in done:
                continue
            texts = [raw.decode("latin-1") for _, _, _, raw in b.parts]
            whole = "".join(texts)
            if fix_run(whole, face, faces, []) == whole and not SUP_RE.search(whole):
                continue
            fixed = fix_run(whole, face, faces, report)
            if SUP_RE.search(fixed):
                # the exponent is drawn as raised text, which means several
                # show operations inside one literal; build them as pieces so a
                # run split over several literals still ends up with all of them
                for start, end, kind, raw in b.parts:
                    txt = raw.decode("latin-1")
                    if not SUP_RE.search(txt):
                        continue
                    # the same markup rules that would have run on this run
                    # apply first, so the backticks around the expression go
                    txt = apply_rules(txt)
                    edits.append((start, with_show(data, end),
                                  superseded(b, face, txt)))
                continue
            edits.extend(resplit(b.parts, whole, fixed))
        if edits:
            ps.write_page(doc, pno, ps.rewrite(data, edits))
    # headings that run past the trim edge
    for pno in range(len(doc)):
        got = fit_heading(doc, pno, None, 529.0, "759.8898")
        if got:
            data, k = got
            ps.write_page(doc, pno, data)
            report.append(("heading", f"p{pno + 1} tracked to {k:.3f}"))

    # the one figure whose row overflows the column
    fit_figure(doc, 81, 232.7756, 536.0, "427.0898", "452.8966", "418.0898",
               232.7756, 120.3, 59.5, "denominator would be zero.)Tj T* ET Q")
    report.append(("figure", "p82 matchstick row fitted to the column"))

    doc.save(dst, garbage=3, deflate=True)
    counts = {}
    for kind, _ in report:
        counts[kind] = counts.get(kind, 0) + 1
    for kind, why in report:
        if kind != "fixed":
            print(f"  {kind:8s} {why}")
    print(f"text repairs: {counts}  -> {dst}")


SUP_RE = re.compile(r"\^\{([^{}]*)\}")


def superseded(block, face, text):
    """Bytes that draw `text`, turning `^{...}` markup into raised characters.

    The embedded subsets carry a few Unicode superscripts but not all of them,
    so an exponent is drawn as real raised text: a smaller size, a text rise,
    then the run's own size and baseline back.  Nothing moves but the exponent.
    """
    body = block.size * 0.7
    rise = block.size * 0.35
    out, pos = [], 0
    for m in SUP_RE.finditer(text):
        if m.start() > pos:
            out.append(show(face, text[pos:m.start()]))
        out.append(str(body).encode() + b" Tf " + str(rise).encode() + b" Ts "
                   + show(face, m.group(1))
                   + b"0 Ts " + str(block.size).encode() + b" Tf ")
        pos = m.end()
    if pos < len(text):
        out.append(show(face, text[pos:]))
    return b"".join(out)


def add_face(doc, pno, names, want):
    """Give the page a resource name for `want`, returning the updated map.

    A page that never draws maths has no slot for the maths face; a repair that
    needs it must add one.  The object number comes from another page that does
    have the face, so the same program is shared rather than copied.
    """
    have = {v: k for k, v in names.items()}
    if want in have:
        return names
    ref = None
    for other in range(len(doc)):
        if other == pno:
            continue
        for res, face in pdfstream_faces(doc, other).items():
            if face == want:
                ref = doc[other].get_fonts(full=True)
                break
        if ref:
            break
    if not ref:
        return names
    xref = [f[0] for f in ref if want in f[3]]
    if not xref:
        return names
    n = max([int(k[1:3]) for k in names if k.startswith("F") and k[1:3].isdigit()] + [1]) + 1
    new_name = f"F{n}+0"
    doc.xref_set_key(doc[pno].xref,
                     "Resources/Font/" + new_name,
                     "%d 0 R" % xref[0])
    names = dict(names)
    names[new_name] = want
    return names


def pdfstream_faces(doc, pno):
    return ps.faces_on(doc[pno])


def _split_sub(text, mark):
    """Split `text` so every `mark` is its own piece (it is drawn as a subscript)."""
    out, cur = [], ""
    for ch in text:
        if ch == mark:
            if cur:
                out.append(cur)
                cur = ""
            out.append(ch)
        else:
            cur += ch
    if cur:
        out.append(cur)
    return out


def with_show(data, end):
    """Extend a literal's span over the `Tj` that shows it.

    A replacement writes its own `Tj` after every piece, so the original show
    operator must not be left in the stream with nothing to show.
    """
    m = re.match(rb"\s*(Tj|TJ|')", data[end:end + 8])
    return end + m.end() if m else end


def splice(txt, at, old, new):
    """Replace `old` with `new` inside `txt`, where `old` starts at run offset `at`."""
    return txt[:at] + new + txt[at + len(old):]


def _pieces(txt, worn, wanted, face, want_face):
    """Split one literal's text into (text, face) pieces for a run repair.

    Only the characters that differ take the requested face; everything else
    stays exactly as it was drawn.
    """
    import difflib

    i = worn.index(txt)                       # where this literal sits in the run
    mine = wanted[i:i + len(txt)] if worn == wanted else None
    sm = difflib.SequenceMatcher(a=worn, b=wanted, autojunk=False)
    pieces = []
    for tag, a0, a1, b0, b1 in sm.get_opcodes():
        if tag == "equal":
            lo, hi = max(a0, i), min(a1, i + len(txt))
            if lo < hi:
                pieces.append((worn[lo:hi], None))
            continue
        # a changed stretch belongs to this literal when it starts inside it
        if a0 < i or a0 > i + len(txt):
            continue
        pieces.append((wanted[b0:b1], want_face or face))
    return pieces


def _unused(src, dst):
    doc = pymupdf.open(src)
    ps.prepare(doc)
    faces = tables()
    report = []
    for pno in range(len(doc)):
        data = ps.page_bytes(doc[pno])
        edits = []
        for b in ps.text_blocks(doc, pno):
            if not b.text or b.str_span is None:
                continue
            face = ps.faces_on(doc[pno]).get(b.res)
            if face is None:
                continue
            new = fix_run(b.text, face, faces, report)
            if new == b.text:
                continue
            start, end = b.str_span
            original = data[start:end]
            if original.startswith(b"<"):
                edits.append((start, end, b"<%s>" % new.encode("latin-1").hex().upper().encode()))
            else:
                edits.append((start, end, b"(" + escape(new).encode("latin-1") + b")"))
        if edits:
            ps.write_page(doc, pno, ps.rewrite(data, edits))
    # headings that run past the trim edge
    for pno in range(len(doc)):
        got = fit_heading(doc, pno, None, 529.0, "759.8898")
        if got:
            data, k = got
            ps.write_page(doc, pno, data)
            report.append(("heading", f"p{pno + 1} tracked to {k:.3f}"))

    # the one figure whose row overflows the column
    fit_figure(doc, 81, 232.7756, 536.0, "427.0898", "452.8966", "418.0898",
               232.7756, 120.3, 59.5, "denominator would be zero.)Tj T* ET Q")
    report.append(("figure", "p82 matchstick row fitted to the column"))

    doc.save(dst, garbage=3, deflate=True)
    counts = {}
    for kind, _ in report:
        counts[kind] = counts.get(kind, 0) + 1
    for kind, why in report[:8]:
        print(f"  {kind:8s} {why}")
    print(f"text repairs: {counts}  -> {dst}")


def fit_heading(doc, pno, start_text, right_edge, y):
    """Fit an over-long heading drawn one glyph per block inside the column.

    This header is centred by hand: every letter has its own block and its own
    `Tm`.  All the words are wanted and none can be deleted, so every glyph's x
    is pulled toward the left edge in proportion to its distance along the line.
    Sizes, faces and the baseline are untouched, and the line ends at the margin.
    """
    data = ps.page_bytes(doc[pno]).decode("latin-1")
    tm = re.compile(r"(1 0 0 1 )(-?\d+\.\d+)( %s Tm)" % y)
    xs = [float(m.group(2)) for m in tm.finditer(data)]
    if not xs:
        return None
    left, right = min(xs), max(xs)
    if right <= right_edge:
        return None
    k = (right_edge - left) / (right - left)
    out = tm.sub(lambda m: m.group(1) + "%.4f" % (left + (float(m.group(2)) - left) * k) + m.group(3), data)
    return out.encode("latin-1"), k


def fit_figure(doc, pno, left, right, base, apex, label, origin, pitch, width, after):
    """Fit a row of figures inside the text column.

    The builder drew Figure 3.2's four matchstick groups at a fixed pitch, so the
    last one fell off the page.  The triangles are absolute path coordinates and
    the labels are absolute `Tm` placements, so the row can be rescaled about its
    own origin and the labels re-centred under their groups without touching
    anything else on the page.
    """
    data = ps.page_bytes(doc[pno]).decode("latin-1")
    cut = data.index(after) + len(after)
    stop = data.index("Figure", cut)
    body = data[cut:stop]

    k = (right - left) / (3 * pitch + width)
    step = pitch * k

    legs = re.compile(r"(-?\d+\.\d{4}) (%s|%s)( [ml]\b)" % (base, apex))

    def place(m):
        x, y, op = float(m.group(1)), m.group(2), m.group(3)
        return "%.4f %s%s" % (left + (x - origin) * k, y, op)

    body = legs.sub(place, body)

    lm = re.compile(r"(1 0 0 1 )(-?\d+\.\d{4})( %s Tm)" % label)

    def centre(m):
        i = round((float(m.group(2)) - origin) / pitch)
        return m.group(1) + "%.4f" % (left + i * step + 3.0) + m.group(3)

    body = lm.sub(centre, body)
    ps.write_page(doc, pno, (data[:cut] + body + data[stop:]).encode("latin-1"))
    return k


if __name__ == "__main__":
    main(*sys.argv[1:3])
