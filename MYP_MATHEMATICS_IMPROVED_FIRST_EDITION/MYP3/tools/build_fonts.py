"""Build clean font programs for the ten faces used by the MYP3 book.

The shipped file's ten typefaces are unreadable: their programs were destroyed
by a text round-trip, so no reader can rasterise them and nobody can tell from
the file what they were.  Their identity was recovered from the PDF's own
/Widths arrays, which survive intact: each face below reproduces all 128 of its
advance widths to 1/1000 em.

Each face is instantiated (for Playfair, at the width and optical size the book
used), trimmed to the characters the book prints, and then laid out so that

    glyph id == character code

for every code in the book's own code map.  That last step is what makes the
repaired file work everywhere: a reader that resolves a byte through the glyph
index, and a reader that resolves it through the embedded cmap, both find the
same glyph, and /ToUnicode then maps it back to real Unicode for search and
copy-paste.

    python3 tools/fetch_fonts.py && python3 tools/build_fonts.py
"""
import os
import sys

from fontTools import subset
from fontTools.agl import UV2AGL
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, "tools"))
from codemap import CODES  # noqa: E402

SRC = os.environ.get("FONTSRC", "/tmp/fx")
OUT = os.path.join(HERE, "fonts")

# shipped family name -> (source file, output name, style name, variable axes)
FACES = {
    "Inter-Regular": ("v/inter-400.ttf", "myp3-inter-regular.ttf", "Regular", None),
    "Inter-Medium": ("v/inter-500.ttf", "myp3-inter-medium.ttf", "Medium", None),
    "Inter-SemiBold": ("v/inter-600.ttf", "myp3-inter-semibold.ttf", "SemiBold", None),
    "STIXTwoText-Regular": ("stix/STIXTwoText-Regular.ttf", "myp3-stix-text-regular.ttf", "Regular", None),
    "STIXTwoText-Italic": ("stix/STIXTwoText-Italic.ttf", "myp3-stix-text-italic.ttf", "Italic", None),
    "STIXTwoText-SemiBold": ("v/stix-two-text-600.ttf", "myp3-stix-text-semibold.ttf", "SemiBold", None),
    "STIXTwoMath-Regular": ("stix/STIXTwoMath.ttf", "myp3-stix-math-regular.ttf", "Regular", None),
    "PlayfairDisplay-Regular": ("pf/PlayfairRomanVF.ttf", "myp3-playfair-regular.ttf", "Regular",
                                {"wdth": 113, "opsz": 14, "wght": 400}),
    "PlayfairDisplay-SemiBold": ("pf/PlayfairRomanVF.ttf", "myp3-playfair-semibold.ttf", "SemiBold",
                                 {"wdth": 113, "opsz": 14, "wght": 600}),
    "PlayfairDisplay-Italic": ("pf/PlayfairItalicVF.ttf", "myp3-playfair-italic.ttf", "Italic",
                               {"wdth": 113, "opsz": 14, "wght": 400}),
}

EXTRA = ("\u00b7\u00a9\u2013\u2014\u00d7\u00f7\u2192\u2026\u00b0\u03be\u2248\u03c0\u00b1"
         "\u2264\u2265\u2260\u221e\u221a\u2211\u222b\u03a9\u0394\u03b8\u03b1\u03b2\u03b3"
         "\u03bc\u03c3\u2202\u2208\u2209\u222a\u2229\u2205\u2261\u2245\u2220\u22a5\u2225"
         "\u2234\u21d2\u21d4\u223c\u25b3\u2153\u2154\u00bd\u00b2\u00b3\u2074\u207f"
         "\u2081\u2082\u0305\u2044\u2115\u211a\u211d\u2124\u03a3")


def rename(font, family, style):
    name = font["name"]
    full = f"{family} {style}"
    ps = f"{family.replace(' ', '')}-{style}"
    recs = {}
    for rec in list(name.names):
        if rec.nameID in (1, 16):
            recs[(rec.nameID, rec.platformID, rec.platEncID, rec.langID)] = family
        elif rec.nameID in (2, 17):
            recs[(rec.nameID, rec.platformID, rec.platEncID, rec.langID)] = style
        elif rec.nameID == 4:
            recs[(rec.nameID, rec.platformID, rec.platEncID, rec.langID)] = full
        elif rec.nameID == 6:
            recs[(rec.nameID, rec.platformID, rec.platEncID, rec.langID)] = ps
    for (nid, plat, enc, lang), value in recs.items():
        name.setName(value, nid, plat, enc, lang)


