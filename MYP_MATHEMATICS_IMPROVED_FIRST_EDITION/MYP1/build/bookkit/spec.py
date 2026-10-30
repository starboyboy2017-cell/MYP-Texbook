"""Design specification for the MYP Mathematics 1 - Improved First Edition.

Every value in this module was derived from measurement of the original
first-edition PDF (MYP-Mathematics-1-Student-Coursebook.pdf) so that the
improved edition keeps the original visual identity:

    deep green   #152F2C   (cover, chapter openers, part dividers, worked-example bars)
    cream        #F9F6EC   (panels, cover type)
    sand         #F6EDDA   (definition panels)
    blush        #F6EAE1   (common-error panels)
    mist         #EBF0EB   (ATL panels)
    gold         #896423   (hairlines, numerals, kickers)
    terracotta   #B14F31   (folios, inquiry bars, accents)
    sage         #3D6257   (key-idea panels)
    slate        #38556D   (data / statistics accents)

Improvements are refinements only: a single baseline grid, one display face
used consistently (the original silently swapped heading faces at chapter 3),
mirrored margins, optical margin alignment, and a calmer accent discipline.
"""
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# ---------------------------------------------------------------- page geometry
PAGE_W, PAGE_H = A4                      # 595.276 x 841.890 pt

MARGIN_OUTER = 56.0
MARGIN_INNER = 48.0
MARGIN_TOP = 66.0
MARGIN_BOTTOM = 64.0

HEAD_RULE_Y = PAGE_H - 44.0              # running-head hairline
HEAD_TEXT_Y = PAGE_H - 40.0
FOLIO_Y = 38.0

GUTTER = 17.0

TEXT_W = PAGE_W - MARGIN_OUTER - MARGIN_INNER          # 491.28
MAIN_W = 318.0                                         # reading column
MARGIN_W = TEXT_W - MAIN_W - GUTTER                    # 156.28 notes column
COL_W = MAIN_W
TEXT_H = PAGE_H - MARGIN_TOP - MARGIN_BOTTOM

BASELINE = 13.5

# ----------------------------------------------------------------------- colour
GREEN      = HexColor("#152F2C")
GREEN_DEEP = HexColor("#0E211F")
GREEN_MID  = HexColor("#22403B")
CREAM      = HexColor("#F9F6EC")
CREAM_SOFT = HexColor("#FDFBF4")
PAPER      = HexColor("#FFFFFF")
INK        = HexColor("#1B2523")
INK_SOFT   = HexColor("#3A4744")
INK_MUTE   = HexColor("#6C7A76")
RULE       = HexColor("#D9D2C4")
RULE_SOFT  = HexColor("#E7E0D2")
SAND       = HexColor("#F6EDDA")
SAND_EDGE  = HexColor("#DCCFAE")
BLUSH      = HexColor("#F6EAE1")
BLUSH_EDGE = HexColor("#E5C4B4")
MIST       = HexColor("#EBF0EB")
MIST_EDGE  = HexColor("#C8D6CC")
GOLD       = HexColor("#A8823F")
GOLD_DEEP  = HexColor("#896423")
GOLD_PALE  = HexColor("#D6CDBB")
TERRACOTTA = HexColor("#B14F31")
SAGE       = HexColor("#3D6257")
SLATE      = HexColor("#38556D")
SLATE_PALE = HexColor("#EAEFF4")

# ------------------------------------------------------------------- type scale
F_DISPLAY = "Playfair"
F_TEXT    = "SourceSerif"
F_SANS    = "Inter"
F_SYM     = "Sym"

SZ_COVER_TITLE = 61
SZ_COVER_SUB   = 19
SZ_PART_TITLE  = 40
SZ_PART_NUM    = 132
SZ_CH_TITLE    = 33
SZ_CH_KICKER   = 7.6
SZ_FM_TITLE    = 27        # front-matter page titles
SZ_H2          = 20.0
SZ_H3          = 11.2
SZ_H4          = 9.3
SZ_LEAD        = 12.0
SZ_BODY        = 9.85
SZ_SMALL       = 8.4
SZ_ITEM        = 9.3
SZ_CAPTION     = 7.2
SZ_LABEL       = 6.5
SZ_TABLE       = 8.3

LD_BODY  = 15.25
LD_LEAD  = 17.6
LD_ITEM  = 13.9
LD_SMALL = 12.4
LD_CAP   = 9.8
LD_TABLE = 11.2

TRACK_LABEL = 1.75      # letterspacing for small caps labels (pt per char)

# ------------------------------------------------------------- panel geometry
PANEL_PAD_X = 11.0
PANEL_PAD_Y = 9.5
PANEL_RULE = 2.6        # left accent rule width
PANEL_GAP  = 9.0        # space above/below a panel

# --------------------------------------------------------- exercise tag chips
TAGS = {
    "F": ("FLUENCY",         SAGE),
    "R": ("REASONING",       SLATE),
    "P": ("PROBLEM SOLVING", TERRACOTTA),
    "E": ("EXTENSION",       GOLD_DEEP),
}

# --------------------------------------------------------------- MYP framework
CRITERIA = {
    "A": ("Knowing and understanding", SAGE),
    "B": ("Investigating patterns",    SLATE),
    "C": ("Communicating",             GOLD_DEEP),
    "D": ("Applying mathematics in real-life contexts", TERRACOTTA),
}
