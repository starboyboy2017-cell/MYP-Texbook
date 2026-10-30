"""Chapter 3 - Rates and unit rates (Number and proportion)."""
from chbase import *

PLATE = dict(
    part="Part I \u00b7 Number and proportion", part_numeral="I", chapter_no=3,
    kicker="Number and proportion", motif="rates",
    title_lines=["Rates and", "unit rates"],
    lead_lines=["A rate compares quantities measured in different units.",
                "Reduced to a single unit, a rate becomes a tool for",
                "comparison: which is cheaper, which is faster, which is",
                "denser."],
    key_concept="Relationships", related=["Change", "Quantity"],
    context="Scientific and technical innovation",
    inquiry_lines=["How does a rate let you compare quantities that are not",
                   "measured in the same unit at all?"])

TITLE = "Rates and unit rates"
SHORT = "Rates and unit rates"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "Rates as comparisons across units, and the unit rate as the fair basis for "
       "a decision."),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "A rate compares quantities measured in different units, and reducing a "
              "rate to a single unit turns a difficult comparison into a direct one."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Relationships.** A rate is a ratio between a quantity "
        "and the time, space or amount it occupies.\n"
        "**Related \u00b7 Change.** Speed, flow and density all describe how one "
        "quantity changes as another changes.\n"
        "**Related \u00b7 Quantity.** The unit attached to a rate is part of its "
        "meaning: 60 km per hour is not 60."),
    BOX("note", "Global context \u00b7 Scientific and technical innovation",
        "Exploration: how engineers and scientists compare systems. A fuel "
        "consumption figure, a pump's delivery and the density of a material are all "
        "rates, and each one lets a designer predict behaviour before building "
        "anything."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** What is the difference between a ratio and a rate?",
        "**Conceptual:** Why does a unit rate make comparison fair?",
        "**Debatable:** When is the cheapest unit price not the best choice?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii",
         "Convert rates; compute unit rates; use speed, density and flow formulas."],
        ["B \u00b7 Investigating patterns", "i, ii",
         "Investigate how unit price changes with pack size."],
        ["C \u00b7 Communicating", "ii, iii",
         "Write rates with correct compound units and interpret them."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv, v",
         "Decide a contract: the breakfast club, on measured evidence."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to compare two products fairly, students must convert "
        "both to the same unit of comparison, state that unit, and check that the "
        "quantities being compared are genuinely equivalent."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Identify a rate and write it with a compound unit.",
         "Write 250 km in 4 hours as a rate with units, and say what it means."],
        ["Convert a rate to a unit rate.",
         "Reduce a price, a speed or a flow to a per-one value correctly."],
        ["Use the speed, density and flow relationships.",
         "Rearrange `s` = `d`/\u00a0`t` for any of the three quantities."],
        ["Compare products using unit price.",
         "Decide which of two pack sizes is better value and show the comparison."],
        ["Solve multi-step rate problems.",
         "Find a total time or cost where two rates act together."],
        ["Judge whether a rate comparison is fair.",
         "Name one factor a unit-price comparison ignores."],
    ], widths=[1.6, 1.8]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Simplify \u00a0 45 : 60.",
               "Find \u00a0 240 \u00f7 4.",
               "Convert \u00a0 1.5 kg \u00a0 to grams.",
               "Convert \u00a0 2 hours 15 minutes \u00a0 to minutes.",
               "A 5 kg bag costs \u00a312. Find the cost per kilogram.",
               "Write \u00a0 3/4 \u00a0 as a decimal."]),
    P("If three or more answers are wrong, revisit section 2.2 before continuing."),

    # ------------------------------------------------------------------ 3.1
    S("3.1", "What is a rate?", "A \u00b7 I", ["Relationships", "Quantity"]),
    L("A rate is a ratio whose two quantities are measured in different units. That "
      "difference is the whole point: a rate tells you how much of one thing happens "
      "for each unit of another."),
    ST("03", "ENGAGE",
       "Which pump fills the tank first? Two pumps give their output in different "
       "ways, and neither number answers the question on its own."),
    P("Pump A delivers 240 litres in 4 minutes. Pump B delivers 150 litres in 2.5 "
      "minutes. A caretaker says pump A is faster because 240 is bigger than 150. "
      "Before reading on, decide whether the caretaker is right, and write the "
      "calculation that settles it."),
    ST("04", "EXPLORE",
       "Reduce both to one unit."),
    P("Copy the table and fill in the third column by dividing the litres by the "
      "minutes."),
    TABLE(["Pump", "Litres", "Minutes", "Litres per minute"],
          [["A", "240", "4", ""], ["B", "150", "2.5", ""],
           ["C", "375", "7.5", ""]],
          widths=[0.6, 0.8, 0.8, 1.2]),
    OL(["Which pump delivers the most litres per minute?",
        "Does the pump with the largest total delivery also have the largest rate?",
        "Pump C is added. Without dividing, predict where it ranks. Then check.",
        "How long would pump B take to deliver 600 litres?",
        "How many litres would pump A deliver in an hour?",
        "Write a conjecture: when two totals differ, what must you compute before "
        "comparing them fairly?",
        "Invent two pumps where the larger total has the smaller rate."]),
    ST("05", "EXPLAIN"),
    DEF("A `rate` compares two quantities measured in different units. A `unit rate` "
        "is that comparison reduced to one unit of the second quantity: litres per "
        "minute, kilometres per hour, grams per cubic centimetre, pounds per "
        "kilogram. A unit rate is found by dividing."),
    P("Because the units are different, they cannot be cancelled away as they are in a "
      "ratio: 240 litres in 4 minutes is 60 litres per minute, and the compound unit "
      "\u201clitres per minute\u201d is retained in the answer. Writing the unit is "
      "not decoration. It is the part of the answer that says what has been "
      "measured."),
    DIAG(150, "flow_rate",
         "A pump as a rate: capacity divided by rate gives the time to fill. The unit "
         "of the answer, minutes, follows from litres \u00f7 (litres per minute)."),
    KEY("Three rates that every other rate problem in this chapter is built on: "
        "**speed** = distance \u00f7 time; **density** = mass \u00f7 volume; "
        "**unit price** = price \u00f7 quantity. Each can be rearranged, and each keeps "
        "its compound unit in the answer."),
    WE("3.1.1", "Find and interpret a unit rate",
       "A printer produces 480 pages in 6 minutes. Find the unit rate and the time "
       "needed for 1 200 pages.",
       ["Divide: 480 \u00f7 6 = 80 pages per minute.",
        "The unit rate is 80 pages per minute; the unit is part of the answer.",
        "For 1 200 pages: 1 200 \u00f7 80 = 15 minutes.",
        "Check by multiplication: 80 \u00d7 15 = 1 200 pages."],
       "80 pages per minute; 15 minutes",
       "Multiply back to the original total, and the units cancel as they should."),
    WE("3.1.2", "Choose the better buy",
       "Rice is sold in 2 kg bags for \u00a33.60 and in 5 kg bags for \u00a38.25. "
       "Which is better value per kilogram?",
       ["Unit price of the small bag: 3.60 \u00f7 2 = \u00a31.80 per kg.",
        "Unit price of the large bag: 8.25 \u00f7 5 = \u00a31.65 per kg.",
        "Compare like with like: \u00a31.65 < \u00a31.80, so the 5 kg bag is cheaper "
        "per kilogram.",
        "State the saving: 15 pence per kilogram."],
       "The 5 kg bag, at \u00a31.65 per kg against \u00a31.80 per kg",
       "Check by total: 5 kg at \u00a31.80 would cost \u00a39.00, and the bag costs "
       "\u00a38.25."),
    WE("3.1.3", "A rate with a mixed unit",
       "A cyclist covers 27 km in 1 hour 30 minutes. Find the average speed in km/h.",
       ["Convert the time to hours: 1 hour 30 minutes = 1.5 hours.",
        "Speed = distance \u00f7 time = 27 \u00f7 1.5 = 18.",
        "The unit is kilometres per hour: 18 km/h.",
        "Check: 18 \u00d7 1.5 = 27 km, the original distance."],
       "18 km/h",
       "Always convert the time unit before dividing, or the answer will carry the "
       "wrong unit."),
    ERR("\u201c480 pages in 6 minutes is 480 \u00f7 6 = 80, so 80 pages.\u201d The "
        "number is right; the answer is not. A rate without its unit is "
        "uninterpretable. Write \u201c80 pages per minute\u201d, or use the compound "
        "unit pages/min."),
    PHOTO("ch03_pour.jpg", 1.5,
          "Filling a measuring jug. The rate is visible only in the unit: millilitres "
          "per second, not simply \u201cmillilitres\u201d.",
          "Photograph: Pexels, free licence (see the image register)."),
    PRAC("3.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Find the unit rate: (a) 360 km in 4 hours  (b) \u00a37.20 for 9 kg  "
          "(c) 240 words in 3 minutes.", "F"),
        Q("Write each as a rate with a compound unit: (a) 15 litres in 5 minutes  "
          "(b) 84 students in 3 classes  (c) 450 g in 6 portions.", "F"),
        Q("A car travels 195 km in 2.5 hours. Find its average speed.", "F"),
        Q("Which is better value: 3 kg for \u00a35.10 or 5 kg for \u00a38.00?", "F"),
        Q("A tap delivers 18 litres in 1.5 minutes. How long for 60 litres?", "F"),
        Q("A 750 ml bottle of juice costs \u00a31.80 and a 1.5 litre bottle costs "
          "\u00a33.30. Find both unit prices per litre.", "P"),
        Q("A train covers 240 km in 2 hours 40 minutes. Find its average speed in "
          "km/h.", "P"),
        Q("Two printers: one prints 90 pages in 2 minutes, the other 200 pages in "
          "5 minutes. Which is faster, and by how many pages per minute?", "P"),
        Q("A recipe serves 4 and uses 0.6 kg of potatoes. Find the mass per serving "
          "in grams.", "P"),
        Q("A student claims \u201c4 kg for \u00a310 is better than 3 kg for "
          "\u00a37.20 because \u00a310 \u2212 \u00a37.20 is less than the price of "
          "1 kg\u201d. Test the reasoning with unit prices and explain the error.",
          "E"),
        Q("A car's fuel consumption is 6.5 litres per 100 km. How many kilometres per "
          "litre is that, and how much fuel is needed for 340 km?", "E"),
        Q("A tap fills a 90-litre tank in 12 minutes. A second tap fills it in 18 "
          "minutes. How long do they take together?", "E"),
    ]),

    # ------------------------------------------------------------------ 3.2
    S("3.2", "Unit prices and best buys", "A \u00b7 II  \u00b7  D \u00b7 II",
      ["Quantity", "Equivalence"]),
    L("Comparing prices is a rate problem, and the fair comparison is almost never the "
      "one the shelf label invites you to make."),
    DIAG(190, "price_bars",
         "Four pack sizes with their prices. The tallest bar is not the best value: "
         "the comparison must be made per unit of quantity, not per pack."),
    H("The comparison routine"),
    OL(["Convert every price to the same unit of quantity \u2014 usually 100 g or "
        "1 kg, or 100 ml or 1 litre.",
        "Divide price by quantity for each product.",
        "Compare the unit prices and state the winner with the units.",
        "Check the decision makes sense: a bulk pack can be worse value if it will "
        "not be used."]),
    WE("3.2.1", "Compare three pack sizes",
       "Pasta is sold at \u00a30.95 for 500 g, \u00a31.70 for 1 kg and \u00a32.40 "
       "for 1.5 kg. Which is the best value?",
       ["Convert all to price per 100 g: 0.95 \u00f7 5 = \u00a30.19; "
        "1.70 \u00f7 10 = \u00a30.17; 2.40 \u00f7 15 = \u00a30.16.",
        "The 1.5 kg pack has the lowest price per 100 g.",
        "The saving against the 500 g pack is 3p per 100 g, or 30p per kilogram.",
        "State the answer with the comparison unit: \u00a30.16 per 100 g."],
       "The 1.5 kg pack, at \u00a30.16 per 100 g",
       "Cross-check: 1.5 kg at \u00a30.19 per 100 g would cost \u00a32.85, and the "
       "pack costs \u00a32.40."),
    WE("3.2.2", "The same rate in different units",
       "A car uses 6.4 litres per 100 km. Express this in kilometres per litre.",
       ["100 km needs 6.4 litres, so 1 litre covers 100 \u00f7 6.4 km.",
        "100 \u00f7 6.4 = 15.625.",
        "The car travels 15.625 km per litre, about 15.6 km/L.",
        "Check by multiplication: 15.625 \u00d7 6.4 = 100 km."],
       "15.625 km per litre",
       "Reciprocal rates are still rates; the unit changes but the relationship does "
       "not."),
    WE("3.2.3", "A rate over a mixed quantity",
       "A 1.5 litre bottle of lemonade costs \u00a32.10 and a 330 ml can costs "
       "\u00a30.85. Which is better value per litre?",
       ["Convert both quantities to litres: 330 ml = 0.33 L.",
        "Bottle: 2.10 \u00f7 1.5 = \u00a31.40 per litre.",
        "Can: 0.85 \u00f7 0.33 = \u00a32.575\u2026 per litre, about \u00a32.58.",
        "The bottle is far better value per litre, though it may not all be drunk."],
       "The 1.5 litre bottle, at \u00a31.40 per litre",
       "Check the can: 0.33 \u00d7 2.575 \u2248 0.85, as priced."),
    ERR("\u201cThe bigger pack is always better value.\u201d Sometimes it is not: "
        "shops price small packs as loss leaders, and a bulk pack that is wasted is "
        "not cheap. Compare unit prices, then decide with the use in mind."),
    PRAC("3.2", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Find the price per 100 g: (a) \u00a31.80 for 400 g  (b) \u00a32.40 for "
          "600 g.", "F"),
        Q("Which is better value: 250 ml for \u00a31.20 or 750 ml for \u00a33.30?",
          "F"),
        Q("A 12-pack of pens costs \u00a34.80. Find the price per pen.", "F"),
        Q("A car travels 480 km on 40 litres. Find the fuel used per 100 km.", "F"),
        Q("Soap powder: 1.5 kg for \u00a34.20, 3 kg for \u00a37.80, 5 kg for "
          "\u00a312.50. Which is the best value per kg?", "P"),
        Q("Convert 45 miles per gallon to a cost per 100 miles if fuel costs "
          "\u00a31.45 per litre (\u00a31 gallon \u2248 4.55 litres).", "P"),
        Q("A café sells coffee at \u00a32.40 for 300 ml and \u00a33.20 for 450 ml. "
          "Which is better value per 100 ml?", "P"),
        Q("Two mobile contracts: \u00a39 for 5 GB and \u00a314 for 8 GB. Find the "
          "cost per GB and say which is cheaper, then name one factor the comparison "
          "ignores.", "R"),
        Q("A shop sells 6 eggs for \u00a31.80 and 10 eggs for \u00a32.80. Find both "
          "unit prices and decide which is better value, showing your working.", "P"),
        Q("A bulk pack is \u00a312 for 4 kg and a small pack is \u00a32.10 for "
          "700 g. Find both unit prices and the percentage saving per kilogram of "
          "the bulk pack.", "E"),
        Q("A shop advertises \u201820 % extra free\u2019 on a 500 g pack at the same "
          "price. By what percentage does the unit price fall?", "E"),
        Q("Fuel consumption rises from 6.0 to 7.5 litres per 100 km. By what "
          "percentage does the distance travelled per litre fall?", "E"),
    ]),

    # ------------------------------------------------------------------ 3.3
    S("3.3", "Speed, density and flow", "A \u00b7 II  \u00b7  C \u00b7 III",
      ["Change", "Quantity"]),
    L("Speed, density and flow are the three rates that carry most of the science in "
      "Year 2. Each is a division, and each can be rearranged to answer the other two "
      "questions."),
    FORMULA("`s` = `d` \u00f7 `t`          `d` = `s t`          `t` = `d` \u00f7 `s`",
            "speed = distance \u00f7 time, and its two rearrangements"),
    FORMULA("\u03c1 = `m` \u00f7 `V`          `m` = \u03c1`V`          "
            "`V` = `m` \u00f7 \u03c1",
            "density = mass \u00f7 volume, in g/cm\u00b3 or kg/m\u00b3"),
    DIAG(210, "speed_graph",
         "Distance against time at a steady 12 km/h. The gradient of the line is the "
         "speed, which is why the unit of a gradient is a rate."),
    P("A worked example in this section always states the formula, substitutes the "
      "values with their units, and then gives the answer. Writing the substitution "
      "is what makes the working checkable \u2014 by you, and by a reader."),
    WE("3.3.1", "Find the time",
       "A car travels 210 km at an average speed of 84 km/h. How long does the "
       "journey take?",
       ["Write the formula: `t` = `d` \u00f7 `s`.",
        "Substitute: `t` = 210 \u00f7 84 = 2.5.",
        "The unit follows from kilometres \u00f7 kilometres per hour, which is hours.",
        "The journey takes 2.5 hours, or 2 hours 30 minutes."],
       "2.5 hours (2 h 30 min)",
       "Check: 84 \u00d7 2.5 = 210 km, as given."),
    WE("3.3.2", "Density",
       "A metal block has mass 540 g and volume 60 cm\u00b3. Find its density in "
       "g/cm\u00b3, and its mass if it were cut to 25 cm\u00b3.",
       ["Density = mass \u00f7 volume = 540 \u00f7 60 = 9.",
        "The density is 9 g/cm\u00b3.",
        "For 25 cm\u00b3: `m` = \u03c1`V` = 9 \u00d7 25 = 225 g.",
        "Check: the volume is just over 40 % of the original, and so is the mass."],
       "9 g/cm\u00b3; 225 g",
       "Density is a property of the material, so it is unchanged by cutting the "
       "block."),
    WE("3.3.3", "Two rates together",
       "Tap A fills a tank in 6 minutes; tap B fills the same tank in 12 minutes. How "
       "long do they take together?",
       ["Convert each to a rate per minute: A fills 1/6 of the tank per minute, B "
        "fills 1/12.",
        "Together they fill 1/6 + 1/12 = 3/12 = 1/4 of the tank per minute.",
        "Time = 1 \u00f7 (1/4) = 4 minutes.",
        "Check: in 4 minutes A fills 4/6 and B fills 4/12, and 4/6 + 4/12 = 1."],
       "4 minutes",
       "Never average the times. Rates add; times do not."),
    ERR("\u201cOne tap takes 6 minutes and the other 12, so together they take "
        "9 minutes.\u201d Averaging times assumes the taps take turns. They work at "
        "the same time, so the rates add: 1/4 of the tank per minute, giving 4 "
        "minutes."),
    PHOTO("ch03_pump.jpg", 1.5,
          "A fuel pump display showing litres delivered and price per litre. The "
          "compound units on the display are the rates this section formalises.",
          "Photograph: Pexels, free licence (see the image register)."),
    PRAC("3.3", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("A car travels 330 km in 3 hours. Find the average speed.", "F"),
        Q("A cyclist rides at 18 km/h for 2.5 hours. How far?", "F"),
        Q("A train covers 405 km at 90 km/h. Find the journey time.", "F"),
        Q("A liquid has mass 246 g and volume 300 cm\u00b3. Find its density.", "F"),
        Q("A tap delivers 15 litres per minute. How long to fill a 240-litre tank?",
          "F"),
        Q("A walker covers 8 km in 1 hour 20 minutes. Find the speed in km/h.", "P"),
        Q("A steel block of density 7.8 g/cm\u00b3 has volume 150 cm\u00b3. Find its "
          "mass.", "P"),
        Q("Two pipes fill a tank in 10 and 15 minutes. How long together?", "P"),
        Q("A car travels 60 km at 80 km/h and then 90 km at 60 km/h. Find the total "
          "time and the average speed for the whole journey.", "P"),
        Q("A 1.2 kg block of material has density 2.4 g/cm\u00b3. Find its volume in "
          "cm\u00b3, then the side of the cube with that volume (to the nearest "
          "0.1 cm).", "E"),
        Q("A tap fills a tank in 8 minutes and a drain empties it in 20 minutes. Both "
          "are open. How long to fill the tank?", "E"),
        Q("A runner's pace is 4 minutes 30 seconds per kilometre. Find the speed in "
          "km/h, to two decimal places.", "E"),
    ]),

    # ----------------------------------------------------------- investigate
    ST("06", "INVESTIGATE AND APPLY",
       "The unit price trap: when the cheaper rate is not cheaper."),
    CARD_I("The unit price trap", [
        ("p", "A school canteen buys juice in three formats. The manager wants the "
              "lowest cost per litre, but the kitchen also wastes what is not used "
              "within two days."),
        ("table", ["Format", "Volume", "Price", "Used within two days"],
         [["Carton", "200 ml", "\u00a30.42", "always"],
          ["Bottle", "1 L", "\u00a31.85", "90 %"],
          ["Drum", "5 L", "\u00a38.20", "55 %"]],
         [1, 0.8, 0.8, 1.0]),
        ("ol", ["Find the cost per litre of each format.",
                "Rank the formats by cost per litre.",
                "Now compute the cost per litre actually used, allowing for waste.",
                "Does the ranking change? Explain why.",
                "The canteen serves 240 portions of 200 ml per day. How many litres "
                "does it need per day?",
                "Write a conjecture about when buying in bulk stops being better "
                "value.",
                "Recommend a purchasing rule to the manager, in three sentences, using "
                "your numbers."]),
    ]),
    CARD_D("The breakfast club contract", [
        ("p", "A breakfast club serves 120 students. A supplier offers two contracts "
              "for milk."),
        ("table", ["Contract", "Delivery", "Price"], [
            ["P", "24 one-litre bottles each week", "\u00a314.40 per delivery"],
            ["Q", "One 30-litre drum each week", "\u00a316.50 per delivery"]],
         [1, 1.4, 1.0]),
        ("ol", ["Find the cost per litre under each contract.",
                "The club uses about 22 litres a week. Which contract leaves less "
                "waste?",
                "Calculate the weekly and annual cost of each contract, taking waste "
                "into account.",
                "One litre of milk serves 8 students. Verify that 22 litres is enough "
                "for 120 students with a sensible allowance for seconds.",
                "Write the ratio of milk to students as a unit rate.",
                "Recommend a contract and justify your choice with the calculations, "
                "naming one assumption you have made."]),
    ]),

    # --------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("3.5", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["A rate compares quantities with different units and keeps its compound unit "
        "in the answer.",
        "A unit rate reduces a comparison to one unit, which is what makes "
        "comparison fair.",
        "Unit price is a rate, and the largest pack is not automatically the best "
        "value.",
        "Speed = distance \u00f7 time; density = mass \u00f7 volume; each rearranges to "
        "give the other quantities.",
        "Rates add when two agents work together; times do not.",
        "A unit-price comparison ignores waste, quality and storage, and should be "
        "reported as a comparison of one thing only."]),
    VOCAB("**rate** \u00b7 **unit rate** \u00b7 **unit price** \u00b7 **speed** "
          "\u00b7 **density** \u00b7 **flow rate** \u00b7 **compound unit** \u00b7 "
          "**per** \u00b7 **average speed** \u00b7 **best buy**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["\u201cA rate is just a number.\u201d",
         "60 means nothing until it is 60 km/h. The unit is the meaning."],
        ["\u201cThe bigger number is the faster rate.\u201d",
         "Totals are not rates. 240 in 4 minutes is 60 per minute, which is slower "
         "than 150 in 2.5 minutes (also 60)."],
        ["\u201cTogether, two taps take the average of their times.\u201d",
         "Rates add, not times: 1/6 + 1/12 = 1/4 per minute gives 4 minutes, not 9."],
        ["\u201cComparing prices means comparing prices.\u201d",
         "Compare prices per unit of the same quantity, in the same unit."],
    ], widths=[1.5, 2.0]),
    H("Revision questions"),
    OL(["Find the unit rate: 420 km in 3.5 hours.",
        "A 1.2 kg pack costs \u00a34.32. Find the price per kilogram.",
        "A tap delivers 2.5 litres per minute. How long to fill 75 litres?",
        "A block of mass 810 g has volume 300 cm\u00b3. Find its density.",
        "Two printers print 60 pages in 4 minutes and 105 pages in 6 minutes. Which "
        "is faster, and by how much per minute?"]),
    GAP(6),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["write and interpret a rate with a compound unit", "\u25a1", "\u25a1",
         "\u25a1"],
        ["find a unit rate and use it to solve a problem", "\u25a1", "\u25a1",
         "\u25a1"],
        ["compare products by unit price and say what the comparison ignores",
         "\u25a1", "\u25a1", "\u25a1"],
        ["use and rearrange the speed, density and flow relationships",
         "\u25a1", "\u25a1", "\u25a1"],
        ["solve a problem where two rates act together", "\u25a1", "\u25a1",
         "\u25a1"],
        ["convert a rate to a different but equivalent unit", "\u25a1", "\u25a1",
         "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], font_size=8.6),
    GAP(8),
    MYP("**Criterion A:** which unit rate are you now able to find without "
        "thinking?\n"
        "**Criterion B:** what pattern appeared when you compared pack sizes?\n"
        "**Criterion C:** how did you make the unit of each answer unambiguous?\n"
        "**Criterion D:** which real decision did a rate change for you?",
        "Reflect on the criteria"),
    ATL("In order for a student to defend a purchasing decision, students must "
        "present the unit prices, name the quantity being compared and state the "
        "assumption the comparison makes.", "ATL \u00b7 Communication"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("3.M", "MIXED 1\u201312", [
        Q("Find the unit rate: \u00a313.50 for 6 kg.", "F"),
        Q("A car travels 276 km in 4 hours. Find its average speed.", "F"),
        Q("Convert 90 km/h to metres per second.", "F"),
        Q("Which is better value: 400 g for \u00a32.20 or 700 g for \u00a33.50?", "F"),
        Q("A tank holds 480 litres and is filled in 16 minutes. Find the flow rate.",
          "F"),
        Q("A liquid of density 1.2 g/cm\u00b3 fills a 250 cm\u00b3 container. Find "
          "the mass.", "P"),
        Q("A journey of 180 km takes 2 hours 15 minutes. Find the average speed.", "P"),
        Q("A student converts 72 km/h to m/s by dividing by 60. Identify the error "
          "and give the correct value.", "R"),
        Q("Three packs: 250 g \u00a31.10, 500 g \u00a32.00, 1 kg \u00a33.90. Rank "
          "them by value.", "P"),
        Q("Two pumps deliver 40 litres in 5 minutes and 65 litres in 8 minutes. "
          "Together, how long for 810 litres?", "E"),
        Q("A car does 12.5 km per litre. Fuel costs \u00a31.42 per litre. Find the "
          "fuel cost of a 400 km journey.", "E"),
        Q("A recipe scales from 4 to 10 people and the cooking time is unchanged. "
          "Explain, using rates, why the time cannot simply be scaled too.", "E"),
    ]),
]

ANSWERS = {
    "3.1": ["(a) 90 km/h (b) \u00a30.80 per kg (c) 80 words per minute.",
            "(a) 3 litres per minute (b) 28 students per class (c) 75 g per portion.",
            "78 km/h.", "5 kg for \u00a38.00 (\u00a31.60 per kg against "
            "\u00a31.70).", "5 minutes.", "\u00a32.40 per litre and \u00a32.20 per "
            "litre; the larger bottle is better value.",
            "90 km/h.", "The first (45 pages per minute against 40).",
            "150 g.", "The reasoning is wrong: 4 kg for \u00a310 is \u00a32.50 per "
            "kg, and 3 kg for \u00a37.20 is \u00a32.40 per kg, so the smaller pack is "
            "better value.",
            "15.38 km per litre; 22.1 litres.", "7.2 minutes."],
    "3.2": ["(a) \u00a30.45 per 100 g (b) \u00a30.40 per 100 g.",
            "750 ml for \u00a33.30 (\u00a30.44 per 100 ml against \u00a30.48).",
            "\u00a30.40 per pen.", "8.33 litres per 100 km.",
            "The 5 kg pack at \u00a32.50 per kg (1.5 kg \u00a32.80; 3 kg "
            "\u00a32.60).",
            "\u00a314.66 per 100 miles: 100 \u00f7 45 = 2.22 gallons, "
            "2.22 \u00d7 4.55 = 10.11 litres, 10.11 \u00d7 \u00a31.45 = \u00a314.66.",
            "The 450 ml at \u00a30.71 per 100 ml (300 ml is \u00a30.80).",
            "\u00a31.80 and \u00a31.75 per GB; the larger bundle is cheaper per GB, "
            "but the comparison ignores coverage and whether 8 GB is needed.",
            "\u00a30.30 and \u00a30.28 per egg; the 10-pack is better value.",
            "\u00a33.00 per kg and \u00a33.00 per kg \u2014 equal (4 kg at "
            "\u00a312 is \u00a33.00 per kg; 700 g at \u00a32.10 is \u00a33.00 per "
            "kg), so the percentage saving is 0 %.", "16.7 %.", "20 %."],
    "3.3": ["110 km/h.", "45 km.", "4.5 hours.", "0.82 g/cm\u00b3.", "16 minutes.",
            "6 km/h.", "1 170 g.", "6 minutes.",
            "Total time 2.25 hours; average speed 66.7 km/h.",
            "500 cm\u00b3; side 7.9 cm.", "13.3 minutes.", "13.33 km/h."],
    "3.M": ["\u00a32.25 per kg.", "69 km/h.", "25 m/s.",
            "700 g for \u00a33.50 (\u00a30.50 per 100 g against \u00a30.55).",
            "30 litres per minute.", "300 g.", "80 km/h.",
            "Dividing by 60 only converts hours to minutes. 72 km/h is "
            "72 000 m \u00f7 3 600 s = 20 m/s.",
            "1 kg at \u00a33.90 (\u00a30.39 per 100 g), then 500 g (\u00a30.40), "
            "then 250 g (\u00a30.44).",
            "About 50 minutes: the rates are 8 and 8.125 litres per minute, so "
            "810 \u00f7 16.125 \u2248 50.2 minutes.", "\u00a345.44.",
            "Browning and oven heat are not proportional to quantity; a larger "
            "quantity needs a longer time in the same oven, but the relationship is "
            "not a simple multiple."],
}
