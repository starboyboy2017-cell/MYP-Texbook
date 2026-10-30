"""Chapter 4 - Fractions and decimals."""
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.flow import Spacer, Pager
import diagrams as dg
from helpers import (section, lead, body, h3, lst, panel, atl, we, practice, q, fig,
                     diag, table, note, gap, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
    part="Part II \u00b7 Fractions, decimals and percentages", part_numeral="II",
    chapter_no=4,
    kicker="Fractions, decimals and percentages",
    title_lines=["Fractions and decimals"],
    lead_lines=["A fraction is not a piece of a cake; it is a number",
                "with a position on the line. Once you can see that,",
                "the four operations stop being separate rules and",
                "become consequences of one idea."],
    key_concept="Relationships", related=["Equivalence", "Quantity"],
    context="Identities and relationships",
    inquiry_lines=["How can two different-looking fractions name the same number,",
                   "and what does that equivalence let us do that we could not do"])

TITLE = "Fractions and decimals"
SHORT = "Fractions and decimals"


def build(bk, p):
    reset_counters(4)
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER"))
    p.add(Spacer(8))
    p.add(DataTable(["Statement of inquiry",
                     "A fraction, a decimal and a percentage are three notations for the "
                     "same relationship between a part and a whole, and equivalence is the "
                     "idea that lets us choose whichever notation makes the current "
                     "question easiest."],
                    [], widths=[1, 3.2], font_size=9.2, stripe=False))
    gap(p, 10)
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Relationships.** A fraction records a "
                     "relationship between two quantities, which is why the same "
                     "relationship has many names.\n"
                     "**Related \u00b7 Equivalence.** Multiplying numerator and denominator "
                     "by the same number changes the writing without changing the number.\n"
                     "**Related \u00b7 Quantity.** A fraction of a quantity is found by "
                     "dividing, then multiplying \u2014 in that order."))
    p.add(Panel("note", title="Global context \u00b7 Identities and relationships",
                text="Exploration: how shared resources, recipes and measurements are "
                     "divided, and why a fair share needs an exact number rather than an "
                     "impression."))
    gap(p, 8)
    h3(p, "Inquiry questions")
    lst(p, ["**Factual:** How do you convert between a fraction, a decimal and a "
            "percentage?",
            "**Conceptual:** Why does multiplying the numerator and denominator by the same "
            "number not change the value?",
            "**Debatable:** Is it more honest to report a share as 1/3 or as 33 %?"])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Convert, compare, order and calculate with fractions and decimals."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate which fractions give terminating decimals and why."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Show working with equivalent fractions so the method is auditable."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Scale a recipe and cost a kitchen for a larger number of people."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 6)
    atl(p, "In order for a student to add fractions with different denominators, students "
           "must first decide on a common unit and rewrite both quantities in it, just as "
           "they would convert metres and centimetres before adding.", "ATL \u00b7 Thinking skills")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("02", "ENGAGE", "The tailor's strip."))
    body(p, "A tailor has a strip of cloth 1 metre long and needs to cut lengths of "
            "\u00be m. She can cut one, and has \u00bc m left over. Someone else needs "
            "\u2154 m from a second strip. How much cloth do the two customers need "
            "together? The answer \u2014 one whole metre and five twelfths \u2014 only "
            "appears once both fractions are measured in the same unit.")
    fig(p, "ch04_plate_banner.jpg",
        "Cutting a strip into equal parts is the physical origin of a fraction: the "
        "denominator is the number of equal parts, the numerator the number taken.",
        wide=True)

    p.add(Stage("03", "EXPLORE", "Find the equivalence before being taught it."))
    body(p, "Fold a strip of paper into halves, then fold again to make quarters, then "
            "again to make eighths. Write the fraction of the strip that is shaded at each "
            "stage, and look at what happens to the numbers.")
    diag(p, 108, dg.fraction_strips_full, "The same shaded length written three ways. The "
                                          "number of parts increases at every row; the "
                                          "amount of strip does not change.", wide=True)
    lst(p, ["What happens to the numerator and denominator when you double the number of "
            "parts?",
            "Write the pattern as a rule using words, not symbols.",
            "Predict the next two fractions in the sequence \u00bd, 2/4, 4/8, \u2026",
            "Why can you not simply add the numerators and denominators to find an "
            "equivalent fraction?"], ordered=True)
    panel(p, "keyidea", title="The rule you found",
          text="Multiplying the numerator and the denominator by the same number produces "
               "an equivalent fraction, because the number of parts and the number taken "
               "both increase in the same proportion.")

    # --------------------------------------------------------------- 4.1
    section(p, "4.1", "Equivalent fractions and simplest form", "A \u00b7 i",
            ["Equivalence", "Simplification"])
    panel(p, "definition", title="Equivalent fractions",
          text="Two fractions are **equivalent** when they name the same point on the "
               "number line. Multiplying or dividing both the numerator and denominator by "
               "the same non-zero number produces an equivalent fraction: 3/4 = 6/8 = 9/12.")
    body(p, "**Simplest form** (also called lowest terms) is the equivalent fraction in "
            "which the numerator and denominator share no factor other than 1. It is not "
            "the \u201cbest\u201d fraction in every context \u2014 6/8 is easier to add to "
            "1/8 \u2014 but it is the standard form for an answer.")
    we(p, "4.1.1", "Reducing to simplest form",
       "Write 36/48 in simplest form.",
       ["Find the highest common factor of 36 and 48.",
        "36 = 2^{2} \u00d7 3^{2} and 48 = 2^{4} \u00d7 3, so the HCF is 2^{2} \u00d7 3 = 12.",
        "Divide both parts by 12: 36 \u00f7 12 = 3 and 48 \u00f7 12 = 4.",
        "So 36/48 = 3/4."],
       answer="3/4",
       check="3 \u00d7 12 = 36 and 4 \u00d7 12 = 48, so the fractions are equivalent \u2713")
    we(p, "4.1.2", "Building an equivalent fraction",
       "Write 2/5 with a denominator of 35.",
       ["Ask what 5 must be multiplied by to reach 35: 5 \u00d7 7 = 35.",
        "Multiply the numerator by the same number: 2 \u00d7 7 = 14.",
        "So 2/5 = 14/35."],
       answer="14/35",
       check="14 \u00f7 35 = 0.4 and 2 \u00f7 5 = 0.4 \u2713")
    panel(p, "error", title="Adding the same number instead of multiplying",
          text="A student writes 2/5 = 3/6 by adding 1 to each part. That changes the value: "
               "2/5 = 0.4 but 3/6 = 0.5. Equivalence is produced by multiplying or dividing, "
               "never by adding or subtracting.")
    practice(p, "4.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 7\u20139", [
        q("Write two fractions equivalent to (a) 1/2 (b) 3/5 (c) 7/10.", "F"),
        q("Write in simplest form: (a) 8/12 (b) 15/25 (c) 18/24.", "F"),
        q("Write 4/7 with a denominator of 42.", "F"),
        q("Which of these are equivalent to 2/3: 8/12, 10/16, 6/9, 12/20?", "F"),
        q("Explain why multiplying numerator and denominator by the same number keeps the "
          "value unchanged.", "R"),
        q("A recipe uses 3/8 of a bag of rice. Write this with a denominator of 24 and "
          "explain what the new numbers mean in the recipe.", "P"),
        q("Is 6/8 always written as 3/4? Give a context in which 6/8 is the more useful "
          "form.", "R"),
        q("Find a fraction equivalent to 2/3 with a numerator of 14.", "E"),
        q("How many fractions with a denominator less than 30 are equal to 1/3? List them.",
          "E"),
    ])

    # --------------------------------------------------------------- 4.2
    section(p, "4.2", "Comparing and ordering fractions", "A \u00b7 ii  \u00b7  C \u00b7 iii",
            ["Equivalence", "Quantity"])
    body(p, "Fractions can be compared in three ways, and the choice depends on the "
            "numbers. Use the same denominator when the parts are easy to find; compare "
            "against a half or a whole when the fractions are close to an obvious landmark; "
            "and convert to decimals when precision matters.")
    panel(p, "keyidea", title="Three strategies",
          text="**Common denominator.** 3/5 and 5/8 become 24/40 and 25/40, so 5/8 is "
               "larger.\n**Landmark.** 5/9 is more than a half (since 4.5/9 is a half), "
               "and 3/7 is less than a half, so 5/9 > 3/7.\n**Decimal.** 3/5 = 0.6 and "
               "5/8 = 0.625.")
    we(p, "4.2.1", "Ordering with a common denominator",
       "Write 2/3, 3/4 and 5/8 in order from smallest to largest.",
       ["The denominators 3, 4 and 8 have LCM 24.",
        "2/3 = 16/24; 3/4 = 18/24; 5/8 = 15/24.",
        "Compare the numerators: 15 < 16 < 18.",
        "So 5/8 < 2/3 < 3/4."],
       answer="5/8 < 2/3 < 3/4",
       check="As decimals: 0.625 < 0.667 < 0.75 \u2713")
    we(p, "4.2.2", "Using a landmark to decide quickly",
       "Which is larger, 7/12 or 9/16?",
       ["Both are more than a half, so the landmark does not separate them.",
        "Use a common denominator: 48 is the LCM of 12 and 16.",
        "7/12 = 28/48 and 9/16 = 27/48.",
        "So 7/12 is larger by 1/48."],
       answer="7/12 is larger.",
       check="7/12 \u2248 0.583 and 9/16 \u2248 0.563 \u2713")
    practice(p, "4.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Insert < or >: (a) 3/5 \u2026 2/3 (b) 5/8 \u2026 7/12.", "F"),
        q("Order from smallest: 1/2, 2/5, 3/8, 7/16.", "F"),
        q("Which is larger, 4/7 or 5/9? Use a common denominator.", "F"),
        q("Write a fraction between 1/2 and 2/3 with a denominator of 12.", "F"),
        q("Explain how you can tell that 11/20 is larger than 1/2 without calculating.",
          "R"),
        q("A student says 3/8 > 2/5 because 3 > 2 and 8 > 5. Explain why this reasoning "
          "fails.", "R"),
        q("Three students run 3/8, 0.4 and 2/5 of a kilometre. Who runs furthest? Justify.",
          "P"),
        q("Find the fraction exactly halfway between 1/3 and 1/2.", "E"),
    ])

    # --------------------------------------------------------------- 4.3
    section(p, "4.3", "Adding and subtracting fractions", "A \u00b7 iii", ["Equivalence"])
    body(p, "You cannot add quantities measured in different units, and a fraction is a "
            "measurement in units of 1/`n`. Adding 1/2 and 1/3 requires rewriting both in "
            "units of 1/6, exactly as adding 1 m and 30 cm requires converting to the same "
            "unit first.")
    diag(p, 88, dg.fraction_addition, "1/2 + 1/3 becomes 3/6 + 2/6. The common denominator "
                                      "is the common unit.", wide=True)
    panel(p, "definition", title="The method",
          text="To add or subtract fractions: **1** find a common denominator (the LCM of "
               "the denominators is efficient but any common multiple works); **2** rewrite "
               "each fraction with that denominator; **3** add or subtract the numerators; "
               "**4** simplify if possible.")
    we(p, "4.3.1", "Adding with different denominators",
       "Calculate 3/4 + 5/6, giving the answer in simplest form.",
       ["LCM of 4 and 6 is 12.",
        "3/4 = 9/12 and 5/6 = 10/12.",
        "9/12 + 10/12 = 19/12.",
        "19/12 is already in simplest form; as a mixed number it is 1 and 7/12."],
       answer="19/12 = 1 7/12",
       check="Estimate: 0.75 + 0.83 = 1.58, and 19/12 \u2248 1.58 \u2713")
    we(p, "4.3.2", "Subtracting from a whole",
       "Calculate 3 \u2212 5/8.",
       ["Write 3 as 24/8.",
        "24/8 \u2212 5/8 = 19/8.",
        "As a mixed number: 2 and 3/8."],
       answer="19/8 = 2 3/8",
       check="2.375 + 0.625 = 3 \u2713")
    panel(p, "error", title="Adding the denominators",
          text="1/2 + 1/3 is not 2/5. Two-fifths is smaller than a half, but the sum of two "
               "positive fractions must be larger than either. An estimate catches the error "
               "immediately: 0.5 + 0.33 = 0.83, not 0.4.")
    practice(p, "4.3", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Calculate: (a) 1/5 + 2/5 (b) 3/8 + 1/8 (c) 7/10 \u2212 3/10.", "F"),
        q("Calculate: (a) 1/2 + 1/3 (b) 2/3 + 1/4 (c) 3/4 \u2212 1/2.", "F"),
        q("Calculate 5/6 + 3/8, in simplest form.", "F"),
        q("Calculate: (a) 2 \u2212 3/5 (b) 4 1/4 + 2 1/2.", "F"),
        q("Explain why a common denominator is needed before adding.", "R"),
        q("A tank is 3/8 full in the morning and 1/2 full after rain. What fraction of the "
          "tank is now full, and how much more can it hold?", "P"),
        q("Find two fractions whose sum is 1 and whose difference is 1/3.", "E"),
        q("Calculate 1/2 + 1/4 + 1/8 and describe the pattern in the answer.", "E"),
        q("A student calculates 5/6 \u2212 1/3 = 4/3. Diagnose the error and give the "
          "correct answer.", "R"),
    ])

    # --------------------------------------------------------------- 4.4
    section(p, "4.4", "Multiplying and dividing fractions", "A \u00b7 iii", ["Quantity"])
    body(p, "Multiplication of fractions needs no common denominator, because multiplying "
            "does not combine unlike units \u2014 it takes a part of a part. A third of a "
            "half is a sixth: 1/3 \u00d7 1/2 = 1/6, and the picture makes the reason obvious.")
    diag(p, 110, dg.fraction_multiplication, "A third of a half is one sixth. Multiplying "
                                             "numerators and denominators corresponds to "
                                             "multiplying the numbers of rows and columns in "
                                             "the grid.", wide=True)
    panel(p, "definition", title="The rules",
          text="**Multiply:** multiply numerators together and denominators together. "
               "Simplify before multiplying if you can. **Divide:** multiply by the "
               "reciprocal of the second fraction \u2014 3/4 \u00f7 2/5 = 3/4 \u00d7 5/2. "
               "The **reciprocal** of a fraction is the fraction turned upside down.")
    panel(p, "keyidea", title="Why division becomes multiplication",
          text="Dividing by 2/5 asks \u201chow many two-fifths fit into the quantity?\u201d "
               "One whole contains 5/2 halves of two-fifths, so dividing by 2/5 is the same "
               "as multiplying by 5/2. Division by a fraction counts how many of that "
               "fraction fit.")
    we(p, "4.4.1", "Multiplying and simplifying early",
       "Calculate 5/8 \u00d7 4/15, in simplest form.",
       ["Look for common factors before multiplying: 4 and 8 share 4; 5 and 15 share 5.",
        "Cancel: 5/8 \u00d7 4/15 = (1 \u00d7 1)/(2 \u00d7 3).",
        "Multiply: 1/6."],
       answer="1/6",
       check="5/8 = 0.625 and 4/15 \u2248 0.267, and 0.625 \u00d7 0.267 \u2248 0.167 = 1/6 "
             "\u2713")
    we(p, "4.4.2", "Dividing by a fraction",
       "Calculate 3/5 \u00f7 2/7.",
       ["The reciprocal of 2/7 is 7/2.",
        "3/5 \u00d7 7/2 = 21/10.",
        "As a mixed number, 2 and 1/10."],
       answer="21/10 = 2 1/10",
       check="2/7 of 21/10 = 42/70 = 3/5 \u2713")
    practice(p, "4.4", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Calculate: (a) 1/2 \u00d7 2/3 (b) 3/4 \u00d7 8/9 (c) 5/6 \u00d7 3/10.", "F"),
        q("Write the reciprocal of (a) 3/4 (b) 5 (c) 1/7.", "F"),
        q("Calculate: (a) 1/2 \u00f7 1/4 (b) 3/4 \u00f7 3/8 (c) 2 \u00f7 1/3.", "F"),
        q("Calculate 2/3 of 45.", "F"),
        q("Explain why 1/2 \u00f7 1/4 is 2 rather than 1/8, using words or a diagram.", "R"),
        q("A recipe for 4 people uses 3/4 cup of oil. How much is needed for 6 people?",
          "P"),
        q("A ribbon 5/6 m long is cut into pieces of 1/12 m. How many pieces are there?",
          "P"),
        q("Without calculating, decide whether 3/4 \u00d7 5/6 is greater or less than 3/4. "
          "Explain.", "E"),
        q("Find a fraction that gives 1 when multiplied by itself, other than 1 and "
          "\u22121.", "E"),
    ])

    # --------------------------------------------------------------- 4.5
    section(p, "4.5", "Decimals: place value, ordering and calculation", "A \u00b7 ii, iii",
            ["Form", "Quantity"])
    body(p, "A decimal is a fraction written in place value. 0.37 means 37/100, and this "
            "single fact connects every decimal rule to something already known about "
            "fractions. Adding decimals works column by column because adding fractions "
            "with the same denominator works numerator by numerator.")
    diag(p, 120, dg.decimal_grid_shaded, "A hundred square with 37 cells shaded: 0.37 = "
                                         "37/100. The grid makes the connection between "
                                         "place value and fraction visible.", wide=True)
    h3(p, "Calculating with decimals")
    lst(p, ["**Adding and subtracting:** align the decimal points, fill empty columns with "
            "zeros, then calculate as for whole numbers.",
            "**Multiplying:** multiply as whole numbers, then count the total number of "
            "decimal places in both factors and place the point accordingly. "
            "0.3 \u00d7 0.4 = 0.12, not 1.2.",
            "**Dividing:** make the divisor a whole number by multiplying both numbers by "
            "the same power of ten, then divide."])
    we(p, "4.5.1", "Multiplying decimals",
       "Calculate 2.4 \u00d7 0.35.",
       ["Ignore the points: 24 \u00d7 35 = 840.",
        "Count decimal places: 1 + 2 = 3.",
        "Place the point three places from the right: 0.840 = 0.84."],
       answer="0.84",
       check="Estimate: 2.5 \u00d7 0.35 \u2248 0.875, and 0.84 is close \u2713")
    we(p, "4.5.2", "Dividing by a decimal",
       "Calculate 4.5 \u00f7 0.15.",
       ["Multiply both numbers by 100 to make the divisor whole: 450 \u00f7 15.",
        "450 \u00f7 15 = 30.",
        "Check by multiplying back: 30 \u00d7 0.15 = 4.5."],
       answer="30",
       check="30 \u00d7 0.15 = 4.5 \u2713")
    panel(p, "error", title="Counting decimal places wrongly",
          text="0.02 \u00d7 0.3 has three decimal places altogether, so the answer is 0.006, "
               "not 0.06. Confirm with an estimate: 0.02 \u00d7 0.3 is about a fiftieth, and "
               "0.06 would be three times too large.")
    practice(p, "4.5", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Calculate: (a) 3.6 + 1.45 (b) 8 \u2212 2.7 (c) 0.4 + 0.06.", "F"),
        q("Calculate: (a) 0.6 \u00d7 0.5 (b) 1.2 \u00d7 0.3 (c) 0.25 \u00d7 4.", "F"),
        q("Calculate: (a) 4.8 \u00f7 0.6 (b) 1.2 \u00f7 0.04.", "F"),
        q("Order from least to greatest: 0.4, 0.04, 0.404, 0.44.", "F"),
        q("Explain why 0.5 \u00d7 0.5 = 0.25 rather than 2.5 or 0.025.", "R"),
        q("A metre of cloth costs 3.75. Find the cost of 2.4 metres.", "P"),
        q("A bottle holds 0.75 litres. How many full cups of 0.15 litres can be poured?",
          "P"),
        q("Without calculating, decide whether 0.9 \u00d7 0.9 is greater or less than 0.9. "
          "Explain.", "E"),
        q("Insert a decimal point in 1250 so that the number lies between 12 and 13.", "E"),
    ])

    # --------------------------------------------------------------- 4.6
    section(p, "4.6", "Fractions, decimals and the same number", "A \u00b7 i  \u00b7  B \u00b7 ii",
            ["Representation", "Pattern"])
    panel(p, "definition", title="Converting",
          text="**Fraction to decimal:** divide the numerator by the denominator. "
               "**Decimal to fraction:** write over the appropriate power of ten and "
               "simplify \u2014 0.36 = 36/100 = 9/25. **Fraction to percentage:** convert to "
               "a decimal and multiply by 100.")
    body(p, "Because the conversion is division, every fraction must do one of two things: "
            "terminate, or repeat. Which happens depends not on the numerator but on the "
            "denominator once the fraction is in simplest form.")
    panel(p, "keyidea", title="Which fractions terminate?",
          text="A fraction in simplest form gives a terminating decimal exactly when its "
               "denominator has no prime factors other than 2 and 5. So 3/8 terminates "
               "(8 = 2^{3}) and 7/20 terminates (20 = 2^{2} \u00d7 5), but 1/3 and 5/6 "
               "recur, because 3 and 6 contain the prime 3.")
    we(p, "4.6.1", "Converting and deciding",
       "Write (a) 5/8 and (b) 2/3 as decimals, and state whether each terminates.",
       ["(a) 5 \u00f7 8 = 0.625; 8 = 2^{3}, so the decimal terminates.",
        "(b) 2 \u00f7 3 = 0.666\u2026; the remainder 2 repeats at every step, so the "
        "decimal recurs: 0.6 with a dot over the 6.",
        "A recurring decimal is usually written to three decimal places with a note, or "
        "with a dot or bar to show the repeating block."],
       answer="(a) 0.625, terminating  (b) 0.666\u2026, recurring",
       check="0.625 \u00d7 8 = 5 \u2713")
    we(p, "4.6.2", "From decimal to fraction",
       "Write 0.45 as a fraction in simplest form.",
       ["0.45 = 45/100.",
        "HCF of 45 and 100 is 5.",
        "45 \u00f7 5 = 9 and 100 \u00f7 5 = 20.",
        "So 0.45 = 9/20."],
       answer="9/20",
       check="9 \u00f7 20 = 0.45 \u2713")
    practice(p, "4.6", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Write as decimals: (a) 3/4 (b) 7/10 (c) 5/8.", "F"),
        q("Write as fractions in simplest form: (a) 0.6 (b) 0.25 (c) 0.05.", "F"),
        q("Write 4/5 as a percentage.", "F"),
        q("Which of 1/4, 1/6, 3/8, 2/9 give terminating decimals?", "R"),
        q("Explain why 1/3 cannot be written exactly as a terminating decimal.", "R"),
        q("A share is reported as 0.33 of a total. Is it exactly one third? Explain the "
          "difference.", "P"),
        q("Order 2/5, 0.41 and 3/7 from smallest to largest, showing your method.", "P"),
        q("Find a fraction that gives a recurring decimal with a repeating block of two "
          "digits.", "E"),
        q("Convert 7/8 to a decimal by division and state whether it terminates.", "F"),
        q("Write 0.375 as a fraction in simplest form.", "F"),
        q("Explain why 0.9 recurring is equal to 1, using the fraction method.", "R"),
        q("A calculator shows 0.333333333. Explain what the display has done and what the "
          "exact value is.", "P"),
    ])

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("04", "INVESTIGATE"))
    section(p, "Investigation 4", "Which fractions stop?", None, ["Pattern", "Form"])
    body(p, "Write the fractions 1/2 to 1/12 in simplest form and convert each to a decimal "
            "by division. Record the denominator's prime factors and whether the decimal "
            "terminates or recurs.")
    table(p, ["Fraction", "Simplest form", "Denominator factors", "Decimal", "Type"], [
        ["1/6", "1/6", "2 \u00d7 3", "0.1666\u2026", "recurs"],
        ["1/8", "1/8", "2^{3}", "0.125", "terminates"],
        ["1/9", "1/9", "3^{2}", "0.1111\u2026", "recurs"],
        ["1/10", "1/10", "2 \u00d7 5", "0.1", "terminates"],
        ["1/12", "1/12", "2^{2} \u00d7 3", "0.08333\u2026", "recurs"],
    ], widths=[0.7, 0.9, 1.2, 1.0, 0.8], fs=7.8)
    h3(p, "Your investigation")
    lst(p, ["Complete the table for every fraction from 1/2 to 1/12.",
            "Sort the fractions into two groups by whether the decimal terminates.",
            "What do the denominators in the terminating group have in common?",
            "Test your rule on 1/16, 1/25 and 1/40.",
            "Find a denominator with only 2s and 5s that makes a decimal with four places.",
            "Explain why the prime 3 forces a repeating pattern."], ordered=True)
    panel(p, "keyidea", title="The rule the investigation produces",
          text="A fraction in simplest form terminates exactly when the denominator is "
               "built from 2s and 5s only. Any other prime in the denominator forces a "
               "repeating block, because the remainders must eventually cycle.")
    atl(p, "In order for a student to state a rule that holds beyond the cases examined, "
           "students must test the rule on fractions outside the table, including at least "
           "one counterexample attempt.", "ATL \u00b7 Transfer")

    gap(p, 8)
    p.add(Stage("05", "APPLY"))
    section(p, "Real-life application", "The scaling kitchen", "D \u00b7 i\u2013iv",
            ["Quantity", "Equivalence"])
    body(p, "A school kitchen has a recipe for 12 portions and needs 30. Scaling a recipe "
            "means multiplying every quantity by 30/12 = 5/2, and then deciding how to "
            "measure the result with the equipment actually available.")
    table(p, ["Ingredient", "For 12 portions", "For 30 portions", "Practical measure"], [
        ["Rice", "3/4 kg", "\u2026", "\u2026"],
        ["Oil", "1/3 litre", "\u2026", "\u2026"],
        ["Tomatoes", "2 1/2 kg", "\u2026", "\u2026"],
        ["Stock", "0.6 litre", "\u2026", "\u2026"],
    ], widths=[0.8, 1.1, 1.1, 1.2])
    h3(p, "Your task")
    lst(p, ["Calculate the scaled quantity for each ingredient, in simplest form.",
            "Decide a practical measure for each: the kitchen has a 100 ml jug and scales "
            "accurate to 10 g.",
            "Calculate the percentage increase in each ingredient and explain why every "
            "one is the same.",
            "The kitchen has 2 kg of rice. Is that enough for 30 portions? Justify with a "
            "calculation.",
            "Explain why the scaled quantities are exact even when the practical measure is "
            "rounded."], ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Identify the quantities and the scale factor.",
                 "Select multiplication by a fraction as the appropriate strategy.",
                 "Apply it accurately and convert between units.",
                 "Justify the practical measures and evaluate suitability."])
    gap(p, 8)
    p.break_page()
    p.add(Stage("06", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "The fraction explainer", "C \u00b7 i\u2013iv  \u00b7  A \u00b7 i, ii", [])
    body(p, "**Context.** A younger class is convinced that 1/2 + 1/3 = 2/5 because "
            "\u201cyou add the tops and add the bottoms\u201d. Your task is a one-page "
            "explanation that corrects this without simply giving the rule.")
    lst(p, ["Draw a diagram that shows why 2/5 is too small.",
            "Show the correct calculation with a common denominator.",
            "Explain, using a unit analogy, why a common denominator is needed.",
            "Give one example where adding denominators accidentally gives a correct answer, "
            "and explain why it is a coincidence.",
            "Test your explanation on a classmate: ask them to evaluate 1/4 + 1/6 and see "
            "whether they use your reasoning.",
            "Evaluate your page: what worked, what did not, what would you change?"],
        ordered=True)
    criteria_panel(p, a="i, ii: accurate equivalence and calculation.",
                   c="i\u2013iv: notation, diagram and explanation for a named audience.")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("07", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, ["Equivalence comes from multiplying or dividing both parts by the same number.",
            "Comparing fractions needs a common unit, a landmark or a decimal.",
            "Adding and subtracting require a common denominator; multiplying and dividing "
            "do not.",
            "A decimal is a fraction in place-value notation, so decimal rules are fraction "
            "rules.",
            "A fraction terminates exactly when its denominator has no prime factors other "
            "than 2 and 5."])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["numerator", "The number of equal parts taken."],
        ["denominator", "The number of equal parts in the whole."],
        ["equivalent fractions", "Fractions naming the same value."],
        ["simplest form", "The equivalent fraction with no common factor."],
        ["reciprocal", "The fraction turned upside down; the number that multiplies to 1."],
        ["terminating decimal", "A decimal that ends."],
        ["recurring decimal", "A decimal with a repeating block of digits."],
    ], widths=[0.9, 2.3])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that persist",
          text="**Add the tops and the bottoms.** A fifth is not a common unit for halves "
               "and thirds.\n**Multiplying makes numbers bigger.** Multiplying by a fraction "
               "less than 1 makes the result smaller.\n**0.5 \u00d7 0.5 = 2.5.** Two decimal "
               "places in the factors give two places in the answer.")
    assessment_close(p, [
        ["write equivalent fractions and simplify", "\u25a1", "\u25a1", "\u25a1"],
        ["compare and order fractions", "\u25a1", "\u25a1", "\u25a1"],
        ["add and subtract fractions", "\u25a1", "\u25a1", "\u25a1"],
        ["multiply and divide fractions", "\u25a1", "\u25a1", "\u25a1"],
        ["calculate with decimals", "\u25a1", "\u25a1", "\u25a1"],
        ["convert between fractions, decimals and percentages", "\u25a1", "\u25a1",
        "\u25a1"],
        
    ],
        "In order for a student to choose the most efficient notation, students must "
               "notice which form the question already uses and which form the answer must "
               "take.",
        next_title="Chapter 5 · Percentages and applications")


    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("08", "MIXED PRACTICE"))
    practice(p, "Mixed practice 4",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201311  \u00b7  EXTENSION 9\u201314", [
        q("Simplify: (a) 12/18 (b) 20/35 (c) 42/56.", "F"),
        q("Calculate 2/3 + 1/6.", "F"),
        q("Calculate 5/8 \u00d7 4/15.", "F"),
        q("Calculate 3/4 \u00f7 9/16.", "F"),
        q("Write 0.35 as a fraction in simplest form and 7/20 as a decimal.", "F"),
        q("Order from least to greatest: 3/5, 0.58, 11/20.", "R"),
        q("Explain why 1/2 + 1/3 = 5/6 rather than 2/5.", "R"),
        q("A recipe for 8 uses 2/3 cup of milk. Find the amount for 20, in simplest form.",
          "P"),
        q("A rope 7/8 m long is cut into four equal pieces. Find the length of each.",
          "P"),
        q("Calculate 1.25 \u00d7 0.8 and explain the position of the decimal point.", "F"),
        q("Find a fraction between 2/5 and 1/2 with a denominator of 20.", "E"),
        q("Show that 0.999\u2026 is equal to 1, using fractions.", "E"),
        q("Explain why multiplying by 3/4 makes a number smaller but dividing by 3/4 makes "
          "it larger.", "R"),
        q("A tank is 2/5 full. After adding 30 litres it is 3/4 full. Find the capacity.",
          "E"),
    ])
    gap(p, 8)
    p.add(Stage("09", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20132", "Revisit 4.1: multiply or divide both parts by the same number."],
        ["3\u20134", "Revisit 4.3 and 4.4: common denominator for add, reciprocal for "
                    "divide."],
        ["5\u20136", "Revisit 4.5 and 4.6: a decimal is a fraction over a power of ten."],
        ["7\u20139", "Revisit 4.2: draw the two fractions on one strip."],
        ["10\u201314", "Revisit the investigation and the key idea on terminating "
                      "decimals."],
    ], widths=[0.7, 2.6])


