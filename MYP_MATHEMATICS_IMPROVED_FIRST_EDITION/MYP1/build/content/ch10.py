"""Chapter 10 - Data, tables and graphs."""
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.flow import Spacer, Pager
import diagrams as dg
from helpers import (section, lead, body, h3, lst, panel, atl, we, practice, q, fig,
                     diag, table, note, gap, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
    part="Part V \u00b7 Reading the story in data", part_numeral="V", chapter_no=10,
    kicker="Reading the story in data",
    title_lines=["Data, tables and", "the shape of a graph"],
    lead_lines=["A table is a set of decisions about what to record. A graph is a",
                "set of decisions about what to show. Neither is neutral, and",
                "both can be read more carefully than they are usually",
                "read."],
    key_concept="Relationships", related=["Representation", "Change"],
    context="Fairness and development",
    inquiry_lines=["How can the same data be displayed so that it tells two different",
                   "stories, and how does a reader tell which one is honest?"])

TITLE = "Data, tables and graphs"
SHORT = "Data, tables and graphs"


def build(bk, p):
    reset_counters(10)
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER"))
    p.add(Spacer(8))
    p.add(DataTable(["Statement of inquiry",
                     "Data becomes evidence only when its collection, summary and display "
                     "are chosen deliberately enough to be examined by someone else."],
                    [], widths=[1, 3.2], font_size=9.2, stripe=False))
    gap(p, 10)
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Relationships.** A graph asserts a relationship "
                     "between quantities; the shape of the graph is the claim.\n"
                     "**Related \u00b7 Representation.** Table, bar chart, dot plot and pie "
                     "chart each hide something and reveal something else.\n"
                     "**Related \u00b7 Change.** A time-series graph is about change, and its "
                     "scale decides whether change looks dramatic."))
    p.add(Panel("note", title="Global context \u00b7 Fairness and development",
                text="Exploration: how statistics about a community are used to argue for "
                     "resources, and what a well-chosen average can conceal about the people "
                     "behind it."))
    gap(p, 8)
    h3(p, "Inquiry questions")
    lst(p, ["**Factual:** What are the mean, median, mode and range, and how is each "
            "calculated?",
            "**Conceptual:** Why can the mean be a misleading summary of a data set?",
            "**Debatable:** When does a graph become a form of persuasion rather than a "
            "report?"])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Calculate and interpret the three averages and the range."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate how one extreme value changes each average."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Choose and justify a display for a given data set."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Report a class survey honestly, including its limitations."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 6)
    atl(p, "In order for a student to read a graph critically, students must check the axes "
           "before reading the shape.", "ATL \u00b7 Media literacy skills")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("02", "ENGAGE", "The best class in the school."))
    body(p, "Two classes compare their test scores. Class A has a mean of 62 % and Class B "
            "a mean of 58 %. Class B claims to be better because it has more students above "
            "70 % and one student scored 100 %. Both claims use the same numbers.")
    fig(p, "ch10_plate_banner.jpg",
        "A canteen ledger: every record is a decision about what to count and how to count "
        "it.", wide=True)

    p.add(Stage("03", "EXPLORE", "Twenty numbers."))
    body(p, "Collect twenty numbers \u2014 shoe sizes, minutes spent on homework, or scores "
            "from a quick quiz. Record them in a table with a tally column.")
    lst(p, ["Which value occurs most often?",
            "Arrange the values in order. Which value sits in the middle?",
            "Add them all and divide by twenty. What do you get?",
            "Which of the three numbers best describes the group, and why?"], ordered=True)
    diag(p, 96, dg.data_table_tally, "A frequency table turns a list into a shape: the "
                                     "tally column is the data, the frequency column is the "
                                     "summary.", wide=True)
    panel(p, "keyidea", title="Three answers to one question",
          text="\u201cWhat is typical?\u201d has at least three mathematical answers: the "
               "mode (most common), the median (middle in order) and the mean (share out "
               "equally). They answer different questions and can disagree.")

    # --------------------------------------------------------------- 10.1
    section(p, "10.1", "Collecting and organising data", "A \u00b7 i  \u00b7  C \u00b7 i",
            ["Representation", "Relationships"])
    panel(p, "definition", title="Data vocabulary",
          text="**Data** are observations. A **variable** is what is being recorded; it is "
               "**categorical** if it names a group and **numerical** if it is a number. "
               "**Discrete** data can be counted exactly; **continuous** data are measured "
               "and depend on the accuracy of the instrument.")
    table(p, ["Question", "Variable", "Type"], [
        ["What is your favourite subject?", "subject", "categorical"],
        ["How many siblings have you?", "number of siblings", "numerical, discrete"],
        ["How tall are you?", "height", "numerical, continuous"],
        ["How do you travel to school?", "mode of travel", "categorical"],
    ], widths=[1.5, 1.1, 1.2], fs=7.8)
    body(p, "A good survey question has one meaning. \u201cHow much screen time do you "
            "have?\u201d can be answered in hours, minutes, or by device, and the answers "
            "will not be comparable. Before collecting data, decide the unit and the "
            "categories.")
    we(p, "10.1.1", "Building a frequency table",
       "The number of goals scored in twelve matches: 2, 1, 3, 0, 2, 4, 1, 2, 0, 3, 2, 1. "
       "Build a frequency table.",
       ["List the possible values: 0, 1, 2, 3, 4.",
        "Count each: 0 appears twice, 1 three times, 2 four times, 3 twice, 4 once.",
        "Check the frequencies add to 12, the number of matches."],
       answer="0 \u2192 2, 1 \u2192 3, 2 \u2192 4, 3 \u2192 2, 4 \u2192 1",
       check="2 + 3 + 4 + 2 + 1 = 12 \u2713")
    panel(p, "error", title="Losing an observation",
          text="If the frequencies do not add to the number of observations, one entry has "
               "been counted twice or missed. Always check the total before calculating "
               "anything from the table.")
    practice(p, "10.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Classify each variable: eye colour, number of pets, mass, month of birth.", "F"),
        q("Build a frequency table for: 4, 5, 4, 3, 5, 4, 6, 5, 4.", "F"),
        q("Which of these is discrete: shoe size, height, temperature?", "F"),
        q("Write a better version of the question \u201cDo you like sport?\u201d", "F"),
        q("Explain why the unit must be fixed before a survey begins.", "R"),
        q("Design a short survey to find how students travel to school, with at most five "
          "categories.", "P"),
        q("A survey records \u201cabout 2 hours\u201d of homework for several students. "
          "Explain why this weakens the data.", "P"),
        q("Investigate two ways the same question could be worded to produce different "
          "answers, and explain the effect.", "E"),
    ])

    # --------------------------------------------------------------- 10.2
    section(p, "10.2", "Averages and range", "A \u00b7 ii  \u00b7  C \u00b7 ii",
            ["Quantity", "Change"])
    panel(p, "definition", title="Mean, median, mode and range",
          text="**Mean** = total \u00f7 number of values. **Median** = the middle value of "
               "the ordered list. **Mode** = the most frequent value. **Range** = largest "
               "\u2212 smallest, a measure of spread, not of average.")
    diag(p, 108, dg.averages_compare, "Five values, summarised three ways. Each marker sits at a "
                                       "different number, and each number answers a "
                                       "different question.", wide=True)
    we(p, "10.2.1", "All three averages",
       "Find the mean, median and mode of 4, 7, 7, 9, 13.",
       ["Mean: (4 + 7 + 7 + 9 + 13) \u00f7 5 = 40 \u00f7 5 = 8.",
        "Median: the ordered list is unchanged; the middle value is 7.",
        "Mode: 7 appears twice, more than any other value.",
        "Range: 13 \u2212 4 = 9."],
       answer="Mean 8, median 7, mode 7, range 9.",
       check="The mean is larger than the median because 13 pulls it upward \u2713")
    we(p, "10.2.2", "An even number of values",
       "Find the median of 3, 5, 8, 10, 12, 15.",
       ["There is no single middle value with six numbers.",
        "The two middle values are 8 and 10.",
        "Median = (8 + 10) \u00f7 2 = 9."],
       answer="9",
       check="Three values lie below 9 and three above \u2713")
    panel(p, "error", title="Taking the median of an unordered list",
          text="The median must be found after ordering. In 10, 2, 6, 4 the middle of the "
               "written list is 6, but the ordered list is 2, 4, 6, 10 and the median is "
               "(4 + 6) \u00f7 2 = 5.")
    practice(p, "10.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Find the mean of 6, 8, 10, 12.", "F"),
        q("Find the median of 3, 9, 4, 7, 5.", "F"),
        q("Find the mode of 2, 3, 3, 5, 7, 3.", "F"),
        q("Find the range of 14, 6, 9, 21, 11.", "F"),
        q("Explain why the median is often used for house prices.", "R"),
        q("A data set has mean 12 and six values. If five are 8, 10, 11, 13 and 15, find "
          "the sixth.", "P"),
        q("Scores: 45, 52, 58, 61, 63, 88. Find all three averages and say which best "
          "represents the group.", "P"),
        q("Investigate: add one very large value to a small data set and describe what "
          "happens to the mean and to the median.", "E"),
    ])

    # --------------------------------------------------------------- 10.3
    section(p, "10.3", "Bar charts, dot plots and pie charts", "C \u00b7 iii  \u00b7  B \u00b7 i",
            ["Representation", "Relationships"])
    body(p, "A display is a decision. A bar chart compares categories, a dot plot shows "
            "every observation and how they cluster, and a pie chart shows each category as "
            "a share of a whole. Choosing the wrong one is not a small mistake: it can make "
            "a comparison invisible.")
    diag(p, 112, dg.barchart_box, "A bar chart of categorical data. The bars are separate "
                              "because the categories are separate.", wide=True,
         args=([("walk", 30), ("bus", 48), ("car", 24), ("cycle", 18)],))
    diag(p, 92, dg.dotplot_box, "A dot plot of the same values shows the shape of the data: "
                            "where it clusters and where it spreads.", wide=True,
         args=([2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7],))
    diag(p, 118, dg.piechart_share, "A pie chart shows shares of one whole. It is the wrong "
                                    "choice when the parts do not add to a meaningful "
                                    "total.", wide=True)
    we(p, "10.3.1", "Reading a pie chart",
       "A pie chart shows 25 % walking, 40 % by bus, 20 % by car and the rest by bicycle. "
       "How many students cycle in a school of 480?",
       ["The four shares must total 100 %: 25 + 40 + 20 = 85, so cycling is 15 %.",
        "15 % of 480 = 0.15 \u00d7 480 = 72.",
        "Check: 120 + 192 + 96 + 72 = 480."],
       answer="72 students",
       check="The four numbers reproduce the whole school \u2713")
    panel(p, "error", title="A pie chart of a total that means nothing",
          text="Pie charts require parts of one whole. A pie chart of \u201cnumber of goals "
               "per player\u201d is meaningless once you realise the goals are not a fixed "
               "total being shared out.")
    practice(p, "10.3", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Which display best compares five categories? Give a reason.", "F"),
        q("A bar chart shows 12, 9, 15 and 6. Find the total.", "F"),
        q("In a pie chart, one sector is 90\u00b0. What percentage is it?", "F"),
        q("Draw a dot plot for 2, 3, 3, 4, 4, 4, 5.", "F"),
        q("Explain why pie charts are unsuitable for data that are not parts of a whole.",
          "R"),
        q("A survey of 200 students shows 30 % prefer cricket, 45 % football and the rest "
          "athletics. Draw a pie chart.", "P"),
        q("The same data are shown once as a bar chart starting at 0 and once starting at "
          "50. Describe the difference in impression.", "E"),
        q("Investigate which display makes a small difference between two groups easiest to "
          "see, using your own data.", "E"),
    ])

    # --------------------------------------------------------------- 10.4
    section(p, "10.4", "Interpreting graphs critically", "C \u00b7 iv  \u00b7  D \u00b7 iv",
            ["Change", "Representation"])
    body(p, "Every graph contains choices: which axis, which scale, where the vertical axis "
            "starts, which summary is quoted. A reader who checks those choices can tell "
            "the difference between a real change and a drawn one.")
    diag(p, 118, dg.misleading_axes, "The same data drawn twice. Left: the vertical axis "
                                     "starts at zero. Right: it starts at 90, and the "
                                     "increase looks enormous.", wide=True)
    h3(p, "Four questions to ask of any graph")
    table(p, ["Check", "What to look for"], [
        ["The axes", "What is on each axis, and in what unit?"],
        ["The scale", "Does the vertical axis start at zero? Are the steps equal?"],
        ["The sample", "How many observations, and who was asked?"],
        ["The summary", "Which average is quoted, and why that one?"],
    ], widths=[0.9, 2.3])
    we(p, "10.4.1", "A misleading claim",
       "A shop advertises \u201caverage customer spending of 45\u201d after recording "
       "spending of 8, 9, 10, 12, 160. Is the claim fair?",
       ["Total = 8 + 9 + 10 + 12 + 160 = 199, so mean = 39.8 \u2014 not 45.",
        "The 160 is an outlier and pulls the mean upward.",
        "The median is 10, which represents four of the five customers far better.",
        "The claim is arithmetically close but statistically misleading."],
       answer="Not fair: the median is 10; the mean is distorted by one outlier.",
       check="Four of five customers spend under 13 \u2713")
    practice(p, "10.4", "SUPPORT 1\u20133  \u00b7  CORE 2\u20136  \u00b7  EXTENSION 5\u20137", [
        q("A graph's vertical axis starts at 100. What effect does this have?", "F"),
        q("Which is affected more by an outlier: the mean or the median?", "F"),
        q("Name one question you should ask about a survey's sample.", "F"),
        q("Explain why \u201caverage\u201d alone is an incomplete statement.", "R"),
        q("Find one misleading graph in a news source and describe the choice that misleads.",
          "P"),
        q("Redraw a misleading graph with a zero axis and describe how the message "
          "changes.", "P"),
        q("Investigate: how many ways can the same five numbers be summarised to support two "
          "opposite conclusions?", "E"),
    ])

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("04", "INVESTIGATE"))
    section(p, "Investigation 10", "What one outlier does", None, ["Change", "Quantity"])
    body(p, "Take the data set 5, 6, 6, 7, 8, 9, 10. Calculate the mean and median. Now add "
            "one extra value of 100 and recalculate. Record everything in a table.")
    table(p, ["Data set", "Mean", "Median", "Range"], [
        ["5, 6, 6, 7, 8, 9, 10", "\u2026", "\u2026", "\u2026"],
        ["with 100 added", "\u2026", "\u2026", "\u2026"],
        ["with 1000 added", "\u2026", "\u2026", "\u2026"],
    ], widths=[1.7, 0.6, 0.7, 0.6])
    h3(p, "Your investigation")
    lst(p, ["Complete the table, showing your working for the means.",
            "Which measure changes most when one value is added?",
            "Which measure changes least?",
            "Write a sentence describing when the median is the better summary.",
            "Give a real example where an outlier is the most important value in the set."],
        ordered=True)
    panel(p, "keyidea", title="The result",
          text="The mean uses every value, so a single extreme value can move it a long way. "
               "The median depends only on position, so it barely moves. Neither is "
               "\u201ccorrect\u201d: the choice depends on what the summary is for.")
    atl(p, "In order for a student to choose a summary, students must ask what decision the "
           "summary will support.", "ATL \u00b7 Critical thinking")
    p.break_page()
    p.add(Stage("05", "APPLY"))
    section(p, "Real-life application", "The school travel survey", "D \u00b7 i\u2013iv",
            ["Representation", "Fairness"])
    body(p, "Your year group is asked how students travel to school, so that the school can "
            "argue for a covered bicycle shelter. You have one week and 120 students to "
            "survey.")
    h3(p, "Your task")
    lst(p, ["Define the categories and the unit before collecting anything.",
            "Collect and tabulate the responses, including a \u201cnot recorded\u201d row.",
            "Choose a display and justify the choice against one alternative.",
            "Calculate one average appropriate to the data and explain why the others are "
            "not.",
            "Write two sentences of findings for the school council, and one limitation of "
            "your evidence.",
            "Explain how a different choice of categories could have changed the "
            "conclusion."], ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Identify the variable, categories and sample.",
                 "Select a display and a summary deliberately.",
                 "Apply them accurately and total the frequencies.",
                 "Evaluate the evidence and state its limits."])
    gap(p, 8)
    p.add(Stage("06", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "The honest infographic", "C \u00b7 i\u2013iv  \u00b7  D \u00b7 iv", [])
    body(p, "**Context.** A community group has one page to show how its after school "
            "programme has changed attendance over five years, and it must not mislead.")
    lst(p, ["Invent five years of attendance figures with a real but modest rise.",
            "Draw the graph twice: once with a zero axis, once with a truncated axis.",
            "Write the caption each version would carry in a leaflet.",
            "Explain which version you would publish and why.",
            "Add one sentence about the size of the sample behind the figures.",
            "Evaluate: is a true graph with a truncated axis still honest?"], ordered=True)
    criteria_panel(p, c="i\u2013iv: axes, labels, scale and caption clarity.",
                   d="ii\u2013iv: choice of display and evaluation of its honesty.")
    diag(p, 104, dg.honest_panel, "The two versions of one data set, side by side, with the "
                                  "claim each one makes.", wide=True)

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("07", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, ["Data are classified by type before they are displayed.",
            "The mean, median and mode answer different versions of \u201ctypical\u201d.",
            "The range describes spread, not average.",
            "Bar charts compare categories, dot plots show shape, pie charts show shares.",
            "A graph's scale and a summary's choice can change the claim it makes."])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["data", "Observations collected for a purpose."],
        ["variable", "The quantity or category being recorded."],
        ["frequency", "How many times a value occurs."],
        ["mean", "Total divided by the number of values."],
        ["median", "The middle value of an ordered list."],
        ["mode", "The most frequent value."],
        ["range", "Largest value minus smallest value."],
        ["outlier", "A value far from the rest of the data."],
    ], widths=[1.0, 2.2])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that persist", items=[
        "**The mean is the typical value.** With an outlier it may describe nobody in the "
        "set.",
        "**The range is an average.** It measures spread, not centre.",
        "**A pie chart suits any data.** It needs parts of one whole.",
    ])
    assessment_close(p, [
            ["build a frequency table", "\u25a1", "\u25a1", "\u25a1"],
            ["calculate mean, median and mode", "\u25a1", "\u25a1", "\u25a1"],
            ["choose an appropriate display", "\u25a1", "\u25a1", "\u25a1"],
            ["read a graph and check its axes", "\u25a1", "\u25a1", "\u25a1"],
            ["explain what a summary conceals", "\u25a1", "\u25a1", "\u25a1"],
            ["report data honestly to an audience", "\u25a1", "\u25a1", "\u25a1"],
        
    ],
        "In order for a student to report data responsibly, students must state what "
               "the data cannot show as clearly as what it can.")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("08", "MIXED PRACTICE"))
    practice(p, "Mixed practice 10",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201311  \u00b7  EXTENSION 9\u201314", [
        q("Find the mean of 7, 9, 11, 13.", "F"),
        q("Find the median of 4, 8, 2, 9, 6.", "F"),
        q("Find the mode of 5, 5, 6, 7, 5, 8.", "F"),
        q("Find the range of 3, 17, 9, 12.", "F"),
        q("Classify the variable \u201cnumber of books read\u201d as discrete or "
          "continuous.", "F"),
        q("Explain why an outlier affects the mean more than the median.", "R"),
        q("A pie chart shows 30 % of 240 students. How many students is that?", "R"),
        q("Scores: 12, 15, 15, 18, 20, 45. Find mean and median and say which better "
          "represents a typical score.", "P"),
        q("A bar chart axis starts at 200 and the bars are 210 and 220. Describe the "
          "impression and how to correct it.", "P"),
        q("A data set of eight values has mean 15. Find the total.", "P"),
        q("Design a frequency table for the letters in MATHEMATICS.", "P"),
        q("A shop claims \u201caverage spend 60\u201d from data 15, 20, 25, 30, 210. "
          "Evaluate the claim.", "E"),
        q("Investigate: construct two data sets with the same mean but different spreads.",
          "E"),
        q("Write a short paragraph advising a student how to read a graph in a news report "
          "critically.", "E"),
    ])
    gap(p, 8)
    p.add(Stage("09", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20135", "Revisit 10.1 and 10.2: type first, then calculate."],
        ["6\u20137", "Revisit 10.3: which display answers which question."],
        ["8\u201311", "Revisit 10.4 and the investigation."],
        ["12\u201314", "Revisit the honest-infographic task and the four checks."],
    ], widths=[0.7, 2.6])
    gap(p, 10)
    panel(p, "keyidea", title="Closing the course",
          text="Nine chapters ago a number was a written symbol. It is now a position, a "
               "power, a factor, a fraction, a percentage, a variable, a length, an area, a "
               "volume and finally a data point \u2014 and each of those is a choice about "
               "what to notice. Mathematics is the discipline of making those choices "
               "explicit enough that someone else can check them.")


