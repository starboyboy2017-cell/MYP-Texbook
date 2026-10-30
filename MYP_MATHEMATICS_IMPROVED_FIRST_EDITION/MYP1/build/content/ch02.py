"""Chapter 2 - Powers, expanded form and order of operations."""
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.flow import Spacer, Pager
import diagrams as dg
from helpers import (section, lead, body, h3, lst, panel, atl, we, practice, q, fig,
                     diag, table, note, gap, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
    part="Part I \u00b7 Number, structure and proof", part_numeral="I", chapter_no=2,
    kicker="Number, structure and proof",
    title_lines=["Powers, expanded form", "and order of operations"],
    lead_lines=["A power is a compressed instruction: it records how",
                "many copies of a factor to multiply. A shared order",
                "of operations keeps that compression unambiguous."],
    key_concept="Form", related=["Pattern", "Simplification"],
    context="Scientific and technical innovation",
    inquiry_lines=["How does a repeated multiplication become a single symbol,",
                   "and what rules let everyone read that symbol the same way?"])

TITLE = "Powers, expanded form and order of operations"
SHORT = "Powers and order of operations"


def build(bk, p):
    reset_counters(2)
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER", "Concepts, context and the evidence the "
                                           "chapter will produce."))
    p.add(Spacer(8))
    p.add(DataTable(["Statement of inquiry",
                     "Compressing repeated multiplication into a power, and agreeing on "
                     "the order in which operations apply, allows complex calculations to "
                     "be recorded compactly and reproduced reliably by anyone."],
                    [], widths=[1, 3.2], font_size=9.2, stripe=False))
    gap(p, 10)
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Form.** A power is a form that hides its own "
                     "history: 2^{5} does not show the five factors, but they are what the "
                     "symbol means.\n"
                     "**Related \u00b7 Pattern.** Powers of ten generate the pattern behind "
                     "place value and behind scientific notation.\n"
                     "**Related \u00b7 Simplification.** An agreed order of operations is "
                     "what makes a compressed expression mean one thing rather than "
                     "several."))
    p.add(Panel("note", title="Global context \u00b7 Scientific and technical innovation",
                text="Exploration: how measurement and computing depend on notation that "
                     "compresses very large and very small values without losing them. "
                     "A scientist writing 3 \u00d7 10^{8} m/s is using the same structure "
                     "as a student writing 10^{3}."))
    gap(p, 8)
    h3(p, "Inquiry questions")
    lst(p, ["**Factual:** What do the base and the exponent tell you, and how do you "
            "evaluate a power?",
            "**Conceptual:** Why do we need an agreed order of operations, and what would "
            "change if there were none?",
            "**Debatable:** Is \u201cBIDMAS\u201d a mathematical rule or a convention that "
            "could reasonably have been decided differently?"])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Evaluate powers, roots and multi-step expressions accurately."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate the pattern in powers of ten and in the last digit of powers."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Record a calculation with one line per operation and name the rule used."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Use powers to describe storage, growth and distance in real contexts."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 6)
    atl(p, "In order for a student to evaluate a complex expression without losing track, "
           "students must annotate each line with the rule being applied, so that the "
           "working can be audited by someone else.", "ATL \u00b7 Thinking skills")

    # ------------------------------------------------------------ engage
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("02", "ENGAGE", "A warehouse where the counting never stops."))
    body(p, "A grain warehouse receives sacks in pallets. A pallet holds 10 rows of 10 "
            "sacks, so it holds 100. A block of pallets is 10 pallets long, 10 wide and "
            "10 high: 1 000 pallets, or 100 000 sacks. The storekeeper does not write "
            "100 000. She writes 10^{5}, and everyone in the warehouse reads the same "
            "number.")
    fig(p, "ch02_plate_banner.jpg",
        "Stacking makes powers visible. A 10 \u00d7 10 layer is 10^{2}; ten such layers "
        "make 10^{3}; the warehouse simply keeps multiplying by ten, and the notation "
        "keeps up.", wide=True)

    p.add(Stage("03", "EXPLORE", "Build the pattern before naming it."))
    body(p, "Copy and complete this table without a calculator. Write each product as a "
            "single number, then look for what changes between rows.")
    table(p, ["Power", "Meaning", "Value"], [
        ["10^{1}", "10", "10"], ["10^{2}", "10 \u00d7 10", "100"],
        ["10^{3}", "10 \u00d7 10 \u00d7 10", "1 000"],
        ["10^{4}", "\u2026", "\u2026"], ["10^{5}", "\u2026", "\u2026"],
        ["10^{6}", "\u2026", "\u2026"],
    ], widths=[0.7, 1.5, 1.0])
    lst(p, ["How many zeros does 10^{n} have, in terms of `n`?",
            "Predict 10^{9} without calculating it.",
            "Now complete the same table for powers of 2: 2^{1} to 2^{6}. Does the same "
            "kind of pattern hold? What is different?",
            "What would 10^{0} have to be for the pattern to continue downward?"],
        ordered=True)
    panel(p, "keyidea", title="Two patterns, one structure",
          text="Powers of ten grow by adding one zero per step, so the exponent counts the "
               "zeros. Powers of two double at each step, so the exponent counts the "
               "doublings. In both cases the exponent counts **how many copies of the base "
               "are multiplied** \u2014 that is the definition, and every pattern follows "
               "from it.")

    # -------------------------------------------------------------- 2.1
    section(p, "2.1", "From repeated multiplication to powers", "A \u00b7 i",
            ["Form", "Pattern"])
    lead(p, "A power is not a new kind of number. It is a shorter way of writing a "
            "multiplication in which every factor is the same.")
    panel(p, "definition", title="Base, exponent, power",
          text="In `a`^{n}, the **base** `a` is the number being multiplied and the "
               "**exponent** `n` is the number of copies. So `a`^{n} = `a` \u00d7 `a` "
               "\u00d7 \u2026 \u00d7 `a`, with `n` factors. The whole expression is called "
               "a **power** of `a`.")
    body(p, "Read 3^{4} as \u201cthree to the power four\u201d or \u201cthree to the "
            "fourth\u201d. It means 3 \u00d7 3 \u00d7 3 \u00d7 3 = 81. Read 3^{4} "
            "carefully: it is not 3 \u00d7 4. The exponent counts factors, not additions.")
    diag(p, 96, dg.power_stack, "3^{4} as four factors of 3. The exponent counts the "
                                 "factors, not their total.", wide=True)
    panel(p, "error", title="Multiplying the base by the exponent",
          text="3^{4} = 81, not 12. A useful check: 3^{2} = 9 and 3^{3} = 27, so 3^{4} "
               "must be larger again. If your answer is only 12, you have multiplied "
               "instead of repeated the multiplication.")
    h3(p, "The two special exponents")
    lst(p, ["**Exponent 1** means one factor: `a`^{1} = `a`. There is nothing to repeat.",
            "**Exponent 0** means no factors at all, and the value is 1 for every non-zero "
            "base. This is not arbitrary: 10^{3} \u00f7 10 = 10^{2}, 10^{2} \u00f7 10 = "
            "10^{1}, and continuing the pattern forces 10^{1} \u00f7 10 = 10^{0} = 1.",
            "**Exponent 2** is read \u201csquared\u201d and **exponent 3** is read "
            "\u201ccubed\u201d, for reasons that become visible in Chapter 9."])
    we(p, "2.1.1", "Writing a product as a power",
       "Write each product as a single power and evaluate it: (a) 5 \u00d7 5 \u00d7 5 "
       "(b) 2 \u00d7 2 \u00d7 2 \u00d7 2 \u00d7 2 \u00d7 2 (c) 7.",
       ["(a) Three factors of 5, so 5^{3} = 125.",
        "(b) Six factors of 2, so 2^{6} = 64.",
        "(c) One factor of 7, so 7^{1} = 7."],
       answer="(a) 5^{3} = 125  (b) 2^{6} = 64  (c) 7^{1} = 7",
       check="2^{5} = 32, so 2^{6} = 64 \u2713")
    we(p, "2.1.2", "Reading a power in context",
       "A sheet of paper is folded in half six times. How many layers are there, and how "
       "does the answer connect to a power?",
       ["Each fold doubles the number of layers.",
        "After 1 fold: 2 layers = 2^{1}.  After 2 folds: 4 = 2^{2}.  After 3 folds: "
        "8 = 2^{3}.",
        "After 6 folds: 2^{6} = 64 layers.",
        "The exponent equals the number of folds, because each fold is one more doubling."],
       answer="64 layers, which is 2^{6}.",
       check="After 5 folds there are 32; 32 \u00d7 2 = 64 \u2713")
    practice(p, "2.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Write as a power: (a) 4 \u00d7 4 \u00d7 4 (b) 9 \u00d7 9 (c) 6.", "F"),
        q("Evaluate: (a) 2^{3} (b) 5^{2} (c) 10^{4} (d) 3^{0}.", "F"),
        q("Evaluate: (a) 7^{2} (b) 2^{7} (c) 4^{3}.", "F"),
        q("Write 81 as a power of 3, and also as a power of 9.", "F"),
        q("A student writes 4^{3} = 12. Identify the error and give the correct value.",
          "R"),
        q("Explain why 10^{0} = 1 using the pattern of dividing by 10.", "R"),
        q("A rumour is passed to 2 people, each of whom tells 2 more, and so on. How many "
          "people hear it at the fifth telling? Write your answer as a power and as a "
          "number.", "P"),
        q("Which is larger, 2^{10} or 10^{2}? Explain without calculating both fully.",
          "E"),
        q("Find all the powers of 2 between 30 and 100.", "E"),
    ])

    # -------------------------------------------------------------- 2.2
    section(p, "2.2", "Powers of ten and expanded form", "A \u00b7 ii  \u00b7  B \u00b7 i",
            ["Pattern", "Representation"])
    body(p, "Place value is a system built on powers of ten. Every column is ten times the "
            "column on its right, so expanded form can be written with a power in every "
            "term, which is exactly how large numbers are handled in science.")
    panel(p, "definition", title="Expanded form with powers",
          text="A number in base ten can be written as a sum of digits multiplied by "
               "powers of ten: 4 507 = 4 \u00d7 10^{3} + 5 \u00d7 10^{2} + 0 \u00d7 "
               "10^{1} + 7 \u00d7 10^{0}. To the right of the point the exponents are "
               "negative: 0.25 = 2 \u00d7 10^{\u22121} + 5 \u00d7 10^{\u22122}.")
    diag(p, 100, dg.powers_of_ten_ladder, "Moving left multiplies by ten; moving right "
                                          "divides by ten. The exponent records how many "
                                          "moves.", wide=True)
    we(p, "2.2.1", "Writing a large number with powers",
       "Write 6 030 000 in expanded form using powers of ten, then as a single digit "
       "multiplied by a power of ten.",
       ["Count the columns: 6 in the millions, 0 in hundred-thousands, 3 in ten-thousands, "
        "then five zeros.",
        "Expanded: 6 \u00d7 10^{6} + 0 \u00d7 10^{5} + 3 \u00d7 10^{4}.",
        "Because everything after the 3 is zero, the number is 603 \u00d7 10^{4}.",
        "The most compact form keeps one digit before the point: 6.03 \u00d7 10^{6}."],
       answer="6 \u00d7 10^{6} + 3 \u00d7 10^{4}, which equals 6.03 \u00d7 10^{6}.",
       check="6.03 \u00d7 1 000 000 = 6 030 000 \u2713")
    we(p, "2.2.2", "Comparing by exponent",
       "Which is larger, 4.1 \u00d7 10^{5} or 3.9 \u00d7 10^{6}?",
       ["4.1 \u00d7 10^{5} = 410 000.",
        "3.9 \u00d7 10^{6} = 3 900 000.",
        "The second is larger: a higher power of ten outweighs a smaller leading digit."],
       answer="3.9 \u00d7 10^{6} is larger, by a factor of nearly ten.",
       check="Compare exponents first; only compare leading digits when the exponents "
             "agree \u2713")
    practice(p, "2.2", "SUPPORT 1\u20133  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Write in expanded form using powers of ten: (a) 3 400 (b) 70 205 (c) 8 000 000.",
          "F"),
        q("Write as a single number: (a) 5 \u00d7 10^{3} + 2 \u00d7 10^{2} (b) 9 \u00d7 "
          "10^{5}.", "F"),
        q("Write 45 000 as a single digit multiplied by a power of ten.", "F"),
        q("Which is larger, 6.2 \u00d7 10^{4} or 5.8 \u00d7 10^{5}? Explain your reasoning.",
          "R"),
        q("A student writes 3 000 = 3 \u00d7 10^{4}. Explain the error using a place-value "
          "argument.", "R"),
        q("The distance from Earth to the Sun is about 1.5 \u00d7 10^{8} km. Write this as "
          "an ordinary number and state how many zeros it has.", "P"),
        q("Write the year 2026 in expanded form using powers of ten, then explain why the "
          "10^{0} term matters.", "E"),
        q("Create a number whose expanded form contains exactly three non-zero terms and "
          "whose value is between 500 000 and 600 000.", "E"),
    ])

    # -------------------------------------------------------------- 2.3
    section(p, "2.3", "Squares, cubes and roots", "A \u00b7 i, ii", ["Form", "Quantity"])
    body(p, "A square number is a number multiplied by itself. The name is not decorative: "
            "16 counters can be arranged in a 4 by 4 square, and no other square "
            "arrangement uses exactly 16. A cube number fills a cube in the same way.")
    diag(p, 108, dg.squares_and_cubes, "Square numbers are the counters in a square; cube "
                                       "numbers are the cubes in a cube. 5^{2} = 25 and "
                                       "3^{3} = 27.", wide=True)
    panel(p, "definition", title="Square and cube roots",
          text="The **square root** of `n`, written \u221a`n`, is the positive number that "
               "multiplies by itself to give `n`. The **cube root**, written \u00b3\u221a`n`, "
               "is the number that multiplies by itself twice to give `n`. So \u221a49 = 7 "
               "because 7 \u00d7 7 = 49, and \u00b3\u221a27 = 3 because 3 \u00d7 3 "
               "\u00d7 3 = 27.")
    h3(p, "Facts worth knowing by heart")
    table(p, ["Square numbers", "1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144"],
          [["Cube numbers", "1, 8, 27, 64, 125, 216, 343, 512, 729, 1 000"]],
          widths=[0.8, 2.4], first_col_bold=True)
    panel(p, "keyidea", title="Why the square root is always positive",
          text="Both 7 \u00d7 7 and (\u22127) \u00d7 (\u22127) equal 49, but the root sign "
               "\u221a is defined to give the positive value only. In Year 1 you will meet "
               "\u221a49 = 7; the negative solution belongs to equation solving in later "
               "years.")
    we(p, "2.3.1", "Squares, cubes and roots together",
       "Evaluate (a) 6^{2} (b) 6^{3} (c) \u221a81 (d) \u00b3\u221a64.",
       ["(a) 6 \u00d7 6 = 36.", "(b) 6 \u00d7 6 \u00d7 6 = 216.",
        "(c) 9 \u00d7 9 = 81, so \u221a81 = 9.",
        "(d) 4 \u00d7 4 \u00d7 4 = 64, so \u00b3\u221a64 = 4."],
       answer="36, 216, 9 and 4.",
       check="\u221a81 = 9 and 9^{2} = 81; \u00b3\u221a64 = 4 and 4^{3} = 64 \u2713")
    we(p, "2.3.2", "A square with a known area",
       "A square courtyard has an area of 144 m^{2}. Find the length of one side and the "
       "perimeter.",
       ["For a square, area = side^{2}, so side = \u221a144.",
        "\u221a144 = 12, so each side is 12 m.",
        "Perimeter = 4 \u00d7 12 = 48 m."],
       answer="Side 12 m; perimeter 48 m.",
       check="12^{2} = 144 \u2713 and the perimeter has four equal sides \u2713")
    practice(p, "2.3", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Evaluate: (a) 9^{2} (b) 11^{2} (c) 2^{3} (d) 5^{3}.", "F"),
        q("Evaluate: (a) \u221a64 (b) \u221a121 (c) \u00b3\u221a125.", "F"),
        q("Which of these are square numbers: 48, 64, 81, 90, 100?", "F"),
        q("Find two consecutive square numbers whose difference is 15.", "R"),
        q("Explain why 30 cannot be a square number, without using a calculator.", "R"),
        q("A square tile has an area of 196 cm^{2}. Find its side length and its perimeter.",
          "P"),
        q("A cubic tank holds 512 litres. Find its edge length in centimetres, given that "
          "1 litre = 1 000 cm^{3}.", "P"),
        q("Is the square of an even number always even? Test three cases and explain the "
          "pattern.", "E"),
        q("Find the smallest whole number that must be added to 50 to make a square "
          "number, and the smallest that must be subtracted.", "E"),
    ])

    # -------------------------------------------------------------- 2.4
    section(p, "2.4", "Order of operations", "A \u00b7 iii  \u00b7  C \u00b7 i",
            ["System", "Simplification"])
    body(p, "Consider 2 + 3 \u00d7 4. Read left to right, it gives 20. Read with "
            "multiplication first, it gives 14. Both readings are possible in English; "
            "only one is mathematics. The convention exists because an expression written "
            "once has to mean one thing to everybody who reads it.")
    panel(p, "definition", title="The agreed order",
          text="**1** Brackets and other grouping symbols. **2** Indices (powers and "
               "roots). **3** Multiplication and division, from left to right. "
               "**4** Addition and subtraction, from left to right. An expression with "
               "brackets inside brackets is worked from the innermost pair outward.")
    panel(p, "keyidea", title="Multiplication and division have equal priority",
          text="24 \u00f7 4 \u00d7 2 is 12, not 3, because division and multiplication rank "
               "equally and are worked left to right. The rule is not \u201cdivision before "
               "multiplication\u201d; it is \u201cwhichever comes first, working left to "
               "right\u201d.")
    we(p, "2.4.1", "Two operations",
       "Evaluate 5 + 2 \u00d7 3^{2}.",
       ["Indices first: 3^{2} = 9, so the expression becomes 5 + 2 \u00d7 9.",
        "Multiplication next: 2 \u00d7 9 = 18, giving 5 + 18.",
        "Addition last: 5 + 18 = 23."],
       answer="23",
       check="Estimate: 3^{2} is 9 and 2 \u00d7 9 = 18, so the total is about 23 \u2713")
    we(p, "2.4.2", "Brackets change the structure",
       "Evaluate (5 + 2) \u00d7 3^{2} and explain why it differs from Worked example "
       "2.4.1.",
       ["Brackets first: 5 + 2 = 7.",
        "Indices: 3^{2} = 9, so the expression is 7 \u00d7 9.",
        "7 \u00d7 9 = 63.",
        "In 2.4.1 the 5 was added to the product; here the 5 is added to the 2 before "
        "multiplying, so the 5 is multiplied by 9 as well."],
       answer="63, compared with 23 in 2.4.1.",
       check="63 \u2212 23 = 40 = 5 \u00d7 (9 \u2212 1): the bracket multiplied the 5 by "
             "9 rather than by 1 \u2713")
    we(p, "2.4.3", "A longer chain",
       "Evaluate 36 \u00f7 6 + 3 \u00d7 (8 \u2212 2)^{2}.",
       ["Innermost bracket: 8 \u2212 2 = 6.",
        "Index: 6^{2} = 36.",
        "Multiplication and division, left to right: 36 \u00f7 6 = 6 and 3 \u00d7 36 = "
        "108.",
        "Addition: 6 + 108 = 114."],
       answer="114",
       check="Reverse the order of the two middle steps and check that the answer is "
             "unchanged, because the two operations are independent \u2713")
    panel(p, "error", title="Working strictly left to right",
          text="A student evaluates 4 + 6 \u00f7 2 as 5 by adding first. The correct value "
               "is 7, because the division happens before the addition. If you want the "
               "addition first, you must write (4 + 6) \u00f7 2, which is 5. The brackets "
               "are the instruction.")
    practice(p, "2.4", "SUPPORT 1\u20133  \u00b7  CORE 1\u20136  \u00b7  EXTENSION 7\u20138", [
        q("Evaluate 8 + 2 \u00d7 5.", "F"),
        q("Evaluate 20 \u2212 3 \u00d7 4.", "F"),
        q("Evaluate: (a) 6 + 4^{2} (b) (6 + 4)^{2} (c) 2^{3} + 3^{2}.", "F"),
        q("Evaluate: (a) 24 \u00f7 4 \u00d7 2 (b) 24 \u00f7 (4 \u00d7 2) (c) 36 \u00f7 6 + 3.",
          "F"),
        q("Evaluate 5 \u00d7 2^{3} \u2212 3^{2}, showing each stage of your working.", "F"),
        q("Insert brackets to make each statement true: (a) 3 + 5 \u00d7 2 = 16 "
          "(b) 12 \u2212 4 \u00d7 2 = 16 (c) 18 \u00f7 3 + 6 = 2.", "R"),
        q("A student calculates 12 + 6 \u00f7 3 as 18 \u00f7 3 = 6. Identify the mistake, "
          "give the correct value, and explain which operation should be performed first.",
          "R"),
        q("Use the digits 2, 3 and 4 once each, with any operations and brackets, to make "
          "as many different values as you can. Record at least four expressions and their "
          "values; one expression must contain an index.", "E"),
    ])

    # -------------------------------------------------------------- 2.5
    section(p, "2.5", "Substitution and expressions with powers", "A \u00b7 iii",
            ["Form", "Model"])
    body(p, "A letter in an expression stands for a number. Substitution means replacing "
            "the letter with a value and evaluating the resulting expression using the "
            "order of operations. The position of the letter inside a power matters.")
    we(p, "2.5.1", "Same substitution, different structure",
       "Evaluate 3`x`^{2} and (3`x`)^{2} when `x` = 4, and explain why the results "
       "differ.",
       ["In 3`x`^{2} the exponent applies only to `x`: 3`x`^{2} = 3 \u00d7 (4)^{2} = "
        "3 \u00d7 16 = 48.",
        "In (3`x`)^{2} the brackets make 3`x` the base: (3 \u00d7 4)^{2} = 12^{2} = 144.",
        "The bracket changes the base of the power. Without it, only `x` is squared. The "
        "second result is three times the first because (3`x`)^{2} = 3^{2} \u00d7 `x`^{2} "
        "= 9`x`^{2}."],
       answer="3`x`^{2} = 48 and (3`x`)^{2} = 144.",
       check="48 \u00d7 3 = 144 \u2713")
    we(p, "2.5.2", "Evaluating formulas",
       "(a) The area of a square is `A` = `s`^{2}. Find `A` when `s` = 7 cm. (b) The "
       "volume of a cube is `V` = `s`^{3}. Find `V` when `s` = 4 cm. (c) A model for the "
       "distance fallen by an object is `d` = 5`t`^{2}, with `d` in metres and `t` in "
       "seconds. Find `d` when `t` = 3.",
       ["(a) Substitute `s` = 7: `A` = 7^{2} = 49 cm^{2}.",
        "(b) Substitute `s` = 4: `V` = 4^{3} = 64 cm^{3}.",
        "(c) Substitute `t` = 3: `d` = 5 \u00d7 3^{2} = 5 \u00d7 9 = 45 m."],
       answer="(a) 49 cm^{2}  (b) 64 cm^{3}  (c) 45 m",
       check="In (c), the index is applied before the multiplication by 5 \u2713")
    panel(p, "note", title="Why substitution is a test of structure",
          text="Two expressions that look similar can behave differently once a value is "
               "inserted. Comparing 3`x`^{2} with (3`x`)^{2}, or `x`^{2} with 2`x`, shows "
               "exactly where the exponent applies \u2014 which is the same question you "
               "will ask of every formula in Chapters 6 and 9.")
    practice(p, "2.5", "SUPPORT 1\u20133  \u00b7  CORE 1\u20136  \u00b7  EXTENSION 7\u20138", [
        q("Evaluate `x`^{2} for (a) `x` = 3 (b) `x` = 6 (c) `x` = 10.", "F"),
        q("Evaluate 2`x`^{2} for (a) `x` = 3 (b) `x` = 6 (c) `x` = 10. Compare each result "
          "with the corresponding result in question 1.", "F"),
        q("For `a` = 2 and `b` = 5, evaluate `a`^{2} + `b`^{2} and (`a` + `b`)^{2}. Are "
          "they equal?", "F"),
        q("A square has side length 9 cm. Use `A` = `s`^{2} to find its area, with units.",
          "P"),
        q("Use `V` = `s`^{3} to find the volume of a cube with edge (a) 3 cm (b) 5 cm.",
          "F"),
        q("The distance-fallen model is `d` = 5`t`^{2}. Find `d` when (a) `t` = 2 "
          "(b) `t` = 4. Explain why doubling `t` does not double `d`.", "R"),
        q("Insert one pair of brackets to make each statement true: (a) 2 + 3^{2} = 25 "
          "(b) 4 \u00d7 3^{2} = 144. Explain how the brackets change the base.", "R"),
        q("A square has area 121 cm^{2}. Find its side length. If the side length is "
          "tripled, find the new area and explain how 3^{2} appears in your answer.", "E"),
    ])

    # ------------------------------------------------------- investigate
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("04", "INVESTIGATE", "A pattern that hides in the last digit."))
    section(p, "Investigation 2", "The doubling sheet", None, ["Pattern", "Form"])
    body(p, "Fold a sheet of paper in half repeatedly. Each fold doubles the number of "
            "layers. Record the layer count and the thickness, then look for structure "
            "rather than arithmetic.")
    table(p, ["Folds", "Layers", "As a power of 2", "Thickness if each sheet is 0.1 mm"], [
        ["0", "1", "2^{0}", "0.1 mm"], ["1", "2", "2^{1}", "0.2 mm"],
        ["2", "4", "2^{2}", "0.4 mm"], ["3", "8", "2^{3}", "0.8 mm"],
        ["4", "16", "2^{4}", "1.6 mm"], ["\u2026", "\u2026", "\u2026", "\u2026"],
    ], widths=[0.6, 0.8, 1.0, 1.8])
    h3(p, "Your investigation")
    lst(p, ["Continue the table to 10 folds.",
            "Describe how the thickness changes from row to row, in one sentence.",
            "Predict the thickness after 20 folds, then calculate it.",
            "Write a rule for the thickness after `n` folds, starting from 0.1 mm.",
            "A ream of 500 sheets is about 5 cm thick. After how many folds does the stack "
            "exceed the height of your classroom (about 3 m)?",
            "Explain why the answer to the last question surprises most people."],
        ordered=True)
    panel(p, "keyidea", title="What the investigation shows",
          text="Doubling is a power of 2, and powers grow far faster than most people "
               "expect. After 20 folds the stack is 2^{20} \u00d7 0.1 mm \u2248 105 m. The "
               "pattern is exponential: each step multiplies rather than adds, so the "
               "graph curves upward rather than rising in a straight line.")
    atl(p, "In order for a student to trust a surprising result, students must check it "
           "against a smaller case where the answer can be counted directly, and then "
           "confirm that the same operation produces both.", "ATL \u00b7 Critical thinking")
    gap(p, 8)
    p.add(Stage("05", "APPLY", "Storage, growth and distance in a real setting."))
    section(p, "Real-life application", "The school data store", "D \u00b7 i\u2013iv",
            ["Quantity", "Model"])
    body(p, "A media club stores video projects on a server with three drives. The labels "
            "use powers of ten: one drive holds 2 \u00d7 10^{11} bytes, a second holds "
            "5 \u00d7 10^{11} bytes and a third holds 1.2 \u00d7 10^{12} bytes. A single "
            "lesson video is about 4 \u00d7 10^{8} bytes.")
    h3(p, "Your task")
    lst(p, ["Write the total capacity in bytes, using a single power of ten.",
            "Estimate how many lesson videos will fit, showing your estimate as a power of "
            "ten.",
            "Calculate the number more precisely, to two significant figures.",
            "The club records 30 lessons. Does the storage suffice? Justify with a "
            "calculation.",
            "Explain why the answer to question 2 is an estimate rather than a fact."],
        ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Recognise the quantities involved and their units.",
                 "Select powers of ten as an appropriate strategy.",
                 "Apply the strategy accurately, keeping track of exponents.",
                 "Justify whether the conclusion about storage is reasonable."])
    gap(p, 8)
    p.break_page()
    p.add(Stage("06", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "A power primer for the science lab", "A \u00b7 i  \u00b7  C \u00b7 ii, iii", [])
    body(p, "**Context.** The science department is producing a one-page reference card "
            "for Year 1 students. It will be pinned beside the microscopes. The card must "
            "explain powers, squares, cubes, roots and the order of operations for a "
            "reader who has not yet studied this chapter.")
    body(p, "**Product.** A card using no more than 180 words of explanation, plus "
            "diagrams and one fully worked example, readable from about one metre.")
    lst(p, ["Define power, base and exponent, using 2^{5} as your example.",
            "Explain 10^{3} and 10^{0} with a pattern that makes clear why 10^{0} is 1 "
            "rather than 0.",
            "Show 4^{2} as a square of 16 unit squares and explain why \u201csquare\u201d "
            "is a suitable name.",
            "Work through 4 + 3 \u00d7 2^{2}, one line per operation, labelling the rule "
            "used each time.",
            "Explain the difference between 3`x`^{2} and (3`x`)^{2} when `x` = 2. State "
            "both values.",
            "Include a science example: a culture of 500 bacteria doubles every hour. "
            "Write an expression for the number after `h` hours and find the number after "
            "5 hours.",
            "Ask a classmate to use your card to evaluate 2 + 4 \u00d7 3^{2}. Record "
            "whether they succeed, then revise one part of the card.",
            "Evaluate your card: one strength, one limitation and one change you would "
            "make for a younger audience."],
        ordered=True)
    criteria_panel(p,
                   a="i: accurate definitions and calculations throughout the card.",
                   c="ii, iii: precise notation, a clear diagram and awareness of the "
                     "reader.")

    # ---------------------------------------------------------- reflect
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("07", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, ["A power records repeated multiplication; the exponent counts factors, not "
            "additions.",
            "Powers of ten generate place value, so expanded form can be written with "
            "exponents.",
            "Square and cube numbers correspond to square and cube arrangements; roots "
            "reverse them.",
            "One agreed order of operations makes a written expression mean exactly one "
            "thing.",
            "Substitution tests the structure of an expression: where a symbol sits "
            "decides what it does."])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["base", "The number that is multiplied repeatedly in a power."],
        ["exponent / index", "The number of copies of the base."],
        ["power", "A product of equal factors, or the whole expression `a`^{n}."],
        ["square number", "The product of a number with itself."],
        ["cube number", "The product of three equal factors."],
        ["square root", "The positive number whose square is the given number."],
        ["substitution", "Replacing a letter by a number and evaluating."],
    ], widths=[0.85, 2.3])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that persist",
          text="**3^{4} = 12.** Powers are not multiplications of base by exponent.\n"
               "**Multiplication always before division.** They rank equally; work left to "
               "right.\n"
               "**\u2212144 = 12.** Roots give positive values in Year 1; the negative "
               "solution arises from equations, not from the root sign.")
    assessment_close(p, [
        ["write a repeated product as a power", "\u25a1", "\u25a1", "\u25a1"],
        ["evaluate powers, squares, cubes and roots", "\u25a1", "\u25a1", "\u25a1"],
        ["write a number using powers of ten", "\u25a1", "\u25a1", "\u25a1"],
        ["apply the order of operations", "\u25a1", "\u25a1", "\u25a1"],
        ["substitute into an expression with a power", "\u25a1", "\u25a1", "\u25a1"],
        ["explain the difference between 3`x`^{2} and (3`x`)^{2}", "\u25a1", "\u25a1",
        "\u25a1"],
        
    ],
        "In order for a student to identify which rule still causes errors, students "
               "must redo one question from the weakest row without looking at the worked "
               "example, then compare their lines with the model.",
        next_title="Chapter 3 · Factors, multiples and primes")


    # ------------------------------------------------------ mixed practice
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("08", "MIXED PRACTICE"))
    practice(p, "Mixed practice 2",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201311  \u00b7  EXTENSION 10\u201314", [
        q("Evaluate: (a) 4^{3} (b) 10^{3} (c) \u221a100 (d) \u00b3\u221a8.", "F"),
        q("Write 5 \u00d7 5 \u00d7 5 \u00d7 5 as a power and evaluate it.", "F"),
        q("Evaluate 7 + 3 \u00d7 2^{2}.", "F"),
        q("Write 90 300 in expanded form using powers of ten.", "F"),
        q("Evaluate (a) 2^{5} (b) 3^{4} \u2212 3^{2} (c) 100 \u2212 4^{2}.", "F"),
        q("Insert brackets to make 2 + 4 \u00d7 3 = 18 true.", "R"),
        q("Explain why 2^{10} is greater than 10^{2} even though 10 is greater than 2.",
          "R"),
        q("A square garden has an area of 225 m^{2}. Find the length of fencing needed to "
          "enclose it.", "P"),
        q("Evaluate 3`x`^{2} + 2`x` when `x` = 4.", "P"),
        q("A sheet of paper is 0.08 mm thick. How thick is a stack of 2^{10} sheets? Give "
          "your answer in millimetres and in metres.", "P"),
        q("Explain, using an example, why 10^{0} = 1 and not 0.", "R"),
        q("Find a two-digit number that is both a square number and a cube number. Explain "
          "why it is the only one below 100.", "E"),
        q("The number 64 can be written as a power of 2, a power of 4 and a power of 8. "
          "Write all three.", "E"),
        q("Investigate the last digit of 2^{1}, 2^{2}, 2^{3}, \u2026 and describe the cycle. "
          "Predict the last digit of 2^{20}.", "E"),
    ])
    gap(p, 8)
    p.add(Stage("09", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20133", "Revisit 2.1 and 2.4: write the meaning of the power before "
                    "evaluating."],
        ["4\u20136", "Revisit 2.2: count the columns from the right and name each "
                    "exponent."],
        ["7\u20139", "Revisit 2.3 and 2.5: draw the square or substitute slowly."],
        ["10\u201312", "Revisit the investigation: doubling is a power of 2."],
        ["13\u201314", "Revisit 2.1 and 2.3: list the powers in order and look at the "
                      "digits."],
    ], widths=[0.7, 2.6])


