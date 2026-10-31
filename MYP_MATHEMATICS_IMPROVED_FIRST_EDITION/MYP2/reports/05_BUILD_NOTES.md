# Build notes

How this edition is typeset, where each part of it lives, and how to rebuild it.

---

## 1. Rebuilding

```
cd build
python build_book.py     ../final/MYP2_Mathematics_Improved_First_Edition.pdf
python export_docx.py    ../final/MYP2_Mathematics_Improved_First_Edition.docx
python export_manuscript.py
```

Requirements: `reportlab`, `pymupdf`, `python-docx`, `Pillow`, `fonttools` (all pure-Python
wheels). Measured on the build machine: PDF 14 s, DOCX 6 s, manuscript 1 s.

The PDF build is **three-pass**:

1. render to a scratch file, recording every chapter, section, figure, table and index term
   with the page it landed on;
2. render again with the contents and the index filled from that registry;
3. re-render if the new contents/index changed the pagination, and stop when the page count is
   stable (it converges on the second pass: `pass 2: 265 pages`, `pass 3: 265 pages`).

Page numbers in the contents, the index and every cross-reference therefore always match the
printed folios. The registry is dumped to `/tmp/myp2_entries.json` and the index map to
`/tmp/myp2_index.json` on every pass, which is what makes a page-number discrepancy
diagnosable without re-reading the PDF.

---

## 2. Source layout

```
build/
  build_book.py          entry point; PARTS / CHAPTERS tables; three-pass driver
  render2.py             the block DSL: one interpreter from block list to page flow
  diagrams2.py           45 numbered figures drawn from 52 registered functions (vector)
  bookkit/
    spec.py              page geometry, palette, type scale, tag and criterion colours
    fonts.py             font registration, per-face renaming and the symbol fallback
    markup.py            inline markup -> reportlab (bold, italic, sup/sub, `math`, symbols)
    flow.py              Pager: reading column, page breaks, keep-with-next
    typeset.py           letterspaced labels, display numerals, tracked setting
    blocks.py            Body, DataTable, Panel, Photo, Diagram, Stage, Practice, Chip …
    book.py              page furniture: running heads, folios, part and chapter plates
    plates.py            cover, part dividers, chapter openers
  content/
    chbase.py            the authoring vocabulary (see §3)
    front2.py            contents, how to use, MYP framework, criteria, course map, notation
    ch01.py … ch11.py    one module per chapter, plus its ANSWERS table
    back2.py             answers, formula bank, glossary, index, references
  fonts/                 instanced subsets of Playfair Display, Source Serif 4, Inter, DejaVu
```

Content modules hold the text; the engine holds the design. Nothing in `content/` sets a font
size, a colour or a coordinate except where a diagram is deliberately drawn (figure geometry is
in `diagrams2.py`, not in chapter modules).

---

## 3. The authoring vocabulary

Each chapter module starts with `from chbase import *` and builds one `BLOCKS` list. The helpers
are short enough to keep the source readable as prose:

| Helper | Renders |
|---|---|
| `S(num, title, criterion, related)` | a section heading with its criterion kicker and concept chips |
| `ST`, `L`, `P`, `H`, `UL`, `OL` | stage marker, lead paragraph, body paragraph, heading, lists |
| `DEF`, `KEY`, `VOCAB`, `MYP`, `ATL`, `STATEMENT` | definition, key-idea, vocabulary, MYP-context, ATL and statement-of-inquiry panels |
| `WE(ref, title, problem, steps, answer, check)` | a worked example with numbered steps and a check line |
| `ERR(text)` | a COMMON ERROR panel |
| `PRAC(ref, tag, ranges, questions)` / `Q(text, tag)` | a practice set; `tag` is `F`, `P`, `R` or `E` |
| `TABLE(head, rows, widths, caption)` | a ruled data table |
| `DIAG(height, name, caption)` | a numbered vector figure |
| `PHOTO(file, aspect, caption, credit)` | a photograph with its credit line |
| `CARD_I`, `CARD_D` | investigation and Criterion D cards |
| `FORMULA`, `GAP`, `BOX` | display formula, vertical space, boxed statement |

`Q` accepts a second tag (`tag2`) where a question carries two skills.

---

## 4. Design system

All measured values live in `bookkit/spec.py`: A4 trim, a 121 mm reading measure, the palette
(`#0F1F2D` cover, `#15263A` ink, `#A64B27` kickers, `#E9DFD0` cream, `#D8B58C` copper,
`#C1764C` terracotta, `#8FA69B` sage), the panel grounds, the hairline weights and the type
scale (body 9.7/13.5, H1 21, kicker 6.6, intro 10.6, caption 7.0). Changing the book's
appearance is a matter of editing this file, not the content.

Diagrams are drawn with a small `Pen` object: unit fractions of the figure box for position,
points for stroke widths and label sizes. This is what keeps one line-weight system across all
45 figures.

---

## 5. Exports

**DOCX** (`export_docx.py`) walks the same block lists and re-renders every figure through a
reportlab canvas, then embeds the resulting pixmap at 220 dpi. It is a real Word document —
styles, headings, tables, images — not a PDF wrapper; text in it is selectable and editable.

**Manuscript** (`export_manuscript.py`) writes one Markdown file per chapter from the block
lists, then writes `front_matter.md` and `back_matter.md` by reading the delivered PDF, because
those pages are drawn page-by-page rather than assembled from blocks.

---

## 6. Regression checks used during the build

```
# page count and contents/index convergence
python build_book.py … | tail -3

# missing glyphs anywhere in the PDF
python -c "import pymupdf; d=pymupdf.open(pdf); print([i+1 for i,p in enumerate(d) if '\x00' in p.get_text()])"

# question/answer pairing
python -c "…" # walks each chapter's practice blocks against ANSWERS

# images actually embedded
python -c "…" # counts image objects per page
```

The same four checks are what `reports/04_MATHEMATICS_QA.md` records.

---

## 7. Known constraints

* The build is deterministic: same sources, same PDF bytes, same page count.
* A `PHOTO` block whose file is missing raises immediately — no placeholder can reach the page.
* Pagination is fractional-space-driven: a change to `spec.py` type sizes will move page breaks
  and therefore the contents and index. Rebuild; do not hand-edit page numbers.
* `bookkit` has no external dependencies beyond reportlab and fontTools, so the book can be
  rebuilt on any machine with Python 3.9+.
