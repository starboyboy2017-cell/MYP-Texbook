"""Assemble the complete MYP Mathematics 2 - Improved First Edition.

The build is iterative. A contents page and an index cannot be set until the
pages they point at exist, and adding them shifts the pagination, so the book is
composed repeatedly (usually three times) until the recorded page numbers stop
changing. Only then is the deliverable written.

Run:  python build_book.py ../final/MYP2_Mathematics_Improved_First_Edition.pdf
"""
import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "content"))

from bookkit import spec, fonts, plates, typeset
from bookkit.book import Book
from bookkit.flow import Pager

import render2 as R2

fonts.register()

CHAPTERS = [
    ("ch01", "Ratios and equivalent ratios"),
    ("ch02", "Proportional reasoning"),
    ("ch03", "Rates and unit rates"),
    ("ch04", "Integers and operations"),
    ("ch05", "Algebraic expressions and equations"),
    ("ch06", "Numerical patterns and generalisation"),
    ("ch07", "2D geometry: angles, perimeter and area"),
    ("ch08", "3D geometry: solids, surface area and volume"),
    ("ch09", "Transformations and symmetry"),
    ("ch10", "Probability and simulation"),
    ("ch11", "Univariate data"),
]

PARTS = [
    ("I", "Number and proportion", [1, 2, 3, 4]),
    ("II", "Algebra and pattern", [5, 6]),
    ("III", "Geometry and space", [7, 8, 9]),
    ("IV", "Probability and data", [10, 11]),
]

PART_OF = {}
FIRST_OF = {}
for _num, _name, _chs in PARTS:
    FIRST_OF[_chs[0]] = _num
    for _c in _chs:
        PART_OF[_c] = (_num, _name)

FRONT_PAGES = ["How to use this coursebook", "The MYP framework in this course",
               "Assessment criteria in practice",
               "Three pathways through the course",
               "Command terms used in this book",
               "Course map and progression", "Notation, working and habits",
               "Calculators, rounding and accuracy"]


def build(path, contents=None, index_map=None):
    bk = Book(path, title="MYP Mathematics 2 \u2014 Improved First Edition",
              author="SADIKOU Moukoddim",
              subject="Student coursebook: an improved first edition of the MYP "
                      "Year 2 mathematics course.")
    entries = []
    index_hits = {}

    # ------------------------------------------------------------------ cover
    bk.new_page("none")
    plates.cover(bk.c)

    # ----------------------------------------------------------- front matter
    import front2
    front2.CONTENTS = contents
    front2.build_front(bk)
    labels = front2.build_orientation(bk, {})
    entries.append(("fronthead", 0, "Front matter", None))
    entries.append(("front", 0, "Half title, title page and imprint", "2\u20134"))
    for t in FRONT_PAGES:
        entries.append(("front", 0, t, labels.get(t, "")))

    # ---------------------------------------------------------------- chapters
    bk.start_body()
    R2.SECTIONS = []
    R2.INDEX_HITS = {}
    for cno, (mod_name, title) in enumerate(CHAPTERS, start=1):
        pnum, pname = PART_OF[cno]
        mod = importlib.import_module(mod_name)
        if cno in FIRST_OF and FIRST_OF[cno] == pnum:
            entries.append(("part", pnum, f"Part {pnum} \u00b7 {pname}", None))
        bk.new_page("none")
        plates.chapter_plate(bk.c, mod.PLATE)
        bk.part_label = f"Part {pnum} \u00b7 {pname}"
        bk.chapter_label = f"Chapter {cno} \u00b7 {title}"
        entries.append(("chapter", cno, title, bk.page_label))

        bk.new_page("wide")
        p = Pager(bk)
        R2.reset(cno)
        R2.SECTIONS = []
        R2.begin_capture(cno, bk)
        R2.render(p, mod.BLOCKS, cno)
        for (_ch, sec_title, label) in R2.SECTIONS:
            entries.append(("section", cno, sec_title, label))

    for term, pages in R2.INDEX_HITS.items():
        index_hits.setdefault(term, [])
        for pg in pages:
            if pg not in index_hits[term]:
                index_hits[term].append(pg)

    # -------------------------------------------------------------- back matter
    import back2
    ref_pages = {}

    bk.new_page("none")
    c = bk.c
    c.saveState()
    c.setFillColor(spec.NAVY)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    L = spec.MARGIN_OUTER
    typeset.draw(c, L, spec.PAGE_H - 96, "PART V", "Inter-Semi", 7.4, spec.GOLD, 3.2)
    typeset.draw(c, L, spec.PAGE_H - 190, "Reference", "Playfair-Display", 52,
                 spec.CREAM, 0.3)
    typeset.draw(c, L, spec.PAGE_H - 230, "Answers, formulas, vocabulary, index and "
                                          "sources.", "SourceSerifItalic", 12.6,
                 spec.GOLD_PALE)
    plates.motif_data(c, spec.PAGE_W - 350, 460, 270, 270)
    typeset.draw(c, L, 62, "SADIKOU MOUKODDIM", "Inter-Semi", 6.3, spec.GOLD_PALE, 2.1)
    typeset.draw(c, spec.PAGE_W - L, 62, "MYP MATHEMATICS 2", "Inter-Semi", 6.3,
                 spec.GOLD_PALE, 2.1, "right")
    bk.part_label = "Part V \u00b7 Reference"
    bk.chapter_label = "Answers, formulas, glossary and index"
    entries.append(("part", "V", "Part V \u00b7 Reference", None))
    entries.append(("chapter", "R", "Answers, formula bank, glossary and index",
                    bk.page_label))

    back2.build_answers(bk, CHAPTERS)
    back2.build_formula_bank(bk)
    back2.build_glossary(bk)
    back2.build_index(bk, index_map or {})
    back2.build_references(bk)

    # -------------------------------------------------------------- back cover
    bk.new_page("none")
    plates.back_cover(bk.c)
    bk.save()
    return bk, entries, index_hits


def converge(out):
    contents, index_map = None, None
    prev = None
    for attempt in range(1, 6):
        tmp = "/tmp/_myp2_pass%d.pdf" % attempt
        bk, entries, hits = build(tmp, contents=contents, index_map=index_map)
        key = json.dumps([[e[0], str(e[1]), e[2], e[3]] for e in entries])
        print(f"  pass {attempt}: {bk.pages} pages, {len(entries)} contents "
              f"entries, {len(hits)} index terms")
        if prev is not None and key == prev:
            break
        prev = key
        contents, index_map = entries, hits
    bk, entries, hits = build(out, contents=entries, index_map=index_map)
    print("final:", bk.pages, "pages ->", out)
    with open("/tmp/myp2_entries.json", "w") as f:
        json.dump(entries, f, indent=1)
    with open("/tmp/myp2_index.json", "w") as f:
        json.dump(hits, f, indent=1)
    return bk, entries, hits


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/MYP2_improved.pdf"
    converge(out)
