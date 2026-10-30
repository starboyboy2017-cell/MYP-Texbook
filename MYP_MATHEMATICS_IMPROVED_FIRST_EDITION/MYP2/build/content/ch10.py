"""Chapter 10 - Probability and simulation (Probability and data)."""
from chbase import *

PLATE = dict(
    part="Part IV \u00b7 Probability and data", part_numeral="IV", chapter_no=10,
    kicker="Probability and data", motif="probability",
    title_lines=["Probability", "and simulation"],
    lead_lines=["Probability does not tell you what will happen. It measures",
                "how strongly the evidence favours each possibility \u2014",
                "and it lets you build a model, then test it."],
    key_concept="Logic", related=["Chance", "Models"],
    context="Fairness and development",
    inquiry_lines=["When is a game fair, and who decides what counts as fair?"])

TITLE = "Probability and simulation"
SHORT = "Probability and simulation"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "From counting outcomes to testing whether a game is fair."),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "Probability assigns a number to uncertainty, and that number can be "
              "checked by experiment, so claims about chance can be tested rather "
              "than believed."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Logic.** A probability follows from the set of possible "
        "outcomes and the assumption that they are equally likely \u2014 or from the "
        "long-run behaviour of an experiment.\n"
        "**Related \u00b7 Chance.** Outcomes may be impossible, unlikely, even "
        "chance, likely or certain.\n"
        "**Related \u00b7 Models.** A tree diagram or sample-space grid is a model of "
        "the situation, and a simulation tests it."),
    BOX("note", "Global context \u00b7 Fairness and development",
        "Exploration: gambling, insurance, weather forecasting and games of chance. "
        "Who bears the risk, and who profits from it, depends on probabilities being "
        "understood."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** How do you calculate the probability of a single event?",
        "**Conceptual:** Why does experimental probability approach theoretical "
        "probability as the number of trials increases?",
        "**Debatable:** Is a game fair if the expected gain is zero but the odds feel "
        "unfair?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii",
         "Calculate simple and combined probabilities."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Simulate an experiment and describe the pattern in the results."],
        ["C \u00b7 Communicating", "ii, iii, iv",
         "Use notation `P`(A), fractions, decimals and tree diagrams correctly."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv, v",
         "Design a fair game and justify its fairness with expected values."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to test a claim about chance, students must design a "
        "simulation that models the situation, collect enough trials, and compare the "
        "experimental result with the theoretical prediction."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Use the probability scale.",
         "Place events from 0 to 1 and use the words correctly."],
        ["Calculate a simple probability.",
         "Write `P`(event) as a fraction, decimal and percentage."],
        ["List a sample space.",
         "Show every outcome for two coins or two dice without missing any."],
        ["Use tree diagrams for combined events.",
         "Multiply along branches and add between branches."],
        ["Calculate experimental probability.",
         "Compare a relative frequency with a theoretical value."],
        ["Design and run a simulation.",
         "Explain what a random device models and how many trials are needed."],
    ], widths=[1.6, 1.8]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Simplify \u00a0 6/36.",
               "Write 0.25 as a fraction and as a percentage.",
               "Calculate \u00a0 0.3 \u00d7 0.3.",
               "How many outcomes when two coins are tossed?",
               "Calculate \u00a0 20% of 150.",
               "Write 3/8 as a decimal."]),
    P("If three or more answers are wrong, revisit fractions and decimals in part I "
      "before continuing."),

    # ------------------------------------------------------------------ 10.1
    S("10.1", "Probability and its scale", "A \u00b7 I  \u00b7  C \u00b7 II",
      ["Chance", "Models"]),
    L("Probability measures how likely an event is, on a scale from 0 (impossible) to "
      "1 (certain). Every other probability sits between them."),
    ST("03", "ENGAGE",
       "The game with a hidden rule."),
    P("A stall offers a prize if you roll a six with one die, but the die looks slightly "
      "worn. Before reading on, write down (a) the probability of a six if the die is "
      "fair, and (b) one experiment you could run to test whether it is fair."),
    DIAG(170, "spinner",
         "A spinner divided into six equal sectors. Each colour's probability is the "
         "number of its sectors divided by six."),
    ST("04", "EXPLORE",
       "Count the outcomes, then reason."),
    OL(["Spin the spinner 20 times and record the results in a tally table.",
        "Calculate the relative frequency of each colour.",
        "Compare your results with the probabilities suggested by the sector "
        "sizes.",
        "Combine your class results. What happens to the relative frequencies?",
        "Explain what would happen with 5000 spins.",
        "Describe a spinner that would give a probability of 1 for blue and 0 for "
        "red."]),
    ST("05", "EXPLAIN"),
    DEF("The `probability` of an event A is written `P`(A). If all outcomes are "
        "equally likely, `P`(A) = (number of favourable outcomes) \u00f7 (total number "
        "of outcomes). For any event, 0 \u2264 `P`(A) \u2264 1, and `P`(not A) = 1 "
        "\u2212 `P`(A)."),
    TABLE(["Probability", "0", "0.25", "0.5", "0.75", "1"], [
        ["Words", "impossible", "unlikely", "even chance", "likely", "certain"],
        ["Fraction", "0", "1/4", "1/2", "3/4", "1"],
        ["Percentage", "0%", "25%", "50%", "75%", "100%"],
    ], widths=[0.9, 0.75, 0.7, 0.75, 0.6, 0.6], fs=8.4),
    WE("10.1.1", "A single event",
       "A bag contains 3 red and 5 blue counters. One is taken at random. Find the "
       "probability that it is (a) red, (b) blue, (c) not red.",
       ["There are 8 counters in total.",
        "(a) `P`(red) = 3/8.",
        "(b) `P`(blue) = 5/8.",
        "(c) `P`(not red) = 1 \u2212 3/8 = 5/8, the same as `P`(blue) because every "
        "counter is either red or blue.",
        "Check: 3/8 + 5/8 = 1."],
       "(a) 3/8 (b) 5/8 (c) 5/8",
       "Probabilities of all possible outcomes always total 1."),
    WE("10.1.2", "Three forms",
       "A spinner has 4 equal sectors, one of which is gold. Write the probability of "
       "gold as a fraction, a decimal and a percentage.",
       ["Favourable outcomes 1, total 4, so `P`(gold) = 1/4.",
        "1 \u00f7 4 = 0.25.",
        "0.25 = 25%.",
        "The complement, `P`(not gold), is 0.75 or 75%."],
       "1/4 = 0.25 = 25%",
       "All three forms describe the same number; choose the form the question "
       "asks for."),
    WE("10.1.3", "Working from a probability",
       "A box contains 20 counters, some red. The probability of drawing red is 0.3. "
       "How many red counters are there?",
       ["`P`(red) = (number red) \u00f7 (total) = 0.3.",
        "Number red = 0.3 \u00d7 20 = 6.",
        "Check: 6/20 = 0.3, as required.",
        "The other 14 counters are not red."],
       "6 red counters",
       "Multiply the probability by the total to recover a count."),
    ERR("\u201cThe probability of winning is 1.2, because there are more chances of "
        "winning than losing.\u201d A probability can never exceed 1: 1.2 would mean "
        "more favourable outcomes than outcomes. Ratios of chances are not "
        "probabilities."),
    PRAC("10.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Find the probability of rolling a 4 on a fair six-sided die.", "F"),
        Q("Write the probability of each event: (a) impossible (b) certain (c) an even "
          "chance.", "F"),
        Q("A bag has 3 red and 5 blue counters. Find `P`(red) and `P`(blue).", "F"),
        Q("A spinner has 4 equal sectors numbered 1 to 4. Find `P`(1).", "F"),
        Q("The probability of rain is 0.35. Find the probability that it does not "
          "rain.", "F"),
        Q("A bag has 5 red, 4 green and 1 yellow counter. Find `P`(not green).", "P"),
        Q("Write `P` = 1/4 as a decimal and as a percentage.", "F"),
        Q("A box of 20 counters has probability 0.3 of drawing red. How many red "
          "counters are there?", "P"),
        Q("A student writes `P`(win) = 1.2 and `P`(lose) = 0.3. Explain what is wrong "
          "with both numbers.", "R"),
        Q("A bag contains red and blue counters only. `P`(red) = 0.45. There are 22 "
          "blue counters. How many counters are there in total?", "E"),
        Q("A die is rolled once. Write the probability of (a) a prime number (b) a "
          "number greater than 2 (c) a multiple of 7.", "E"),
        Q("Explain why the probabilities of all the possible outcomes of an event must "
          "add to 1.", "E"),
    ]),

    # ------------------------------------------------------------------ 10.2
    S("10.2", "Sample spaces", "A \u00b7 II  \u00b7  C \u00b7 III", ["Chance",
      "Logic"]),
    L("A sample space is a complete list of what could happen. Listing it "
      "systematically turns a probability question into a counting question."),
    PHOTO("ch10_dice.jpg", 1.5,
          "A pair of dice. Six faces each give thirty-six ordered pairs, and the pairs "
          "are not all equally likely to give the same total.",
          "Photograph: Pexels, free licence (see the image register)."),
    DIAG(200, "sample_grid",
         "A sample-space grid for rolling two dice. Thirty-six equally likely cells "
         "allow every sum to be counted rather than guessed."),
    DEF("A `sample space` is the set of all possible outcomes of an experiment. Two "
        "events are `mutually exclusive` if they cannot happen at the same time; their "
        "probabilities then add."),
    WE("10.2.1", "Two coins",
       "Two fair coins are tossed. List the sample space and find the probability of "
       "(a) two heads, (b) exactly one head.",
       ["The sample space is HH, HT, TH, TT \u2014 four outcomes, all equally likely.",
        "(a) HH occurs once, so `P`(two heads) = 1/4.",
        "(b) HT and TH give exactly one head, so `P` = 2/4 = 1/2.",
        "Check: 1/4 + 1/2 + 1/4 = 1, counting also TT."],
       "(a) 1/4 (b) 1/2",
       "HT and TH are different outcomes; treating them as one gives the classic "
       "wrong answer of 1/3."),
    WE("10.2.2", "Two dice",
       "Two fair dice are rolled. Find the probability that the total is (a) 7 and (b) "
       "less than 4.",
       ["There are 6 \u00d7 6 = 36 equally likely outcomes.",
        "(a) The total is 7 for (1,6), (2,5), (3,4), (4,3), (5,2), (6,1): six "
        "outcomes, so `P` = 6/36 = 1/6.",
        "(b) Totals below 4 are 2 and 3: (1,1) gives 2; (1,2) and (2,1) give 3, so "
        "three outcomes.",
        "`P`(less than 4) = 3/36 = 1/12."],
       "(a) 1/6 (b) 1/12",
       "Counting from the grid prevents the common error of assuming totals are "
       "equally likely."),
    WE("10.2.3", "A coin and a die",
       "A coin is tossed and a die is rolled. How many outcomes are in the sample "
       "space, and what is the probability of a head and an even number?",
       ["The coin has 2 outcomes and the die has 6, so there are 2 \u00d7 6 = 12 "
        "outcomes.",
        "Even numbers on the die are 2, 4 and 6, three outcomes.",
        "Together with a head this gives 3 favourable outcomes.",
        "`P`(head and even) = 3/12 = 1/4."],
       "12 outcomes; `P` = 1/4",
       "Multiply the numbers of outcomes, then count the favourable ones."),
    ERR("\u201cWith two dice, a total of 7 and a total of 8 are equally likely because "
        "each can be made in several ways.\u201d A 7 can be made in six ways and an 8 "
        "in five, so 7 is more likely. Only the sample-space grid shows this."),
    PRAC("10.2", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Two coins are tossed. List the sample space and find `P`(two heads).", "F"),
        Q("A die is rolled. Find `P`(even).", "F"),
        Q("Two dice are rolled. Find `P`(total 12).", "F"),
        Q("A coin is tossed and a die rolled. How many outcomes are there?", "F"),
        Q("Two dice are rolled. Find `P`(total 7).", "P"),
        Q("Two dice are rolled. Find `P`(total less than 4).", "P"),
        Q("Two dice are rolled. Find `P`(total is prime).", "P"),
        Q("Two coins are tossed. Find the probability of at least one head.", "P"),
        Q("A student says `P`(two heads) with two coins is 1/3 because there are three "
          "possibilities: two heads, two tails, or one of each. Explain the error.",
          "R"),
        Q("Three coins are tossed. List the sample space and find `P`(exactly two "
          "heads).", "E"),
        Q("Two dice are rolled. Find the probability that the two numbers are the "
          "same.", "E"),
        Q("Two dice are rolled 200 times. Predict how often the total will be 7, and "
          "explain your reasoning.", "E"),
    ]),

    # ------------------------------------------------------------------ 10.3
    S("10.3", "Tree diagrams and combined events", "A \u00b7 III  \u00b7  C \u00b7 "
      "IV", ["Models", "Logic"]),
    L("A tree diagram shows a sequence of events branch by branch. Multiply along a "
      "branch for \u201cand\u201d; add between branches for \u201cor\u201d."),
    PHOTO("ch10_coins.jpg", 1.5,
          "Two coins. HT and TH are different outcomes, which is why counting the "
          "sample space carefully matters.",
          "Photograph: Pexels, free licence (see the image register)."),
    DIAG(165, "tree_diagram",
         "A tree diagram for two tosses of a coin. Multiplying along a branch gives the "
         "probability of both outcomes occurring."),
    KEY("**Multiplication rule:** for independent events, `P`(A and B) = `P`(A) "
        "\u00d7 `P`(B).\n**Addition rule:** for mutually exclusive events, `P`(A or B) "
        "= `P`(A) + `P`(B).\n**Without replacement**, the second probability changes "
        "because the first item has been removed."),
    WE("10.3.1", "Two independent events",
       "A bag has 4 red and 6 blue counters. One is taken, replaced, then another is "
       "taken. Find `P`(both red) and `P`(one of each colour).",
       ["The total stays 10 because the counter is replaced.",
        "`P`(red) = 4/10 = 0.4 on each draw.",
        "`P`(both red) = 0.4 \u00d7 0.4 = 0.16.",
        "`P`(one of each) = `P`(RB) + `P`(BR) = 0.4\u00d70.6 + 0.6\u00d70.4 = 0.24 + "
        "0.24 = 0.48."],
       "`P`(RR) = 0.16; `P`(one of each) = 0.48",
       "There are two orders for \u201cone of each\u201d, so both branches must be "
       "included."),
    WE("10.3.2", "Without replacement",
       "A bag has 4 red and 6 blue counters. Two are taken without replacement. Find "
       "`P`(both red) and `P`(one of each colour).",
       ["First draw: `P`(red) = 4/10. After removing one red, 3 red remain out of 9.",
        "`P`(RR) = 4/10 \u00d7 3/9 = 12/90 = 2/15.",
        "`P`(RB) = 4/10 \u00d7 6/9 = 24/90 and `P`(BR) = 6/10 \u00d7 4/9 = 24/90.",
        "`P`(one of each) = 48/90 = 8/15."],
       "`P`(RR) = 2/15; `P`(one of each) = 8/15",
       "Both the numerator and the denominator change on the second draw."),
    WE("10.3.3", "At least one",
       "The probability of rain on any day is 0.3, independently. Find the probability "
       "of rain on at least one of two days.",
       ["Easier to find the complement: no rain on a day has probability 0.7.",
        "`P`(no rain on either day) = 0.7 \u00d7 0.7 = 0.49.",
        "`P`(at least one rainy day) = 1 \u2212 0.49 = 0.51.",
        "Check that this is more than 0.3 and less than 0.6, as it must be."],
       "0.51",
       "\u201cAt least one\u201d is almost always quicker through the complement."),
    ERR("\u201cTwo events each with probability 0.5 have probability 1 of happening "
        "between them.\u201d Adding probabilities works only for mutually exclusive "
        "events. If both can happen, adding double counts the overlap, and the total "
        "can even exceed 1."),
    PRAC("10.3", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Two coins are tossed. Use a tree diagram to find `P`(two tails).", "F"),
        Q("A bag has 4 red and 6 blue counters. One is taken and replaced, then another "
          "is taken. Find `P`(both red).", "F"),
        Q("The probability of rain on a day is 0.3. Find the probability of rain on two "
          "independent days.", "F"),
        Q("A fair coin is tossed twice. Find `P`(exactly one head).", "F"),
        Q("A bag has 4 red and 6 blue counters. Two are taken without replacement. "
          "Find `P`(both red).", "P"),
        Q("For the same bag, find `P`(one of each colour) without replacement.", "P"),
        Q("The probability of rain on any day is 0.3. Find the probability of rain on "
          "at least one of two independent days.", "P"),
        Q("A family has two children. Assuming each is equally likely to be a boy or a "
          "girl, find `P`(one boy and one girl).", "P"),
        Q("A student adds `P`(head) + `P`(even) for a coin and a die. Explain why the "
          "answer is meaningless.", "R"),
        Q("A bag has 5 red and 3 green counters. Two are taken without replacement. "
          "Find `P`(both green).", "E"),
        Q("Two dice are rolled. Find `P`(at least one six).", "E"),
        Q("A machine produces a faulty item with probability 0.05. Find the probability "
          "that in three independent items none is faulty, and hence the probability "
          "that at least one is faulty.", "E"),
    ]),

    # ------------------------------------------------------------------ 10.4
    S("10.4", "Experimental probability and simulation", "B \u00b7 I  \u00b7  D "
      "\u00b7 III", ["Chance", "Models"]),
    L("Experimental probability comes from data. As the number of trials grows, the "
      "relative frequency settles towards the theoretical probability \u2014 which is "
      "why a simulation can test a model."),
    DEF("`Experimental probability` (relative frequency) = number of times the event "
        "occurred \u00f7 number of trials. `Expected frequency` = probability \u00d7 "
        "number of trials. A `simulation` replaces a real experiment with a random "
        "device that models it."),
    WE("10.4.1", "From a table of results",
       "A spinner is spun 200 times; red appears 84 times. Find the experimental "
       "probability of red and comment on whether the spinner looks fair if red has one "
       "third of the sectors.",
       ["Experimental probability = 84 \u00f7 200 = 0.42.",
        "The theoretical probability for a fair spinner with one third red is about "
        "0.333.",
        "The experimental value is higher, but 200 trials still allow noticeable "
        "variation.",
        "A conclusion needs more trials: the difference is suggestive, not "
        "conclusive."],
       "0.42; inconclusive but worth more trials",
       "Small samples vary; state how many trials would settle the question."),
    WE("10.4.2", "Expected frequency",
       "A die is rolled 150 times. How many sixes would you expect, and how many "
       "would you expect for an even number?",
       ["`P`(six) = 1/6, so expected sixes = 1/6 \u00d7 150 = 25.",
        "`P`(even) = 1/2, so expected even numbers = 1/2 \u00d7 150 = 75.",
        "Expected values are averages over many repetitions, not predictions of a "
        "single run.",
        "Check: 25 \u00d7 6 = 150, which is consistent."],
       "25 sixes; 75 even numbers",
       "Expectation multiplies the probability by the number of trials."),
    WE("10.4.3", "Designing a simulation",
       "Design a simulation to estimate the probability that, in a group of 30 people, "
       "at least two share a birthday. State the model, the trials and the "
       "comparison.",
       ["Model: each person's birthday is a random whole number from 1 to 365, chosen "
        "independently.",
        "Use a random-number generator to produce 30 numbers in that range; check "
        "whether any repeat.",
        "Repeat for many trials \u2014 100 or more \u2014 and count the trials with a "
        "repeat.",
        "The estimate is (trials with a repeat) \u00f7 (total trials); compare with "
        "the theoretical value of about 0.71."],
       "Random numbers 1\u2013365, 30 per trial, many trials",
       "A simulation must state what is random, how it is generated, and how many "
       "trials."),
    ERR("\u201cThe experimental probability is 0.42, so the true probability is "
        "0.42.\u201d An experimental value estimates the true probability and varies "
        "from sample to sample. It becomes more reliable as the number of trials "
        "increases, but it never becomes exact."),
    PRAC("10.4", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("A spinner lands on red 84 times in 200 spins. Find the experimental "
          "probability of red.", "F"),
        Q("A die is rolled 150 times. How many sixes would you expect?", "F"),
        Q("A coin is tossed 50 times and lands heads 22 times. Find the experimental "
          "probability of heads.", "F"),
        Q("`P`(win) = 0.2. In 80 games, how many wins would you expect?", "F"),
        Q("A die is rolled 300 times. How many even numbers would you expect, and how "
          "many ones?", "P"),
        Q("A bag has 3 red and 7 blue counters. In 200 draws with replacement, how "
          "many reds would you expect?", "P"),
        Q("A coin lands heads 30 times in 40 tosses. Is the coin likely to be biased? "
          "Explain carefully.", "R"),
        Q("Describe a simulation to estimate the probability of getting at least one "
          "six in four rolls of a die.", "P"),
        Q("Why does an experimental probability from 20 trials differ more from the "
          "theoretical value than one from 2000 trials?", "R"),
        Q("A spinner is spun 500 times; blue appears 260 times. If blue has one quarter "
          "of the sectors, comment on whether the spinner is fair.", "E"),
        Q("A machine produces faulty items with probability 0.05. In a day's production "
          "of 400 items, how many faults are expected, and what would 12 faults "
          "suggest?", "E"),
        Q("Design a simulation to decide whether a coin is fair, stating the number of "
          "trials and the decision rule.", "E"),
    ]),

    CARD_D("The school fair game", [
        ("p", "A stall charges \u00a31 to roll two dice. A player wins \u00a33 if the "
              "total is 7, \u00a32 if the total is 11, and nothing otherwise. The "
              "organiser wants to know whether the stall will raise money."),
        ("ol", ["List the sample space for two dice and count the outcomes giving 7 "
                "and 11.",
                "Calculate `P`(7) and `P`(11).",
                "Calculate the expected payout per game.",
                "Find the expected profit per game for the stall.",
                "Estimate the profit from 300 games.",
                "Suggest one change to the prizes that would increase the expected "
                "profit, and justify it with calculations."]),
    ]),

    # ----------------------------------------------------------- investigate
    ST("06", "INVESTIGATE AND APPLY",
       "Simulation and the fair game."),
    CARD_I("Simulating a queue", [
        ("p", "A small shop has one till. Customers arrive at random, and the manager "
              "wants to know how long queues become."),
        ("ol", ["Decide which quantities are random and give each a range.",
                "Use random numbers to generate a short sequence of arrivals and "
                "service times.",
                "Simulate ten customers and record the queue length after each.",
                "Repeat the simulation and compare the two runs.",
                "Estimate the average queue length over your runs.",
                "Decide how many runs would be needed before the estimate could be "
                "trusted.",
                "Explain one assumption in your model that might be unrealistic."]),
    ]),
    CARD_I("Is the game fair?", [
        ("p", "Two players each roll a die. Player A scores the difference between the "
              "two numbers; player B scores the smaller number."),
        ("ol", ["Build a 6 by 6 grid of the difference and a second grid of the "
                "smaller number.",
                "Find the probability of each possible score for A and for B.",
                "Calculate the expected score for each player.",
                "Decide whether the game is fair.",
                "Change one rule so that the game becomes fair, and verify with "
                "expected scores.",
                "Explain why a game can look fair and still favour one player."]),
    ]),

    # --------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("10.6", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["Probability lies between 0 and 1, and `P`(not A) = 1 \u2212 `P`(A).",
        "For equally likely outcomes, `P`(A) = favourable \u00f7 total.",
        "A sample space lists every outcome; a grid makes two-stage experiments "
        "countable.",
        "Multiply along branches of a tree for \u201cand\u201d, add between branches "
        "for \u201cor\u201d.",
        "Without replacement, the second probability changes.",
        "Experimental probability estimates theoretical probability and improves with "
        "more trials."]),
    VOCAB("**probability** \u00b7 **outcome** \u00b7 **event** \u00b7 **sample "
          "space** \u00b7 **equally likely** \u00b7 **mutually exclusive** \u00b7 "
          "**independent** \u00b7 **complement** \u00b7 **relative frequency** \u00b7 "
          "**expected frequency** \u00b7 **simulation**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["Two coins give three outcomes, so `P`(two heads) = 1/3.",
         "HT and TH are different, giving four equally likely outcomes and `P` = "
         "1/4."],
        ["Adding probabilities of events that can happen together.",
         "Addition is for mutually exclusive events; otherwise the overlap is counted "
         "twice."],
        ["Assuming a total of 7 and a total of 8 are equally likely.",
         "There are six ways to score 7 and five ways to score 8."],
        ["Thinking an experimental probability is the exact probability.",
         "It is an estimate that varies; more trials narrow the variation."],
    ], widths=[1.55, 1.95]),
    H("Revision questions"),
    OL(["A bag has 7 red and 3 blue counters. Find `P`(blue).",
        "Two dice are rolled. Find `P`(total 5).",
        "A coin is tossed three times. Find `P`(three heads).",
        "`P`(rain) = 0.4 each day. Find `P`(no rain on two independent days).",
        "A die is rolled 240 times. How many threes would you expect?"]),
    GAP(6),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["calculate a simple probability and its complement", "\u25a1", "\u25a1",
         "\u25a1"],
        ["list a sample space systematically", "\u25a1", "\u25a1", "\u25a1"],
        ["use a tree diagram for two-stage events", "\u25a1", "\u25a1", "\u25a1"],
        ["handle \u201cwithout replacement\u201d correctly", "\u25a1", "\u25a1",
         "\u25a1"],
        ["calculate expected frequencies", "\u25a1", "\u25a1", "\u25a1"],
        ["design and interpret a simulation", "\u25a1", "\u25a1", "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], font_size=8.6),
    GAP(8),
    MYP("**Criterion A:** which probability rule can you now apply without a "
        "prompt?\n"
        "**Criterion B:** what did the simulation show that a single calculation could "
        "not?\n"
        "**Criterion C:** were your fractions, decimals and tree diagrams clear enough "
        "to follow?\n"
        "**Criterion D:** how did expected values settle a question about fairness?",
        "Reflect on the criteria"),
    ATL("In order for a student to evaluate a probability claim, students must compare "
        "a theoretical prediction with experimental evidence and judge whether the "
        "difference is larger than chance would explain.", "ATL \u00b7 Research "
        "skills"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("10.M", "MIXED 1\u201312", [
        Q("Find `P`(rolling an odd number) on a fair die.", "F"),
        Q("A bag has 2 red, 3 green and 5 blue counters. Find `P`(green).", "F"),
        Q("Write 0.6 as a fraction and a percentage.", "F"),
        Q("Two coins are tossed. Find `P`(no heads).", "F"),
        Q("A die is rolled 60 times. How many fives would you expect?", "F"),
        Q("Two dice are rolled. Find `P`(total 9).", "P"),
        Q("A bag has 5 red and 3 green counters. One is taken without replacement, "
          "then another. Find `P`(both green).", "P"),
        Q("A spinner lands on red 96 times in 300 spins. Find the experimental "
          "probability.", "P"),
        Q("A student says `P`(at least one head in two tosses) = 1/2 + 1/2 = 1. "
          "Explain the error.", "R"),
        Q("A game costs \u00a32 and pays \u00a35 with probability 0.25. Find the "
          "expected profit per game.", "E"),
        Q("Three fair coins are tossed. Find `P`(at least two heads).", "E"),
        Q("Two dice are rolled. Find `P`(both numbers even or a total of 7), and "
          "explain why the addition rule applies here.", "E"),
    ]),
]

ANSWERS = {
    "10.1": ["1/6.", "(a) 0 (b) 1 (c) 0.5.", "3/8 and 5/8.", "1/4.", "0.65.",
             "6/10 = 3/5.", "0.25 and 25%.", "6.",
             "A probability cannot exceed 1, and the two probabilities cannot add to "
             "more than 1 while describing only two outcomes.",
             "`P`(blue) = 0.55, so total = 22 \u00f7 0.55 = 40 counters.",
             "(a) 3/6 = 1/2 (b) 4/6 = 2/3 (c) 0.",
             "The outcomes are mutually exclusive and together cover every "
             "possibility, so their probabilities account for the whole of certainty, "
             "which is 1."],
    "10.2": ["HH, HT, TH, TT; 1/4.", "1/2.", "1/36.", "12 outcomes.", "1/6.",
             "1/12.", "15/36 = 5/12.", "3/4.",
             "\u201cOne of each\u201d can happen in two orders, HT and TH, so the four "
             "outcomes are not equally split into three groups.",
             "HHH, HHT, HTH, HTT, THH, THT, TTH, TTT; `P`(exactly two heads) = 3/8.",
             "6/36 = 1/6.", "About 33 times, since `P`(7) = 1/6 and 1/6 \u00d7 200 "
             "\u2248 33."],
    "10.3": ["1/4.", "0.16.", "0.09.", "1/2.", "2/15.", "8/15.", "0.51.", "1/2.",
             "The events are not mutually exclusive and belong to different "
             "experiments, so they cannot be added.",
             "3/8 \u00d7 2/7 = 6/56 = 3/28.", "1 \u2212 (5/6)\u00b2 = 11/36.",
             "0.95\u00b3 = 0.857; at least one faulty = 0.143."],
    "10.4": ["0.42.", "25.", "0.44.", "16.", "150 even and 50 ones.",
             "60 reds.", "30/40 = 0.75 is high, but 40 tosses is a small sample; a "
             "larger number of tosses is needed before calling the coin biased.",
             "Roll a die four times and record whether any six appears; repeat for "
             "many trials.",
             "Smaller samples vary more about the theoretical value; larger samples "
             "average out the variation.",
             "260/500 = 0.52 against 0.25, which is far too high for chance, so the "
             "spinner looks biased.",
             "20 faults expected; 12 is below expectation and would not by itself "
             "suggest a problem.",
             "Toss the coin 200 times; if heads lies outside a reasonable range "
             "around 100, judge it biased."],
    "10.M": ["1/2.", "3/10.", "3/5 and 60%.", "1/4.", "10.", "4/36 = 1/9.",
             "3/28.", "0.32.", "The events overlap: heads on the first toss and heads "
             "on the second can both happen, so the probabilities cannot simply be "
             "added.",
             "Expected payout 0.25 \u00d7 5 = \u00a31.25 against a \u00a32 cost, so the "
             "expected profit is \u2212\u00a30.75 per game.",
             "4/8 = 1/2.", "9/36 + 6/36 = 15/36 = 5/12; a total of 7 is odd, so it "
             "cannot have both numbers even and the events are mutually exclusive."],
}
