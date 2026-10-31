"""Front matter: half title, title page, imprint, contents, orientation pages.

The original first edition opened with a cover, a quiet half title, a full
title page, an imprint, then five orientation pages before the first chapter.
This edition keeps that order and that restraint: the front matter is set on
paper, the title page alone carries the navy field, and the contents page
borrows its rules and letterspaced labels directly from the original.
"""
import os

from bookkit import spec, typeset
from bookkit.blocks import (PageTitle, Statement, DataTable, Panel, ListBlock,
                            H3, H4, Body, Lead, Card, ChipRow)
from bookkit.flow import Flow, Pager, Spacer, Rule, Stack
from bookkit.markup import plain, inline, style
from bookkit.plates import _line, _grid, motif_proportion, motif_data
from reportlab.platypus import Paragraph

import render2 as R2

T = typeset.draw
L, R = spec.MARGIN_OUTER, spec.PAGE_W - spec.MARGIN_OUTER

CONTENTS = None      # filled on the second pass


# --------------------------------------------------------------------- plates
def half_title(c):
    c.saveState()
    c.setFillColor(spec.PAPER)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    T(c, L, spec.PAGE_H - 120, "MYP MATHEMATICS 2", "Inter-Semi", 7.4, spec.TERRACOTTA,
      2.6)
    T(c, L, spec.PAGE_H - 236, "MYP Mathematics 2", "Playfair", 40, spec.INK)
    T(c, L, spec.PAGE_H - 282, "Student Coursebook", "PlayfairItalic", 22,
      spec.INK_LABEL)
    _line(c, L, spec.PAGE_H - 310, L + 210, spec.PAGE_H - 310, 0.8, 1.0,
          colour=spec.GOLD)
    T(c, L, spec.PAGE_H - 356, "SADIKOU MOUKODDIM", "Inter-Semi", 8.0, spec.INK_LABEL,
      2.2)
    T(c, L, spec.PAGE_H - 380, "FIRST EDITION", "Inter", 7.0, spec.INK_MUTE, 2.0)
    T(c, L, 96, "An inquiry-led course in number, algebra, geometry, probability "
                "and statistics", "SourceSerifItalic", 9.6, spec.INK_MUTE)


def title_page(c):
    c.saveState()
    c.setFillColor(spec.NAVY)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    _grid(c, R - 200, 120, 200, 200, 22, 0.14)
    motif_proportion(c, R - 200, 120, 200, 200)

    T(c, L, spec.PAGE_H - 110, "MYP MATHEMATICS", "Inter-Semi", 7.4, spec.GOLD, 2.8)
    T(c, L, spec.PAGE_H - 124, "YEAR 2", "Inter-Semi", 7.4, spec.GOLD, 2.8)
    T(c, R, spec.PAGE_H - 110, "STUDENT COURSEBOOK", "Inter-Semi", 6.8, spec.GOLD_PALE,
      2.4, "right")
    T(c, R, spec.PAGE_H - 124, "FIRST EDITION \u00b7 2026", "Inter-Semi", 6.8,
      spec.GOLD_PALE, 2.4, "right")

    size = typeset.fit("Mathematics 2", "Playfair-Display", 68, R - L)
    T(c, L, spec.PAGE_H - 250, "MYP", "Inter-Semi", 10.0, spec.GOLD, 4.0)
    T(c, L, spec.PAGE_H - 330, "Mathematics 2", "Playfair-Display", size, spec.CREAM,
      0.3)
    _line(c, L, spec.PAGE_H - 356, L + 150, spec.PAGE_H - 356, 1.0, 0.9,
          colour=spec.GOLD)
    T(c, L, spec.PAGE_H - 388, "Student Coursebook", "SourceSerif", 19.0, spec.CREAM)

    body = ["An inquiry-led course in number, algebra, geometry, probability",
            "and statistics, built around the concepts, contexts and",
            "assessment criteria of the Middle Years Programme."]
    y = spec.PAGE_H - 428
    for ln in body:
        T(c, L, y, ln, "SourceSerifItalic", 11.4, spec.GOLD_PALE)
        y -= 17.0

    _line(c, L, 176, R, 176, 0.55, 0.55, colour=spec.GOLD)
    T(c, L, 150, "SADIKOU MOUKODDIM", "SourceSerif-Semi", 14.0, spec.CREAM, 0.4)
    T(c, L, 132, "HEAD OF MATHEMATICS DEPARTMENT  \u00b7  MATHEMATICS TEACHER  "
                 "\u00b7  CATEGORY 1", "Inter", 6.4, spec.GOLD_PALE, 1.1)
    T(c, L, 88, "An independent educational publication", "Inter", 6.6, spec.GOLD)


