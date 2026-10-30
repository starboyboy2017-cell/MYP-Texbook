# Design reference — the page system of the Improved First Edition

The source first edition was measured page by page (screen colours sampled from the
cover, part dividers, chapter openers, panels and folios; measures taken from the text
block, the head rule and the folio baseline). The values below are the ones this edition
uses; they keep the original's identity and correct its inconsistencies.

Everything is implemented in `build/bookkit/spec.py`; no value is hard-coded in a
chapter file.

## 1. Page geometry

| Item | Value |
|---|---|
| Trim | A4 — 595.28 × 841.89 pt (210 × 297 mm) |
| Outer margin | 56 pt |
| Inner margin | 48 pt (mirrored on verso) |
| Top margin | 66 pt |
| Bottom margin | 64 pt |
| Type area | 491.28 × 711.89 pt |
| Reading column | 318 pt |
| Gutter | 17 pt |
| Outer note / writing column | 156.28 pt |
| Baseline grid | 13.5 pt |
| Head rule | 44 pt below the top trim |
| Folio baseline | 38 pt above the bottom trim |

Left and right pages mirror, so the wide column always sits on the outside of the spread.
That is what makes the outer margin usable as a student's writing space.

## 2. Colour

| Name | Hex | Where it is used |
|---|---|---|
| Deep green | `#152F2C` | cover, part dividers, chapter openers, worked-example bars |
| Green deep | `#0E211F` | plate shadows |
| Green mid | `#22403B` | plate detail |
| Cream | `#F9F6EC` | cover type, panels |
| Cream soft | `#FDFBF4` | table cells, page panels |
| Paper | `#FFFFFF` | body pages |
| Ink | `#1B2523` | running text |
| Ink soft | `#3A4744` | margin notes |
| Ink mute | `#6C7A76` | captions |
| Rule | `#D9D2C4` | hairlines |
| Rule soft | `#E7E0D2` | table rules |
| Sand | `#F6EDDA` | definition panels |
| Sand edge | `#DCCFAE` | definition panel edge |
| Blush | `#F6EAE1` | common-error panels |
| Blush edge | `#E5C4B4` | common-error edge |
| Mist | `#EBF0EB` | ATL panels, table heads |
| Mist edge | `#C8D6CC` | ATL edge |
| Gold | `#A8823F` | hairlines, numerals |
| Gold deep | `#896423` | kickers, category labels |
| Gold pale | `#D6CDBB` | plate numerals |
| Terracotta | `#B14F31` | folios, inquiry bars, extension tags |
| Sage | `#3D6257` | key-idea panels, fluency tags |
| Slate | `#38556D` | data accents, reasoning tags |
| Slate pale | `#EAEFF4` | data panel fills |

Colour never carries meaning alone: each tag and panel also carries a text label.

## 3. Type scale

| Role | Face | Size / leading |
|---|---|---|
| Cover title | Playfair Display | 61 pt |
| Part title / numeral | Playfair Display | 40 / 132 pt |
| Chapter title | Playfair Display | 33 pt |
| Front-matter page title | Playfair Display | 27 pt |
| Section heading (H2) | Playfair Display | 20 pt |
| Sub-heading (H3) | Source Serif Semi | 11.2 / 15 pt |
| Run-in heading (H4) | Inter Semi | 9.3 pt |
| Lead paragraph | Source Serif | 12 / 17.6 pt |
| Body | Source Serif | 9.85 / 15.25 pt |
| Numbered item | Source Serif | 9.3 / 13.9 pt |
| Small / margin note | Source Serif | 8.4 / 12.4 pt |
| Table | Inter | 8.3 / 11.2 pt |
| Caption | Inter | 7.2 / 9.8 pt |
| Label / kicker | Inter Semi | 6.5 pt, tracking 1.75 |

Headings are set with hyphenation off; running text is justified with hyphenation on.

## 4. Panel system

Five panel types, each with a 2.6 pt left rule, 11 × 9.5 pt padding and a 9 pt gap:

| Panel | Fill | Rule | Carries |
|---|---|---|---|
| Definition | sand | gold deep | a precise statement, once per idea |
| Key idea | mist | sage | the principle a method rests on |
| Common error | blush | terracotta | a mistake in a student's voice, then the correction |
| ATL skill | mist | sage | an approaches-to-learning prompt in IB wording |
| Note | cream | gold | the teacher-facing note |

## 5. Exercise tags

Grading letters are set as small caps chips after each question:
`F` fluency (sage), `R` reasoning (slate), `P` problem solving (terracotta),
`E` extension (gold deep).

## 6. What changed from the source design, and why

| Source problem | This edition |
|---|---|
| heading face silently swapped part-way through the book | one display face throughout |
| body leading drifted between sections | one 13.5 pt baseline grid |
| margin used decoratively | margin is a working note column with a fixed measure |
| figures unnumbered and unreferenced | every figure and table numbered, captioned and referenced |
| folios inconsistent in position | folio fixed at 38 pt from the foot, outside edge |
| accent colours used loosely | one accent per meaning, always paired with a label |

Nothing in this list changes the visual identity: the green, the cream, the gold hairlines,
the Playfair display type and the two-column-with-margin architecture are all as measured
from the original.