ANSWERS = [
    ("4.1", "1 e.g. (a) 2/4, 3/6 (b) 6/10, 9/15 (c) 14/20, 21/30.  2 (a) 2/3 (b) 3/5 "
            "(c) 3/4.  3 24/42.  4 8/12 and 6/9.  6 9/24: the bag is cut into 24 parts and "
            "9 are used.  7 No: 6/8 is useful when the whole is cut into eight parts.  "
            "8 14/21.  9 1/3, 2/6, 3/9, 4/12, 5/15, 6/18, 7/21, "
            "8/24, 9/27."),
    ("4.2", "1 (a) < (b) <.  2 3/8 < 2/5 < 7/16 < 1/2.  3 5/9 (36/63 > 35/63).  "
            "4 7/12.  6 Comparing numerators and denominators separately ignores that the "
            "denominator is the unit.  7 2/5 km (0.4 km).  8 5/12."),
    ("4.3", "1 (a) 3/5 (b) 1/2 (c) 2/5.  2 (a) 5/6 (b) 11/12 (c) 1/4.  3 29/24 = 1 5/24.  "
            "4 (a) 1 2/5 (b) 6 3/4.  6 7/8 full; 1/8 remains.  7 2/3 and 1/3.  8 7/8.  "
            "9 5/6 \u2212 2/6 = 3/6 = 1/2."),
    ("4.4", "1 (a) 1/3 (b) 2/3 (c) 1/4.  2 (a) 4/3 (b) 1/5 (c) 7.  3 (a) 2 (b) 2 (c) 6.  "
            "4 30.  6 1 1/8 cups (9/8).  7 10 pieces.  9 3/4 \u00d7 5/6 < 3/4 because 5/6 "
            "< 1."),
    ("4.5", "1 (a) 5.05 (b) 5.3 (c) 0.46.  2 (a) 0.3 (b) 0.36 (c) 1.  3 (a) 8 (b) 30.  "
            "4 0.04 < 0.4 < 0.404 < 0.44.  6 9.00.  7 5 cups."),
    ("4.6", "1 (a) 0.75 (b) 0.7 (c) 0.625.  2 (a) 3/5 (b) 1/4 (c) 1/20.  3 80 %.  "
            "4 1/4 and 3/8.  6 No: 0.33 is 33/100, which is less than 1/3.  7 2/5 < 0.41 < "
            "3/7.  8 e.g. 1/11 = 0.0909\u2026"),
    ("Investigation 4", "Terminating: 1/2, 1/4, 1/5, 1/8, 1/10. Recurring: 1/3, 1/6, 1/7, "
                        "1/9, 1/11, 1/12. Denominators of terminating decimals contain only "
                        "2s and 5s."),
    ("Mixed 4", "1 (a) 2/3 (b) 4/7 (c) 3/4.  2 5/6.  3 1/6.  4 4/3 = 1 1/3.  5 7/20; "
                "0.35.  6 11/20 < 0.58 < 3/5.  8 5/3 cups = 1 2/3.  9 7/32 m.  10 1.00.  "
                "11 9/20.  14 600/7 \u2248 85.7 litres."),
]
