"""Chapter 8 - Sets and classification."""
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.flow import Spacer, Pager
import diagrams as dg
from helpers import (section, lead, body, h3, lst, panel, atl, we, practice, q, fig,
                     diag, table, note, gap, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
    part="Part IV \u00b7 Describing space and belonging", part_numeral="IV", chapter_no=8,
    kicker="Describing space and belonging",
    title_lines=["Sets and the art of", "classification"],
    lead_lines=["A set is only a collection with a rule for belonging. Almost",
                "every mathematical idea begins with deciding what belongs",
                "together \u2014 and stating the rule precisely enough that",
                "nothing slips in unnoticed."],
    key_concept="Form", related=["Representation", "System"],
    context="Identities and relationships",
    inquiry_lines=["What makes a classification useful rather than merely tidy, and who",
                   "decides where the boundary lies?"])

TITLE = "Sets and classification"
SHORT = "Sets and classification"


def build(bk, p):
    reset_counters(8)
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER"))
    p.add(Spacer(8))
    p.add(DataTable(["Statement of inquiry",
                     "Classifying objects into sets with precisely stated rules reveals "
                     "structure that is invisible when the objects are considered one at a "
                     "time."],
                    [], widths=[1, 3.2], font_size=9.2, stripe=False))
    gap(p, 10)
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Form.** A set is defined by the form of its rule, "
                     "not by the objects it happens to collect.\n"
                     "**Related \u00b7 Representation.** Venn diagrams, set brackets and "
                     "number-system trees are three representations of the same relation.\n"
                     "**Related \u00b7 System.** Number systems nest inside one another, and "
                     "the nesting is itself a set relation."))
    p.add(Panel("note", title="Global context \u00b7 Identities and relationships",
                text="Exploration: how a community sorts its own members \u2014 by age, by "
                     "trade, by household \u2014 and what a sorting rule includes and "
                     "excludes."))
    gap(p, 8)
    h3(p, "Inquiry questions")
    lst(p, ["**Factual:** What does it mean for an element to belong to a set, and how is "
            "this written?",
            "**Conceptual:** Why does a precise rule matter more than a list?",
            "**Debatable:** Can any classification be neutral?"])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Use set notation accurately to describe a collection."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Find the pattern in the number of subsets of a set."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Draw a Venn diagram that another student can read correctly."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Sort a real collection and justify the rule chosen."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 6)
    atl(p, "In order for a student to classify without ambiguity, students must state the "
           "rule in a form that can be tested on a borderline object.",
           "ATL \u00b7 Critical and creative thinking")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("02", "ENGAGE", "Everything in this room."))
    body(p, "Sort everything in the room into two groups, then into three, then into five. "
            "Each time, write the rule you used. Now swap rules with another group and try "
            "to sort by their rule without asking what it means.")
    fig(p, "ch08_plate_banner.jpg",
        "A sorting hall is a classification made physical: the shelves encode a rule that "
        "customers are expected to infer.", wide=True)

    p.add(Stage("03", "EXPLORE", "One rule, two results."))
    body(p, "Take the numbers from 1 to 20. Sort them using the rule \u201ceven\u201d, then "
            "using the rule \u201cmultiple of 3\u201d, then using both rules at once.")
    lst(p, ["Which numbers appear in both groups?",
            "Which numbers appear in neither group?",
            "Does every number belong to at least one group this time? Try a different pair "
            "of rules where it does not.",
            "Write a rule that puts every number 1\u201320 into exactly one group."],
        ordered=True)
    diag(p, 100, dg.set_sort_grid, "The numbers 1 to 20 arranged by two rules at once. The "
                                   "overlap is the set of numbers satisfying both.",
         wide=True)
    panel(p, "keyidea", title="Classification needs a test",
          text="A classification is only as good as the test it implies. If you cannot say "
               "whether a borderline object belongs, the rule is not yet precise enough.")

    # --------------------------------------------------------------- 8.1
    section(p, "8.1", "Sets, elements and notation", "A \u00b7 i, ii  \u00b7  C \u00b7 i",
            ["Form", "Representation"])
    panel(p, "definition", title="Set and element",
          text="A **set** is a well-defined collection of objects. Each object in it is an "
               "**element** (or member). We write `x` \u2208 `A` to mean that `x` belongs to "
               "set `A`, and `x` \u2209 `A` to mean that it does not.")
    h3(p, "Two ways to name a set")
    table(p, ["Method", "Example", "When to use it"], [
        ["Listing (roster)", "`A` = {2, 4, 6, 8}", "The set is small or finite."],
        ["Rule (set-builder)", "`B` = {`x` : `x` is an even number, 1 \u2264 `x` \u2264 8}",
         "The pattern is clearer than the list."],
    ], widths=[1.25, 1.7, 1.1])
    body(p, "Curly brackets always mean a set. Round brackets never do. The colon in a "
            "rule reads \u201csuch that\u201d, and the condition after it must be precise "
            "enough to decide any candidate object.")
    we(p, "8.1.1", "Reading set notation",
       "`A` = {2, 4, 6, 8, 10}. Decide whether each statement is true or false: "
       "6 \u2208 `A`, 7 \u2208 `A`, 10 \u2209 `A`.",
       ["6 is listed in `A`, so 6 \u2208 `A` is true.",
        "7 is not listed, so 7 \u2208 `A` is false, which means 7 \u2209 `A` is true.",
        "10 is listed, so 10 \u2209 `A` is false."],
       answer="True, false, false.",
       check="Every element of `A` satisfies the rule \u201ceven, between 1 and 11\u201d \u2713")
    we(p, "8.1.2", "Describing a set by rule",
       "Write the set of whole numbers between 5 and 15 that are divisible by 3, both by "
       "listing and by rule.",
       ["Candidates: 6, 9, 12, 15.",
        "Listed: {6, 9, 12, 15}.",
        "By rule: {`x` : `x` is a whole number, 5 < `x` \u2264 15, `x` is a multiple of 3}.",
        "The rule must state the range as well as the property, or it describes an infinite "
        "set."],
       answer="{6, 9, 12, 15}",
       check="Check the boundaries: 5 is excluded, 15 is included \u2713")
    panel(p, "error", title="Confusing \u2208 with \u2282",
          text="\u2208 compares an object with a set; \u2282 compares two sets. 3 \u2208 "
               "{1, 2, 3} is true, but {3} \u2282 {1, 2, 3} is a different statement about a "
               "set, not the number.")
    practice(p, "8.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("List the set of vowels in the word MATHEMATICS.", "F"),
        q("Decide whether 12 \u2208 {multiples of 4}. Explain.", "F"),
        q("Write {3, 6, 9, 12} by rule.", "F"),
        q("Write the set of even numbers from 2 to 12 by listing.", "F"),
        q("Explain the difference between \u2208 and \u2282.", "R"),
        q("Write a rule that describes {1, 4, 9, 16, 25}.", "P"),
        q("A set `S` = {`x` : `x` is a letter in BANANA}. List `S` and explain why it has "
          "fewer elements than the word has letters.", "P"),
        q("Find a rule that is precise for whole numbers but ambiguous for decimals, and "
          "explain the ambiguity.", "E"),
    ])

    # --------------------------------------------------------------- 8.2
    section(p, "8.2", "Subsets, the universal set and the complement", "A \u00b7 iii  \u00b7  C \u00b7 ii",
            ["System", "Representation"])
    panel(p, "definition", title="Subset, universal set, complement",
          text="`A` \u2282 `B` means every element of `A` is also in `B`. The **universal "
               "set** \u03be is everything under discussion. The **complement** `A`\u2032 "
               "contains every element of \u03be that is not in `A`.")
    body(p, "The universal set is a decision, not a fact. If \u03be is the whole numbers, "
            "the complement of the evens is the odds; if \u03be is the digits 0\u20139, the "
            "complement is {1, 3, 5, 7, 9}. Always state \u03be before using a complement.")
    diag(p, 108, dg.complement_venn, "The shaded region is the complement of `A` inside the "
                                     "universal set \u03be.", wide=True)
    we(p, "8.2.1", "Listing subsets",
       "List all subsets of {`a`, `b`}.",
       ["The empty set \u2205 is a subset of every set.",
        "Single-element subsets: {`a`}, {`b`}.",
        "The whole set: {`a`, `b`}.",
        "That is four subsets."],
       answer="\u2205, {`a`}, {`b`}, {`a`, `b`}.",
       check="A set with 2 elements has 2^{2} = 4 subsets \u2713")
    we(p, "8.2.2", "Using the complement",
       "\u03be = {1, 2, 3, \u2026, 12}, `A` = {multiples of 3}. List `A` and `A`\u2032.",
       ["`A` = {3, 6, 9, 12}.",
        "`A`\u2032 contains everything in \u03be not in `A`: {1, 2, 4, 5, 7, 8, 10, 11}.",
        "Check that the two sets together give all twelve elements with no repeats."],
       answer="`A`\u2032 = {1, 2, 4, 5, 7, 8, 10, 11}",
       check="4 + 8 = 12 elements in total \u2713")
    practice(p, "8.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Is {2, 4} a subset of {1, 2, 3, 4}? Explain.", "F"),
        q("List all subsets of {`p`, `q`, `r`}.", "F"),
        q("\u03be = {1, \u2026, 10}, `A` = {primes}. List `A` and `A`\u2032.", "F"),
        q("How many subsets has a set with 4 elements?", "F"),
        q("Explain why the empty set is a subset of every set.", "R"),
        q("Investigate the pattern in the number of subsets of a set with `n` elements and "
          "write the rule.", "P"),
        q("A class of 30 students is the universal set; 12 play football, 9 play chess. "
          "Explain why you cannot yet find the complement of the football players without "
          "more information.", "E"),
        q("Is every set a subset of itself? Justify your answer.", "E"),
    ])

    # --------------------------------------------------------------- 8.3
    section(p, "8.3", "Union, intersection and Venn diagrams", "A \u00b7 ii  \u00b7  C \u00b7 iii",
            ["Representation", "System"])
    panel(p, "definition", title="Union and intersection",
          text="The **union** `A` \u222a `B` contains everything in `A` or `B` or both. The "
               "**intersection** `A` \u2229 `B` contains only what is in both. Two sets with "
               "no common element are **disjoint**.")
    diag(p, 112, dg.set_operations, "Union and intersection shown on two identical circles. "
                                     "The shading, not the labels, carries the meaning.",
         wide=True)
    we(p, "8.3.1", "Reading a Venn diagram",
       "In a class of 32, 18 study French, 15 study Spanish and 7 study both. Find the "
       "number who study at least one language and the number who study neither.",
       ["Both: 7.",
        "French only: 18 \u2212 7 = 11.",
        "Spanish only: 15 \u2212 7 = 8.",
        "At least one: 11 + 7 + 8 = 26.",
        "Neither: 32 \u2212 26 = 6."],
       answer="26 study at least one; 6 study neither.",
       check="11 + 7 + 8 + 6 = 32, the whole class \u2713",
       prompt="Fill the overlap first: everything else is a subtraction from it.")
    we(p, "8.3.2", "Counting without a diagram",
       "`A` = {2, 4, 6, 8, 10} and `B` = {4, 8, 12}. Find `A` \u222a `B` and `A` \u2229 `B`.",
       ["Intersection: elements in both \u2014 4 and 8.",
        "Union: everything in either, listed once \u2014 2, 4, 6, 8, 10, 12.",
        "Note that 4 and 8 appear once in the union, not twice."],
       answer="`A` \u2229 `B` = {4, 8}; `A` \u222a `B` = {2, 4, 6, 8, 10, 12}",
       check="|`A`| + |`B`| \u2212 |`A` \u2229 `B`| = 5 + 3 \u2212 2 = 6 = |`A` \u222a `B`| "
             "\u2713")
    panel(p, "error", title="Adding the overlap twice",
          text="Adding 18 and 15 in Example 8.3.1 gives 33, which is larger than the whole "
               "class. The seven students in both were counted twice; subtract them once.")
    practice(p, "8.3", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("`A` = {1, 2, 3, 4}, `B` = {3, 4, 5}. Find `A` \u222a `B` and `A` \u2229 `B`.", "F"),
        q("In a group of 20, 12 like tea, 9 like coffee, 5 like both. How many like "
          "neither?", "F"),
        q("Draw a Venn diagram for two disjoint sets.", "F"),
        q("`C` = {vowels}, `D` = {letters in MATHEMATICS}. Find `C` \u2229 `D`.", "F"),
        q("Explain why `A` \u2229 `B` is always a subset of `A`.", "R"),
        q("In a survey of 40 students, 25 walk to school, 18 cycle, 10 do both. Draw the "
          "diagram and find how many do neither.", "P"),
        q("Two sets have 12 and 15 elements and their union has 20. Find the size of the "
          "intersection.", "P"),
        q("Investigate whether `A` \u222a `B` can ever have fewer elements than `A`. Explain "
          "using a diagram.", "E"),
    ])

    # --------------------------------------------------------------- 8.4
    section(p, "8.4", "Classifying numbers and shapes", "A \u00b7 i, iii  \u00b7  B \u00b7 i",
            ["Form", "System"])
    body(p, "Sets give classification a language. The number systems from Chapter 1 nest "
            "inside one another, and each nesting is a subset relation that can be drawn.")
    diag(p, 120, dg.number_system_tree, "The number systems as nested sets. Every natural "
                                        "number is a whole number, every whole number an "
                                        "integer, and so on.", wide=True)
    panel(p, "definition", title="Classifying by more than one property",
          text="A quadrilateral can be classified by two independent properties: the number "
               "of pairs of parallel sides, and whether the sides are equal. Drawing the "
               "two properties as a two-way table reveals the categories and their "
               "overlaps at the same time.")
    table(p, ["", "One pair parallel", "Two pairs parallel"], [
        ["All sides equal", "\u2014", "rhombus (and square)"],
        ["Opposite sides equal", "trapezium", "parallelogram / rectangle"],
        ["No sides equal", "trapezium", "parallelogram"],
    ], widths=[1.0, 1.0, 1.4])
    we(p, "8.4.1", "Classifying a number",
       "Place \u22125 in as many number sets as it belongs to.",
       ["\u22125 is an integer, because it is a whole number with a sign.",
        "It is rational, because it can be written \u22125/1.",
        "It is real. It is not natural or whole, because those sets start at 0 or 1."],
       answer="Integer, rational, real.",
       check="Check each definition rather than the appearance of the number \u2713")
    practice(p, "8.4", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("List the number sets to which 0 belongs.", "F"),
        q("Is every square a rectangle? Explain using sets.", "F"),
        q("Sort these into rational and irrational: 0.25, \u221a2, 7, \u03c0, \u22123/4.", "F"),
        q("Name the quadrilateral with two pairs of parallel sides and four right angles.",
          "F"),
        q("Explain why every natural number is an integer but not every integer is a "
          "natural number.", "R"),
        q("Draw a two-way table classifying triangles by angle type and by side equality.",
          "P"),
        q("Classify the numbers 1 to 20 by \u201cprime\u201d and \u201ceven\u201d in a "
          "two-way table, and describe the empty cell.", "P"),
        q("Investigate whether a classification can be complete and non-overlapping at the "
          "same time, using shapes as an example.", "E"),
    ])

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("04", "INVESTIGATE"))
    section(p, "Investigation 8", "How many subsets?", None, ["Form", "System"])
    body(p, "A set with one element has two subsets. Build sets of two, three and four "
            "elements, list every subset and count them. Record the counts in a table and "
            "look for the pattern.")
    table(p, ["Elements", "Number of subsets", "Subsets"], [
        ["0", "1", "\u2205"], ["1", "2", "\u2205, {`a`}"],
        ["2", "4", "\u2026"], ["3", "8", "\u2026"], ["4", "\u2026", "\u2026"],
    ], widths=[0.8, 1.1, 1.6])
    h3(p, "Your investigation")
    lst(p, ["Complete the table by listing, not by guessing.",
            "Describe the pattern in the middle column as a rule involving `n`.",
            "Explain why doubling happens each time a new element is added: what can you do "
            "with every existing subset?",
            "Predict the number of subsets of a five-element set and check by listing.",
            "State the rule for the number of subsets of a set with `n` elements."],
        ordered=True)
    panel(p, "keyidea", title="The result",
          text="A set with `n` elements has 2^{n} subsets. Each element is either in or out "
               "of a given subset, so there are two independent choices per element.")
    atl(p, "In order for a student to generalise, students must move from counting cases to "
           "explaining why the count doubles.", "ATL \u00b7 Transfer")
    p.break_page()
    p.add(Stage("05", "APPLY"))
    section(p, "Real-life application", "The clinic waiting list", "D \u00b7 i\u2013iv",
            ["System", "Change"])
    body(p, "A clinic records which of two services each patient used last month: the "
            "general clinic (G) and the laboratory (L). In a sample of 60 patients, 38 used "
            "G, 27 used L and 15 used both. The clinic must justify its staffing to a "
            "funding committee.")
    h3(p, "Your task")
    lst(p, ["Draw a Venn diagram and fill in all four regions.",
            "Find the number who used exactly one service.",
            "Find the number who used neither, and explain what that group could be.",
            "Write two sentences the clinic director could use, each reporting a different "
            "true number in a way that supports a different staffing decision.",
            "Explain why the same data can support two different conclusions.",
            "State one way the survey could have produced misleading numbers."],
        ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Identify the given quantities and the universal set.",
                 "Use the Venn diagram and subtraction as strategies.",
                 "Apply the method accurately and check that the four regions sum to 60.",
                 "Evaluate how presentation of the same data changes its effect."])
    gap(p, 8)
    p.add(Stage("06", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "The sorting rule", "C \u00b7 i\u2013iv  \u00b7  B \u00b7 ii", [])
    body(p, "**Context.** Your class library needs re-shelving. The current rule "
            "\u201cfiction and non-fiction\u201d no longer works for the collection.")
    lst(p, ["Collect or imagine 20 items. State a sorting rule with two properties.",
            "Draw the two-way table and place every item.",
            "Identify any item that is hard to place and explain why.",
            "Revise the rule so that the difficult item can be placed.",
            "Test the revised rule on a classmate's item list.",
            "Evaluate: which rule produced fewer empty cells, and did that make it a better "
            "classification?"], ordered=True)
    criteria_panel(p, b="i\u2013iii: the pattern in the number of subsets.",
                   c="i\u2013iv: table clarity, notation and justification of the rule.")
    diag(p, 150, dg.sorting_table, "A two-property classification drawn as a table: each "
                                   "cell is an intersection of the two rules.", wide=True)
    panel(p, "keyidea", title="An empty cell is evidence",
          text="A cell with no items is not a failure: it says no object in your "
               "collection satisfies both properties. Ask whether the property is badly "
               "chosen or the collection is genuinely limited, and say which in your "
               "write-up.")
    h3(p, "Before you hand this in")
    lst(p, ["Name both properties in the table heading.",
            "The four cell counts must add to the total.",
            "Show where your revised rule puts the awkward item.",
            "Say what the table revealed that a list would hide."])

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("07", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, ["A set is defined by a rule, and \u2208 tests membership of elements.",
            "Curly brackets name sets; the colon in a rule reads \u201csuch that\u201d.",
            "`A` \u2282 `B`, the universal set \u03be and the complement `A`\u2032 extend set "
            "vocabulary.",
            "`A` \u222a `B` and `A` \u2229 `B` describe everything-in-either and "
            "everything-in-both.",
            "A set with `n` elements has 2^{n} subsets."])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["element", "An object belonging to a set."],
        ["subset", "A set all of whose elements lie in another set."],
        ["universal set \u03be", "Everything under discussion in a particular problem."],
        ["complement", "The elements of \u03be that are not in the set."],
        ["union", "Everything in either set, listed once."],
        ["intersection", "Only the elements in both sets."],
        ["disjoint", "Having no elements in common."],
        ["empty set \u2205", "The set with no elements; a subset of every set."],
    ], widths=[1.0, 2.2])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that persist", items=[
        "**A list is a set.** {1, 2, 2, 3} is the set {1, 2, 3}: repeats collapse.",
        "**\u2208 and \u2282 are interchangeable.** They compare an object with a set and a "
        "set with a set.",
        "**Sets are always numbers.** A set can contain letters, shapes or people.",
    ])
    assessment_close(p, [
            ["read and write set notation", "\u25a1", "\u25a1", "\u25a1"],
            ["list subsets of a set", "\u25a1", "\u25a1", "\u25a1"],
            ["use a universal set and complement", "\u25a1", "\u25a1", "\u25a1"],
            ["find unions and intersections", "\u25a1", "\u25a1", "\u25a1"],
            ["complete a Venn diagram from a word problem", "\u25a1", "\u25a1", "\u25a1"],
            ["justify a classification rule", "\u25a1", "\u25a1", "\u25a1"],
        
    ],
        "In order for a student to state a rule, students must test it against one "
               "object that does and one that does not belong.",
        next_title="Chapter 9 · Perimeter, area and surface area")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("08", "MIXED PRACTICE"))
    practice(p, "Mixed practice 8",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201311  \u00b7  EXTENSION 9\u201314", [
        q("List the set of factors of 12.", "F"),
        q("Is 15 \u2208 {multiples of 5}? Explain.", "F"),
        q("Write {1, 8, 27, 64} by rule.", "F"),
        q("How many subsets has a set with 5 elements?", "F"),
        q("\u03be = {1, \u2026, 9}, `A` = {1, 3, 5, 7, 9}. List `A`\u2032.", "F"),
        q("Explain what a universal set is and why it must be stated.", "R"),
        q("`A` = {2, 3, 5, 7}, `B` = {1, 2, 3, 4}. Find `A` \u222a `B` and `A` \u2229 `B`.",
          "R"),
        q("In a group of 50, 30 read the newspaper, 22 read magazines, 12 read both. Draw "
          "the diagram and find the number who read neither.", "P"),
        q("A set has 64 subsets. How many elements has it?", "P"),
        q("Explain why a Venn diagram with two circles has four regions, and draw a third "
          "circle to show how many regions appear.", "P"),
        q("Sort the numbers 1 to 30 by the properties \u201cprime\u201d and \u201cmultiple "
          "of 3\u201d in a two-way table.", "P"),
        q("A survey of 40 people asked whether they owned a bicycle (B) and a helmet (H). "
          "22 had B, 18 had H and 10 had neither. Find how many had both.", "E"),
        q("Investigate whether the number of regions in a Venn diagram with `n` circles "
          "follows a simple rule, testing up to three circles.", "E"),
        q("Design a classification of the quadrilaterals in this chapter using two "
          "properties, and state which cells are empty and why.", "E"),
    ])
    gap(p, 8)
    p.add(Stage("09", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20135", "Revisit 8.1 and 8.2: rule first, list second."],
        ["6\u20137", "Revisit 8.3: name each region before adding."],
        ["8\u201311", "Revisit 8.3 and the investigation: fill the overlap first."],
        ["12\u201314", "Revisit 8.4: two properties give a table, not a list."],
    ], widths=[0.7, 2.6])


