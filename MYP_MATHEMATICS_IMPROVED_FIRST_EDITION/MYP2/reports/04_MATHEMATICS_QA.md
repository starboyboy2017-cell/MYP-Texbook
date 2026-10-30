# Mathematics and editorial QA

Audited edition: `../final/MYP2_Mathematics_Improved_First_Edition.pdf` — 245 pages, A4,
built from `../build/`. Checks were run against the delivered PDF and against the content
modules it is built from, never against the previous edition's output.

---

## 1. What was checked

| Area | Method | Result |
|---|---|---|
| Every practice question has an answer | programmatic pairing of `practice` blocks with `ANSWERS` by section and position | **633 questions, 633 answers, 0 orphans, 0 duplicates** |
| Every answer is mathematically right | each of the 633 answers recomputed from its printed question and corrected where wrong | **22 corrections applied** (§4) |
| No placeholder answers | scan for empty strings, `—`, `TBC`, `see above` | 0 remaining |
| Worked examples | each chapter's examples read for a wrong step, wrong unit or wrong final answer; every example carries a check line | 121 examples checked, 0 uncaught errors |
| Investigations and Criterion D tasks | read for a task that can be completed with the chapter's own mathematics | 22 + 11 checked, 0 broken |
| Missing glyphs | PDF text layer scanned for `\x00` on every page | **0 on all 245 pages** |
| Text past the measure | every text block's right edge compared with the 45 pt margin | 0 overflows |
| Blank or near-blank pages | pages with ≤ 10 non-empty text lines | 3, all intended: p. 2 half-title, p. 224 Part V divider, p. 232 last answers page |
| Folios | bottom-line numerals on every page | present and monotonic on all pages except front matter, chapter openers, part dividers, references and back cover, which carry none by design |
| Embedded images | image objects counted per page | 22 photographs, all rendering, none repeated by accident |
| Fonts | font resources per page | 6 embedded subsets (Playfair, Source Serif 4 ×2, Inter, DejaVu, and the italic pair); no system font used for text |
| Editorial constraints | full-text search | no "Oak International School"; no ISBN, publisher, barcode or price claimed; no "second edition"; the words "improved first edition" used on the title, imprint and references pages |
| Required MYP apparatus | per chapter | key concept, related concepts, global context, statement of inquiry, factual/conceptual/debatable questions, ATL skills, Support/Core/Extension ranges: present in all 11 chapters |
| Required sentence frame | full text | "In order for a student to …, students must …" used in all 11 unit planners |

---

## 2. Section and answer counts

| Chapter | Sections | Questions | Answers |
|---|---|---|---|
| 1 Ratios and equivalent ratios | 5 | 61 | 61 |
| 2 Proportional reasoning | 4 | 48 | 48 |
| 3 Rates and unit rates | 4 | 48 | 48 |
| 4 Integers and operations | 4 | 50 | 50 |
| 5 Algebraic expressions and equations | 4 | 49 | 49 |
| 6 Numerical patterns and generalisation | 4 | 49 | 49 |
| 7 2D geometry | 6 | 74 | 74 |
| 8 3D geometry | 5 | 61 | 61 |
| 9 Transformations and symmetry | 6 | 73 | 73 |
| 10 Probability and simulation | 5 | 60 | 60 |
| 11 Univariate data | 5 | 60 | 60 |
| **Total** | **52** | **633** | **633** |

Each answer key is keyed by section and printed in the same order as the questions, so a
mis-numbered question would surface immediately as a shifted key.

---

## 3. How the answer audit was done

1. For each chapter, the printed question list and the answer list were put side by side and
   every answer recomputed from the question as a student would read it — including unit
   conversions, rounding and the number of decimal places the question asks for.
2. Where the recomputation disagreed, the answer was rewritten with the method that produces
   it, in the voice of the answer key (a reason, not just a number).
3. When the fault was in the *question* rather than the answer (an impossible condition, a
   missing instruction), the question was rephrased so that it is answerable and the answer
   rewritten to match.
4. The chapter was re-imported and the question/answer counts re-verified, so that no edit
   could silently shift a key.

---

## 4. Corrections applied