ANSWERS = [
    ("2.1", "1 (a) 4^{3} (b) 9^{2} (c) 6^{1}.  2 (a) 8 (b) 25 (c) 10 000 (d) 1.  "
            "3 (a) 49 (b) 128 (c) 64.  4 3^{4} = 81 = 9^{2}.  5 4^{3} = 64, not 12.  "
            "7 2^{5} = 32 people.  8 2^{10} = 1 024 > 100.  9 32 and 64."),
    ("2.2", "1 (a) 3 \u00d7 10^{3} + 4 \u00d7 10^{2} (b) 7 \u00d7 10^{4} + 2 \u00d7 "
            "10^{2} + 5 \u00d7 10^{0} (c) 8 \u00d7 10^{6}.  2 (a) 5 200 (b) 900 000.  "
            "3 4.5 \u00d7 10^{4}.  4 5.8 \u00d7 10^{5} is larger: a higher power of ten "
            "dominates.  5 3 000 = 3 \u00d7 10^{3}: three zeros means exponent 3.  "
            "6 150 000 000 km; eight zeros.  7 2 \u00d7 10^{3} + 0 \u00d7 10^{2} + "
            "2 \u00d7 10^{1} + 6 \u00d7 10^{0}."),
    ("2.3", "1 (a) 81 (b) 121 (c) 8 (d) 125.  2 (a) 8 (b) 11 (c) 5.  3 64, 81, 100.  "
            "4 49 and 64.  5 30 lies between 25 and 36.  6 14 cm; 56 cm.  7 80 cm.  "
            "9 Add 14 (64) and subtract 1 (49)."),
    ("2.4", "1 18.  2 8.  3 (a) 22 (b) 100 (c) 17.  4 (a) 12 (b) 3 (c) 9.  5 31.  "
            "6 (a) (3 + 5) \u00d7 2 (b) (12 \u2212 4) \u00d7 2 (c) 18 \u00f7 (3 + 6).  "
            "7 6 \u00f7 3 = 2 first, so 12 + 2 = 14."),
    ("2.5", "1 (a) 9 (b) 36 (c) 100.  2 (a) 18 (b) 72 (c) 200 \u2014 each is double "
            "question 1.  3 29 and 49; not equal.  4 81 cm^{2}.  5 (a) 27 cm^{3} "
            "(b) 125 cm^{3}.  6 (a) 20 m (b) 80 m; doubling `t` multiplies `d` by 4 "
            "because `t` is squared.  7 (a) (2 + 3)^{2} (b) (4 \u00d7 3)^{2}.  8 11 cm; "
            "new area 1 089 cm^{2} = 9 \u00d7 121."),
    ("Investigation 2", "10 folds: 1 024 layers, 102.4 mm. 20 folds: 2^{20} \u00d7 0.1 mm "
                        "\u2248 104.9 m. Thickness after `n` folds = 0.1 \u00d7 2^{n} mm. "
                        "About 15 folds exceeds 3 m."),
    ("Mixed 2", "1 (a) 64 (b) 1 000 (c) 10 (d) 2.  2 5^{4} = 625.  3 19.  "
                "4 9 \u00d7 10^{4} + 0 \u00d7 10^{3} + 3 \u00d7 10^{2}.  5 (a) 32 (b) 72 "
                "(c) 84.  6 (2 + 4) \u00d7 3.  8 60 m.  9 56.  10 81.92 mm \u2248 "
                "0.082 m.  12 64 = 2^{6} = 4^{3} = 8^{2}.  14 Cycle 2, 4, 8, 6; "
                "2^{20} ends in 6."),
]
