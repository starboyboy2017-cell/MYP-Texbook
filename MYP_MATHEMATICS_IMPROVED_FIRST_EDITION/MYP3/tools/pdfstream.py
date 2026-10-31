"""Read the MYP3 content streams glyph by glyph.

The book is drawn with ReportLab-style output: every run sits in its own
``BT ... Tm /F<name> <size> Tf (bytes) Tj T* ET`` block, and non-ASCII
characters are written as octal escapes of single-byte codes.  That makes the
page fully recoverable without trusting any font program: this module walks the
stream and returns, in drawing order, each glyph with its page position, its
font, its size and the raw byte code that drew it.

Everything else in tools/ builds on that: repair_pdf.py rewrites the codes,
fix_titles.py moves glyphs, verify_pdf.py audits what is left.
"""
import re
import zlib

import pymupdf

# font object number in the shipped file -> face name
FACES = {
    311: "Inter-SemiBold",
    315: "PlayfairDisplay-Regular",
    319: "PlayfairDisplay-Italic",
    323: "STIXTwoText-Regular",
    327: "STIXTwoText-Italic",
    331: "Inter-Medium",
    335: "PlayfairDisplay-SemiBold",
    339: "STIXTwoText-SemiBold",
    343: "STIXTwoMath-Regular",
    347: "Inter-Regular",
}

PAGE_W, PAGE_H = 595.2756, 841.8898

TOKEN = re.compile(
    rb"""
    (?P<str>\((?:\\.|[^\\()])*\))
  | (?P<hex><[0-9A-Fa-f\s]*>)
  | (?P<name>/[^\s/\[\]()<>{}%]*)
  | (?P<num>[-+]?(?:\d+\.\d*|\.\d+|\d+))
  | (?P<op>[A-Za-z'"*][A-Za-z0-9'"*]*)
  | (?P<arr>[\[\]])
    """,
    re.S | re.X,
)

OCT = re.compile(rb"\\([0-7]{1,3})")
SIMPLE = {b"n": b"\n", b"r": b"\r", b"t": b"\t", b"b": b"\b", b"f": b"\f"}


class Hex(bytes):
    """A hex string's bytes, marked so the text operators can tell it apart.

    Non-ASCII characters are written as `<...>` rather than as a literal, so a
    walk of the stream has to carry both kinds or it misses every maths symbol.
    """


def unescape(raw):
    """The bytes a PDF literal string stands for."""
    out = bytearray()
    i = 0
    n = len(raw)
    while i < n:
        c = raw[i]
        if c != 0x5C:
            out.append(c)
            i += 1
            continue
        i += 1
        if i >= n:
            break
        m = OCT.match(raw, i - 1)
        if m:
            out.append(int(m.group(1), 8) & 0xFF)
            i = m.end()
            continue
        if raw[i] in (0x0A, 0x0D):          # escaped newline
            i += 1
            continue
        out += SIMPLE.get(bytes([raw[i]]), bytes([raw[i]]))
        i += 1
    return bytes(out)


def mul(m, n):
    a, b, c, d, e, f = m
    A, B, C, D, E, F = n
    return (a * A + b * C, a * B + b * D,
            c * A + d * C, c * B + d * D,
            e * A + f * C + E, e * B + f * D + F)


IDENT = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


def page_bytes(page):
    data = page.read_contents()
    try:
        return zlib.decompress(data)
    except Exception:
        return data


class Glyph:
    """One drawn character."""
    __slots__ = ("page", "order", "x", "y", "size", "face", "code", "res")

    def __init__(self, page, order, x, y, size, face, code, res):
        self.page, self.order = page, order
        self.x, self.y, self.size = x, y, size
        self.face, self.code, self.res = face, code, res

    @property
    def ch(self):
        return chr(self.code)

    def __repr__(self):
        return f"<{self.face} {self.code:#04x} ({self.x:.1f},{self.y:.1f})>"