def imprint(c, page_label):
    c.saveState()
    c.setFillColor(spec.PAPER)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    T(c, L, spec.PAGE_H - 150, "MYP Mathematics 2 \u2014 Student Coursebook",
      "Playfair", 15.0, spec.INK)
    T(c, L, spec.PAGE_H - 170, "IMPROVED FIRST EDITION \u00b7 2026", "Inter-Semi", 6.4,
      spec.TERRACOTTA, 2.2)
    _line(c, L, spec.PAGE_H - 190, R, spec.PAGE_H - 190, 0.6, 1.0, colour=spec.RULE)

    paras = [
        "Copyright \u00a9 2026 SADIKOU Moukoddim. All rights reserved. No part of "
        "this publication may be reproduced, stored in a retrieval system, or "
        "transmitted in any form or by any means \u2014 electronic, mechanical, "
        "photocopying, recording or otherwise \u2014 without prior written permission "
        "from the author, except for brief quotations in reviews and for classroom "
        "use by the purchasing teacher.",
        "Author: SADIKOU Moukoddim \u00b7 Head of Mathematics Department \u00b7 "
        "Mathematics Teacher \u00b7 Category 1.",
        "Independence statement. This is an independent educational publication. It "
        "is not published by, sponsored by, endorsed by or affiliated with the "
        "International Baccalaureate Organization. \u201cIB\u201d, \u201cIBO\u201d and "
        "\u201cMYP\u201d are trademarks of the International Baccalaureate "
        "Organization. References to the MYP framework are provided for curriculum "
        "alignment and planning; they do not imply endorsement. Teachers should "
        "consult the current official MYP Mathematics guide for authoritative "
        "statements of aims, objectives and assessment criteria.",
        "About this edition. This is an improved first edition of the same course, "
        "not a new course. The curriculum scope, the sequence of chapters, the "
        "learning objectives and the level of difficulty are unchanged. What has "
        "changed is the finish: one display face used consistently, one baseline "
        "grid, mirrored folios and running heads, numbered and captioned figures and "
        "tables, and real photographs and original diagrams where the first printing "
        "had none.",
        "Typographic note. The text is set in Source Serif 4 (Frank Grie\u00dfhammer, "
        "SIL Open Font License 1.1), the display type in Playfair Display (Claus "
        "Eggers S\u00f8rensen, SIL Open Font License 1.1) and the labels, tables and "
        "captions in Inter (Rasmus Andersson, SIL Open Font License 1.1). "
        "Mathematical symbols are drawn from the same three families; a small subset "
        "of DejaVu Sans supplies the few signs they lack (also SIL OFL).",
        "Illustrations and photographs are listed, with their sources and licensing, "
        "in the image register supplied with this edition. Diagrams are original "
        "vector drawings created for this book.",
        "Printed and distributed by the author for classroom use. No ISBN is "
        "claimed, and no publisher, barcode or official endorsement is implied.",
    ]
    y = spec.PAGE_H - 214
    for p in paras:
        par = Paragraph(inline(p), style("imp", fontSize=8.2, leading=12.4,
                                         textColor=spec.INK_SOFT, alignment=0))
        h = par.wrap(R - L, 1e6)[1]
        par.drawOn(c, L, y - h)
        y -= h + 12
    T(c, L, 96, "MYP MATHEMATICS 2  \u00b7  STUDENT COURSEBOOK  \u00b7  IMPROVED FIRST "
                "EDITION", "Inter-Semi", 6.2, spec.INK_MUTE, 1.7)
    T(c, R, 78, page_label, "Inter-Semi", 7.8, spec.TERRACOTTA, 0, "right")


# ------------------------------------------------------------------- contents
class Contents(Flow):
    """Two-column-free, rule-led contents page in the original's manner."""

    def __init__(self, entries):
        self.entries = entries
        self.h = 0

    def _row(self, e):
        return {"part": 54, "chapter": 36, "section": 16.0, "front": 19.0,
                "fronthead": 34}.get(e[0], 16.0)

    splittable = True

    def wrap(self, w):
        self._hs = [self._row(e) for e in self.entries]
        self.h = sum(self._hs)
        return self.h

    def min_split(self):
        return 120

    def split(self, w, avail):
        self.wrap(w)
        used, cut = 0.0, 0
        for h in self._hs:
            if used + h > avail:
                break
            used += h
            cut += 1
        if cut == 0 or cut >= len(self.entries):
            return None
        a = Contents(self.entries[:cut])
        b = Contents(self.entries[cut:])
        return a, b

    def draw(self, c, x, top, w):
        y = top
        for e, h in zip(self.entries, self._hs):
            kind, ch, title, label = e
            if kind in ("part", "fronthead"):
                y -= 18
                T(c, x, y, (title if kind == "fronthead" else title).upper(),
                  "Inter-Semi", 7.2, spec.TERRACOTTA, 2.4)
                _line(c, x, y - 8, x + w, y - 8, 0.8, 1.0, colour=spec.GOLD)
                y -= 28
            elif kind == "chapter":
                y -= 17
                T(c, x, y, str(ch), "SourceSerif-Semi", 13.0, spec.TERRACOTTA)
                T(c, x + 24, y - 1, title, "Playfair-Med", 14.2, spec.INK)
                T(c, x + w, y, label, "Inter-Semi", 8.0, spec.INK, 0, "right")
                y -= 14
            elif kind == "front":
                T(c, x + 8, y - 12, title, "SourceSerif", 9.8, spec.INK)
                T(c, x + w, y - 12, label, "Inter", 7.6, spec.INK_MUTE, 0, "right")
                y -= h
            else:
                T(c, x + 24, y - 11.4, title, "SourceSerif", 9.0, spec.INK_SOFT)
                T(c, x + w, y - 11.4, label, "Inter", 7.4, spec.INK_MUTE, 0, "right")
                y -= h