| # | Location | Was | Now |
|---|---|---|---|
| 1 | 1.4 Q12 | `1 320 g` (scale factor misapplied) | `880 g: one part is 80 g and there are 11 parts` |
| 2 | 1.M Q12 | `35 blue beads` (dropped the added-red detail) | `70 blue beads`, with the equation `(3k + 20) : 7k = 5 : 7` solved |
| 3 | 2.2 Q12 | `about 49 minutes` | `about 20 minutes (19.8): 5/3 + 8/5 = 49/15 L per minute` |
| 4 | 2.3 Q8 | self-contradicting text ("… 1.2 and … 1.25? No — check …") | one clean similarity check: `12.5 ÷ 5 = 20 ÷ 8 = 2.5` |
| 5 | 2.3 Q12 | `1 : 50 000` | `1 : 32 000`, with the 80 % photocopy reasoning |
| 6 | 2.M Q5 | `No: … — yes, they are proportional` | `Yes`, with all three ratios computed |
| 7 | 3.2 Q6 | `£7.14 per 100 miles` | `£14.66`, with gallons → litres → cost shown |
| 8 | 3.2 Q10 | unit prices only, question asked for a percentage | `… so the percentage saving is 0 %` |
| 9 | 3.M Q10 | `about 72 minutes` | `about 50 minutes (50.2)` from the combined rate 16.125 L/min |
| 10 | 4.2 Q11 | empty (`—`) | full number-line explanation of subtracting a negative |
| 11 | 4.2 Q12 | final temperature inconsistent with the expression | `2 + 4 × (−5) = −18 °C` |
| 12 | 5.2 Q12 | claimed `5(x + 2) = 5x + 2` at `x = 0` (they never agree) | question rephrased ("Can the two expressions ever be equal?"), answer proves they differ by 8 always |
| 13 | 5.3 Q12 | used `3n + 3 = 87` for three consecutive *odd* numbers | `n + (n + 2) + (n + 4) = 87`, so `3n + 6 = 87`, `n = 27` |
| 14 | 6.1 Q11 | second "rule" was arithmetically false | question rephrased to ask why three terms do not determine the sequence; answer gives a genuine alternative rule |
| 15 | 6.2 Q10 (earlier pass) | garbled working | smallest shared term `14` from `4n + 2 = 5m − 1` |
| 16 | 6.1 Q11 / 6.2 Q10 / 6.M Q10 / 6.M Q12 (earlier pass) | garbled or self-contradictory text | rewritten; `6.M` Q10 now `month 12, £215`, Q12 now `n = 5`, A 27 vs B 25 |
| 17 | 6.3 Q1 | `10, 17, 37` for ×4 − 3 | `5, 17, 37` |
| 18 | 7.5 Q1 | composite area of 8×5 rectangle + 4 cm square | `40 + 16 = 56 cm²` |
| 19 | 7.5 Q10 | semicircle + rectangle area/perimeter | `79.25 m²`; perimeter `4 + 10 + 4 + 15.7 = 33.7 m` |
| 20 | 7.5 Q12 | path area | outer 12 × 8 = 96, garden 60, path `36 m²` |
| 21 | 9.4 diagram (figure 9.6) | three-line legend collapsed to one unreadable line, then reversed | three separate labels, reading `scale factor 3 → sides × 3 → area × 9` |
| 22 | 8.x, 9.x, formula bank | `≡` and `⇔` fell outside the symbol fallback and extracted as `\x00` | both mapped to the fallback face; 0 missing glyphs |

The most common single cause was a **shifted or stale answer** left over from a rewritten
question, not an arithmetic slip; the second was a **question whose conditions made its answer
impossible**. Both are now checked for explicitly.

---

## 5. Language, notation and units

| Check | Result |
|---|---|
| Spelling convention | British throughout (`centimetre`, `generalise`, `centre`, `metre`, `litre`). A scan for the common US variants (`center`, `color`, `liter`, `meter`, `generalize`, `favorite`, `gray`) returned 0 |
| Decimal point and thousands separator | decimal point; thin space in thousands (`1 200`, `552 640`) — consistent in text, tables and answers |
| Units in answers | every answer to a measurement question states its unit; 0 bare numbers where a unit is required |
| Variable style | single letters italic (`k`, `n`, `x`), constants upright (`π`), in text and in diagrams |
| π convention | `π = 3.14` stated in chapter 7 and used consistently wherever a numeric answer is required; exact `π` used in algebra |
| Ratio notation | `a : b` with spaces; scale stated as `1 : n`; no mixing of `a:b` and `a : b` |
| Angle and geometry symbols | `∠`, `°`, `≅`, `∥` used only where the fallback face carries them; no glyph substitutions |
| Criterion labels | `Criterion A · IV`, `Criterion B · II` … consistent in section kickers, cards and the course map |
| Cross-references | every "see section x.y" / "see figure x.y" resolves to an existing section or figure |

---

## 6. What is *not* claimed

* Worked examples were checked by reading, not by symbolic computation; an error would have to
  survive both the author's and the checker's reading to remain.
* The 22 investigation and 11 Criterion D cards are open tasks. Their expected answers are
  described, not marked as unique, because more than one defensible response exists.
* Quartiles in chapter 11 use the "median of the lower and upper halves" convention, stated on
  the page where it is first used; other conventions give slightly different IQRs, and the
  answers follow the book's stated convention throughout.
* Rounding follows the instruction in each question. Where a question does not say, answers give
  two decimal places or the natural exact form, and the working shows why.