def faces_on(page):
    """PDF resource name (F5+0) -> face name, using the page's font list."""
    out = {}
    for f in page.get_fonts(full=True):
        xref = f[0]
        base = f[3]
        if xref in FACES:
            name = FACES[xref]
        elif "+" in base:                    # a file written by PyMuPDF keeps
            name = base.split("+", 1)[1]     # the face name in /BaseFont
        else:
            continue
        out[f[4] if len(f) > 4 else f[3]] = name
    return out


def glyphs(doc, pno):
    """Every glyph on page `pno`, in drawing order."""
    page = doc[pno]
    names = faces_on(page)
    data = page_bytes(page)
    ctm = IDENT
    stack = []
    tm = tlm = IDENT
    size = 0.0
    res = None
    face = None
    out = []
    operands = []
    order = 0
    for m in TOKEN.finditer(data):
        kind = m.lastgroup
        text = m.group(0)
        if kind == "op":
            op = text
            if op == b"q":
                stack.append(ctm)
            elif op == b"Q":
                ctm = stack.pop() if stack else IDENT
            elif op == b"cm" and len(operands) >= 6:
                ctm = mul(tuple(float(v) for v in operands[-6:]), ctm)
            elif op == b"BT":
                tm = tlm = IDENT
            elif op == b"Tf" and len(operands) >= 2:
                name = operands[-2]
                res = (name.decode("latin-1") if isinstance(name, bytes) else name).lstrip("/")
                face = names.get(res)
                size = float(operands[-1])
            elif op == b"Tm" and len(operands) >= 6:
                tm = tlm = tuple(float(v) for v in operands[-6:])
            elif op in (b"Td", b"TD") and len(operands) >= 2:
                tx, ty = float(operands[-2]), float(operands[-1])
                tm = tlm = mul((1, 0, 0, 1, tx, ty), tlm)
            elif op == b"T*":
                tm = tlm = mul((1, 0, 0, 1, 0, -size * 1.2), tlm)
            elif op in (b"Tj", b"'", b'"', b"TJ"):
                if op in (b"'", b'"'):
                    tm = tlm = mul((1, 0, 0, 1, 0, -size * 1.2), tlm)
                if op == b"TJ":
                    parts = [p for p in operands if isinstance(p, bytes)]
                else:
                    parts = [operands[-1]] if operands and isinstance(operands[-1], bytes) else []
                for part in parts:
                    body = bytes(part) if isinstance(part, Hex) else unescape(part[1:-1])
                    for code in body:
                        x, y = mul(tm, ctm)[4:6]
                        out.append(Glyph(pno, order, x, y, size, face, code, res))
                        order += 1
                        if face:
                            tm = mul((1, 0, 0, 1, 0, 0), tm)
            operands = []
            continue
        if kind == "str":
            operands.append(text)
        elif kind == "hex":
            raw = re.sub(rb"\s+", b"", text[1:-1])
            if len(raw) % 2:
                raw += b"0"
            operands.append(Hex(bytes.fromhex(raw.decode())))
        elif kind == "num":
            operands.append(text.decode())
        elif kind == "name":
            operands.append(text.decode("latin-1"))
        elif kind == "arr":
            operands.append(text)
    return out


def line_key(g):
    return (g.page, round(g.y, 1))


def lines(doc, pno):
    """Glyphs on a page grouped into visual lines, top to bottom, left to right."""
    gs = glyphs(doc, pno)
    gs.sort(key=lambda g: (-round(g.y, 1), g.x, g.order))
    out, cur, cy = [], [], None
    for g in gs:
        if cy is None or abs(g.y - cy) <= 0.9:
            cur.append(g)
            cy = g.y if cy is None else cy
        else:
            out.append(cur)
            cur = [g]
            cy = g.y
    if cur:
        out.append(cur)
    for ln in out:
        ln.sort(key=lambda g: (g.x, g.order))
    return out


def line_text(ln, decode=None):
    return "".join(decode(g) if decode else g.ch for g in ln)


