"""Chapter 1 - Ratios and equivalent ratios (Number and proportion)."""
from chbase import *

PLATE = dict(
    part="Part I \u00b7 Number and proportion", part_numeral="I", chapter_no=1,
    kicker="Number and proportion", motif="ratio",
    title_lines=["Ratios and equivalent", "ratios"],
    lead_lines=["A ratio can describe an entire family of situations:",
                "the same relationship at a different size, in different",
                "units, or on a different scale."],
    key_concept="Form", related=["Equivalence", "Representation"],
    context="Fairness and development",
    inquiry_lines=["How can one comparison describe many different-sized",
                   "situations without losing what matters?"])

TITLE = "Ratios and equivalent ratios"
SHORT = "Ratios and equivalent ratios"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "The chapter in one view: the concepts, the context and the evidence "
       "that will be looked for."),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "Equivalent ratios preserve a multiplicative relationship, so one "
              "comparison can organise fair shares and scaled quantities across "
              "different totals and units."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Form.** A ratio has a written form \u2014 a : b, and a "
        "simplest form. Its form shows which quantities are compared, and in what "
        "order.\n"
        "**Related \u00b7 Equivalence.** Multiplying or dividing both parts by the "
        "same non-zero number gives a different-looking ratio with the same "
        "relationship.\n"
        "**Related \u00b7 Representation.** Tape diagrams, ratio tables, double "
        "number lines and graphs each expose a different feature of the same "
        "comparison."),
    BOX("note", "Global context \u00b7 Fairness and development",
        "Exploration: fair distribution, shared resources and just comparison. A "
        "harvest shared between three families, or a recipe scaled for a hundred "
        "people, needs a rule that can be stated, checked and defended. A ratio "
        "makes that rule visible, so a decision can be examined rather than merely "
        "asserted."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** What is a ratio, and how is an equivalent ratio formed?",
        "**Conceptual:** How can different ratios show the same relationship?",
        "**Debatable:** When a fixed-ratio share is fair, and when is another "
        "comparison needed?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Simplify and interpret ratios; share quantities accurately."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate equivalent ratio chains and state the scaling rule."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Use ratio notation and units; move between representations."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv, v",
         "Garden task: select quantities, justify a share, evaluate fairness."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to test the claim that adding the same amount to "
        "both parts keeps a ratio the same, students must produce a counterexample, "
        "explain why it fails and repair the claim."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Read, write and interpret ratio language in context.",
         "Describe a situation with a part-to-part and a part-to-whole ratio, and "
         "say what each term counts."],
        ["Form equivalent ratios and write a ratio in simplest form.",
         "Simplify \u00a0 18 : 24 \u00a0 and generate three ratios equivalent to it."],
        ["Use a ratio table and a double number line to scale a relationship.",
         "Solve a scaling problem with a table and check it on a double number line."],
        ["Share a quantity in a given ratio.",
         "Divide \u00a0 120 \u00a0 in the ratio \u00a0 5 : 3 \u00a0 and check by "
         "recombining."],
        ["Compare two ratios and justify which is greater.",
         "Decide whether \u00a0 4 : 5 \u00a0 or \u00a0 7 : 9 \u00a0 is greater, "
         "with a calculation, not an impression."],
        ["Explain why a ratio is unchanged by scaling but changed by adding.",
         "Give one example that works and one that fails, and say where the "
         "difference lies."],
    ], widths=[1.55, 1.85]),
    GAP(8),
    H("How this chapter runs"),
    TABLE(["Stage", "What happens"], [
        ["Engage", "A school fair sells lemonade in three sizes at the same taste."],
        ["Explore", "Strips of paper are folded to compare parts before any rule is "
                    "named."],
        ["Explain", "Ratio notation, simplest form, ratio tables, double number "
                    "lines, sharing."],
        ["Worked examples", "Seven complete solutions with a check on each."],
        ["Practise", "Five graded sets: fluency, reasoning, problem solving, "
                     "extension."],
        ["Investigate", "The lemonade stand: four recipes, one conjecture."],
        ["Reflect", "Summary, vocabulary, misconceptions and a self-assessment."],
    ], widths=[0.9, 3.0]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Write \u00a0 3/4 \u00a0 as a decimal and as a percentage.",
               "Find \u00a0 1/5 \u00a0 of 60.",
               "Simplify \u00a0 12/18.",
               "Calculate \u00a0 7 \u00d7 8 \u00a0 and \u00a0 56 \u00f7 8.",
               "Which is greater, \u00a0 2/3 \u00a0 or \u00a0 3/5? \u00a0 Explain "
               "in one sentence.",
               "Share 40 sweets equally between 5 children."]),
    P("If more than two answers are wrong, revise equivalent fractions and finding "
      "a fraction of a quantity before starting section 1.2. Answers are in the "
      "back of the book."),

    # ------------------------------------------------------------------ 1.1
    S("1.1", "Understanding ratio language", "A \u00b7 I, II, III",
      ["Representation", "Ratio as comparison"]),
    L("A ratio is not a pair of numbers that happen to sit beside each other. It is "
      "a statement about how quantities are related by multiplication, and the order "
      "of the statement is part of its meaning."),
    ST("03", "ENGAGE",
       "Three jugs, one taste. Which information do you actually need in order to "
       "repeat a recipe for a larger crowd?"),
    PHOTO("ch01_lemonade.jpg", 1.5,
          "Lemonade at a stall. Three jugs made to the same recipe taste the same "
          "because the ratio of juice to water is unchanged, not the amounts.",
          "Photograph: Pexels, free licence (see the image register)."),
    P("At a school fair the lemonade stall sells three jugs. The small jug mixes 2 "
      "cups of lemon juice with 5 cups of water. The medium jug mixes 4 cups with "
      "10. The large jug mixes 6 cups with 15. Customers say all three taste the "
      "same, and the stallholder insists she has not changed the recipe."),
    P("Before reading on, write down one sentence that explains how all three jugs "
      "can be the same recipe when the numbers are different. Then write a second "
      "sentence that says what would change the taste."),
    ST("04", "EXPLORE",
       "Two strips, folded and compared."),
    P("Take two strips of paper of equal length. Fold the first into 3 equal parts "
      "and shade 1 part. Fold the second into 6 equal parts and shade 2 parts. Hold "
      "them side by side."),
    OL(["What fraction of each strip is shaded?",
        "Are the two shaded lengths the same? How can you tell without measuring?",
        "Now shade 1 part of a strip folded into 4. Is that the same comparison as "
        "either of the others?",
        "Fold a third strip into 9 equal parts and shade 3. Which earlier strip does "
        "it match?",
        "Write a conjecture: when do two shaded strips show the same comparison?",
        "Test the conjecture on a strip folded into 12 parts. How many parts would "
        "you shade to match a strip with 1 part in 4 shaded?"]),
    ST("05", "EXPLAIN"),
    DEF("A `ratio` compares two or more quantities multiplicatively. For quantities "
        "`a` and `b`, the ratio is written `a` : `b`, read \u201c`a` to `b`\u201d. "
        "The quantities must be measured in the same unit before the ratio is "
        "written or simplified."),
    P("There are three common ways to write a two-part ratio: in words, with a "
      "colon, or as a fraction. A ratio of 3 parts blue to 5 parts yellow can be "
      "written \u201c3 to 5\u201d, 3 : 5, or 3/5 when the fraction is understood as "
      "a comparison, not as a share of the whole. The notation you choose should "
      "make the meaning clearer, not merely shorter."),
    DIAG(150, "ratio_tape", "A tape diagram for the ratio 3 : 5. The whole bar has "
                            "3 + 5 = 8 equal parts. Blue is 3/8 of the whole, while "
                            "the ratio of blue to yellow is 3 : 5."),
    H("Part to part, and part to whole"),
    P("A **part-to-part** ratio compares two parts of a group. A **part-to-whole** "
      "ratio compares one part with the entire group. In the diagram above, the "
      "part-to-part ratio of blue to yellow is 3 : 5. The part-to-whole ratio of "
      "blue to all counters is 3 : 8. Confusing these two is the most common source "
      "of error in the whole chapter, because the second term answers a different "
      "question."),
    KEY("Order matters. The ratio of blue to yellow is not the same statement as the "
        "ratio of yellow to blue. Reversing the terms describes a different "
        "comparison, even though both ratios use the same two numbers."),
    WE("1.1.1", "Reading the terms",
       "A paint mix uses 3 parts blue to 5 parts yellow. State (a) the ratio of blue "
       "to yellow, (b) the ratio of blue to the whole mix, (c) the fraction of the "
       "mix that is yellow.",
       ["The order of the words decides the order of the numbers: blue to yellow is "
        "3 : 5.",
        "The whole mix has 3 + 5 = 8 parts, so blue to the whole is 3 : 8.",
        "Yellow is 5 of those 8 parts, so the fraction is 5/8.",
        "State each answer with its unit of meaning: parts, not cups."],
       "(a) 3 : 5   (b) 3 : 8   (c) 5/8",
       "Check the two parts add to the whole: 3 + 5 = 8 equal parts, and 3/8 + 5/8 = 1."),
    WE("1.1.2", "Same unit first",
       "A shelf holds 45 cm of books and has 1.2 m of space in total. Write the ratio "
       "of the books to the total space in simplest form.",
       ["The quantities are in different units, so convert first: "
        "1.2 m = 120 cm.",
        "The ratio of books to total space is 45 : 120.",
        "Divide both terms by 15: 45 \u00f7 15 = 3 and 120 \u00f7 15 = 8.",
        "The ratio in simplest form is 3 : 8."],
       "3 : 8",
       "The books fill 3/8 of the shelf, which is a little under half \u2014 "
       "plausible for a shelf with space to spare."),
    WE("1.1.3", "Which comparison is being asked for?",
       "In a box of 24 counters, 9 are red and the rest are green. Write (a) red to "
       "green, (b) green to red, and (c) red to all counters, each in simplest form.",
       ["Green counters: 24 \u2212 9 = 15.",
        "Red to green is 9 : 15, which divides by 3 to give 3 : 5.",
        "Green to red is 15 : 9, which divides by 3 to give 5 : 3.",
        "Red to all counters is 9 : 24, which divides by 3 to give 3 : 8."],
       "(a) 3 : 5   (b) 5 : 3   (c) 3 : 8",
       "3 + 5 = 8 parts, and 3/8 of 24 is 9 red counters, as stated."),
    ERR("Writing \u201cthe ratio of red to green is 3 : 5, so 3/5 of the counters "
        "are red\u201d. The ratio 3 : 5 compares red with green only. Red is 3/8 of "
        "the whole box, because the whole is 3 + 5 = 8 parts. Always identify what "
        "the second term counts before writing a fraction."),
    PRAC("1.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION 10\u201312", [
        Q("A recipe uses 2 parts lemon to 5 parts water. Write the ratio of lemon to "
          "water, and of lemon to the whole mixture.", "F"),
        Q("In a class of 30 students, 18 walk to school. Write the ratio of walkers "
          "to non-walkers in simplest form.", "F"),
        Q("Write each ratio in simplest form: (a) 12 : 18  (b) 25 : 40  "
          "(c) 36 : 24  (d) 45 : 60.", "F"),
        Q("A model car is 24 cm long and the real car is 4.8 m long. Write the ratio "
          "of model length to real length in simplest form.", "F"),
        Q("A bag contains 15 white and 10 black beads. State the ratio of white to "
          "black, and the fraction of the beads that are black.", "F"),
        Q("Two quantities are in the ratio 4 : 9. The smaller is 28. Find the larger.",
          "R"),
        Q("Explain why 0.6 m : 45 cm is not written as 0.6 : 45, and give the "
          "simplified ratio.", "R"),
        Q("A smoothie mixes mango, yoghurt and milk in the ratio 3 : 2 : 5. State the "
          "ratio of mango to the whole drink.", "P"),
        Q("A photograph is 15 cm wide and 10 cm high. A print is made at 45 cm wide. "
          "What should its height be if the shape is unchanged?", "P"),
        Q("A student says \u201cthe ratio 5 : 2 means the first quantity is 2.5 times "
          "the second\u201d. Is the student right? Justify with a calculation.", "E"),
        Q("Two ratios are 3 : 4 and 6 : 8. A student claims they are different "
          "because the numbers are different. Write a reply in two sentences.", "E"),
        Q("Find a ratio equivalent to 2 : 3 whose two terms add to 45.", "E"),
    ]),

    # ------------------------------------------------------------------ 1.2
    S("1.2", "Equivalent ratios and simplest form", "A \u00b7 II",
      ["Equivalence", "Simplification"]),
    L("Two ratios are equivalent when they describe the same multiplicative "
      "relationship. The numbers may change; the comparison does not."),
    DEF("Ratios `a` : `b` and `c` : `d` are `equivalent` if there is a non-zero "
        "number `k` such that `c` = `k a` and `d` = `k b`. A useful test is the "
        "cross-product condition `a d` = `b c`."),
    P("Multiplying or dividing both terms by the same non-zero number produces an "
      "equivalent ratio. This is the same operation that produces equivalent "
      "fractions, applied to each part of the comparison. A ratio is in **simplest "
      "form** when the terms are whole numbers with no common factor greater than "
      "1."),
    KEY("To test whether `a` : `b` = `c` : `d`, check whether `a d` = `b c`. For "
        "example, 6 : 9 and 10 : 15 are equivalent because 6 \u00d7 15 = 90 and "
        "9 \u00d7 10 = 90."),
    DIAG(190, "double_number_line",
         "A double number line for 3 : 5. Every mark on the upper line is paired "
         "with the mark directly below it. Multiplying both quantities by the same "
         "factor moves you to another equivalent pair."),
    WE("1.2.1", "Simplify and justify",
       "Write 42 : 56 in simplest form and justify your answer with a common factor.",
       ["Both terms are even, so divide by 2: 21 : 28.",
        "Both are multiples of 7, so divide by 7: 3 : 4.",
        "Equivalently, divide once by the highest common factor, 14: "
        "42 \u00f7 14 = 3 and 56 \u00f7 14 = 4.",
        "Check with the cross-product: 42 \u00d7 4 = 168 and 56 \u00d7 3 = 168."],
       "3 : 4",
       "3 and 4 share no factor greater than 1, so the ratio is in simplest form."),
    WE("1.2.2", "Find the missing term",
       "The ratios 4 : 7 and 12 : `x` are equivalent. Find `x`.",
       ["The first term has been multiplied by 3, because 4 \u00d7 3 = 12.",
        "Multiply the second term by the same factor: 7 \u00d7 3 = 21.",
        "Check with cross-products: 4 \u00d7 21 = 84 and 7 \u00d7 12 = 84."],
       "`x` = 21",
       "Both cross-products agree, so the ratios are equivalent."),
    WE("1.2.3", "Decide, do not guess",
       "Are 8 : 12 and 14 : 21 equivalent? Are 8 : 12 and 10 : 14 equivalent? "
       "Justify each answer.",
       ["Simplify 8 : 12 by dividing both terms by 4: 2 : 3.",
        "Simplify 14 : 21 by dividing both terms by 7: 2 : 3. The ratios are "
        "equivalent.",
        "Simplify 10 : 14 by dividing both terms by 2: 5 : 7, which is not 2 : 3. "
        "Check: 8 \u00d7 14 = 112 and 12 \u00d7 10 = 120, and these differ.",
        "When the simplified forms match, the ratios are equivalent; when they do "
        "not, they are not."],
       "8 : 12 = 14 : 21, but 8 : 12 \u2260 10 : 14.",
       "Simplest form is a fingerprint: two equivalent ratios always share it."),
    ERR("\u201c5 : 10 simplifies to 1 : 2 because 5 \u2212 4 = 1 and 10 \u2212 8 = "
        "2.\u201d Subtracting the same amount from both terms changes the ratio, "
        "because a ratio is a multiplicative comparison. Only multiplying or "
        "dividing both terms by the same non-zero number preserves it."),
    PRAC("1.2", "SUPPORT 1\u20135  \u00b7  CORE 6\u201310  \u00b7  EXTENSION "
                "11\u201313", [
        Q("Write each ratio in simplest form: (a) 8 : 12  (b) 15 : 25  "
          "(c) 27 : 36  (d) 48 : 64.", "F"),
        Q("Copy and complete: 3 : 4 = 9 : \u2026 = \u2026 : 20 = 30 : \u2026.", "F"),
        Q("Write three ratios equivalent to 5 : 6.", "F"),
        Q("Are 9 : 12 and 15 : 20 equivalent? Justify with a common simplified form.",
          "F"),
        Q("Find `x`: 7 : 8 = `x` : 40.", "F"),
        Q("A recipe uses flour and sugar in the ratio 5 : 2. If 350 g of flour is "
          "used, what mass of sugar is needed, and what is the total mass of the two "
          "ingredients?", "P"),
        Q("Which ratio is equivalent to 6 : 9?  A 2 : 3   B 3 : 2   C 6 : 3   "
          "D 12 : 15", "R"),
        Q("A student says \u201cadding 3 to both terms of 2 : 5 gives the equivalent "
          "ratio 5 : 8\u201d. Find a counterexample to the claim in general, and "
          "explain in one sentence why adding fails while multiplying works.", "R"),
        Q("The ratio of two angles is 3 : 7 and their sum is 180\u00b0. Find both "
          "angles.", "P"),
        Q("A map uses a scale of 1 : 25 000. A path measures 6 cm on the map. How "
          "long is the real path, in kilometres?", "P"),
        Q("Two ratios are in the form `k` : 12 and 15 : 20. Find `k` if they are "
          "equivalent.", "E"),
        Q("Find all whole numbers `n` such that 4 : `n` is equivalent to a ratio "
          "whose terms add to 21.", "E"),
        Q("The ratio of boys to girls in a year group is 5 : 4. There are 12 more "
          "boys than girls. How many students are there in the year group?", "E"),
    ]),

    # ------------------------------------------------------------------ 1.3
    S("1.3", "Ratio tables and double number lines", "A \u00b7 II  \u00b7  "
      "C \u00b7 II", ["Representation", "Scaling"]),
    L("A ratio table organises equivalent pairs so that the scaling factor becomes "
      "visible. A double number line shows the same relationship spatially, and a "
      "graph turns the same relationship into a line."),
    H("Building a ratio table"),
    P("Each row of a ratio table contains one pair of equivalent quantities. To move "
      "from one entry to the next, multiply or divide both quantities by the same "
      "factor. A useful strategy is to scale through a convenient unit, such as one "
      "part, because that makes every other entry easier to find."),
    TABLE(["Concentrate (cups)", "2", "4", "6", "8", "10"],
          [["Water (cups)", "5", "10", "15", "20", "25"]],
          widths=[1.6, 0.7, 0.7, 0.7, 0.7, 0.7],
          caption="A ratio table for lemon concentrate and water. The ratio "
                  "2 : 5 holds in every column."),
    P("The ratio is 2 : 5 in every column. Multiplying both quantities by 2 gives "
      "4 : 10, by 3 gives 6 : 15, by 4 gives 8 : 20. If a table is built by adding "
      "the same amount to each row instead, the entries no longer line up and the "
      "table no longer represents equivalent ratios."),
    H("Using a unit rate"),
    P("Dividing both terms so that the first is 1 gives the **unit rate**: the amount "
      "of the second quantity for each one of the first. For the concentrate above, "
      "1 cup of concentrate needs 2.5 cups of water. Once the unit rate is known, any "
      "quantity can be found with one multiplication."),
    WE("1.3.1", "Complete the table and scale",
       "A recipe uses 3 cups of rice for every 4 people. Complete a ratio table for "
       "3, 6, 9 and 15 people, and state the unit rate.",
       ["Write the base pair: 3 cups : 4 people.",
        "Scale by 2 for 8 people: 6 cups. Scale by 3 for 12 people: 9 cups.",
        "For 15 people, scale by 3.75: 3 \u00d7 3.75 = 11.25 cups.",
        "The unit rate is 3 \u00f7 4 = 0.75 cups per person."],
       "6 cups for 8 people, 9 cups for 12 people, 11.25 cups for 15 people; unit "
       "rate 0.75 cups per person.",
       "Check with the unit rate: 15 \u00d7 0.75 = 11.25, as in the table."),
    WE("1.3.2", "Read a double number line",
       "On a double number line, kilometres run 0, 15, 30, 45 and miles run 0, 9, 18, "
       "27. How many kilometres are in 21 miles?",
       ["Each 9 miles matches 15 km, so the scale factor from miles to kilometres is "
        "15 \u00f7 9 = 5/3.",
        "For 21 miles: 21 \u00d7 5/3 = 35 km.",
        "Alternatively, use the unit rate: 1 mile is 5/3 km, so "
        "21 miles is 21 \u00d7 5/3 = 35 km."],
       "21 miles = 35 km",
       "Sanity check: 21 miles is a little more than twice 9 miles, and 35 km is a "
       "little more than twice 15 km."),
    WE("1.3.3", "From table to graph",
       "Paint costs \u00a36 for 2 litres. Complete the pairs (2, 6), (3, 9), (5, 15), "
       "(8, 24) and describe the graph of cost against litres.",
       ["Every pair has the same quotient: 6 \u00f7 2 = 9 \u00f7 3 = 15 \u00f7 5 = "
        "24 \u00f7 8 = 3.",
        "The points lie on a straight line through the origin.",
        "The gradient of that line is the cost per litre, \u00a33.",
        "A straight line through the origin is exactly what a constant ratio looks "
        "like on a graph."],
       "A straight line through the origin with gradient 3.",
       "Check one point off the line: 4 litres should cost \u00a312, and "
       "4 \u00d7 3 = 12."),
    DIAG(210, "prop_graph",
         "Cost against volume for paint at \u00a33 per litre. The constant quotient "
         "becomes the gradient of a straight line through the origin."),
    PRAC("1.3", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Copy and complete the ratio table for 3 : 7:  3 : 7,  6 : \u2026,  "
          "9 : \u2026,  \u2026 : 35.", "F"),
        Q("A car travels 48 km on 4 litres of fuel. Complete the table for 6, 8 and "
          "10 litres.", "F"),
        Q("On a map, 4 cm represents 10 km. How many kilometres does 14 cm "
          "represent?", "F"),
        Q("State the unit rate: (a) 5 pens cost \u00a34  (b) 8 kg cost \u00a312  "
          "(c) 240 km in 3 hours.", "F"),
        Q("Lemonade mixes 250 ml of syrup with 1.5 litres of water. How much syrup is "
          "needed for 6 litres of water?", "P"),
        Q("A printer produces 45 pages in 3 minutes. How long will 300 pages take? "
          "Give your answer in minutes and seconds.", "P"),
        Q("The pairs (1, 4), (2, 8), (3, 12) and (5, 22) are plotted. Which pair does "
          "not belong, and how does the graph show it?", "R"),
        Q("A recipe for 8 people uses 600 g of pasta. Write a ratio table for 8, 12 "
          "and 20 people and state the mass per person.", "P"),
        Q("Two ratio tables are given. In the first, both rows double each time. In "
          "the second, the second row gains 3 each time while the first gains 1. "
          "Which is a ratio table, and why?", "R"),
        Q("A shop sells rope at \u00a31.20 per metre. Write five equivalent pairs "
          "(metres, cost) and explain why they lie on a straight line through the "
          "origin.", "E"),
        Q("Express 3 : 8 as a unit rate with first term 1, and as a unit rate with "
          "second term 1, using fractions.", "E"),
        Q("A photograph is enlarged so that 2 cm becomes 7 cm. A detail 6 mm long in "
          "the original is how long in the enlargement? Give your answer in "
          "centimetres.", "E"),
    ]),

    # ------------------------------------------------------------------ 1.4
    S("1.4", "Sharing and comparing with ratios", "A \u00b7 III  \u00b7  "
      "C \u00b7 III", ["Quantity", "Proportionality"]),
    L("To share a quantity in a given ratio, find the value of one part first: divide "
      "the total by the number of parts, then multiply by each term."),
    H("Sharing in a ratio"),
    OL(["Add the terms of the ratio to find the total number of parts.",
        "Divide the quantity by the number of parts to find the value of one part.",
        "Multiply the value of one part by each term of the ratio.",
        "Check that the shares add back to the original quantity."]),
    PHOTO("ch01_tiles.jpg", 1.5,
          "A gridded facade. Every bay repeats the same proportions, so one bay "
          "measured gives the whole elevation without counting it.",
          "Photograph: Pexels, free licence (see the image register)."),
    DIAG(170, "share_bars",
         "A quantity of 360 shared in the ratio 2 : 3 : 4. The bar is cut into nine "
         "equal parts of 40, giving shares of 80, 120 and 160."),
    WE("1.4.1", "Two-part sharing",
       "Share \u00a372 in the ratio 5 : 3.",
       ["There are 5 + 3 = 8 parts.",
        "One part is 72 \u00f7 8 = \u00a39.",
        "The first share is 5 \u00d7 9 = \u00a345; the second is "
        "3 \u00d7 9 = \u00a327.",
        "Check: 45 + 27 = 72, and 45 : 27 simplifies to 5 : 3."],
       "\u00a345 and \u00a327",
       "Recombine the shares and re-simplify the ratio: both checks pass."),
    WE("1.4.2", "Three-part sharing from a difference",
       "Two amounts are in the ratio 3 : 8 and their difference is 45. Find both "
       "amounts.",
       ["The difference of the terms is 8 \u2212 3 = 5 parts.",
        "Those 5 parts are worth 45, so one part is 45 \u00f7 5 = 9.",
        "The amounts are 3 \u00d7 9 = 27 and 8 \u00d7 9 = 72.",
        "Check: 72 \u2212 27 = 45, as required."],
       "27 and 72",
       "The difference check confirms the ratio, not just the arithmetic."),
    WE("1.4.3", "Comparing two ratios",
       "Which is greater, 4 : 5 or 7 : 9? Justify your answer.",
       ["Write each as a fraction of the first quantity: 4/5 = 0.8 and "
        "7/9 \u2248 0.778.",
        "Since 0.8 > 0.778, the ratio 4 : 5 represents a larger first quantity "
        "relative to the second.",
        "Cross-product check: 4 \u00d7 9 = 36 and 5 \u00d7 7 = 35. Because "
        "36 > 35, 4 : 5 > 7 : 9.",
        "Alternatively write both with a common second term of 45: 4 : 5 = 36 : 45 "
        "and 7 : 9 = 35 : 45."],
       "4 : 5 is greater than 7 : 9",
       "Two methods agree, so the comparison is robust."),
    ERR("To share 72 in the ratio 5 : 3, dividing 72 \u00f7 2 = 36 treats the ratio "
        "as two equal shares. The ratio tells you there are 5 + 3 = 8 parts, not two. "
        "Always find the number of parts first."),
    PRAC("1.4", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Share 72 in the ratio 5 : 3.", "F"),
        Q("Share 180 in the ratio 2 : 3 : 4.", "F"),
        Q("Share 96 in the ratio 3 : 5.", "F"),
        Q("Two amounts are in the ratio 4 : 7. The smaller amount is 36. Find the "
          "larger amount and the total.", "P"),
        Q("Two amounts are in the ratio 3 : 8. Their difference is 45. Find both "
          "amounts.", "P"),
        Q("Share 120 in the ratio 7 : 3 : 2.", "F"),
        Q("A rectangle has perimeter 60 cm. Its length and width are in the ratio "
          "7 : 3. Find the length and width.", "P"),
        Q("The angles of a triangle are in the ratio 2 : 3 : 4. Find the three "
          "angles.", "P"),
        Q("Which is greater, 4 : 5 or 7 : 9? Show your method.", "R"),
        Q("Three classes share 360 students in the ratio 5 : 6 : 7. How many students "
          "are in each class?", "P"),
        Q("A sum of money is shared in the ratio 3 : 5. The larger share is \u00a3120 "
          "more than the smaller. Find the total sum.", "E"),
        Q("A recipe uses flour, sugar and butter in the ratio 6 : 2 : 3. The butter "
          "weighs 240 g. Find the total mass of the three ingredients.", "E"),
    ]),

    # ------------------------------------------------------- investigation
    ST("06", "INVESTIGATE AND APPLY",
       "The lemonade stand: four recipes, one conjecture, one test."),
    CARD_I("Which recipe is which?", [
        ("p", "A community fair is selling lemonade. Four teams use different "
              "recipes, each described by the ratio of lemon juice to water. The "
              "teams want to know which recipes taste the same and how to scale any "
              "recipe to a larger container."),
        ("table", ["Recipe", "Lemon juice", "Water", "Total"], [
            ["A", "2", "5", "7"],
            ["B", "4", "10", "14"],
            ["C", "6", "15", "21"],
            ["D", "3", "8", "11"],
        ], [1, 1, 1, 1]),
        ("ol", ["Write each recipe as a ratio of lemon juice to water, in simplest "
                "form.",
                "Which recipes have the same simplified ratio? What does that suggest "
                "about their taste?",
                "Complete a table showing the amount of lemon juice needed for 30 "
                "cups of water for each recipe.",
                "Plot the pairs (lemon juice, water) for recipe A for 1, 2, 3 and 4 "
                "times the base quantity. Describe the graph.",
                "Write a conjecture: if two recipes have the same simplified ratio, "
                "what is true about the taste? Test it with the pair 3 : 7 and "
                "9 : 21.",
                "Recipe D uses 3 cups of lemon and 8 cups of water. Is it more or "
                "less lemony than recipe A? Justify with a calculation.",
                "Give one reason why the ratio alone might not guarantee that two "
                "lemonades taste identical."]),
    ]),
    CARD_D("Cooking for 45", [
        ("p", "A community kitchen has a recipe for 12 people: 600 g rice, 450 g "
              "lentils and 90 ml oil. The team needs to cook for 45 people, keeping "
              "the ingredients in the same ratio."),
        ("ol", ["Find the scale factor from 12 people to 45 people.",
                "Calculate the mass of each ingredient needed for 45 people. Give "
                "masses to the nearest gram and oil to the nearest millilitre.",
                "Explain why tripling the recipe and then adding a quarter of the "
                "original recipe gives the same result as multiplying by 3.75.",
                "The kitchen has 2.4 kg of rice. Is that enough? Justify with a "
                "comparison, and comment on the accuracy of your answer.",
                "Suggest one realistic reason why a cook might deliberately use a "
                "ratio slightly different from the written one."]),
    ]),

    # ------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("1.6", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["A ratio compares quantities multiplicatively, and the order of the terms "
        "carries meaning.",
        "Part-to-part and part-to-whole ratios answer different questions; the "
        "denominator of a fraction comes from the total number of parts.",
        "Quantities must be in the same unit before a ratio is written.",
        "Multiplying or dividing both terms by the same non-zero number gives an "
        "equivalent ratio; adding does not.",
        "A ratio table, a double number line and a straight-line graph are three "
        "representations of one relationship.",
        "Sharing in a ratio needs the value of one part, found by dividing the total "
        "by the number of parts."]),
    VOCAB("**ratio** \u00b7 **term** \u00b7 **part-to-part** \u00b7 "
          "**part-to-whole** \u00b7 **equivalent ratios** \u00b7 **simplest form** "
          "\u00b7 **ratio table** \u00b7 **double number line** \u00b7 **unit rate** "
          "\u00b7 **scale factor** \u00b7 **share**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["\u201c3 : 5 means 3/5 of the whole.\u201d",
         "3 : 5 compares two parts. The whole is 3 + 5 = 8 parts, so the fraction is "
         "3/8."],
        ["\u201cAdding the same amount to both terms keeps the ratio.\u201d",
         "It does not. 2 : 3 becomes 5 : 6 when 3 is added, and 5/6 \u2260 2/3. Only "
         "multiplying or dividing works."],
        ["\u201cThe larger numbers mean the larger ratio.\u201d",
         "10 : 20 is smaller than 3 : 4, because 0.5 < 0.75. Compare the quotients "
         "or use cross-products."],
        ["\u201cSharing in a ratio means dividing by the number of terms.\u201d",
         "Divide by the number of parts, which is the sum of the terms."],
    ], widths=[1.5, 2.0]),
    H("Revision questions"),
    OL(["Write 18 : 24 in simplest form and state the scale factor from the simplest "
        "form to the original.",
        "Share \u00a3154 in the ratio 4 : 7.",
        "Are 12 : 20 and 15 : 25 equivalent? Justify.",
        "A map scale is 1 : 50 000. A road measures 7 cm. How long is the real road, "
        "in kilometres?",
        "Two amounts are in the ratio 5 : 9 and add to 210. Find both."]),
    P("Answers to the revision questions are in the answer section, with the method "
      "for each."),
    GAP(6),
    H("Before you move on"),
    P("Four things you should be able to do without help before the next "
      "chapter. If one of them is not yet secure, reread the section that "
      "taught it before attempting the mixed practice again.", 4),
    UL([
        "Write a ratio in simplest form and explain what the division preserved.",
        "Share a total in a given ratio and check that the parts recombine to the total.",
        "Scale a recipe, a plan or a map, stating the units at every step.",
        "Choose between a part-to-part and a part-to-whole comparison and say why.",
    ]),
    KEY("A ratio is a comparison; the simplest form is the comparison with the numbers removed."),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["write a ratio from a description and say what each term counts",
         "\u25a1", "\u25a1", "\u25a1"],
        ["simplify a ratio and form equivalent ratios", "\u25a1", "\u25a1", "\u25a1"],
        ["use a ratio table, a double number line and a graph", "\u25a1", "\u25a1",
         "\u25a1"],
        ["share a quantity in a two- or three-part ratio and check it",
         "\u25a1", "\u25a1", "\u25a1"],
        ["compare two ratios with a calculation and justify the comparison",
         "\u25a1", "\u25a1", "\u25a1"],
        ["explain why scaling preserves a ratio but adding does not",
         "\u25a1", "\u25a1", "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], fs=8.6),
    GAP(8),
    MYP("**Criterion A:** which calculation would you now do without checking?\n"
        "**Criterion B:** what pattern did the ratio tables reveal that a single "
        "ratio did not?\n"
        "**Criterion C:** where did a diagram carry an argument that words alone "
        "would have made slower?\n"
        "**Criterion D:** which real context changed how you understood a ratio?",
        "Reflect on the criteria"),
    ATL("In order for a student to explain a method to someone who was absent, "
        "students must name each step, give the reason for it and check the result "
        "by recombining the shares.", "ATL \u00b7 Communication"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("1.M", "MIXED 1\u201312", [
        Q("Simplify: (a) 14 : 21  (b) 30 : 45  (c) 64 : 80.", "F"),
        Q("Share 252 in the ratio 5 : 4.", "F"),
        Q("A 3.5 m length of timber is cut in the ratio 2 : 5. Find both pieces in "
          "centimetres.", "P"),
        Q("A recipe for 6 people uses 450 g of flour. How much flour is needed for 10 "
          "people?", "F"),
        Q("Which is greater, 5 : 8 or 7 : 11? Justify.", "R"),
        Q("A photograph 12 cm by 8 cm is enlarged so that its width becomes 30 cm. "
          "Find its new height.", "P"),
        Q("Three friends share a prize in the ratio 2 : 3 : 6. The largest share is "
          "\u00a3180. Find the total prize.", "P"),
        Q("A student simplifies 24 : 36 to 4 : 6 and says it is in simplest form. "
          "Identify the error and give the correct answer.", "R"),
        Q("A juice blend uses orange, mango and water in the ratio 5 : 2 : 8. State "
          "the fraction of the blend that is water.", "F"),
        Q("Two quantities are in the ratio 7 : 4 and their difference is 27. Find "
          "both quantities.", "P"),
        Q("A map has a scale of 1 : 20 000. Two villages are 4.5 km apart. How far "
          "apart are they on the map, in centimetres?", "E"),
        Q("The ratio of red to blue beads in a jar is 3 : 7. After 20 red beads are "
          "added, the ratio becomes 5 : 7. How many blue beads are there?", "E"),
    ]),
]

ANSWERS = {
    "1.1": ["2 : 5 and 2 : 7.", "18 : 12 = 3 : 2.", "(a) 2 : 3 (b) 5 : 8 (c) 3 : 2 "
            "(d) 3 : 4.", "24 cm : 480 cm = 1 : 20.", "3 : 2; 2/5 are black.",
            "63.", "The units differ, so convert to centimetres: 60 : 45 = 4 : 3.",
            "3 : 10.", "30 cm.", "Yes: 5 \u00f7 2 = 2.5, so the first quantity is 2.5 "
            "times the second.", "They are equivalent: both simplify to 3 : 4, so the "
            "same multiplicative comparison is described.", "2 : 3 = 18 : 27."],
    "1.2": ["(a) 2 : 3 (b) 3 : 5 (c) 3 : 4 (d) 3 : 4.",
            "3 : 4 = 9 : 12 = 15 : 20 = 30 : 40.",
            "10 : 12, 15 : 18, 20 : 24 (any three equivalent pairs).",
            "Yes: both simplify to 3 : 4.", "`x` = 35.", "Sugar 140 g; total 490 g.",
            "A (2 : 3).", "Counterexample: 2 : 5 = 10 : 25, but 5 : 8 \u2260 2 : 5. "
            "Adding changes the difference between the terms, while multiplying "
            "scales both by the same factor, which is what preserves a "
            "multiplicative comparison.", "54\u00b0 and 126\u00b0.", "150 km.",
            "`k` = 9.", "`n` = 8 (4 : 8 = 7 : 14, terms 21) or `n` = 3 "
            "(4 : 3 = 12 : 9, terms 21).", "108 students (6 parts = 12)."],
    "1.3": ["6 : 14, 9 : 21, 15 : 35.", "72 km, 96 km, 120 km.", "35 km.",
            "(a) \u00a30.80 per pen (b) \u00a31.50 per kg (c) 80 km per hour.",
            "1 L of syrup.", "20 minutes.", "(5, 22): 22 \u00f7 5 = 4.4, not 4, so the "
            "point is off the line.", "1.2 kg for 12 people, 2 kg for 20; 75 g per "
            "person.", "The first: doubling both rows keeps the quotient constant. "
            "The second does not, because 4/1 \u2260 7/2.", "\u00a31.20 covers 1 m, "
            "\u00a32.40 covers 2 m, and so on; cost \u00f7 metres is always 1.2, which "
            "is the gradient of a straight line through the origin.",
            "3 : 8 = 1 : 8/3 and 3 : 8 = 3/8 : 1.", "2.1 cm."],
    "1.4": ["\u00a345 and \u00a327.", "40, 60 and 80.", "36 and 60.",
            "Larger 63, total 99.", "27 and 72.", "70, 30 and 20.",
            "Length 21 cm, width 9 cm.", "40\u00b0, 60\u00b0 and 80\u00b0.",
            "4 : 5 is greater: 4/5 = 0.8 > 7/9 \u2248 0.778; cross-products 36 > 35.",
            "100, 120 and 140.", "\u00a3480 (one part is \u00a360).",
            "880 g: one part is 80 g and there are 11 parts."],
    "1.M": ["(a) 2 : 3 (b) 2 : 3 (c) 4 : 5.", "140 and 112.",
            "100 cm and 250 cm.", "750 g.",
            "5 : 8 = 0.625 and 7 : 11 \u2248 0.636, so 7 : 11 is greater "
            "(55 < 56 by cross-product).", "20 cm.", "\u00a3330 (11 parts, "
            "one part \u00a330).", "4 : 6 is not in simplest form: divide again by 2 "
            "to get 2 : 3.", "8/15.", "63 and 36.", "22.5 cm.",
            "70 blue beads: if red = 3`k` and blue = 7`k`, then (3`k` + 20) : 7`k` = 5 : 7, "
            "so 21`k` + 140 = 35`k` and `k` = 10."],
}
