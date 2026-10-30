"""Front matter: half title, title page, imprint, contents, orientation."""
from bookkit import spec, typeset
from bookkit.blocks import Panel, DataTable, H3, Body, ListBlock, Lead
from bookkit.flow import Flow, Pager, Spacer, Rule
from bookkit.markup import inline, plain, style
from bookkit.plates import _motif
import helpers as H

T = typeset.draw

# Filled by the second build pass, when every page number is known.
CONTENTS_ENTRIES = None


# ------------------------------------------------------------------ contents
class Contents(Flow):
    splittable = True

    def __init__(self, entries):
        self.entries = entries
        self.h = 0

    def _row(self, e):
        kind, ch, title, label = e
        if kind == "part":
            return 30
        if kind == "chapter":
            return 30
        if kind == "front":
            return 21
        return 15.5

    def wrap(self, w):
        self._hs = [self._row(e) for e in self.entries]
        self.h = sum(self._hs)
        return self.h

    _ROMAN = ["I", "II", "III", "IV", "V", "VI"]

    def draw(self, c, x, top, w):
        y = top
        part_i = 0
        for e, h in zip(self.entries, self._hs):
            kind, ch, title, label = e
            if kind == "part":
                y -= 9
                num = self._ROMAN[part_i] if part_i < len(self._ROMAN) else str(part_i + 1)
                part_i += 1
                T(c, x, y, num, "SourceSerif-Semi", 9.0, spec.TERRACOTTA, 0.6)
                T(c, x + 20, y, title.upper(), "Inter-Semi", 7.4, spec.TERRACOTTA, 2.2)
                c.saveState()
                c.setStrokeColor(spec.GOLD)
                c.setLineWidth(0.8)
                c.line(x, y - 6, x + w, y - 6)
                c.restoreState()
                y -= 21
            elif kind == "front":
                T(c, x + 8, y - 10.6, title, "SourceSerif", 9.6, spec.INK)
                T(c, x + w, y - 10.2, label, "Inter", 7.6, spec.INK_MUTE, 0, "right")
                y -= 21
            elif kind == "chapter":
                T(c, x + 1, y - 12, str(ch).zfill(2), "Playfair-Med", 15.5, spec.GOLD_DEEP)
                tn = title
                sz = 12.6
                while typeset.width(tn, "SourceSerif-Semi", sz) > w - 108:
                    sz -= 0.3
                T(c, x + 30, y - 11.6, tn, "SourceSerif-Semi", sz, spec.GREEN)
                T(c, x + w, y - 11, label, "Inter-Semi", 7.6, spec.GREEN, 0, "right")
                y -= 30
            else:
                T(c, x + 30, y - 9.4, title, "SourceSerif", 8.8, spec.INK_SOFT)
                tw = typeset.width(title, "SourceSerif", 8.8)
                pw = typeset.width(label, "Inter", 7.4)
                # dot leader
                c.saveState()
                c.setStrokeColor(spec.RULE_SOFT)
                c.setLineWidth(0.5)
                c.setDash(0.6, 3.2)
                c.line(x + 34 + tw, y - 6.4, x + w - pw - 8, y - 6.4)
                c.restoreState()
                T(c, x + w, y - 9.4, label, "Inter", 7.4, spec.INK_MUTE, 0, "right")
                y -= 15.5

    def min_split(self):
        return 60

    def split(self, w, avail):
        hs = [self._row(e) for e in self.entries]
        used, cut = 0, 0
        for h in hs:
            if used + h > avail:
                break
            used += h
            cut += 1
        if cut == 0:
            return None
        return Contents(self.entries[:cut]), Contents(self.entries[cut:])


class Heading(Flow):
    def __init__(self, kicker, title, space_before=0):
        self.kicker, self.title = kicker, title
        self.space_before = space_before
        self.h = 0

    def wrap(self, w):
        self._p = inline(self.title)
        self._lines = self._wrap_title(w)
        self.h = 30 + len(self._lines) * 31 + 6
        return self.h

    def draw(self, c, x, top, w):
        y = top
        T(c, x, y - 8, self.kicker.upper(), "Inter-Semi", 7.0, spec.TERRACOTTA, 2.4)
        c.setFont("Playfair-Med", spec.SZ_FM_TITLE)
        yy = y - 34
        for ln in self._lines:
            T(c, x, yy, ln, "Playfair-Med", spec.SZ_FM_TITLE, spec.GREEN)
            yy -= 31
        c.saveState()
        c.setStrokeColor(spec.GOLD)
        c.setLineWidth(0.9)
        c.line(x, yy + 14, x + 72, yy + 14)
        c.restoreState()

    def _wrap_title(self, w):
        words = plain(self.title).split()
        lines, cur = [], ""
        for word in words:
            trial = (cur + " " + word).strip()
            if typeset.width(trial, "Playfair-Med", spec.SZ_FM_TITLE) <= w:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        return lines