ANSWERS = [
    ("8.1", "1 {A, E, I}.  2 No: 12 is a multiple of 4, so the statement is true only if "
            "12 \u2208 {4, 8, 12, \u2026}.  3 {3`x` : 1 \u2264 `x` \u2264 4}.  "
            "4 {2, 4, 6, 8, 10, 12}.  6 Square numbers.  7 {B, A, N}: 3 elements."),
    ("8.2", "1 Yes: both elements are in the larger set.  2 \u2205, {`p`}, {`q`}, {`r`}, "
            "{`p`,`q`}, {`p`,`r`}, {`q`,`r`}, {`p`,`q`,`r`}.  3 {2, 3, 5, 7}; "
            "{1, 4, 6, 8, 9, 10}.  4 16."),
    ("8.3", "1 \u222a = {1, 2, 3, 4, 5}; \u2229 = {3, 4}.  2 4.  "
            "4 {A, E, I}.  6 7 do neither.  7 7."),
    ("8.4", "1 Natural, whole, integer, rational, real.  2 Yes: a square satisfies the "
            "definition of a rectangle, so squares \u2282 rectangles.  3 Rational: 0.25, 7, "
            "\u22123/4; irrational: \u221a2, \u03c0.  4 Rectangle."),
    ("Investigation 8", "Subsets: 1, 2, 4, 8, 16, 32 for `n` = 0, 1, 2, 3, 4, 5. Each new "
                        "element doubles the count, because every subset either contains it "
                        "or does not: 2^{n}."),
    ("Mixed 8", "1 {1, 2, 3, 4, 6, 12}.  2 Yes.  3 {`n`^{3} : 1 \u2264 `n` \u2264 4}.  "
                "4 32.  5 {2, 4, 6, 8}.  7 \u222a = {1, 2, 3, 4, 5, 7}; \u2229 = {2, 3}.  "
                "8 10 read neither.  9 6 elements.  12 10 had both.  13 Regions 2, 4, 8 for "
                "1, 2, 3 circles."),
]
