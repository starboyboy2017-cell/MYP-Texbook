"""Wrap the ten chapter plate titles inside the text area.

The shipped book sets every plate title on one line at whatever size fits the
builder's rough guess: 21 pt for the longest, 36 pt for the shortest.  Two
consequences show in the delivered file - the long titles run past the right
trim edge, and the titles are all different sizes from plate to plate.

This script gives every plate one size, 28 pt, and wraps the long titles onto
two lines, which is how the printed MYP coursebooks set them (the reference book
uses 39 pt on two lines).  Positions are computed from the face's real advance
widths, so a wrapped title stays inside 60..539.3 pt and keeps clear of the
standfirst below it.

Nothing else on the page moves: the numeral, the kicker, the standfirst and
every body run keep their own coordinates.
"""
import os
import sys

import pymupdf
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, "tools"))
import pdfstream as ps  # noqa: E402
from codemap import decode  # noqa: E402

FONTS = {
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

# resource name -> face, read from the repaired file's own font list
PLAYFAIR_BY_RES = {}

TITLE_SIZE = 28.0
LEFT, RIGHT = 60.0, 539.3      # the text area
WIDTH = RIGHT - LEFT

_ADV = {}


def advances(face):
    if face not in _ADV:
        f = TTFont(os.path.join(HERE, "fonts", FONTS[face]))
        upm, hmtx, order = f["head"].unitsPerEm, f["hmtx"], f.getGlyphOrder()
        _ADV[face] = [hmtx.metrics[g][0] * 1000.0 / upm for g in order]
    return _ADV[face]


def text_width(face, text, size):
    adv = advances(face)
    total = 0.0
    for ch in text:
        code = ord(ch)
        total += adv[code] if code < len(adv) else 0.0
    return total * size / 1000.0


def is_plate(doc, pno):
    """A chapter plate carries a numeral larger than 60 pt above the title."""
    return any(b.size > 60 and b.text.strip().isdigit() and 560 < b.y < 600
               for b in ps.text_blocks(doc, pno))


def find_title(doc, pno):
    """The plate title: the largest serif run below the numeral."""
    best = None
    for b in ps.text_blocks(doc, pno):
        if 17 < b.size < 60 and 360 < b.y < 600 and b.text.strip():
            if b.y > 520:          # the kicker sits just under the numeral
                continue
            if len(b.text.strip()) < 4:
                continue
            if best is None or b.size > best.size:
                best = b
    return best


def face_of(block):
    for face in FONTS:
        if ps.faces_on.__module__:
            pass
    return None


def wrap(text, face, size):
    """Break a title into lines that fit the text area, at word boundaries."""
    words = text.split()
    if text_width(face, text, size) <= WIDTH:
        return [text]
    lines, cur = [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if cur and text_width(face, trial, size) > WIDTH:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def cap_height(face):
    """The face's cap height as a fraction of the em."""
    f = TTFont(os.path.join(HERE, "fonts", FONTS[face]))
    cap = getattr(f["OS/2"], "sCapHeight", 0) if "OS/2" in f else 0
    return (cap / f["head"].unitsPerEm) if cap else 0.70


def block_above(doc, pno, title):
    """The nearest text run above the title (the plate kicker)."""
    best = None
    for b in ps.text_blocks(doc, pno):
        if b.text.strip() and b.y > title.y + 6:
            if best is None or b.y < best.y:
                best = b
    return best


def block_below(doc, pno, title):
    """The nearest text run below the title (the standfirst)."""
    best = None
    for b in ps.text_blocks(doc, pno):
        if b.text.strip() and b.y < title.y - 6:
            if best is None or b.y > best.y:
                best = b
    return best


def main(src, dst):
    doc = pymupdf.open(src)
    global PLAYFAIR_BY_RES
    PLAYFAIR_BY_RES = {res: face for face, res in
                       ((face, res) for res, face in ps.faces_on(doc[0]).items())
                       if face.startswith("Playfair")}
    if not PLAYFAIR_BY_RES:
        for pno in range(min(60, len(doc))):
            for res, face in ps.faces_on(doc[pno]).items():
                if face.startswith("Playfair"):
                    PLAYFAIR_BY_RES[res] = face
    ps.prepare(doc)
    reports = []
    for pno in range(len(doc)):
        if not is_plate(doc, pno):
            continue
        title = find_title(doc, pno)
        if not title:
            continue
        face = PLAYFAIR_BY_RES.get(title.res)
        if face is None:
            continue
        text = "".join(decode(face, ord(c)) for c in title.text)
        lines = wrap(text, face, TITLE_SIZE)

        data = ps.page_bytes(doc[pno])
        edits = []
        if len(lines) == 1:
            if abs(title.size - TITLE_SIZE) > 0.05:
                edits.append((title.size_span[0], title.size_span[1],
                              b"%.4f" % TITLE_SIZE))
        else:
            # Fit the wrapped block into the band between the kicker above and
            # the standfirst below, centred, at display leading.
            lead = TITLE_SIZE * 1.05
            cap, desc = cap_height(face) * TITLE_SIZE, 0.24 * TITLE_SIZE
            above = block_above(doc, pno, title)
            below = block_below(doc, pno, title)
            top = above.y if above else title.y + 40
            bottom = (below.y + 0.7 * below.size) if below else title.y - 60
            span = cap + lead * (len(lines) - 1) + desc
            slack = max(0.0, (top - bottom) - span)
            first = top - slack / 2 - cap              # baseline of line 1
            x0 = LEFT
            produced = b""
            for i, line in enumerate(lines):
                y = first - i * lead
                produced += (b"BT 1 0 0 1 %.4f %.4f Tm /%s %.4f Tf 0 0 Td (%s) Tj T* ET\n"
                             % (x0, y, title.res.encode(), TITLE_SIZE,
                                line.encode("latin-1")))
            edits.append((title.start, title.end, produced.rstrip()))
        if not edits:
            continue
        new = ps.rewrite(data, edits)
        if b"(\\" in new or not new.strip():
            raise RuntimeError("refusing to write a damaged content stream")
        ps.write_page(doc, pno, new)
        reports.append((pno + 1, TITLE_SIZE, lines))

    doc.save(dst, garbage=3, deflate=True)
    for pno, size, lines in reports:
        print(f"  p{pno}: {size} pt  " + "  |  ".join(repr(l) for l in lines))
    print(f"wrapped {len(reports)} chapter titles -> {dst}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
