# Design reference — measured from the original first edition

These notes record what was measured from the original *MYP Mathematics 2 — Student Coursebook*
(260 pp), what was deliberately kept, and what was refined. The measurements were taken from
rendered original pages and from the PDF's own colour and font data, not guessed from screenshots.

## 1. What the original looks like, measured

**Colour.** Sampling the original pages gives the following working palette. Every value below is
the value used in `build/bookkit/spec.py` for this edition, so that the print output matches the
original rather than merely resembling it.

| Role | Hex | Where it appears |
|---|---|---|
| Cover and back cover | `#0F1F2D` | full-bleed boards |
| Chapter opener plate | `#15263A` | chapter divider pages |
| Body ink | `#15263A` | running text |
| Cream | `#E9DFD0` | quiet panels, part dividers |
| Copper | `#D8B58C` | rules on the cover, small ornaments |
| Terracotta | `#C1764C` | section numerals, kickers, accents |
| Sage grey | `#8FA69B` | secondary diagram lines |
| Kicker ink | `#A64B27` | CRITERION · related concept lines |
| Intro italic | `#263D52` | the italic lead under a section head |
| Caption grey | `#66717A` | figure and table captions |
| Panel labels | `#42604F` | DEFINITION / KEY IDEA / NOTE labels |
| Panels | `#F8EDE5`, `#EDF3EC`, `#F8F0DC`, `#FFFCF6`, `#F1F4F8` | blush, sage, sand, cream, mist |
| Hairlines | `#E7E1D5` | table rules, panel edges |
| Table rules | `#D8D0C2` / `#C9BFAF` | header rule, row rules |

**Type.** Body text on a typical original page is 9.7 pt on 13.5 pt leading; the opening paragraph
of a section (the italic lead) is 10.6 pt; section titles are 21 pt; the kicker above a section
head is 6.6 pt with +1.5 tracking; captions are 7.0 pt. Display headings are a Playfair-style
didone serif; text is a Source-Serif-style transitional; labels are a neutral grotesque with wide
tracking. This edition embeds Playfair Display, Source Serif 4 and Inter, all under the SIL OFL,
which reproduces the character of the original without reusing its files.

**Page architecture.** A4, 210 × 297 mm. Body measure 121 mm, generous outer margin, folio at the
outer foot in terracotta, running heads in 6.3 pt letterspaced caps. Chapter anatomy is fixed:
divider plate → planner (statement of inquiry, key and related concepts, global context, inquiry
questions, A–D table, ATL) → learning intentions and success criteria → sections `x.1 … x.n`, each
with a `CRITERION · related concept` kicker, an italic lead, a definition, worked examples numbered
`x.y.z`, practice tagged Support / Core / Extension, and a common-error panel → investigation cards
→ Criterion D task → summary, revision and reflection → mixed practice.

## 2. What was kept, deliberately and exactly

- **Cover identity.** The same dark navy board, the same three-line title arrangement, the same
  hairline rule below the subtitle, the same author line at the foot, and the same restrained
  geometric ornament. This is a **first edition**, so the cover says so.
- **Palette.** All the values in the table above.
- **Typography and hierarchy.** Display serif for chapter and section titles, transitional serif
  for text, grotesque for labels; italic lead paragraphs; letterspaced caps for kickers.
- **Red section numerals** and terracotta folios.
- **Criterion kickers** in the exact original form: `CRITERION A · I, II` followed by a bullet and
  the related concept.
- **Panels.** Five tinted panel types with a coloured left rule, used for exactly the purposes the
  original used them: DEFinition, KEY IDEA, NOTE, COMMON ERROR, ATL.
- **Cards.** The original's investigation and task boxes, with a boxed chip on the right
  (`INVESTIGATION`, `CRITERION D`) and a hairline under the card title.
- **Table styling.** Header rule above, thin row rules below, no vertical rules, zebra tint.
- **Chapter sequence and topic scope.** Unchanged: 4 parts, 11 chapters, the same sequence.

## 3. What was refined, and why

| Refinement | Reason | Effect on the page |
|---|---|---|
| Optical tracking removed from the last glyph of every tracked line | The original's letterspaced caps ended with a wide gap before the following rule | Kickers and running heads now align with the rules they sit on |
| Baseline grid tightened to 13.5 pt across all block types | Original panels and tables drifted off the text baseline by 1–3 pt | Text on facing pages now sits on the same lines |
| Panel padding regularised to 15 pt / 7 pt | Original panels varied between 9 and 18 pt of padding | Panels read as one family rather than one-offs |
| Figure captions split into a coloured number and a grey sentence | Original captions began with the number inside the sentence | Figures can now be referenced quickly while reading |
| Every figure redrawn as vector | Original figures were inconsistent in weight and some were low-resolution bitmaps | Print-sharp at any size, one line weight system |
| **22 photographs added** | The original edition carried no photographs at all | Each chapter now opens with a real-world image that does work in the argument, not decoration |
| Practice lists made splittable at a question boundary | Original practice blocks sometimes broke mid-question | No question is ever divided across a page |
| Answers section set as a two-level list with the practice reference as a heading | Original answers ran as one dense paragraph per section | Answers can be found without reading a block of prose |
| Contents set with three row heights (part, chapter, section) | Original contents used one row height, which flattened the hierarchy | Part and chapter levels now read at a glance |

## 4. What was *not* changed

- No new chapter, no removed chapter, no reordering.
- No change to the MYP framework vocabulary: key and related concepts, global contexts,
  statements of inquiry, factual/conceptual/debatable questions, ATL clusters and criteria
  A–D are the ones the original used for each chapter.
- No invented ISBN, publisher, barcode, date, price or IB endorsement. The book states that it is
  an independently produced course and names no school.
- The sentence frame *"In order for a student to …, students must …"* is used verbatim in every
  chapter's ATL statement, as in the original.

## 5. Page budget

| Part | Chapters | Pages in this edition |
|---|---|---|
| Front matter | — | 1–14 |
| Part I · Number and proportion | 1–4 | 15–85 |
| Part II · Algebra and pattern | 5–6 | 86–119 |
| Part III · Geometry and space | 7–9 | 120–184 |
| Part IV · Probability and data | 10–11 | 185–223 |
| Part V · Reference | answers, formulas, glossary, index, sources | 224–244 |
| Back cover | — | 245 |
