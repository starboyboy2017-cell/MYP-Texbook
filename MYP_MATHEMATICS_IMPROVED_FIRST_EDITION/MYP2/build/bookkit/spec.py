"""Design specification for MYP Mathematics 2 - Improved First Edition.

Every value in this module was measured from the original first-edition PDF
(MYP-Mathematics-2-Student-Coursebook.pdf) rather than invented, so that the
improved edition keeps the original visual identity:

  page            A4 595 x 842 pt, single reading column of 425 pt, 85 pt margins
  field           navy  #101F2D  (cover, part dividers, chapter plates)
  bar             #15263A       (worked-example headers, table headers)
  body ink        #15263A
  plate type      cream #E9DFD0
  copper          #C1764C       (cover rules, plate numerals, part numerals)
  terracotta      #A64B27       (folios, kickers, section numbers, criterion strips)
  sage            #42604F       (definition labels, practice rules)
  slate           #33566C       (data accents, tags)
  sand            #F8F0DC       (definition panel fill)
  blush           #F8EDE5       (key idea and common-error panel fill)
  mist            #EDF3EC       (ATL panel fill, table heads)
  hairlines       #D8D0C2 / #E7E1D5

Improvements are refinements only: one display face and one text face used
consistently, a shared 14.2 pt baseline grid, mirrored (outer-edge) folios and
running heads, a fixed vertical rhythm on every plate, a real caption and
figure-numbering system, and - the largest change - actual embedded
photography and drawn diagrams where the original had none.
"""
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4

# ---------------------------------------------------------------- page geometry
PAGE_W, PAGE_H = A4                      # 595.276 x 841.890 pt

MARGIN_OUTER = 85.0
MARGIN_INNER = 85.0
MARGIN_TOP = 76.0
MARGIN_BOTTOM = 96.0

HEAD_TEXT_Y = PAGE_H - 41.2              # running-head baseline (as original)
FOLIO_Y = PAGE_H - 799.3                 # folio baseline (as original)

TEXT_W = PAGE_W - MARGIN_OUTER - MARGIN_INNER          # 425.28
COL_W = TEXT_W
TEXT_H = PAGE_H - MARGIN_TOP - MARGIN_BOTTOM           # 669.89

GUTTER = 0.0
MAIN_W = TEXT_W
MARGIN_W = 0.0

BASELINE = 14.2

# ----------------------------------------------------------------------- colour
NAVY        = HexColor("#101F2D")
NAVY_DEEP   = HexColor("#0B1721")
NAVY_MID    = HexColor("#1B3047")
BAR         = HexColor("#15263A")
GREEN       = NAVY                       # alias: the "field" colour
GREEN_DEEP  = NAVY_DEEP
GREEN_MID   = NAVY_MID
CREAM       = HexColor("#E9DFD0")
CREAM_SOFT  = HexColor("#FDFAF2")
PAPER       = HexColor("#FFFFFF")
INK         = HexColor("#15263A")
INK_SOFT    = HexColor("#3B4A5A")
INK_MUTE    = HexColor("#66717A")
INK_LABEL   = HexColor("#4A5B6B")
RULE        = HexColor("#D8D0C2")
RULE_SOFT   = HexColor("#E7E1D5")
SAND        = HexColor("#F8F0DC")
SAND_EDGE   = HexColor("#E0D0AC")
BLUSH       = HexColor("#F8EDE5")
BLUSH_EDGE  = HexColor("#E5C4B4")
MIST        = HexColor("#EDF3EC")
MIST_EDGE   = HexColor("#C8D6CC")
GOLD        = HexColor("#C1764C")
GOLD_DEEP   = HexColor("#7C5A17")
GOLD_PALE   = HexColor("#D8B58C")
TERRACOTTA  = HexColor("#A64B27")
RUST        = HexColor("#8E3B20")
SAGE        = HexColor("#42604F")
SLATE       = HexColor("#33566C")
SLATE_PALE  = HexColor("#E8EEF3")
STONE       = HexColor("#F5F2EA")

# ------------------------------------------------------------------- type scale
F_DISPLAY = "Playfair"
F_TEXT    = "SourceSerif"
F_SANS    = "Inter"
F_SYM     = "Sym"

SZ_COVER_TITLE = 62
SZ_PART_TITLE  = 44
SZ_PART_NUM    = 144
SZ_CH_TITLE    = 34
SZ_CH_KICKER   = 7.0
SZ_FM_TITLE    = 28
SZ_H2          = 21.0     # section title (measured 21 pt in the original)
SZ_H3          = 11.4
SZ_H4          = 9.3
SZ_LEAD        = 10.6     # measured 10.6 pt
SZ_BODY        = 9.7      # measured 9.7 pt
SZ_SMALL       = 8.4
SZ_ITEM        = 9.4
SZ_CAPTION     = 7.0
SZ_LABEL       = 6.0
SZ_TABLE       = 8.4

LD_BODY  = 14.2           # measured line pitch
LD_LEAD  = 15.8
LD_ITEM  = 13.7
LD_SMALL = 12.4
LD_CAP   = 9.8
LD_TABLE = 11.6

TRACK_LABEL = 1.55

# ------------------------------------------------------------- panel geometry
PANEL_PAD_X = 12.0
PANEL_PAD_Y = 10.0
PANEL_RULE = 2.6
PANEL_GAP  = 10.0

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
