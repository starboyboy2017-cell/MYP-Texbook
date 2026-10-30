"""Inline markup.

Authoring syntax (kept deliberately small so that prose stays readable in the
source files):

    **bold**            <b>
    *italic*            <i>
    ^{2}                superscript
    _{n}                subscript
    `x`                 inline mathematics (Source Serif italic)
    --                  en dash          ---  em dash
    ...                 ellipsis

Everything else passes through as text.  Characters that the text faces do not
carry (angle, congruence, set membership) are automatically wrapped in the
symbol fallback font, so authors never have to think about it.
"""
import re

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

from . import spec

# characters absent from Source Serif 4 / Inter / Playfair Display
_FALLBACK = set("\u2220\u2245\u2208\u2209\u2282\u2286\u222a\u2229\u2205\u2234\u2235"
                "\u2192\u2190\u2194\u21a6\u2211\u221e\u221a\u2260\u2264\u2265\u2248"
                "\u2212\u00d7\u00f7\u00b1\u03c0\u03b8\u0394\u03a9\u221d\u22a5\u2225"
                "\u25a1\u25a2\u25cf\u25cb\u25b2\u25bc\u2261\u21d4\u21d2")
# a few of these *are* present in some faces; harmless either way, but the
# common ones we always render with the text face for better colour:
_KEEP = set("\u2212\u00d7\u00f7\u00b1\u03c0\u03b8\u0394\u03a9\u2248\u2260\u2264\u2265\u221e\u2211")
_FALLBACK = _FALLBACK - _KEEP


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _sym(m):
    ch = m.group(0)
    return f'<font name="Sym">{ch}</font>'


def inline(text, math=False):
    """Convert authoring markup to reportlab intra-paragraph markup."""
    t = esc(text)
    # characters unsupported by the text faces -> symbol fallback
    t = re.sub("[" + "".join(sorted(_FALLBACK)) + "]", _sym, t)
    t = t.replace("---", "\u2014").replace("--", "\u2013")
    t = re.sub(r"\.\.\.", "\u2026", t)

    # superscript / subscript
    t = re.sub(r"\^\{([^{}]*)\}", lambda m: f"<super rise=3.1 size=6.1>{m.group(1)}</super>", t)
    t = re.sub(r"_\{([^{}]*)\}", lambda m: f"<sub rise=-1.6 size=6.1>{m.group(1)}</sub>", t)

    # inline maths in italic text face
    t = re.sub(r"`([^`]*)`", lambda m: f'<font name="SourceSerifItalic">{m.group(1)}</font>', t)

    # emphasis
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", t)
    return t


def plain(text):
    """Strip authoring markup, for DOCX and for text-only measurements."""
    t = text.replace("^{", "\u2c7c").replace("}", "")
    t = re.sub(r"\^\{([^{}]*)\}", r"\1", text)
    t = re.sub(r"_\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"\*([^*]+)\*", r"\1", t)
    t = t.replace("---", "\u2014").replace("--", "\u2013").replace("...", "\u2026")
    return t


def style(name="body", **kw):
    base = dict(fontName="SourceSerif", fontSize=spec.SZ_BODY, leading=spec.LD_BODY,
                textColor=spec.INK, alignment=TA_JUSTIFY, spaceBefore=0, spaceAfter=0,
                hyphenationLang="en_GB", embeddedHyphenation=1, uriWasteReduce=0.3,
                splitLongWords=1)
    presets = {
        "body":   {},
        "body_l": dict(alignment=TA_LEFT),
        "lead":   dict(fontSize=spec.SZ_LEAD, leading=spec.LD_LEAD, textColor=spec.INK_SOFT,
                       alignment=TA_LEFT),
        "small":  dict(fontSize=spec.SZ_SMALL, leading=spec.LD_SMALL),
        "item":   dict(fontSize=spec.SZ_ITEM, leading=spec.LD_ITEM, alignment=TA_LEFT),
        "panel":  dict(fontSize=spec.SZ_SMALL + 0.35, leading=spec.LD_SMALL + 1.2,
                       alignment=TA_LEFT),
        "caption": dict(fontName="Inter", fontSize=spec.SZ_CAPTION, leading=spec.LD_CAP,
                        textColor=spec.INK_MUTE, alignment=TA_LEFT),
        "label":  dict(fontName="Inter-Semi", fontSize=spec.SZ_LABEL,
                       leading=spec.SZ_LABEL * 1.6, textColor=spec.GOLD_DEEP,
                       alignment=TA_LEFT),
        "table":  dict(fontSize=spec.SZ_TABLE, leading=spec.LD_TABLE, alignment=TA_LEFT),
        "table_h": dict(fontName="Inter-Semi", fontSize=spec.SZ_TABLE - 0.7,
                        leading=spec.LD_TABLE, textColor=spec.GREEN, alignment=TA_LEFT),
        "quote":  dict(fontName="SourceSerifItalic-Med", fontSize=11, leading=15.6,
                       textColor=spec.GREEN, alignment=TA_LEFT),
    }
    base.update(presets.get(name, {}))
    base.update(kw)
    return ParagraphStyle(name + str(hash(tuple(sorted(kw.items()))))[:6], **base)


def tracked(text, tracking=spec.TRACK_LABEL):
    """Manual letterspacing (reportlab has no tracking attribute)."""
    return ("\u200a" * max(1, int(round(tracking / 1.6)))).join(text)
