"""Chapter 11 - Univariate data (Probability and data)."""
from chbase import *

PLATE = dict(
    part="Part IV \u00b7 Probability and data", part_numeral="IV", chapter_no=11,
    kicker="Probability and data", motif="data",
    title_lines=["Univariate data"],
    lead_lines=["One variable, many values. A single average hides almost",
                "everything, so this chapter is about choosing the right",
                "summary and the right display \u2014 and about saying what",
                "the data does not show."],
    key_concept="Representation", related=["Measurement", "Patterns"],
    context="Scientific and technical innovation",
    inquiry_lines=["What is a fair way to summarise a set of measurements,",
                   "and what does the summary leave out?"])

TITLE = "Univariate data"
SHORT = "Univariate data"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "Collecting one variable well, summarising it honestly, and comparing "
       "groups."),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "A single variable can be represented by a table, a display and a small "
              "set of summary numbers, and each representation reveals something the "
              "others hide."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Representation.** Data becomes evidence only when it is "
        "organised into a form that can be read and compared.\n"
        "**Related \u00b7 Measurement.** Every value carries the error of the "
        "instrument that produced it.\n"
        "**Related \u00b7 Patterns.** Spread and shape are patterns in data, not "
        "noise to be averaged away."),
    BOX("note", "Global context \u00b7 Scientific and technical innovation",
        "Exploration: measurement, sensor data and the displays that turn readings "
        "into decisions. A graph is an argument, and it can mislead."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** How do you calculate the mean, median, mode and range?",
        "**Conceptual:** Why can two data sets with the same mean look completely "
        "different?",
        "**Debatable:** Should a summary always report the average, or the median?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii",
         "Calculate and interpret the averages, range, quartiles and IQR."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate how an outlier changes each summary."],
        ["C \u00b7 Communicating", "ii, iii, iv",
         "Choose and construct an appropriate display."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv, v",
         "Analyse school data and justify a recommendation."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to interpret a data display, students must state what "
        "the display shows, what it leaves out, and how the choice of summary changes "
        "the conclusion."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Classify data as numerical or categorical.",
         "Say whether a variable is discrete, continuous or categorical."],
        ["Calculate the mean, median, mode and range.",
         "Choose the summary that suits the data and say why."],
        ["Find the mean from a frequency table.",
         "Use \u03a3`fx` \u00f7 \u03a3`f` correctly."],
        ["Construct and read displays.",
         "Draw a bar chart, dot plot or frequency diagram with sensible scales."],
        ["Find quartiles and the interquartile range.",
         "Read them from an ordered list and from a box plot."],
        ["Compare two data sets.",
         "Compare an average and a measure of spread, not just the averages."],
    ], widths=[1.6, 1.8]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Add \u00a0 4 + 7 + 7 + 9 + 13.",
               "Find the middle value of 3, 5, 8, 10, 12.",
               "Divide 40 by 5.",
               "How many values are in 2, 4, 4, 6, 7, 8?",
               "Write 0.25 as a percentage.",
               "Find the difference between 45 and 20."]),
    P("If three or more answers are wrong, revisit arithmetic with decimals before "
      "continuing."),

    # ------------------------------------------------------------------ 11.1
    S("11.1", "Data and how to collect it", "A \u00b7 I  \u00b7  C \u00b7 II",
      ["Measurement", "Representation"]),
    L("Before any calculation, the important decisions are what to measure, how to "
      "measure it, and whose values to include."),
    ST("03", "ENGAGE",
       "The average that hid the problem."),
    P("A class reports that the average journey to school is 12 minutes. One student "
      "travels 55 minutes. Before reading on, decide what the reporter should do about "
      "that value, and whether removing it would improve the report or damage it."),
    ST("04", "EXPLORE",
       "Measure, tabulate, interrogate."),
    PHOTO("ch11_charts.jpg", 0.66,
          "A dashboard of charts. Each chart answers a question; none of them answers "
          "every question.",
          "Photograph: Pexels, free to use under the Pexels licence.", 0.60),
    TABLE(["Variable", "Type", "Possible values"], [
        ["Number of people in a household", "numerical, discrete", "1, 2, 3, \u2026"],
        ["Height in centimetres", "numerical, continuous", "any value in a range"],
        ["Favourite subject", "categorical", "named categories"],
        ["Time to walk to school", "numerical, continuous", "any value in minutes"],
        ["Number of pets", "numerical, discrete", "0, 1, 2, \u2026"],
    ], widths=[1.7, 1.15, 1.35], fs=8.6),
    OL(["Decide which of the variables above you could collect in your class in five "
        "minutes.",
        "For one variable, write the exact question you would ask, so that two people "
        "would answer it the same way.",
        "Collect ten values and check whether any are impossible or misread.",
        "Decide whether your data is discrete, continuous or categorical.",
        "Identify one way your sample could be biased.",
        "Suggest how to collect a fairer sample."]),
    ST("05", "EXPLAIN"),
    DEF("`Numerical` data are numbers; they are `discrete` if the values are counted "
        "and `continuous` if they are measured. `Categorical` data are names or labels. "
        "A `population` is the whole group of interest and a `sample` is the part "
        "measured; a sample is `biased` if it does not represent the population."),
    KEY("**Good data collection**\n\u2022 Ask one unambiguous question.\n\u2022 Use a "
        "consistent unit and record it.\n\u2022 Include every value, including zeros "
        "and unusually large ones.\n\u2022 State the size of the sample and how it was "
        "chosen.", "Four rules that prevent most errors"),
    WE("11.1.1", "Classifying variables",
       "Classify each variable: (a) shoe size, (b) time to run 100 m, (c) favourite "
       "colour, (d) number of siblings.",
       ["(a) Shoe size is numerical and discrete: sizes are counted in fixed steps.",
        "(b) Time is numerical and continuous: it can take any value, limited only by "
        "the stopwatch.",
        "(c) Favourite colour is categorical: the values are names.",
        "(d) Number of siblings is numerical and discrete."],
       "(a) discrete (b) continuous (c) categorical (d) discrete",
       "Ask whether the values are names, counts or measurements."),
    WE("11.1.2", "Recognising a biased sample",
       "A survey asks students in the football club how often they exercise. Explain "
       "why the results will be biased.",
       ["The sample contains only students who already choose to play football.",
        "They are likely to exercise more than the school population as a whole.",
        "The mean from this sample will overestimate the school's exercise "
        "frequency.",
        "A better sample would be chosen at random across all year groups."],
       "The sample is not representative",
       "Bias comes from how the sample was chosen, not from the size of the "
       "numbers."),
    ERR("\u201cMore data is always better data.\u201d A large biased sample is still "
        "biased \u2014 a million responses from a football club tell you about the "
        "football club. Size reduces random variation; it does nothing for bias."),
    PRAC("11.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Classify each variable as numerical or categorical: (a) shoe size "
          "(b) favourite colour (c) number of siblings.", "F"),
        Q("State whether each is discrete or continuous: (a) mass in grams (b) number "
          "of cars in a car park.", "F"),
        Q("Write one question that would collect data about how students travel to "
          "school.", "F"),
        Q("Explain why \u201cHow tall are you?\u201d can produce unusable data.", "F"),
        Q("Why should zeros be included when recording the number of pets a student "
          "owns?", "F"),
        Q("A survey asks shoppers in a sports shop how often they exercise. Explain "
          "the bias.", "P"),
        Q("Give one reason a sample of 30 students from one class might not represent "
          "a school of 900.", "P"),
        Q("A student records heights to the nearest metre: 1 m, 2 m, 2 m. Explain what "
          "has gone wrong and how to fix it.", "R"),
        Q("Describe how to choose a sample of 40 students from a school of 900 so that "
          "it is representative.", "P"),
        Q("A website asks visitors to rate a product. Explain two reasons the results "
          "may be unreliable.", "E"),
        Q("Design a short data-collection plan for measuring the time students spend on "
          "homework, including the question, the unit and the sample.", "E"),
        Q("Explain the difference between a population and a sample, using an example "
          "of each.", "E"),
    ]),

    # ------------------------------------------------------------------ 11.2
    S("11.2", "Averages and range", "A \u00b7 II  \u00b7  C \u00b7 III",
      ["Patterns", "Measurement"]),
    L("An average is a single number standing in for a set. There are three of them, "
      "and they disagree in useful ways."),
    PHOTO("ch11_screen.jpg", 0.75,
          "A spreadsheet of readings and its summary charts. The summary is a choice, "
          "and a different choice gives a different story.",
          "Photograph: Pexels, free licence (see the image register).", 0.66),
    DIAG(150, "mean_balance",
         "The mean as a balance point: the distances of the values above it counter the "
         "distances below."),
    KEY("**Mean** = sum of values \u00f7 number of values.\n**Median** = the middle "
        "value of an ordered list; with an even count, the mean of the two middle "
        "values.\n**Mode** = the most frequent value (there may be none or "
        "several).\n**Range** = largest \u2212 smallest."),
    WE("11.2.1", "All four summaries",
       "Find the mean, median, mode and range of 4, 7, 7, 9, 13.",
       ["Sum = 40 and there are 5 values, so the mean is 40 \u00f7 5 = 8.",
        "The ordered list has middle value 7, so the median is 7.",
        "7 occurs twice, more than any other, so the mode is 7.",
        "Range = 13 \u2212 4 = 9.",
        "Check the mean by balance: 4 and 13 are 4 and 5 away from 8; 7, 7, 9 are 1 "
        "each side; the total below equals the total above."],
       "mean 8, median 7, mode 7, range 9",
       "Order the list before finding the median, and count the values carefully."),
    WE("11.2.2", "An even number of values",
       "Find the median of 3, 5, 8, 10, 12, 15.",
       ["There are six values, so there is no single middle value.",
        "The two middle values are the 3rd and 4th: 8 and 10.",
        "The median is their mean: (8 + 10) \u00f7 2 = 9.",
        "Check that three values lie below 9 and three above."],
       "9",
       "With an even count the median may not be a value in the list at all."),
    WE("11.2.3", "Mean from a frequency table",
       "Find the mean of the data in the table.",
       ["Multiply each value by its frequency: 1\u00d74 = 4, 2\u00d76 = 12, 3\u00d79 = "
        "27, 4\u00d75 = 20, 5\u00d71 = 5.",
        "\u03a3`fx` = 68 and \u03a3`f` = 25.",
        "Mean = 68 \u00f7 25 = 2.72.",
        "Check the median instead: the 13th value lies in the group with value 3, so "
        "the median is 3."],
       "2.72",
       "Divide by the total frequency, not by the number of rows."),
    ERR("\u201cThe mean of 2, 3, 3, 4 and 48 is about 4, so the typist's speed is "
        "about 4.\u201d The mean is 12, dragged up by the value 48. The median, 3, "
        "describes the typical value far better. An extreme value is an `outlier`, and "
        "it affects the mean much more than the median."),
    PRAC("11.2", "SUPPORT 1\u20135  \u00b7  CORE 6\u201310  \u00b7  EXTENSION "
                "11\u201313", [
        Q("Find the mean, median, mode and range of 4, 7, 7, 9, 13.", "F"),
        Q("Find the mean, median, mode and range of 12, 15, 11, 14, 13.", "F"),
        Q("Find the median of 3, 5, 8, 10, 12, 15.", "F"),
        Q("Find the range of 20, 31, 45, 27.", "F"),
        Q("Find the mean of 2, 3, 3, 4 and 48, and the median. Which is more typical?",
          "F"),
        Q("Find the mean from the frequency table: value 1 (frequency 4), 2 (6), 3 (9), "
          "4 (5), 5 (1).", "P"),
        Q("Five numbers have mean 7. Four of them are 6, 8, 5 and 9. Find the "
          "fifth.", "P"),
        Q("Find the median and mode of 5, 8, 5, 9, 12, 5, 7.", "P"),
        Q("A data set is 3, 4, 4, 5, 6. Add the value 40 and recalculate the mean and "
          "median. Describe what changed.", "R"),
        Q("Class A has 20 students with mean score 60; class B has 30 students with "
          "mean score 70. Find the mean score of all 50 students.", "E"),
        Q("A cyclist's times for five laps are 42, 45, 44, 46 and 48 seconds. Find the "
          "mean, and the time needed on a sixth lap for the mean to be 45 seconds.",
          "E"),
        Q("Explain why the median is often preferred to the mean for house prices.",
          "E"),
    ]),

    # ------------------------------------------------------------------ 11.3
    S("11.3", "Displaying data", "C \u00b7 II  \u00b7  A \u00b7 II", ["Patterns",
      "Representation"]),
    L("A display is chosen to make a pattern visible. The wrong display can hide the "
      "pattern the data actually contains."),
    DIAG(158, "bar_frequency",
         "A bar chart for the scores on a die. The bars are separated because the "
         "scores are discrete categories."),
    DIAG(140, "dot_plot",
         "A dot plot of a small data set. Each dot is one value, so both the centre and "
         "the spread can be read at once."),
    DIAG(158, "frequency_table",
         "A frequency table. It is the first step towards every display: the counts "
         "must be correct before anything is drawn."),
    TABLE(["Display", "Best for", "Watch out for"], [
        ["Bar chart", "comparing counts in categories", "bars must have equal width "
         "and be separated"],
        ["Dot plot", "small numerical sets; spotting clusters", "each dot must "
         "represent exactly one value"],
        ["Histogram", "continuous data in classes", "bars touch, because the classes "
         "are continuous"],
        ["Box plot", "comparing median and spread of two sets", "it hides the shape of "
         "the data"],
    ], widths=[0.85, 1.55, 1.6], fs=8.6),
    WE("11.3.1", "From table to bar chart",
       "The table gives the number of students choosing each subject. Describe the "
       "chart you would draw and the scale you would use.",
       ["The variable is categorical, so a bar chart with separated bars is "
        "appropriate.",
        "The frequencies run from 6 to 18, so a vertical scale of 0 to 20 in steps of "
        "2 fits comfortably.",
        "Bars should be of equal width, with the subject names on the horizontal "
        "axis.",
        "The axis must start at zero, otherwise the comparison of lengths is "
        "misleading."],
       "A bar chart, 0\u201320 in steps of 2",
       "Starting a bar axis above zero exaggerates differences."),
    WE("11.3.2", "Reading a dot plot",
       "A dot plot shows 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 9. Find the median and "
       "describe the shape.",
       ["There are 13 values, so the median is the 7th value.",
        "Counting the dots: 3, then two 4s (3rd), three 5s (6th), so the 7th is the "
        "first 6.",
        "The median is 6.",
        "The dots are clustered around 5\u20137 with single values at 3 and 9, so the "
        "distribution is roughly symmetric with a small spread."],
       "median 6; clustered around 5\u20137",
       "Count the dots cumulatively; do not average the distinct values."),
    WE("11.3.3", "Choosing a display",
       "A student wants to show how the mass of 60 apples is distributed. Which display "
       "should be used, and why?",
       ["Mass is continuous, so the values should be grouped into equal class "
        "intervals.",
        "A histogram is appropriate: the bars touch because neighbouring classes are "
        "continuous.",
        "A bar chart with gaps would wrongly suggest the classes are separate "
        "categories.",
        "The vertical axis shows frequency, so 0 must be included."],
       "A histogram with equal class intervals",
       "Ask whether the variable is continuous before drawing bars."),
    ERR("\u201cI have used two different colours on a bar chart, so the bars need not "
        "have equal width.\u201d Unequal bar widths distort the comparison: readers "
        "compare area, not height. Keep bars equal in width and the gaps equal "
        "too."),
    PRAC("11.3", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Name a display suitable for comparing the number of students in four year "
          "groups.", "F"),
        Q("How many values are shown by a dot plot with dots 3, 4, 4, 5, 5, 5, 6?",
          "F"),
        Q("Why must the vertical axis of a bar chart start at zero?", "F"),
        Q("Which display is suitable for continuous data grouped into classes?", "F"),
        Q("A dot plot shows 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 9. Find the median.",
          "P"),
        Q("Draw a frequency table for the values 2, 3, 3, 4, 4, 4, 5, 5, 6 and state "
          "the mode.", "P"),
        Q("A bar chart shows frequencies 6, 18, 9 and 12 for four subjects. Describe a "
          "suitable scale.", "P"),
        Q("Explain why a histogram's bars touch but a bar chart's do not.", "R"),
        Q("A student draws a bar chart with bars of different widths. Explain the "
          "problem.", "R"),
        Q("Thirty students record the number of hours of sleep. Choose a display and "
          "justify your choice in two sentences.", "E"),
        Q("What information does a box plot show that a bar chart of the same data "
          "cannot?", "E"),
        Q("Describe how a misleading graph could be produced from truthful data, and "
          "how a reader could detect it.", "E"),
    ]),

    # ------------------------------------------------------------------ 11.4
    S("11.4", "Quartiles, spread and comparing groups", "A \u00b7 III  \u00b7  D "
      "\u00b7 IV", ["Patterns", "Measurement"]),
    L("Two groups can share a mean and differ completely. Comparing spread as well as "
      "centre is what makes a comparison honest."),
    DIAG(170, "box_plot_pair",
         "Two box plots compared. The median marks the centre; the box holds the middle "
         "half of the data and the whiskers reach the extremes."),
    DEF("The `lower quartile` (LQ) is the median of the lower half of the data and the "
        "`upper quartile` (UQ) the median of the upper half. The `interquartile range` "
        "(IQR) = UQ \u2212 LQ and measures the spread of the middle half. A `box plot` "
        "shows the smallest value, LQ, median, UQ and largest value."),
    WE("11.4.1", "Quartiles and IQR",
       "Find the median, lower quartile, upper quartile and interquartile range of 3, "
       "5, 6, 8, 9, 11, 12, 14, 15.",
       ["There are 9 values, so the median is the 5th value: 9.",
        "The lower half is 3, 5, 6, 8, whose median is (5 + 6) \u00f7 2 = 5.5.",
        "The upper half is 11, 12, 14, 15, whose median is (12 + 14) \u00f7 2 = "
        "13.",
        "IQR = 13 \u2212 5.5 = 7.5."],
       "median 9, LQ 5.5, UQ 13, IQR 7.5",
       "Do not include the median value itself in either half when the count is "
       "odd."),
    WE("11.4.2", "Comparing two classes",
       "Class A has median 62 and IQR 8; class B has median 66 and IQR 22. Compare the "
       "two classes.",
       ["Class B's median is higher, so its typical score is better.",
        "Class A's IQR is much smaller, so its scores are tightly grouped.",
        "Class B's scores are far more spread out: some are well above and some well "
        "below its median.",
        "A fair statement: B is better on average, but less consistent."],
       "B higher median; A far more consistent",
       "Compare a measure of centre and a measure of spread; one alone is never "
       "enough."),
    WE("11.4.3", "Outliers and the IQR",
       "The data are 12, 14, 15, 16, 18, 19, 21, 45. Find the IQR and state whether 45 "
       "is an outlier by the 1.5 \u00d7 IQR rule.",
       ["Median = (16 + 18) \u00f7 2 = 17.",
        "Lower half 12, 14, 15, 16 has LQ = 14.5; upper half 18, 19, 21, 45 has UQ = "
        "20.",
        "IQR = 20 \u2212 14.5 = 5.5, so 1.5 \u00d7 IQR = 8.25.",
        "The upper boundary is 20 + 8.25 = 28.25, and 45 is above it, so 45 is an "
        "outlier."],
       "IQR 5.5; 45 is an outlier",
       "An outlier should be investigated, not deleted: it may be a mistake or the "
       "most important value."),
    ERR("\u201cBoth groups have the same mean, so they are the same.\u201d 10, 10, 10, "
        "10 and 0, 5, 15, 20 both have mean 10, but one has no spread at all. Always "
        "report a measure of spread alongside the average."),
    PRAC("11.4", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Find the median of 3, 5, 6, 8, 9, 11, 12, 14, 15.", "F"),
        Q("Find the range of 4, 9, 12, 15, 21.", "F"),
        Q("State what the box in a box plot represents.", "F"),
        Q("Find the IQR of 2, 4, 6, 8, 10, 12, 14.", "F"),
        Q("Find the LQ, UQ and IQR of 3, 5, 6, 8, 9, 11, 12, 14, 15.", "P"),
        Q("Class A has median 62 and IQR 8; class B has median 66 and IQR 22. Compare "
          "them.", "P"),
        Q("Find the IQR of 12, 14, 15, 16, 18, 19, 21, 45 and decide whether 45 is an "
          "outlier.", "P"),
        Q("Two data sets both have mean 10. One is 10, 10, 10, 10; the other is 0, 5, "
          "15, 20. Compare their spreads.", "R"),
        Q("A student removes a value of 45 from a data set because it is an outlier. "
          "Give one reason this might be wrong.", "R"),
        Q("Thirty students' test scores have median 70, LQ 60 and UQ 84. Describe the "
          "middle half of the scores and the spread.", "E"),
        Q("Compare two runners' times: runner A 60, 61, 60, 62, 61; runner B 55, 68, "
          "58, 66, 63. Which would you select for a single race, and why?", "E"),
        Q("Explain why the IQR is less affected by outliers than the range.", "E"),
    ]),

    CARD_D("The school survey", [
        ("p", "A school surveys 80 students about the time spent on homework each "
              "week. The results have median 4.5 hours, LQ 3 hours, UQ 6.5 hours, "
              "smallest 1 hour and largest 12 hours."),
        ("ol", ["Draw a box plot of the results and describe the spread.",
                "Calculate the IQR and interpret it in context.",
                "Identify whether 12 hours is an outlier using the 1.5 \u00d7 IQR "
                "rule.",
                "The school proposes a policy limiting homework to 5 hours. Use the "
                "data to predict how many of the 80 students would be affected.",
                "Write one further question you would need answered before supporting "
                "the policy.",
                "Present a recommendation in three sentences, quoting at least two "
                "summary values."]),
    ]),

    # ----------------------------------------------------------- investigate
    ST("06", "INVESTIGATE AND APPLY",
       "Outliers and honest comparison."),
    CARD_I("How one value changes every summary", [
        ("p", "A data set of nine values is 4, 5, 5, 6, 7, 8, 8, 9, 10. A tenth value "
              "is then added."),
        ("ol", ["Calculate the mean, median, mode and range of the original nine "
                "values.",
                "Add the value 40 and recalculate all four summaries.",
                "Record the change in each summary.",
                "Repeat with the value 11 instead of 40, and compare.",
                "Which summary changed least? Which changed most?",
                "Explain, using the way each summary is calculated, why the change "
                "happened.",
                "State one situation where removing an outlier would be honest and one "
                "where it would be dishonest."]),
    ]),
    CARD_I("Reading a display critically", [
        ("p", "Every graph is a choice. This investigation looks at what a graph "
              "decides for the reader."),
        ("ol", ["Find a graph in a news report, advertisement or textbook.",
                "State the variable, the population and the sample size if given.",
                "Describe the scale on each axis, including whether it starts at "
                "zero.",
                "Identify the average used, and whether any spread is shown.",
                "Decide whether the graph overstates or understates its case, and "
                "explain how.",
                "Redraw the graph so that it is not misleading, keeping the data "
                "unchanged.",
                "Write two sentences on what a careful reader should check first."]),
    ]),

    # --------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("11.6", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["Data are numerical (discrete or continuous) or categorical, and the choice "
        "determines the display.",
        "Mean, median and mode each describe a different sense of \u2018typical\u2019; "
        "the range and IQR describe spread.",
        "An outlier moves the mean much more than the median, so the median is safer "
        "for skewed data.",
        "The mean from a frequency table is \u03a3`fx` \u00f7 \u03a3`f`.",
        "Bar charts compare categories and histograms show continuous classes; axes "
        "must start at zero.",
        "Comparing two groups needs a measure of centre and a measure of spread."]),
    VOCAB("**population** \u00b7 **sample** \u00b7 **bias** \u00b7 **discrete** "
          "\u00b7 **continuous** \u00b7 **categorical** \u00b7 **mean** \u00b7 "
          "**median** \u00b7 **mode** \u00b7 **range** \u00b7 **quartile** \u00b7 "
          "**interquartile range** \u00b7 **outlier** \u00b7 **box plot**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["Using the mean for any data set.",
         "One extreme value can distort it; the median is better for skewed data."],
        ["Drawing a bar chart for continuous data.",
         "Continuous classes need a histogram, whose bars touch."],
        ["Starting a bar chart axis at the smallest value.",
         "It exaggerates differences; the axis must start at zero."],
        ["Comparing two groups by their means only.",
         "Two sets can share a mean and have completely different spreads."],
    ], widths=[1.55, 1.95]),
    H("Revision questions"),
    OL(["Find the mean and range of 8, 11, 14, 17, 20.",
        "Find the median of 2, 5, 7, 7, 9, 12.",
        "Find the mean of the frequency table: value 1 (3), 2 (5), 3 (4), 4 (2).",
        "Find the IQR of 5, 7, 8, 10, 12, 14, 15.",
        "Two classes have medians 55 and 58 and IQRs 4 and 15. Write one sentence "
        "comparing them."]),
    GAP(6),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["classify data and spot a biased sample", "\u25a1", "\u25a1", "\u25a1"],
        ["calculate the mean, median, mode and range", "\u25a1", "\u25a1", "\u25a1"],
        ["find a mean from a frequency table", "\u25a1", "\u25a1", "\u25a1"],
        ["choose and construct a suitable display", "\u25a1", "\u25a1", "\u25a1"],
        ["find quartiles and the IQR", "\u25a1", "\u25a1", "\u25a1"],
        ["compare two data sets fairly", "\u25a1", "\u25a1", "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], font_size=8.6),
    GAP(8),
    MYP("**Criterion A:** which summary can you now calculate and interpret without "
        "help?\n"
        "**Criterion B:** what did the outlier investigation show you about "
        "averages?\n"
        "**Criterion C:** was your display readable and correctly scaled?\n"
        "**Criterion D:** how did the data support or weaken your recommendation?",
        "Reflect on the criteria"),
    ATL("In order for a student to report data honestly, students must state the "
        "sample, the summary chosen and the spread, and must not suppress values that "
        "weaken the case.", "ATL \u00b7 Information literacy"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("11.M", "MIXED 1\u201312", [
        Q("Classify the variable \u2018number of goals scored\u2019.", "F"),
        Q("Find the mean of 6, 9, 12, 15, 18.", "F"),
        Q("Find the median of 4, 8, 8, 10, 13, 17.", "F"),
        Q("Find the mode of 3, 5, 5, 6, 8, 8, 8.", "F"),
        Q("Find the range of 14, 22, 9, 31, 18.", "F"),
        Q("Find the mean of the frequency table: value 2 (5), 4 (7), 6 (3).", "P"),
        Q("Find the IQR of 3, 6, 7, 9, 11, 14, 18.", "P"),
        Q("A data set has mean 9 and range 4, and contains six values. Suggest one "
          "possible data set.", "P"),
        Q("A graph shows exam results with the vertical axis starting at 40. Explain "
          "why the graph may mislead.", "R"),
        Q("A class of 24 students has mean height 152 cm; a class of 16 has mean height "
          "160 cm. Find the mean height of all 40 students.", "E"),
        Q("Two shops record daily sales for a week: A 40, 42, 41, 43, 40, 41, 42; B 20, "
          "60, 35, 70, 25, 50, 38. Compare them using an average and a measure of "
          "spread.", "E"),
        Q("Explain, using the formulas, why adding one very large value raises the mean "
          "but may leave the mode unchanged.", "E"),
    ]),
]

ANSWERS = {
    "11.1": ["(a) numerical (b) categorical (c) numerical.",
             "(a) continuous (b) discrete.",
             "For example: \u201cHow do you usually travel to school: walk, cycle, "
             "bus, car or other?\u201d",
             "Answers may be given in different units (feet, inches, metres), so the "
             "values cannot be compared until converted.",
             "A student with no pets would otherwise be left out, which makes the mean "
             "too high.",
             "Shoppers in a sports shop are more likely to exercise than the general "
             "population, so the results overestimate.",
             "One class may differ in age, ability or background from the school as a "
             "whole.",
             "Heights were rounded to the nearest metre, which is far too coarse; "
             "record to the nearest centimetre.",
             "Number every student and use a random number generator to select 40, "
             "keeping the year groups in proportion.",
             "Only people who visit the site respond, and they may be those with the "
             "strongest opinions; the sample is self-selected.",
             "Answers vary; must state the question, the unit, the sample size and how "
             "the sample is chosen.",
             "The population is the whole group of interest, such as all 900 students; "
             "a sample is the part measured, such as 40 of them."],
    "11.2": ["mean 8, median 7, mode 7, range 9.",
             "mean 13, median 13, no mode, range 4.", "9.", "25.",
             "Mean 12, median 3; the median is far more typical because 48 is an "
             "outlier.",
             "2.72.", "7.", "Median 7, mode 5.",
             "The mean rises from 4.4 to 10.33 while the median rises only from 4 to "
             "4.5; the mean is pulled towards the outlier.",
             "66.", "Mean 45 s; a sixth lap of 45 s keeps the mean at 45 s.",
             "A few very expensive houses pull the mean well above the price most "
             "houses actually sell for, while the median stays typical."],
    "11.3": ["A bar chart.", "Seven.", "Otherwise the lengths of the bars do not "
             "represent the values, so differences are exaggerated.",
             "A histogram.", "6.",
             "2 (1), 3 (2), 4 (3), 5 (2), 6 (1); mode 4.",
             "0 to 20 with steps of 2.",
             "A histogram's classes are continuous and adjacent, so bars touch; bar "
             "chart categories are separate, so bars are separated.",
             "Readers compare the area of the bars, so unequal widths distort the "
             "comparison.",
             "A histogram, because sleep time is continuous and can be grouped into "
             "equal class intervals.",
             "A box plot shows the median, the quartiles, the spread and possible "
             "outliers.",
             "For example, by starting the vertical axis above zero or by using "
             "unequal bar widths; a reader should check the scale and the axis "
             "start."],
    "11.4": ["9.", "17.", "The middle half of the data, from LQ to UQ.", "8.",
             "LQ 5.5, UQ 13, IQR 7.5.",
             "B has the higher median but a much larger IQR, so A is more "
             "consistent.",
             "IQR 5.5; upper boundary 28.25, so 45 is an outlier.",
             "The first has no spread; the second has a range of 20, so the same mean "
             "hides very different data.",
             "The value may be genuine and important; removing it changes the evidence "
             "to suit a conclusion.",
             "The middle half of scores lies between 60 and 84, a spread of 24 "
             "marks.",
             "Runner B has the better best time but a far larger spread; for a single "
             "race A is the safer choice.",
             "The IQR ignores the extreme quarters of the data, while the range is "
             "determined entirely by the two extreme values."],
    "11.M": ["Numerical, discrete.", "12.", "9.", "8.", "22.", "3.73.",
             "LQ 6, UQ 14, IQR 8.",
             "For example 7, 8, 9, 9, 10, 11.",
             "Starting at 40 exaggerates differences: a small rise looks like a "
             "doubling.",
             "155.2 cm.",
             "A has mean about 41.3 and range 3; B has mean about 42.6 and range 50. "
             "A is consistent, B is erratic.",
             "The mean divides the total by the count, so one large value adds a lot "
             "to the total; the mode counts frequency, which a single new value may "
             "not change."],
}
