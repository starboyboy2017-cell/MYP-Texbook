"""Repair the shipped MYP3 PDF object by object.

The delivered file came out of a builder whose embedded font programs and
ToUnicode maps were destroyed by a text round-trip.  Twenty stream objects are
invalid: the ten typefaces are unreadable and there is no searchable text at
all, so the book renders in whatever fallback face the viewer owns.

Everything else is intact - the page tree, every image, every content stream and
every /Widths array - so this script rewrites the file object by object:

  * each FontFile2 is replaced by the matching face built by build_fonts.py;
  * each ToUnicode CMap is regenerated from the recovered code map, so every
    glyph is mapped back to real Unicode for search and copy-paste;
  * the /Differences array is written out for each face, so a reader that
    resolves byte codes through glyph names finds the same glyph as one that
    resolves them through the embedded cmap;
  * a fresh cross-reference table and trailer are written, and the binary
    header comment is restored.

Drawing operators keep their original codes, coordinates and widths, so page
geometry is preserved exactly.
"""
import json
import os
import re
import sys
import zlib

from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, "tools"))
from codemap import CODES, table  # noqa: E402

# What the empty slot of each face actually draws (see build_fonts.py).
EMPTY_SLOTS = {
    "STIXTwoText-Regular": {0: "<"},
    "STIXTwoText-Italic": {0: "<"},
    "PlayfairDisplay-SemiBold": {0: "\u2260"},
}
# The correlation labels draw code 0 in the text face but mean "not equal", and
# the text faces only carry "<".  The drawn glyph is a property of the document,
# not of the face, so it is corrected in the content stream instead.

