"""Chapter 7 - Lines, angles, triangles and constructions."""
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.flow import Spacer, Pager
import diagrams as dg
from helpers import (section, lead, body, h3, lst, panel, atl, we, practice, q, fig,
                     diag, table, note, gap, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
    part="Part IV \u00b7 Describing space and belonging", part_numeral="IV", chapter_no=7,
    kicker="Describing space and belonging",
    title_lines=["Lines, angles, triangles", "and constructions"],
    lead_lines=["A single straight line contains 180\u00b0, and a full turn",
                "contains 360\u00b0. From those two facts, and one statement",
                "about parallel lines, a whole system of shape reasoning",
                "follows."],
    key_concept="Relationships", related=["Space", "System"],
    context="Orientation in space and time",
    inquiry_lines=["How do a few angle facts generate everything that can be known",
                   "about a triangle or a polygon?"])

TITLE = "Lines, angles, triangles and constructions"
SHORT = "Lines, angles and constructions"


def build(bk, p):
    reset_counters(7)
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER"))
    p.add(Spacer(8))
    p.add(DataTable(["Statement of inquiry",
                     "Spatial relationships obey a small number of angle rules, and precise "
                     "constructions let those rules be checked and reproduced in real "
                     "structures."],
                    [], widths=[1, 3.2], font_size=9.2, stripe=False))
    gap(p, 10)
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Relationships.** Each angle fact relates two or "
                     "more angles, which is why a single measurement can determine many "
                     "others.\n"
                     "**Related \u00b7 Space.** Angles describe direction and turn, so the "
                     "same facts appear in roofs, roads and folded paper.\n"
                     "**Related \u00b7 System.** Triangles and polygons are systems: a few "
                     "properties force all the rest."))
    p.add(Panel("note", title="Global context \u00b7 Orientation in space and time",
                text="Exploration: how builders have established square corners and level "
                     "lines without modern instruments, and why the 3\u20134\u20135 triangle "
                     "was used for thousands of years."))
    gap(p, 8)
    h3(p, "Inquiry questions")
    lst(p, ["**Factual:** What are the angle facts for a straight line, a point, parallel "
            "lines and a triangle?",
            "**Conceptual:** Why must the angles of every triangle add to 180\u00b0?",
            "**Debatable:** Is a construction with ruler and compass more convincing than a "
            "measurement with a protractor?"])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Apply angle facts to find unknown angles and justify each step."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate the triangle inequality and the angle sums of polygons."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Draw and label a construction so another student can repeat it."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Design a roof truss and check that it can be built."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 6)
    atl(p, "In order for a student to give a complete reason for an angle calculation, "
           "students must name the fact used at each step rather than only the arithmetic.",
           "ATL \u00b7 Communication skills")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("02", "ENGAGE", "The carpenter's square."))
    body(p, "A carpenter needs a right angle but owns no square. She marks 3 units along "
            "one edge, 4 along the other, and adjusts until the distance between the marks "
            "is exactly 5. The corner is now square. She is using a fact about triangles "
            "that was known in Egypt long before it was proved.")
    fig(p, "ch07_plate_banner.jpg",
        "Roof trusses are triangles for a reason: a triangle cannot change shape without a "
        "side changing length, which is why it carries load so reliably.", wide=True)

    p.add(Stage("03", "EXPLORE", "Tear the corners off."))
    body(p, "Draw three different triangles on paper: one acute, one with a right angle and "
            "one obtuse. Measure every angle with a protractor and record the three sums.")
    lst(p, ["What do the three sums have in common?",
            "Tear the corners off one triangle and place them together along a straight "
            "edge. What do you notice?",
            "Repeat with a quadrilateral. What is the sum, and how does it relate to the "
            "triangle result?",
            "Could a triangle have two obtuse angles? Explain using the sum."], ordered=True)
    diag(p, 116, dg.triangle_tear, "The three angles of a triangle rearrange to form a "
                                   "straight line, which is why their sum is 180\u00b0.",
         wide=True)
    panel(p, "keyidea", title="The first big result",
          text="The angles of any triangle add to 180\u00b0. Every other triangle fact in "
               "this chapter follows from it, and it follows in turn from the fact that "
               "angles on a straight line add to 180\u00b0 together with the parallel-line "
               "facts.")

    # --------------------------------------------------------------- 7.1
    section(p, "7.1", "Lines, angles and angle facts", "A \u00b7 i  \u00b7  C \u00b7 iii",
            ["Space", "System"])
    panel(p, "definition", title="Angle vocabulary",
          text="An **acute** angle is less than 90\u00b0; a **right** angle is exactly "
               "90\u00b0; an **obtuse** angle is between 90\u00b0 and 180\u00b0; a "
               "**straight** angle is 180\u00b0 and a **reflex** angle is between 180\u00b0 "
               "and 360\u00b0. Two angles that add to 90\u00b0 are **complementary**; two "
               "that add to 180\u00b0 are **supplementary**.")
    diag(p, 92, dg.angle_types, "The angle families, drawn on the same baseline.", wide=True)
    h3(p, "The facts you will use")
    table(p, ["Fact", "Statement", "Why it is true"], [
        ["Straight line", "Angles on a straight line add to 180\u00b0.",
         "A half turn is 180\u00b0."],
        ["Point", "Angles at a point add to 360\u00b0.", "A full turn is 360\u00b0."],
        ["Vertically opposite", "Angles opposite each other at a crossing are equal.",
         "Each is supplementary to the same angle."],
        ["Corresponding", "Angles in the same position at each crossing of parallel lines "
                           "are equal.", "A translation maps one onto the other."],
        ["Alternate", "Angles on opposite sides of the transversal, between the parallels, "
                       "are equal.", "Follows from corresponding angles and vertically "
                       "opposite angles."],
        ["Co-interior", "Angles between the parallels on the same side add to 180\u00b0.",
         "They are supplementary."],
    ], widths=[0.85, 1.75, 1.3], fs=7.8)
    diag(p, 96, dg.parallel_lines, "A transversal crossing two parallel lines creates two "
                                   "families of equal angles. Naming the position is what "
                                   "makes the reason precise.", wide=True)
    we(p, "7.1.1", "A straight line and a right angle",
       "Two angles sit on a straight line. One is 118\u00b0. Find the other.",
       ["Angles on a straight line add to 180\u00b0.",
        "180\u00b0 \u2212 118\u00b0 = 62\u00b0.",
        "Check: 118 + 62 = 180."],
       answer="62\u00b0",
       check="The answer is acute, which matches the diagram \u2713")
    we(p, "7.1.2", "Parallel lines",
       "Two parallel lines are crossed by a transversal. One angle is 73\u00b0. Find the "
       "alternate angle, the corresponding angle and the co-interior angle.",
       ["The alternate angle is equal: 73\u00b0.",
        "The corresponding angle is equal: 73\u00b0.",
        "The co-interior angle is supplementary: 180\u00b0 \u2212 73\u00b0 = 107\u00b0.",
        "Each answer should be stated with the reason, not only the number."],
       answer="73\u00b0, 73\u00b0 and 107\u00b0.",
       check="All four angles at a crossing must add to 360\u00b0: 73 + 107 + 73 + 107 = "
             "360 \u2713")
    panel(p, "error", title="Assuming lines are parallel because they look parallel",
          text="The parallel-line facts apply only when the lines are given as parallel, "
               "usually marked with arrows. Without the marking, an equal-looking angle "
               "proves nothing.")
    practice(p, "7.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Classify each angle as acute, right, obtuse or reflex: 45\u00b0, 90\u00b0, "
          "170\u00b0, 210\u00b0.", "F"),
        q("Find the complement of 37\u00b0 and the supplement of 37\u00b0.", "F"),
        q("Two angles on a straight line are 3`x`\u00b0 and 60\u00b0. Find `x`.", "F"),
        q("Angles at a point are 90\u00b0, 120\u00b0 and `y`\u00b0. Find `y`.", "F"),
        q("Explain why vertically opposite angles are equal.", "R"),
        q("A gate brace makes a 65\u00b0 angle with the horizontal. Find the angle it makes "
          "with the vertical post.", "P"),
        q("Two parallel roads are crossed by a straight path at 112\u00b0. Find the "
          "co-interior angle and explain your reasoning.", "P"),
        q("Can two angles on a straight line both be obtuse? Explain.", "E"),
    ])

    # --------------------------------------------------------------- 7.2
    section(p, "7.2", "Parallel lines and triangles", "A \u00b7 ii  \u00b7  B \u00b7 ii",
            ["System", "Space"])
    body(p, "The angle sum of a triangle is not an independent fact: it follows from the "
            "straight-line fact together with the parallel-line facts. Drawing a line "
            "parallel to one side through the opposite vertex makes the proof visible in a "
            "single diagram.")
    diag(p, 120, dg.triangle_parallel_proof, "A line parallel to the base creates alternate "
                                             "angles equal to the base angles, so the three "
                                             "angles of the triangle fill a straight line.",
         wide=True)
    panel(p, "keyidea", title="The reasoning, in three steps",
          text="**1** Draw a line through the top vertex parallel to the base. **2** The two "
               "angles between this line and the sides are alternate to the base angles, so "
               "they equal them. **3** The three angles at the top vertex now sit on a "
               "straight line, so they add to 180\u00b0 \u2014 and those three angles are "
               "the three angles of the triangle.")
    we(p, "7.2.1", "Finding a missing angle",
       "A triangle has angles of 47\u00b0 and 68\u00b0. Find the third angle.",
       ["The three angles add to 180\u00b0.",
        "47 + 68 = 115.",
        "180 \u2212 115 = 65\u00b0."],
       answer="65\u00b0",
       check="47 + 68 + 65 = 180 \u2713")
    we(p, "7.2.2", "An isosceles triangle",
       "An isosceles triangle has two equal angles and a third angle of 40\u00b0. Find the "
       "equal angles.",
       ["The two equal angles share what is left: 180 \u2212 40 = 140\u00b0.",
        "Each is 140 \u00f7 2 = 70\u00b0.",
        "Check that all three are positive and add to 180."],
       answer="70\u00b0 each",
       check="70 + 70 + 40 = 180 \u2713")
    practice(p, "7.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Find the third angle: (a) 60\u00b0 and 50\u00b0 (b) 90\u00b0 and 35\u00b0.", "F"),
        q("A triangle has two equal angles of 55\u00b0. Find the third.", "F"),
        q("Can a triangle have angles 100\u00b0, 50\u00b0 and 40\u00b0? Explain.", "F"),
        q("A right-angled triangle has one angle of 28\u00b0. Find the third.", "F"),
        q("Explain why a triangle cannot have two right angles.", "R"),
        q("A roof triangle has a base angle of 35\u00b0 and is isosceles. Find all three "
          "angles.", "P"),
        q("The angles of a triangle are `x`, 2`x` and 3`x`. Find each angle.", "P"),
        q("An exterior angle of a triangle equals the sum of the two opposite interior "
          "angles. Test this with two examples and explain why it works.", "E"),
    ])

    # --------------------------------------------------------------- 7.3
    section(p, "7.3", "Polygons and their angles", "A \u00b7 iii  \u00b7  B \u00b7 ii",
            ["Pattern", "System"])
    body(p, "Any polygon can be cut into triangles by drawing diagonals from one vertex. A "
            "quadrilateral gives two triangles, a pentagon three, a hexagon four \u2014 and "
            "the pattern is the rule.")
    diag(p, 110, dg.polygon_dissection, "Cutting a polygon from one vertex into triangles "
                                        "gives the angle sum without measuring anything.",
         wide=True)
    panel(p, "definition", title="Angle sum of a polygon",
          text="An `n`-sided polygon can be divided into `n` \u2212 2 triangles from one "
               "vertex, so its interior angles add to (`n` \u2212 2) \u00d7 180\u00b0. For a "
               "quadrilateral this gives 360\u00b0; for a pentagon, 540\u00b0.")
    table(p, ["Polygon", "Sides", "Triangles", "Angle sum"], [
        ["Triangle", "3", "1", "180\u00b0"], ["Quadrilateral", "4", "2", "360\u00b0"],
        ["Pentagon", "5", "3", "540\u00b0"], ["Hexagon", "6", "4", "720\u00b0"],
        ["Octagon", "8", "6", "1 080\u00b0"],
    ], widths=[1.0, 0.6, 0.8, 0.9])
    we(p, "7.3.1", "A regular polygon",
       "Find the interior angle of a regular pentagon.",
       ["Angle sum of a pentagon: (5 \u2212 2) \u00d7 180\u00b0 = 540\u00b0.",
        "A regular pentagon has five equal angles.",
        "540\u00b0 \u00f7 5 = 108\u00b0."],
       answer="108\u00b0",
       check="5 \u00d7 108 = 540 \u2713")
    we(p, "7.3.2", "Working backwards",
       "A regular polygon has an interior angle of 150\u00b0. How many sides has it?",
       ["Let the polygon have `n` sides: (`n` \u2212 2) \u00d7 180\u00b0 must equal 150`n`.",
        "Try values: a 12-sided polygon has angle sum 1 800\u00b0, and 1 800 \u00f7 12 = "
        "150\u00b0.",
        "So the polygon has 12 sides."],
       answer="12 sides (a regular dodecagon).",
       check="(12 \u2212 2) \u00d7 180 = 1 800 and 1 800 \u00f7 12 = 150 \u2713")
    practice(p, "7.3", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Find the angle sum of a quadrilateral and a hexagon.", "F"),
        q("Find the interior angle of a regular hexagon.", "F"),
        q("Three angles of a quadrilateral are 80\u00b0, 95\u00b0 and 100\u00b0. Find the "
          "fourth.", "F"),
        q("Find the interior angle of a regular octagon.", "F"),
        q("Explain why the exterior angles of any polygon add to 360\u00b0.", "R"),
        q("A regular polygon has an interior angle of 140\u00b0. How many sides has it?", "P"),
        q("Explain why a regular pentagon cannot tile a floor, while a square can.", "E"),
        q("Investigate the number of diagonals in an `n`-sided polygon and describe the "
          "pattern.", "E"),
    ])

    # --------------------------------------------------------------- 7.4
    section(p, "7.4", "Constructions with ruler and compass", "C \u00b7 i, iii  \u00b7  D \u00b7 ii",
            ["Space", "System"])
    body(p, "A construction uses only a straight edge and a pair of compasses, with no "
            "measurement. Its value is that every step is justified by a geometric fact, so "
            "the result is exact rather than close.")
    diag(p, 128, dg.constructions, "Three standard constructions: the perpendicular "
                                   "bisector, the angle bisector and a triangle from three "
                                   "sides.", wide=True)
    h3(p, "Constructions you should be able to perform")
    table(p, ["Construction", "Steps", "Justification"], [
        ["Perpendicular bisector of AB",
         "Arcs of equal radius from A and from B, crossing twice; join the crossings.",
         "Every point on the bisector is equidistant from A and B."],
        ["Bisector of an angle",
         "Arc across both arms; equal arcs from those two points; join the vertex to the "
         "crossing.", "The two triangles formed are congruent."],
        ["Triangle from three sides",
         "Draw one side; arcs of the other two lengths from its ends; join the crossing.",
         "Two sides and the included construction fix the triangle."],
        ["Perpendicular at a point on a line",
         "Equal marks either side of the point; equal arcs above; join.",
         "The construction is symmetric about the point."],
    ], widths=[1.0, 1.7, 1.2], fs=7.8)
    panel(p, "error", title="Losing accuracy through a blunt pencil",
          text="In a construction the compass point must sit exactly on the intersection, "
               "and the pencil must be sharp. A 1 mm slip at the first arc can produce a "
               "visibly wrong bisector \u2014 and the geometry will be right even though the "
               "drawing is not.")
    we(p, "7.4.1", "Constructing a triangle",
       "Construct a triangle with sides 6 cm, 5 cm and 4 cm, and check whether a second "
       "triangle with the same sides could be a different shape.",
       ["Draw the 6 cm side as the base.",
        "From one end, draw an arc of radius 5 cm; from the other, an arc of radius 4 cm.",
        "Join each end of the base to the crossing point.",
        "The three sides fix the triangle completely: any other arrangement gives a "
        "congruent triangle."],
       answer="One triangle shape only, up to reflection.",
       check="Measure the three angles; they are determined by the sides \u2713")
    practice(p, "7.4", "SUPPORT 1\u20133  \u00b7  CORE 2\u20136  \u00b7  EXTENSION 5\u20137", [
        q("Construct a triangle with sides 5 cm, 5 cm and 7 cm. Measure its angles.", "F"),
        q("Construct the perpendicular bisector of a 7 cm segment and check that every "
          "point on it is equidistant from the ends.", "F"),
        q("Bisect an angle of about 70\u00b0 and check both halves with a protractor.", "F"),
        q("Construct a triangle with sides 3 cm, 4 cm and 5 cm. What do you notice about "
          "one angle?", "R"),
        q("Explain why the construction of a perpendicular bisector works, using congruent "
          "triangles.", "R"),
        q("Plan a construction to draw an angle of exactly 60\u00b0 without a protractor, "
          "and carry it out.", "P"),
        q("Investigate whether a triangle can be constructed with sides 2 cm, 3 cm and 7 cm. "
          "Explain what happens.", "E"),
        q("Construct an equilateral triangle of side 4 cm with compasses only.", "F"),
        q("Construct the perpendicular bisector of a 6 cm segment and measure the distance "
          "from a point on it to each end.", "F"),
        q("Explain in one sentence why a construction needs no measuring.", "R"),
        q("Construct a 45\u00b0 angle by bisecting a right angle, and check it with a "
          "protractor.", "P"),
    ])

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("04", "INVESTIGATE"))
    section(p, "Investigation 7", "The triangle inequality", None, ["Space", "System"])
    body(p, "Cut straws or strips into lengths of 2, 3, 4, 5, 6 and 8 units. Try to form a "
            "triangle from each triple. Record which triples work and which fail, then look "
            "for the rule.")
    table(p, ["Lengths", "Triangle possible?", "Reason"], [
        ["2, 3, 4", "yes", "\u2026"], ["2, 3, 5", "\u2026", "\u2026"],
        ["2, 3, 7", "no", "\u2026"], ["3, 4, 5", "yes", "\u2026"],
        ["4, 5, 8", "yes", "\u2026"], ["5, 5, 10", "\u2026", "\u2026"],
    ], widths=[0.8, 1.0, 1.6])
    h3(p, "Your investigation")
    lst(p, ["Complete the table.",
            "For each failing triple, add the two shorter lengths and compare with the "
            "longest.",
            "Write the rule as a sentence about the three sides.",
            "Test the rule on 4, 7, 11 and on 4, 7, 12.",
            "Explain why the rule must hold: what happens to the two shorter sides as the "
            "angle between them opens?"], ordered=True)
    panel(p, "keyidea", title="The triangle inequality",
          text="A triangle can be made from three lengths exactly when the sum of any two is "
               "greater than the third. If two sides just reach the third, the triangle "
               "collapses into a straight line; if they fall short, they cannot meet.")
    atl(p, "In order for a student to generalise from physical trials, students must record "
           "the boundary cases, because the rule is revealed where a figure just succeeds or "
           "just fails.", "ATL \u00b7 Critical thinking")
    gap(p, 8)
    p.add(Stage("05", "APPLY"))
    section(p, "Real-life application", "The roof-truss workshop", "D \u00b7 i\u2013iv",
            ["Space", "Model"])
    body(p, "A workshop is building a triangular roof truss with a horizontal span of 8 m. "
            "The two sloping rafters are equal in length and meet at 100\u00b0 at the apex. "
            "The workshop needs the base angles and the rafter length.")
    h3(p, "Your task")
    lst(p, ["Sketch the truss and mark the known angle.",
            "Find the two base angles, stating the triangle fact you used.",
            "Draw the truss to scale, 1 cm to 1 m, and measure the rafter length.",
            "Explain why the truss must be a triangle rather than a quadrilateral for "
            "strength.",
            "Calculate the total length of timber needed for the two rafters and the span, "
            "and add 10 % wastage.",
            "State one assumption your model makes."], ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Identify the given and required quantities.",
                 "Select angle facts and scale drawing as strategies.",
                 "Apply them and convert units consistently.",
                 "Justify the wastage allowance and evaluate the assumptions."])
    p.break_page()
    p.add(Stage("06", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "The geometry guide", "C \u00b7 i\u2013iv  \u00b7  A \u00b7 i, ii", [])
    body(p, "**Context.** A younger class is about to learn angle facts and keeps confusing "
            "alternate with corresponding angles. Produce a one-page guide that makes the "
            "distinction obvious.")
    lst(p, ["Draw one diagram containing both pairs and shade them differently.",
            "State each fact in words, using the shaded diagram as the reference.",
            "Give one worked example per fact, with the reason named.",
            "Add a warning about assuming lines are parallel.",
            "Test the guide on a classmate: give them an unseen diagram and see whether they "
            "name the correct fact.",
            "Evaluate: what did the diagram make easy, and what did it hide?"],
        ordered=True)
    criteria_panel(p, a="i, ii: correct statements and calculations.",
                   c="i\u2013iv: notation, diagram clarity and audience awareness.")
    diag(p, 118, dg.guide_layout, "How the guide might be laid out: one diagram of the "
                                  "pair being distinguished, then a short fact and a "
                                  "warning in words.", wide=True)

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("07", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, ["Angles on a straight line add to 180\u00b0; angles at a point add to 360\u00b0.",
            "Parallel lines create equal corresponding and alternate angles, and "
            "supplementary co-interior angles.",
            "The angles of every triangle add to 180\u00b0, and this follows from the earlier "
            "facts.",
            "The interior angles of an `n`-sided polygon add to (`n` \u2212 2) \u00d7 "
            "180\u00b0.",
            "Ruler-and-compass constructions are exact because each step is justified."])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["acute / obtuse / reflex", "Less than 90\u00b0 / between 90\u00b0 and 180\u00b0 / "
                                    "between 180\u00b0 and 360\u00b0."],
        ["complementary / supplementary", "Adding to 90\u00b0 / adding to 180\u00b0."],
        ["transversal", "A line crossing two or more other lines."],
        ["alternate angles", "Equal angles on opposite sides of a transversal."],
        ["corresponding angles", "Equal angles in matching positions."],
        ["co-interior angles", "Angles between parallels on the same side, adding to "
                               "180\u00b0."],
        ["bisector", "A line dividing an angle or segment into two equal parts."],
    ], widths=[1.0, 2.2])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that persist", items=[
        "**Lines that look parallel are parallel.** Only the marking justifies the facts.",
        "**All triangles have a 60\u00b0 angle.** Only equilateral triangles do.",
        "**A bigger triangle has a bigger angle sum.** The sum is 180\u00b0 at every size.",
    ])
    assessment_close(p, [
            ["use straight-line and point facts", "\u25a1", "\u25a1", "\u25a1"],
            ["identify parallel-line angle pairs", "\u25a1", "\u25a1", "\u25a1"],
            ["find missing angles in a triangle", "\u25a1", "\u25a1", "\u25a1"],
            ["find the angle sum of a polygon", "\u25a1", "\u25a1", "\u25a1"],
            ["carry out the standard constructions", "\u25a1", "\u25a1", "\u25a1"],
            ["give a reason for each step", "\u25a1", "\u25a1", "\u25a1"],
        
    ],
        "In order for a student to give a complete answer, students must write the "
               "reason beside each calculated angle, even when the arithmetic was obvious.",
        next_title="Chapter 8 · Sets and classification")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("08", "MIXED PRACTICE"))
    practice(p, "Mixed practice 7",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201311  \u00b7  EXTENSION 9\u201314", [
        q("Find the supplement of 63\u00b0 and the complement of 28\u00b0.", "F"),
        q("Two angles on a straight line are 45\u00b0 and `a`\u00b0. Find `a`.", "F"),
        q("Find the third angle of a triangle with 72\u00b0 and 39\u00b0.", "F"),
        q("Find the interior angle of a regular hexagon.", "F"),
        q("A quadrilateral has angles 90\u00b0, 90\u00b0 and 120\u00b0. Find the fourth.",
          "F"),
        q("Explain the difference between alternate and corresponding angles.", "R"),
        q("Can a triangle have angles of 30\u00b0, 45\u00b0 and 115\u00b0? Explain.", "R"),
        q("A ladder makes a 70\u00b0 angle with the ground. Find the angle it makes with a "
          "vertical wall.", "P"),
        q("The angles of a pentagon are 100\u00b0, 110\u00b0, 120\u00b0, 130\u00b0 and "
          "`x`\u00b0. Find `x`.", "P"),
        q("Explain why the exterior angles of any polygon add to 360\u00b0, using a "
          "square-walking argument.", "R"),
        q("Construct an angle of 90\u00b0 at the end of a 6 cm segment, using only a ruler "
          "and compasses, and describe each step.", "P"),
        q("A regular polygon has an exterior angle of 24\u00b0. How many sides has it?", "E"),
        q("Investigate whether a triangle can be cut into two triangles each with the same "
          "angle sum, and explain the result.", "E"),
        q("Design a truss with a span of 6 m and a height of 2 m. Find the rafter length to "
          "one decimal place and check it satisfies the triangle inequality.", "E"),
    ])
    gap(p, 8)
    p.add(Stage("09", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20135", "Revisit 7.1 to 7.3: name the fact before calculating."],
        ["6\u20137", "Revisit 7.2: draw the parallel line through the vertex."],
        ["8\u201310", "Revisit 7.4 and the investigation: boundary cases reveal the rule."],
        ["11\u201314", "Revisit the key idea on constructions and the polygon pattern."],
    ], widths=[0.7, 2.6])


