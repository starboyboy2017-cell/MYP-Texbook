"""Chapter 5 - Algebraic expressions and equations (Algebra and pattern)."""
from chbase import *

PLATE = dict(
    part="Part II \u00b7 Algebra and pattern", part_numeral="II", chapter_no=5,
    kicker="Algebra and pattern", motif="algebra",
    title_lines=["Algebraic expressions", "and equations"],
    lead_lines=["A letter is a number you have not chosen yet. An expression",
                "describes what would happen to it; an equation is a",
                "question written as a balance, and solving it is a search",
                "for the one number that keeps the balance level."],
    key_concept="Relationships", related=["Equivalence", "Simplification"],
    context="Identities and relationships",
    inquiry_lines=["How can a letter stand for something unknown without",
                   "losing precision?"])

TITLE = "Algebraic expressions and equations"
SHORT = "Algebraic expressions and equations"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "Notation, equivalence and the balance method: the grammar of algebra."),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "Algebraic notation compresses a relationship into symbols, and the "
              "balance of an equation makes the unknown recoverable by inverse "
              "operations."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Relationships.** An expression describes how an output "
        "depends on an input; an equation states that two such descriptions are "
        "equal.\n"
        "**Related \u00b7 Equivalence.** Two expressions are equivalent when they "
        "give the same value for every substitution, which is why simplifying is "
        "allowed.\n"
        "**Related \u00b7 Simplification.** Collecting like terms and expanding "
        "brackets change the form of an expression without changing its values."),
    BOX("note", "Global context \u00b7 Identities and relationships",
        "Exploration: how a formula relates quantities that vary independently, and "
        "how an unknown quantity can be described precisely before it is found. Every "
        "spreadsheet, price list and plan uses this idea."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** What is the difference between a term, an expression and an "
        "equation?",
        "**Conceptual:** Why can an expression be simplified without changing its "
        "value?",
        "**Debatable:** Is algebra a language for describing, or a machine for "
        "solving?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Use notation; substitute; simplify; solve linear equations."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate number tricks and prove why they always give the same "
         "result."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Write and read algebraic notation; explain each solving step."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv, v",
         "Choose between two pricing plans, with an equation as the evidence."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to justify a solving step, students must name the "
        "inverse operation used and show that the same operation was applied to both "
        "sides."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Use algebraic notation correctly.",
         "Write \u201cfive more than three times a number\u201d as 3`n` + 5 and say "
         "what each part means."],
        ["Substitute values into expressions, including negative values.",
         "Evaluate 4`x` \u2212 3 when `x` = \u22122 without a sign error."],
        ["Simplify expressions by collecting like terms and multiplying out "
         "brackets.",
         "Simplify 5`a` + 3 \u2212 2`a` + 7 and 3(2`x` \u2212 4)."],
        ["Solve one- and two-step linear equations.",
         "Solve 4`x` \u2212 7 = 21 and check the answer by substitution."],
        ["Solve equations with brackets and with the unknown on both sides.",
         "Solve 3(`x` + 2) = 5`x` \u2212 4 and explain each step."],
        ["Form an equation from a real situation and interpret the solution.",
         "Write and solve an equation for two pricing plans, and say what the "
         "solution means."],
    ], widths=[1.6, 1.8]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Calculate \u00a0 7 \u00d7 8 \u2212 9.",
               "Calculate \u00a0 \u22123 + 11.",
               "Evaluate \u00a0 2`n` + 1 \u00a0 when `n` = 4.",
               "Simplify \u00a0 3 + 3 + 3 + 3.",
               "Solve \u00a0 `x` + 7 = 12.",
               "Simplify \u00a0 2 \u00d7 5`a`."]),
    P("If three or more answers are wrong, revisit signed arithmetic in chapter 4 "
      "before continuing."),

    # ------------------------------------------------------------------ 5.1
    S("5.1", "The language of algebra", "A \u00b7 I  \u00b7  C \u00b7 I",
      ["Relationships", "Notation"]),
    L("Algebra is compressed reasoning. A letter stands for a number, and everything "
      "written around it is a statement about what would happen to that number."),
    ST("03", "ENGAGE",
       "The number trick that always ends in three."),
    P("Think of a number. Add 5. Double it. Subtract 4. Halve it. Subtract your "
      "original number. Your answer is 3 \u2014 every time, for every starting number. "
      "Before reading on, try it with three different starting numbers, including a "
      "negative one, and write down what you notice."),
    PHOTO("ch05_notebook.jpg", 1.5,
          "Working with symbols. The point of notation is not brevity for its own "
          "sake: it is that every step can be checked without re-reading the words.",
          "Photograph: Pexels, free licence (see the image register)."),
    ST("04", "EXPLORE",
       "Track the same number through the machine."),
    P("Let the starting number be `n`, and record the expression after each step."),
    TABLE(["Step", "Instruction", "What you have"],
          [["1", "Think of a number", "`n`"],
           ["2", "Add 5", "`n` + 5"],
           ["3", "Double it", "2(`n` + 5) = 2`n` + 10"],
           ["4", "Subtract 4", "2`n` + 6"],
           ["5", "Halve it", "`n` + 3"],
           ["6", "Subtract your number", "3"]],
          widths=[0.5, 1.6, 1.6]),
    OL(["Why does the final answer not contain `n`?",
        "Try the same trick with the final instruction changed to \u201csubtract "
        "twice your number\u201d. What is the result now, and why?",
        "Test your prediction with `n` = 4 and `n` = \u22123.",
        "Invent a trick of your own that always ends in 5, and write the expression "
        "at each step.",
        "Write a conjecture: what makes a number trick end in a constant?",
        "Exchange tricks with a partner and prove each other's."]),
    ST("05", "EXPLAIN"),
    DEF("A `variable` is a letter standing for a number that may change. A `term` is "
        "a single number, letter or product of them; an `expression` combines terms "
        "with operations and has no equals sign; an `equation` states that two "
        "expressions are equal. `Like terms` have exactly the same letters with the "
        "same indices."),
    P("Notation is conventional and worth learning exactly: 3`n` means 3 \u00d7 `n`; "
      "`n`/5 means `n` \u00f7 5; `n`\u00b2 means `n` \u00d7 `n`. Writing 3`n` and "
      "never 3 \u00d7 `n` is not laziness \u2014 it keeps the coefficient visually "
      "separate from the variable, which makes collecting terms possible."),
    DIAG(120, "algebra_tiles",
         "Algebra tiles for 3`x` + 4 \u2212 2`x`. Like tiles cancel in pairs, which "
         "is what collecting terms does symbolically."),
    H("Substitution"),
    P("Substituting means replacing each letter with a number, in brackets if the "
      "number is negative, and then evaluating by the order of operations."),
    WE("5.1.1", "Substitute a negative value",
       "Evaluate 4`x` \u2212 3 when `x` = \u22122, and when `x` = 1.5.",
       ["Write the substitution with brackets: 4(\u22122) \u2212 3.",
        "Multiply first: \u22128 \u2212 3 = \u221211.",
        "For `x` = 1.5: 4(1.5) \u2212 3 = 6 \u2212 3 = 3.",
        "Check the second by another route: 4 \u00d7 1.5 = 6, and 6 \u2212 3 = 3."],
       "\u221211 and 3",
       "The brackets are not optional: 4 \u00d7 \u22122 \u2212 3 invites a sign "
       "error, while 4(\u22122) \u2212 3 does not."),
    WE("5.1.2", "Write an expression",
       "A taxi charges \u00a34 plus \u00a32 per kilometre. Write an expression for the "
       "cost of `k` kilometres, and find the cost of 7 km.",
       ["The distance part costs 2`k` pounds.",
        "The fixed charge is added: 2`k` + 4.",
        "For `k` = 7: 2(7) + 4 = 18.",
        "The cost is \u00a318."],
       "2`k` + 4; \u00a318 for 7 km",
       "Check a simple case: 1 km should cost \u00a32 + \u00a34 = \u00a36, and "
       "2(1) + 4 = 6."),
    WE("5.1.3", "Interpret an expression",
       "An expression for the total cost of a school trip is 12`n` + 45. Explain what "
       "each part means and find the cost when `n` = 30.",
       ["12`n` is a cost per student, so 12 is the cost in pounds for each of `n` "
        "students.",
        "45 is a fixed cost that does not depend on the number of students: a "
        "minibus hire, for example.",
        "For `n` = 30: 12(30) + 45 = 360 + 45 = 405.",
        "The total cost is \u00a3405."],
       "\u00a312 per student plus a fixed \u00a345; \u00a3405 for 30 students",
       "If `n` = 0 the cost is \u00a345, confirming the fixed part."),
    ERR("\u201c3`n` means 3 followed by `n`, that is, 3`n` = 30 when `n` = 0.\u201d "
        "Juxtaposition means multiplication: 3`n` = 3 \u00d7 `n`, which is 0 when "
        "`n` = 0. The coefficient is a multiplier, never a digit."),
    PRAC("5.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Write using algebra: (a) 7 more than a number `n`  (b) three times a "
          "number `m`  (c) a number `t` divided by 4.", "F"),
        Q("Evaluate 5`x` + 2 when (a) `x` = 3  (b) `x` = \u22124  (c) `x` = 0.", "F"),
        Q("Evaluate 3`y`\u00b2 when (a) `y` = 2  (b) `y` = \u22123.", "F"),
        Q("Identify the terms and the like terms in 4`a` + 3`b` \u2212 2`a` + 5.", "F"),
        Q("Simplify: (a) 6`m` + 2`m`  (b) 5`p` \u2212 8`p`  (c) 3 + 4`x` + 5.", "F"),
        Q("A phone contract costs \u00a38 plus \u00a30.15 per minute. Write an "
          "expression for `m` minutes and find the cost of 40 minutes.", "P"),
        Q("A rectangle has length `x` + 3 and width `x`. Write an expression for its "
          "perimeter.", "P"),
        Q("Explain why 2`n` + 3 and 3 + 2`n` are always equal, using one numerical "
          "example and one sentence about the operations.", "R"),
        Q("The expression 5`n` + 20 gives the total cost in pounds of `n` tickets "
          "plus a booking fee. Find the cost of 6 tickets and describe the booking "
          "fee.", "P"),
        Q("A student says \u201c4`x` means 40 when `x` = 10, because 4 and the 0 "
          "make 40\u201d. Explain the error.", "E"),
        Q("Write an expression for the sum of three consecutive integers, the "
          "smallest being `n`. Simplify it.", "E"),
        Q("The cost of hiring a hall is \u00a360 plus \u00a35 per person. Write an "
          "expression for `p` people and find the number of people when the cost is "
          "\u00a3210.", "E"),
    ]),

    # ------------------------------------------------------------------ 5.2
    S("5.2", "Equivalent expressions", "A \u00b7 II  \u00b7  C \u00b7 II",
      ["Equivalence", "Simplification"]),
    L("Two expressions are equivalent when they give the same value for every value of "
      "the variable. Simplifying is the art of finding a shorter form that keeps every "
      "value."),
    DEF("Expressions are `equivalent` when substituting any number for the variable "
        "gives the same result in both. Collecting like terms and expanding brackets "
        "both produce equivalent expressions, because they follow from the "
        "distributive and commutative laws."),
    H("Two operations that preserve value"),
    UL(["**Collecting like terms.** 5`a` + 3`b` \u2212 2`a` simplifies to 3`a` + "
        "3`b`: the `a`-terms are combined and the `b`-term is untouched.",
        "**Expanding brackets.** 3(2`x` \u2212 4) becomes 6`x` \u2212 12: every term "
        "inside is multiplied by the factor outside."]),
    H("Testing equivalence"),
    P("To show two expressions are equivalent, simplify both and compare, or substitute "
      "two different values and check both give the same result. To show they are not, "
      "one counterexample is enough \u2014 and it is also complete."),
    WE("5.2.1", "Simplify by collecting",
       "Simplify 7`x` + 4 \u2212 3`x` + 9 \u2212 `x`.",
       ["Collect the `x`-terms: 7`x` \u2212 3`x` \u2212 `x` = 3`x`.",
        "Collect the numbers: 4 + 9 = 13.",
        "The simplified expression is 3`x` + 13.",
        "Check with `x` = 2: original 14 + 4 \u2212 6 + 9 \u2212 2 = 19; simplified "
        "3(2) + 13 = 19."],
       "3`x` + 13",
       "A single substitution catches most collecting errors, which is why it is worth "
       "doing."),
    WE("5.2.2", "Expand and simplify",
       "Simplify 4(2`x` + 3) \u2212 2(`x` \u2212 5).",
       ["Expand the first bracket: 4(2`x` + 3) = 8`x` + 12.",
        "Expand the second, keeping the minus sign with every term: \u22122(`x` "
        "\u2212 5) = \u22122`x` + 10.",
        "Collect: 8`x` \u2212 2`x` + 12 + 10 = 6`x` + 22.",
        "Check with `x` = 1: original 4(5) \u2212 2(\u22124) = 20 + 8 = 28; "
        "simplified 6 + 22 = 28."],
       "6`x` + 22",
       "The common error is writing \u22122(`x` \u2212 5) = \u22122`x` \u2212 10. "
       "Both terms inside change sign."),
    WE("5.2.3", "Are they equivalent?",
       "Are 3(`x` + 2) and 3`x` + 2 equivalent? Are 2(`x` + 3) and 2`x` + 6?",
       ["Expand 3(`x` + 2) = 3`x` + 6, which differs from 3`x` + 2.",
        "Test `x` = 1: 3(3) = 9 but 3 + 2 = 5. One counterexample proves they are not "
        "equivalent.",
        "Expand 2(`x` + 3) = 2`x` + 6, which is identical to the second expression.",
        "Both are correct statements, but only the second pair is equivalent."],
       "3(`x` + 2) \u2261 3`x` + 6, so the first pair is not equivalent; the second "
       "pair is.",
       "Expanding is the test; a counterexample settles a negative answer."),
    ERR("\u201c3(`x` + 2) = 3`x` + 2, because the 3 only multiplies the first "
        "term.\u201d The factor outside a bracket multiplies every term inside: "
        "3(`x` + 2) = 3`x` + 6. Substituting `x` = 1 exposes the error immediately."),
    PRAC("5.2", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Simplify: (a) 8`y` + 3`y`  (b) 9`m` \u2212 12`m`  (c) 4 + 6`t` \u2212 4.",
          "F"),
        Q("Simplify: (a) 3`x` + 5 + 2`x` + 7  (b) 6`a` \u2212 2`a` + 4 \u2212 9.",
          "F"),
        Q("Expand: (a) 5(`x` + 2)  (b) 3(2`y` \u2212 4)  (c) 6(3 \u2212 `m`).", "F"),
        Q("Simplify 2(`x` + 5) + 3(`x` \u2212 1).", "F"),
        Q("Are 4(`x` + 1) and 4`x` + 4 equivalent? Justify.", "F"),
        Q("Simplify 5(2`a` \u2212 3) \u2212 2(`a` \u2212 4).", "P"),
        Q("Write two different expressions equivalent to 6`x` + 9.", "P"),
        Q("A student simplifies 3(`x` + 4) to 3`x` + 4. Substitute `x` = 2 into both "
          "to show the error.", "R"),
        Q("The perimeter of a rectangle is 2(`l` + `w`). Expand it and explain what "
          "each part counts.", "P"),
        Q("Simplify 4(2`x` + 1) \u2212 3(`x` \u2212 2) + `x`.", "E"),
        Q("Show that 2(`n` + 3) \u2212 2`n` always equals 6, whatever the value of "
          "`n`.", "E"),
        Q("Find a value of `x` for which 5(`x` + 2) and 5`x` + 2 give different "
          "results. Can the two expressions ever be equal? Explain.", "E"),
    ]),

    # ------------------------------------------------------------------ 5.3
    PHOTO("ch05_study.jpg", 1.5,
          "Solving by hand. Writing each step on its own line is not fussiness: it is "
          "what makes an error findable.",
          "Photograph: Pexels, free licence (see the image register)."),
    S("5.3", "Solving linear equations", "A \u00b7 III  \u00b7  C \u00b7 III",
      ["Equivalence", "Balance"]),
    L("An equation is a balance. Whatever you do to one side, you must do to the other, "
      "until the unknown stands alone."),
    DIAG(150, "balance",
         "A balance with three `x`-tiles on one side and six unit tiles on the other. "
         "Removing the same quantity from both sides keeps it level."),
    H("The balance method"),
    OL(["Simplify each side if necessary, expanding any brackets.",
        "Undo addition or subtraction first, using the inverse operation on both "
        "sides.",
        "Undo multiplication or division last.",
        "Check by substituting the solution into the original equation."]),
    P("The order matters. Undoing the operations in reverse order of their application "
      "is exactly what keeps the working readable: if the unknown was multiplied and "
      "then added to, we subtract first, then divide."),
    WE("5.3.1", "Two steps",
       "Solve 4`x` \u2212 7 = 21.",
       ["Add 7 to both sides: 4`x` = 28.",
        "Divide both sides by 4: `x` = 7.",
        "Check: 4(7) \u2212 7 = 28 \u2212 7 = 21, as required.",
        "Report the solution as `x` = 7."],
       "`x` = 7",
       "Substitution is not optional: it is the only evidence that the solution is "
       "right."),
    WE("5.3.2", "Unknown on both sides",
       "Solve 3(`x` + 2) = 5`x` \u2212 4.",
       ["Expand the left side: 3`x` + 6 = 5`x` \u2212 4.",
        "Collect the unknown on one side: subtract 3`x` from both sides, giving "
        "6 = 2`x` \u2212 4.",
        "Add 4 to both sides: 10 = 2`x`, so `x` = 5.",
        "Check in the original: 3(5 + 2) = 21 and 5(5) \u2212 4 = 21. Both agree."],
       "`x` = 5",
       "Collecting the unknown on the side that keeps it positive avoids sign "
       "slips."),
    WE("5.3.3", "A fractional solution",
       "Solve `x`/3 + 4 = 10.",
       ["Subtract 4 from both sides: `x`/3 = 6.",
        "Multiply both sides by 3: `x` = 18.",
        "Check: 18/3 + 4 = 6 + 4 = 10, as required.",
        "The solution is a whole number here, but it need not be in general."],
       "`x` = 18",
       "Multiplying by the denominator is the inverse of dividing by it."),
    ERR("\u201c4`x` \u2212 7 = 21, so 4`x` = 21 \u2212 7 = 14, so `x` = 3.5.\u201d "
        "The 7 was subtracted although it was already being subtracted. Undo "
        "\u22127 by adding 7: 4`x` = 28, so `x` = 7. Check by substitution to settle "
        "any doubt."),
    PRAC("5.3", "SUPPORT 1\u20135  \u00b7  CORE 6\u201310  \u00b7  EXTENSION "
                "11\u201313", [
        Q("Solve: (a) `x` + 9 = 15  (b) `x` \u2212 4 = 11  (c) 3`x` = 27.", "F"),
        Q("Solve: (a) 2`x` + 5 = 17  (b) 5`x` \u2212 3 = 32  (c) 4`x` + 9 = 1.", "F"),
        Q("Solve: (a) `x`/2 + 3 = 8  (b) `x`/5 \u2212 1 = 4.", "F"),
        Q("Solve 6`x` + 4 = 3`x` + 19.", "F"),
        Q("Solve 2(`x` + 3) = 16.", "F"),
        Q("Solve 5(`x` \u2212 2) = 3`x` + 4.", "P"),
        Q("Solve 4(2`x` + 1) = 3(`x` + 8).", "P"),
        Q("The perimeter of a rectangle is 46 cm. Its length is 3 cm more than its "
          "width. Write an equation and solve it.", "P"),
        Q("Two plans: Plan A costs \u00a320 plus \u00a36 per hour; Plan B costs "
          "\u00a335 plus \u00a33 per hour. Write an equation for equal cost and solve "
          "it.", "P"),
        Q("A student solves 3`x` + 4 = 19 by writing 3`x` = 19 + 4 = 23. Identify the "
          "error and give the correct solution.", "R"),
        Q("Solve 3(`x` \u2212 4) = 2(`x` + 1) and check your answer.", "E"),
        Q("The sum of three consecutive odd numbers is 87. Form an equation and solve "
          "it.", "E"),
        Q("Solve 5 \u2212 2`x` = 17 and explain why the answer is negative.", "E"),
    ]),

    CARD_D("Choosing a repair plan", [
        ("p", "A workshop offers two repair plans for a machine. Plan A charges a "
              "call-out of \u00a345 and \u00a32 for each kilometre travelled. Plan B "
              "charges no call-out but \u00a3 per kilometre, given by the expression "
              "6`k`."),
        ("ol", ["Write an expression for the cost of Plan A for `k` kilometres.",
                "For what distance do the two plans cost the same? Form an equation "
                "and solve it.",
                "For a job 15 km away, which plan is cheaper, and by how much?",
                "For a job 4 km away, which plan is cheaper?",
                "Sketch both cost lines on one set of axes and mark the point where "
                "they cross.",
                "Write one sentence of advice to a customer, using the numbers.",
                "Name one factor this comparison ignores."]),
    ]),

    # ----------------------------------------------------------- investigate
    ST("06", "INVESTIGATE AND APPLY",
       "The number trick, proved."),
    CARD_I("The number trick", [
        ("p", "A trick that always gives 3 is convincing once, but a proof is what "
              "makes it certain. This investigation turns the trick into algebra."),
        ("ol", ["Perform the trick with `n` = 2, `n` = 7 and `n` = \u22124. Record "
                "each intermediate value.",
                "Now write the expression after each step, starting from `n`: add 5, "
                "double, subtract 4, halve, subtract `n`.",
                "Simplify your final expression. Why does `n` disappear?",
                "Change one instruction and predict the new result: for example, "
                "double before adding 5.",
                "Test your prediction with two different starting numbers.",
                "Design a trick that ends in 7, and give its algebraic proof.",
                "Write a generalisation: what must be true of the instructions for "
                "the trick to end in a constant?",
                "Explain why a trick that ends in `n` + 3 cannot be used as a "
                "guessing trick."]),
    ]),

    # --------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("5.6", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["A variable is a number not yet chosen; an expression describes what would "
        "happen to it; an equation states an equality to be solved.",
        "Like terms have identical letters and indices, and only like terms can be "
        "collected.",
        "A factor outside a bracket multiplies every term inside it.",
        "Equivalent expressions agree for every substitution; one counterexample "
        "proves two expressions are not equivalent.",
        "Solving is undoing: apply inverse operations to both sides, in reverse order "
        "of application.",
        "Every solution should be checked by substitution."]),
    VOCAB("**variable** \u00b7 **term** \u00b7 **coefficient** \u00b7 "
          "**expression** \u00b7 **equation** \u00b7 **like terms** \u00b7 "
          "**simplify** \u00b7 **expand** \u00b7 **equivalent** \u00b7 "
          "**substitute** \u00b7 **solve** \u00b7 **inverse operation**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["\u201c3(`x` + 2) = 3`x` + 2.\u201d",
         "The 3 multiplies both terms: 3`x` + 6. Substituting `x` = 1 shows it."],
        ["\u201c\u22122(`x` \u2212 5) = \u22122`x` \u2212 10.\u201d",
         "Both terms change sign: \u22122`x` + 10."],
        ["\u201c4`x` \u2212 7 = 21 gives 4`x` = 14.\u201d",
         "The 7 is subtracted, so it must be added back: 4`x` = 28."],
        ["\u201c2`x` and 2`x`\u00b2 are like terms.\u201d",
         "The indices differ, so they cannot be collected: 2`x` + 2`x`\u00b2 stays "
         "as it is."],
    ], widths=[1.5, 2.0]),
    H("Revision questions"),
    OL(["Simplify 6`a` + 5 \u2212 2`a` + 3.",
        "Expand and simplify 3(2`x` \u2212 1) + 2(`x` + 4).",
        "Solve 7`x` \u2212 5 = 30.",
        "Solve 2(`x` + 4) = 5`x` \u2212 1.",
        "A hire firm charges \u00a325 plus \u00a38 per hour. Write an expression for "
        "`h` hours and find the cost of 6 hours."]),
    GAP(6),
    H("Before you move on"),
    P("Four things you should be able to do without help before the next "
      "chapter. If one of them is not yet secure, reread the section that "
      "taught it before attempting the mixed practice again.", 4),
    UL([
        "Write an expression from a description and substitute into it.",
        "Collect like terms and expand a bracket correctly.",
        "Show that two expressions are or are not equivalent.",
        "Solve a linear equation and check the solution in the original equation.",
    ]),
    KEY("A letter stands for a number, so every rule of arithmetic still applies to it."),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["write an expression from a description", "\u25a1", "\u25a1", "\u25a1"],
        ["substitute, including negative values", "\u25a1", "\u25a1", "\u25a1"],
        ["collect like terms and expand brackets", "\u25a1", "\u25a1", "\u25a1"],
        ["solve a two-step equation and check it", "\u25a1", "\u25a1", "\u25a1"],
        ["solve an equation with brackets or an unknown on both sides", "\u25a1",
         "\u25a1", "\u25a1"],
        ["form an equation from a real situation", "\u25a1", "\u25a1", "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], font_size=8.6),
    GAP(8),
    MYP("**Criterion A:** which equation type can you now solve without writing every "
        "step?\n"
        "**Criterion B:** what did the number trick show about why algebra is more "
        "than arithmetic?\n"
        "**Criterion C:** how did you show that each step kept the balance?\n"
        "**Criterion D:** which equation came from a real decision you might face?",
        "Reflect on the criteria"),
    ATL("In order for a student to solve an unfamiliar equation, students must "
        "identify which operations were applied to the unknown, and undo them in "
        "reverse order.", "ATL \u00b7 Thinking skills"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("5.M", "MIXED 1\u201312", [
        Q("Simplify 9`x` \u2212 4 + 3`x` \u2212 6.", "F"),
        Q("Expand 4(3`m` \u2212 2).", "F"),
        Q("Evaluate 3`a` + 5 when `a` = \u22123.", "F"),
        Q("Solve 8`x` + 3 = 35.", "F"),
        Q("Solve 5(`x` \u2212 2) = 20.", "F"),
        Q("Simplify 2(3`x` + 1) \u2212 4(`x` \u2212 3).", "P"),
        Q("Solve 4`x` + 7 = 2`x` + 19.", "P"),
        Q("A student writes 5`x` + 3 = 28, so 5`x` = 31. Identify the error and solve "
          "correctly.", "R"),
        Q("Write an expression for the area of a rectangle with length 2`x` + 5 and "
          "width 3.", "P"),
        Q("Two brothers' ages add to 27. One is twice the other minus 3. Form an "
          "equation and solve it.", "E"),
        Q("Show that 3(2`n` + 1) \u2212 2(3`n` \u2212 1) always equals 5.", "E"),
        Q("Solve 6 \u2212 3`x` = 21 and explain the sign of the answer.", "E"),
    ]),
]

ANSWERS = {
    "5.1": ["(a) `n` + 7 (b) 3`m` (c) `t`/4.",
            "(a) 17 (b) \u221218 (c) 2.",
            "(a) 12 (b) 27.",
            "Terms: 4`a`, 3`b`, \u22122`a`, 5; like terms 4`a` and \u22122`a`.",
            "(a) 8`m` (b) \u22123`p` (c) 4`x` + 8.",
            "0.15`m` + 8; \u00a314.",
            "4`x` + 6.",
            "Both equal 7 when `n` = 2; addition is commutative, so the order of the "
            "two terms does not change the total.",
            "\u00a350; the booking fee is \u00a320.",
            "Juxtaposition means multiplication: 4`x` with `x` = 10 is 40 only by "
            "coincidence, since 4 \u00d7 10 = 40. With `x` = 5 the expression is 20, "
            "not 45.",
            "`n` + (`n` + 1) + (`n` + 2) = 3`n` + 3.",
            "5`p` + 60; 30 people."],
    "5.2": ["(a) 11`y` (b) \u22123`m` (c) 6`t`.", "(a) 5`x` + 12 (b) 4`a` \u2212 5.",
            "(a) 5`x` + 10 (b) 6`y` \u2212 12 (c) 18 \u2212 6`m`.",
            "5`x` + 7.", "Yes: 4`x` + 4 in both cases.",
            "8`a` \u2212 7.", "3(2`x` + 3) and 6(`x` + 1.5).",
            "3(2 + 4) = 18 but 3(2) + 4 = 10, so the expansion is wrong.",
            "2`l` + 2`w`: two lengths and two widths.",
            "6`x` + 10.", "2`n` + 6 \u2212 2`n` = 6.",
            "`x` = 1 gives 15 against 7, so they differ. They can never be equal: "
            "5(`x` + 2) = 5`x` + 10, which is always 8 more than 5`x` + 2."],
    "5.3": ["(a) 6 (b) 15 (c) 9.", "(a) 6 (b) 7 (c) \u22122.", "(a) 10 (b) 25.",
            "`x` = 5.", "`x` = 5.", "`x` = 7.", "`x` = 4.",
            "2(`w` + `w` + 3) = 46, so `w` = 10 cm and the length is 13 cm.",
            "20 + 6`h` = 35 + 3`h`, so `h` = 5 hours.",
            "The 4 was added rather than subtracted: 3`x` = 15, `x` = 5.",
            "`x` = 14.",
            "The three numbers are 27, 29 and 31, from `n` + (`n` + 2) + (`n` + 4) "
            "= 87, so 3`n` + 6 = 87 and `n` = 27.",
            "`x` = \u22126; the unknown was multiplied by \u22122 before the 5 was "
            "added, so a negative value is needed."],
    "5.M": ["12`x` \u2212 10.", "12`m` \u2212 8.", "\u22124.", "`x` = 4.", "`x` = 6.",
            "2`x` + 14.", "`x` = 6.",
            "The 3 should be subtracted: 5`x` = 25, `x` = 5.",
            "3(2`x` + 5) = 6`x` + 15.",
            "`a` + (2`a` \u2212 3) = 27, so `a` = 10 and the ages are 10 and 17.",
            "6`n` + 3 \u2212 6`n` + 2 = 5.",
            "`x` = \u22125; dividing a positive by \u22123 gives a negative."],
}