# ---------------------------------------------------------------- page plates
def _half_title(bk):
    bk.new_page("plain")
    c = bk.c
    c.saveState()
    c.setFillColor(spec.CREAM)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    T(c, 62, spec.PAGE_H - 120, "MYP MATHEMATICS 1", "Inter-Semi", 7.2, spec.GOLD_DEEP, 2.6)
    T(c, 62, spec.PAGE_H - 260, "Mathematics 1", "Playfair-Display", 46, spec.GREEN)
    T(c, 62, spec.PAGE_H - 296, "Student Coursebook", "Playfair-Med", 19, spec.GREEN_MID)
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(0.8)
    c.line(62, spec.PAGE_H - 316, 240, spec.PAGE_H - 316)
    c.restoreState()
    T(c, 62, spec.PAGE_H - 340, "Improved First Edition", "SourceSerifItalic", 12.4,
      spec.INK_SOFT)
    T(c, 62, 120, "SADIKOU MOUKODDIM", "SourceSerif-Semi", 12.0, spec.GREEN, 0.6)
    _motif(c, spec.PAGE_W - 250, 60, 210, 210, spec.GOLD_DEEP, 0.22, 21)


def _title_page(bk):
    bk.new_page("none")
    c = bk.c
    c.saveState()
    c.setFillColor(spec.GREEN)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    _motif(c, spec.PAGE_W - 240, 500, 220, 220, spec.GOLD, 0.22, 22)
    L = 62
    T(c, L, spec.PAGE_H - 100, "MYP YEAR 1", "Inter-Semi", 7.0, spec.GOLD, 2.6)
    T(c, L, 560, "Mathematics 1", "Playfair-Display", 52, spec.CREAM, 0.3)
    T(c, L, 522, "Student Coursebook", "SourceSerif", 18, spec.GOLD_PALE)
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(0.8)
    c.line(L, 500, L + 160, 500)
    c.restoreState()
    lines = ["An inquiry-led introduction to number, place value, proportion,",
             "algebra, geometry, measurement, sets and data, built around the",
             "concepts, global contexts and assessment criteria of the",
             "Middle Years Programme.",
             ]
    y = 476
    for ln in lines:
        T(c, L, y, ln, "SourceSerif", 10.4, spec.GOLD_PALE)
        y -= 16
    y -= 20
    T(c, L, y, "IMPROVED FIRST EDITION", "Inter-Semi", 7.0, spec.GOLD, 2.6)
    T(c, L, y - 16, "2026", "Inter-Semi", 7.0, spec.GOLD, 2.6)
    T(c, L, 210, "SADIKOU MOUKODDIM", "SourceSerif-Semi", 15.0, spec.CREAM, 0.6)
    T(c, L, 192, "HEAD OF MATHEMATICS DEPARTMENT  \u00b7  MATHEMATICS TEACHER",
      "Inter-Semi", 6.4, spec.GOLD, 2.1)
    T(c, L, 62, "MYP MATHEMATICS 1  \u00b7  STUDENT COURSEBOOK", "Inter-Semi", 6.2,
      spec.GOLD_PALE, 2.0)


