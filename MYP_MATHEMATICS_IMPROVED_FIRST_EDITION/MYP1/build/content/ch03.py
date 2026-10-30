"""Chapter 3 - Factors, multiples and primes."""
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.flow import Spacer, Pager
import diagrams as dg
from helpers import (section, lead, body, h3, lst, panel, atl, we, practice, q, fig,
                     diag, table, note, gap, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
    part="Part I \u00b7 Number, structure and proof", part_numeral="I", chapter_no=3,
    kicker="Number, structure and proof",
    title_lines=["Factors, multiples", "and primes"],
    lead_lines=["Every whole number is built from smaller whole",
                "numbers. Learning to see that structure turns division,",
                "fair sharing and repeating schedules into questions",
                "with exact answers."],
    key_concept="Relationships", related=["System", "Pattern"],
    context="Fairness and development",
    inquiry_lines=["How is a whole number built from smaller whole numbers,",
                   "and how does that structure decide what can be shared fairly"])

TITLE = "Factors, multiples and primes"
SHORT = "Factors, multiples and primes"


def build(bk, p):
    reset_counters(3)
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER"))
    p.add(Spacer(8))
    p.add(DataTable(["Statement of inquiry",
                     "Whole numbers are built from factors in a structured way, and that "
                     "structure makes it possible to divide quantities fairly, schedule "
                     "repeating events and communicate results with exact precision."],
                    [], widths=[1, 3.2], font_size=9.2, stripe=False))
    gap(p, 10)
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Relationships.** Every number greater than 1 "
                     "relates to the primes that build it, and that relationship does not "
                     "change however the number is written.\n"
                     "**Related \u00b7 System.** Divisibility rules form a system: each "
                     "one tests a specific structure in the digits.\n"
                     "**Related \u00b7 Pattern.** Multiples repeat on a regular grid, which "
                     "is why the lowest common multiple can be read from the pattern."))
    p.add(Panel("note", title="Global context \u00b7 Fairness and development",
                text="Exploration: how the structure of numbers decides what can be "
                     "shared equally, from splitting a harvest among households to "
                     "scheduling two services that must not clash."))
    gap(p, 8)
    h3(p, "Inquiry questions")
    lst(p, ["**Factual:** What is a factor, what is a multiple, and how can you tell "
            "whether one number divides another?",
            "**Conceptual:** Why is prime factorisation called the \u201cbuilding block\u201d "
            "representation of a number?",
            "**Debatable:** Is it fairer to divide a quantity using the highest common "
            "factor or the lowest common multiple?"])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Find factors, multiples, primes, HCF, LCM and prime factorisations."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate the factor table and the pattern of primes."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Present a factor tree and a Venn diagram so another reader can follow it."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Plan a fair relay schedule using common multiples."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 6)
    atl(p, "In order for a student to decide whether a large number is prime, students must "
           "test divisibility systematically and stop at the square root, rather than "
           "trying divisors at random.", "ATL \u00b7 Thinking skills")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("02", "ENGAGE", "The bakery trays."))
    body(p, "A bakery lays loaves on rectangular trays. Twelve loaves fit as 1 \u00d7 12, "
            "2 \u00d7 6 or 3 \u00d7 4. Thirteen loaves fit only as 1 \u00d7 13. The baker "
            "says thirteen is \u201ca stubborn number\u201d. Mathematicians say it is "
            "prime \u2014 and the stubbornness is the same property that makes large primes "
            "valuable in protecting messages sent across the internet.")
    fig(p, "ch03_plate_banner.jpg",
        "Arranging loaves in equal rows is a physical factorisation. Some quantities allow "
        "many rectangles; some allow only one.", wide=True)

    p.add(Stage("03", "EXPLORE", "Sort before defining."))
    body(p, "Write the numbers 1 to 20 in a row. For each number, list every way it can be "
            "written as a product of two whole numbers. Then sort the twenty numbers into "
            "three groups: those with one product, those with two, and those with more.")
    lst(p, ["Which numbers had only one product, and what do they have in common?",
            "What is special about 1, and why is it usually excluded from the primes?",
            "Which number has the most products below 21?",
            "Predict where 24 and 25 will fall before checking."], ordered=True)
    panel(p, "keyidea", title="The three families you found",
          text="**Primes** have exactly two different factors: 1 and the number itself. "
               "**Composite** numbers have more than two. **1** has only one factor, so it "
               "is neither, which keeps every statement about primes true without exception.")

    # --------------------------------------------------------------- 3.1
    section(p, "3.1", "Factors, multiples and factor pairs", "A \u00b7 i", ["System"])
    panel(p, "definition", title="Factor and multiple",
          text="A **factor** of a whole number divides it exactly, leaving no remainder. A "
               "**multiple** is the result of multiplying that number by a whole number. So "
               "6 is a factor of 24, and 24 is a multiple of 6. Factors and multiples are "
               "the same relationship seen from two directions.")
    body(p, "Factors come in pairs. Since 24 = 3 \u00d7 8, both 3 and 8 are factors, and "
            "they belong together as a pair. The factor pairs of 24 are 1 \u00d7 24, "
            "2 \u00d7 12, 3 \u00d7 8 and 4 \u00d7 6. The list stops when the two members of "
            "a pair meet or cross, which is why you never need to test beyond the square "
            "root.")
    diag(p, 108, dg.factor_pairs, "The factor pairs of 36 as rectangular arrays. Every pair "
                                  "is the same 36 counters arranged differently.", wide=True)
    panel(p, "keyidea", title="Why the square root is the stopping point",
          text="If `a` \u00d7 `b` = `n` and `a` < `b`, then `a` must be less than \u221a`n`. "
               "So every factor pair has one member below the square root. Searching up to "
               "\u221a`n` finds every pair, and searching further finds only repeats.")
    we(p, "3.1.1", "Listing the factors of 48",
       "Find all the factors of 48 and write them as pairs.",
       ["Start from 1: 1 \u00d7 48 = 48, so 1 and 48 are a pair.",
        "2 \u00d7 24 = 48; 3 \u00d7 16 = 48; 4 \u00d7 12 = 48; 6 \u00d7 8 = 48.",
        "5 and 7 do not divide 48. The next number to test is \u221a48 \u2248 6.9, and we "
        "have already passed it.",
        "So the factors are 1, 2, 3, 4, 6, 8, 12, 16, 24 and 48."],
       answer="1, 2, 3, 4, 6, 8, 12, 16, 24, 48 \u2014 ten factors.",
       check="Count them: ten. Pairs: 1\u00d748, 2\u00d724, 3\u00d716, 4\u00d712, 6\u00d78 "
             "\u2713")
    we(p, "3.1.2", "Multiples in a real schedule",
       "One bus leaves every 6 minutes and another every 8 minutes. They leave together at "
       "08:00. When will they next leave together?",
       ["List multiples of 6: 6, 12, 18, 24, 30, 36, 42, 48.",
        "List multiples of 8: 8, 16, 24, 32, 40, 48.",
        "The first common multiple is 24, and every common multiple is a multiple of 24.",
        "08:00 + 24 minutes = 08:24."],
       answer="At 08:24, and again every 24 minutes.",
       check="24 is a multiple of 6 and of 8, and no smaller number is \u2713")
    practice(p, "3.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 7\u20139", [
        q("List the factor pairs of (a) 18 (b) 28 (c) 45.", "F"),
        q("Write the first five multiples of (a) 7 (b) 11.", "F"),
        q("How many factors does 36 have? List them.", "F"),
        q("Find the numbers between 20 and 40 with exactly four factors.", "F"),
        q("Explain why 1 is a factor of every whole number.", "R"),
        q("A red light flashes every 4 seconds and a blue light every 6 seconds. They flash "
          "together at the start. When do they next flash together?", "P"),
        q("Is a multiple of a number always larger than the number? Explain using a counter-"
          "example or a justification.", "R"),
        q("Find the smallest number with exactly six factors.", "E"),
        q("Two numbers have a highest common factor of 6 and a lowest common multiple of "
          "36. Suggest a possible pair and explain how you found it.", "E"),
    ])

    # --------------------------------------------------------------- 3.2
    section(p, "3.2", "Divisibility tests", "A \u00b7 ii  \u00b7  B \u00b7 i", ["System", "Pattern"])
    body(p, "A divisibility test is a shortcut that reads the digits instead of performing "
            "the division. Each test works because of the structure of base ten, and each "
            "one can be explained rather than merely memorised.")
    diag(p, 118, dg.divisibility_rules, "Seven divisibility rules. Each is a statement about "
                                        "the digits, not about the size of the number.",
         wide=True)
    panel(p, "keyidea", title="Why the digit-sum test works for 3 and 9",
          text="Any power of 10 is one more than a multiple of 9: 10 = 9 + 1, 100 = 99 + 1, "
               "1 000 = 999 + 1. When a number is broken into its columns, every column "
               "contributes a multiple of 9 plus the digit itself. So the remainders "
               "depend only on the sum of the digits.")
    we(p, "3.2.1", "Testing 3 528 for divisibility",
       "Test 3 528 for divisibility by 3, 4, 6 and 9.",
       ["Digit sum 3 + 5 + 2 + 8 = 18, which is a multiple of 3, so 3 528 is divisible by 3.",
        "18 is not a multiple of 9? It is: 18 = 2 \u00d7 9, so 3 528 is also divisible by 9.",
        "Last two digits are 28, and 28 \u00f7 4 = 7, so divisible by 4.",
        "Divisible by 2 (it is even) and by 3, so divisible by 6."],
       answer="Divisible by 3, 4, 6 and 9.",
       check="3 528 \u00f7 9 = 392, and 392 is even \u2713")
    panel(p, "error", title="Using a digit rule on the wrong digit",
          text="The test for 4 uses the last two digits, not the last digit: 1 514 ends in "
               "4, but 14 is not a multiple of 4, so 1 514 is not divisible by 4. Read "
               "each rule precisely before applying it.")
    practice(p, "3.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Which of these are divisible by 3: 114, 205, 321, 400, 891?", "F"),
        q("Which are divisible by 9: 234, 567, 808, 1 008?", "F"),
        q("Test 2 340 for divisibility by 2, 3, 4, 5, 6 and 10.", "F"),
        q("Is 7 254 divisible by 6? Show the two tests you used.", "F"),
        q("Explain why a number ending in 0 is always divisible by both 2 and 5.", "R"),
        q("A number is divisible by 3 but not by 9. What can you say about its digit sum?",
          "R"),
        q("Find the smallest three-digit number divisible by 2, 3 and 5.", "P"),
        q("Use the structure of base ten to explain the divisibility test for 9.", "E"),
    ])

    # --------------------------------------------------------------- 3.3
    section(p, "3.3", "Prime and composite numbers", "A \u00b7 ii  \u00b7  B \u00b7 ii",
            ["Pattern", "System"])
    panel(p, "definition", title="Prime and composite",
          text="A **prime number** is a whole number greater than 1 with exactly two "
               "factors: 1 and itself. A **composite number** has more than two factors. "
               "1 is neither prime nor composite, because it has only one factor.")
    body(p, "Primes are the atoms of multiplication. Every composite number can be broken "
            "into primes, and no composite number is itself a building block. This is why "
            "primes appear in unexpected places: in the lengths of repeating patterns, in "
            "the design of calendars, and in the encryption that protects a bank transfer.")
    diag(p, 108, dg.prime_sieve, "The primes below 60. Notice that after 2 and 5, every "
                                 "prime ends in 1, 3, 7 or 9 \u2014 but not every number "
                                 "ending in those digits is prime (21 and 51 are not).",
         wide=True)
    h3(p, "Testing whether a number is prime")
    lst(p, ["Test divisibility by 2, 3, 5 and 7 first; most composites fail one of these.",
            "If nothing divides it, test the remaining primes up to its square root.",
            "Stop at the square root: if no factor has been found by then, none exists.",
            "A prime can be large; a test does not need to try every number below it."])
    we(p, "3.3.1", "Is 97 prime?",
       "Decide whether 97 is prime, showing your reasoning.",
       ["\u221a97 \u2248 9.8, so only 2, 3, 5 and 7 need be tested.",
        "97 is odd, so not divisible by 2. Digit sum 16, not a multiple of 3. It does not "
        "end in 0 or 5.",
        "97 \u00f7 7 = 13 remainder 6, so not divisible by 7.",
        "No prime up to the square root divides 97."],
       answer="97 is prime.",
       check="The next primes are 101 and 103, both larger than 97 \u2713")
    panel(p, "note", title="Why primes matter beyond the classroom",
          text="Modern encryption relies on the fact that multiplying two large primes is "
               "easy but recovering the primes from the product is not. A 200-digit number "
               "built from two 100-digit primes cannot realistically be factorised by "
               "testing, which is what protects the message.")
    practice(p, "3.3", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("List the primes between 20 and 50.", "F"),
        q("Which of these are prime: 51, 53, 57, 59, 61?", "F"),
        q("Explain why 2 is the only even prime.", "R"),
        q("Is 91 prime? Show your test.", "F"),
        q("Find two primes whose sum is 30. How many such pairs are there?", "P"),
        q("A student says 87 is prime because it is not divisible by 2, 3 or 5. Identify "
          "the error.", "R"),
        q("Find the smallest prime greater than 100, explaining each test.", "P"),
        q("Investigate: is the sum of two primes always even? Test five cases and explain "
          "the exception.", "E"),
    ])

    # --------------------------------------------------------------- 3.4
    section(p, "3.4", "Prime factorisation", "A \u00b7 iii  \u00b7  C \u00b7 iii",
            ["Representation", "System"])
    body(p, "Prime factorisation writes a number as a product of primes only. The result is "
            "unique: 60 is 2 \u00d7 2 \u00d7 3 \u00d7 5 however you find it, and no other "
            "product of primes gives 60. That uniqueness is called the fundamental theorem "
            "of arithmetic, and it is the reason factor trees always agree.")
    diag(p, 150, dg.factor_tree_full, "Two different factor trees for 60, arriving at the "
                                      "same prime factorisation: 2^{2} \u00d7 3 \u00d7 5.",
         wide=True)
    panel(p, "definition", title="Prime factorisation",
          text="The **prime factorisation** of a number is its expression as a product of "
               "prime factors, usually written with indices and with the primes in order: "
               "60 = 2^{2} \u00d7 3 \u00d7 5.")
    we(p, "3.4.1", "Factorising 84 by division",
       "Write 84 as a product of prime factors.",
       ["Divide by the smallest prime that works: 84 \u00f7 2 = 42.",
        "42 \u00f7 2 = 21. 21 is odd, so move to 3: 21 \u00f7 3 = 7.",
        "7 is prime, so stop.",
        "Collect the divisors: 2 \u00d7 2 \u00d7 3 \u00d7 7 = 2^{2} \u00d7 3 \u00d7 7."],
       answer="84 = 2^{2} \u00d7 3 \u00d7 7",
       check="2^{2} \u00d7 3 \u00d7 7 = 4 \u00d7 21 = 84 \u2713")
    we(p, "3.4.2", "Using a factorisation to test divisibility",
       "Use the prime factorisation of 360 to decide whether 360 is divisible by 24.",
       ["360 = 2^{3} \u00d7 3^{2} \u00d7 5.",
        "24 = 2^{3} \u00d7 3.",
        "Every prime power in 24 appears in 360, with at least the same exponent.",
        "So 360 \u00f7 24 = 15 exactly."],
       answer="Yes. 360 \u00f7 24 = 15.",
       check="24 \u00d7 15 = 360 \u2713")
    practice(p, "3.4", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Write as a product of prime factors: (a) 36 (b) 45 (c) 100.", "F"),
        q("Write 72 in prime factorisation form, using indices.", "F"),
        q("Write 128 as a power of 2.", "F"),
        q("Two students factorise 90 differently but reach the same answer. Show two "
          "routes.", "R"),
        q("Use prime factorisation to decide whether 210 is divisible by 14.", "P"),
        q("Explain why the prime factorisation of a prime number is just the number "
          "itself.", "R"),
        q("Find the smallest number whose prime factorisation contains exactly three "
          "different primes.", "P"),
        q("A number has prime factorisation 2^{a} \u00d7 3^{b}. It has exactly six factors. "
          "Find all possible values of the number.", "E"),
    ])

    # --------------------------------------------------------------- 3.5
    section(p, "3.5", "Highest common factor and lowest common multiple",
            "A \u00b7 iii  \u00b7  D \u00b7 i", ["Relationships", "System"])
    body(p, "Two numbers always share factors and share multiples. The largest shared "
            "factor (HCF) answers \u201chow can this be split into equal groups?\u201d The "
            "smallest shared multiple (LCM) answers \u201cwhen do these cycles meet "
            "again?\u201d Both can be read directly from the prime factorisations.")
    panel(p, "keyidea", title="Reading HCF and LCM from the factorisations",
          text="For HCF, take the primes common to both numbers and give each the "
               "**lower** exponent. For LCM, take every prime that appears and give each "
               "the **higher** exponent. With 12 = 2^{2} \u00d7 3 and 18 = 2 \u00d7 "
               "3^{2}: HCF = 2 \u00d7 3 = 6 and LCM = 2^{2} \u00d7 3^{2} = 36.")
    diag(p, 120, dg.hcf_lcm, "12 and 18 arranged as sets of factors. The shared factors sit "
                             "in the overlap; the highest common factor is the largest of "
                             "them.", wide=True)
    we(p, "3.5.1", "Splitting into equal groups",
       "A harvest of 84 mangoes and 60 oranges is to be packed into identical bags with no "
       "fruit left over, each bag holding only one kind of fruit. What is the largest "
       "number of bags possible?",
       ["The number of bags must divide both 84 and 60, so find the HCF.",
        "84 = 2^{2} \u00d7 3 \u00d7 7 and 60 = 2^{2} \u00d7 3 \u00d7 5.",
        "Common primes with lower exponents: 2^{2} \u00d7 3 = 12.",
        "So 12 bags: 7 mangoes in each of 7 bags and 5 oranges in each of 5 bags."],
       answer="12 bags.",
       check="12 \u00d7 7 = 84 and 12 \u00d7 5 = 60 \u2713")
    we(p, "3.5.2", "When do the cycles meet?",
       "One water pump is checked every 12 days and another every 18 days. Both were "
       "checked today. In how many days will both be checked on the same day again?",
       ["Find the LCM of 12 and 18.",
        "12 = 2^{2} \u00d7 3 and 18 = 2 \u00d7 3^{2}.",
        "LCM = 2^{2} \u00d7 3^{2} = 36.",
        "So both are checked together again after 36 days."],
       answer="36 days.",
       check="36 \u00f7 12 = 3 and 36 \u00f7 18 = 2, both whole numbers \u2713")
    practice(p, "3.5", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Find the HCF of (a) 12 and 20 (b) 18 and 27.", "F"),
        q("Find the LCM of (a) 4 and 6 (b) 8 and 12.", "F"),
        q("Find the HCF and LCM of 24 and 36.", "F"),
        q("Why is the HCF of two numbers never larger than the smaller number?", "R"),
        q("Two bells ring every 15 and every 20 minutes. If they ring together at 09:00, "
          "when do they next ring together?", "P"),
        q("A teacher has 48 pencils and 36 rulers and wants identical packs with no "
          "remainder. What is the greatest number of packs?", "P"),
        q("Explain why the product of the HCF and LCM of two numbers equals the product of "
          "the numbers, using 12 and 18.", "E"),
        q("Find two numbers whose HCF is 4 and whose LCM is 60.", "E"),
    ])

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("04", "INVESTIGATE"))
    section(p, "Investigation 3", "The factor table", None, ["Pattern", "System"])
    body(p, "Draw a table with the numbers 1 to 20 across the top and down the side. Shade "
            "the cell where the row number is a factor of the column number. Work "
            "systematically; do not shade cell by cell.")
    table(p, ["Number", "1", "2", "3", "4", "5", "6", "8", "10", "12"],
          [["Factors", "all", "even", "digit sum", "last two", "ends 0/5", "2 and 3",
            "three 2s", "2 and 5", "3 and 4"]],
          widths=[0.85] + [0.42] * 9, fs=7.6)
    h3(p, "Your investigation")
    lst(p, ["Which column is fully shaded, and why?",
            "Which rows have the fewest shaded cells, and what kind of number are they?",
            "Describe the shading pattern for row 2, row 3 and row 4 in words.",
            "Predict the shading for row 7 without drawing it.",
            "Explain why a number with exactly two shaded cells in the table is prime.",
            "Look down the diagonal. What do the shaded cells there represent?"],
        ordered=True)
    panel(p, "keyidea", title="The structure the table reveals",
          text="Multiples form a regular grid: row `n` is shaded every `n` columns. Primes "
               "are the rows with exactly two shaded cells. The diagonal is shaded because "
               "every number is a factor of itself \u2014 which is precisely what makes the "
               "definition of a prime depend on having exactly one other factor.")
    atl(p, "In order for a student to generalise from a table, students must describe the "
           "rule in words before writing any symbol, then test the description on a row "
           "they have not shaded.", "ATL \u00b7 Transfer")
    gap(p, 8)
    p.add(Stage("05", "APPLY"))
    section(p, "Real-life application", "The fairness relay", "D \u00b7 i\u2013iv",
            ["Relationships", "System"])
    body(p, "A school sports day runs three relay races around the same track. The junior "
            "race takes 4 minutes per lap, the middle race 6 minutes and the senior race 9 "
            "minutes. All three start together at 09:00. The organisers need to know when "
            "the track is free for the award ceremony.")
    h3(p, "Your task")
    lst(p, ["Find the LCM of 4, 6 and 9, showing your prime factorisations.",
            "State the first three times all three races finish together.",
            "The ceremony needs 30 clear minutes. Recommend a start time and justify it.",
            "Each race has 24 runners, 18 runners and 12 runners, and the organisers want "
            "equal teams within each race with no one left out. Find the largest possible "
            "team size shared by all three races.",
            "Explain which of your two answers came from the LCM and which from the HCF, "
            "and why the context decided it."],
        ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Identify the quantities and the constraint (simultaneous, or no "
                 "remainder).",
                 "Choose HCF or LCM from the structure of the problem.",
                 "Apply prime factorisation accurately.",
                 "Justify that the recommended schedule is realistic."])
    gap(p, 8)
    p.break_page()
    p.add(Stage("06", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "The fairness poster", "C \u00b7 i\u2013iii  \u00b7  D \u00b7 ii", [])
    body(p, "**Context.** A community association wants a poster that explains, without "
            "using the words \u201chighest common factor\u201d or \u201clowest common "
            "multiple\u201d, how to share a harvest equally and how to schedule two "
            "repeating events.")
    lst(p, ["Choose two quantities (one shared, one scheduled) and state them.",
            "Show the factorisation of each quantity using a diagram.",
            "Explain, in no more than 60 words, how the diagram answers each question.",
            "Include one worked example with a check.",
            "Ask a classmate to use your poster on a new pair of numbers. Record whether "
            "they succeed, then revise one part.",
            "Evaluate your poster: one strength, one limitation, one improvement."],
        ordered=True)
    criteria_panel(p, a="ii: accurate factorisation and correct HCF and LCM.",
                   c="i, ii, iii: precise language and a diagram a reader can follow.")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("07", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, ["Factors and multiples describe the same relationship from opposite directions.",
            "Divisibility tests read the structure of the digits, and each can be explained.",
            "Primes are the multiplicative building blocks; 1 is neither prime nor composite.",
            "Prime factorisation is unique, so different routes give the same answer.",
            "HCF answers \u201cequal groups\u201d; LCM answers \u201cwhen do cycles "
            "meet\u201d."])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["factor", "A whole number that divides another exactly."],
        ["multiple", "The product of a number and a whole number."],
        ["prime", "A whole number greater than 1 with exactly two factors."],
        ["composite", "A whole number with more than two factors."],
        ["prime factorisation", "A number written as a product of primes."],
        ["HCF", "The largest number dividing two or more numbers exactly."],
        ["LCM", "The smallest number that is a multiple of two or more numbers."],
    ], widths=[0.85, 2.3])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that persist",
          text="**1 is prime.** It has only one factor, so it fails the definition.\n"
               "**The LCM is the product.** Only when the numbers share no factor; "
               "LCM(4, 6) = 12, not 24.\n"
               "**A number ending in 3 is prime.** 33, 63 and 93 all end in 3 and none is "
               "prime.")
    assessment_close(p, [
        ["list factors and multiples systematically", "\u25a1", "\u25a1", "\u25a1"],
        ["apply divisibility tests", "\u25a1", "\u25a1", "\u25a1"],
        ["decide whether a number is prime", "\u25a1", "\u25a1", "\u25a1"],
        ["write a prime factorisation", "\u25a1", "\u25a1", "\u25a1"],
        ["find the HCF and LCM", "\u25a1", "\u25a1", "\u25a1"],
        ["choose HCF or LCM from a context", "\u25a1", "\u25a1", "\u25a1"],
        
    ],
        "In order for a student to recognise which of HCF and LCM a word problem "
               "needs, students must state in one sentence what the answer represents "
               "\u2014 equal groups, or a repeat \u2014 before calculating anything.",
        next_title="Chapter 4 · Fractions and decimals")


    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("08", "MIXED PRACTICE"))
    practice(p, "Mixed practice 3",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201311  \u00b7  EXTENSION 9\u201314", [
        q("List all the factors of 60.", "F"),
        q("Find the HCF of 30 and 45.", "F"),
        q("Find the LCM of 6, 8 and 12.", "F"),
        q("Write 180 as a product of prime factors.", "F"),
        q("Which of 97, 111, 121 and 131 are prime?", "F"),
        q("Explain why every even number greater than 2 is composite.", "R"),
        q("A number has exactly three factors. What kind of number is it? Give two "
          "examples.", "R"),
        q("Two runners complete a lap in 45 and 60 seconds. Starting together, when do they "
          "next pass the start line together?", "P"),
        q("Pencils come in packs of 12 and pens in packs of 18. What is the smallest number "
          "of each that gives equal numbers of pencils and pens?", "P"),
        q("Use divisibility tests to decide whether 4 356 is divisible by 12.", "R"),
        q("Find the largest two-digit prime and justify that it is prime.", "E"),
        q("Show that the product of two consecutive numbers is always even.", "E"),
        q("Find two numbers whose LCM is 48 and whose HCF is 4.", "E"),
        q("A rectangular courtyard is 84 tiles long and 60 tiles wide. Square tiles of the "
          "largest possible size are to cover it exactly. Find the tile size and the "
          "number of tiles.", "E"),
    ])
    gap(p, 8)
    p.add(Stage("09", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20132", "Revisit 3.1: write factor pairs and stop at the square root."],
        ["3\u20134", "Revisit 3.4 and 3.5: build the prime factorisations first."],
        ["5\u20137", "Revisit 3.3: test primes up to the square root only."],
        ["8\u201310", "Revisit 3.5: decide whether the question asks for equal groups or "
                      "for a repeat."],
        ["11\u201314", "Revisit the investigation: patterns in factors explain all of "
                      "these."],
    ], widths=[0.7, 2.6])


