# MYP Mathematics 2 — Improved First Edition

**Year 2 student coursebook.** Author: SADIKOU MOUKODDIM. 265 A4 pages.
Independent educational publication; not published by, sponsored by or affiliated with the
International Baccalaureate Organization.

This edition rebuilds the first edition of MYP Mathematics 2 from the original source book.
It is an **improved first edition**, not a second edition: the curriculum scope, chapter
sequence, learning objectives and level of difficulty are the first edition's. What was
rebuilt is the teaching apparatus, the artwork and the page design — every explanation,
worked example, investigation and exercise in this book was written or drawn for this
edition, and all original files are left untouched in the repository.

## Deliverable

| File | What it is |
|---|---|
| `final/MYP2_Mathematics_Improved_First_Edition.pdf` | The complete book: cover, front matter, eleven chapters in four parts, answers, formula bank, glossary, index, references, back cover. 265 pages, A4, print-ready. |
| `final/MYP2_Mathematics_Improved_First_Edition.docx` | The same book as an editable Word document: all text, 121 worked examples, 673 questions, 64 tables, 45 figures (re-rendered at 220 dpi) and 22 photographs. |

## Everything else in this folder

| Folder | Contents |
|---|---|
| `manuscript/` | Text extracts of the typeset pages: `chapter_01.md` … `chapter_11.md`, `front_matter.md`, `back_matter.md`, one page marker per printed page. ≈ 74 500 words. The PDF is authoritative. |
| `reports/` | `01_CHAPTER_PRESERVATION.md` (scope and topic coverage against the original), `02_PEDAGOGICAL_IMPROVEMENT.md` (the seven-step section sequence and what it changed), `03_DESIGN_PRESERVATION_REFINEMENT.md` (measured design system, preservation table, what was refined), `04_MATHEMATICS_QA.md` (answer audit, corrections, glyph and page checks), `05_BUILD_NOTES.md` (source layout and how to rebuild). |
| `design_reference/` | `DESIGN_NOTES.md` — page geometry, palette, type scale, panel system, and the page budget actually used. |
| `image_references/` | `IMAGE_REGISTER.md` (every photograph: file, chapter, subject, source, licence) and `LICENCES.md` (font licences, provenance, what is not claimed). |
| `images/` | `photos/` — the 22 embedded photographs at full size; `diagrams/_crop/` — the figure crops used by the DOCX. |
| `build/` | The typesetting source: `bookkit/` engine, `diagrams2.py` (45 figures), `content/ch01…ch11.py`, `front2.py`, `back2.py`, and the three exporters. |
| `source_audit/` | `original_myp2_text_layer.json` — the text layer of the original 260-page PDF, used to audit scope and to be certain no sentence was copied. |

## Structure of the book

Four parts, eleven chapters, one inquiry rhythm:

| Part | Chapters | Printed pages |
|---|---|---|
| I · Number and proportion | 1 Ratios and equivalent ratios · 2 Proportional reasoning · 3 Rates and unit rates · 4 Integers and operations · Part I review | 19–92 |
| II · Algebra and pattern | 5 Algebraic expressions and equations · 6 Numerical patterns and generalisation · Part II review | 93–127 |
| III · Geometry and space | 7 2D geometry: angles, perimeter and area · 8 3D solids, surface area and volume · 9 Transformations and symmetry · Part III review | 128–193 |
| IV · Probability and data | 10 Probability and simulation · 11 Univariate data · Part IV review | 194–233 |
| V · Reference | Answers 235 · Formula bank 253 · Glossary 256 · Index 260 · References 264 | 234–265 |

Every chapter: unit planner (key and related concepts, global context, statement of inquiry,
factual/conceptual/debatable questions, ATL skills, Support/Core/Extension pathways) →
learning intentions and prerequisite check → **Engage → Explore → Explain → worked examples →
Practice → Investigate/Apply → Reflect**, with each section naming the MYP criterion it
develops and each chapter closing with a summary, a mixed practice set, a “Before you move on”
checkpoint and a Criterion D task. Each part then closes with a Part review: ten mixed questions
that draw on every chapter in that part, with answers in the reference section.

## The book in numbers

| | |
|---|---|
| Pages | 265 (the original first edition was 260) |
| Chapters / parts | 11 / 4 |
| Sections | 52 numbered (41 teaching, 11 summary) + 4 part reviews |
| Worked examples | 121 — every one with steps, answer and a check |
| Practice questions | 673, each with an answer or a reasoned solution |
| Answers | 673 |
| Part reviews | 4 (10 mixed questions each, with answers) |
| “Before you move on” checkpoints | 11 |
| COMMON ERROR panels | 40 |
| Panels | 153 |
| Investigation / Criterion D cards | 22 / 11 |
| Photographs | 22 |
| Numbered vector figures | 45 |
| Tables | 64 |
| Contents entries / index terms | 83 / 98 |

## Rebuilding

```
cd build
python build_book.py     ../final/MYP2_Mathematics_Improved_First_Edition.pdf
python export_docx.py    ../final/MYP2_Mathematics_Improved_First_Edition.docx
python export_manuscript.py
```

Requires `reportlab`, `pymupdf`, `python-docx`, `Pillow` and `fonttools`. A full rebuild takes
about 20 seconds. The build is three-pass: contents and index are filled from a page registry
recorded by the previous pass, so references always match the body.

## Rights

Text, worked examples, exercises, investigations and diagrams were written or drawn for this
edition. Photographs are public-domain or openly licensed stock, credited in
`image_references/IMAGE_REGISTER.md`. Playfair Display, Source Serif 4 and Inter are used under
the SIL Open Font License 1.1. No ISBN, publisher, barcode, price or IB endorsement is claimed.
