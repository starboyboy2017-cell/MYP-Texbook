# MYP Mathematics 3 — print repair report

`final/MYP3_Mathematics_Repaired.pdf` is the repaired build: 285 pages, same page
size, same pagination, same text column (60 → 539.3 pt), no line reflowed.

The input `final/MYP3_Mathematics_Improved_First_Edition.pdf` has no build source;
every defect below is repaired in the PDF itself. Text that the source does not
determine is **reported, not guessed** (see the last section).

## Pipeline

The build is reproducible from the committed tools alone:

    python3 tools/fetch_fonts.py                     # upstream faces (once)
    python3 tools/build_fonts.py                     # rebuild the 10 subsets -> fonts/
    python3 tools/repair_pdf.py   IN.pdf /tmp/rep.pdf     # embed the good faces
    python3 tools/fix_titles.py   /tmp/rep.pdf /tmp/titled.pdf
    python3 tools/fix_text.py     /tmp/titled.pdf OUT.pdf

`fix_text.py` prints what it changed on every run:

    text repairs: {'code0': 20, 'nbsp': 57, 'markup': 5, 'heading': 2, 'figure': 1}

## What was wrong, and what was done

### 1. Tofu — `□` in place of symbols (20 sites)

The input's embedded font streams are damaged; MuPDF reports
`FT_New_Memory_Face … unknown file format` and `zlib error: incorrect header check`
for every one of them. Rebuilding the faces from upstream fixed the glyphs but
left each damaged code mapped to the face's **empty slot (code 0)**, which is what
a reader draws as a hollow box.

Each site is repaired by rewriting the single literal that holds the bad byte, so
neighbouring text cannot move:

| page | what | symbol |
|------|------|--------|
| 16, 24 (×2), 269, 270 | square roots | `√` |
| 28 (×3) | absolute-value rows `\|x - 3\| < 1` | `<` |
| 82 (×4) | matchstick labels `1 < 3` … `4 < 9` | `<` |
| 213 (×3) | correlation labels `r ≠ 0.95`, `r ≠ 0.25`, `r ≠ -0.9` | `≠` |
| 275 (×3) | subscript letters `a_k`, `u_n` | `k`, `n` |

The symbols are drawn from `STIXTwoMath-Regular`, which is named explicitly around
each one and restored after it. Two details mattered: the *text* faces map `√` to
code 0 as well, so a symbol routed to them lands on the empty slot; and the
book's own subscript style is a smaller size with a **negative** rise (page 36
sets `(1)` at 6.3 pt, `-6.7 Ts`), which is what the `k`/`n` use.

### 2. Literal markup left in the text (62 fixes + 5 rule applications)

`&nbsp;` appeared 57 times as literal text (all in the read-aloud `Figure`
descriptions), and stray `` ` ``, `\_`, `^{…}`, `\{`, `\}` markup elsewhere.
Replaced with the space or the character they stand for; `^{…}` became real raised
text. Every replacement passes a width guard, so no run can grow into the margin.

### 3. Figure 3.2 running off the page (page 82)

The builder drew the four matchstick groups at a fixed 120.3 pt pitch from
x = 232.8, so the fourth group and its label `4 < 9` lay between x = 543 and 663 —
entirely outside the 595.3 pt trim. The row is rescaled about its own origin
(×0.721) to fit the column, and the four labels, which are absolute `Tm`
placements, are re-centred under their groups. Triangles and labels stay in step.

### 4. Running heads past the trim (pages 106, 234)

`PRACTICE 4.3 · LINEAR MODELS AND SIMULTANEOUS LINES (CONTINUED)` and
`PRACTICE 10.1 · …` are centred by hand, one glyph per block, and ended at
x = 569.3 and 548.8. No word can be dropped, so each glyph's x is pulled toward
the line's left edge in proportion to its distance along it (×0.885 and ×0.989);
sizes, faces and the baseline are untouched.

## Verification

* 285 pages before and after; every page size identical; 21 images before and
  after; no links in either.
* Character comparison against the pre-repair build, ignoring whitespace:
  **removed** — only debris (`\x00` ×19, `&nbsp;` ×57, `` ` `` ×26, `\`, `_`,
  `^`, `{`, `}`); **added** — only real symbols (`√` ×7, `<` ×7, `≠` ×3, `k` ×2,
  `n`, `9`, `1`). Nothing else changed.
* No `\x00`, backtick or `&nbsp;` left in extracted text on any page.
* Path overflow scan over all 285 pages: 0 glyphs past x = 539.4. (The other 17
  pages that carry coordinates at 595.3 are full-bleed rules, not overflow.)

## Reported, not guessed

* **Page 275, `a_k` / `u_n`:** the source sets these slots at 6.3 pt with a
  **+3.3 pt rise** — a superscript position — but the DOCX reads
  `0.a₁…aₖ = (a₁…aₖ)/99…9` and `uₙ = a + (n - 1)d`, which are subscripts. They are
  drawn as subscripts (−2.4 pt rise) to match the source text and the book's own
  convention. If the printed original really meant raised letters, this is the one
  place to change: `CODE0_SUBS` in `tools/fix_text.py`.
* **Answer blanks** (`Insert < or >:`, `Insert ∈ or ∉:`) are left as blanks. The
  source does not say which sign belongs there, so neither was filled in.
