"""Chapter 1 - Number systems and place value."""
from bookkit import spec
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.plates import chapter_plate
from bookkit.flow import Spacer
import diagrams as dg
from helpers import (section, lead, body, h3, h4, lst, panel, atl, we, practice, q,
                     fig, diag, table, note, gap, rule, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
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
                   "calculations become reliable?"])

TITLE = "Number systems and place value"
SHORT = "Number systems and place value"


def build(bk, p):
    from bookkit.flow import Pager
    reset_counters(1)
    # ------------------------------------------------------------ planner
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER",
                "The whole chapter in one view: concepts, context and the evidence "
                "that will be looked for."))
    p.add(Spacer(10))
    p.add(DataTable(
        ["Statement of inquiry",
         "A number's written form is an organised system of positions: a small set of "
         "digits can represent any magnitude when place and zero are used consistently, "
         "and the way we record a number decides how precisely we can compare, calculate "
         "and communicate it."],
        [], widths=[1, 3.2], font_size=9.2, first_col_bold=True, stripe=False))
    gap(p, 12)

    from bookkit.blocks import Panel
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Form.** A number's written form is not one "
                     "symbol but an organised arrangement of positions; changing a "
                     "position changes the quantity it records.\n"
                     "**Related \u00b7 Quantity.** Place value lets ten digits stand for "
                     "any size, while rounding records an appropriate level of precision.\n"
                     "**Related \u00b7 Representation.** The same value can appear as "
                     "words, digits, an expanded sum, a point on a number line or a "
                     "rounded claim.", space_before=4))
    p.add(Panel("note", title="Global context \u00b7 Orientation in space and time",
                text="Exploration: how different cultures have recorded quantity, and why "
                     "the invention of a place-value system with zero changed what numbers "
                     "could do. Every tally system works; only a positional system scales."))
    gap(p, 10)
    h3(p, "Inquiry questions")
    lst(p, [
        "**Factual:** What is the value of a digit in a given position, and how does "
        "multiplying or dividing by ten change a number's digits?",
        "**Conceptual:** Why is zero essential in a place-value system, and how can one "
        "number have several equivalent representations?",
        "**Debatable:** When a number is reported as \u201cabout 2 000\u201d, is the "
        "result more useful than the exact count?",
    ])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Read, write, compare, round and rewrite integers and decimals; choose sensible "
         "accuracy."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate how many numbers a given number of digits can write; generalise the "
         "count."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Record working with correct notation; explain how place value works to a reader "
         "who has not met it."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Design a community noticeboard that reports counts and costs at a sensible "
         "accuracy."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 8)
    atl(p, "In order for a student to judge whether a reported figure is precise enough, "
           "students must identify what each digit contributes and decide which digits "
           "still carry meaning in the context.", "ATL \u00b7 Critical thinking")

    # ---------------------------------------------------- intentions page
    # (continues on the planner page rather than starting a new leaf)
    p = Pager(bk)
    p.add(Stage("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"))
    p.add(Spacer(8))
    table(p, ["You are learning to", "You have succeeded when you can"], [
        ["Understand how natural numbers, whole numbers and integers are related.",
         "Classify a given number correctly and give an example that belongs to one set "
         "but not the other."],
        ["Know that the value of a digit depends on its place in a base-ten number.",
         "State the value of any digit in a whole number or decimal, including zeros."],
        ["Write numbers in expanded form and return to standard form.",
         "Move between 3 048, 3 \u00d7 1000 + 0 \u00d7 100 + 4 \u00d7 10 + 8 and words "
         "without error."],
        ["Compare and order integers and decimals using place value.",
         "Place five mixed values in order and justify each decision with one sentence."],
        ["Round to a stated place and choose sensible accuracy in context.",
         "Round to a named place and explain why a different place would be misleading."],
        ["Estimate before calculating and judge whether an answer is reasonable.",
         "Produce an estimate within about 10 % and use it to catch an error."],
    ], widths=[1.5, 1.9])
    gap(p, 8)
    h3(p, "Inquiry pathway for this chapter")
    table(p, ["Stage", "What happens"], [
        ["1 \u00b7 Context", "A market stall and a community noticeboard report quantities "
         "in many different forms."],
        ["2 \u00b7 Question", "What does each digit in a displayed number actually "
         "contribute?"],
        ["3 \u00b7 Concept", "Base-ten place value, zero as a placeholder, precision."],
        ["4 \u00b7 Investigation", "Count the numbers that different digit-lengths can "
         "write; generalise the count."],
        ["5 \u00b7 Communication", "Expanded form, number lines and justified rounding."],
        ["6 \u00b7 Reflection", "When does extra precision help, and when does it "
         "mislead?"],
    ], widths=[1.0, 2.4])
    gap(p, 8)
    p.add(Panel("note", title="Prerequisite check \u00b7 10 minutes, no calculator",
                items=["Write \u201cfour thousand and sixty\u201d using digits.",
                       "Which is greater, 3.5 or 3.45? Explain in one sentence.",
                       "Calculate 7 \u00d7 8 and 56 \u00f7 7.",
                       "What is 100 more than 2 950?",
                       "Write \u00be as a decimal.",
                       "Put 0.6, 0.06 and 0.66 in order from least to greatest."],
                ordered=True))
    body(p, "If more than two answers are incorrect, review place value to thousands and "
            "simple fractions of a whole before continuing. The answers, with the reasoning "
            "for each, are in the answer section.")

    # ------------------------------------------------------------- 1.1
    # the engage stage continues on the same page rather than starting a new leaf
    p.add(Stage("03", "ENGAGE", "A morning at the market, and a noticeboard that has to "
                                "be read by everybody."))
    body(p, "The trader at the next stall has three boxes of tomatoes: one labelled "
            "\u201c120\u201d, one labelled \u201c1 200\u201d and one labelled \u201c12.00\u201d. "
            "A customer reads all three as \u201ctwelve\u201d. She is wrong about at least "
            "two of them, and the trader loses money either way. Nothing about the digits "
            "changed. Only their positions did.")
    gap(p, 4)
    body(p, "That small scene is the whole chapter. Our number system does not invent a new "
            "symbol for every size. It reuses ten symbols and lets position do the work. "
            "Understand position, and you can read any number in the market, on a meter, on "
            "a bank statement or on a medicine bottle.")
    fig(p, "ch01_plate_a_banner.jpg",
        "A market stall organises quantity before anyone writes a number: produce is "
        "stacked in rectangular arrays, weights are nested by size, and the counting frame "
        "records position. Place value formalises what the stall already does.", wide=True)

    p.add(Stage("04", "EXPLORE", "Before any definitions, find the pattern in your own "
                                 "writing."))
    body(p, "Write the number 3 048.76 on a strip of paper. Now carry out these changes "
            "and write what happens to the digits each time: multiply by 10; multiply by "
            "100; divide by 10; divide by 100. Do not use a calculator.")
    lst(p, [
        "What happens to the digits themselves?",
        "What happens to the position of every digit relative to the decimal point?",
        "Which digit never changes its value, and why?",
        "Predict what happens if you multiply by 1 000. Test your prediction.",
    ], ordered=True)
    panel(p, "keyidea", title="What you should have noticed",
          text="The digits are unchanged in every case. Only their positions move. "
               "Multiplying by 10 moves every digit one place to the left; dividing by 10 "
               "moves every digit one place to the right. The decimal point stays where it "
               "is \u2014 it marks the boundary between whole values and parts of one.")

    # ---------------------------------------------------------- 1.1 explain
    section(p, "1.1", "Number systems and the number line", "A \u00b7 i",
            ["Form", "Representation"])
    lead(p, "A number line turns \u201cwhich is bigger?\u201d into a question about "
            "position. Everything else in this chapter is a way of writing down what the "
            "line already shows.")
    body(p, "Mathematicians keep several number families because each one answers a "
            "different question. The counting numbers tell you how many objects there are. "
            "Add zero and you can describe an empty shelf. Add the negatives and you can "
            "describe a debt, a temperature below freezing, or a depth below sea level.")
    panel(p, "definition", title="The number families",
          text="The **natural numbers** are the counting numbers 1, 2, 3, 4, \u2026  The "
               "**whole numbers** are the natural numbers together with zero: 0, 1, 2, 3, "
               "\u2026  The **integers** are the whole numbers and their negatives: \u2026, "
               "\u22123, \u22122, \u22121, 0, 1, 2, 3, \u2026")
    body(p, "Every integer is also a rational number, because it can be written over 1: "
            "`7` = 7/1 and \u22123 = \u22123/1. Terminating decimals such as 0.25 are "
            "rational too, since 0.25 = 25/100. The families are nested, like boxes inside "
            "boxes: the natural numbers sit inside the whole numbers, which sit inside the "
            "integers, which sit inside the rationals.")
    note(p, "WHY IT MATTERS", "A number line is not a picture of a number: it is a picture "
                              "of **order**. Once two values sit on it, every comparison "
                              "between them has an answer.")
    diag(p, 74, dg.number_line, "On a horizontal number line, values increase from left to "
                                "right. Negative numbers lie to the left of zero; positive "
                                "numbers lie to the right. Distance from zero gives "
                                "magnitude, direction gives sign.", wide=True)
    body(p, "A number line is more than a display device. It gives a shared order to every "
            "integer, fraction and decimal. To compare two values, locate both: the one "
            "further to the right is greater. That rule never fails, which is why it is "
            "worth carrying a mental number line for the rest of your mathematical life.")
    panel(p, "keyidea", title="Reading the symbols",
          text="The symbols < and > describe position, not size alone. \u201c3 < 8\u201d is "
               "correct because 3 lies to the left of 8. \u201c\u22128 < \u22123\u201d is "
               "also correct \u2014 even though 8 is greater than 3 \u2014 because "
               "\u22128 lies further left. Reversing the symbol reverses the claim.")
    panel(p, "error", title="Reversing a sign when comparing negatives",
          text="A student writes \u22128 > \u22123 because 8 > 3. On the number line "
               "\u22128 sits to the left of \u22123, so \u22128 < \u22123. Check every "
               "negative comparison against a sketch of the line, not against the size of "
               "the digits.")
    h3(p, "Working with the line")
    lst(p, [
        "**Distance from zero** is the magnitude. \u22128 and 8 are equally far from zero; "
        "they are different numbers because their directions differ.",
        "**Between any two values** there is another value. Between 3 and 4 lies 3.5; "
        "between 3.5 and 3.6 lies 3.55. This is why decimals can always be refined.",
        "**Inequalities** read left to right like a sentence: \u22125 < \u22122 < 0 < 3.",
    ])
    practice(p, "1.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 7\u20139", [
        q("Write down the value of (a) the number 4 more than \u22126, (b) the number 9 less "
          "than 2.", "F"),
        q("Copy and complete: \u22127 \u2026 \u22123 using <, > or =.", "F"),
        q("List the integers greater than \u22124 and less than 2.", "F"),
        q("Draw a number line from \u22126 to 6 and mark \u22124.5, \u22121, 0.5 and 5.",
          "F"),
        q("Which is greater: \u22122.5 or \u22122.05? Justify your answer using the line.",
          "R"),
        q("A submarine is at \u221240 m and rises 15 m. A second submarine is at \u221222 m "
          "and dives 10 m. Which is deeper, and by how much?", "P"),
        q("Explain why \u22123 is smaller than \u22122 even though 3 is larger than 2.",
          "R"),
        q("Find two integers whose sum is \u22125 and whose difference is 7.", "E"),
        q("The temperature was \u22123 \u00b0C at 06:00 and 5 \u00b0C at midday. Describe "
          "the change in two different ways, one using subtraction and one using a number "
          "line.", "E"),
    ])

    # --------------------------------------------------------------- 1.2
    section(p, "1.2", "Place value and the role of zero", "A \u00b7 i, ii",
            ["Form", "Quantity"])
    body(p, "Our system is positional. The digit 3 means three, thirty or three hundred "
            "depending on where it stands, and each move to the left multiplies the value "
            "by ten. Zero is what makes this possible: it holds a place open so that every "
            "other digit keeps its position.")
    diag(p, 96, dg.place_value_table, "Each position in 3 048.76 carries a different "
                                      "value; the point marks where values fall below one.",
         wide=True)
    body(p, "Read the table from the right. The ones column is worth 1; every column to "
            "its left is worth ten times as much. Moving right from the point, each column "
            "is worth one tenth as much. A table that works this way can be extended "
            "indefinitely in either direction, which is why no number is ever too large or "
            "too small to write.")
    panel(p, "definition", title="Place value",
          text="In a base-ten number, the value of a digit is the digit multiplied by ten "
               "raised to the power of its position from the decimal point. The number "
               "3 048.76 therefore means 3 \u00d7 1000 + 0 \u00d7 100 + 4 \u00d7 10 + "
               "8 \u00d7 1 + 7 \u00d7 0.1 + 6 \u00d7 0.01.")
    h3(p, "Why zero is not \u201cnothing\u201d")
    body(p, "Compare 305, 35 and 3.05. All three use the digits 3 and 5 only. The zero in "
            "305 keeps the 3 in the hundreds column and the 5 in the ones column, forcing "
            "an empty tens column. In 3.05 the zero holds the tenths column open so that "
            "the 5 lands in the hundredths. Remove the zero and the number changes "
            "completely \u2014 the digits have not changed, but every value they carry has.")
    panel(p, "error", title="Deleting an \u201cunimportant\u201d zero",
          text="Writing 4.5 for 4.05, or 4 500 for 4 005, is a place-value error, not a "
               "slip of the pen. Test any suspicious zero by asking: which column does it "
               "hold open? If deleting it moves another digit, the zero is doing work.")
    we(p, "1.2.1", "Zero as a placeholder",
       "Write the number \u201cfour thousand and sixty\u201d in digits, and explain why a "
       "zero is needed.",
       ["The thousands digit is 4, so the number begins 4 _ _ _.",
        "There is no \u201chundreds\u201d in the name, so the hundreds digit is 0.",
        "The tens digit is 6 and the ones digit is 0.",
        "Writing 4 060 keeps every digit in its correct column: four thousands, no "
        "hundreds, six tens, no ones."],
       answer="4 060. Without the zero, 46 would mean four tens and six ones.",
       check="4 \u00d7 1000 + 0 \u00d7 100 + 6 \u00d7 10 + 0 \u00d7 1 = 4 060 \u2713")
    we(p, "1.2.2", "Multiplying and dividing by powers of ten",
       "Describe what happens to the digits of 3.48 when the number is multiplied by 10, "
       "multiplied by 100 and divided by 10.",
       ["\u00d7 10: every digit moves one place to the left, so 3.48 becomes 34.8.",
        "\u00d7 100: every digit moves two places to the left, so 3.48 becomes 348.",
        "\u00f7 10: every digit moves one place to the right, so 3.48 becomes 0.348.",
        "In each case the digits are unchanged; only their positions relative to the point "
        "move."],
       answer="34.8, 348 and 0.348 respectively.",
       check="Estimate: 3.5 \u00d7 10 \u2248 35 and 34.8 is close \u2713")
    practice(p, "1.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Write in digits: (a) two thousand and seven (b) nine hundred and forty "
          "(c) six thousand, two hundred and ten.", "F"),
        q("State the value of the digit 7 in each number: (a) 2 714 (b) 507 (c) 7.35 "
          "(d) 12.07.", "F"),
        q("Write 6 045 in expanded form in two different ways.", "F"),
        q("Insert the missing digit: 5 \u2009_\u2009 2 is between 5 300 and 5 400.", "R"),
        q("A student says 0.7 is larger than 0.65 because 7 > 65. Explain the error and "
          "give the correct comparison.", "R"),
        q("A museum ticket costs 12.50. Estimate the cost of 18 tickets, then calculate it "
          "exactly and compare the two results.", "P"),
        q("A crate is labelled 2.4 tonnes. Write this in kilograms and state which position "
          "the decimal point moved to.", "P"),
        q("Find two different three-digit numbers that use 4, 0 and 9 exactly once each. "
          "Which is larger, and why?", "E"),
        q("Explain why \u201cthree thousandths\u201d is written 0.003 rather than 0.300.",
          "E"),
    ])

    # --------------------------------------------------------------- 1.3
    section(p, "1.3", "Expanded form and equivalent representations", "A \u00b7 i, ii",
            ["Representation", "Form"])
    body(p, "Expanded form unpacks a number into the sum of its column values. It is not a "
            "different number, only a different way of writing the same one, and it makes "
            "the structure visible: every zero in the original disappears into a "
            "multiplication by zero, and every digit shows exactly what it contributes.")
    diag(p, 82, dg.expanded_form_strip, "3 048 written as the sum of its column values. "
                                        "Each column contributes digit \u00d7 value.",
         wide=True)
    body(p, "Three equivalent representations of the same quantity:")
    lst(p, ["**Words:** three thousand and forty-eight.",
            "**Digits:** 3 048.",
            "**Expanded:** 3 \u00d7 1000 + 0 \u00d7 100 + 4 \u00d7 10 + 8 \u00d7 1, or "
            "3 000 + 40 + 8."])
    panel(p, "definition", title="Equivalent representations",
          text="Two representations are equivalent when they name exactly the same value. "
               "3 048, 3 000 + 40 + 8, 3 048.0 and \u201cthree thousand and forty-eight\u201d "
               "are all equivalent; 3 480 is not, however similar it looks.")
    we(p, "1.3.1", "From expanded form back to digits",
       "Write 5 \u00d7 10 000 + 0 \u00d7 1000 + 2 \u00d7 100 + 9 \u00d7 1 + 3 \u00d7 0.01 "
       "as a single number.",
       ["List the columns the expression uses: ten-thousands, thousands, hundreds, ones, "
        "hundredths.",
        "The thousands column contributes nothing, so it must be held open by a zero.",
        "The tenths column is empty too, so it also needs a zero.",
        "Assemble the digits in order: 5 0 2 0 9 . 0 3."],
       answer="50 209.03",
       check="Read back: fifty thousand, two hundred and nine, and three hundredths \u2713")
    we(p, "1.3.2", "Spotting a false equivalence",
       "A student claims 4 \u00d7 100 + 7 \u00d7 10 + 3 \u00d7 0.1 = 473. Is the claim "
       "correct?",
       ["Evaluate each term: 400, 70 and 0.3.",
        "Add: 400 + 70 + 0.3 = 470.3.",
        "473 would need 3 \u00d7 1, not 3 \u00d7 0.1."],
       answer="The claim is false. The correct value is 470.3.",
       check="Estimate: the answer must lie between 470 and 471 \u2713")
    practice(p, "1.3", "SUPPORT 1\u20133  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Write in expanded form: (a) 8 502 (b) 7.04 (c) 60.5.", "F"),
        q("Write as a single number: (a) 9 000 + 300 + 7 (b) 2 \u00d7 10 + 5 \u00d7 0.1.",
          "F"),
        q("Write 30 407 in words and in expanded form.", "F"),
        q("Which is larger, 6 \u00d7 100 + 4 \u00d7 0.1 or 604? Explain.", "R"),
        q("Find the mistake: 2 030 = 2 \u00d7 1000 + 3 \u00d7 10. Correct it.", "R"),
        q("A receipt reads 12 \u00d7 100 + 5 \u00d7 1 + 9 \u00d7 0.01. Write the amount in "
          "currency and explain why a zero is needed after the decimal point.", "P"),
        q("Write a four-digit number and a four-decimal-place number that use the digits 1, "
          "2, 3, 4 once each and have the smallest possible value.", "E"),
        q("Explain why expanded form makes rounding easier, using 4 876 as an example.", "E"),
    ])

    # --------------------------------------------------------------- 1.4
    section(p, "1.4", "Comparing, ordering and rounding", "A \u00b7 ii, iii",
            ["Quantity", "Form"])
    body(p, "Comparing decimals by digit length is the most common place-value error. 0.65 "
            "is not larger than 0.7 merely because it has more digits: 0.65 means six "
            "tenths and five hundredths; 0.7 means seven tenths. Line the decimal points "
            "up, fill empty columns with zeros, and compare like with like.")
    panel(p, "keyidea", title="A reliable comparison routine",
          text="1. Write both numbers with the decimal points aligned, filling empty "
               "columns with zeros: 0.70 and 0.65. 2. Compare the columns from left to "
               "right. 3. Stop at the first difference \u2014 that column decides. Here "
               "7 > 6 in the tenths column, so 0.70 > 0.65.")
    diag(p, 96, dg.rounding_line, "Rounding 348 to the nearest ten. The number sits between "
                                  "340 and 350; the midpoint 345 decides which way it goes.",
         wide=True)
    panel(p, "definition", title="Rounding",
          text="To round to a stated place, find the digit in that place and look at the "
               "digit immediately to its right. If that digit is 5 or more, increase the "
               "place digit by 1; otherwise leave it. Replace every digit to the right of "
               "the place with zeros (or drop them after the decimal point).")
    we(p, "1.4.1", "Rounding to a named place",
       "Round 3 847.265 to (a) the nearest thousand (b) the nearest ten (c) two decimal "
       "places.",
       ["(a) The thousands digit is 3; the next digit is 8, so round up: 4 000.",
        "(b) The tens digit is 4; the next digit is 7, so round up: 3 850.",
        "(c) Keep two decimal places; the third digit is 5, so round up: 3 847.27."],
       answer="(a) 4 000  (b) 3 850  (c) 3 847.27",
       check="Each answer is closer to the original than the neighbouring rounded value "
             "\u2713")
    we(p, "1.4.2", "Ordering a mixed set",
       "Write 0.7, 0.07, 0.707 and 0.77 in order from least to greatest.",
       ["Give every number three decimal places: 0.700, 0.070, 0.707, 0.770.",
        "Compare tenths: 0 is smallest, so 0.070 comes first.",
        "The remaining three all have 7 tenths; compare hundredths: 0, 0 and 7, so 0.700 "
        "and 0.707 are next.",
        "Compare thousandths of those two: 0 < 7, then 0.770 is largest."],
       answer="0.07 < 0.7 < 0.707 < 0.77",
       check="Four numbers, four positions, no repeats \u2713")
    practice(p, "1.4", "SUPPORT 1\u20135  \u00b7  CORE 4\u20138  \u00b7  EXTENSION 8\u20139", [
        q("Insert < or >: (a) 0.6 \u2026 0.58 (b) 2.07 \u2026 2.7 (c) \u22123.5 \u2026 "
          "\u22123.05.", "F"),
        q("Round to the nearest whole number: (a) 7.4 (b) 12.8 (c) 0.62.", "F"),
        q("Round 45 678 to the nearest ten, hundred and thousand.", "F"),
        q("Order from least to greatest: 3.4, 3.04, 3.44, 3.404.", "F"),
        q("Round 9.996 to two decimal places. Explain why the whole-number part changes.",
          "R"),
        q("A runner's time is recorded as 12.36 s. Round it to one decimal place and "
          "explain what information is lost.", "P"),
        q("Give a number that rounds to 5.6 to one decimal place but not to 5.60 to two "
          "decimal places.", "R"),
        q("The population of a town is 48 512. Write two different rounded versions and "
          "state a context in which each would be appropriate.", "P"),
        q("Is it possible for a number to round to 100 and also to 0.1? Explain.", "E"),
    ])

    # --------------------------------------------------------------- 1.5
    section(p, "1.5", "Estimation and sensible accuracy", "A \u00b7 iii  \u00b7  D \u00b7 i",
            ["Quantity", "Approximation"])
    body(p, "An estimate is not a guess. It is a deliberately simpler calculation whose "
            "answer is close enough to be useful and rough enough to be done in your head. "
            "Estimates do real work: they tell you whether a calculator answer is plausible "
            "before you trust it.")
    panel(p, "keyidea", title="Round, calculate, adjust",
          text="Round each number to one significant figure, do the simplified calculation, "
               "then adjust for the direction of your rounding. 48 \u00d7 21 \u2248 50 "
               "\u00d7 20 = 1 000. Because both numbers were rounded up, the exact answer "
               "must be a little below 1 000: 1 008.")
    we(p, "1.5.1", "Estimating before calculating",
       "A school orders 19 boxes of exercise books. Each box holds 48 books. Estimate the "
       "total, then calculate it exactly.",
       ["Round: 19 \u2248 20 and 48 \u2248 50.",
        "Estimate: 20 \u00d7 50 = 1 000 books.",
        "Exact: 19 \u00d7 48 = 19 \u00d7 (50 \u2212 2) = 950 \u2212 38 = 912.",
        "The exact answer is a little below the estimate, as predicted."],
       answer="Estimate 1 000; exact 912.",
       check="912 is within 10 % of 1 000 \u2713")
    panel(p, "error", title="Reporting more precision than you have",
          text="A student measures a desk as 1.2 m and reports its area as 1.44 m\u00b2. "
               "The measurement is accurate to the nearest 0.1 m, so the area is only "
               "meaningful to about one decimal place: 1.4 m\u00b2. Extra digits are not "
               "extra accuracy; they are a claim you cannot support.")
    h3(p, "Choosing a sensible level of accuracy")
    lst(p, ["**Money** is usually reported to the nearest 0.01, because that is the "
            "smallest unit in use.",
            "**Populations and attendance** are usually reported to the nearest ten, "
            "hundred or thousand.",
            "**Measurements** should be reported to the precision of the instrument, not "
            "beyond it.",
            "**Intermediate calculations** should keep more digits than the final answer, "
            "so that rounding errors do not accumulate."])
    practice(p, "1.5", "SUPPORT 1\u20133  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Estimate: (a) 29 \u00d7 41 (b) 612 \u00f7 19 (c) 98 + 203 + 397.", "F"),
        q("Estimate 4.9 \u00d7 20.2 and then calculate it exactly.", "F"),
        q("A packet holds 24 pens. Estimate the number of packets needed for 500 pens.",
          "F"),
        q("Explain why 3 987 \u00d7 0.51 is roughly 2 000, without calculating it.", "R"),
        q("A student calculates 5.2 \u00d7 3.1 = 161.2. Use an estimate to show the answer "
          "is wrong and give the correct value.", "R"),
        q("A community noticeboard reports attendances of 247, 1 083 and 96. Round each to "
          "a sensible accuracy and explain your choices.", "P"),
        q("A tank holds 1 250 litres. A pump delivers 18 litres a minute. Estimate the "
          "time to fill it, then calculate it to the nearest minute.", "P"),
        q("Describe a situation in which rounding a number makes it less useful, and "
          "explain why.", "E"),
        q("Estimate (a) 8.1 \u00d7 4.9 (b) 3 950 \u00f7 19 (c) 0.48 \u00d7 61.", "F"),
        q("A school orders 312 books at 4.95 each. Estimate the total cost, then say "
          "whether a calculator answer of 1 544.40 is plausible.", "R"),
        q("Round 46 738 to the nearest (a) ten (b) hundred (c) thousand, and state which "
          "is most useful for a newspaper headline.", "R"),
        q("A car travels 148 km in 2.4 hours. Estimate the average speed, then calculate "
          "it to one decimal place.", "P"),
    ])

    # ------------------------------------------------- application + inv
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("05", "INVESTIGATE", "Count the possibilities, then generalise."))
    section(p, "Investigation 1", "How many numbers can a given number of digits write?",
            None, ["Form", "Quantity"])
    body(p, "Work in pairs. You will count possibilities systematically and look for a "
            "pattern rather than listing every case. A whole number may not begin with "
            "zero, because 007 is simply 7.")
    table(p, ["Digits used", "No leading zero", "Leading zero allowed", "Difference"], [
        ["1", "9", "10", "1"],
        ["2", "90", "100", "10"],
        ["3", "900", "1 000", "100"],
        ["4", "9 000", "10 000", "1 000"],
    ], widths=[1.1, 1.2, 1.3, 1.0],
        caption="Counts of whole numbers that can be written with exactly this many digits.")
    h3(p, "Your investigation")
    lst(p, [
        "Check the first two rows by listing the numbers directly.",
        "Describe in words how each row is obtained from the row above it.",
        "Predict the seven-digit entries before you calculate them.",
        "Write a rule for the count when `n` digits are allowed, both with and without a "
        "leading zero.",
        "Explain why the two counts differ by exactly 10^{n\u22121}.",
        "Test your rule for `n` = 1 and `n` = 2, then state whether it holds for every "
        "whole number `n`.",
    ], ordered=True)
    panel(p, "keyidea", title="Conjecture to test",
          text="With zero allowed there are 10^{n} strings of `n` digits. Without a leading "
               "zero there are 9 \u00d7 10^{n\u22121}. The difference, 10^{n\u22121}, is "
               "exactly the number of strings that begin with zero \u2014 the same count "
               "for `n \u2212 1` digits.")
    atl(p, "In order for a student to generalise a counting pattern, students must move "
           "from listing cases to describing the operation that produces each case, and "
           "then test the description against an unfamiliar case.", "ATL \u00b7 Transfer")
    gap(p, 10)
    p.add(Stage("06", "APPLY", "A task that leaves the page and goes into a community."))
    section(p, "Real-life application", "Numbers for a community noticeboard", "D \u00b7 i\u2013iv",
            ["Quantity", "Representation"])
    body(p, "A neighbourhood association is putting up a noticeboard. It has to report "
            "four things: the number of households registered, the total collected for a "
            "repair fund, the cost of one repair and the percentage of the target reached. "
            "The board will be read from several metres away, by people in a hurry.")
    lst(p, ["Collected: 486 350 units of currency. Target: 600 000.",
            "Households registered: 1 284. Repairs completed: 37 of 45.",
            "One repair costs 12 500."], ordered=False)
    h3(p, "Your task")
    lst(p, [
        "Decide the accuracy at which each figure should be shown, and justify each choice "
        "in one sentence.",
        "Rewrite each figure at that accuracy without losing its meaning.",
        "Compute the percentage of the target reached, to a sensible accuracy.",
        "Explain why showing 486 350 next to a rounded target of 600 000 would be "
        "inconsistent.",
        "Draft the four figures as they would appear on the board, then ask someone outside "
        "your class to read them back to you.",
    ], ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Identify the relevant elements of the real-life situation.",
                 "Select and apply appropriate mathematical strategies.",
                 "Justify the degree of accuracy chosen.",
                 "Evaluate whether the board communicates what it intended."])
    gap(p, 10)
    p.add(Stage("07", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "The noticeboard card", "C \u00b7 ii, iii  \u00b7  D \u00b7 ii", [])
    body(p, "**Context.** The association wants a single card, no larger than A5, that "
            "explains place value to a reader who has never thought about it. It will be "
            "pinned beside the noticeboard.")
    body(p, "**Product.** A card with no more than 120 words of explanation, one diagram "
            "and one worked example, readable from about one metre.")
    lst(p, [
        "State what place value is in one sentence, using 3 048 as your example.",
        "Show 3 048 in expanded form and explain what the zero is doing.",
        "Include a diagram that makes the columns visible.",
        "Work one example of rounding, naming the place each time.",
        "Explain, in no more than two sentences, why 0.7 is larger than 0.65.",
        "Ask a classmate to use the card to round 27 486 to the nearest hundred. Record "
        "whether they succeed, then revise one part of the card.",
        "Evaluate the card: one strength, one limitation and one change for a younger "
        "reader.",
    ], ordered=True)
    criteria_panel(p,
                   a="ii, iii: accurate place-value statements and correct expanded form.",
                   c="ii, iii: precise language, notation, diagram and audience awareness.",
                   d="ii: applying place value to a real communication problem.")

    # ---------------------------------------------------------- review
    p = _body(bk)
    p.add(Stage("08", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, [
        "Numbers belong to nested families; each extension of the family makes a new kind "
        "of question answerable.",
        "In base ten, a digit's value is the digit multiplied by a power of ten determined "
        "by its position.",
        "Zero holds a column open and is therefore essential, not decorative.",
        "Expanded form is an equivalent representation that exposes structure.",
        "Rounding replaces a value with a nearby value at a stated precision, and the "
        "choice of precision is a mathematical decision, not a presentation one.",
    ])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["natural number", "A counting number: 1, 2, 3, \u2026"],
        ["whole number", "A natural number or zero."],
        ["integer", "A whole number or its negative."],
        ["rational number", "A number that can be written as a fraction of two integers, "
                            "with a non-zero denominator."],
        ["place value", "The value a digit carries because of its position."],
        ["expanded form", "A number written as the sum of its column values."],
        ["rounding", "Replacing a number with a nearby value at a stated precision."],
        ["estimate", "A deliberately simplified calculation used to judge size or "
                     "reasonableness."],
    ], widths=[0.85, 2.2])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that survive into later years",
          text="**Longer decimal, larger number.** 0.65 is not larger than 0.7. Align "
               "columns and compare like with like.\n"
               "**Zero is nothing.** A zero in the middle of a number does essential work; "
               "deleting it changes the value.\n"
               "**More digits, more accuracy.** Digits beyond the precision of the "
               "measurement are a claim, not a fact.")
    assessment_close(p, [
        ["classify numbers as natural, whole or integer", "\u25a1", "\u25a1", "\u25a1"],
        ["state the value of any digit in a decimal", "\u25a1", "\u25a1", "\u25a1"],
        ["write and reverse expanded form", "\u25a1", "\u25a1", "\u25a1"],
        ["order decimals correctly", "\u25a1", "\u25a1", "\u25a1"],
        ["round to a named place and justify it", "\u25a1", "\u25a1", "\u25a1"],
        ["estimate before calculating", "\u25a1", "\u25a1", "\u25a1"],
        
    ],
        "In order for a student to know which habit still needs work, students must "
               "mark the table honestly and then attempt one question from the weakest row "
               "before reading the answer.",
        next_title="Chapter 2 · Powers, expanded form and order of operations")


    # ------------------------------------------------------ mixed practice
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("09", "MIXED PRACTICE"))
    p.add(Spacer(6))
    practice(p, "Mixed practice 1",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201312  \u00b7  EXTENSION 10\u201315", [
        q("Write 8 007 040 in words.", "F"),
        q("Write the value of the digit 6 in 3.062.", "F"),
        q("Round 6.478 to one decimal place and to the nearest whole number.", "F"),
        q("Insert < or >: (a) 0.08 \u2026 0.1 (b) \u22121.4 \u2026 \u22121.35.", "F"),
        q("Write 7 \u00d7 1000 + 0 \u00d7 100 + 9 \u00d7 10 + 2 \u00d7 1 + 5 \u00d7 0.001 as "
          "a single number.", "F"),
        q("A student writes 2.5 for 2.05. Explain what has gone wrong and give the correct "
          "statement.", "R"),
        q("Order from least to greatest: \u22120.5, 0.05, \u22120.05, 0.5, 0.", "R"),
        q("Estimate 38 \u00d7 51 and then compute it. By what percentage does your estimate "
          "differ?", "P"),
        q("A shop sells rice at 6.75 per kilogram. Estimate the cost of 14 kg and calculate "
          "the exact price.", "P"),
        q("The distance to a village is quoted as \u201cabout 12 km\u201d. What range of "
          "actual distances is consistent with this statement if the quote is to the "
          "nearest kilometre?", "R"),
        q("Explain why \u20140.0\u201d and \u201c0\u201d can be written differently but "
          "represent the same value.", "E"),
        q("Write the largest and smallest numbers you can make with the digits 3, 0, 7, 5 "
          "and a decimal point, using each digit once.", "E"),
        q("A pump delivers 0.75 litres per second. Estimate how long it takes to deliver "
          "1 000 litres, then calculate it to a sensible accuracy.", "P"),
        q("Show that 4 096 and 4 096.000 are equivalent, then explain what the extra digits "
          "might legitimately indicate.", "E"),
        q("Design a five-question place-value diagnostic for a younger student. Include the "
          "answers and say what each question tests.", "E"),
    ])
    gap(p, 10)
    p.add(Stage("10", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20133", "Revisit 1.2 and 1.4: read each digit's column aloud before writing."],
        ["4\u20136", "Revisit 1.4: align the decimal points and fill empty columns."],
        ["7\u20139", "Revisit 1.5: round first, calculate second, adjust third."],
        ["10\u201312", "Revisit 1.3: expanded form exposes what rounding removes."],
        ["13\u201315", "Revisit the chapter review; write your own version of each summary "
                      "point."],
    ], widths=[0.7, 2.6])