def wanted_chars(family):
    chars = set(chr(c) for c in range(32, 127))
    chars |= set(EXTRA)
    chars |= set(CODES.get(family, {}).values())
    chars.discard("\n")
    return chars


def trim(font, chars):
    opts = subset.Options()
    opts.layout_features = []
    opts.drop_tables += ["GSUB", "GPOS", "GDEF", "BASE", "MATH", "JSTF", "morx", "mort"]
    opts.name_IDs = ["*"]
    opts.name_legacy = True
    opts.recalc_bounds = True
    opts.glyph_names = True
    opts.notdef_outline = True
    opts.passthrough_unintegrated = False
    sub = subset.Subsetter(options=opts)
    sub.populate(unicodes=[ord(c) for c in chars])
    sub.subset(font)
    return font


def flat_glyph(glyphset, name):
    """A standalone glyph for `name`, with every component drawn out."""
    rec = DecomposingRecordingPen(glyphset)
    glyphset[name].draw(rec)
    pen = TTGlyphPen(None)
    rec.replay(pen)
    return pen.glyph()


def decompose_composites(font):
    """Flatten accented and precomposed glyphs so slots can be duplicated.

    A composite points at another glyph by name; once the layout is renumbered
    those references would dangle, so every composite is drawn out as contours
    before the glyph order changes.
    """
    glyf = font["glyf"]
    order = font.getGlyphOrder()
    glyphset = font.getGlyphSet()
    flat = 0
    for name in order:
        if glyf[name].isComposite():
            glyf[name] = flat_glyph(glyphset, name)
            flat += 1
    return flat


def lay_out_codes(font, family):
    """Give every code in the book's map its own glyph slot, numbered by code.

    The book is drawn with single-byte codes.  A reader resolves a byte either
    through the embedded cmap or, for a subset TrueType program, through the
    glyph index; making the two agree is the only description that works in
    every reader.  Codes that share a character get a copy of the outline,
    because one glyph cannot sit at two indexes.
    """
    codes = CODES.get(family, {})
    cmap = font.getBestCmap()
    glyf = font["glyf"]
    hmtx = font["hmtx"]
    glyphset = font.getGlyphSet()
    old = font.getGlyphOrder()
    n = max(max(codes) + 1, 128) if codes else 128

    def slot_name(code, want):
        """A name PostScript can carry; printable codes use standard names."""
        if code == 0:
            return ".notdef"
        if 32 <= code < 127 and (want is None or want == chr(code)):
            return UV2AGL.get(code) or f"uni{code:04X}"
        if want is None:
            return f"pad{code}"
        return f"uni{ord(want):04X}c{code}"

    names = [slot_name(c, chr(c) if 32 <= c < 127 else codes.get(c)) for c in range(n)]
    glyphs = {names[0]: flat_glyph(glyphset, old[0])}
    metrics = {names[0]: hmtx.metrics[old[0]]}
    new_cmap = {}

    for code in range(1, n):
        want = chr(code) if 32 <= code < 127 else codes.get(code)
        src = cmap.get(ord(want)) if want else None
        if src is None:
            glyphs[names[code]] = TTGlyphPen(None).glyph()
            metrics[names[code]] = (0, 0)
        else:
            glyphs[names[code]] = flat_glyph(glyphset, src)
            metrics[names[code]] = hmtx.metrics[src]
        if want:
            new_cmap[ord(want)] = names[code]

    glyf.glyphs = glyphs
    glyf.glyphOrder = list(names)
    font.setGlyphOrder(list(names))
    hmtx.metrics = {nm: metrics[nm] for nm in names}
    font["maxp"].numGlyphs = n

    # one cmap subtable, keyed by the characters the book prints
    for table_ in font["cmap"].tables:
        if table_.isUnicode():
            table_.cmap = dict(new_cmap)
            table_.platEncID = 3
            table_.format = 4
            break
    font["cmap"].tables = [t for t in font["cmap"].tables if t.isUnicode()][:1]
    return font


# Code 0 is the slot a reader falls back to when a byte has no glyph.  The book
# draws a character there in 20 places: a comparison sign in the absolute-value
# rows and the matchstick labels, and "not equal" in the correlation labels.
# The slot keeps the width the book gives it, so nothing moves on the page.
EMPTY_SLOT_FILL = {
    "STIXTwoText-Regular": {
        0: (0x003C, "STIXTwoMath.ttf", 0x003C),   # "<", in the p82 labels
    },
    "STIXTwoText-Italic": {
        0: (0x003C, "STIXTwoMath.ttf", 0x003C),   # "<"
    },
    "PlayfairDisplay-SemiBold": {
        0: (0x2260, "STIXTwoMath.ttf", 0x2260),   # "not equal", correlation labels
    },
}