def page_text(doc, pno, decode=None):
    return [line_text(ln, decode) for ln in lines(doc, pno)]


def load(path):
    return pymupdf.open(path)


# --- block-level editing -------------------------------------------------
#
# Every text run is `BT ... ET` with its own Tm, Tf and Tj.  To move or resize a
# run without touching anything else, the editor needs the byte offsets of the
# numbers it is going to replace, which is what text_blocks() returns.

BT_RE = re.compile(rb"BT(.*?)ET", re.S)
TM_OPERANDS = re.compile(rb"([-+]?[\d.]+) ([-+]?[\d.]+) Tm")
SIZE_OPERANDS = re.compile(rb"/([A-Za-z0-9+.-]+) ([\d.]+) Tf")


class Block:
    __slots__ = ("page", "start", "end", "x", "y", "size", "res", "text",
                 "tm_span", "size_span", "str_span", "parts")

    def __init__(self, page, start, end, x, y, size, res, text, tm_span, size_span, str_span):
        self.page, self.start, self.end = page, start, end
        self.x, self.y, self.size, self.res, self.text = x, y, size, res, text
        self.tm_span, self.size_span, self.str_span = tm_span, size_span, str_span
        self.parts = []

    def __repr__(self):
        return f"<Block p{self.page+1} ({self.x:.1f},{self.y:.1f}) {self.size} {self.text!r}>"


def text_blocks(doc, pno):
    """Text runs on a page, with the byte spans an editor needs."""
    page = doc[pno]
    names = faces_on(page)
    data = page_bytes(page)
    out = []
    for m in BT_RE.finditer(data):
        body = m.group(1)
        tm = TM_OPERANDS.search(body)
        sz = SIZE_OPERANDS.search(body)
        if not (tm and sz):
            continue
        text = b""
        span = None
        parts = []
        for sm in re.finditer(rb"(\((?:\\.|[^\\()])*\)|<[0-9A-Fa-f\s]*>)", body):
            lit = sm.group(0)
            raw = unescape(lit[1:-1]) if lit[:1] == b"(" else bytes.fromhex(
                re.sub(rb"\s+", b"", lit[1:-1]).decode())
            text += raw
            parts.append((m.start(1) + sm.start(1), m.start(1) + sm.end(1),
                          lit[:1].decode(), raw))
            if span is None:
                span = (m.start(1) + sm.start(1), m.start(1) + sm.end(1))
        blk = Block(
            pno, m.start(), m.end(),
            float(tm.group(1)), float(tm.group(2)), float(sz.group(2)),
            sz.group(1).decode("latin-1"), text.decode("latin-1"),
            (m.start(1) + tm.start(1), m.start(1) + tm.end(2)),
            (m.start(1) + sz.start(2), m.start(1) + sz.end(2)),
            span,
        )
        blk.parts = parts
        out.append(blk)
    return out


def rewrite(data, edits):
    """Apply (start, end, replacement bytes) edits to a content stream."""
    out = bytearray()
    pos = 0
    for start, end, rep in sorted(edits):
        out += data[pos:start]
        out += rep
        pos = end
    out += data[pos:]
    return bytes(out)


def prepare(doc):
    """Merge each page's content streams so a page has exactly one.

    Called before any byte offset is measured: cleaning rewrites the stream, and
    an offset taken beforehand would point into the old bytes.
    """
    for page in doc:
        page.clean_contents()


def write_page(doc, pno, data):
    """Replace a page's (single, prepared) content stream."""
    xrefs = doc[pno].get_contents()
    if not xrefs:
        raise RuntimeError(f"page {pno + 1} has no content stream")
    doc.update_stream(xrefs[0], data, compress=True)
    for extra in xrefs[1:]:
        doc.update_stream(extra, b"", compress=False)


def tm_text(tm):
    """The operands before `Tm` as a flat list of numbers."""
    return [float(v) for v in tm.decode("latin-1").split()[:6]]
