"""Chapter 6 - Patterns, expressions and equations."""
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.flow import Spacer, Pager
import diagrams as dg
from helpers import (section, lead, body, h3, lst, panel, atl, we, practice, q, fig,
                     diag, table, note, gap, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
    part="Part III \u00b7 Algebra as compressed reasoning", part_numeral="III",
    chapter_no=6,
    kicker="Algebra as compressed reasoning",
    title_lines=["Patterns, expressions", "and equations"],
    lead_lines=["A letter is a number you have not chosen yet. An",
                "equation is a question written as a balance. Algebra",
                "is not a new arithmetic; it is arithmetic that keeps",
                "its options open."],
    key_concept="Relationships", related=["Pattern", "Generalisation"],
    context="Personal and cultural expression",
    inquiry_lines=["How does a pattern become a rule, and how does a rule let us",
                   "answer a question without doing every step by hand?"])

TITLE = "Patterns, expressions and equations"
SHORT = "Patterns and equations"


def build(bk, p):
    reset_counters(6)
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER"))
    p.add(Spacer(8))
    p.add(DataTable(["Statement of inquiry",
                     "A pattern becomes mathematics when it is described by a general "
                     "rule, and a rule becomes useful when it can be rearranged to answer "
                     "a question about a value that is not yet known."],
                    [], widths=[1, 3.2], font_size=9.2, stripe=False))
    gap(p, 10)
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Relationships.** An expression records how one "
                     "quantity depends on another, which is why substituting a value "
                     "produces a predictable result.\n"
                     "**Related \u00b7 Pattern.** A linear pattern changes by a constant "
                     "difference, and that constant is the coefficient in the rule.\n"
                     "**Related \u00b7 Generalisation.** A rule stated with a letter holds "
                     "for every case, not only the cases examined."))
    p.add(Panel("note", title="Global context \u00b7 Personal and cultural expression",
                text="Exploration: how weaving, tiling and ornament use repeating structures, "
                     "and how the same structure can be described in words, in a table, in "
                     "a graph and in a rule."))
    gap(p, 8)
    h3(p, "Inquiry questions")
    lst(p, ["**Factual:** How do you find the next term of a sequence, and how do you "
            "substitute into an expression?",
            "**Conceptual:** Why does solving an equation preserve the equality when you "
            "do the same thing to both sides?",
            "**Debatable:** Is a rule more useful in words, in a table, in a graph or in "
            "symbols?"])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Substitute, simplify, expand and solve one- and two-step equations."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate the matchstick chain and generalise the rule."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Explain a pattern in words, symbols and a table consistently."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Model a courtyard paving project and judge the model."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 6)
    atl(p, "In order for a student to generalise a pattern, students must first record "
           "several cases in a table, then describe in words what changes by a constant "
           "amount, and only then introduce a letter.", "ATL \u00b7 Transfer")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("02", "ENGAGE", "The loom."))
    body(p, "A narrow-strip weaver repeats one motif along a long band. Each repeat adds "
            "the same length of cloth. If she knows the length of one motif and the length "
            "of the starting border, she can predict the length of a band with any number "
            "of motifs without measuring it \u2014 provided she has found the rule.")
    fig(p, "ch06_plate_banner.jpg",
        "A repeating motif is a linear pattern: the length grows by a constant amount per "
        "repeat. Algebra is the shortest way to write that sentence.", wide=True)
    p.add(Stage("03", "EXPLORE", "Find the rule from the table."))
    body(p, "A band has a border of 6 cm, then motifs of 9 cm each. Complete the table, then "
            "describe how the length grows.")
    table(p, ["Motifs", "1", "2", "3", "4", "10", "`n`"],
          [["Length (cm)", "15", "24", "33", "\u2026", "\u2026", "\u2026"]],
          widths=[0.8, 0.45, 0.45, 0.45, 0.45, 0.45, 0.5])
    lst(p, ["By how much does the length grow for each extra motif?",
            "What would the length be with 0 motifs, and what does that number mean?",
            "Write the rule in words.",
            "Write the rule with a letter `n` for the number of motifs.",
            "Use the rule to find the length for 25 motifs."], ordered=True)
    panel(p, "keyidea", title="The structure you found",
          text="Length = 9`n` + 6. The 9 is the amount added per motif; the 6 is what is "
               "there before any motif is added. Every linear pattern has those two parts: "
               "a constant difference and a starting value.")

    # --------------------------------------------------------------- 6.1
    section(p, "6.1", "Patterns and rules", "B \u00b7 i, ii  \u00b7  A \u00b7 i",
            ["Pattern", "Generalisation"])
    body(p, "A sequence is an ordered list of numbers. If consecutive terms differ by the "
            "same amount, the sequence is linear, and the rule has the form term = "
            "difference \u00d7 position + starting value.")
    diag(p, 96, dg.linear_sequence, "A linear sequence as steps of equal height: each step "
                                    "adds the same difference.", wide=True)
    panel(p, "definition", title="nth term",
          text="The **nth term** of a linear sequence is an expression in `n` that gives the "
               "value at position `n`. If the first term is `a` and the common difference is "
               "`d`, then the nth term is `a` + (`n` \u2212 1)`d`.")
    we(p, "6.1.1", "Finding the nth term",
       "Find the nth term of the sequence 5, 8, 11, 14, \u2026",
       ["The difference between consecutive terms is 3, so the rule contains 3`n`.",
        "Compare 3`n` with the terms: for `n` = 1, 3`n` = 3, but the term is 5.",
        "The rule must add 2: 3`n` + 2.",
        "Check with `n` = 3: 3 \u00d7 3 + 2 = 11, which matches the third term."],
       answer="nth term = 3`n` + 2",
       check="`n` = 4 gives 14 \u2713 and `n` = 1 gives 5 \u2713")
    we(p, "6.1.2", "Using the rule to answer a question",
       "A sequence has nth term 4`n` \u2212 1. Which position in the sequence holds 39?",
       ["Set the rule equal to the value: 4`n` \u2212 1 = 39.",
        "Add 1 to both sides: 4`n` = 40.",
        "Divide both sides by 4: `n` = 10.",
        "So 39 is the 10th term."],
       answer="The 10th term.",
       check="4 \u00d7 10 \u2212 1 = 39 \u2713")
    practice(p, "6.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Write the next three terms: (a) 3, 7, 11, \u2026 (b) 20, 17, 14, \u2026", "F"),
        q("Find the nth term: (a) 2, 5, 8, \u2026 (b) 10, 14, 18, \u2026", "F"),
        q("Find the nth term of 1, 6, 11, 16, \u2026", "F"),
        q("A sequence has nth term 5`n` + 3. Find the 10th term.", "F"),
        q("Explain how you can tell from a table whether a sequence is linear.", "R"),
        q("A tiling pattern uses 12 tiles for the first row and 5 more for each row after. "
          "Write a rule for the number of tiles in row `n`.", "P"),
        q("Which term of the sequence 7, 12, 17, \u2026 is 62?", "P"),
        q("Find a sequence whose nth term is 2`n` + 1 and another whose nth term is 3`n` "
          "\u2212 2. Write the first four terms of each and compare.", "E"),
        q("Explain why the nth term of an increasing linear sequence must contain `n` with "
          "a positive coefficient.", "E"),
    ])

    # --------------------------------------------------------------- 6.2
    section(p, "6.2", "Expressions and substitution", "A \u00b7 i, ii", ["Form"])
    panel(p, "definition", title="Expression, term, coefficient",
          text="An **expression** combines numbers, letters and operations without an equals "
               "sign: 3`x` + 5. A **term** is one part of it separated by + or \u2212. A "
               "**coefficient** is the number multiplying a letter: in 3`x`, the "
               "coefficient is 3.")
    body(p, "Substituting a value into an expression is a test of whether you can read its "
            "structure. In 3`x` + 5, the multiplication happens before the addition, so "
            "`x` = 2 gives 11, not 16.")
    we(p, "6.2.1", "Substituting into expressions",
       "Evaluate 4`a` \u2212 2`b` when `a` = 3 and `b` = 5.",
       ["Replace each letter: 4 \u00d7 3 \u2212 2 \u00d7 5.",
        "Multiply first: 12 \u2212 10.",
        "Subtract: 2."],
       answer="2",
       check="Pick easier numbers: `a` = 1, `b` = 1 gives 4 \u2212 2 = 2, the same value "
             "coincidentally; test `a` = 2, `b` = 1 to confirm the method gives 6 \u2713")
    we(p, "6.2.2", "Writing an expression from a situation",
       "A taxi charges a fixed 3 plus 2 per kilometre. Write an expression for the cost of "
       "`k` kilometres and find the cost of a 7 km journey.",
       ["The fixed charge does not change with distance: 3.",
        "The distance charge is 2 per kilometre: 2`k`.",
        "Expression: 2`k` + 3.",
        "For `k` = 7: 2 \u00d7 7 + 3 = 17."],
       answer="2`k` + 3; a 7 km journey costs 17.",
       check="A 1 km journey should cost 5; 2(1) + 3 = 5 \u2713")
    practice(p, "6.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Evaluate 2`x` + 7 when `x` = 4.", "F"),
        q("Evaluate 5`y` \u2212 3 when `y` = 2.", "F"),
        q("Evaluate 3`a` + 2`b` when `a` = 2 and `b` = 5.", "F"),
        q("Write an expression for: (a) 5 more than `n` (b) 3 times `m` (c) 8 less than "
          "twice `p`.", "F"),
        q("Explain why 3`x` + 2 with `x` = 4 is 14 and not 18.", "R"),
        q("A phone plan costs 12 a month plus 0.05 per minute. Write an expression for the "
          "monthly cost of `m` minutes.", "P"),
        q("A rectangle has length `x` + 3 and width `x`. Write an expression for its "
          "perimeter.", "P"),
        q("Find a value of `n` for which 4`n` and `n`^{2} are equal, other than `n` = 0.",
          "E"),
    ])

    # --------------------------------------------------------------- 6.3
    section(p, "6.3", "Simplifying and expanding", "A \u00b7 ii", ["Simplification"])
    body(p, "Like terms contain the same letter with the same power, so they can be "
            "combined: 3`x` + 5`x` = 8`x` because three lots of `x` plus five lots of `x` "
            "is eight lots of `x`. Unlike terms such as 3`x` and 3`x`^{2} cannot be "
            "combined, because they count different things.")
    panel(p, "keyidea", title="Expanding a bracket",
          text="A bracket is a multiplication: 3(`x` + 4) means three copies of (`x` + 4). "
               "Multiplying each term inside by the number outside gives 3`x` + 12. This is "
               "the distributive law, and it is the reverse of factorising.")
    we(p, "6.3.1", "Collecting like terms",
       "Simplify 7`a` + 3`b` \u2212 2`a` + 5`b`.",
       ["Collect the `a` terms: 7`a` \u2212 2`a` = 5`a`.",
        "Collect the `b` terms: 3`b` + 5`b` = 8`b`.",
        "The simplified expression is 5`a` + 8`b`; the two terms are unlike, so they stay "
        "separate."],
       answer="5`a` + 8`b`",
       check="Substitute `a` = 1, `b` = 1: original gives 7 + 3 \u2212 2 + 5 = 13; "
             "simplified gives 5 + 8 = 13 \u2713")
    we(p, "6.3.2", "Expanding and simplifying",
       "Expand and simplify 4(`x` + 3) + 2(`x` \u2212 1).",
       ["Expand each bracket: 4`x` + 12 and 2`x` \u2212 2.",
        "Add the results: 4`x` + 12 + 2`x` \u2212 2.",
        "Collect like terms: 6`x` + 10."],
       answer="6`x` + 10",
       check="`x` = 2: original 4(5) + 2(1) = 22; simplified 12 + 10 = 22 \u2713")
    panel(p, "error", title="3`x` + 4 = 7`x`",
          text="Adding unlike terms is not allowed. 3`x` + 4 stays as it is; only if the "
               "second number also multiplies `x` can the two be combined. Substitute a "
               "value to see the difference: with `x` = 10, 3`x` + 4 = 34, not 70.")
    practice(p, "6.3", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Simplify: (a) 4`x` + 3`x` (b) 9`y` \u2212 2`y` (c) 6`a` + `a`.", "F"),
        q("Simplify: (a) 3`x` + 2 + 5`x` (b) 8`m` \u2212 3 \u2212 2`m`.", "F"),
        q("Expand: (a) 3(`x` + 2) (b) 5(2`y` \u2212 1).", "F"),
        q("Expand and simplify 2(`x` + 4) + 3(`x` + 1).", "F"),
        q("Explain why 2`x` + 3`x` can be simplified but 2`x` + 3`x`^{2} cannot.", "R"),
        q("A rectangle has sides `x` + 2 and 3. Write and simplify an expression for its "
          "perimeter.", "P"),
        q("A student writes 5(`x` + 2) = 5`x` + 2. Diagnose the error and correct it.", "R"),
        q("Find two expressions that simplify to 4`x` + 6, one of which uses a bracket.",
          "E"),
    ])

    # --------------------------------------------------------------- 6.4
    section(p, "6.4", "Equations and formulas", "A \u00b7 iii  \u00b7  C \u00b7 ii",
            ["Relationships", "Model"])
    panel(p, "definition", title="Equation and solution",
          text="An **equation** states that two expressions are equal: 3`x` + 2 = 11. A "
               "**solution** is the value of the letter that makes the statement true. "
               "Solving means finding that value, not guessing it.")
    diag(p, 92, dg.balance_scale, "An equation is a balance. Whatever is done to one side "
                                  "must be done to the other, or the equality is destroyed.",
         wide=True)
    h3(p, "The method")
    lst(p, ["Undo addition or subtraction first, using the inverse operation on both sides.",
            "Undo multiplication or division second.",
            "Check by substituting the solution back into the original equation.",
            "Keep the equals signs aligned so that each line states a true equality."])
    we(p, "6.4.1", "A two-step equation",
       "Solve 4`x` + 7 = 31.",
       ["Subtract 7 from both sides: 4`x` = 24.",
        "Divide both sides by 4: `x` = 6.",
        "Check: 4 \u00d7 6 + 7 = 24 + 7 = 31."],
       answer="`x` = 6",
       check="Substitution returns the original right-hand side \u2713")
    we(p, "6.4.2", "An equation with a bracket",
       "Solve 3(`x` \u2212 2) = 18.",
       ["Divide both sides by 3: `x` \u2212 2 = 6.",
        "Add 2 to both sides: `x` = 8.",
        "Alternatively expand first: 3`x` \u2212 6 = 18, so 3`x` = 24 and `x` = 8."],
       answer="`x` = 8",
       check="3(8 \u2212 2) = 18 \u2713")
    we(p, "6.4.3", "Rearranging a formula",
       "The perimeter of a rectangle is `P` = 2(`l` + `w`). Find `l` when `P` = 26 and "
       "`w` = 4.",
       ["Substitute: 26 = 2(`l` + 4).",
        "Divide by 2: 13 = `l` + 4.",
        "Subtract 4: `l` = 9."],
       answer="`l` = 9",
       check="2(9 + 4) = 26 \u2713")
    panel(p, "error", title="Doing an operation to one side only",
          text="From 4`x` + 7 = 31, subtracting 7 from the left alone gives 4`x` = 31, which "
               "is false. The balance metaphor is precise: an equation is a statement of "
               "equality, and equality survives only if both sides change together.")
    practice(p, "6.4", "SUPPORT 1\u20134  \u00b7  CORE 3\u20138  \u00b7  EXTENSION 7\u20139", [
        q("Solve: (a) `x` + 5 = 12 (b) `x` \u2212 3 = 9 (c) 2`x` = 14.", "F"),
        q("Solve: (a) 3`x` + 1 = 16 (b) 5`x` \u2212 4 = 21.", "F"),
        q("Solve 2`x` + 9 = 3.", "F"),
        q("Solve 4(`x` + 1) = 20.", "F"),
        q("Explain why you subtract before dividing in 3`x` + 5 = 20.", "R"),
        q("A taxi charges 3 plus 2 per kilometre. A journey costs 23. How far was it?", "P"),
        q("The perimeter of a square is 44 cm. Write an equation and solve it to find the "
          "side length.", "P"),
        q("Solve 3`x` + 2 = `x` + 10, explaining each step.", "E"),
        q("Write an equation with solution `x` = 5 that contains a bracket and a constant.",
          "E"),
        q("Solve `x`/4 = 7.", "F"),
        q("Solve 5 \u2212 `x` = 2.", "F"),
        q("Explain what happens to the balance when you multiply both sides by 3.", "R"),
        q("A rectangle has length `x` + 4 and width 3. Its perimeter is 30. Write and solve "
          "an equation.", "P"),
    ])

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("04", "INVESTIGATE"))
    section(p, "Investigation 6", "The matchstick chain", None, ["Pattern", "Generalisation"])
    body(p, "Squares are made from matchsticks in a chain, sharing one side each time. "
            "Build the first four shapes or draw them, then count the matchsticks carefully "
            "\u2014 the shared side is the whole difficulty.")
    diag(p, 88, dg.matchstick_chain, "Three squares in a chain use 10 matchsticks, not 12, "
                                     "because each new square shares one side.", wide=True)
    table(p, ["Squares", "1", "2", "3", "4", "5", "`n`"],
          [["Matchsticks", "4", "7", "10", "\u2026", "\u2026", "\u2026"]],
          widths=[0.85, 0.42, 0.42, 0.42, 0.42, 0.42, 0.45])
    h3(p, "Your investigation")
    lst(p, ["Count the matchsticks for 1, 2, 3 and 4 squares.",
            "Explain in words why the count does not grow by 4 each time.",
            "Find the constant difference and write the rule.",
            "Predict the number of matchsticks for 20 squares and check by calculation.",
            "How many squares can be made with 100 matchsticks? Write the equation you "
            "solved.",
            "Now build a different chain: an L-shape, or a row of triangles. Find its rule "
            "and compare the constant differences."], ordered=True)
    panel(p, "keyidea", title="Why the rule has that shape",
          text="The first square needs 3 matchsticks plus the closing side: 4. Each extra "
               "square adds 3. So matchsticks = 3`n` + 1. The constant 3 is the number of "
               "new matchsticks per square; the +1 is the side that closes the first "
               "square.")
    atl(p, "In order for a student to trust a general rule, students must test it against "
           "the smallest case, where the count can be verified by hand.", "ATL \u00b7 Critical thinking")
    gap(p, 8)
    p.add(Stage("05", "APPLY"))
    section(p, "Real-life application", "The courtyard pond", "D \u00b7 i\u2013iv",
            ["Relationships", "Model"])
    body(p, "A courtyard is to be paved around a rectangular pond. The pond is 3 m by 2 m, "
            "and the paved border is `x` metres wide on every side. The builder needs the "
            "paved area to quote for tiles.")
    h3(p, "Your task")
    lst(p, ["Draw the courtyard for `x` = 1 and label every dimension.",
            "Write the overall length and width in terms of `x`.",
            "Write an expression for the total area and a second expression for the pond "
            "area.",
            "Hence write an expression for the paved area, simplified.",
            "Find the paved area when `x` = 1.5 m.",
            "Explain one limitation of the model for very large `x`."], ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Identify the variables and the fixed quantities.",
                 "Select algebraic modelling as the strategy.",
                 "Apply expansion correctly to obtain the paved area.",
                 "Evaluate the model's limits in the real context."])
    gap(p, 8)
    p.break_page()
    p.add(Stage("06", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "The pattern explainer", "B \u00b7 i, ii  \u00b7  C \u00b7 i, ii", [])
    body(p, "**Context.** Your class is producing a display of patterns for a parents' "
            "evening. Each student explains one pattern so that a visitor can predict the "
            "next term and the hundredth term without counting.")
    lst(p, ["Choose a pattern that grows by a constant difference and draw its first four "
            "terms.",
            "Present the pattern in three forms: a drawing, a table and a rule.",
            "Explain the meaning of each number in your rule in words.",
            "Predict the 100th term and show the substitution.",
            "Ask a visitor or classmate to use your display to find the 50th term. Record "
            "the result.",
            "Evaluate your display: what made the rule easy to see, and what obscured it?"],
        ordered=True)
    criteria_panel(p, b="i, ii: correct generalisation from the cases examined.",
                   c="i, ii: consistent presentation across three representations.")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("07", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, ["A linear pattern has a constant difference, which appears as the coefficient.",
            "The nth term lets you answer questions about any position without listing.",
            "Substituting into an expression tests whether you can read its structure.",
            "Like terms can be combined; unlike terms cannot.",
            "Solving an equation means keeping a balance true at every step."])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["sequence", "An ordered list of numbers."],
        ["nth term", "An expression giving the value at position `n`."],
        ["expression", "A combination of numbers, letters and operations."],
        ["term", "One part of an expression separated by + or \u2212."],
        ["coefficient", "The number multiplying a letter."],
        ["expand", "Multiply out a bracket."],
        ["equation", "A statement that two expressions are equal."],
        ["solution", "The value that makes an equation true."],
    ], widths=[0.85, 2.3])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that persist",
          text="**3`x` + 4 = 7`x`.** 4 is not a number of `x`.\n**5(`x` + 2) = 5`x` + 2.** "
               "The 5 multiplies both terms.\n**Moving a term without changing its sign.** "
               "Subtract from both sides rather than \u201cmoving\u201d.")
    assessment_close(p, [
        ["find the next terms of a sequence", "\u25a1", "\u25a1", "\u25a1"],
        ["find and use the nth term", "\u25a1", "\u25a1", "\u25a1"],
        ["substitute into an expression", "\u25a1", "\u25a1", "\u25a1"],
        ["simplify and expand", "\u25a1", "\u25a1", "\u25a1"],
        ["solve one- and two-step equations", "\u25a1", "\u25a1", "\u25a1"],
        ["form an equation from a situation", "\u25a1", "\u25a1", "\u25a1"],
        
    ],
        "In order for a student to check an algebraic simplification, students must "
               "substitute one convenient value into both the original and the simplified "
               "expression and confirm the results agree.",
        next_title="Chapter 7 · Lines, angles, triangles and constructions")


    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("08", "MIXED PRACTICE"))
    practice(p, "Mixed practice 6",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201312  \u00b7  EXTENSION 10\u201315", [
        q("Write the next two terms: 6, 11, 16, \u2026", "F"),
        q("Find the nth term of 4, 7, 10, \u2026", "F"),
        q("Evaluate 3`x` \u2212 4 when `x` = 5.", "F"),
        q("Simplify 5`a` + 2`b` \u2212 `a` + 3`b`.", "F"),
        q("Solve 2`x` + 7 = 19.", "F"),
        q("Expand 4(2`x` \u2212 3).", "F"),
        q("Solve 3(`x` \u2212 4) = 15.", "F"),
        q("Explain why 6`x` and 6`x`^{2} cannot be added.", "R"),
        q("A plumber charges 25 call-out plus 18 per hour. Write an expression for `h` hours "
          "and find the charge for 3 hours.", "P"),
        q("Which term of 9, 13, 17, \u2026 is 97?", "P"),
        q("Solve 5`x` \u2212 2 = 2`x` + 13.", "E"),
        q("The sum of three consecutive numbers is 72. Form an equation and solve it.", "E"),
        q("A rectangle has length `x` + 4 and width `x` \u2212 1. Write and simplify an "
          "expression for its perimeter, then find the perimeter when `x` = 6.", "P"),
        q("Explain how the constant difference of a sequence appears in its graph.", "R"),
        q("Write two different expressions that both give the perimeter of a rectangle of "
          "length `l` and width `w`.", "E"),
    ])
    gap(p, 8)
    p.add(Stage("09", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20132", "Revisit 6.1: find the difference, then adjust the constant."],
        ["3\u20135", "Revisit 6.2 and 6.3: multiplication before addition."],
        ["6\u20137", "Revisit 6.4: undo the addition, then the multiplication."],
        ["8\u201310", "Revisit 6.3 and the taxi example in 6.2."],
        ["11\u201315", "Revisit the investigation: build the pattern in a table first."],
    ], widths=[0.7, 2.6])


