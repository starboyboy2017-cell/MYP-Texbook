"""Design prototype: six pages used to compare against the original edition."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bookkit import spec, fonts, plates
from bookkit.book import Book
from bookkit.flow import Pager, Spacer, Rule, Stack
from bookkit.blocks import (SectionHead, H3, H4, Lead, Body, ListBlock, Panel,
                            WorkedExample, Practice, PracticeSplit, Figure,
                            Diagram, DataTable, MarginNote)

import diagrams as dg

fonts.register()
OUT = "/tmp/proto.pdf"
b = Book(OUT, title="MYP Mathematics 1 \u2014 Improved First Edition",
         author="SADIKOU Moukoddim")

# ------------------------------------------------------------------ 1. cover
b.pages = 0
b.new_page("none")
plates.cover(b.c, {})

# ------------------------------------------------------- 2. chapter opener
b.new_page("none")
plates.chapter_plate(b.c, dict(
    part="Part I \u00b7 Number, structure and proof", part_numeral="I", chapter_no=1,
    kicker="Number, structure and proof",
    title_lines=["Number systems and", "place value"],
    lead_lines=["Ten digits are enough to write any number we can name.",
                "Their power comes from position: the same symbol can",
                "mean seven, seventy or seven thousandths."],
    key_concept="Form", related=["Quantity", "Representation"],
    context="Orientation in space and time",
    inquiry_lines=["How does a digit's position change its value, and how can we",
                   "describe that structure so precisely that comparisons and",
                   "calculations become reliable?"]))

# --------------------------------------------------- 3. explanation spread
b.part_label = "Part I \u00b7 Number, structure and proof"
b.chapter_label = "Chapter 1 \u00b7 Number systems and place value"
b.new_page("body")
p = Pager(b)

p.add(SectionHead("1.1", "Number systems and the number line",
                  "A \u00b7 i", ["Form", "Representation"]))
p.add(Lead("A number line turns the question \u201cwhich is bigger?\u201d into a question "
           "about position. Everything else in this chapter is a way of writing down what "
           "the line already shows."))

p.add(Body("Mathematicians keep several number families because each one answers a "
           "different question. The counting numbers tell you how many objects there are. "
           "Add zero and you can describe an empty shelf. Add the negatives and you can "
           "describe a debt, a temperature below freezing, or a depth below sea level."))
p.add(Panel("definition", title="The number families",
            text="The **natural numbers** are the counting numbers 1, 2, 3, \u2026  The "
                 "**whole numbers** are the natural numbers together with zero. The "
                 "**integers** are the whole numbers and their negatives: \u2026, \u22123, "
                 "\u22122, \u22121, 0, 1, 2, 3, \u2026"))
p.add(Body("Every integer is also a rational number, because it can be written over 1: "
           "`7` = 7/1 and \u22123 = \u22123/1. Terminating decimals such as 0.25 are "
           "rational too, since 0.25 = 25/100. The families are nested, like boxes inside "
           "boxes: the natural numbers sit inside the whole numbers, which sit inside the "
           "integers, which sit inside the rationals."))
p.note(MarginNote("A number line is not a picture of a number: it is a picture of "
                  "**order**. Once two values sit on it, every comparison between them "
                  "has an answer.", title="WHY IT MATTERS"))
p.add(Diagram(74, dg.number_line, number="Figure 1.1",
              caption="On a horizontal number line, values increase from left to right. "
                      "Negative numbers lie to the left of zero."), wide=True)

p.add(Panel("keyidea", title="Reading the symbols",
            text="\u201c3 < 8\u201d is correct because 3 lies to the left of 8. \u201c\u22128 "
                 "< \u22123\u201d is also correct \u2014 even though 8 is greater than 3 \u2014 "
                 "because \u22128 lies further left. The inequality sign describes position, "
                 "not size alone.", space_before=2))
p.add(Panel("error", title="Reversing a sign when comparing negatives",
            text="A student writes \u22128 > \u22123 because 8 > 3. On the number line "
                 "\u22128 sits to the left of \u22123, so \u22128 < \u22123. Check every "
                 "negative comparison against a sketch of the line."))

# ------------------------------------------------------ 4. worked examples
b.new_page("body")
p = Pager(b)
p.add(SectionHead("1.2", "Place value and the role of zero", "A \u00b7 i, ii",
                  ["Form", "Quantity"]))
p.add(Body("Our system is positional. The digit 3 means three, thirty or three hundred "
           "depending on where it stands, and each move to the left multiplies the value "
           "by ten. Zero is what makes this possible: it holds a place open so that every "
           "other digit keeps its position."))
p.add(Spacer(4))
p.add(Diagram(96, dg.place_value_table, number="Figure 1.2",
              caption="Each position in 3048.76 carries a different value; the point marks "
                      "where values fall below one."), wide=True)

p.add(WorkedExample(
    "1.2.1", "Zero as a placeholder",
    "Write the number \u201cfour thousand and sixty\u201d in digits and explain why a zero "
    "is needed.",
    ["The thousands digit is 4, so the number starts 4\u2009_\u2009_\u2009_.",
     "The hundreds digit is 0 because there is no \u201chundreds\u201d word in the name.",
     "The tens digit is 6 and the ones digit is 0.",
     "Writing 4060 keeps each digit in its correct column: four thousands, no hundreds, "
     "six tens, no ones."],
    answer="4060. Without the zero, 46 would mean four tens and six ones.",
    check="4 \u00d7 1000 + 0 \u00d7 100 + 6 \u00d7 10 + 0 \u00d7 1 = 4060 \u2713"))

p.add(WorkedExample(
    "1.2.2", "Multiplying by ten",
    "Describe what happens to the digits of 3.48 when the number is multiplied by 10 and "
    "by 100.",
    ["\u00d7 10: every digit moves one place to the left, so 3.48 becomes 34.8.",
     "\u00d7 100: every digit moves two places to the left, so 3.48 becomes 348.",
     "The digits themselves never change \u2014 only their positions do."],
    answer="3.48 \u00d7 10 = 34.8 and 3.48 \u00d7 100 = 348.",
    check="Estimate first: 3.5 \u00d7 10 \u2248 35, and 34.8 is close \u2713"))

# ------------------------------------------------------------ 5. practice
b.new_page("body")
p = Pager(b)
p.add(Practice("1.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
    dict(q="Write each number in digits: (a) two thousand and seven (b) nine hundred and "
           "forty (c) six thousand, two hundred and ten.", tag="F"),
    dict(q="State the value of the digit 7 in each number: (a) 2714 (b) 507 (c) 7.35 "
           "(d) 12.07.", tag="F"),
    dict(q="Write 6045 in expanded form in two different ways.", tag="F"),
    dict(q="Insert the missing digit: 5\u2009_\u20092 is between 5300 and 5400.", tag="R"),
    dict(q="A student says 0.7 is larger than 0.65 because 7 > 65. Explain the error and "
           "give the correct comparison.", tag="R"),
    dict(q="A museum ticket costs 12.50. Estimate the cost of 18 tickets, then calculate "
           "it exactly and compare.", tag="P"),
    dict(q="The label on a crate reads 2.4 tonnes. Write this in kilograms and explain "
           "which position the decimal point moved to.", tag="P"),
    dict(q="Find two different three-digit numbers that use the digits 4, 0 and 9 once "
           "each. Which is larger, and why?", tag="E"),
    dict(q="Explain why \u201c3 thousandths\u201d is written 0.003 rather than 0.300.",
         tag="E"),
]))

p.add(Panel("atl", title="ATL \u00b7 Critical thinking",
            text="In order for a student to compare decimals reliably, students must "
                 "line up the place-value columns before comparing, rather than comparing "
                 "the digits from left to right as if they were whole numbers."))

# ------------------------------------------- 6. investigation / application
b.new_page("wide")
p = Pager(b)
p.add(SectionHead("Investigation 1", "How many numbers can a given number of digits write?",
                  None, ["Form", "Quantity"]))
p.add(Body("Work in pairs. You will count possibilities systematically and look for a "
           "pattern rather than listing every case."))
p.add(DataTable(["Digits allowed", "Cannot start with zero", "May start with zero"],
                [["1 digit", "9", "10"],
                 ["2 digits", "90", "100"],
                 ["3 digits", "900", "1 000"],
                 ["4 digits", "9 000", "10 000"]],
                widths=[1.2, 1.4, 1.4], number="Table 1.1",
                caption="Counts of whole numbers that can be written with each number of "
                        "digits."), wide=True)
p.add(H3("Your investigation"))
p.add(ListBlock([
    "Copy the table and check the first two rows by listing the numbers directly.",
    "Describe in words how each row is obtained from the row above it.",
    "Predict the 7-digit entries before you calculate them.",
    "Write a rule for the number of whole numbers with `n` digits when zero is allowed, "
    "and a second rule for when it is not.",
    "Explain why the two rules differ by exactly 1 at every row.",
], ordered=True))
p.add(Panel("keyidea", title="Conjecture",
            text="With zero allowed there are 10^{n} numbers using at most `n` digits. "
                 "Without a leading zero the count is 9 \u00d7 10^{n\u22121}. The difference "
                 "of 1 is the single number 0.", space_before=8))


b.save()
print("pages:", b.pages)
