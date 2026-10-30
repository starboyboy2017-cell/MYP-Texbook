# MYP Mathematics 1 — Improved First Edition

**Year 1 student coursebook.** Author: SADIKOU MOUKODDIM.
205 A4 pages. Independent educational publication; not published by, sponsored by or
affiliated with the International Baccalaureate Organization.

## Deliverable

| File | What it is |
|---|---|
| `final/MYP1_Mathematics_Improved_First_Edition.pdf` | The complete book: cover, front matter, ten chapters in five parts, answers, formula bank, glossary, index, references. 205 pages, print-ready PDF. |
| `final/MYP1_cover.png` | The cover, rendered at 160 dpi for preview and catalogue use. |

## Everything else in this folder

| Folder | Contents |
|---|---|
| `manuscript/` | Text extracts of the typeset pages, one Markdown file per chapter plus front and back matter, with a page marker on every page. For searching, reuse and word counts. The PDF is authoritative. |
| `reports/` | `EDITORIAL_REPORT.md` (scope, structure, pedagogy, decisions), `QA_REPORT.md` (measured checks on the delivered PDF), `BUILD_NOTES.md` (how to rebuild). |
| `design_reference/` | `DESIGN_NOTES.md` — page geometry, palette, type scale and panel system, with a table of what was corrected relative to the source design. |
| `image_references/` | `IMAGE_REGISTER.md` (every asset, where it is used, what it shows, rights position) and `LICENCES.md` (font licences, provenance, what is not claimed). |
| `images/` | The ten original chapter illustrations at full size, plus the banner crops used in the book. |
| `build/` | The typesetting source: the `bookkit` engine, `diagrams.py`, and the chapter content. Rebuild with `python build_book.py out.pdf`. |
| `source_audit/` | Text-layer extraction of the source PDF, used to audit coverage and to be certain no sentence was copied. |

## Structure of the book

Five parts, ten chapters, seven stages per chapter:

1. Number, structure and proof — number systems; powers and order of operations; factors, multiples and primes
2. Fractions, decimals and percentages
3. Algebra as compressed reasoning — patterns, expressions and equations
4. Describing space and belonging — angles and constructions; sets and classification; perimeter, area, volume
5. Reading the story in data — data, tables and graphs

Each chapter: MYP unit planner → learning intentions → engage → explore → explain
(sections with worked examples, common errors and graded practice) → investigate and
apply → criterion-mapped mini-task → review, self-assessment and teacher note.

## Rebuilding

```
cd build
python build_book.py ../final/MYP1_Mathematics_Improved_First_Edition.pdf
```

Requires `reportlab`, `pymupdf`, `pyphen`, `fonttools`, `brotli`.
