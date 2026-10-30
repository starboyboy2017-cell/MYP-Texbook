"""Chapter 5 - Percentages and applications."""
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.flow import Spacer, Pager
import diagrams as dg
from helpers import (section, lead, body, h3, lst, panel, atl, we, practice, q, fig,
                     diag, table, note, gap, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
    part="Part II \u00b7 Fractions, decimals and percentages", part_numeral="II",
    chapter_no=5,
    kicker="Fractions, decimals and percentages",
    title_lines=["Percentages", "and applications"],
    lead_lines=["Per cent means \u201cper hundred\u201d, and that is the whole",
                "idea. Everything else \u2014 a discount, a tax, a budget,",
                "a price rise \u2014 is a fraction of a hundred wearing",
                "a different coat."],
    key_concept="Relationships", related=["Quantity", "Equivalence"],
    context="Fairness and development",
    inquiry_lines=["How does a percentage make two different quantities comparable,",
                   "and when does comparing them mislead?"])

TITLE = "Percentages and applications"
SHORT = "Percentages"


def build(bk, p):
    reset_counters(5)
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER"))
    p.add(Spacer(8))
    p.add(DataTable(["Statement of inquiry",
                     "A percentage expresses a part in units of one hundred, which makes "
                     "quantities with different wholes comparable; that same act of "
                     "standardising can clarify a decision or conceal what produced it."],
                    [], widths=[1, 3.2], font_size=9.2, stripe=False))
    gap(p, 10)
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Relationships.** A percentage relates a part to "
                     "its whole, so the whole must always be named.\n"
                     "**Related \u00b7 Quantity.** A percentage of a quantity is found by "
                     "dividing by 100 and multiplying by the percentage.\n"
                     "**Related \u00b7 Equivalence.** 25 %, 0.25 and 1/4 are three names for "
                     "one number, and each makes a different calculation easy."))
    p.add(Panel("note", title="Global context \u00b7 Fairness and development",
                text="Exploration: how discounts, taxes, interest and aid targets are "
                     "communicated, and how a percentage can be accurate and still "
                     "misleading when its base is hidden."))
    gap(p, 8)
    h3(p, "Inquiry questions")
    lst(p, ["**Factual:** How do you find a percentage of a quantity, and how do you "
            "express one quantity as a percentage of another?",
            "**Conceptual:** Why does a 20 % discount followed by a 20 % increase not "
            "restore the original price?",
            "**Debatable:** Is a \u201c50 % off\u201d label informative if the original "
            "price is unknown?"])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Convert between forms; find percentages of quantities; increase and decrease."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate whether two successive discounts equal their sum."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Present a price comparison so that the base of each percentage is visible."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Cost a market stall, set prices and evaluate a budget."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 6)
    atl(p, "In order for a student to judge a percentage claim, students must identify the "
           "base it refers to before accepting the figure, because the same number can "
           "describe very different quantities.", "ATL \u00b7 Critical thinking")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("02", "ENGAGE", "Two shops, two discounts."))
    body(p, "Shop A offers 30 % off a shirt marked 40. Shop B offers 20 % off the same "
            "shirt marked 45. Both signs look generous. One shirt is cheaper, and the "
            "difference is only visible after both percentages have been applied to their "
            "own base \u2014 which is the whole point of a percentage, and the whole danger "
            "of one.")
    fig(p, "ch05_plate_banner.jpg",
        "A shop window standardises everything to hundreds. The standardising is what "
        "makes comparison possible; the base is what makes it honest.", wide=True)

    p.add(Stage("03", "EXPLORE", "Build a hundred square."))
    body(p, "Draw a 10 by 10 square of 100 cells. Shade 35 of them. Now answer without "
            "counting the shading again:")
    lst(p, ["What fraction of the square is shaded?",
            "What decimal is shaded?",
            "What percentage is shaded?",
            "Shade a further 15 cells. What percentage is shaded now, and how did you get "
            "the answer?",
            "What percentage would you need to shade to reach exactly three quarters?"],
        ordered=True)
    diag(p, 118, dg.percent_hundred, "A hundred square makes 35 % visible as 35/100 = "
                                     "0.35. The three notations describe one region.",
         wide=True)

    # --------------------------------------------------------------- 5.1
    section(p, "5.1", "Per cent: a proportion of 100", "A \u00b7 i", ["Equivalence"])
    panel(p, "definition", title="Percentage",
          text="A **percentage** is a fraction with denominator 100. So 47 % = 47/100 = "
               "0.47. The symbol % is shorthand for \u201cdivided by 100\u201d.")
    h3(p, "Converting between the three forms")
    table(p, ["From", "To", "Method", "Example"], [
        ["Fraction", "Decimal", "Divide numerator by denominator", "3/8 = 0.375"],
        ["Decimal", "Percentage", "Multiply by 100", "0.375 = 37.5 %"],
        ["Percentage", "Decimal", "Divide by 100", "45 % = 0.45"],
        ["Percentage", "Fraction", "Write over 100 and simplify", "45 % = 9/20"],
        ["Fraction", "Percentage", "Decimal first, then multiply by 100", "3/8 = 37.5 %"],
    ], widths=[0.75, 0.75, 1.5, 0.95])
    we(p, "5.1.1", "Three names for one number",
       "Express 5/8 as a decimal and as a percentage.",
       ["5 \u00f7 8 = 0.625.",
        "0.625 \u00d7 100 = 62.5.",
        "So 5/8 = 0.625 = 62.5 %."],
       answer="0.625 and 62.5 %",
       check="62.5 % of 8 = 5, so the conversion is consistent \u2713")
    panel(p, "error", title="Forgetting that the base must be 100",
          text="A student writes 0.4 % for 0.4. Percentages are already hundredths, so 0.4 "
               "= 40 %. Reversing the direction of the conversion is the most common "
               "percentage error; check by asking whether the answer is bigger or smaller "
               "than the original number.")
    practice(p, "5.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Write as percentages: (a) 0.6 (b) 0.08 (c) 1.25.", "F"),
        q("Write as decimals: (a) 45 % (b) 7 % (c) 120 %.", "F"),
        q("Write as fractions in simplest form: (a) 25 % (b) 60 % (c) 12.5 %.", "F"),
        q("Write 7/20 as a percentage.", "F"),
        q("Explain why 1 % of a quantity is not always small.", "R"),
        q("A survey of 40 students finds 12 prefer football. Write this as a percentage.",
          "P"),
        q("Which is larger, 35 % of 80 or 40 % of 70? Show your reasoning.", "R"),
        q("Find a percentage that is equal to 2/3 when rounded to one decimal place, and "
          "state whether it is exact.", "E"),
    ])

    # --------------------------------------------------------------- 5.2
    section(p, "5.2", "Finding a percentage of a quantity", "A \u00b7 ii", ["Quantity"])
    panel(p, "definition", title="The method",
          text="To find `p` % of a quantity: convert the percentage to a decimal and "
               "multiply, or multiply by `p` and divide by 100. So 15 % of 240 = 0.15 "
               "\u00d7 240 = 36.")
    body(p, "The decimal method is faster with a calculator; the fraction method is often "
            "faster in the head. 25 % of 84 is a quarter of 84, which is 21 \u2014 no "
            "calculator needed. Choosing the notation that fits the numbers is a "
            "mathematical decision, not a shortcut.")
    diag(p, 74, dg.percent_of_quantity, "10 % and 5 % land-markers give 15 % of 240 without "
                                        "a calculator: 24 + 12 = 36.", wide=True)
    we(p, "5.2.1", "Two routes to the same answer",
       "Find 35 % of 260.",
       ["Decimal route: 35 % = 0.35, and 0.35 \u00d7 260 = 91.",
        "Fraction route: 35/100 \u00d7 260 = 9 100/100 = 91.",
        "Landmark route: 10 % is 26, so 30 % is 78, and 5 % is 13; 78 + 13 = 91."],
       answer="91",
       check="35 % is a bit more than a third, and a third of 260 is about 87 \u2713")
    we(p, "5.2.2", "Expressing one quantity as a percentage of another",
       "A class of 32 students has 24 who walk to school. What percentage walk?",
       ["Divide the part by the whole: 24 \u00f7 32 = 0.75.",
        "Multiply by 100: 75 %.",
        "Check: 75 % of 32 = 24."],
       answer="75 %",
       check="0.75 \u00d7 32 = 24 \u2713")
    practice(p, "5.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Find (a) 10 % of 90 (b) 25 % of 84 (c) 50 % of 7.", "F"),
        q("Find (a) 15 % of 240 (b) 35 % of 260 (c) 60 % of 45.", "F"),
        q("Find 12.5 % of 96.", "F"),
        q("A team plays 40 matches and wins 26. What percentage does it win?", "F"),
        q("Explain how to find 15 % of a quantity using only 10 % and half of that.",
          "R"),
        q("A shop has 180 items, of which 45 are sold. What percentage remains?", "P"),
        q("In a school of 750 students, 54 % are girls. How many boys are there?", "P"),
        q("A jacket costs 64. Its price is reduced by 12.5 %. Find the new price using "
          "fractions.", "E"),
        q("A student says 20 % of 50 is 10 and 50 % of 20 is 10, so the two statements are "
          "the same. Are they? Explain.", "E"),
    ])

    # --------------------------------------------------------------- 5.3
    section(p, "5.3", "Increasing and decreasing by a percentage", "A \u00b7 iii",
            ["Quantity", "Change"])
    body(p, "An increase of 20 % can be calculated in two ways: find 20 % and add it, or "
            "multiply by 1.20 directly. The second method is shorter and, more importantly, "
            "it generalises: a multiplier of 0.85 decreases by 15 % in one step.")
    panel(p, "keyidea", title="The multiplier",
          text="An increase of `p` % multiplies by 1 + `p`/100. A decrease of `p` % "
               "multiplies by 1 \u2212 `p`/100. So +20 % is \u00d7 1.20, \u221215 % is "
               "\u00d7 0.85, and +100 % is \u00d7 2.")
    we(p, "5.3.1", "A price rise",
       "A bus fare of 2.40 rises by 15 %. Find the new fare.",
       ["The multiplier is 1 + 0.15 = 1.15.",
        "2.40 \u00d7 1.15 = 2.76.",
        "Check: the increase is 0.36, which is 15 % of 2.40."],
       answer="2.76",
       check="2.40 + 0.36 = 2.76 \u2713")
    we(p, "5.3.2", "Comparing two changes",
       "A quantity rises by 20 % and then falls by 20 %. Is it back to where it started?",
       ["Rising by 20 % multiplies by 1.20; falling by 20 % multiplies by 0.80.",
        "Overall multiplier: 1.20 \u00d7 0.80 = 0.96.",
        "So the quantity ends at 96 % of its original value: a 4 % decrease.",
        "The two percentages applied to different bases, so they do not cancel."],
       answer="No \u2014 it finishes 4 % below the starting value.",
       check="On 100: 120, then 96 \u2713")
    panel(p, "error", title="Adding percentages that apply to different bases",
          text="A 20 % rise followed by a 20 % fall is not 0 %. The second percentage is "
               "taken from the new, larger value, so it removes more than the first added. "
               "Multiply the multipliers; never add the percentages.")
    practice(p, "5.3", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Increase 80 by 10 %.", "F"),
        q("Decrease 250 by 20 %.", "F"),
        q("Find the multiplier for (a) +35 % (b) \u221212 % (c) +150 %.", "F"),
        q("A salary of 1 800 rises by 4 %. Find the new salary.", "F"),
        q("Explain why a 10 % rise followed by a 10 % fall does not return to the original "
          "value.", "R"),
        q("A phone costs 320 and is reduced by 15 % in a sale, then by a further 10 % at the "
          "till. Find the final price.", "P"),
        q("After a 25 % increase a price is 75. Find the original price.", "P"),
        q("A population grows by 5 % in year 1 and 8 % in year 2. Find the two-year "
          "percentage change.", "E"),
        q("Find a single multiplier equivalent to +20 % followed by \u221225 %.", "E"),
    ])

    # --------------------------------------------------------------- 5.4
    section(p, "5.4", "Discounts, taxes and budgets", "D \u00b7 i  \u00b7  A \u00b7 iii",
            ["Quantity", "Model"])
    body(p, "Financial contexts are where percentages meet decisions. A discount reduces a "
            "price; a tax adds to it; a budget allocates a whole into parts. Each requires "
            "the same three questions: what is the base, what is the percentage, and is the "
            "result sensible?")
    diag(p, 96, dg.price_tag, "A reduction of 25 % applies to the marked price, not to the "
                              "reduced price. Naming the base is part of the calculation.",
         wide=True)
    we(p, "5.4.1", "Discount then tax",
       "An item marked 80 is reduced by 25 %, then a 10 % tax is added to the reduced "
       "price. Find the final amount.",
       ["Reduction: 80 \u00d7 0.75 = 60.",
        "Tax on the reduced price: 60 \u00d7 1.10 = 66.",
        "Combined multiplier: 0.75 \u00d7 1.10 = 0.825, so the final amount is 82.5 % of "
        "the marked price."],
       answer="66",
       check="80 \u00d7 0.825 = 66 \u2713")
    we(p, "5.4.2", "Allocating a budget",
       "A household income of 2 400 is allocated as 35 % housing, 25 % food, 15 % "
       "transport, 10 % school costs and the rest to savings. Find each amount.",
       ["Housing: 0.35 \u00d7 2 400 = 840.",
        "Food: 0.25 \u00d7 2 400 = 600.  Transport: 0.15 \u00d7 2 400 = 360.",
        "School: 0.10 \u00d7 2 400 = 240.",
        "Percentages used: 35 + 25 + 15 + 10 = 85, so savings take 15 %: 360."],
       answer="840, 600, 360, 240 and 360 to savings.",
       check="840 + 600 + 360 + 240 + 360 = 2 400 \u2713")
    practice(p, "5.4", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("A 60 item is reduced by 15 %. Find the sale price.", "F"),
        q("A bill of 45 attracts 10 % tax. Find the total.", "F"),
        q("A budget of 900 allocates 40 % to rent. How much is left?", "F"),
        q("Find the total cost of a 120 item with 20 % discount and 5 % tax.", "F"),
        q("Explain why a shop can honestly advertise \u201c25 % off\u201d and still make a "
          "profit.", "R"),
        q("A stall sells 150 items at 4.50 each, with 8 % of revenue paid as a market fee. "
          "Find the amount the trader keeps.", "P"),
        q("A family spends 30 % of income on rent and 45 % on food and transport. It saves "
          "500. Find the income.", "P"),
        q("Two shops discount the same 200 item: shop A by 30 %, shop B by 20 % then a "
          "further 10 % at the till. Which is cheaper, and by how much?", "E"),
        q("Design a budget for 3 000 in which savings are exactly 12 % and no category "
          "exceeds 40 %.", "E"),
    ])

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("04", "INVESTIGATE"))
    section(p, "Investigation 5", "Do two discounts add up?", None, ["Pattern", "Quantity"])
    body(p, "A shop advertises \u201c20 % off, then a further 20 % off at the till\u201d. "
            "Most customers assume the total discount is 40 %. Test that assumption on a "
            "range of starting prices before deciding.")
    table(p, ["Starting price", "After 20 %", "After a further 20 %", "Total discount %"], [
        ["50", "\u2026", "\u2026", "\u2026"], ["100", "\u2026", "\u2026", "\u2026"],
        ["250", "\u2026", "\u2026", "\u2026"], ["400", "\u2026", "\u2026", "\u2026"],
    ], widths=[1.0, 0.9, 1.1, 1.1])
    h3(p, "Your investigation")
    lst(p, ["Complete the table.",
            "Is the total discount the same for every starting price? Explain why.",
            "Write the total discount as a single multiplier.",
            "Predict the total discount for two successive discounts of `p` % each, and "
            "test your rule with `p` = 10 and `p` = 50.",
            "Find the single discount that is equivalent to 20 % followed by 20 %.",
            "Explain, in one sentence, why the two discounts do not add."],
        ordered=True)
    panel(p, "keyidea", title="The general result",
          text="Two successive discounts of `p` % and `q` % multiply: the combined "
               "multiplier is (1 \u2212 `p`/100)(1 \u2212 `q`/100). For 20 % and 20 % this "
               "is 0.8 \u00d7 0.8 = 0.64, a total discount of 36 %, always \u2014 the "
               "difference from 40 % is the discount on the discount.")
    atl(p, "In order for a student to test a claim that \u201cfeels obvious\u201d, students "
           "must compute at least three cases with different starting values, because a "
           "single case can agree with a false rule by coincidence.", "ATL \u00b7 Transfer")
    gap(p, 8)
    p.add(Stage("05", "APPLY"))
    section(p, "Real-life application", "The community market stall", "D \u00b7 i\u2013iv",
            ["Quantity", "Model"])
    body(p, "A trader buys 200 kg of tomatoes at 1.20 per kilogram. Transport costs 45. "
            "About 8 % of the stock spoils before sale. The trader wants a 35 % profit on "
            "total cost and sells the rest in 2 kg bags.")
    h3(p, "Your task")
    lst(p, ["Find the total cost, including transport.",
            "Find the mass of tomatoes that can be sold.",
            "Find the target revenue for a 35 % profit on cost.",
            "Find the selling price per 2 kg bag, to the nearest 0.10.",
            "State one reason the trader might choose a lower price, and calculate the "
            "profit at that price.",
            "Explain how a small error in the spoilage percentage affects the price."],
        ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Identify costs, losses and the target.",
                 "Select percentage increase and unit pricing strategies.",
                 "Apply them accurately across several steps.",
                 "Justify the price and evaluate the sensitivity to the spoilage rate."])
    gap(p, 8)
    p.break_page()
    p.add(Stage("06", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "The fair-price card", "C \u00b7 i\u2013iii  \u00b7  D \u00b7 ii, iii", [])
    body(p, "**Context.** Customers at the stall often misread percentage labels. Produce a "
            "card, no larger than A5, that explains how a discount and a tax combine, using "
            "one worked example and one diagram.")
    lst(p, ["State what a percentage is in one sentence.",
            "Show 80 with a 25 % discount and then 10 % tax, line by line.",
            "Include a diagram showing that the two percentages apply to different bases.",
            "Explain why \u201c20 % then 20 %\u201d is not 40 %.",
            "Add one sentence telling a customer how to check a price quickly.",
            "Test the card on someone outside the class and record one misunderstanding it "
            "did not prevent.",
            "Revise one part of the card and evaluate the revision."],
        ordered=True)
    criteria_panel(p, c="i\u2013iii: precise language, a clear diagram and an identified "
                        "audience.",
                   d="ii, iii: an accurate worked example and a justified check.")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("07", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, ["A percentage is a fraction over 100, so all three notations are interchangeable.",
            "A percentage always has a base, and the base must be named to interpret it.",
            "A percentage of a quantity is found by multiplying by a decimal or a fraction.",
            "Successive percentage changes multiply; they never add.",
            "Financial decisions require the calculation and a judgement about "
            "reasonableness."])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["percentage", "A fraction expressed in hundredths."],
        ["base", "The whole to which a percentage refers."],
        ["multiplier", "The single number by which a quantity is multiplied for a change."],
        ["discount", "A reduction from a marked price."],
        ["tax", "A percentage added to a price by an authority."],
        ["budget", "An allocation of a whole amount into named parts."],
    ], widths=[0.85, 2.3])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that persist",
          text="**0.4 = 0.4 %.** 0.4 is 40 %; percentages are already hundredths.\n"
               "**+20 % then \u221220 % is no change.** The multipliers 1.2 and 0.8 give "
               "0.96.\n**A bigger percentage means a bigger amount.** 40 % of 70 (28) is "
               "less than 35 % of 80 (28 is equal, in fact) \u2014 always compare the "
               "calculated amounts.")
    assessment_close(p, [
        ["convert between fractions, decimals and percentages", "\u25a1", "\u25a1",
        "\u25a1"],
        ["find a percentage of a quantity", "\u25a1", "\u25a1", "\u25a1"],
        ["express one quantity as a percentage of another", "\u25a1", "\u25a1", "\u25a1"],
        ["increase and decrease by a percentage", "\u25a1", "\u25a1", "\u25a1"],
        ["use a multiplier for successive changes", "\u25a1", "\u25a1", "\u25a1"],
        ["judge whether a percentage claim is informative", "\u25a1", "\u25a1", "\u25a1"],
        
    ],
        "In order for a student to read a percentage claim critically, students must "
               "ask what the base is, whether the percentages were added or multiplied, and "
               "what the absolute amounts are.",
        next_title="Chapter 6 · Patterns, expressions and equations")


    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("08", "MIXED PRACTICE"))
    practice(p, "Mixed practice 5",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201311  \u00b7  EXTENSION 9\u201314", [
        q("Write 0.85 as a percentage and 6 % as a decimal.", "F"),
        q("Find 15 % of 320.", "F"),
        q("Increase 180 by 12 %.", "F"),
        q("Decrease 90 by 30 %.", "F"),
        q("Write 18 out of 24 as a percentage.", "F"),
        q("A price of 48 rises by 25 % and then falls by 20 %. Find the final price and "
          "compare it with the original.", "R"),
        q("Explain why a 50 % increase followed by a 50 % decrease is not a return to the "
          "original value.", "R"),
        q("A jacket is reduced from 120 to 102. Find the percentage reduction.", "P"),
        q("A school has 480 students; 45 % are in the lower school. How many are in the "
          "upper school?", "P"),
        q("A meal costs 32 and a 15 % service charge is added. Find the total and the "
          "amount of the charge.", "P"),
        q("A trader's cost is 80 and the selling price is 100. Find the profit as a "
          "percentage of cost and as a percentage of selling price. Explain why the two "
          "differ.", "E"),
        q("Find the original price if 64 is the price after a 20 % discount.", "E"),
        q("Investigate: after what single percentage increase does a 25 % decrease return "
          "the value to its start?", "E"),
        q("A population of 2 500 grows by 4 % a year for two years. Find the population, "
          "and compare with a single 8 % increase.", "E"),
    ])
    gap(p, 8)
    p.add(Stage("09", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20132", "Revisit 5.1 and 5.2: write the percentage as a decimal first."],
        ["3\u20135", "Revisit 5.3: use a multiplier, not two steps."],
        ["6\u20138", "Revisit the investigation: successive changes multiply."],
        ["9\u201311", "Revisit 5.4: name the base before calculating."],
        ["12\u201314", "Revisit 5.3 and work backwards by dividing by the multiplier."],
    ], widths=[0.7, 2.6])


