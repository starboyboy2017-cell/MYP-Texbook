# Build and source notes

## Rebuilding the book

```
pip install reportlab pymupdf pyphen fonttools brotli
cd build
python build_book.py out.pdf
```

The build is **two-pass**: the first pass renders to a scratch file and records every
chapter, section, figure and table label; the second pass renders the real file with the
contents page and the index filled in from that registry. Page numbers in the contents and
index therefore always match the body.

Typical build time: 6 seconds. Output: 205 pages, ≈ 3.5 MB.

## Source layout

```
build/
  build_book.py        entry point; CHAPTERS / PARTS tables; two-pass driver
  bookkit/
    spec.py            page geometry, palette, type scale (all measured values live here)
    fonts.py           font registration and the symbol fallback
    markup.py          inline markup -> reportlab (bold, italic, sup, sub, symbol fallback)
    flow.py            Pager: reading column, margin notes, full-width blocks, page breaks
    typeset.py         display-type helpers (letterspaced labels, numerals)
    blocks.py          Body, DataTable, Panel, Figure, Diagram, Stage, WritingSpace, ...
    book.py            page furniture: running heads, folios, plates
    plates.py          cover, part dividers, chapter openers
  diagrams.py          every vector figure in the book, as drawing callbacks
  content/
    helpers.py         the authoring vocabulary (section, body, panel, we, practice, q, ...)
    front.py           contents, orientation, MYP framework, criteria, course map, notation
    ch01.py ... ch10.py  one file per chapter
    back.py            answers, formula bank, glossary, index, references
  fonts/               instanced and subset TTF files
```

## Authoring vocabulary (`content/helpers.py`)

| Call | Produces |
|---|---|
| `section(p, "1.2", title, "A · i", [heads])` | numbered section head with criterion/strand line |
| `body / lead / lst / h3 / h4` | running text, lead paragraph, list, sub-heads |
| `panel(p, kind, title, text)` | one of the five panel types (definition, keyidea, error, atl, note) |
| `atl(p, verbatim_text, title)` | ATL skill panel, wording preserved from the framework |
| `we(p, "1.5.1", title, problem, steps, answer, check)` | worked example with numbered steps, answer line and check |
| `practice(p, "1.5", "SUPPORT 1–3 · CORE 3–7", [q(...)])` | graded practice set |
| `q(text, "F")` | one question with a fluency / reasoning / problem-solving / extension tag |
| `fig(p, name, caption)` / `diag(p, height, fn, caption)` | numbered figure, raster or vector |
| `table(p, head, rows, widths=...)` | numbered table |
| `note(p, title, text)` | note in the outer margin |
| `criteria_panel(p, a=..., b=..., c=..., d=...)` | criterion/strand summary panel |
| `assessment_close(p, rows, atl_text, next_title=...)` | the seven-part chapter close, including the ruled writing space |

## Conventions that the build relies on

* `content/ch01.py` `_body(bk)` and `_wide(bk)` already open a page — never call
  `bk.new_page(...)` as well, or the page is left blank.
* A flow whose height exceeds the frame's remaining space starts a new page; anything that
  must size itself from the remaining space (the writing space at the end of a chapter)
  computes its height from `p.frame.remaining` at wrap time.
* Chapter-level counters are reset with `reset_counters(chapter)`, so figure and table
  numbers restart at 1 in each chapter.
* Tables with more than nine rows need `splittable` set to survive a page break.
* `helpers.table()` takes `fs=`, not `font_size=`.

## Dependencies

`reportlab` (PDF), `pymupdf` (QA and raster checks), `pyphen` (hyphenation),
`fonttools` (font instancing and subsetting), `brotli` (compressed font tables).
All are permissively licensed and none is redistributed with the book.