ANSWERS = [
    ("10.1", "1 Categorical, discrete, continuous, categorical.  2 3 \u2192 1, 4 \u2192 4, "
             "5 \u2192 3, 6 \u2192 1.  3 Shoe size."),
    ("10.2", "1 9.  2 5.  3 3.  4 15.  6 15.  7 Mean 54.5, median 59.5, mode none; the "
             "median represents the group better because 88 is an outlier."),
    ("10.3", "1 A bar chart.  2 42.  3 25 %.  5 Because the parts must share one whole.  "
             "6 Cricket 108\u00b0, football 162\u00b0, athletics 90\u00b0."),
    ("10.4", "1 It exaggerates small differences.  2 The mean.  3 Who was asked, and how "
             "many."),
    ("Investigation 10", "Mean and median of 5, 6, 6, 7, 8, 9, 10 are 7.29 and 7. With 100: "
                         "mean 18.9, median 7.5. With 1000: mean 130.6, median 7.5. The mean "
                         "changes most; the median barely moves."),
    ("Mixed 10", "1 10.  2 6.  3 5.  4 14.  6 The median depends only on position.  "
                 "7 72 students.  8 Mean 20.8, median 16.5; the median is more "
                 "representative.  10 120.  11 A 2, C 1, E 1, H 1, I 1, M 2, S 1, T 2.  "
                 "12 Mean 60, median 25: the 210 is an outlier, so the claim overstates a "
                 "typical spend."),
]