def fill_empty_slots(font, family, math_font):
    """Draw a real character in slot 0 without changing its advance.

    The slot is as wide as the book says (1000/1000 em in the text faces), so
    the glyph is scaled to fill it exactly; a reader that draws the outline and
    a reader that uses the advance therefore agree on where the next character
    starts.
    """
    fill = EMPTY_SLOT_FILL.get(family)
    if not fill:
        return 0
    glyf, hmtx = font["glyf"], font["hmtx"]
    src_cmap = math_font.getBestCmap()
    src_glyf = math_font["glyf"]
    src_set = math_font.getGlyphSet()
    done = 0
    for code, (_char, _src, src_code) in fill.items():
        name = font.getGlyphOrder()[code]
        src = src_cmap.get(src_code)
        if src is None:
            continue
        src_glyph = src_glyf[src]
        glyph = flat_glyph(src_set, src)
        advance = hmtx.metrics[name][0]
        span = src_glyph.xMax - src_glyph.xMin
        # scale the outline to the slot, then centre it in the advance so the
        # mark sits where the book put it
        k = float(advance) * 0.9 / span if span and advance else 1.0
        dx = int(round((advance - (src_glyph.xMax - src_glyph.xMin) * k) / 2.0 - src_glyph.xMin * k))
        coords = glyph.coordinates
        for i, (x, y) in enumerate(coords):
            coords[i] = (int(round(x * k)) + dx, y)
        glyph.recalcBounds(glyf)
        glyf[name] = glyph
        done += 1
    return done


def set_unique_id(font, family):
    """Give each build its own /UniqueID and version string.

    Readers cache an embedded program under its PostScript name and version, so
    two builds that differ only in a glyph outline can be confused for each
    other.  The content hash makes every build distinct.
    """
    import hashlib

    digest = hashlib.sha1()
    glyf, hmtx = font["glyf"], font["hmtx"]
    for name in font.getGlyphOrder():
        g = glyf[name]
        digest.update(repr((g.numberOfContours,
                            getattr(g, "coordinates", None),
                            hmtx.metrics.get(name))).encode())
    stamp = digest.hexdigest()[:8]
    name = font["name"]
    name.setName(f"Version 1.00 ({stamp})", 5, 3, 1, 0x409)
    name.setName(f"{family}-{stamp}", 3, 3, 1, 0x409)
    font["head"].fontRevision = float(int(stamp[:4], 16)) / 65535.0
    return stamp


def set_names_in_post(font):
    """Rebuild `post` as version 2 from the current glyph order.

    Without names, a /Differences array cannot be resolved and some readers fall
    back to a default face; with them, every byte code in the book resolves.
    """
    post = font["post"]
    post.formatType = 2.0
    post.extraNames = []
    post.glyphOrder = list(font.getGlyphOrder())
    post.mapping = {}
    return font


def build(family, path, out, style, axes):
    print(f"  {family}")
    font = TTFont(os.path.join(SRC, path))
    if axes:
        font = instantiateVariableFont(font, axes, inplace=False)
    trim(font, wanted_chars(family))
    for dead in ("fvar", "avar", "gvar", "HVAR", "MVAR", "STAT", "cvar"):
        if dead in font:
            del font[dead]
    # /Widths in the book is in 1/1000 em, so every program is rescaled to a
    # 1000-unit em; the outlines scale with it and nothing else changes
    if font["head"].unitsPerEm != 1000:
        from fontTools.ttLib.scaleUpem import scale_upem
        scale_upem(font, 1000)
    flat = decompose_composites(font)
    lay_out_codes(font, family)
    filled = fill_empty_slots(font, family, TTFont(os.path.join(SRC, "stix/STIXTwoMath.ttf")))
    print(f"    flattened {flat} composites")
    rename(font, family.split("-")[0], style)
    if filled:
        print(f"    filled {filled} empty slot(s)")
    set_unique_id(font, family)
    set_names_in_post(font)
    font["head"].unitsPerEm = font["head"].unitsPerEm
    font.save(os.path.join(OUT, out))
    print(f"    -> {out}")


def main():
    os.makedirs(OUT, exist_ok=True)
    for family, (path, out, style, axes) in FACES.items():
        build(family, path, out, style, axes)
    print(f"wrote {len(FACES)} faces to {OUT}")


if __name__ == "__main__":
    main()