def _body(bk):
    from bookkit.flow import Pager
    bk.new_page("wide")
    p = Pager(bk)
    bk.part_label = PLATE["part"]
    bk.chapter_label = "Chapter 1 \u00b7 Number systems and place value"
    return p


ANSWERS = [
    ("Prereq 1", "4 060 \u2014 the zeros hold the hundreds and ones columns open."),
    ("Prereq 2", "3.5 > 3.45: compare tenths first, 5 > 4."),
    ("Prereq 3", "56 and 8."),
    ("Prereq 4", "3 050."),
    ("Prereq 5", "0.75."),
    ("Prereq 6", "0.06 < 0.6 < 0.66."),
    ("1.1", "1 (a) \u22122 (b) \u22127.  2 \u22127 < \u22123.  3 \u22123, \u22122, \u22121, 0, 1.  "
             "5 \u22122.05 is greater (\u22122.05 lies to the right of \u22122.5).  "
             "6 First submarine: \u221225 m; second: \u221232 m, so the second is 7 m "
             "deeper.  8 \u22126 and 1 (or any pair summing to \u22125 with difference 7)."),
    ("1.2", "1 (a) 2 007 (b) 940 (c) 6 210.  2 (a) 700 (b) 7 (c) 7 (d) 0.07.  "
            "3 6 000 + 0 + 40 + 5 = 6 \u00d7 1000 + 4 \u00d7 10 + 5 \u00d7 1.  4 3 or 4 "
            "(5 302 to 5 492).  5 0.7 = 0.70 > 0.65.  6 Estimate 250; exact 225.  "
            "7 2 400 kg.  9 0.003 means three thousandths; 0.300 means three tenths."),
    ("1.3", "1 (a) 8 000 + 500 + 2 (b) 7 + 0.04 (c) 60 + 0.5.  2 (a) 9 307 (b) 20.5.  "
            "3 Thirty thousand, four hundred and seven; 3 \u00d7 10 000 + 0 \u00d7 1000 + "
            "4 \u00d7 100 + 0 \u00d7 10 + 7 \u00d7 1.  4 604 is larger (600.4).  "
            "5 3 \u00d7 10 must be 3 \u00d7 100: 2 300, not 2 030.  6 1 205.09; the zero "
            "holds the tenths column open."),
    ("1.4", "1 (a) > (b) < (c) <.  2 (a) 7 (b) 13 (c) 1.  3 45 680; 45 700; 46 000.  "
            "4 3.04 < 3.4 < 3.404 < 3.44.  5 10.00 \u2014 the hundredths digit 6 rounds "
            "9.99 up.  7 5.64 rounds to 5.6 but to 5.64 at two places.  9 No: a number "
            "cannot be both about 100 and about 0.1."),
    ("1.5", "1 (a) 1 200 (b) 30 (c) 700.  2 100; 98.98.  3 About 21 packets (500 \u00f7 "
            "24 = 20.8).  4 4 000 \u00d7 0.5 = 2 000.  5 Estimate 5 \u00d7 3 = 15, so "
            "161.2 is impossible; 5.2 \u00d7 3.1 = 16.12.  7 1 250 \u00f7 18 \u2248 69 "
            "minutes."),
    ("Investigation 1", "Each row multiplies the previous row by 10. With a leading zero "
                        "allowed the count is 10^{n}; without it, 9 \u00d7 10^{n\u22121}. "
                        "The difference is the 10^{n\u22121} strings that begin with zero."),
    ("Mixed 1", "1 Eight million, seven thousand and forty.  2 0.06.  3 6.5 and 6.  "
                "4 (a) < (b) <.  5 7 092.005.  6 The zero holds the tenths column; the "
                "number is 2.05.  7 \u22120.5 < \u22120.05 < 0 < 0.05 < 0.5.  "
                "8 Estimate 2 000; exact 1 938.  9 Estimate 94.50; exact 94.50 \u2014 "
                "6.75 \u00d7 14 = 94.50.  10 11.5 km to 12.5 km.  12 Largest 7 530.0, "
                "smallest 0.035 7 (with one decimal point only).  13 About 22 minutes."),
]
