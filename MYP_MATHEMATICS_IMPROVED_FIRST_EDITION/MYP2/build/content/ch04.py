"""Chapter 4 - Integers and operations (Algebra and pattern)."""
from chbase import *

PLATE = dict(
    part="Part I \u00b7 Number and proportion", part_numeral="I", chapter_no=4,
    kicker="Algebra and pattern", motif="integers",
    title_lines=["Integers and", "operations"],
    lead_lines=["Negative numbers extend the number line in both directions.",
                "Their arithmetic is not a set of rules to memorise but a",
                "consequence of one idea: every number has an opposite, and",
                "opposites cancel."],
    key_concept="Logic", related=["Quantity", "Change"],
    context="Scientific and technical innovation",
    inquiry_lines=["Why does multiplying two negative numbers give a",
                   "positive result, and what would break if it did not?"])

TITLE = "Integers and operations"
SHORT = "Integers and operations"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "Signed numbers on the line, and the arithmetic that keeps the line "
       "consistent."),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "Extending the number line below zero forces a consistent arithmetic of "
              "signs, so that every calculation can be represented as movement along "
              "a line."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Logic.** The rules for signed arithmetic are not "
        "arbitrary: each follows from requiring that the number line and the laws of "
        "arithmetic keep working below zero.\n"
        "**Related \u00b7 Quantity.** A negative number records a quantity in the "
        "opposite direction: a debt, a fall, a depth.\n"
        "**Related \u00b7 Change.** Adding a negative number is a move left; "
        "subtracting a negative is a move right."),
    BOX("note", "Global context \u00b7 Scientific and technical innovation",
        "Exploration: temperatures below freezing, depths below sea level and balances "
        "below zero. Instruments report signed quantities because the world has "
        "directions, not only sizes."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** How do you order and compare negative numbers?",
        "**Conceptual:** Why is subtracting a negative the same as adding a positive?",
        "**Debatable:** Does a negative number measure anything real, or is it only a "
        "bookkeeping device?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Order integers; add, subtract, multiply and divide signed numbers."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate the pattern that forces (\u2212) \u00d7 (\u2212) = +."],
        ["C \u00b7 Communicating", "ii, iii, iv",
         "Use the number line and bracket notation to make the working readable."],
        ["D \u00b7 Applying mathematics", "i, ii, iv",
         "Model a weather station's readings and justify a decision."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to explain a rule for signs, students must show the "
        "pattern that makes the rule necessary and give the counterexample that would "
        "follow if the rule were different."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Order integers and find absolute values.",
         "Order \u22127, 4, \u22122, 0, \u22125 and state each distance from zero."],
        ["Add and subtract integers.",
         "Compute \u22128 + 3, \u22125 \u2212 7 and 4 \u2212 (\u22126) with a number "
         "line."],
        ["Multiply and divide integers.",
         "Predict and check the sign of a product before computing it."],
        ["Apply the order of operations to signed expressions.",
         "Evaluate \u22123\u00b2 + 4 \u00d7 (\u22122) correctly."],
        ["Use integers to model real situations.",
         "Write a signed expression for a temperature change or an account "
         "balance."],
        ["Justify a rule for signs.",
         "Explain, with a pattern, why a negative times a negative is positive."],
    ], widths=[1.6, 1.8]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Calculate \u00a0 7 + 8 \u00a0 and \u00a0 15 \u2212 9.",
               "Which is greater, \u00a0 \u22123 \u00a0 or \u00a0 \u22127?",
               "Calculate \u00a0 6 \u00d7 7 \u00a0 and \u00a0 42 \u00f7 6.",
               "What is \u00a0 3\u00b2?",
               "Evaluate \u00a0 2 + 3 \u00d7 4.",
               "Write the next two terms of \u00a0 10, 7, 4, \u2026"]),
    P("If three or more answers are wrong, revisit the four operations and the order "
      "of operations before section 4.2."),

    # ------------------------------------------------------------------ 4.1
    S("4.1", "Integers, order and absolute value", "A \u00b7 I",
      ["Quantity", "Number line"]),
    L("An integer is a whole number that may be positive, negative or zero. The "
      "number line shows all of them, equally spaced, with zero in the middle."),
    ST("03", "ENGAGE",
       "Two readings, one morning. Which is colder, and by how much?"),
    PHOTO("ch04_thermometer.jpg", 1.5,
          "A thermometer in snow. The scale continues below zero, which is exactly "
          "what the integers were invented to describe.",
          "Photograph: Pexels, free licence (see the image register)."),
    P("At 06:00 a mountain weather station records \u22129\u00b0C. At 14:00 it "
      "records \u22122\u00b0C. A student says the temperature has fallen because "
      "\u22129 is a bigger number than \u22122. Before reading on, sketch a number "
      "line, mark both readings, and write the size of the change with its direction."),
    ST("04", "EXPLORE",
       "Walking the line."),
    P("Copy a number line from \u221210 to 10 and mark these points: \u22127, "
      "\u22122, 0, 3, 8."),
    OL(["Which two marked numbers are furthest apart? How did you find the "
        "distance?",
        "How far is each mark from zero? Record each distance without a sign.",
        "Start at \u22123 and move 5 places right. Where do you finish? Write the "
        "calculation.",
        "Start at 2 and move 6 places left. Where do you finish? Write the "
        "calculation.",
        "Compare \u22125 and \u22122. Which is less, and which is further from zero?",
        "Write a conjecture: how can a number line turn every addition into a "
        "movement, and every subtraction into a movement in the opposite "
        "direction?"]),
    ST("05", "EXPLAIN"),
    PHOTO("ch04_stairs.jpg", 1.1,
          "A flight of steps. Each step is the same height, so the treads give a "
          "natural number line: up is positive, down is negative.",
          "Photograph: Pexels, free licence (see the image register).", 0.62),
    DEF("An `integer` is a whole number that may be positive, negative or zero. The "
        "`absolute value` of an integer is its distance from zero, written with "
        "vertical bars: |\u22125| = 5 and |5| = 5. On the number line, larger means "
        "further right, so \u22122 > \u22125."),
    DIAG(170, "signed_line",
         "Integers ordered on the number line. The arrow shows the change from "
         "\u22123 to 2: five steps to the right, so the change is +5."),
    P("Adding a negative number moves left; subtracting a positive number also moves "
      "left. Subtracting a negative number moves right, because removing a debt "
      "increases what you have. The number line makes both statements visible, which "
      "is why it is worth drawing before computing."),
    KEY("|\u2212`a`| = |`a`|: a number and its opposite are the same distance from "
        "zero. That is why cancelling one +1 with one \u22121 leaves nothing: the two "
        "distances are equal and opposite."),
    DIAG(150, "integer_chips",
         "Three +1 chips and five \u22121 chips. Each opposite pair cancels, leaving "
         "two \u22121 chips: 3 + (\u22125) = \u22122."),
    WE("4.1.1", "Order and absolute value",
       "Order \u22124, 3, \u22127, 0, \u22121 from least to greatest, then write the "
       "absolute value of each.",
       ["On the number line, further left is smaller: \u22127 < \u22124 < \u22121 < "
        "0 < 3.",
        "Take distances from zero: |\u22127| = 7, |\u22124| = 4, |\u22121| = 1, "
        "|0| = 0, |3| = 3.",
        "Note that the order of the numbers and the order of their absolute values "
        "differ.",
        "Report both orders, since the question asks for both."],
       "\u22127 < \u22124 < \u22121 < 0 < 3; absolute values 7, 4, 1, 0, 3",
       "The smallest number has the largest absolute value \u2014 a useful check."),
    WE("4.1.2", "Two readings, one change",
       "A temperature rises from \u22129\u00b0C to \u22122\u00b0C. What is the change?",
       ["Change = final \u2212 initial = \u22122 \u2212 (\u22129).",
        "Subtracting \u22129 is the same as adding 9: \u22122 + 9 = 7.",
        "The change is +7 degrees, that is, a rise of 7 degrees.",
        "Check on the line: from \u22129, move right 7 places to \u22122."],
       "A rise of 7 degrees",
       "A negative answer would have meant a fall; the sign carries the direction."),
    ERR("\u201c\u22129 is bigger than \u22122, so the temperature rose by 11.\u201d "
        "The sign of the answer comes from the calculation \u22122 \u2212 (\u22129) = "
        "+7, not from the sizes of the digits. Compare positions on the line, not "
        "digit values."),
    PRAC("4.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Write the integer that describes each: (a) a debt of \u00a340  (b) 12 m "
          "below sea level  (c) a gain of 6 points  (d) 3\u00b0C below zero.", "F"),
        Q("Order from least to greatest: \u22126, 2, \u22129, 0, \u22121, 5.", "F"),
        Q("Find each absolute value: |\u221212|, |7|, |0|, |\u22123|.", "F"),
        Q("Write the integers between \u22124 and 1 inclusive.", "F"),
        Q("Calculate: (a) \u22125 + 8  (b) \u22126 \u2212 4  (c) 3 \u2212 9.", "F"),
        Q("The temperature falls from 4\u00b0C to \u22127\u00b0C. By how much does it "
          "fall?", "P"),
        Q("A submarine is at \u221235 m and rises 12 m. What is its new depth?", "P"),
        Q("Which is greater, \u22128 or \u221211? Which has the greater absolute "
          "value? Explain the difference in one sentence.", "R"),
        Q("Find two integers whose difference is \u22126 and whose sum is 4.", "P"),
        Q("A student says \u201c\u22125 is further from zero than \u22122, so "
          "\u22125 is bigger\u201d. Explain the error, using the number line.", "E"),
        Q("The temperature at midnight was \u22126\u00b0C. It rose 3\u00b0C by 06:00 "
          "and then fell 8\u00b0C by noon. Find the noon temperature.", "E"),
        Q("Find all integers `x` such that |`x`| = 7 and `x` < 0.", "E"),
    ]),

    # ------------------------------------------------------------------ 4.2
    S("4.2", "Adding and subtracting integers", "A \u00b7 II",
      ["Change", "Number line"]),
    L("Every addition of a signed number can be read as a movement along the line, and "
      "every subtraction as a movement in the reverse direction."),
    H("Two equivalent readings"),
    UL(["**Movement:** \u22128 + 3 means start at \u22128 and move 3 right, "
        "finishing at \u22125.",
        "**Cancelling:** \u22128 + 3 combines eight \u22121 chips with three +1 chips; "
        "three pairs cancel, leaving five \u22121 chips."]),
    P("Both readings give the same answer, and both are worth knowing. The movement "
      "reading is fast for small numbers; the cancelling reading explains why the "
      "answer has the sign it does."),
    WE("4.2.1", "Add and subtract",
       "Calculate (a) \u22125 \u2212 7, (b) 4 \u2212 (\u22126), (c) \u22123 + "
       "(\u22124) + 9.",
       ["(a) Subtracting 7 moves 7 left from \u22125: the result is \u221212.",
        "(b) Subtracting \u22126 is the same as adding 6, so 4 + 6 = 10.",
        "(c) Combine the negatives first: \u22123 + (\u22124) = \u22127, then "
        "\u22127 + 9 = 2.",
        "Check (b) on the line: from 4, move 6 right, finishing at 10."],
       "(a) \u221212   (b) 10   (c) 2",
       "For (c), the total leftward movement is 7 and the rightward movement is 9, so "
       "the net movement is 2 right."),
    WE("4.2.2", "A real balance",
       "An account balance is \u2212\u00a3120. A payment of \u00a350 is made into it, "
       "then a bill of \u00a380 is taken out. Find the balance and interpret it.",
       ["Start at \u2212120.",
        "Adding \u00a350: \u2212120 + 50 = \u221270.",
        "Subtracting \u00a380: \u221270 \u2212 80 = \u2212150.",
        "The balance is \u2212\u00a3150: the account is overdrawn by \u00a3150."],
       "\u2212\u00a3150, an overdraft of \u00a3150",
       "Check the net change: +50 \u2212 80 = \u221230, and \u2212120 \u2212 30 = "
       "\u2212150."),
    WE("4.2.3", "A distance between two points",
       "The temperature at the summit is \u22128\u00b0C and at the base \u22123\u00b0C. "
       "How much colder is the summit?",
       ["Change = summit \u2212 base = \u22128 \u2212 (\u22123).",
        "\u22128 + 3 = \u22125.",
        "A change of \u22125 degrees means the summit is 5 degrees colder.",
        "Check on the line: \u22128 is five places left of \u22123."],
       "5 degrees colder",
       "The sign gives the direction; the size gives the amount."),
    ERR("\u201c4 \u2212 (\u22126) = \u22122, because the two minus signs "
        "cancel.\u201d Cancelling does happen, but it produces addition: 4 \u2212 "
        "(\u22126) = 4 + 6 = 10. Two signs together are not a multiplication."),
    PRAC("4.2", "SUPPORT 1\u20135  \u00b7  CORE 6\u201310  \u00b7  EXTENSION "
                "11\u201313", [
        Q("Calculate: (a) \u22126 + 9  (b) \u22128 \u2212 3  (c) 5 \u2212 12  "
          "(d) \u22124 + (\u22127).", "F"),
        Q("Calculate: (a) 7 \u2212 (\u22125)  (b) \u22123 \u2212 (\u22129)  "
          "(c) \u22129 + 9.", "F"),
        Q("Fill in the missing number: \u22127 + \u2026 = \u22122.", "F"),
        Q("A lift starts at floor \u22122, goes up 5 floors, then down 7. Which floor "
          "is it on?", "F"),
        Q("Calculate: (a) \u22125 + 3 \u2212 4  (b) 6 \u2212 9 + 2  (c) \u22122 "
          "\u2212 6 \u2212 1.", "F"),
        Q("The temperature rises from \u221211\u00b0C by 7\u00b0C. What is the new "
          "temperature?", "P"),
        Q("An account holds \u00a3240 and two payments of \u00a3165 and \u00a3190 are "
          "taken out. Find the balance and interpret it.", "P"),
        Q("Find the distance between \u22127 and 4 on the number line.", "P"),
        Q("A mountain is 3 200 m above sea level and a trench is 1 450 m below. Find "
          "the difference in height.", "P"),
        Q("Two numbers have a sum of \u22127 and a difference of 15. Find both.", "R"),
        Q("Explain, using the number line, why subtracting a negative number is the "
          "same as adding a positive one.", "E"),
        Q("The temperature fell by 5\u00b0C each night for four nights, starting at "
          "2\u00b0C. Write and evaluate an expression for the final temperature.",
          "E"),
        Q("Find two integers, one positive and one negative, whose product is "
          "\u221236 and whose sum is 5.", "E"),
    ]),

    # ------------------------------------------------------------------ 4.3
    S("4.3", "Multiplying and dividing integers", "A \u00b7 III  \u00b7  "
      "B \u00b7 III", ["Logic", "Change"]),
    L("Multiplication of signs follows from one requirement: the number line and the "
      "laws of arithmetic must keep working when negative numbers are included."),
    H("Repeated addition"),
    P("3 \u00d7 (\u22124) means three lots of \u22124: \u22124 + (\u22124) + "
      "(\u22124) = \u221212. When the first factor is negative, the reading is less "
      "obvious, and the pattern below settles it."),
    DIAG(200, "neg_mult",
         "The product \u22122 \u00d7 `n` as `n` falls by 1. Each step raises the "
         "product by 2, and continuing past zero forces \u22122 \u00d7 (\u22121) = "
         "+2."),
    KEY("The four cases, in one line: (+) \u00d7 (+) = +, (+) \u00d7 (\u2212) = "
        "\u2212, (\u2212) \u00d7 (+) = \u2212, (\u2212) \u00d7 (\u2212) = +. Exactly "
        "two negatives give a positive; one negative gives a negative."),
    WE("4.3.1", "Compute with signs",
       "Calculate (a) \u22126 \u00d7 4, (b) \u22126 \u00d7 (\u22124), "
       "(c) \u221248 \u00f7 8, (d) \u221248 \u00f7 (\u22126).",
       ["(a) One negative factor, so the product is negative: \u221224.",
        "(b) Two negative factors, so the product is positive: 24.",
        "(c) One negative term, so the quotient is negative: \u22126.",
        "(d) Two negatives, so the quotient is positive: 8."],
       "(a) \u221224   (b) 24   (c) \u22126   (d) 8",
       "Check (d) by multiplying back: 8 \u00d7 (\u22126) = \u221248."),
    WE("4.3.2", "Order of operations with signs",
       "Evaluate \u22123\u00b2 + 4 \u00d7 (\u22122) \u2212 (\u22125).",
       ["Indices first, and the minus sign is not part of the square: \u22123\u00b2 "
        "= \u22129.",
        "Multiplication next: 4 \u00d7 (\u22122) = \u22128.",
        "Now the expression reads \u22129 \u2212 8 + 5.",
        "Working left to right: \u221217 + 5 = \u221212."],
       "\u221212",
       "Note that (\u22123)\u00b2 = +9: the brackets matter, and so does the order."),
    WE("4.3.3", "Division as the inverse",
       "Given that \u22127 \u00d7 9 = \u221263, write two division statements and "
       "explain the signs.",
       ["Divide the product by one factor: \u221263 \u00f7 9 = \u22127.",
        "Divide by the other factor: \u221263 \u00f7 (\u22127) = 9.",
        "Each quotient has exactly one negative because each product has exactly one "
        "negative factor.",
        "The two statements check each other: they reconstruct the original "
        "product."],
       "\u221263 \u00f7 9 = \u22127 and \u221263 \u00f7 (\u22127) = 9",
       "Division is multiplication read backwards, so the sign rules must agree."),
    ERR("Writing \u22123\u00b2 = 9. Without brackets, the square applies only to 3, "
        "so \u22123\u00b2 = \u2212(3 \u00d7 3) = \u22129. With brackets, "
        "(\u22123)\u00b2 = +9. Write the brackets whenever the sign is inside the "
        "power."),
    PRAC("4.3", "SUPPORT 1\u20135  \u00b7  CORE 6\u201310  \u00b7  EXTENSION "
                "11\u201313", [
        Q("Calculate: (a) \u22125 \u00d7 6  (b) \u22125 \u00d7 (\u22126)  "
          "(c) 7 \u00d7 (\u22123).", "F"),
        Q("Calculate: (a) \u221236 \u00f7 4  (b) \u221236 \u00f7 (\u22124)  "
          "(c) 36 \u00f7 (\u22129).", "F"),
        Q("State the sign of each product without computing: (a) \u22123 \u00d7 8  "
          "(b) \u22123 \u00d7 (\u22128)  (c) \u22123 \u00d7 (\u22128) \u00d7 "
          "(\u22122).", "F"),
        Q("Evaluate: (a) \u22124\u00b2  (b) (\u22124)\u00b2  (c) \u22122\u00b3.",
          "F"),
        Q("Evaluate: (a) 2 \u2212 3 \u00d7 (\u22124)  (b) (\u22126 + 2) \u00d7 "
          "\u22125.", "F"),
        Q("A submarine descends 15 m every minute for 6 minutes. Write and evaluate an "
          "expression for its total change in depth.", "P"),
        Q("The product of two integers is \u221248 and one of them is 6. Find the "
          "other.", "P"),
        Q("Find two integers whose product is \u221212 and whose sum is \u22121.",
          "P"),
        Q("Explain why (\u22122) \u00d7 (\u22123) = 6, using the pattern of "
          "\u22122 \u00d7 3, \u22122 \u00d7 2, \u22122 \u00d7 1, \u22122 \u00d7 0.",
          "R"),
        Q("A student writes \u22123\u00b2 = 9. Identify the error and give the correct "
          "value, with and without brackets.", "R"),
        Q("Evaluate \u22122 \u00d7 (\u22123 + 7) \u2212 4\u00b2 \u00f7 (\u22122).",
          "E"),
        Q("The product of three integers is negative. What do you know about the "
          "signs of the integers? Give two different possibilities.", "E"),
        Q("Find all pairs of integers whose product is \u221236 and whose sum is "
          "positive.", "E"),
    ]),

    CARD_D("A mountain weather station", [
        ("p", "A weather station records temperatures every six hours for two days. "
              "The records are: \u22126, \u22122, 3, \u22121, \u22124, \u22127, "
              "0, 2, all in degrees Celsius."),
        ("ol", ["Find the highest and lowest readings and the range.",
                "Find the change between each consecutive pair of readings.",
                "Which change is the largest fall, and which is the largest rise?",
                "Find the mean of the eight readings.",
                "The station's sensor is accurate to \u00b11\u00b0C. State the mean to "
                "an appropriate accuracy, and justify your rounding.",
                "On the third day the temperature falls by 3\u00b0C every six hours "
                "from a start of 4\u00b0C. Write an expression for the reading after "
                "four intervals and evaluate it.",
                "Write two sentences a walker would find useful, based on these "
                "figures."]),
    ]),

    # ----------------------------------------------------------- investigate
    ST("06", "INVESTIGATE AND APPLY",
       "Why is a negative times a negative positive?"),
    CARD_I("Why is negative times negative positive?", [
        ("p", "The rule (\u2212) \u00d7 (\u2212) = + is often given as something to "
              "memorise. This investigation derives it, and tests what would happen "
              "if it were different."),
        ("ol", ["Complete the table of \u22123 \u00d7 `n` for `n` = 4, 3, 2, 1, 0, "
                "\u22121, \u22122. What happens to the product each time `n` falls "
                "by 1?",
                "Continue the pattern for another three rows. Does the pattern force "
                "a particular value at each step?",
                "Now suppose (\u22123) \u00d7 (\u22121) were \u22123 instead of +3. "
                "Complete the table again with that assumption and describe what "
                "happens to the step size.",
                "Test the same reasoning starting from \u22125 \u00d7 `n`. Does the "
                "conclusion depend on the choice of \u22123 or \u22125?",
                "Use a different argument: the distributive law gives "
                "(\u22122) \u00d7 (3 + (\u22123)) = 0. Expand and see what value "
                "(\u22122) \u00d7 (\u22123) must have.",
                "Write your generalisation in one sentence, and name the two "
                "principles it relies on.",
                "Find one place in real life where a negative times negative "
                "naturally appears, and explain it."]),
    ]),

    # --------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("4.6", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["Integers continue the number line below zero; larger means further right, "
        "not further from zero.",
        "The absolute value is the distance from zero, and it is never negative.",
        "Adding a negative moves left; subtracting a negative moves right.",
        "The sign of a product or quotient depends only on the number of negative "
        "factors: an even count gives positive, an odd count gives negative.",
        "The order of operations applies to signed numbers, and brackets around a "
        "sign change the meaning of a power.",
        "Signed numbers model debt, depth, temperature and any quantity with a "
        "direction."]),
    VOCAB("**integer** \u00b7 **negative number** \u00b7 **opposite** \u00b7 "
          "**absolute value** \u00b7 **number line** \u00b7 **sign** \u00b7 "
          "**order of operations** \u00b7 **index (power)** \u00b7 **inverse "
          "operation**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["\u201c\u22129 is larger than \u22122 because 9 > 2.\u201d",
         "\u22129 is further left, so it is smaller. The digits describe the "
         "distance, the sign describes the direction."],
        ["\u201cTwo minus signs always cancel by disappearing.\u201d",
         "They combine into a plus: 4 \u2212 (\u22126) = 4 + 6 = 10."],
        ["\u201c\u22123\u00b2 = 9.\u201d",
         "Without brackets the square applies to 3 only: \u22123\u00b2 = \u22129, "
         "while (\u22123)\u00b2 = 9."],
        ["\u201cA negative answer means the calculation is wrong.\u201d",
         "A negative answer means a direction or a deficit; it can be entirely "
         "correct."],
    ], widths=[1.5, 2.0]),
    H("Revision questions"),
    OL(["Order from least to greatest: \u22123, 7, \u221210, 0, \u22121.",
        "Calculate \u221212 + 5 \u2212 (\u22123).",
        "Calculate \u22126 \u00d7 (\u22125) \u00f7 (\u22122).",
        "Evaluate \u22122\u00b2 + (\u22123)\u00b2.",
        "The temperature is \u22124\u00b0C and falls 7\u00b0C. Find the new "
        "temperature, and state the absolute value of the change."]),
    GAP(6),
    H("Before you move on"),
    P("Four things you should be able to do without help before the next "
      "chapter. If one of them is not yet secure, reread the section that "
      "taught it before attempting the mixed practice again.", 4),
    UL([
        "Order signed numbers and explain the order on a number line.",
        "Add and subtract signed numbers without a rule you cannot justify.",
        "Multiply and divide signed numbers and give the sign before the value.",
        "Apply the order of operations where a negative sign and a power compete.",
    ]),
    KEY("The sign is part of the number; the operations extend the number line rather than replace it."),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["order integers and find absolute values", "\u25a1", "\u25a1", "\u25a1"],
        ["add and subtract integers without a calculator", "\u25a1", "\u25a1",
         "\u25a1"],
        ["predict the sign of a product or quotient", "\u25a1", "\u25a1", "\u25a1"],
        ["apply the order of operations to signed expressions", "\u25a1", "\u25a1",
         "\u25a1"],
        ["model a real situation with a signed expression", "\u25a1", "\u25a1",
         "\u25a1"],
        ["explain why a negative times a negative is positive", "\u25a1", "\u25a1",
         "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], font_size=8.6),
    GAP(8),
    MYP("**Criterion A:** which signed calculation are you now able to do "
        "mentally?\n"
        "**Criterion B:** what pattern convinced you of the sign rules?\n"
        "**Criterion C:** where did the number line make your reasoning clearer?\n"
        "**Criterion D:** which real quantity would be misreported without a sign?",
        "Reflect on the criteria"),
    ATL("In order for a student to explain a rule that others memorise, students must "
        "produce the pattern that makes the rule necessary and describe what would "
        "fail without it.", "ATL \u00b7 Critical thinking"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("4.M", "MIXED 1\u201312", [
        Q("Calculate: (a) \u22129 + 4  (b) \u22129 \u2212 4  (c) 9 \u2212 14.", "F"),
        Q("Calculate: (a) \u22127 \u00d7 8  (b) \u221272 \u00f7 (\u22129).", "F"),
        Q("Order: \u22125, 0, 3, \u22128, 1.", "F"),
        Q("Evaluate: \u22125 + 2 \u00d7 (\u22123).", "F"),
        Q("The temperature falls from 3\u00b0C to \u22128\u00b0C. Find the change.",
          "F"),
        Q("A diver descends in 4 stages of 12 m each. Write and evaluate an "
          "expression for the total descent.", "P"),
        Q("Find the mean of \u22124, 2, \u22127, 5.", "P"),
        Q("Explain why the product of two negatives must be positive, using one "
          "example and one pattern.", "R"),
        Q("Evaluate (\u22123)\u00b2 \u2212 4 \u00d7 (\u22122) + 1.", "F"),
        Q("The sum of two integers is \u22125 and their product is 6. Find them.",
          "E"),
        Q("A shop's balance is \u2212\u00a3240. Three payments of \u00a395 each are "
          "received. Find the new balance.", "E"),
        Q("Find all integer values of `n` such that \u22123 < `n` \u2264 2, and state "
          "the sum of their absolute values.", "E"),
    ]),
]

ANSWERS = {
    "4.1": ["(a) \u221240 (b) \u221212 (c) +6 (d) \u22123.",
            "\u22129 < \u22126 < \u22121 < 0 < 2 < 5.", "12, 7, 0, 3.",
            "\u22124, \u22123, \u22122, \u22121, 0, 1.", "(a) 3 (b) \u221210 (c) "
            "\u22126.", "11 degrees.", "\u221223 m.",
            "\u22128 is greater; \u221211 has the greater absolute value. On the "
            "line, \u22128 lies to the right of \u221211, while \u221211 is further "
            "from zero.", "\u22121 and 5.", "\u22125 is further from zero but lies "
            "to the left of \u22122, so it is smaller.",
            "\u221211\u00b0C.", "`x` = \u22127."],
    "4.2": ["(a) 3 (b) \u221211 (c) \u22127 (d) \u221211.",
            "(a) 12 (b) 6 (c) 0.", "5.", "Floor \u22124.",
            "(a) \u22126 (b) \u22121 (c) \u22129.", "\u22124\u00b0C.",
            "\u2212\u00a3115, an overdraft of \u00a3115.", "11.",
            "4 650 m.", "\u221211 and 4.",
            "Subtracting a number means moving left by that many places; subtracting a negative number means moving left by a negative amount, which is moving right \u2014 the same as adding the positive number.",
            "2 + 4 \u00d7 (\u22125) = \u221218\u00b0C.", "\u22124 and 9."],
    "4.3": ["(a) \u221230 (b) 30 (c) \u221221.", "(a) \u22129 (b) 9 (c) \u22124.",
            "(a) negative (b) positive (c) negative.",
            "(a) \u221216 (b) 16 (c) \u22128.", "(a) 14 (b) 20.",
            "\u221215 \u00d7 6 = \u221290 m.", "\u22128.",
            "\u22124 and 3.",
            "Each time the second factor falls by 1 the product rises by 2, so "
            "after 0 the next products must be +2 and +4; any other choice would "
            "break the constant step of the pattern.",
            "The square applies to the 3 only, so \u22123\u00b2 = \u22129; with "
            "brackets, (\u22123)\u00b2 = +9.",
            "0.",
            "One negative and two positives, or all three negative.",
            "(\u22124, 9), (\u22123, 12), (\u22122, 18), (\u22121, 36) with "
            "positive sums: 5, 9, 16, 35."],
    "4.M": ["(a) \u22125 (b) \u221213 (c) \u22125.", "(a) \u221256 (b) 8.",
            "\u22128 < \u22125 < 0 < 1 < 3.", "\u221211.", "\u221211 degrees.",
            "4 \u00d7 (\u221212) = \u221248 m.", "\u22121.",
            "Every time the second factor falls by 1 the product rises by 2, so "
            "continuing past zero forces a positive result; without that the "
            "distributive law fails, since "
            "(\u22122)\u00d7(3+(\u22123)) = 0 needs "
            "(\u22122)\u00d7(\u22123) = +6.",
            "18.", "\u22122 and \u22123.",
            "\u00a345.", "\u22122, \u22121, 0, 1, 2; sum of absolute values 6."],
}


# ------------------------------------------------------------------ part review
BLOCKS += [
    GAP(14),
    ("head", "Part I review"),
    ("pagetitle", "Part I review", "Consolidation \u00b7 chapters 1\u20134"),
    L("Ten questions that draw on the whole of Part I. Nothing here is new: "
      "each item mixes two ideas that were taught in different chapters, which is "
      "what an examination does."),
    P("Work without notes first; an item you cannot start is a signal to reread "
      "one section, not to guess. Compare your answers with the key only after "
      "the whole set is finished.", 6),
    PRAC("R1", "SUPPORT 1\u20134  \u00b7  CORE 5\u20137  \u00b7  EXTENSION 8\u201310", [
        Q("Simplify the ratio 45 minutes : 2 hours.", "F"),
        Q("Share \u00a3252 in the ratio 4 : 5.", "F"),
        Q("A recipe for 5 people uses 350 g of rice. Find the mass needed for 8 "
          "people.", "F"),
        Q("A map has scale 1 : 40 000. Two towns are 6.5 cm apart on the map. Find "
          "the real distance in kilometres.", "P"),
        Q("A car travels 135 km in 1 hour 30 minutes. Find its average speed.", "P"),
        Q("Which is better value: 750 g for \u00a32.70 or 1.25 kg for \u00a34.25? "
          "Show the unit prices you compare.", "P"),
        Q("Convert 54 km/h to metres per second.", "R"),
        Q("Calculate (\u22127) + 12 \u2212 (\u22125).", "F"),
        Q("Evaluate (\u22123)\u00b2 \u2212 4 \u00d7 (\u22122).", "R"),
        Q("The temperature at 06:00 was \u22124 \u00b0C. It rose 9 \u00b0C by noon "
          "and then fell 6 \u00b0C by 18:00. Find the temperature at 18:00, and "
          "explain which of the two changes mattered more.", "E"),
    ]),
    GAP(8),
]

ANSWERS["R1"] = [
    "3 : 8 (45 : 120, dividing both parts by 15).",
    "One part is \u00a328, so the shares are \u00a3112 and \u00a3140.",
    "560 g: the mass per person is 350 \u00f7 5 = 70 g, and 8 \u00d7 70 = 560 g.",
    "2.6 km: 6.5 \u00d7 40 000 = 260 000 cm = 2 600 m.",
    "90 km/h: 1 hour 30 minutes is 1.5 hours, and 135 \u00f7 1.5 = 90.",
    "The 1.25 kg pack: \u00a30.36 per 100 g for 750 g, against \u00a30.34 per "
    "100 g (\u00a34.25 \u00f7 12.5) for 1.25 kg.",
    "15 m/s: 54 km/h is 54 000 m \u00f7 3 600 s = 15 m/s.",
    "10: (\u22127) + 12 = 5, and 5 \u2212 (\u22125) = 5 + 5 = 10.",
    "17: (\u22123)\u00b2 = 9 and 4 \u00d7 (\u22122) = \u22128, so 9 \u2212 "
    "(\u22128) = 17.",
    "\u22121 \u00b0C: \u22124 + 9 = 5, then 5 \u2212 6 = \u22121. The two "
    "changes have different sizes (9\u00b0 and 6\u00b0), so the rise counts for "
    "more; adding them as if they were equal would misreport the day.",
]