ANSWERS = [
    ("6.1", "1 (a) 15, 19, 23 (b) 11, 8, 5.  2 (a) 3`n` \u2212 1 (b) 4`n` + 6.  "
            "3 5`n` \u2212 4.  4 53.  6 5`n` + 7.  7 The 12th term."),
    ("6.2", "1 15.  2 7.  3 16.  4 (a) `n` + 5 (b) 3`m` (c) 2`p` \u2212 8.  6 12 + 0.05`m`.  "
            "7 4`x` + 6.  8 `n` = 4."),
    ("6.3", "1 (a) 7`x` (b) 7`y` (c) 7`a`.  2 (a) 8`x` + 2 (b) 6`m` \u2212 3.  "
            "3 (a) 3`x` + 6 (b) 10`y` \u2212 5.  4 5`x` + 11.  6 2`x` + 10.  8 e.g. "
            "2(2`x` + 3) and 4`x` + 2 + 4."),
    ("6.4", "1 (a) 7 (b) 12 (c) 7.  2 (a) 5 (b) 5.  3 \u22123.  4 4.  6 10 km.  7 4`s` = "
            "44, `s` = 11 cm.  8 `x` = 4.  9 e.g. 2(`x` + 1) + 4 = 16."),
    ("Investigation 6", "1, 2, 3, 4 squares use 4, 7, 10, 13 matchsticks. Rule 3`n` + 1. "
                        "20 squares: 61. 100 matchsticks: 3`n` + 1 = 100 gives `n` = 33."),
    ("Mixed 6", "1 21, 26.  2 3`n` + 1.  3 11.  4 4`a` + 5`b`.  5 6.  6 8`x` \u2212 12.  "
                "7 9.  9 25 + 18`h`; 79.  10 The 23rd term.  11 `x` = 5.  12 The numbers "
                "are 23, 24, 25.  13 4`x` + 6; 30."),
]
