# Report 3 — Design preservation and refinement

**Deliverable:** *MYP Mathematics 2 — Student Coursebook, Improved First Edition*
**Reference:** original First Edition, measured page by page (see `design_reference/DESIGN_NOTES.md`)

This report answers one question: *does the improved edition still look like the original, and
where it does not, is the difference defensible?*

## 1. Method

1. The original PDF was opened in PyMuPDF and its colour and font data extracted (not sampled from
   screenshots, which shift colour).
2. Pages were rendered at 80–150 dpi and inspected for grid, margins, folio position, rule weights
   and panel padding.
3. The same measurements were taken from this edition's pages.
4. Every difference was either corrected to match the original, or recorded below with a reason.

## 2. Preservation — what is unchanged

| Element | Verdict | Evidence |
|---|---|---|
| Cover board colour `#0F1F2D`, back cover same | preserved | page 1 and page 245 |
| Cover title arrangement (three lines, rule, subtitle, author foot) | preserved | page 1 |
| Chapter opener plate `#15263A` with part label, chapter numeral, key/related concepts, global context, inquiry line | preserved | 11 plates, pp. 15, 36, 54, 71, 86, 103, 120, 143, 163, 185, 204 |
| Gold hairline rules under kickers and part heads | preserved | all section heads |
| Playfair-style display serif for chapter and section titles | preserved (Playfair Display, OFL) | embedded font list |
| Source-Serif-style text face | preserved (Source Serif 4, OFL) | embedded font list |
| Grotesque labels with wide tracking | preserved (Inter, OFL) | kickers, running heads, captions |
| Terracotta section numerals and folios | preserved | every body page |
| Cream / sand / blush / mist panels with a coloured left rule | preserved | 7 panel kinds, 153 panels + 28 cards |
| Criterion kicker form `CRITERION A · I, II · related concept` | preserved verbatim | every section |
| Investigation and Criterion D cards with a boxed chip at the right | preserved | 33 cards |
| Table style: header rule, thin row rules, no vertical rules, zebra tint | preserved | 64 tables |
| Chapter anatomy (divider → planner → intentions → sections → cards → summary → mixed practice) | preserved | all 11 chapters |

## 3. Refinement — what changed and why

### 3.1 Typographic fixes

| Change | Before | After | Reason |
|---|---|---|---|
| Tracking on the final glyph | letterspaced caps ended with a wide gap that pushed the last letter off the rule | tracking stops before the final glyph | the original's kickers visibly overhung their rules |
| Baseline grid | panel and table text drifted up to 3 pt off the text baseline | one 13.5 pt grid for every block | facing pages now agree line for line |
| Panel padding | 9–18 pt, varying by panel kind | 15 pt horizontal, 7 pt vertical, uniform | panels read as one family |
| Figure captions | number inside the sentence | coloured figure number, then grey sentence | figures can be located while reading |
| Running heads | 6.3 pt caps, sometimes colliding with the rule | same size, aligned to the measure | no collision on any page |

### 3.2 Structural fixes

| Change | Reason |
|---|---|
| Practice lists split only at a question boundary | the original sometimes divided a question across a page |
| Section heads kept with their first two lines | the original occasionally left a head alone at the foot of a page |
| Contents set with three row heights (part 19 pt, chapter 36 pt, section 16 pt) | the original's single row height flattened the hierarchy |
| Answers set as a two-level list with the practice reference as a heading | the original ran answers as one paragraph per section |

### 3.3 The substantive visual change: photographs

The original edition contains **no photographs at all** — every illustration is a diagram. This was
the single most serious visual weakness relative to a published coursebook, and it is the change
that most affects how the book reads.

This edition adds **22 photographs**, two per chapter, each doing work in the argument:

| Chapter | Photograph | The work it does |
|---|---|---|
| 1 | lemonade jugs | the opening problem *is* the picture: three jugs, same recipe |
| 1 | gridded facade | a repeated bay is a part-to-whole comparison you can see |
| 2 | architectural model | scale factor made physical |
| 2 | compass on a map | map scale, and what a model leaves out |
| 3 | water into a measuring jug | a rate you can watch |
| 3 | fuel pump | price per litre as a rate read off a display |
| 4 | thermometer in snow | the scale continues below zero |
| 4 | stone steps | equal risers as a number line |
| 5 | handwritten algebra | notation as a checkable record |
| 5 | two students solving | equivalence shown line by line |
| 6 | running-bond brick | each course is a translation of the last |
| 6 | repeating facade | one rule generates the elevation |
| 7 | truss bridge | triangulation as a rigidity argument |
| 7 | hexagonal paving | 3 × 120° = 360°, so the tiling closes |
| 8 | stacked cartons | one volume, repeated |
| 8 | cylindrical tank | capacity versus material |
| 9 | Ferris wheel | equal rotations about a hub |
| 9 | mosaic tiles | a pattern generated by two translations |
| 10 | two dice | thirty-six ordered pairs |
| 10 | tossed coins | HT ≠ TH |
| 11 | dashboard of charts | each chart answers one question |
| 11 | spreadsheet and charts | a summary is a choice |

Every photograph is captioned in the original's caption style, numbered in the same figure
sequence as the diagrams, and credited on the page. Cropping is centre-frame to one of two aspect
ratios so that a photograph behaves like a figure and cannot break the page rhythm.

### 3.4 Diagrams

All 45 numbered figures that are not photographs are **vector drawings generated from code**
(`build/diagrams2.py`, 52 functions). This means:

- one line-weight system across the whole book (0.4 pt hairlines, 0.8–1.1 pt outlines);
- one label style (6.0–7.4 pt Inter, terracotta for results, grey for construction lines);
- one caption/credit geometry, identical to the photographs;
- no bitmap artefacts, and no figure that cannot be re-proportioned.

Several diagrams were redrawn during review because they did not read correctly at print size:
the triangle-number staircases (originally a heavy parallelogram, now a true staircase), the
matchstick pattern (originally overlapping its own labels), the parallel-line transversal (angle
labels originally sat on the wrong side of the lines), the cylinder net (circles originally
overlapped the curved surface), the symmetry gallery (mirror lines originally crossed the wrong
shapes), and the sample-space grid (originally too small to read).

## 4. Consistency audit

| Check | Result |
|---|---|
| Every body page carries the running head and the folio in the same position | pass, 245 pages |
| No text crosses the 121 mm measure | pass, 0 overflows above y = 788 pt |
| No text crosses the outer margin | pass, 0 overflows beyond x = 512 pt |
| Every panel uses one of the five defined fills | pass |
| Every card uses a defined chip colour | pass |
| Figure numbers run continuously 1.1 … 11.x | pass |
| No page is blank | pass, 0 blank pages |
| Photographs and diagrams share one caption geometry | pass |

## 5. Where this edition still differs from the original, honestly

1. **Page count** is 245 rather than 260. The difference is the removal of the original's
   part-empty pages, not a loss of content.
2. **The typefaces are different files** (Playfair Display, Source Serif 4, Inter) with the same
   character as the original's faces. They are open-licence fonts that can legally be embedded and
   redistributed with the book; the original's exact faces could not be.
3. **Photographs are new** and have no counterpart in the original (see §3.3).
4. **The cover says "Improved First Edition"** rather than "First Edition", because the user's
   brief requires the edition statement to be accurate and this is not a second edition.
