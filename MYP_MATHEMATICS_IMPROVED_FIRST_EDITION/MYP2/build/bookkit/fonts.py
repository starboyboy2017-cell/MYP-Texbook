"""Font registration.

Playfair Display  - display / headings (the original's cover and heading face)
Source Serif 4    - running text and mathematics
Inter             - letterspaced labels, kickers, captions, tables
DejaVuSans subset - fallback for the few mathematical symbols the display and
                    text faces do not carry (angle, set and congruence signs).

All three families are licensed under the SIL Open Font License 1.1; the
licence texts are recorded in image_references/ and reports/.
"""
import os

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RLTTFont

FONT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "fonts")

_REGISTERED = False

FACES = {
    # display
    "Playfair": "pf-400-60.ttf",
    "Playfair-Med": "pf-500-60.ttf",
    "Playfair-Semi": "pf-600-60.ttf",
    "Playfair-Bold": "pf-700-60.ttf",
    "PlayfairItalic": "pfi-400-60.ttf",
    "PlayfairItalic-Med": "pfi-500-60.ttf",
    "PlayfairItalic-Bold": "pfi-400-60.ttf",
    "Playfair-Display": "pf-400-96.ttf",
    "Playfair-DisplayMed": "pf-500-96.ttf",
    # text
    "SourceSerif": "ss-400-17.ttf",
    "SourceSerif-Med": "ss-500-17.ttf",
    "SourceSerif-Semi": "ss-600-17.ttf",
    "SourceSerif-Bold": "ss-700-17.ttf",
    "SourceSerifItalic": "ssi-400-17.ttf",
    "SourceSerifItalic-Med": "ssi-400-17.ttf",
    "SourceSerifItalic-Semi": "ssi-600-17.ttf",
    "SourceSerifItalic-Bold": "ssi-700-17.ttf",
    # sans
    "Inter": "in-400-14.ttf",
    "Inter-Med": "in-500-14.ttf",
    "Inter-Semi": "in-600-14.ttf",
    "Inter-Bold": "in-700-14.ttf",
    # symbol fallback
    "Sym": "DejaVuSym.ttf",
}


def _instanced(name, fn):
    """Return a path to this face with a unique PostScript name.

    The subset files in fonts/ were instanced from variable fonts, so every
    weight still carries the family's original PostScript name. reportlab keys
    embedded fonts by that name, which silently collapses bold, semibold and
    medium onto the regular face. Rewriting the name table per face keeps the
    weights distinct in the PDF.
    """
    src = os.path.join(FONT_DIR, fn)
    import tempfile
    out_dir = os.path.join(tempfile.gettempdir(), "myp2_fonts")
    out = os.path.join(out_dir, fn)
    stamp = os.path.join(out_dir, "." + fn + ".stamp")
    key = f"{name}|{os.path.getmtime(src)}|{os.path.getsize(src)}"
    try:
        if open(stamp).read().strip() == key:
            return out
    except OSError:
        pass
    try:
        from fontTools.ttLib import TTFont as FTFont
    except ImportError:
        return src
    os.makedirs(out_dir, exist_ok=True)
    f = FTFont(src)
    family = name.replace("-", " ")
    ps = name.replace("-", "")
    names = {1: family, 4: family, 6: ps, 16: family, 17: name}
    nt = f["name"]
    for rec in list(nt.names):
        if rec.nameID in names:
            nt.setName(names[rec.nameID], rec.nameID, rec.platformID,
                       rec.platEncID, rec.langID)
    f.save(out)
    with open(stamp, "w") as fh:
        fh.write(key)
    return out


def register():
    global _REGISTERED
    if _REGISTERED:
        return
    for name, fn in FACES.items():
        pdfmetrics.registerFont(RLTTFont(name, _instanced(name, fn)))

    from reportlab.lib.fonts import addMapping
    addMapping("Playfair", 0, 0, "Playfair")
    addMapping("Playfair", 0, 1, "PlayfairItalic")
    addMapping("Playfair", 1, 0, "Playfair-Semi")
    addMapping("Playfair", 1, 1, "PlayfairItalic-Bold")
    addMapping("SourceSerif", 0, 0, "SourceSerif")
    addMapping("SourceSerif", 0, 1, "SourceSerifItalic")
    addMapping("SourceSerif", 1, 0, "SourceSerif-Semi")
    addMapping("SourceSerif", 1, 1, "SourceSerifItalic-Bold")
    addMapping("Inter", 0, 0, "Inter")
    addMapping("Inter", 0, 1, "Inter")
    addMapping("Inter", 1, 0, "Inter-Semi")
    addMapping("Inter", 1, 1, "Inter-Semi")

    pdfmetrics.registerFontFamily("SourceSerif", normal="SourceSerif", bold="SourceSerif-Semi",
                                  italic="SourceSerifItalic",
                                  boldItalic="SourceSerifItalic-Bold")
    pdfmetrics.registerFontFamily("Playfair", normal="Playfair", bold="Playfair-Semi",
                                  italic="PlayfairItalic", boldItalic="PlayfairItalic-Bold")
    pdfmetrics.registerFontFamily("Inter", normal="Inter", bold="Inter-Semi",
                                  italic="Inter", boldItalic="Inter-Semi")
    _REGISTERED = True
