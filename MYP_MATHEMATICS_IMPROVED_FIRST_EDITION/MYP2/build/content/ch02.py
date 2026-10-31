"""Chapter 2 - Proportional reasoning (Number and proportion)."""
from chbase import *

PLATE = dict(
    part="Part I \u00b7 Number and proportion", part_numeral="I", chapter_no=2,
    kicker="Number and proportion", motif="proportion",
    title_lines=["Proportional", "reasoning"],
    lead_lines=["Two quantities are proportional when one is always a fixed",
                "multiple of the other. That single number can connect a",
                "recipe to a banquet, a map to a journey and a model to the",
                "building it represents."],
    key_concept="Relationships", related=["Models", "Equivalence"],
    context="Orientation in space and time",
    inquiry_lines=["How can one constant multiplier connect a small model",
                   "to a much larger reality?"])

TITLE = "Proportional reasoning"
SHORT = "Proportional reasoning"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "What makes a relationship proportional, and what does the constant of "
       "proportionality let you predict?"),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "A single constant of proportionality links a model to the reality it "
              "represents, so a measurement in one can be converted into a claim "
              "about the other."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Relationships.** In a proportional relationship every "
        "pair of values has the same quotient, and the graph is a straight line "
        "through the origin.\n"
        "**Related \u00b7 Models.** A scale drawing or a recipe is a model: it keeps "
        "one relationship and discards everything else.\n"
        "**Related \u00b7 Equivalence.** Proportion problems are solved by writing an "
        "equivalent ratio whose missing term is the answer."),
    BOX("note", "Global context \u00b7 Orientation in space and time",
        "Exploration: how maps, plans and timelines compress a reality too large to "
        "see at once. Every scale is a decision about what to keep and what to "
        "leave out, and a good model makes that decision visible."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** How do you test whether two quantities are proportional?",
        "**Conceptual:** Why does the graph of a proportional relationship pass "
        "through the origin?",
        "**Debatable:** When is a scale model more useful than the real thing?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii",
         "Find constants of proportionality; solve proportions."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Compare proportional and non-proportional tables and graphs."],
        ["C \u00b7 Communicating", "ii, iii, iv",
         "Use scale notation; explain what a scale factor preserves."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv, v",
         "Design a nature-reserve map with a justified scale."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to decide whether a relationship is proportional, "
        "students must test the quotient for every pair, not only for the first, "
        "and describe the graph that the table would produce."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Recognise a proportional relationship from a table, a graph or a "
         "description.",
         "Say whether a table is proportional and name the test you used."],
        ["Find the constant of proportionality.",
         "State the constant as a number and as a sentence with units."],
        ["Solve proportion problems with equivalent ratios.",
         "Set up \u00a0 3 : 5 = `x` : 40 \u00a0 and solve it two ways."],
        ["Use a scale drawing or map to find real lengths.",
         "Convert a drawing length to a real length and back without losing the "
         "unit."],
        ["Recognise similar figures and use a scale factor.",
         "Find a missing side of a similar figure and justify the factor."],
        ["Distinguish proportional from additive change.",
         "Give one table that looks proportional and show with a calculation why "
         "it is not."],
    ], widths=[1.6, 1.8]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Simplify \u00a0 18 : 24.",
               "Find \u00a0 3/4 \u00a0 of 60.",
               "Solve \u00a0 4 : 7 = 12 : `x`.",
               "Convert \u00a0 2.5 m \u00a0 to centimetres.",
               "Which is greater, \u00a0 5 : 8 \u00a0 or \u00a0 3 : 5?",
               "Write the next three terms of 3, 6, 9, 12, \u2026."]),
    P("If three or more answers are wrong, revisit section 1.2 before continuing."),

    # ------------------------------------------------------------------ 2.1
    S("2.1", "Recognising proportional relationships", "A \u00b7 I  \u00b7  "
      "B \u00b7 II", ["Relationships", "Constant of proportionality"]),
    L("A proportional relationship is not simply a relationship that grows. It is a "
      "relationship in which every value of the second quantity is the same multiple "
      "of the first."),
    ST("03", "ENGAGE",
       "Two shops, two price lists. Which shop simply charges more per rule, and "
       "which one behaves differently?"),
    P("Shop A sells ribbon at \u00a31.20 per metre: 2 m cost \u00a32.40, 5 m cost "
      "\u00a36.00. Shop B charges \u00a32 for the first metre and \u00a31.20 for each "
      "metre after that: 2 m cost \u00a33.20, 5 m cost \u00a36.80. Both price lists "
      "rise. Only one of them is proportional."),
    PHOTO("ch02_model.jpg", 1.5,
          "An architectural scale model keeps the proportions of the building and "
          "discards its materials, its weight and its plumbing. A model is a set of "
          "deliberate decisions about what to keep.",
          "Photograph: Pexels, free licence (see the image register)."),
    P("Before reading on, work out the cost per metre for both shops at 2 m and at "
      "5 m. Write a sentence that says which shop's price per metre stays constant."),
    ST("04", "EXPLORE",
       "Do the quotients agree?"),
    P("Copy the two tables. For each pair, divide the second quantity by the first "
      "and record the result to two decimal places."),
    TABLE(["Shop A length (m)", "2", "3", "4", "5", "6"],
          [["Cost (\u00a3)", "2.40", "3.60", "4.80", "6.00", "7.20"],
           ["Cost \u00f7 length", "1.20", "1.20", "1.20", "1.20", "1.20"]],
          widths=[1.4, 0.75, 0.75, 0.75, 0.75, 0.75]),
    TABLE(["Shop B length (m)", "1", "2", "3", "4", "5"],
          [["Cost (\u00a3)", "2.00", "3.20", "4.40", "5.60", "6.80"],
           ["Cost \u00f7 length", "2.00", "1.60", "1.47", "1.40", "1.36"]],
          widths=[1.4, 0.75, 0.75, 0.75, 0.75, 0.75]),
    OL(["Which table has the same quotient in every column?",
        "Plot both sets of points on one set of axes. What shape does each make?",
        "Does either line pass through the origin? What does that mean about the "
        "cost of 0 metres?",
        "Write a conjecture: a table is proportional if and only if \u2026",
        "Test your conjecture on the pairs (1, 4), (2, 7), (3, 10). Does the second "
        "quantity grow by a constant amount each time? Is the relationship "
        "proportional?",
        "Invent a table of your own that grows but is not proportional, and one that "
        "is. Swap with a partner and test each other's."]),
    ST("05", "EXPLAIN"),
    DEF("Two quantities are in `direct proportion` when one is a constant multiple "
        "of the other: `y` = `k x`, where `k` is not zero. The constant `k` is the "
        "`constant of proportionality`. A relationship is proportional exactly when "
        "`y` \u00f7 `x` has the same value for every pair, and its graph is a "
        "straight line through the origin."),
    DIAG(210, "prop_graph",
         "A proportional relationship graphed: cost against volume at "
         "\u00a33 per litre. Equal quotients produce equal gradients, and a zero "
         "volume costs zero."),
    KEY("Two tests, used together. **Divide:** if `y` \u00f7 `x` is constant, the "
        "relationship is proportional. **Graph:** if the points lie on a straight "
        "line through the origin, it is proportional. A straight line that misses the "
        "origin is called linear, not proportional."),
    P("Proportional relationships are everywhere in measurement: cost and quantity at "
      "a fixed unit price; distance and time at a steady speed; the circumference and "
      "diameter of any circle; the mass and volume of one material. Recognising one "
      "means you can predict a value you have not measured."),
    WE("2.1.1", "Find the constant",
       "Four litres of paint cost \u00a334. Find the constant of proportionality and "
       "the cost of 7 litres.",
       ["The constant is the cost per litre: `k` = 34 \u00f7 4 = 8.5.",
        "Write the relationship: cost = 8.5 \u00d7 litres.",
        "For 7 litres: 8.5 \u00d7 7 = \u00a359.50.",
        "State the constant in words, with its unit: \u00a38.50 per litre."],
       "`k` = 8.5; 7 litres cost \u00a359.50",
       "Check by ratio: 34 : 4 = 59.5 : 7, since 34 \u00d7 7 = 4 \u00d7 59.5 = 238."),
    WE("2.1.2", "Proportional or not?",
       "A taxi charges \u00a34 to start plus \u00a32 per kilometre. Is the cost "
       "proportional to the distance? Justify with a table.",
       ["Build a table: 1 km \u00a36, 2 km \u00a38, 3 km \u00a310, 4 km \u00a312.",
        "Divide: 6 \u00f7 1 = 6, 8 \u00f7 2 = 4, 10 \u00f7 3 \u2248 3.33. The "
        "quotients are not constant.",
        "The graph is a straight line, but it starts at \u00a34, not at \u00a30, so "
        "it does not pass through the origin.",
        "The cost is linear but not proportional; the fixed charge is what breaks the "
        "proportionality."],
       "Not proportional \u2014 the quotients differ and the line misses the origin.",
       "At 0 km the cost is \u00a34, whereas a proportional relationship must give 0."),
    WE("2.1.3", "Reasoning from the graph",
       "A line passes through (0, 0) and (6, 15). State the constant of "
       "proportionality and the value of `y` when `x` = 10.",
       ["Because the line passes through the origin, `k` = `y` \u00f7 `x`.",
        "Using the point (6, 15): `k` = 15 \u00f7 6 = 2.5.",
        "Then `y` = 2.5`x`, so when `x` = 10, `y` = 25.",
        "Check the point is on the line: 25 \u00f7 10 = 2.5, the same constant."],
       "`k` = 2.5; `y` = 25",
       "Any two points on a proportional line give the same quotient."),
    ERR("\u201cThe table adds 3 each time, so it is proportional.\u201d Constant "
        "addition gives a linear pattern, not a proportional one: 2, 5, 8, 11 grows "
        "by 3 but 5 \u00f7 2 \u2260 8 \u00f7 5. Proportionality is about a constant "
        "multiplier, so test by dividing."),
    PRAC("2.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Find the constant of proportionality: (a) 5 kg cost \u00a312.50  "
          "(b) 8 m of cable cost \u00a336  (c) 3 hours produce 195 parts.", "F"),
        Q("A car travels 240 km in 3 hours at a steady speed. Write the relationship "
          "and find the distance in 7 hours.", "F"),
        Q("Which of these tables are proportional? (a) 2, 4, 6 with 7, 14, 21  "
          "(b) 1, 2, 3 with 5, 8, 11  (c) 4, 6, 8 with 10, 15, 20.", "F"),
        Q("A photocopier produces 84 pages in 3 minutes. How many pages in 11 "
          "minutes?", "F"),
        Q("A line passes through the origin and (4, 10). State `k` and find `y` when "
          "`x` = 14.", "F"),
        Q("A plumber charges \u00a340 call-out plus \u00a325 per hour. Make a table "
          "for 1 to 4 hours, then explain why the charge is not proportional to the "
          "time.", "R"),
        Q("Two students disagree. One says \u201ca proportional graph is a straight "
          "line\u201d, the other says \u201ca straight-line graph is "
          "proportional\u201d. Who is right, and what is the counterexample?", "R"),
        Q("A recipe uses 3 eggs for every 8 portions. How many eggs are needed for 28 "
          "portions?", "P"),
        Q("The cost of 7 identical books is \u00a359.50. Find the cost of 11 books and "
          "state the constant of proportionality with its unit.", "P"),
        Q("A relationship satisfies `y` = `k x`. When `x` increases from 4 to 12, "
          "`y` increases by 30. Find `k`.", "E"),
        Q("Explain why the circumference of a circle is proportional to its diameter, "
          "and state the constant in exact form.", "E"),
        Q("A shop's price list is: 1 kg \u00a34.50, 2 kg \u00a38.00, 3 kg "
          "\u00a311.50. A customer claims the price is proportional. Test the claim "
          "and describe the pricing rule you can infer.", "E"),
    ]),

    # ------------------------------------------------------------------ 2.2
    S("2.2", "Solving proportional problems", "A \u00b7 II  \u00b7  C \u00b7 II",
      ["Equivalence", "Proportion"]),
    L("A proportion is an equation saying that two ratios are equal. Solving one means "
      "finding the missing term without abandoning the relationship."),
    DEF("A `proportion` is a statement that two ratios are equal, such as "
        "`a` : `b` = `c` : `d`. The cross-product condition `a d` = `b c` follows "
        "from multiplying both sides by `b d`, and it holds for every true "
        "proportion."),
    DIAG(150, "proportion_table",
         "Scaling a proportion through a unit: multiplying the first column by 2.5 "
         "gives the fourth, and every pair keeps the quotient 3."),
    H("Three reliable methods"),
    OL(["**Scale by a factor.** If the known pair is multiplied by `k`, multiply the "
        "other term by the same `k`.",
        "**Find the unit rate.** Divide to get the value for one unit, then multiply.",
        "**Cross-multiply.** Write `a`/\u00a0`b` = `c`/\u00a0`d` and solve "
        "`a d` = `b c`."]),
    P("All three give the same answer when the relationship is proportional. Choose "
      "the one that keeps the numbers easiest to handle, and say which you used."),
    WE("2.2.1", "Solve by scaling",
       "A recipe for 12 people needs 600 g of rice. How much rice is needed for 45 "
       "people?",
       ["Find the scale factor from 12 to 45: 45 \u00f7 12 = 3.75.",
        "Multiply the quantity by the same factor: 600 \u00d7 3.75 = 2 250 g.",
        "State the answer in a sensible unit: 2.25 kg.",
        "Check with the unit rate: 600 \u00f7 12 = 50 g per person, and "
        "50 \u00d7 45 = 2 250 g."],
       "2 250 g, or 2.25 kg",
       "Both methods agree, and 2.25 kg is plausible for 45 servings."),
    DIAG(150, "proportional_recipe",
         "Scaling a recipe by 3.75. Every ingredient is multiplied by the same "
         "factor, so the dish tastes the same."),
    WE("2.2.2", "Solve by cross-multiplying",
       "If 5 pens cost \u00a34, how much do 8 pens cost?",
       ["Write the proportion: 5/\u00a04 = 8/\u00a0`x`, where `x` is the cost in "
        "pounds.",
        "Cross-multiply: 5`x` = 32.",
        "Divide both sides by 5: `x` = 6.4.",
        "State the answer with its unit: \u00a36.40."],
       "8 pens cost \u00a36.40",
       "The unit price is \u00a30.80, and 8 \u00d7 0.80 = 6.40."),
    WE("2.2.3", "A proportion with a fractional term",
       "A tap fills 3/4 of a tank in 18 minutes. How long does it take to fill the "
       "whole tank?",
       ["Let `t` be the time for the whole tank. Then 18/\u00a0(3/4) = `t`/\u00a01.",
        "18 \u00f7 (3/4) = 18 \u00d7 4/3 = 24.",
        "So `t` = 24 minutes.",
        "Check: three quarters of 24 minutes is 18 minutes, as stated."],
       "24 minutes",
       "The whole is larger than three quarters, so the time must be larger than 18 "
       "minutes."),
    ERR("Setting up the proportion upside down. \u201c5 pens cost \u00a34, so 8 pens "
        "cost `x`\u201d gives 5/\u00a08 = 4/\u00a0`x`, which solves to \u00a36.40 "
        "only by accident here. Keep the same quantity on top of both fractions: "
        "pens over pens, money over money."),
    PRAC("2.2", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Solve: (a) 3 : 5 = `x` : 45  (b) 7 : 4 = 21 : `x`  (c) `x` : 9 = 8 : 12.",
          "F"),
        Q("If 6 identical notebooks cost \u00a39, what do 10 cost?", "F"),
        Q("A car uses 8 litres to travel 96 km. How many litres for 156 km?", "F"),
        Q("A recipe for 4 people needs 300 g of pasta. How much for 10 people?", "F"),
        Q("A map scale is 1 : 25 000. A road is 8 cm on the map. Find its real length "
          "in kilometres.", "F"),
        Q("A tap fills 2/5 of a tank in 12 minutes. How long to fill it completely?",
          "P"),
        Q("Two quantities are proportional. When the first is 15 the second is 40. "
          "Find the second when the first is 21.", "P"),
        Q("A printer prints 45 pages in 3 minutes. How long for 300 pages? Give the "
          "answer in minutes and seconds.", "P"),
        Q("A recipe uses flour and sugar in the ratio 5 : 2. If 350 g of flour is "
          "used, find the mass of sugar and the total mass.", "P"),
        Q("A photograph 12 cm by 8 cm is enlarged so that the width is 30 cm. Find "
          "the new height, and the factor by which the area increases.", "E"),
        Q("A model car is 18 cm long and the real car is 4.5 m long. Find the scale "
          "as a ratio in the form 1 : `n`.", "E"),
        Q("Two taps run at constant rates. Tap A fills 5 litres in 3 minutes; tap B "
          "fills 8 litres in 5 minutes. Together, how long will they take to fill a "
          "120-litre tank?", "E"),
    ]),

    # ------------------------------------------------------------------ 2.3
    S("2.3", "Scale drawings, maps and similar figures", "C \u00b7 III  \u00b7  "
      "D \u00b7 II", ["Models", "Scale"]),
    L("A scale drawing is a proportional model of something too large or too small to "
      "handle at full size. Every length is multiplied by the same scale factor, and "
      "every angle is unchanged."),
    DEF("A drawing is to `scale` when every length in the drawing is the same "
        "multiple of the corresponding real length. The multiplier is the "
        "`scale factor`; a map is often written as a ratio, 1 : 50 000, meaning "
        "1 unit on the map represents 50 000 of the same units on the ground."),
    DIAG(180, "scale_pair",
         "A model at 1 : 15 and the object it represents. Lengths are multiplied by "
         "15; angles are unchanged."),
    P("Converting between drawing and reality is a multiplication, so the only real "
      "care needed is with units. A scale of 1 : 50 000 used with centimetres gives "
      "centimetres on the ground, which must then be converted to metres or "
      "kilometres."),
    PHOTO("ch02_map.jpg", 1.5,
          "A compass on a printed map. The map keeps direction and relative "
          "distance, and discards height, weather and time \u2014 a model is defined "
          "as much by what it leaves out as by what it keeps.",
          "Photograph: public domain, via Wikimedia Commons (see the image register)."),
    WE("2.3.1", "Map to ground",
       "A map has scale 1 : 50 000. Two villages are 7 cm apart on the map. Find the "
       "real distance in kilometres.",
       ["Multiply the map length by the scale: 7 \u00d7 50 000 = 350 000 cm.",
        "Convert to metres: 350 000 \u00f7 100 = 3 500 m.",
        "Convert to kilometres: 3 500 \u00f7 1 000 = 3.5 km.",
        "Write the answer with the unit the question asked for: 3.5 km."],
       "3.5 km",
       "Sanity check: 1 cm represents 0.5 km, so 7 cm represents 3.5 km."),
    WE("2.3.2", "Ground to map",
       "A garden is 24 m long. On a plan it is drawn 16 cm long. Find the scale of the "
       "plan in the form 1 : `n`.",
       ["Convert to the same unit: 24 m = 2 400 cm.",
        "The scale factor is 2 400 \u00f7 16 = 150.",
        "So 1 cm on the plan represents 150 cm in the garden.",
        "The scale is 1 : 150."],
       "1 : 150",
       "Check: 16 \u00d7 150 = 2 400 cm = 24 m, as stated."),
    WE("2.3.3", "Similar figures",
       "Two rectangles are similar. The first is 6 cm by 9 cm; the second has a "
       "shorter side of 10 cm. Find its longer side.",
       ["Similar means a single scale factor applies to every side.",
        "The factor is 10 \u00f7 6 = 5/3.",
        "The longer side is 9 \u00d7 5/3 = 15 cm.",
        "Check that the ratios of corresponding sides agree: 6 : 9 = 10 : 15, since "
        "6 \u00d7 15 = 90 = 9 \u00d7 10."],
       "15 cm",
       "Cross-products agree, so the sides are in the same ratio."),
    ERR("\u201cThe map is 1 : 50 000, so 7 cm becomes 350 000 km.\u201d The scale "
        "relates like units to like units: 7 cm becomes 350 000 cm, which is 3.5 km. "
        "Convert the unit before you convert the magnitude."),
    PRAC("2.3", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("A map has scale 1 : 20 000. Find the real distance, in metres, of 6 cm on "
          "the map.", "F"),
        Q("A plan uses 1 cm for every 2 m. Find the plan length of a 14 m wall.", "F"),
        Q("A model is built at 1 : 40. The real door is 2 m high. How high is the "
          "door on the model, in centimetres?", "F"),
        Q("Two similar triangles have corresponding sides 8 cm and 20 cm. Find the "
          "scale factor.", "F"),
        Q("A photograph 15 cm by 10 cm is enlarged to 45 cm wide. Find its new height "
          "and describe how the area changes.", "P"),
        Q("A map shows a lake as a rectangle 4 cm by 2.5 cm. The scale is "
          "1 : 25 000. Find the real dimensions in metres.", "P"),
        Q("A model aircraft is 35 cm long. The real aircraft is 42 m long. Find the "
          "scale as 1 : `n`.", "P"),
        Q("Two rectangles are 5 cm \u00d7 8 cm and 12.5 cm \u00d7 20 cm. Are they "
          "similar? Justify with a calculation.", "R"),
        Q("A student says \u201ca scale of 1 : 50 means the drawing is 50 times "
          "bigger\u201d. Correct the statement and give one example.", "R"),
        Q("A garden plan is drawn at 1 : 200. The plan shows a path 3.5 cm long. The "
          "path is widened from 1.2 m to 1.5 m. How wide is it on the plan, in "
          "millimetres?", "E"),
        Q("Two similar rectangles have areas 24 cm\u00b2 and 96 cm\u00b2. Find the "
          "scale factor between them.", "E"),
        Q("A map is photocopied at 80 % of its original size. A distance measured as "
          "5 cm on the copy corresponds to 2 km in reality. Find the original scale.",
          "E"),
    ]),

    # ---------------------------------------------------------- investigate
    ST("06", "INVESTIGATE AND APPLY",
       "A plan that fits: the nature-reserve map."),
    CARD_I("A plan that fits", [
        ("p", "A nature reserve is a rectangle 2.4 km by 1.5 km. The warden wants a "
              "single A4 plan on which the whole reserve is drawn, with a 2 cm "
              "margin on every side, and on which the paths can be measured to "
              "within 10 m."),
        ("ol", ["Convert the reserve's dimensions to centimetres.",
                "An A4 page is 21.0 cm by 29.7 cm. Find the largest possible drawing "
                "area once the margins are removed.",
                "Test three candidate scales: 1 : 10 000, 1 : 12 500 and "
                "1 : 15 000. For each, work out the drawn dimensions and decide "
                "whether the whole reserve fits.",
                "Choose a scale and justify it with the measurements, not with a "
                "preference.",
                "At your chosen scale, what real distance does 1 mm on the plan "
                "represent? Is the 10 m measuring requirement met?",
                "Write a conjecture about what happens to the accuracy of a plan as "
                "the scale ratio gets larger.",
                "A path is 1.2 km long. Draw it to your scale and label its "
                "length."]),
    ]),
    CARD_D("The community orchard", [
        ("p", "A community orchard is planned as a rectangle 60 m by 45 m, divided "
              "into equal square plots. The committee must decide how many plots to "
              "make and how to draw the plan for the noticeboard."),
        ("ol", ["Find the largest square plot size that divides both dimensions "
                "exactly.",
                "How many plots does that give?",
                "Draw a scale plan at 1 : 500 and state the drawn size of one plot.",
                "The fence costs \u00a318.50 per metre. Estimate the cost of fencing "
                "the perimeter, then calculate it exactly.",
                "The committee wants at least 20 plots. What is the largest plot size "
                "that allows this, and how does it change the plan?",
                "Justify your recommendation in three sentences, using the "
                "mathematics."]),
    ]),

    # --------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("2.5", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["A relationship is proportional when `y` \u00f7 `x` is the same for every "
        "pair; its graph is a straight line through the origin.",
        "The constant of proportionality `k` carries units and meaning: cost per "
        "litre, kilometres per hour, centimetres per centimetre.",
        "A linear relationship with a non-zero starting value is not proportional.",
        "Proportions are solved by scaling, by unit rate, or by cross-multiplying, "
        "and all three must give the same answer.",
        "A scale drawing multiplies every length by the same factor and leaves every "
        "angle unchanged.",
        "Similar figures have equal angles and proportional sides."]),
    VOCAB("**proportion** \u00b7 **proportional** \u00b7 **constant of "
          "proportionality** \u00b7 **unit rate** \u00b7 **scale** \u00b7 "
          "**scale factor** \u00b7 **scale drawing** \u00b7 **similar** \u00b7 "
          "**cross-multiply** \u00b7 **linear (not proportional)**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["\u201cIt grows by the same amount, so it is proportional.\u201d",
         "Constant addition is linear, not proportional. 2, 5, 8 has a constant "
         "difference of 3 but quotients 2.5, 2.5, 2.67 that do not agree."],
        ["\u201cAny straight line is proportional.\u201d",
         "Only a line through the origin is. A \u00a34 call-out charge breaks "
         "proportionality."],
        ["\u201cScale 1 : 50 000 means the map is 50 000 times smaller in every "
         "way.\u201d",
         "It is 50 000 times smaller in length; areas scale by the square of the "
         "factor."],
        ["\u201cSimilar shapes have equal sides.\u201d",
         "Congruent shapes have equal sides; similar shapes have proportional "
         "sides."],
    ], widths=[1.5, 2.0]),
    H("Revision questions"),
    OL(["Is the table 3, 6, 9 with 12, 24, 33 proportional? Justify.",
        "A car uses 7 litres for 84 km. Find the constant of proportionality and the "
        "fuel for 150 km.",
        "A map has scale 1 : 40 000. Two points are 6.5 cm apart. Find the real "
        "distance in kilometres.",
        "Two similar rectangles have sides 9 cm and 15 cm corresponding. The smaller "
        "has area 54 cm\u00b2. Find the area of the larger.",
        "Explain in two sentences why a scale plan cannot preserve both lengths and "
        "areas by the same factor."]),
    GAP(6),
    H("Before you move on"),
    P("Four things you should be able to do without help before the next "
      "chapter. If one of them is not yet secure, reread the section that "
      "taught it before attempting the mixed practice again.", 4),
    UL([
        "Decide from a table, a graph or a description whether two quantities are proportional.",
        "Find the constant of proportionality and state its unit.",
        "Solve a proportion in either direction without cross-multiplying blindly.",
        "Use a scale factor on a drawing and say what stays the same.",
    ]),
    KEY("Proportional means one quantity is a constant multiple of the other; the constant is the whole relationship."),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["test whether a relationship is proportional and say why",
         "\u25a1", "\u25a1", "\u25a1"],
        ["find and interpret a constant of proportionality", "\u25a1", "\u25a1",
         "\u25a1"],
        ["solve a proportion by two different methods", "\u25a1", "\u25a1",
         "\u25a1"],
        ["convert between map and ground distances", "\u25a1", "\u25a1", "\u25a1"],
        ["use a scale factor on similar figures", "\u25a1", "\u25a1", "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], font_size=8.6),
    GAP(8),
    MYP("**Criterion A:** which proportion did you solve fastest, and why?\n"
        "**Criterion B:** what did the two tables reveal that one pair of values "
        "could not?\n"
        "**Criterion C:** how did you show which quantity was on top of each "
        "fraction?\n"
        "**Criterion D:** where did a model change a decision you would have made?",
        "Reflect on the criteria"),
    ATL("In order for a student to choose a scale for a plan, students must estimate "
        "the drawn dimensions before drawing, compare them with the space available "
        "and revise the scale on evidence.", "ATL \u00b7 Thinking skills"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("2.M", "MIXED 1\u201312", [
        Q("Find the constant: 12 kg cost \u00a336.", "F"),
        Q("Solve 8 : 11 = 24 : `x`.", "F"),
        Q("A recipe for 6 needs 450 g of flour. Find the mass for 15.", "F"),
        Q("A map scale is 1 : 30 000. Find 9 cm in kilometres.", "F"),
        Q("Are 4, 10, 16 with 6, 15, 24 proportional? Justify.", "R"),
        Q("A 3 m length of timber is cut in the ratio 2 : 5. Find both pieces in "
          "centimetres.", "P"),
        Q("A photograph 10 cm by 15 cm is enlarged to 25 cm wide. Find the new "
          "height.", "P"),
        Q("A student writes 3/\u00a05 = `x`/\u00a08 for \u201c3 pens to \u00a35, "
          "`x` pens to \u00a38\u201d. Is the set-up correct? Explain.", "R"),
        Q("A car travels 150 km in 2 hours at a steady speed. How far in 5 hours?",
          "P"),
        Q("A model is 1 : 25. A real window is 1.5 m wide. How wide on the model, in "
          "centimetres?", "P"),
        Q("Two similar triangles have areas 36 cm\u00b2 and 81 cm\u00b2. Find the "
          "ratio of their corresponding sides.", "E"),
        Q("A tap fills 3/8 of a tank in 15 minutes. How long for 5/8 of the tank?",
          "E"),
    ]),
]

ANSWERS = {
    "2.1": ["(a) 2.50 (b) 4.50 (c) 65.", "`d` = 80`t`; 560 km.",
            "(a) yes (b) no (c) yes.", "308 pages.", "`k` = 2.5; `y` = 35.",
            "Table 65, 90, 115, 140; 65 \u00f7 1 = 65 but 90 \u00f7 2 = 45, so not "
            "proportional \u2014 the \u00a340 call-out is a fixed charge.",
            "The first student is right: a proportional graph is straight and passes "
            "through the origin. A taxi graph is straight but starts at the call-out "
            "charge.", "10.5 eggs, so 11 whole eggs.", "\u00a393.50; \u00a38.50 per "
            "book.", "`k` = 3.75.", "`C` = \u03c0`d`, with `k` = \u03c0 exactly.",
            "Not proportional: 4.50 \u00f7 1 = 4.50, 8 \u00f7 2 = 4.00, "
            "11.50 \u00f7 3 \u2248 3.83. The price per kg falls as the quantity "
            "rises, as a bulk discount would."],
    "2.2": ["(a) 27 (b) 12 (c) 6.", "\u00a315.", "13 litres.", "750 g.",
            "2 km.", "30 minutes.", "56.", "20 minutes.",
            "Sugar 140 g; total 490 g.", "20 cm; area \u00d7 6.25.",
            "1 : 25.",
            "About 20 minutes: together they deliver 5/3 + 8/5 = 49/15 litres "
            "each minute, so 120 \u00f7 49/15 \u2248 19.8 minutes."],
    "2.3": ["1 200 m.", "7 cm.", "5 cm.", "2.5.",
            "30 cm high; the area multiplies by 9.", "1 000 m by 625 m.",
            "1 : 120.", "Yes: 12.5 \u00f7 5 = 2.5 and 20 \u00f7 8 = 2.5, so the "
            "scale factor is 2.5 in both directions.",
            "It means the drawing is 50 times smaller: 1 unit on the drawing "
            "represents 50 of the same units in reality.",
            "7.5 mm.", "Scale factor 2 (areas in the ratio 4 : 1).",
            "1 : 32 000. 5 cm on the copy is 6.25 cm on the original, and 6.25 cm "
            "represents 2 km = 200 000 cm, so 1 cm represents 32 000 cm."],
    "2.M": ["3.", "33.", "1 125 g.", "2.7 km.",
            "Yes: 6 \u00f7 4 = 1.5, 15 \u00f7 10 = 1.5 and 24 \u00f7 16 = 1.5, so "
            "each pair shares the same ratio.",
            "85.7 cm and 214.3 cm (approximately 86 cm and 214 cm).", "37.5 cm.",
            "No: the pens are on top in the first fraction and the money in the "
            "second. Keep like quantities in the same position.",
            "375 km.", "6 cm.", "2 : 3.", "25 minutes."],
}