ANSWERS = [
    ("3.1", "1 (a) 1\u00d718, 2\u00d79, 3\u00d76 (b) 1\u00d728, 2\u00d714, 4\u00d77 "
            "(c) 1\u00d745, 3\u00d715, 5\u00d79.  2 (a) 7, 14, 21, 28, 35 (b) 11, 22, 33, "
            "44, 55.  3 Nine factors: 1, 2, 3, 4, 6, 9, 12, 18, 36.  4 21, 22, 26, 27, 33, "
            "34, 35, 38, 39.  6 12 seconds.  8 12 (factors 1, 2, 3, 4, 6, 12)."),
    ("3.2", "1 114, 321, 891.  2 234, 567.  3 Divisible by 2, 3, 4, 5, 6 and 10.  "
            "4 Yes: even, and digit sum 18.  6 The digit sum is a multiple of 3 but not of "
            "9.  7 120."),
    ("3.3", "1 23, 29, 31, 37, 41, 43, 47.  2 53, 59, 61.  4 91 = 7 \u00d7 13, not "
            "prime.  5 7 + 23, 11 + 19, 13 + 17: three pairs.  7 101."),
    ("3.4", "1 (a) 2^{2}\u00d73^{2} (b) 3^{2}\u00d75 (c) 2^{2}\u00d75^{2}.  "
            "2 2^{3} \u00d7 3^{2}.  3 2^{7}.  5 210 = 2\u00d73\u00d75\u00d77 and "
            "14 = 2\u00d77, so yes.  7 30.  8 2^{2}\u00d73 = 12 or 2\u00d73^{2} = 18."),
    ("3.5", "1 (a) 4 (b) 9.  2 (a) 12 (b) 24.  3 HCF 12, LCM 72.  5 10:00.  "
            "6 12 packs.  8 4 and 60, or 12 and 20."),
    ("Investigation 3", "Column 1 is fully shaded because 1 divides everything. Prime rows "
                        "have exactly two shaded cells (1 and the number). Row `n` is "
                        "shaded every `n` columns."),
    ("Mixed 3", "1 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60.  2 15.  3 24.  "
                "4 2^{2} \u00d7 3^{2} \u00d7 5.  5 97 and 131.  7 A square of a prime: "
                "4, 9, 25.  8 180 seconds.  9 36 pencils and 24 pens.  10 Yes: divisible "
                "by 3 (digit sum 18) and by 4 (last two digits 56).  11 97.  "
                "13 16 and 12, or 48 and 4.  14 12-tile squares; 7 \u00d7 5 = 35 tiles."),
]