def _imprint(bk):
    bk.new_page("plain")
    c = bk.c
    L = 62
    T(c, L, spec.PAGE_H - 96, "MYP MATHEMATICS 1", "Inter-Semi", 6.8, spec.GOLD_DEEP, 2.4)
    T(c, L, spec.PAGE_H - 118, "Student Coursebook  \u00b7  Improved First Edition",
      "SourceSerifItalic", 11.4, spec.INK_SOFT)
    body = [
        ("Copyright \u00a9 2026 SADIKOU Moukoddim. All rights reserved.", "h"),
        ("No part of this publication may be reproduced, stored in a retrieval system, or "
         "transmitted in any form or by any means \u2014 electronic, mechanical, "
         "photocopying, recording or otherwise \u2014 without prior written permission "
         "from the author, except for brief quotations in reviews and for classroom use "
         "by the purchasing teacher.", "p"),
        ("Author and publisher: SADIKOU Moukoddim, Head of Mathematics Department, "
         "Mathematics Teacher, Category 1.", "p"),
        ("Edition", "h"),
        ("Improved First Edition, 2026. This edition revises the first edition of the "
         "same course: the mathematical scope, chapter sequence and learning outcomes are "
         "unchanged, while the explanations, investigations, worked examples, practice, "
         "illustration and page design have been rebuilt.", "p"),
        ("Independence", "h"),
        ("This is an independent educational publication. It is not published by, "
         "sponsored by, endorsed by or affiliated with the International Baccalaureate "
         "Organization. \u201cIB\u201d, \u201cIBO\u201d and \u201cMYP\u201d are trademarks "
         "of the International Baccalaureate Organization. References to the MYP "
         "framework are provided for curriculum alignment and planning and do not imply "
         "endorsement. Teachers should consult the current official MYP Mathematics "
         "subject guide and their school's programme documentation for authoritative "
         "requirements.", "p"),
        ("Originality", "h"),
        ("All explanatory prose, worked examples, exercises, investigations, diagrams and "
         "illustrations in this book were written or drawn for this edition. The book is "
         "not a reproduction of any published coursebook. Where a concept is standard "
         "mathematics \u2014 place value, equivalent fractions, the angle sum of a "
         "triangle \u2014 the treatment and wording are the author's own.", "p"),
        ("Typefaces", "h"),
        ("Playfair Display (display), Source Serif 4 (text and mathematics) and Inter "
         "(labels and tables), all under the SIL Open Font License 1.1. Mathematical "
         "diagrams were drawn as vector artwork; the contextual illustrations were created "
         "for this edition. Full source and licence details are recorded in the "
         "image-licensing report that accompanies the manuscript.", "p"),
        ("Answers", "h"),
        ("Answers and brief worked solutions to the practice sets, mixed practice and "
         "chapter reviews appear in the answer section at the back of the book. Attempt a "
         "question fully before checking: the value of an answer key lies in comparing "
         "reasoning, not in matching a number.", "p"),
    ]
    y = spec.PAGE_H - 156
    for text, kind in body:
        if kind == "h":
            y -= 12
            T(c, L, y, plain(text), "Inter-Semi", 6.6, spec.GOLD_DEEP, 1.9)
            y -= 14
        else:
            p = style("imp", fontSize=8.5, leading=12.2, textColor=spec.INK_SOFT,
                      hyphenationLang="en_GB")
            from reportlab.platypus import Paragraph
            par = Paragraph(inline(text), p)
            ph = par.wrap(spec.TEXT_W - 40, 1e6)[1]
            par.drawOn(c, L, y - ph)
            y -= ph + 8