def build_front(bk):
    # half title (page 2)
    bk.new_page("plain")
    half_title(bk.c)
    # title page (page 3)
    bk.new_page("none")
    title_page(bk.c)
    # imprint (page 4)
    bk.new_page("plain")
    imprint(bk.c, "4")

    # contents (pages 5-6)
    bk.new_page("body")
    p = Pager(bk)
    p.add(PageTitle("Contents", "MYP Mathematics 2 \u00b7 Student Coursebook"))
    p.add(Contents(CONTENTS or []))
    bk.save_contents_page = True
    return bk


# ---------------------------------------------------------------- orientation
def build_orientation(bk, labels=None):
    labels = labels if labels is not None else {}
    p = Pager(bk)

    # ----- how to use this coursebook
    bk.new_page("body")
    p = Pager(bk)
    labels["How to use this coursebook"] = bk.page_label
    p.add(PageTitle("How to use this coursebook", "Orientation"))
    p.add(Lead("This is a working book, not a book of answers to memorise. Read with "
               "a pencil in hand, test ideas, write down conjectures, and return to "
               "your reasoning when it needs repair."))
    p.add(Spacer(8))
    p.add(Body("The course is arranged in four parts. Each part gathers chapters that "
               "share a way of thinking: comparing quantities; generalising with "
               "symbols; describing space and measurement; and making decisions from "
               "uncertainty and data. The chapters build on one another, but each is "
               "also designed to be entered on its own after the prerequisite check."))
    p.add(Body("Every chapter follows the same inquiry rhythm. You meet a situation "
               "that mathematics can clarify. You frame a question. You build the "
               "concepts and representations needed to answer it. You practise until "
               "the method is reliable. Then you investigate, communicate, apply and "
               "reflect. The answer key at the back supports this cycle; it should "
               "confirm your reasoning, not replace it.", space_before=8))
    p.add(H3("Mathematical habits this course builds"))
    p.add(DataTable(
        ["Habit", "What it looks like in your book"],
        [["Name the quantities", "Before calculating, write what each number counts "
                                 "and in which unit."],
         ["Draw the relationship", "A tape diagram, table, number line or sketch "
                                   "before a formula."],
         ["Estimate first", "A rough answer written beside the question, to catch a "
                            "slip later."],
         ["Check by another route", "Substitute back, recombine a share, or compute a "
                                    "second way."],
         ["Say why", "One sentence of reasoning after a result, in your own "
                     "words."],
         ["Record confusion", "A question mark in the margin where an idea is still "
                              "unsteady."]],
        widths=[1.0, 2.4],
        caption="Six habits that every chapter assumes and every practice set "
                "rehearses."))
    p.add(Spacer(6))
    p.add(Panel("keyidea", title="How the labels work",
                text="**Definition** panels state the precise meaning of a term. "
                     "**Key idea** panels connect a method to the principle it "
                     "rests on. **Common error** panels show a mistake in a "
                     "student's voice, then the correction. **ATL** panels name an "
                     "approaches-to-learning skill and how it is used here. "
                     "**Criterion** panels link the work to the four MYP mathematics "
                     "assessment criteria."))

    # ----- exercise types + study cycle (facing page)
    bk.new_page("body")
    p = Pager(bk)
    p.add(H3("Exercise types"))
    p.add(Body("Every practice item carries a letter in a small box. The letter is "
               "not a difficulty rating; it names the kind of thinking the item "
               "asks for."))
    p.add(DataTable(["", "Type", "What it asks you to do"], [
        ["F", "Fluency", "Short, deliberate practice to make a method accurate and "
                         "automatic."],
        ["R", "Reasoning", "Explain, compare, justify, find a counterexample or "
                           "diagnose an error."],
        ["P", "Problem solving", "Multi-step and unfamiliar contexts that require "
                                 "choosing a method."],
        ["E", "Extension", "Deeper structure, generalisation or an open task."],
    ], widths=[0.25, 0.85, 2.5], caption="The four exercise types used throughout "
                                        "the course."))
    p.add(Spacer(8))
    p.add(H3("A four-step study cycle"))
    p.add(DataTable(["Step", "What to do"], [
        ["1 \u00b7 Read", "Restate the question in your own words; name what is "
                          "given, what is asked and which units apply."],
        ["2 \u00b7 Attempt", "Cover the worked solution. Commit to a method, even a "
                             "partial one, before comparing."],
        ["3 \u00b7 Compare", "If your answer differs, find the first line where the "
                             "reasoning diverges, not the last."],
        ["4 \u00b7 Name the change", "Write one sentence about what you will do "
                                     "differently on the next similar task."],
    ], widths=[0.8, 2.7], caption="The cycle that turns practice into learning."))
    p.add(Spacer(8))
    p.add(Panel("atl", title="ATL \u00b7 Self-management",
                text="In order for a student to improve between two practice sets, "
                     "students must keep a short record of the errors they made and "
                     "return to it before the next set, rather than starting again "
                     "from a blank page."))

    # ----- the MYP framework
    bk.new_page("body")
    p = Pager(bk)
    labels["The MYP framework in this course"] = bk.page_label
    p.add(PageTitle("The MYP framework in this course", "The programme in practice"))
    p.add(Lead("Key concepts, related concepts, global contexts and statements of "
               "inquiry are not decoration on a chapter. They decide which questions "
               "are worth asking."))
    p.add(Spacer(6))
    p.add(Body("Each chapter opens with a planner page that states the concepts and "
               "context it uses, the statement of inquiry that holds the chapter "
               "together, and the inquiry questions \u2014 factual, conceptual and "
               "debatable \u2014 that the work should let you answer."))
    p.add(H3("Key concepts used in Year 2 mathematics"))
    p.add(DataTable(["Key concept", "Where it appears in this book"], [
        ["Form", "Chapter 1: a ratio's written form; chapter 8: the form of a solid."],
        ["Relationships", "Chapter 2: proportionality; chapter 7: angle and side "
                          "relationships."],
        ["Logic", "Chapters 4 and 11: signs, rules and the logic of a claim."],
        ["Change", "Chapters 6 and 9: sequences, transformations and growth."],
    ], widths=[0.8, 2.7]))
    p.add(Spacer(6))
    p.add(H3("Global contexts in this course"))
    p.add(DataTable(["Global context", "Chapter context"], [
        ["Fairness and development", "Chapters 1 and 11: fair shares, fair claims."],
        ["Orientation in space and time", "Chapters 2, 7 and 9: maps, plans and "
                                          "transformation."],
        ["Scientific and technical innovation", "Chapters 3, 8 and 10: rates, "
                                                "containers, simulation."],
        ["Personal and cultural expression", "Chapters 6 and 9: pattern, ornament and "
                                             "design."],
        ["Identities and relationships", "Chapter 5: describing an unknown and "
                                         "choosing a plan."],
    ], widths=[1.1, 2.4]))
    p.add(Spacer(6))
    p.add(Panel("criteria", title="In order for a student to use a global context "
                                  "well\u2026",
                text="In order for a student to connect mathematics to a global "
                     "context, students must be able to name the real decision the "
                     "mathematics informs, choose quantities that carry it, and "
                     "explain what the answer means for that decision \u2014 not "
                     "only what number it produced."))

    bk.new_page("body")
    p = Pager(bk)
    p.add(H3("Statements of inquiry, and how to read them"))
    p.add(Body("A statement of inquiry is one sentence that names the concept, the "
               "context and the direction of the relationship between them. It is "
               "written so that it can be tested. In this book you will find it at "
               "the head of each chapter's planner page; by the end of the chapter "
               "you should be able to explain it in your own words and give one "
               "example that supports it."))
    p.add(Spacer(6))
    p.add(Panel("keyidea", title="Example, chapter 1",
                text="\u201cEquivalent ratios preserve a multiplicative relationship, "
                     "so one comparison can organise fair shares and scaled "
                     "quantities across different totals and units.\u201d Read it as "
                     "a claim with two halves: the first says what is preserved; the "
                     "second says what that preservation is good for."))
    p.add(H3("Approaches to learning (ATL) in mathematics"))
    p.add(DataTable(["ATL skill cluster", "How it is used in this book"], [
        ["Thinking", "Testing a conjecture with three cases and a counterexample."],
        ["Communication", "Choosing a representation and defending it to a reader."],
        ["Research", "Judging whether a statistic or a claim is well founded."],
        ["Self-management", "Planning a multi-step problem and checking the result."],
        ["Social", "Comparing methods in a pair and agreeing on the more efficient."],
    ], widths=[1.0, 2.5]))
    p.add(Spacer(6))
    p.add(Body("Each chapter includes at least one ATL panel that names the skill it "
               "develops and states the task in the framework's own sentence "
               "structure: \u201cIn order for a student to \u2026, students "
               "must \u2026\u201d."))

    # ----- criteria in practice
    bk.new_page("body")
    p = Pager(bk)
    labels["Assessment criteria in practice"] = bk.page_label
    p.add(PageTitle("Assessment criteria in practice", "Assessment"))
    p.add(Lead("Four criteria describe what a student of MYP mathematics should be able "
               "to do. Each chapter names the strands it develops and the evidence "
               "that will be looked for."))
    p.add(Spacer(6))
    p.add(DataTable(["Criterion", "What it asks", "How this book gives evidence"], [
        ["A \u00b7 Knowing and understanding",
         "Select and apply mathematics: knowledge, skills, procedures.",
         "Fluency sets; worked examples with a check; short criterion-A tasks."],
        ["B \u00b7 Investigating patterns",
         "Describe patterns, select and apply tools, test and justify "
         "generalisations.",
         "An investigation card in every chapter, with a conjecture stage."],
        ["C \u00b7 Communicating",
         "Use appropriate forms of mathematical representation; communicate "
         "coherently.",
         "Explain-it questions; notation checks; the vocabulary panel."],
        ["D \u00b7 Applying mathematics in real-life contexts",
         "Identify relevant elements, select tools, justify the degree of accuracy, "
         "interpret results.",
         "A criterion-mapped mini-task in every chapter, with a hand-in checklist."],
    ], widths=[1.05, 1.55, 1.9], caption="The four MYP mathematics criteria as they "
                                        "are used in this course."))
    p.add(Spacer(8))
    p.add(Panel("note", title="Strands are named, not scored",
                text="An item is labelled with the criterion and strands it exercises "
                     "\u2014 for example \u201cCriterion C \u00b7 iii, iv\u201d. The "
                     "book does not award levels: achievement levels are a "
                     "professional judgement made against the current official "
                     "criteria, using the evidence a student produces."))
    p.add(Spacer(6))
    p.add(H3("Support, core and extension"))
    p.add(Body("Each practice set is banded: the support items rehearse the method in "
               "the form it was taught; the core items require a choice; the "
               "extension items ask for generalisation or a second representation. "
               "The banding is printed beside the practice heading so that a student "
               "can aim deliberately rather than guess."))
    p.add(Spacer(6))
    p.add(Panel("atl", title="ATL \u00b7 Critical thinking",
                text="In order for a student to judge which practice items to attempt "
                     "first, students must read the tag, recall what that kind of "
                     "thinking demands, and choose a deliberate starting point."))

    # ----- pathways: one page setting out the three bands
    bk.new_page("body")
    p = Pager(bk)
    labels["Three pathways through the course"] = bk.page_label
    p.add(PageTitle("Three pathways through the course",
                    "Differentiation"))
    p.add(Lead("Every chapter can be worked at three depths without changing the "
               "mathematics it teaches. The pathway decides how much a student "
               "generalises, not which topics they meet."))
    p.add(Spacer(6))
    p.add(Body("The three bands are printed beside every practice heading as a "
               "range of question numbers, and each question carries a letter for "
               "the kind of thinking it asks for. The two systems answer different "
               "questions: the band says *how far to go*, the letter says *what "
               "kind of work this is*. A support-route student still meets "
               "reasoning questions; a core-route student is not expected to reach "
               "the generalisation items without help."))
    p.add(Spacer(8))
    p.add(DataTable(["Pathway", "What the student does", "What to look for in the book"], [
        ["Support",
         "Rehearses the method in the form it was taught, with the worked "
         "example open, then repeats it on a near-identical question.",
         "The F items, the first two worked examples of each section, and the "
         "\u201cTry this first\u201d line in the COMMON ERROR panel."],
        ["Core",
         "Chooses a method, applies it to an unfamiliar context, and writes one "
         "sentence of justification.",
         "The P items, all worked examples, the investigation card, and the "
         "mixed practice at the end of the chapter."],
        ["Extension",
         "Generalises, compares two representations, or constructs a "
         "counterexample; often writes the reasoning for someone else.",
         "The E items, the second investigation card, and the Criterion D task "
         "with its hand-in checklist."],
    ], widths=[0.7, 1.75, 1.75], caption="The three pathways and where each one "
                                        "lives on the page."))
    p.add(Spacer(8))
    p.add(H3("Choosing a route through a chapter"))
    p.add(DataTable(["If this is true of the student\u2026", "Start here"], [
        ["The prerequisite check has gaps",
         "Read the worked examples, do the support items in sections x.1 and x.2, "
         "then attempt the first investigation with a partner."],
        ["The methods are reliable but the contexts are new",
         "Skip straight to the core items and the mixed practice; use the "
         "summary page as a checklist before the Criterion D task."],
        ["The methods and the contexts are secure",
         "Work the extension items and both investigations; then write the "
         "Criterion D task as a short report in the form a reader would need."],
    ], widths=[1.55, 2.65]))
    p.add(Spacer(8))
    p.add(Panel("note", title="What is not differentiated",
                text="The concepts, the global context, the statement of inquiry "
                     "and the criteria are the same for every student. A support "
                     "route is not a reduced curriculum; it is the same curriculum "
                     "travelled with more support and fewer generalisations."))

    # ----- pathways: chapter by chapter
    p.add(H3("The three pathways, chapter by chapter"))
    p.add(Body("The table names, for each chapter, the idea a support route should "
               "secure, the choice a core route should be able to make, and the "
               "generalisation an extension route should reach."))
    p.add(Spacer(4))
    p.add(DataTable(["Ch", "Support: secure this", "Core: choose this",
                     "Extension: generalise this"], [
        ["1", "Simplify a ratio by dividing both parts",
         "Share a total in a given ratio and check the parts recombine",
         "Explain why equivalent ratios describe the same comparison"],
        ["2", "Read a constant of proportionality from a table",
         "Solve a proportion in either direction, with units",
         "Derive a relationship from two data points and test it on a third"],
        ["3", "Find a unit rate by dividing",
         "Compare two offers by a common unit and say which is better value",
         "Combine rates, including a rate that works against another"],
        ["4", "Order integers on a number line",
         "Add, subtract, multiply and divide signed numbers with a reason",
         "Justify the sign rules from a pattern rather than a mnemonic"],
        ["5", "Substitute into an expression",
         "Expand a bracket and solve a two-step equation",
         "Show that two expressions are or are not equivalent, and prove it"],
        ["6", "Continue a sequence by its term-to-term rule",
         "Find the `n`th term of a linear sequence and use it",
         "Model a context with a linear rule and interpret the gradient"],
        ["7", "Name angles and use the straight-line fact",
         "Find missing angles and areas in a composite figure",
         "Decide which facts a figure does and does not determine"],
        ["8", "Count faces, edges and vertices; find a volume",
         "Find surface area of a prism or cylinder and explain each face",
         "Compare two packagings that use the same material differently"],
        ["9", "Read and plot coordinates",
         "Carry out and describe a single transformation",
         "Combine two transformations and describe the single equivalent one"],
        ["10", "Write a probability as a fraction",
         "Use a sample space or tree diagram for two events",
         "Decide whether a set of trials is evidence of bias, and why"],
        ["11", "Find the mean and range of a small list",
         "Compare two distributions using an average and a measure of spread",
         "Judge a published claim from the display that supports it"],
    ], widths=[0.25, 1.35, 1.6, 1.65], font_size=7.8,
        caption="A route through each chapter at three depths."))
    p.add(Body("Three rules keep the pathways honest in use. Decide the route "
               "after the prerequisite check, never before it, because the check "
               "exists to make the decision evidence-based. Keep every student on "
               "the same concept and the same context: the route changes the "
               "amount of structure, not the mathematics. And move a student "
               "between routes at a section boundary rather than inside a practice "
               "set, so that the evidence from a whole section stays comparable.",
               space_before=10))

    # ----- command terms
    bk.new_page("body")
    p = Pager(bk)
    labels["Command terms used in this book"] = bk.page_label
    p.add(PageTitle("Command terms used in this book", "Assessment language"))
    p.add(Lead("A command term tells you what a complete answer contains. Marks are "
               "lost more often by answering a different verb than by calculating "
               "wrongly."))
    p.add(Spacer(4))
    p.add(DataTable(["Command term", "A complete answer"], [
        ["State", "The value or fact, with its unit. No working is required, but a "
                  "wrong value scores nothing."],
        ["Describe", "The features of the object or result in order, in words, with "
                     "the values named."],
        ["Explain", "A reason that connects the result to a fact, definition or "
                    "earlier step: because \u2026, so \u2026"],
        ["Calculate", "The working, with the substitution shown, and the result in "
                      "the unit the question used."],
        ["Determine", "The value reached by a stated method, with the choice of "
                      "method made explicit."],
        ["Show that", "A chain of steps that ends at the given result; the final "
                      "line must match the statement exactly."],
        ["Verify", "A substitution or second route that confirms a stated claim."],
        ["Estimate", "A reasoned approximate value, with the rounding or benchmark "
                     "used named."],
        ["Compare", "Both values or distributions described, then a judgement that "
                    "says on what basis they differ."],
        ["Justify", "Evidence for a claim: a counterexample, a test on the general "
                    "case, or a property that must hold."],
        ["Construct / Draw", "Accurate work with instruments; labelled vertices, "
                             "lengths and angles."],
        ["Sketch", "The essential shape and labelled key features; not to scale."],
        ["Solve", "The value of the unknown, with the equation shown at each "
                  "stage and the answer checked."],
        ["Interpret", "What the number means in the context, in a sentence a "
                      "non-mathematician could act on."],
        ["Generalise", "A rule in symbols that holds for every case, justified "
                       "rather than illustrated by one example."],
        ["Investigate", "A systematic set of cases, a conjecture, a test, and a "
                        "statement of what the evidence supports."],
    ], widths=[0.85, 3.35], font_size=7.9,
        caption="The command terms used in questions, investigations and the "
                "Criterion D tasks."))
    p.add(Spacer(8))
    p.add(Panel("keyidea", title="One verb, one shape of answer",
                text="Before writing, underline the command term. If it says "
                     "**explain**, a bare number cannot earn the mark; if it says "
                     "**state**, a page of working does not earn more. The worked "
                     "examples model the shape of each term, so the shortest route "
                     "to a full answer is to copy that shape."))

    # ----- course map
    bk.new_page("body")
    p = Pager(bk)
    labels["Course map and progression"] = bk.page_label
    p.add(PageTitle("Course map and progression", "Progression"))
    p.add(Lead("Eleven chapters form a cumulative course. Each chapter names the "
               "knowledge it assumes, the structure it builds, and the territory "
               "that Year 2 deliberately does not enter."))
    p.add(Spacer(6))
    p.add(DataTable(["Ch", "Chapter", "Assumes", "Builds"], [
        ["1", "Ratios and equivalent ratios", "Equivalent fractions, units",
         "Ratio language, simplest form, sharing, comparison"],
        ["2", "Proportional reasoning", "Chapter 1",
         "Constant of proportionality, solving proportions, scale"],
        ["3", "Rates and unit rates", "Chapters 1\u20132",
         "Unit rates, best buys, speed, density, flow"],
        ["4", "Integers and operations", "Chapter 1",
         "Order on the number line, signed arithmetic, order of operations"],
        ["5", "Algebraic expressions and equations", "Chapter 4",
         "Notation, substitution, equivalent expressions, linear equations"],
        ["6", "Numerical patterns and generalisation", "Chapter 5",
         "Term-to-term rules, nth term, function machines, linear graphs"],
        ["7", "2D geometry: angles, perimeter and area", "Measurement language",
         "Angle relationships, triangles, quadrilaterals, circles, composites"],
        ["8", "3D geometry: solids, surface area and volume", "Chapter 7",
         "Nets, surface area, volume, capacity, composite solids"],
        ["9", "Transformations and symmetry", "Coordinates, chapter 7",
         "Translation, reflection, rotation, enlargement, tessellation"],
        ["10", "Probability and simulation", "Fractions, chapter 3",
         "Sample spaces, theoretical and experimental probability, fairness"],
        ["11", "Univariate data", "Chapters 3 and 10",
         "Frequency tables, averages, quartiles, box plots, claims"],
    ], widths=[0.25, 1.25, 0.85, 2.0], font_size=7.8,
        caption="The eleven chapters, what each assumes and what each builds."))
    p.add(Spacer(6))
    p.add(Panel("keyidea", title="How the four criteria accumulate",
                text="Criterion A grows as the toolkit grows: by chapter 11 a student "
                     "is choosing among several methods, not applying one. Criterion "
                     "B appears in every investigation, from the scaling rule of "
                     "chapter 1 to the relationship between a cylinder's radius and "
                     "its volume. Criterion C is practised in every written "
                     "explanation. Criterion D appears in every chapter's "
                     "application, where the answer has to be judged as well as "
                     "calculated."))

    # ----- notation and working
    bk.new_page("body")
    p = Pager(bk)
    labels["Notation, working and habits"] = bk.page_label
    p.add(PageTitle("Notation, working and habits", "Mathematical language"))
    p.add(Lead("Notation is not a code to memorise; it is a way of making meaning "
               "unambiguous. These are the conventions this book uses."))
    p.add(Spacer(6))
    p.add(DataTable(["Notation", "Read as", "Used for"], [
        ["`a` : `b`", "the ratio of a to b", "comparing two quantities "
                                              "multiplicatively"],
        ["`a`/\u00a0`b`", "a divided by b", "a fraction of a whole, or a quotient for "
                                            "comparison"],
        ["`k`", "the constant of proportionality", "`y` = `k x` for a proportional "
                                                   "relationship"],
        ["\u2248", "is approximately equal to", "a rounded or estimated value"],
        ["\u00d7, \u00f7, +, \u2212", "the four operations", "with the order of "
                                                             "operations applied"],
        ["\u2220`ABC`", "angle ABC", "the angle at vertex B"],
        ["\u00b0", "degrees", "the measure of an angle"],
        ["\u03c0", "pi", "the ratio of circumference to diameter, \u2248 3.142"],
        ["`P`(`A`)", "the probability of event A", "a value from 0 to 1"],
        ["\u00a3, $, km, kg, L, cm\u00b3", "units", "always written with the number"],
    ], widths=[0.9, 1.35, 1.9], caption="Notation used throughout the course."))
    p.add(Spacer(8))
    p.add(H3("Five habits that prevent most lost marks"))
    p.add(ListBlock([
        "Write the unit on every quantity, including intermediate results.",
        "Show the substitution before the arithmetic: \u201c`y` = 3(4) + 1\u201d, "
        "then the value.",
        "Keep equals signs aligned down the page; one equals sign per line means one "
        "true statement.",
        "Do not round in the middle of a calculation. Keep full accuracy and round at "
        "the end.",
        "Answer the question that was asked: a length, a cost, a comparison or a "
        "decision, in the unit the question used."], ordered=True))
    p.add(Spacer(6))
    p.add(Panel("error", title="Rounding too early",
                text="A student computes 7 \u00f7 3 \u2248 2.3, then multiplies by 3 "
                     "and reports 6.9. The exact value is 7. Round only when the "
                     "value is reported, and keep the exact form in the working."))

    # ----- calculator and rounding
    bk.new_page("body")
    p = Pager(bk)
    labels["Calculators, rounding and accuracy"] = bk.page_label
    p.add(PageTitle("Calculators, rounding and accuracy",
                    "Working accurately"))
    p.add(Lead("A calculator answers the arithmetic you typed, not the question you "
               "meant. These are the conventions this book uses."))
    p.add(Spacer(4))
    p.add(H3("How the questions expect an answer to be given"))
    p.add(DataTable(["The question says", "Give the answer", "Example"], [
        ["\u201cgive your answer to 1 decimal place\u201d",
         "One digit after the decimal point, rounded from the exact value",
         "7.46 \u2192 7.5"],
        ["\u201cto 2 significant figures\u201d",
         "Two meaningful digits, counting from the first non-zero digit",
         "0.004 837 \u2192 0.0048"],
        ["\u201cto the nearest whole number\u201d / \u201cnearest penny\u201d",
         "Rounded at the last step only",
         "\u00a312.376 \u2192 \u00a312.38"],
        ["\u201cleave your answer in exact form\u201d",
         "A fraction, a surd or \u03c0, not a decimal",
         "\u03c0`r`\u00b2, 22/7, \u221a50"],
        ["no instruction and the value is not exact",
         "Two decimal places, with the exact form shown first in the working",
         "\u2248 3.14"],
    ], widths=[1.45, 1.55, 0.9], font_size=8.0,
        caption="The rounding instructions used in the practice sets."))
    p.add(Spacer(6))
    p.add(H3("Three habits with a calculator"))
    p.add(Body("**Estimate first.** Write a rough value before the keystrokes: 4.9 "
               "\u00d7 21 is about 5 \u00d7 20 = 100, so a display of 1 029 is a "
               "keystroke error, not a surprise."))
    p.add(Body("**Keep the exact value.** Rounding at every step turns a small error "
               "into a wrong answer: 3 \u00d7 2.33 = 6.99, while 3 \u00d7 7/3 = 7.",
               space_before=6))
    p.add(Body("**Use the sign key for a negative number.** (\u22123)\u00b2 is 9, "
               "while \u22123\u00b2 is \u22129; the two keystroke sequences "
               "differ and the display will not warn you.", space_before=6))
    p.add(Spacer(4))
    p.add(Panel("keyidea", title="What the calculator is for, and what it is not",
                text="A calculator removes the arithmetic, not the reasoning. It is "
                     "expected in the chapters on circles, solids, probability and "
                     "data, where numbers are messy by design; it is never a "
                     "substitute for choosing the operation, stating the units or "
                     "checking that the size of the answer is plausible. A student "
                     "who computes the area of a circle of radius 4.5 cm as "
                     "63.61725124 is arithmetically right and wrong as an answer: "
                     "to 1 decimal place it is 63.6 cm\u00b2."))
    return labels
