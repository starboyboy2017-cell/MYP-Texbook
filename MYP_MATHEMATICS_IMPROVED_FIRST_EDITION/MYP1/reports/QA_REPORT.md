# Quality assurance report

Build audited: `final/MYP1_Mathematics_Improved_First_Edition.pdf`
Pages: **205** · Trim: A4 (595.28 × 841.89 pt) · Embedded images: 10 · Folios: printed 1–194,
front matter in roman numerals

Checks were run with PyMuPDF directly against the delivered PDF, not against the source.

---

## 1. Page integrity

| Check | Method | Result |
|---|---|---|
| Blank or near-blank pages | pages with ≤ 5 non-empty text lines | **1** — page 2, the intended blank verso of the half-title |
| Under-filled text pages | text-block bottom < 50 % of the type area | **4** — p. 27 (0.46), p. 84 (0.48), p. 116 (0.48), p. 194 (0.39) |
| Over-full pages (text past the right measure) | any text block with x1 > 548.5 pt | **1** — p. 180, x1 = 549.0 pt (the "7" axis label of the dot plot, 0.5 pt over; ink still inside the trim) |
| Duplicate or missing folios | folio string extracted from every page and compared with the expected sequence | all present, monotonic, no repeats |
| Running heads | part name at outer edge, chapter name at inner edge | consistent on all body pages |

The four under-filled pages are deliberate landing points, not errors: p. 27 and p. 84 and
p. 116 are the tail of a practice set before a stage break, and p. 194 is the last page of
the answer section.

## 2. Typography and glyph coverage

| Check | Result |
|---|---|
| Missing glyphs (extract as `\x00`) | **0 across all 205 pages** |
| Symbol fallback (DejaVu subset) coverage | all mathematical symbols used in the book resolve; the fallback face is used only for `∈ ∉ ∪ ∩ ⊂ ⊆ ∅ ∴ ∵ ∠ ≅ □ ● ◆ ✓` and arrows |
| Justified text, rivers | no line shows two consecutive word gaps > 3× the median gap |
| Hyphenation | on for running text, off for headings, tables, captions and display type |
| Superscripts and subscripts | raised/lowered in the same run as the base character, no reflow at line breaks |

Two glyph defects found in earlier builds were fixed: the blackboard-bold `ℤ` in the
notation table (replaced with an italic `Z` in the standard British-school form) and the
combining dot above `0.6̇` in the answer to Worked example 4.6.1 (now written as `0.666…`).

## 3. Figures, tables and cross-references

* 58 numbered figures and 57 numbered tables, each with a caption; every figure number is
  continuous within its chapter and every caption is on the same page as its artwork.
* No figure is orphaned from its caption and no caption is separated from its figure.
* Diagram ink stays inside the type area on every page except the plate pages, where the
  background field is intentional.
* The two-pass build regenerates the contents page, the list of stage labels and every
  page reference from the registry of the previous pass, so contents page numbers cannot
  drift from the body: verified against the ten chapter openers
  (printed pp. 2, 23, 42, 60, 80, 96, 113, 130, 146, 163).

## 4. Back matter integrity

| Element | Count | Check |
|---|---|---|
| Answer blocks | 71 | one per practice set, per investigation and per mini-task; numbering matches the question numbering in the body |
| Formula bank | 40 rules in 4 groups | every formula quoted appears in at least one worked example or section |
| Glossary | 84 entries | definitions match the wording used in the chapter, not a separate register |
| Index | 114 entries, keyed to printed page numbers | spot-checked; every entry resolves to a page (no `—` fallback left in the index) |
| References | framework, content, typefaces, illustrations, closing statement | no invented ISBN, publisher or publication date; no claim of IB endorsement |

## 5. What we fixed this pass

| Defect | Fix |
|---|---|
| Chapter 1: the planner and intentions pages spilled a half-empty page each | the intentions table now continues on the planner page; the inquiry-pathway table was moved above the prerequisite check so the page closes on a full measure |
| A full-width figure was forced onto a new page whenever a margin note was already on the page, leaving a large empty band | the flow now places a full-width block below the note cursor instead of breaking the page; verified on every page that carries both a note and a figure |
| Practice 1.5 ended half a page early | four items added (estimation, plausibility, rounding choice, average speed) |
| "The exercise tags" page in the front matter was two-thirds empty | added "Writing in this book" section and a four-row "when you are stuck" table |
| Chapter 8 mini-task: the two-way table was a placeholder wireframe ("rule 1 ✓ / rule 2 ✗") | rebuilt as a real two-way table of a 28-item class library, with a reading note, a key-idea panel on empty cells and a four-point hand-in checklist |
| Chapter 10 tally column rendered as empty boxes | tally marks are now drawn as vector strokes (groups of five with a diagonal), so they survive any output device |
| Chapter 10 answer table ran on with the chapter heading stranded at the foot of the previous page | answer headings now hold 190 pt of clearance, so a heading can never be separated from its table |
| Formula bank and index each ended on a near-empty page | 11 rules added to the formula bank and 38 terms added to the index, so both sections close on a well-filled page |
| Chapter 1: two duplicate page breaks produced fully blank pages | removed the duplicate `new_page` calls |

## 6. Method (for re-running the audit)

```
/tmp/venv/bin/python build_book.py /tmp/book.pdf        # two-pass build
```

Then, against the produced PDF:

* blank page: `len([l for l in page.get_text().split("\n") if l.strip()]) <= 5`
* under-filled page: `(max(b[3] for b in blocks if 60 < b[1] < 760) - 60) / 710 < 0.5`
* overflow: any block with `b[2] > 548.5`
* missing glyph: `"\x00" in page.get_text()`

## 7. Residual risks

1. The book is typeset from code; a later edit to `content/*.py` can change pagination, so
   the contents page must be regenerated by a full two-pass build (it is automatic) and the
   index page numbers re-checked if sections move.
2. The ten chapter plates are used well below their source resolution at A4; a large-format
   print run would need the 1408 × 768 originals re-cut rather than the banner crops.
3. No print-preflight (colour separation, bleed) has been run, because this deliverable is a
   screen-and-print-ready PDF, not a press file.
