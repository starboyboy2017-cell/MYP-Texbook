"""Assemble the complete MYP Mathematics 1 - Improved First Edition.

Two passes:
  1. render once, recording the printed page label of every chapter, section,
     figure and definition so that the contents, list of figures and index can
     be built from real data;
  2. render again with those page references inserted.
"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "content"))

from bookkit import spec, fonts, plates
from bookkit.book import Book
from bookkit.flow import Pager

fonts.register()

CHAPTERS = [
    ("ch01", "Number systems and place value", "Number, structure and proof"),
    ("ch02", "Powers, expanded form and order of operations", "Number, structure and proof"),
    ("ch03", "Factors, multiples and primes", "Number, structure and proof"),
    ("ch04", "Fractions and decimals", "Fractions, decimals and percentages"),
    ("ch05", "Percentages and applications", "Fractions, decimals and percentages"),
    ("ch06", "Patterns, expressions and equations", "Algebra as compressed reasoning"),
    ("ch07", "Lines, angles, triangles and constructions", "Describing space and belonging"),
    ("ch08", "Sets and classification", "Describing space and belonging"),
    ("ch09", "Perimeter, area, surface area and volume", "Describing space and belonging"),
    ("ch10", "Data, tables and graphs", "Reading the story in data"),
]

PARTS = [
    ("I", ["Number, structure", "and proof"],
     ["What a written number actually says, and the rules that",
      "keep calculation reliable."],
     "The first three chapters establish the grammar of number:",
     "position, power, and the structure of factors and primes."),
    ("II", ["Fractions,", "decimals and", "percentages"],
     ["Three ways of writing the same part of a whole, and the",
      "decisions each one makes easy."],
     "Fractions, decimals and percentages are not three topics;",
     "they are three notations for one idea."),
    ("III", ["Algebra as", "compressed", "reasoning"],
     ["A letter is a number you have not chosen yet, and an",
      "equation is a question written as a balance."],
     "Algebra begins as shorthand for a pattern and becomes a",
     "method for finding what is not yet known."),
    ("IV", ["Describing space", "and belonging"],
     ["Lines, angles, shapes, sets and measured space: the",
      "mathematics of arranging and classifying."],
     "Geometry is the study of what must be true of any figure,",
     "and sets are the study of what must belong where."),
    ("V", ["Reading the story", "in data"],
     ["Every table and graph is a set of choices, and every",
      "choice decides what a reader notices."],
     "Data becomes evidence only when the display is honest and",
     "the summary is appropriate."),
]

PART_OF = {1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4}


# ------------------------------------------------------------------- registry
class Registry:
    def __init__(self):
        self.entries = []      # (kind, chapter, title, page_label)

    def record(self, kind, chapter, title, label):
        self.entries.append((kind, chapter, title, label))


def render(path, reg=None, contents=None):
    reg = reg or Registry()
    bk = Book(path, title="MYP Mathematics 1 \u2014 Improved First Edition",
              author="SADIKOU Moukoddim",
              subject="Student coursebook: an improved first edition of the MYP Year 1 "
                      "mathematics course.")

    # ---------------------------------------------------------------- cover
    bk.pages = 0
    bk.new_page("none")
    plates.cover(bk.c)

    # ------------------------------------------------------------- front matter
    fm = importlib.import_module("front")
    fm.CONTENTS_ENTRIES = contents
    fm.build_front(bk, reg)

    # ------------------------------------------------------------- chapters
    bk.start_body()
    current_part = -1
    for i, (mod_name, title, part) in enumerate(CHAPTERS, start=1):
        pi = PART_OF[i]
        if pi != current_part:
            current_part = pi
            num, tlines, subs, meta1, meta2 = PARTS[pi]
            bk.new_page("none")
            plates.part_open(bk.c, num, tlines, subs, [meta1, meta2])
            reg.record("part", 0, " ".join(tlines), bk.page_label)

        mod = importlib.import_module(mod_name)
        import helpers as H
        H.set_registry(reg, i)
        H.bind_book(bk)
        bk.new_page("none")
        plates.chapter_plate(bk.c, mod.PLATE)
        reg.record("chapter", i, title, bk.page_label)
        full = {"Number, structure": "Number, structure and proof",
                "Fractions,": "Fractions, decimals and percentages",
                "Algebra as": "Algebra as compressed reasoning",
                "Describing space": "Describing space and belonging",
                "Reading the story": "Reading the story in data"}[PARTS[pi][1][0]]
        bk.part_label = f"Part {PARTS[pi][0]} \u00b7 {full}"
        bk.chapter_label = f"Chapter {i} \u00b7 {title}"
        mod.build(bk, None)

    # -------------------------------------------------------------- back matter
    bm = importlib.import_module("back")
    bm.build_back(bk, reg)

    # ---------------------------------------------------------- back cover
    bk.new_page("none")
    plates.back_cover(bk.c)

    bk.save()
    return bk, reg


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/MYP1_improved.pdf"
    # first pass: collect the page labels the contents page needs, then rebuild
    _bk1, reg1 = render("/tmp/_pass1.pdf")
    entries = [e for e in reg1.entries if e[0] in ("part", "chapter", "front")]
    bk, reg = render(out, contents=entries)
    print("pages:", bk.pages, "->", out)
    import json
    with open("/tmp/labels.json", "w") as f:
        json.dump(bk.labels, f)