FONT_FILES = {
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

OBJ_RE = re.compile(rb"(?m)^(\d+) 0 obj")


def split_objects(raw):
    objs = {}
    for m in OBJ_RE.finditer(raw):
        start, num = m.start(), int(m.group(1))
        end = raw.find(b"endobj", start)
        objs[num] = raw[start:end + len(b"endobj")]
    return objs


def dict_of(obj):
    """The dictionary part of an object: from '<<' to '>>', stream or not."""
    start = obj.find(b"<<")
    end = obj.find(b">>", start)
    if start < 0 or end < 0:
        return obj.decode("latin-1")
    return obj[start:end + 2].decode("latin-1")


def make_tounicode(codes):
    lines = [
        "/CIDInit /ProcSet findresource begin",
        "12 dict begin",
        "begincmap",
        "/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def",
        "/CMapName /Adobe-Identity-UCS def",
        "/CMapType 2 def",
        "1 begincodespacerange",
        "<00> <FF>",
        "endcodespacerange",
    ]
    items = []
    for code in range(256):
        ch = table_from(codes, code)
        if ch is None:
            continue
        items.append((code, ch))
    for i in range(0, len(items), 100):
        chunk = items[i:i + 100]
        lines.append(f"{len(chunk)} beginbfchar")
        for code, ch in chunk:
            lines.append(f"<{code:02X}> <{ch.encode('utf-16-be').hex().upper()}>")
        lines.append("endbfchar")
    lines += ["endcmap", "CMapName currentdict /CMap defineresource pop", "end", "end"]
    return "\n".join(lines).encode("latin-1")


def table_from(codes, code):
    """The character a code stands for, ASCII included.

    Code 0 is never given a character: it is the slot a reader falls back to for
    any byte it does not know, and the builder already emits one character for
    it elsewhere in the same map.  Describing it here would write two entries for
    one code, and a CMap keeps only the first.
    """
    if code == 0:
        return None
    if 32 <= code < 127:
        return chr(code)
    return codes.get(code)


def differences(face):
    """A /Differences array naming every glyph in the built program.

    The names come from the program itself, so an /Encoding that resolves them
    reaches exactly the glyph that sits at the byte code's index.
    """
    from fontTools.ttLib import TTFont as _TT

    path = os.path.join(HERE, "fonts", FONT_FILES[face])
    order = _TT(path).getGlyphOrder()
    names = [f"/{n}" for n in order[1:128]]
    return "[1 " + " ".join(names) + "]"


def stream_object(num, data, extra=b""):
    head = b"/Filter [ /FlateDecode ]\n/Length %d\n" % len(data) + extra
    return (b"%d 0 obj\n<<\n" % num) + head + b">>\nstream\n" + data + b"\nendstream\nendobj"


def font_meta(raw):
    """Read the font dictionaries out of the shipped file.

    The book's own dictionaries are the authority for the face name, the first
    code and the width of every code, so nothing has to be carried over from the
    machine that built it.
    """
    meta = {}
    for num, blob in split_objects(raw).items():
        d = dict_of(blob)
        m = re.search(r"/BaseFont /([A-Z]{6})\+([\w-]+)", d)
        if not m or "/Type /Font" not in d:
            continue
        w = re.search(r"/Widths \[(.*?)\]", d, re.S)
        if not w:
            continue
        meta[str(num)] = {
            "name": m.group(2),
            "prefix": m.group(1),
            "first": int(re.search(r"/FirstChar (\d+)", d).group(1)),
            "widths": [float(v) for v in w.group(1).split()],
        }
    return meta


def rebuild_font_dict(fdict, face, prefix, tounicode_ref, descriptor_ref):
    """A font dictionary that states its encoding outright.

    /Differences names every glyph, and because the built program numbers its
    glyphs by byte code, the glyph index a reader looks up is the code itself.
    """
    widths = re.search(r"/Widths \[.*?\]", fdict, re.S).group(0)
    widths = re.sub(r"^/Widths\s*", "", re.sub(r"\s+", " ", widths))
    name = re.search(r"/Name /([\w+.-]+)", fdict)
    return (
        "<</BaseFont /%s+%s\n"
        "/FirstChar 0\n"
        "/LastChar 127\n"
        "/Encoding << /Type /Encoding /Differences %s >>\n"
        "/FontDescriptor %d 0 R\n"
        "/Name /%s\n"
        "/Subtype /TrueType\n"
        "/ToUnicode %d 0 R\n"
        "/Type /Font\n"
        "/Widths %s >>"
    ) % (prefix, face, differences(face), descriptor_ref,
         name.group(1) if name else "F0", tounicode_ref, widths)


def main(pdf_in, pdf_out):
    raw = open(pdf_in, "rb").read()
    meta = font_meta(raw)
    objs = split_objects(raw)

    by_family = {}
    for xref, info in meta.items():
        by_family[info["name"]] = (int(xref), info)

    replaced = {}
    report = []
    for family, (xref, info) in sorted(by_family.items()):
        path = os.path.join(HERE, "fonts", FONT_FILES[family])
        fdict = dict_of(objs[xref])
        fd_num = int(re.search(r"/FontDescriptor (\d+) 0 R", fdict).group(1))
        fdesc = dict_of(objs[fd_num])
        ff_num = int(re.search(r"/FontFile2 (\d+) 0 R", fdesc).group(1))
        tu_num = int(re.search(r"/ToUnicode (\d+) 0 R", fdict).group(1))

        font = TTFont(path)
        upm, hmtx = font["head"].unitsPerEm, font["hmtx"]
        order = font.getGlyphOrder()
        codes = CODES.get(family, {})
        first, widths = info["first"], info["widths"]
        # slots the builder left empty that the book still has text for
        codes = dict(codes)
        codes.update(EMPTY_SLOTS.get(family, {}))

        problems = []
        for code, ch in [(c, chr(c)) for c in range(32, 127)] + list(codes.items()):
            if not (0 <= code - first < len(widths)):
                continue
            if code >= len(order):
                problems.append((code, ch, "no slot"))
                continue
            g = order[code]
            w = hmtx.metrics[g][0] * 1000.0 / upm if g in hmtx.metrics else 0.0
            # a program scaled to a 1000-unit em can only hold whole units, so
            # anything inside one unit reproduces the book's spacing
            if abs(w - widths[code - first]) > 1.0:
                problems.append((code, ch, round(w, 1), round(widths[code - first], 1)))
        report.append((family, ff_num, tu_num, problems))

        tt = open(path, "rb").read()
        replaced[ff_num] = stream_object(ff_num, zlib.compress(tt, 9), b"/Length1 %d\n" % len(tt))
        replaced[tu_num] = stream_object(tu_num, zlib.compress(make_tounicode(codes), 9))
        newdict = rebuild_font_dict(fdict, family, info["prefix"], tu_num, fd_num)
        replaced[xref] = (b"%d 0 obj\n" % xref) + newdict.encode("latin-1") + b"\nendobj"

        # the descriptor still needs to agree with the rebuilt program
        fixed = re.sub(r"/FontFile2 \d+ 0 R", "/FontFile2 %d 0 R" % ff_num, fdesc)
        fixed = re.sub(r"/FontName /[^\s/]+", "/FontName /%s+%s" % (info["prefix"], family), fixed)
        replaced[fd_num] = (b"%d 0 obj\n" % fd_num) + fixed.encode("latin-1") + b"\nendobj"

    size = max(objs) + 1
    out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = {}
    for num in range(1, size):
        if num not in objs:
            continue
        blob = replaced.get(num, objs[num])
        if not blob.endswith(b"\n"):
            blob = blob + b"\n"
        offsets[num] = len(out)
        out += blob

    xref_at = len(out)
    out += b"xref\n0 %d\n" % size
    out += b"0000000000 65535 f \n"
    for num in range(1, size):
        if num in offsets:
            out += b"%010d 00000 n \n" % offsets[num]
        else:
            out += b"0000000000 65535 f \n"

    trailer = re.search(rb"trailer\s*<<(.*?)>>\s*startxref", raw, re.S).group(1)
    root = re.search(rb"/Root (\d+) 0 R", trailer).group(1)
    info_num = re.search(rb"/Info (\d+) 0 R", trailer)
    ids = re.search(rb"/ID\s*\[\s*<([0-9a-fA-F]+)>\s*<([0-9a-fA-F]+)>\s*\]", trailer)
    out += b"trailer\n<<\n/Size %d\n/Root %s 0 R\n" % (size, root)
    if info_num:
        out += b"/Info %s 0 R\n" % info_num.group(1)
    if ids:
        out += b"/ID [<%s><%s>]\n" % (ids.group(1), ids.group(2))
    out += b">>\nstartxref\n%d\n%%%%EOF\n" % xref_at

    open(pdf_out, "wb").write(bytes(out))

    for family, ff, tu, problems in report:
        flag = "OK " if not problems else "BAD"
        print(f"{flag} {family:26s} fontfile={ff:4d} tounicode={tu:4d} problems={problems[:3]}")
    print(f"wrote {pdf_out}  {len(out):,} bytes  ({size - 1} objects)")


if __name__ == "__main__":
    main(*sys.argv[1:3])