ANSWERS = [
    ("7.1", "1 Acute, right, obtuse, reflex.  2 53\u00b0; 143\u00b0.  3 `x` = 40.  "
            "4 `y` = 150.  6 25\u00b0.  7 68\u00b0 (co-interior)."),
    ("7.2", "1 (a) 70\u00b0 (b) 55\u00b0.  2 70\u00b0.  3 No: the sum is 190\u00b0.  "
            "4 62\u00b0.  6 35\u00b0, 72.5\u00b0, 72.5\u00b0.  7 30\u00b0, 60\u00b0, "
            "90\u00b0."),
    ("7.3", "1 360\u00b0; 720\u00b0.  2 120\u00b0.  3 85\u00b0.  4 135\u00b0.  "
            "6 9 sides.  8 `n`(`n` \u2212 3)/2."),
    ("7.4", "1 Base angles 45.6\u00b0 each, apex 88.8\u00b0 (to 1 d.p.).  2 Every point "
            "on the bisector is the same distance from both ends of the segment.  3 About "
            "35\u00b0 each.  4 A right angle: 5^{2} = 3^{2} + 4^{2}.  6 Construct an "
            "equilateral triangle on any segment; each angle is 60\u00b0.  7 Impossible: "
            "2 + 3 < 7, so the two short sides cannot meet."),
    ("Investigation 7", "2, 3, 5 fail (they form a straight line); 2, 3, 7 fail; 5, 5, 10 "
                        "fail; 4, 7, 12 fail. A triangle needs the sum of any two sides to "
                        "exceed the third."),
    ("Mixed 7", "1 117\u00b0; 62\u00b0.  2 135.  3 69\u00b0.  4 120\u00b0.  5 60\u00b0.  "
                "7 No: the sum is 190\u00b0.  8 20\u00b0.  9 80\u00b0.  12 15 sides.  "
                "14 Rafter = \u221a(3^{2} + 2^{2}) \u2248 3.6 m; 3.6 + 3.6 > 6."),
]