# --------------------------------------------------------------- front build
def build_front(bk, reg):
    """Roman-numbered front matter."""
    _half_title(bk)          # ii (page i is the cover)
    _title_page(bk)          # iii
    _imprint(bk)             # iv

    # ---------------------------------------------------------- contents
    bk.new_page("plain")
    p = Pager(bk)
    p.add(Heading("Front matter", "Contents"))
    p.add(Spacer(6))

    fm_entries = [
        ("chapter", 0, "How to use this coursebook", ""),
        ("chapter", 0, "The MYP framework in this course", ""),
        ("chapter", 0, "Assessment criteria in practice", ""),
        ("chapter", 0, "Course map and progression", ""),
        ("chapter", 0, "Notation, working and habits", ""),
    ]
    # front-matter rows reuse the chapter row style
    entries = [e for e in (CONTENTS_ENTRIES or []) if e[0] in ("part", "chapter", "front")]
    if not entries:
        # first pass: render a skeleton so pagination is stable
        entries = []
    p.add(Contents(entries))

    # ------------------------------------------------------ how to use
    bk.new_page("plain")
    reg.record("front", 0, "How to use this coursebook", bk.page_label)
    p = Pager(bk)
    p.add(Heading("Orientation", "How to use this coursebook"))
    p.add(Lead("This is a working book. Expect to write in the margins, test an idea, "
               "compare your method with a classmate's, and return to a question after "
               "your thinking has changed."))
    p.add(Body("Year 1 is where many familiar ideas become precise. You already know how "
               "numbers are written, how shapes are named and how data can be displayed. "
               "This course asks you to look underneath those familiar forms: why a "
               "digit's position changes its value, why equivalent fractions name the same "
               "quantity, why an angle fact must hold for every triangle rather than "
               "merely one drawing.", space_before=6))
    p.add(Body("The book is arranged in five parts. Part I establishes the structure of "
               "the number system and the rules that keep calculation reliable. Part II "
               "develops fractions, decimals and percentages as connected ways of "
               "describing parts of a whole. Part III introduces algebraic thinking "
               "through patterns and balance. Part IV brings together sets, shape and "
               "measurement. Part V examines data, graphs and the claims people make from "
               "them.", space_before=6))
    p.add(Body("Every chapter follows one rhythm, and the rhythm is visible on the page: "
               "Engage, Explore, Explain, Worked Examples, Practice, Investigate and Apply, "
               "Reflect and Consolidate. The stage labels tell you where you are, so that a "
               "lesson can be planned around a stage rather than a page number.",
               space_before=6))
    p.add(DataTable(
        ["Stage", "What you do", "What it is for"],
        [["01 Engage", "Meet a situation, photograph or puzzle.",
          "Give the mathematics a reason to exist."],
         ["02 Explore", "Try something before being told the rule.",
          "Build a conjecture you can test."],
         ["03 Explain", "Read definitions, notation and properties.",
          "Turn the conjecture into a structure you can use."],
         ["04 Worked examples", "Follow reasoning line by line, including checks.",
          "See what a complete answer looks like."],
         ["05 Practice", "Work from fluency to application and extension.",
          "Make the method reliable and portable."],
         ["06 Investigate and apply", "Use mathematics on a real task.",
          "Meet the MYP criteria in a genuine setting."],
         ["07 Reflect", "Summarise, check vocabulary, self-assess.",
          "Know precisely what you can and cannot yet do."]],
        widths=[0.9, 1.6, 1.5], caption="The seven stages of every chapter.",
        space_before=10))

    p.add(Spacer(8))
    p.add(Panel("note", title="How the labels work",
                text="**Definition** boxes state precise meanings. **Key idea** boxes "
                     "connect a method to a larger principle. **Common error** boxes show a "
                     "mistake worth anticipating. **ATL** boxes name a learning skill and "
                     "give a way to practise it. **Criterion** strips name the MYP "
                     "criterion and strands developed by a section.", space_before=6))
    p.add(Panel("atl", title="The exercise tags",
                text="**F Fluency** \u2014 short, deliberate practice to make a method "
                     "accurate and efficient. **R Reasoning** \u2014 explain, compare, "
                     "justify or diagnose an error. **P Problem solving** \u2014 multi-step "
                     "and unfamiliar contexts. **E Extension** \u2014 deeper structure, "
                     "generalisation or a more open task."))
    p.add(Panel("keyidea", title="Three habits that make the book work",
                text="**Estimate first.** Predict the size of an answer before calculating "
                     "it. **Ask what a symbol means.** Every letter, bracket and index is "
                     "doing a job. **Write the check.** A calculation you cannot check is a "
                     "calculation you do not yet trust."))
    p.add(H3("Writing in this book", space_before=12))
    p.add(Body("The wide outer margin is part of the page, not decoration. Use it for a "
               "question you could not finish, a note that a method reminded you of "
               "something, or the reason a step works. When you return to a chapter before "
               "an assessment, the margin is the fastest way back into your own thinking."))
    p.add(DataTable(["When you are stuck", "What to do before asking"], [
        ["The question is unreadable", "Underline the noun the question is asking about; "
                                        "the verb is usually the operation."],
        ["The method is forgotten", "Read the most recent worked example in the same "
                                    "section and copy its first line."],
        ["The answer looks wrong", "Estimate the size first, then check the units and the "
                                    "last step."],
        ["The question is ambiguous", "Write down both readings and say which one you are "
                                      "answering."],
    ], widths=[1.1, 2.2], font_size=8.2, space_before=10))

    # ------------------------------------------------------- MYP framework
    bk.new_page("plain")
    reg.record("front", 0, "The MYP framework in this course", bk.page_label)
    p = Pager(bk)
    p.add(Heading("Framework", "The MYP framework in this course"))
    p.add(Lead("The Middle Years Programme asks students to learn mathematics as a "
               "connected, conceptual and applicable discipline. Concepts organise the "
               "content, contexts give it purpose, and criteria make the quality of "
               "thinking visible."))
    p.add(H3("Key concepts", space_before=8))
    p.add(DataTable(["Key concept", "What it asks in Year 1 mathematics"], [
        ["Form", "What is this number, figure or display made of, and how is it arranged?"],
        ["Logic", "When must a statement be true, and what would count as a "
                  "counterexample?"],
        ["Relationships", "How do quantities, variables and shapes depend on one another?"],
    ], widths=[0.7, 2.6]))
    p.add(H3("Related concepts used in this course"))
    p.add(Body("Quantity, Representation, Approximation, Equivalence, Pattern, "
               "Simplification, Generalisation, Space, Measurement, System, Model and "
               "Change. Each chapter names the two related concepts it develops most "
               "directly, so that the concept is a lens on the content rather than a label "
               "attached to it."))
    p.add(H3("Global contexts"))
    p.add(DataTable(["Global context", "Chapters"], [
        ["Identities and relationships", "4, 8"],
        ["Orientation in space and time", "1, 7"],
        ["Personal and cultural expression", "6"],
        ["Scientific and technical innovation", "2, 9"],
        ["Fairness and development", "3, 5"],
        ["Globalisation and sustainability", "10"],
    ], widths=[1.6, 0.8]))
    p.add(H3("Inquiry"))
    p.add(Body("Each chapter opens with a statement of inquiry, one factual, one conceptual "
               "and one debatable question, and a pathway that shows how the inquiry "
               "develops. A factual question has a settled answer. A conceptual question "
               "requires you to connect ideas. A debatable question has more than one "
               "defensible answer and must be argued."))
    p.add(Panel("atl", title="ATL skills in this course",
                text="Approaches to learning are written in the form the MYP uses: "
                     "\u201cIn order for a student to \u2026, students must \u2026\u201d. "
                     "Every chapter contains at least two ATL boxes: one for a thinking "
                     "skill and one for a self-management, communication or research skill.",
                space_before=6))

    # --------------------------------------------------------- criteria
    bk.new_page("plain")
    reg.record("front", 0, "Assessment criteria in practice", bk.page_label)
    p = Pager(bk)
    p.add(Heading("Assessment", "Assessment criteria in practice"))
    p.add(Lead("MYP mathematics uses four criteria. They describe different qualities of "
               "mathematical work, not four separate syllabuses: a single rich task can "
               "provide evidence for more than one criterion."))
    p.add(DataTable(["Criterion", "What it looks for", "Typical evidence in this book"], [
        ["A \u00b7 Knowing and understanding",
         "Selecting and applying the right mathematics, accurately.",
         "Practice sets, chapter reviews, fluency items."],
        ["B \u00b7 Investigating patterns",
         "Recognising, describing and justifying a pattern, then generalising it.",
         "The numbered investigations, extension items."],
        ["C \u00b7 Communicating",
         "Using notation, language and representations precisely, for an audience.",
         "Explanations, diagrams, mini-tasks written for a named reader."],
        ["D \u00b7 Applying mathematics",
         "Using mathematics in a real context and judging whether the answer is "
         "reasonable.",
         "Real-life applications and criterion-mapped mini-tasks."],
    ], widths=[1.0, 1.5, 1.5], space_before=8))
    p.add(H3("Command words that shape the evidence"))
    p.add(DataTable(["Command word", "What a complete answer contains"], [
        ["State", "The value, name or fact, with no working required."],
        ["Describe", "What happens, in order, with the key features named."],
        ["Explain", "A reason, connected to a property, definition or example."],
        ["Justify", "Evidence: a calculation, a counterexample or a diagram."],
        ["Show that", "A chain of working that ends at the stated result."],
        ["Investigate", "Cases, a pattern, a general rule and a test of that rule."],
        ["Evaluate", "A judgement with stated criteria and a limitation."],
    ], widths=[0.8, 2.5]))
    p.add(Panel("note", title="Formative practice is not a formal assessment",
                text="The exercises in this book build the understanding that assessed "
                     "tasks later require. Marks are not the point of a practice set; a "
                     "question you cannot yet do is information, not a verdict.",
                space_before=8))

    # ------------------------------------------------------- course map
    bk.new_page("plain")
    reg.record("front", 0, "Course map and progression", bk.page_label)
    p = Pager(bk)
    p.add(Heading("Progression", "Course map and progression"))
    p.add(Lead("The ten chapters form a cumulative course. Each chapter names the knowledge "
               "it assumes, the new structure it builds, and the Year 2 territory it "
               "deliberately does not yet enter."))
    p.add(DataTable(["Ch", "Chapter", "Assumes", "Builds"], [
        ["1", "Number systems and place value", "Counting, place value to thousands",
         "Number families, decimals, rounding, estimation"],
        ["2", "Powers, expanded form and order of operations", "Chapter 1",
         "Index notation, squares and roots, order of operations"],
        ["3", "Factors, multiples and primes", "Chapter 1\u20132",
         "Divisibility, prime factorisation, HCF and LCM"],
        ["4", "Fractions and decimals", "Chapters 1\u20133",
         "Equivalence, four operations on fractions, decimal calculation"],
        ["5", "Percentages and applications", "Chapter 4",
         "Percentage of a quantity, increase and decrease, financial contexts"],
        ["6", "Patterns, expressions and equations", "Chapters 1\u20135",
         "Sequences, expressions, simplifying, solving linear equations"],
        ["7", "Lines, angles, triangles and constructions", "Measurement language",
         "Angle facts, triangle and polygon results, ruler and compass work"],
        ["8", "Sets and classification", "Chapter 1",
         "Set notation, Venn diagrams, two-set problems"],
        ["9", "Perimeter, area, surface area and volume", "Chapter 7",
         "Area formulae, circles, nets, volume and capacity"],
        ["10", "Data, tables and graphs", "Chapters 4\u20135",
         "Data types, displays, averages, misleading graphs"],
    ], widths=[0.3, 1.5, 1.1, 1.6], font_size=7.8))
    p.add(Panel("keyidea", title="How the four criteria accumulate",
                text="Criterion A grows as the toolkit grows: by Chapter 10 you are "
                     "selecting among many methods rather than applying one. Criterion B "
                     "appears in every investigation, from counting strings of digits to "
                     "the relationship between a cylinder's radius and its volume. "
                     "Criterion C is practised in every written explanation and every "
                     "diagram. Criterion D appears in each chapter's application, where the "
                     "answer has to be judged as well as calculated.", space_before=8))

    # ---------------------------------------------------------- notation
    bk.new_page("plain")
    reg.record("front", 0, "Notation, working and habits", bk.page_label)
    p = Pager(bk)
    p.add(Heading("Conventions", "Notation, working and habits"))
    p.add(Lead("Clear notation is part of the mathematics. It lets another person follow "
               "your reasoning, and it helps you notice when a claim is not yet precise."))
    p.add(DataTable(["Notation", "Means", "Example"], [
        ["<  >", "is less than / is greater than", "3 < 8,  \u22128 < \u22123"],
        ["\u2264  \u2265", "is at most / is at least", "x \u2264 5"],
        ["\u2248", "is approximately equal to", "48 \u00d7 21 \u2248 1 000"],
        ["\u00d7  \u00f7", "multiplied by, divided by", "24 \u00f7 4 = 6"],
        ["a/b", "a divided by b", "\u00be means 3 \u00f7 4"],
        ["a^{n}", "a raised to the power n", "10^{3} = 1 000"],
        ["\u221a", "square root", "\u221a49 = 7"],
        ["%", "per hundred", "25 % = 0.25 = \u00bc"],
        ["\u2208  \u2209", "is an element of / is not an element of",
         "5 \u2208 `Z` (the integers)"],
        ["\u222a  \u2229", "union / intersection", "A \u222a B"],
        ["\u2220", "angle", "\u2220ABC = 90\u00b0"],
        ["\u2245", "is congruent to", "\u25b3ABC \u2245 \u25b3DEF"],
    ], widths=[0.55, 1.7, 1.35]))
    p.add(H3("Five habits that protect accuracy"))
    p.add(ListBlock([
        "**Align equal signs.** Write one equals sign beneath another so that each line "
        "states a true equality.",
        "**Carry units.** A number without its unit is an incomplete answer in any "
        "measurement question.",
        "**Estimate first.** Write the estimate before the calculation, then compare.",
        "**Show the check.** Substitute back, reverse the operation, or test with a "
        "simpler case.",
        "**Name the rounding.** Say \u201cto the nearest hundred\u201d rather than "
        "silently changing the value.",
    ]))
    p.add(Panel("atl", title="ATL \u00b7 Self-management",
                text="In order for a student to keep a page of working readable, students "
                     "must decide the layout before starting: number the question, align "
                     "the equals signs, leave one line between parts, and box the final "
                     "answer.", space_before=8))
    p.add(Panel("note", title="Reading a mathematics question",
                text="Read it twice. The first reading finds the quantities; the second "
                     "finds the question. Underline the instruction \u2014 calculate, "
                     "estimate, explain, justify \u2014 because the instruction decides what "
                     "a complete answer contains."))