ANSWERS = [
    ("5.1", "1 (a) 60 % (b) 8 % (c) 125 %.  2 (a) 0.45 (b) 0.07 (c) 1.2.  3 (a) 1/4 "
            "(b) 3/5 (c) 1/8.  4 35 %.  6 30 %.  7 35 % of 80 = 28; 40 % of 70 = 28: equal.  "
            "8 66.7 % (not exact)."),
    ("5.2", "1 (a) 9 (b) 21 (c) 3.5.  2 (a) 36 (b) 91 (c) 27.  3 12.  4 65 %.  "
            "6 75 %.  7 345 boys.  8 56.  9 The products are equal but the statements "
            "describe different bases."),
    ("5.3", "1 88.  2 200.  3 (a) 1.35 (b) 0.88 (c) 2.5.  4 1 872.  6 244.80.  "
            "7 60.  8 13.4 %.  9 0.90, a 10 % decrease."),
    ("5.4", "1 51.  2 49.50.  3 540.  4 100.80.  6 621.  7 2 000.  8 Shop A: 140; shop B: "
            "144; shop A is cheaper by 4."),
    ("Investigation 5", "Every starting price gives 36 %: 0.8 \u00d7 0.8 = 0.64. For `p` % "
                        "twice, total discount = 100(1 \u2212 (1 \u2212 p/100)^{2})."),
    ("Mixed 5", "1 85 %; 0.06.  2 48.  3 201.60.  4 63.  5 75 %.  6 48: 48 \u00d7 1.25 "
                "\u00d7 0.8 = 48, unchanged.  8 15 %.  9 264.  10 36.80; 4.80.  "
                "11 25 % of cost; 20 % of selling price.  12 80.  14 2 704, which is more "
                "than 2 700."),
]
