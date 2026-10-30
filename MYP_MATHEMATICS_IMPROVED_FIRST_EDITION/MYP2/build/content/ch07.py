"""Chapter 7 - 2D geometry (Geometry and space)."""
from chbase import *

PLATE = dict(
    part="Part III \u00b7 Geometry and space", part_numeral="III", chapter_no=7,
    kicker="Geometry and space", motif="geometry",
    title_lines=["2D geometry"],
    lead_lines=["Every figure in this chapter obeys a small number of angle",
                "and length facts. Learn to see which fact applies, and the",
                "diagram stops being a puzzle and becomes an argument."],
    key_concept="Relationships", related=["Space", "Measurement"],
    context="Orientation in space and time",
    inquiry_lines=["How do a few angle facts explain the shape of bridges,",
                   "tiles and roofs we walk past every day?"])

TITLE = "2D geometry"
SHORT = "2D geometry"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "From naming shapes to proving what their angles must be."),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "The properties of a two-dimensional figure are consequences of a "
              "small set of relationships, so a measurement you cannot make can "
              "still be deduced."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Relationships.** Angles, sides and areas are linked: "
        "changing one property constrains the others.\n"
        "**Related \u00b7 Space.** Shapes occupy the plane, and their boundaries meet "
        "at points, lines and angles.\n"
        "**Related \u00b7 Measurement.** Perimeter, area and angle size are quantities "
        "we can calculate from structure rather than by measuring."),
    BOX("note", "Global context \u00b7 Orientation in space and time",
        "Exploration: how structures and surfaces around us are shaped by geometry "
        "\u2014 trusses, paving, roofs and screens. Geometry is how a culture fixes a "
        "form so that it can be rebuilt."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** What are the angle facts for a straight line, a point and "
        "parallel lines?",
        "**Conceptual:** Why does the angle sum of a polygon depend only on its "
        "number of sides?",
        "**Debatable:** Is a formula more reliable than a careful measurement?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii",
         "Recall and apply angle, triangle, polygon and circle facts."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate polygon angle sums and tessellation."],
        ["C \u00b7 Communicating", "ii, iii, iv",
         "Give reasons for each step and label diagrams fully."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Cost and plan a paved area with a justified design."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to justify an angle calculation, students must name "
        "the geometric fact used at each step rather than simply stating the answer."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Use angle facts for a straight line, a point and parallel lines.",
         "Find a missing angle and state which fact you used."],
        ["Find angles in triangles and quadrilaterals.",
         "Use the 180\u00b0 and 360\u00b0 sums and the exterior angle result."],
        ["Find interior and exterior angles of polygons.",
         "Use (`n` \u2212 2) \u00d7 180\u00b0 and 360\u00b0 \u00f7 `n` correctly."],
        ["Calculate circumference and area of circles.",
         "Use `C` = 2\u03c0`r` and `A` = \u03c0`r`\u00b2 with units."],
        ["Work with composite shapes.",
         "Split a shape, then find area and perimeter without double counting."],
        ["Explain rather than assert.",
         "Write a two-line reason for every angle you find."],
    ], widths=[1.6, 1.8]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Classify 45\u00b0, 90\u00b0 and 130\u00b0 as acute, right or obtuse.",
               "Calculate \u00a0 180 \u2212 63.",
               "Calculate \u00a0 3 \u00d7 7\u00b2.",
               "Find the perimeter of a rectangle 7 cm by 4 cm.",
               "Find the area of a triangle with base 8 cm and height 5 cm.",
               "Name a quadrilateral with four equal sides and four right angles."]),
    P("If three or more answers are wrong, revisit the angle and area work in "
      "chapter 1 before continuing."),

    # ------------------------------------------------------------------ 7.1
    S("7.1", "Angle relationships and parallel lines", "A \u00b7 I  \u00b7  "
      "C \u00b7 II", ["Space", "Relationships"]),
    L("An angle is a measure of turn between two lines meeting at a point. A handful "
      "of facts about angles then let you find angles you never measured."),
    ST("03", "ENGAGE",
       "Why a bridge is a lattice of triangles."),
    P("Look at the steel truss of a railway bridge. The diagonals divide the span into "
      "triangles, not rectangles. Before reading on, write down one reason a designer "
      "would choose triangles: think about what happens to a rectangle when you push "
      "one corner."),
    PHOTO("ch07_bridge.jpg", 1.30,
          "A steel truss bridge. The diagonals lock each bay into triangles, so the "
          "span keeps its shape under load.",
          "Photograph: Pexels, free to use under the Pexels licence.", 0.72),
    ST("04", "EXPLORE",
       "Measure, then explain."),
    DIAG(200, "parallel_transversal",
         "Two parallel lines cut by a transversal. The eight angles formed fall into "
         "two equal groups, which is why one measurement determines all of them."),
    OL(["Measure every angle marked in the diagram with a protractor and record them "
        "in two groups of equal size.",
        "Which pairs are equal because they are vertically opposite?",
        "Which pairs add to 180\u00b0? Describe where they sit.",
        "Write a conjecture about the angles formed when a transversal cuts two "
        "parallel lines.",
        "Predict the effect on corresponding angles if the two lines were not "
        "parallel.",
        "Explain why a truss of triangles cannot be distorted by pushing on a corner, "
        "while a rectangle can."]),
    ST("05", "EXPLAIN"),
    DEF("Angles on a straight line add to 180\u00b0. Angles at a point add to "
        "360\u00b0. `Vertically opposite` angles are equal. When a transversal cuts "
        "two parallel lines, `corresponding` angles are equal, `alternate` angles are "
        "equal, and `co-interior` angles add to 180\u00b0."),
    TABLE(["Fact", "What it looks like", "What you may write"], [
        ["Straight line", "two angles side by side on a line",
         "`a` + `b` = 180\u00b0"],
        ["At a point", "angles all the way round one vertex",
         "`a` + `b` + `c` = 360\u00b0"],
        ["Vertically opposite", "an X shape", "the two angles are equal"],
        ["Corresponding (parallel)", "same position at each intersection",
         "the two angles are equal"],
        ["Alternate (parallel)", "opposite sides of the transversal, Z shape",
         "the two angles are equal"],
        ["Co-interior (parallel)", "same side of the transversal, C shape",
         "the two angles add to 180\u00b0"],
    ], widths=[1.05, 1.65, 1.5], fs=8.6),
    WE("7.1.1", "Two facts, one answer",
       "Two angles lie on a straight line. One is 118\u00b0. Find the other.",
       ["Angles on a straight line add to 180\u00b0.",
        "So the other angle is 180\u00b0 \u2212 118\u00b0 = 62\u00b0.",
        "Check: 118 + 62 = 180, as required."],
       "62\u00b0",
       "Name the fact before you calculate; it is the first mark in an examination."),
    WE("7.1.2", "Parallel lines",
       "A transversal cuts two parallel lines. One of the co-interior angles is "
       "73\u00b0. Find the alternate angle to the 73\u00b0 angle and the co-interior "
       "angle.",
       ["Co-interior angles add to 180\u00b0, so the other is 180\u00b0 \u2212 73\u00b0 "
        "= 107\u00b0.",
        "The alternate angle equals the 73\u00b0 angle, so it is 73\u00b0.",
        "Check: 73 + 107 = 180, and the alternate angle sits in the Z shape with the "
        "73\u00b0 angle."],
       "Alternate 73\u00b0; co-interior 107\u00b0",
       "Sketch the Z and C shapes; the letters remind you which pair is which."),
    WE("7.1.3", "Angles with algebra",
       "Two angles on a straight line are (3`x` + 10)\u00b0 and (`x` + 30)\u00b0. Find "
       "`x` and both angles.",
       ["Angles on a straight line add to 180\u00b0: (3`x` + 10) + (`x` + 30) = 180.",
        "Collect: 4`x` + 40 = 180, so 4`x` = 140 and `x` = 35.",
        "The angles are 3(35) + 10 = 115\u00b0 and 35 + 30 = 65\u00b0.",
        "Check: 115 + 65 = 180."],
       "`x` = 35; 115\u00b0 and 65\u00b0",
       "Always substitute back: the check catches an algebra slip in one line."),
    ERR("\u201cThe answer is 62\u00b0 because the two angles look equal.\u201d Angles "
        "in a diagram are not drawn to scale, and equal-looking angles may be "
        "supplementary. Every angle must be justified by a named fact, not by "
        "appearance."),
    PRAC("7.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Classify each angle: (a) 38\u00b0  (b) 90\u00b0  (c) 141\u00b0  "
          "(d) 205\u00b0.", "F"),
        Q("Find the complement of 34\u00b0 and the supplement of 34\u00b0.", "F"),
        Q("Two angles on a straight line are 118\u00b0 and `x`\u00b0. Find `x`.", "F"),
        Q("Two lines cross. One angle is 47\u00b0. Write the sizes of the other three "
          "angles at the crossing.", "F"),
        Q("A transversal cuts two parallel lines and one corresponding angle is "
          "72\u00b0. Find the alternate angle and the co-interior angle.", "F"),
        Q("Angles at a point are 130\u00b0, 96\u00b0 and `x`\u00b0. Find `x`.", "P"),
        Q("Two angles on a straight line are (3`x` + 10)\u00b0 and (`x` + 30)\u00b0. "
          "Find `x` and both angles.", "P"),
        Q("Two co-interior angles are 3`x`\u00b0 and (2`x` + 20)\u00b0. Find `x` and "
          "both angles.", "P"),
        Q("A student says two angles of 50\u00b0 and 130\u00b0 must be co-interior. "
          "Is that reasoning valid? Explain.", "R"),
        Q("In a parallelogram, one angle is 68\u00b0. Using parallel-line facts, find "
          "the other three angles and justify each.", "E"),
        Q("Two parallel lines are cut by a transversal. One angle is 5`x`\u00b0 and "
          "the alternate angle is (2`x` + 45)\u00b0. Find `x`.", "E"),
        Q("Explain, using the straight-line fact, why the three angles of a triangle "
          "add to 180\u00b0.", "E"),
    ]),

    # ------------------------------------------------------------------ 7.2
    S("7.2", "Triangles", "A \u00b7 II  \u00b7  C \u00b7 III", ["Space",
      "Generalisation"]),
    L("A triangle is the simplest rigid polygon: fix its three sides and its shape "
      "cannot change. Its angles follow a single rule."),
    DIAG(180, "triangle_angles", None, a=52, b=61),
    P("Draw any triangle, tear off its three corners and place them together along a "
      "straight line: they fit exactly. That experiment is the reason for the angle "
      "sum, and the reason is the straight-line fact from section 7.1."),
    KEY("**Angle sum of a triangle.** The three interior angles of any triangle add "
        "to 180\u00b0.\n**Exterior angle.** An exterior angle of a triangle equals the "
        "sum of the two interior opposite angles.", "Two results worth knowing by name"),
    H("Types of triangle"),
    TABLE(["Name", "Property", "Consequence"], [
        ["Equilateral", "three equal sides", "each angle is 60\u00b0"],
        ["Isosceles", "two equal sides", "the angles opposite them are equal"],
        ["Scalene", "no equal sides", "no equal angles"],
        ["Right-angled", "one angle of 90\u00b0", "the other two add to 90\u00b0"],
    ], widths=[0.9, 1.5, 1.8], fs=8.6),
    WE("7.2.1", "Two angles given",
       "A triangle has angles of 42\u00b0 and 67\u00b0. Find the third angle.",
       ["The angles of a triangle add to 180\u00b0.",
        "Third angle = 180\u00b0 \u2212 42\u00b0 \u2212 67\u00b0 = 71\u00b0.",
        "Check: 42 + 67 + 71 = 180."],
       "71\u00b0",
       "Subtract both known angles in one step to avoid rounding twice."),
    WE("7.2.2", "Isosceles triangle",
       "An isosceles triangle has an apex angle of 44\u00b0. Find the two base angles.",
       ["The base angles are equal because the sides opposite them are equal.",
        "They share 180\u00b0 \u2212 44\u00b0 = 136\u00b0.",
        "Each base angle is 136\u00b0 \u00f7 2 = 68\u00b0.",
        "Check: 44 + 68 + 68 = 180."],
       "68\u00b0 each",
       "Divide after subtracting: the equal pair shares the remainder."),
    WE("7.2.3", "The exterior angle",
       "The exterior angle at one vertex of a triangle is 125\u00b0. One interior "
       "opposite angle is 48\u00b0. Find the other interior opposite angle.",
       ["The exterior angle equals the sum of the two interior opposite angles.",
        "So 125\u00b0 = 48\u00b0 + `y`.",
        "`y` = 125\u00b0 \u2212 48\u00b0 = 77\u00b0.",
        "Check: the third interior angle is 180 \u2212 48 \u2212 77 = 55\u00b0, and "
        "125 + 55 = 180 on a straight line."],
       "77\u00b0",
       "The exterior angle and the adjacent interior angle always add to 180\u00b0."),
    ERR("\u201cThe angles of a triangle are 90\u00b0, 45\u00b0 and 55\u00b0 because "
        "the diagram looks right.\u201d Those three add to 190\u00b0, so no such "
        "triangle exists. Always add your three answers as a check; if the sum is not "
        "180\u00b0, one of them is wrong."),
    PRAC("7.2", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Two angles of a triangle are 58\u00b0 and 71\u00b0. Find the third.", "F"),
        Q("An isosceles triangle has an apex angle of 44\u00b0. Find each base "
          "angle.", "F"),
        Q("What is each angle of an equilateral triangle?", "F"),
        Q("An exterior angle is 125\u00b0 and one interior opposite angle is 48\u00b0. "
          "Find the other.", "F"),
        Q("A triangle has sides 5 cm, 5 cm and 8 cm. Name its type and state which "
          "angles are equal.", "F"),
        Q("The angles of a triangle are 2`x`, 3`x` and 4`x`. Find `x` and the three "
          "angles.", "P"),
        Q("A right-angled triangle has one acute angle of 37\u00b0. Find the other "
          "acute angle.", "P"),
        Q("An isosceles triangle has a base angle of 74\u00b0. Find the apex angle.",
          "P"),
        Q("A student claims a triangle can have angles 100\u00b0, 50\u00b0 and "
          "40\u00b0. Show why this is impossible.", "R"),
        Q("A triangle has angles `x`, 2`x` and 3`x`. Find the angles and classify the "
          "triangle.", "E"),
        Q("The exterior angle at the apex of an isosceles triangle is 130\u00b0. Find "
          "the two base angles.", "E"),
        Q("Explain why a triangle with two right angles cannot exist, using the angle "
          "sum.", "E"),
    ]),

    # ------------------------------------------------------------------ 7.3
    S("7.3", "Quadrilaterals and polygons", "B \u00b7 I  \u00b7  A \u00b7 III",
      ["Patterns", "Generalisation"]),
    L("A polygon's angle sum is fixed by its number of sides. That single relationship "
      "replaces a page of separate facts."),
    DIAG(170, "quadrilateral_row",
         "Families of quadrilaterals. Each shape's angle and side properties follow "
         "from its definition, not from the way it is drawn."),
    TABLE(["Quadrilateral", "Angle fact", "Side fact"], [
        ["Parallelogram", "opposite angles equal; all four add to 360\u00b0",
         "opposite sides equal and parallel"],
        ["Rhombus", "opposite angles equal", "all four sides equal"],
        ["Rectangle", "all four angles 90\u00b0", "opposite sides equal"],
        ["Square", "all four angles 90\u00b0", "all four sides equal"],
        ["Trapezium", "angles add to 360\u00b0", "one pair of parallel sides"],
        ["Kite", "one pair of opposite angles equal", "two pairs of adjacent equal "
         "sides"],
    ], widths=[0.95, 1.75, 1.65], fs=8.4),
    DIAG(190, "polygon_dissection",
         "Dissecting a polygon from one vertex gives `n` \u2212 2 triangles, so its "
         "interior angles sum to (`n` \u2212 2) \u00d7 180\u00b0."),
    KEY("**Interior angle sum** of a polygon with `n` sides: (`n` \u2212 2) \u00d7 "
        "180\u00b0.\n**Exterior angles** of any convex polygon add to 360\u00b0, so "
        "each exterior angle of a regular polygon is 360\u00b0 \u00f7 `n`.\n**Each "
        "interior angle** of a regular polygon is (`n` \u2212 2) \u00d7 180\u00b0 "
        "\u00f7 `n`."),
    WE("7.3.1", "Quadrilateral and pentagon",
       "Find the missing angle of a quadrilateral whose other angles are 85\u00b0, "
       "95\u00b0 and 110\u00b0, then find each interior angle of a regular pentagon.",
       ["A quadrilateral's angles add to 360\u00b0, so the missing angle is 360 "
        "\u2212 85 \u2212 95 \u2212 110 = 70\u00b0.",
        "A pentagon has 5 sides, so its sum is (5 \u2212 2) \u00d7 180 = 540\u00b0.",
        "A regular pentagon divides this equally: 540 \u00f7 5 = 108\u00b0.",
        "Check with the exterior angle: 360 \u00f7 5 = 72, and 180 \u2212 72 = "
        "108\u00b0."],
       "70\u00b0; 108\u00b0",
       "The exterior-angle check works for every regular polygon."),
    WE("7.3.2", "How many sides?",
       "A regular polygon has an exterior angle of 24\u00b0. How many sides does it "
       "have, and what is each interior angle?",
       ["Exterior angles add to 360\u00b0 and are equal in a regular polygon.",
        "Number of sides = 360 \u00f7 24 = 15.",
        "Each interior angle = 180 \u2212 24 = 156\u00b0.",
        "Check: 15 \u00d7 156 = 2340, and (15 \u2212 2) \u00d7 180 = 2340."],
       "15 sides; 156\u00b0",
       "Two independent routes \u2014 exterior angles and the interior sum \u2014 "
       "agreeing is a strong check."),
    WE("7.3.3", "Is it possible?",
       "Can a regular polygon have an interior angle of 130\u00b0?",
       ["If the interior angle were 130\u00b0, the exterior angle would be 50\u00b0.",
        "The number of sides would be 360 \u00f7 50 = 7.2.",
        "A polygon cannot have 7.2 sides, so no such regular polygon exists.",
        "The angle must be one that divides 360 exactly when subtracted from "
        "180\u00b0."],
       "No \u2014 it would need 7.2 sides",
       "Test candidates with the exterior angle; a whole-number result is required."),
    ERR("\u201cA regular polygon with 10 sides has each interior angle 180\u00b0 "
        "\u00f7 10 = 18\u00b0.\u201d That is the exterior angle. Interior and exterior "
        "angles add to 180\u00b0, so the interior angle is 144\u00b0, and 10 \u00d7 "
        "144 = 1440 = (10 \u2212 2) \u00d7 180."),
    PRAC("7.3", "SUPPORT 1\u20135  \u00b7  CORE 6\u201310  \u00b7  EXTENSION "
                "11\u201313", [
        Q("Find the fourth angle of a quadrilateral with angles 85\u00b0, 95\u00b0 and "
          "110\u00b0.", "F"),
        Q("A parallelogram has one angle of 68\u00b0. Find the other three.", "F"),
        Q("Find the interior angle sum of (a) a pentagon  (b) a hexagon  (c) a "
          "decagon.", "F"),
        Q("Find each interior and exterior angle of a regular hexagon.", "F"),
        Q("Find the interior angle sum of an octagon.", "F"),
        Q("A regular polygon has an exterior angle of 24\u00b0. How many sides does "
          "it have?", "P"),
        Q("Find each interior angle of a regular octagon.", "P"),
        Q("A polygon has an interior angle sum of 1260\u00b0. How many sides?", "P"),
        Q("A regular polygon has an exterior angle of 45\u00b0. Find its number of "
          "sides and each interior angle.", "P"),
        Q("A student says a regular polygon can have an interior angle of 130\u00b0. "
          "Test the claim.", "R"),
        Q("Each interior angle of a regular polygon is 156\u00b0. Find the number of "
          "sides.", "E"),
        Q("Find the interior angle sum of a 20-sided polygon.", "E"),
        Q("Explain why the exterior angles of any convex polygon add to 360\u00b0.",
          "E"),
    ]),

    # ------------------------------------------------------------------ 7.4
    S("7.4", "Circles: circumference and area", "A \u00b7 II  \u00b7  D \u00b7 II",
      ["Measurement", "Models"]),
    L("A circle is fixed by one length \u2014 its radius. Both its boundary and its "
      "interior follow from that single number."),
    DIAG(190, "circle_parts",
         "The parts of a circle. The ratio of circumference to diameter is \u03c0 for "
         "every circle, whatever its size."),
    KEY("**Circumference:** `C` = \u03c0`d` = 2\u03c0`r`.\n**Area:** `A` = "
        "\u03c0`r`\u00b2.\nUse \u03c0 = 3.14 unless the question says otherwise, and "
        "always state the unit: cm, cm\u00b2, m\u00b2."),
    P("The constant \u03c0 is a ratio, not a measurement: for any circle, the distance "
      "round the edge is about 3.14 times the distance across the middle. The area "
      "formula comes from cutting the circle into thin sectors and rearranging them "
      "into a shape close to a parallelogram of base \u03c0`r` and height `r`."),
    WE("7.4.1", "From diameter to area",
       "A circular table top has diameter 1.4 m. Find its circumference and area, "
       "using \u03c0 = 3.14.",
       ["The radius is half the diameter: `r` = 0.7 m.",
        "Circumference = 2\u03c0`r` = 2 \u00d7 3.14 \u00d7 0.7 = 4.396 m.",
        "Area = \u03c0`r`\u00b2 = 3.14 \u00d7 0.7\u00b2 = 3.14 \u00d7 0.49 = 1.5386 "
        "m\u00b2.",
        "State units: circumference in metres, area in square metres."],
       "4.40 m and 1.54 m\u00b2 (2 d.p.)",
       "Square the radius before multiplying by \u03c0; order matters."),
    WE("7.4.2", "A semicircle",
       "A semicircle has radius 6 cm. Find its perimeter and area.",
       ["Area of the full circle is \u03c0 \u00d7 6\u00b2 = 113.04 cm\u00b2; half is "
        "56.52 cm\u00b2.",
        "The curved edge of the semicircle is half the circumference: \u03c0 \u00d7 "
        "6 = 18.84 cm.",
        "The perimeter also includes the straight diameter, 12 cm.",
        "Perimeter = 18.84 + 12 = 30.84 cm."],
       "Area 56.52 cm\u00b2; perimeter 30.84 cm",
       "Perimeter follows the boundary, so the diameter must be included."),
    WE("7.4.3", "Working backwards",
       "A circular flower bed has circumference 31.4 m. Find its radius and area.",
       ["`C` = 2\u03c0`r`, so `r` = `C` \u00f7 (2\u03c0) = 31.4 \u00f7 6.28 = 5 m.",
        "Area = \u03c0`r`\u00b2 = 3.14 \u00d7 25 = 78.5 m\u00b2.",
        "Check: 2 \u00d7 3.14 \u00d7 5 = 31.4, the given circumference."],
       "`r` = 5 m; area 78.5 m\u00b2",
       "Rearranging before substituting avoids arithmetic clutter."),
    ERR("\u201cThe area of a circle of diameter 10 cm is 3.14 \u00d7 10\u00b2 = 314 "
        "cm\u00b2.\u201d The formula needs the radius, not the diameter: with `r` = 5 "
        "the area is 78.5 cm\u00b2. A factor of four error is the classic circle "
        "mistake."),
    PRAC("7.4", "SUPPORT 1\u20135  \u00b7  CORE 6\u201310  \u00b7  EXTENSION "
                "11\u201313", [
        Q("Find the circumference of circles with (a) `r` = 5 cm  (b) `r` = 12 m. Use "
          "\u03c0 = 3.14.", "F"),
        Q("Find the area of circles with (a) `r` = 4 cm  (b) `r` = 10 m.", "F"),
        Q("A circle has diameter 14 cm. Find its circumference and area.", "F"),
        Q("A semicircle has radius 6 cm. Find its perimeter and area.", "F"),
        Q("A circle has area 78.5 cm\u00b2. Find its radius.", "F"),
        Q("A bicycle wheel has diameter 0.7 m. How far does the bicycle travel in 100 "
          "complete turns of the wheel?", "P"),
        Q("A ring has outer radius 10 cm and inner radius 6 cm. Find the area of the "
          "ring.", "P"),
        Q("A quadrant has radius 8 cm. Find its area and its perimeter.", "P"),
        Q("A circle has circumference 62.8 cm. Find its radius and area.", "F"),
        Q("Which is larger: the area of one circle of radius 10 cm, or the total area "
          "of two circles of radius 5 cm? Show the comparison.", "R"),
        Q("A running track consists of a rectangle 60 m by 30 m with a semicircle on "
          "each short side. Find the distance round the track.", "E"),
        Q("A circular pizza of diameter 30 cm is cut into 8 equal sectors. Find the "
          "area of one sector and the length of its curved edge.", "E"),
        Q("Explain why doubling the radius multiplies the area by 4 but the "
          "circumference by only 2.", "E"),
    ]),

    # ------------------------------------------------------------------ 7.5
    S("7.5", "Composite shapes and perimeter", "C \u00b7 I  \u00b7  D \u00b7 III",
      ["Measurement", "Models"]),
    L("Most real surfaces are not one shape. Splitting them into shapes you know is "
      "the core skill; deciding how to split them is the judgement."),
    DIAG(190, "composite_area",
         "A composite shape split into a rectangle and a semicircle. The dashed line "
         "shows one useful split; other splits give the same area."),
    P("Areas add: the area of a composite shape is the sum of the areas of its parts, "
      "provided the parts do not overlap. Perimeters do not add in the same carefree "
      "way, because the boundary of a composite shape excludes the internal dividing "
      "line."),
    WE("7.5.1", "Rectangle and semicircle",
       "A window is a rectangle 80 cm wide and 120 cm high with a semicircle on top. "
       "Find its total area and its perimeter, using \u03c0 = 3.14.",
       ["Rectangle area = 80 \u00d7 120 = 9600 cm\u00b2.",
        "Semicircle radius = 40 cm, so its area = \u03c0 \u00d7 40\u00b2 \u00f7 2 = "
        "2512 cm\u00b2.",
        "Total area = 9600 + 2512 = 12 112 cm\u00b2.",
        "Perimeter = 120 + 80 + 120 + (\u03c0 \u00d7 80 \u00f7 2) = 320 + 125.6 = "
        "445.6 cm."],
       "Area 12 112 cm\u00b2; perimeter 445.6 cm",
       "The top edge of the rectangle is inside the shape, so it is not part of the "
       "perimeter."),
    WE("7.5.2", "Subtracting a shape",
       "A square lawn of side 10 m has a circular pond of diameter 6 m in the middle. "
       "Find the grassed area.",
       ["Lawn area = 10 \u00d7 10 = 100 m\u00b2.",
        "Pond radius = 3 m, so pond area = 3.14 \u00d7 9 = 28.26 m\u00b2.",
        "Grassed area = 100 \u2212 28.26 = 71.74 m\u00b2.",
        "Check that the pond fits inside the square: diameter 6 m < 10 m."],
       "71.74 m\u00b2",
       "Subtracting is splitting with a negative sign; keep the units consistent."),
    WE("7.5.3", "A shape with a missing corner",
       "An L-shaped room is a 6 m by 5 m rectangle with a 2 m by 3 m rectangle removed "
       "from one corner. Find its area and perimeter.",
       ["Whole rectangle area = 6 \u00d7 5 = 30 m\u00b2.",
        "Removed area = 2 \u00d7 3 = 6 m\u00b2, so the room is 24 m\u00b2.",
        "Boundary: 6 + 5 + 4 + 2 + 2 + 3 = 22 m, walking round the L.",
        "Check the boundary by adding only outer edges, skipping the internal lines."],
       "24 m\u00b2; perimeter 22 m",
       "Walk the boundary once, in order, and add each edge as you pass it."),
    ERR("\u201cThe perimeter of the composite shape is the perimeter of the rectangle "
        "plus the circumference of the circle.\u201d Parts of the boundary are "
        "internal, and some circle edges are only partly exposed. Trace the actual "
        "outline of the finished shape before adding anything."),
    PRAC("7.5", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Find the area of a rectangle 8 cm by 5 cm joined to a square of side 4 cm.",
          "F"),
        Q("A shape is a square of side 10 m with a circular hole of diameter 6 m. Find "
          "the remaining area.", "F"),
        Q("Find the area of a right-angled triangle with base 9 cm and height 6 cm.",
          "F"),
        Q("A rectangle 12 cm by 7 cm has a triangle of base 12 cm and height 4 cm on "
          "top. Find the total area.", "F"),
        Q("A window is a rectangle 80 cm by 120 cm with a semicircle on top (radius 40 "
          "cm). Find its total area.", "P"),
        Q("An L-shaped room is a 6 m by 5 m rectangle with a 2 m by 3 m rectangle "
          "removed. Find its area and perimeter.", "P"),
        Q("A running track is a 60 m by 30 m rectangle with a semicircle on each short "
          "side. Find its perimeter.", "P"),
        Q("A circular pond of diameter 8 m sits in a square lawn of side 12 m. Find "
          "the grassed area.", "P"),
        Q("A student adds the perimeters of the two shapes to find the perimeter of a "
          "joined shape. Explain the error.", "R"),
        Q("A flower bed is a semicircle of diameter 10 m attached to a rectangle 10 m "
          "by 4 m. Find its area and perimeter.", "E"),
        Q("A logo is a square of side 8 cm with a quarter circle of radius 8 cm "
          "removed from one corner. Find the remaining area.", "E"),
        Q("A path 1 m wide runs round the outside of a rectangular garden 10 m by 6 m. "
          "Find the area of the path.", "E"),
    ]),

    CARD_D("Paving the courtyard", [
        ("p", "A school courtyard 9 m by 6 m is to be paved. The design must include a "
              "circular planting bed of diameter 3 m and a semicircular seating area "
              "of radius 1.5 m, both inside the courtyard. Paving costs \u00a328 per "
              "square metre."),
        ("ol", ["Calculate the total area of the courtyard.",
                "Calculate the area taken by the planting bed and the seating area, "
                "and the area left to pave.",
                "Find the cost of the paving, to the nearest pound.",
                "The paving slabs are 0.6 m squares. How many slabs are needed, "
                "allowing 10% extra for cutting?",
                "Propose one change to the design that reduces the cost by at least "
                "10%, keeping both circular features.",
                "Justify your change with calculations, and state one assumption you "
                "made."]),
    ]),

    # ----------------------------------------------------------- investigate
    ST("06", "INVESTIGATE AND APPLY",
       "Angle sums and the hexagonal paving."),
    CARD_I("The polygon angle sum", [
        ("p", "The angle sum of a polygon can be found by dissecting it into "
              "triangles from one vertex."),
        ("ol", ["Draw a quadrilateral and one diagonal. How many triangles? What is "
                "the angle sum?",
                "Repeat for a pentagon and a hexagon, drawing all diagonals from one "
                "vertex.",
                "Record your results in a table: sides, triangles, angle sum.",
                "Write the angle sum in terms of `n` and test it on a decagon.",
                "Explain why the number of triangles is always `n` \u2212 2.",
                "A regular polygon has an interior angle of 150\u00b0. Use your rule "
                "to find how many sides it has.",
                "Write one sentence explaining why the rule works for every polygon, "
                "not only the ones you drew."]),
    ]),
    PHOTO("ch07_hexagons.jpg", 1.5,
          "Hexagonal paving. Three 120\u00b0 angles meet at every vertex and total "
          "360\u00b0 exactly, which is why no gap or overlap appears.",
          "Photograph: Pexels, free licence (see the image register)."),
    CARD_I("Why hexagons tile", [
        ("p", "Bees build hexagonal cells and pavements are often laid in hexagons. "
              "The reason is arithmetic, not preference."),
        ("ol", ["Find each interior angle of a regular hexagon.",
                "Three hexagons meet at each vertex. Show that the angles fit exactly "
                "with no gap.",
                "Test a regular pentagon: show that three cannot meet at a point.",
                "Test a regular octagon in the same way.",
                "Which regular polygons tile the plane on their own? Write a "
                "conjecture.",
                "Explain your conjecture using the interior angle formula.",
                "Find one combination of two different regular polygons that also "
                "fits around a point, and show the arithmetic."]),
    ]),

    # --------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("7.6", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["Angles on a straight line add to 180\u00b0; angles at a point add to "
        "360\u00b0; vertically opposite angles are equal.",
        "Parallel lines give equal corresponding and alternate angles; co-interior "
        "angles add to 180\u00b0.",
        "The angles of a triangle add to 180\u00b0, and an exterior angle equals the "
        "sum of the two interior opposite angles.",
        "The interior angles of an `n`-sided polygon add to (`n` \u2212 2) \u00d7 "
        "180\u00b0; exterior angles add to 360\u00b0.",
        "`C` = 2\u03c0`r` and `A` = \u03c0`r`\u00b2; the radius, not the diameter, "
        "belongs in both.",
        "Composite areas add, but perimeters must be traced along the real "
        "boundary."]),
    VOCAB("**acute** \u00b7 **obtuse** \u00b7 **reflex** \u00b7 **vertically "
          "opposite** \u00b7 **corresponding** \u00b7 **alternate** \u00b7 "
          "**co-interior** \u00b7 **isosceles** \u00b7 **exterior angle** \u00b7 "
          "**regular polygon** \u00b7 **circumference** \u00b7 **composite shape**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["Judging angles by appearance.",
         "Diagrams are not to scale; only named facts justify an answer."],
        ["Using the diameter in the area formula.",
         "Area needs the radius; halving the diameter first changes the answer by a "
         "factor of 4."],
        ["Adding perimeters of joined shapes.",
         "Internal edges are not part of the boundary and must be removed."],
        ["Writing 18\u00b0 for a decagon's interior angle.",
         "18\u00b0 is the exterior angle; the interior angle is 144\u00b0."],
    ], widths=[1.5, 2.0]),
    H("Revision questions"),
    OL(["Two angles on a straight line are 4`x`\u00b0 and 2`x`\u00b0. Find `x`.",
        "A triangle has angles 39\u00b0 and 58\u00b0. Find the third.",
        "Find each interior angle of a regular nonagon (9 sides).",
        "A circle has radius 9 cm. Find its area and circumference.",
        "A rectangle 10 m by 4 m has a semicircle of radius 2 m removed from one long "
        "side. Find the remaining area."]),
    GAP(6),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["use the straight-line and point angle facts", "\u25a1", "\u25a1", "\u25a1"],
        ["identify corresponding, alternate and co-interior angles", "\u25a1",
         "\u25a1", "\u25a1"],
        ["find angles in triangles, including isosceles cases", "\u25a1", "\u25a1",
         "\u25a1"],
        ["use the polygon angle formula", "\u25a1", "\u25a1", "\u25a1"],
        ["calculate circumference and area of circles", "\u25a1", "\u25a1", "\u25a1"],
        ["find the area and perimeter of composite shapes", "\u25a1", "\u25a1",
         "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], font_size=8.6),
    GAP(8),
    MYP("**Criterion A:** which facts can you now apply without a prompt?\n"
        "**Criterion B:** what did the polygon dissection let you predict?\n"
        "**Criterion C:** did you name the fact you used at every step?\n"
        "**Criterion D:** where did an area calculation decide a real choice?",
        "Reflect on the criteria"),
    ATL("In order for a student to communicate a geometric argument, students must "
        "label the diagram, name each fact used, and give the reason before the "
        "result.", "ATL \u00b7 Communication skills"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("7.M", "MIXED 1\u201312", [
        Q("Find the supplement of 47\u00b0.", "F"),
        Q("Two angles of a triangle are 63\u00b0 and 44\u00b0. Find the third.", "F"),
        Q("Find the interior angle sum of a heptagon (7 sides).", "F"),
        Q("Find the circumference of a circle of radius 3.5 cm.", "F"),
        Q("Find the area of a circle of diameter 20 cm.", "F"),
        Q("A regular polygon has exterior angle 15\u00b0. How many sides?", "P"),
        Q("An isosceles triangle has apex angle 96\u00b0. Find each base angle.",
          "P"),
        Q("A square of side 9 cm has a quarter circle of radius 9 cm removed. Find the "
          "remaining area.", "P"),
        Q("A student writes \u201ca decagon has interior angle 36\u00b0\u201d. "
          "Correct the error.", "R"),
        Q("A circular mirror of diameter 60 cm is framed with a 5 cm wide wooden rim. "
          "Find the area of the rim.", "E"),
        Q("A regular polygon has each interior angle 140\u00b0. Find the number of "
          "sides and the exterior angle.", "E"),
        Q("Two parallel lines are cut by a transversal. One angle is 3`x` + 12 and its "
          "co-interior partner is 2`x` + 8. Find both angles.", "E"),
    ]),
]

ANSWERS = {
    "7.1": ["(a) acute (b) right (c) obtuse (d) reflex.",
            "Complement 56\u00b0; supplement 146\u00b0.", "62\u00b0.",
            "47\u00b0, 133\u00b0, 133\u00b0.", "Alternate 72\u00b0; co-interior "
            "108\u00b0.", "134\u00b0.", "`x` = 35; 115\u00b0 and 65\u00b0.",
            "`x` = 32; 96\u00b0 and 84\u00b0.",
            "No \u2014 many pairs add to 180\u00b0 without being co-interior; the "
            "reason must be the parallel lines.",
            "112\u00b0, 112\u00b0 and 68\u00b0: adjacent angles on the transversal "
            "are co-interior, opposite angles are equal.",
            "`x` = 15.", "Placing the three angles together along a straight line at "
            "one vertex gives 180\u00b0, because a straight line is 180\u00b0."],
    "7.2": ["51\u00b0.", "68\u00b0 each.", "60\u00b0.", "77\u00b0.",
            "Isosceles; the angles opposite the two 5 cm sides are equal.",
            "`x` = 20; 40\u00b0, 60\u00b0, 80\u00b0.", "53\u00b0.", "32\u00b0.",
            "100 + 50 + 40 = 190 \u2260 180, so no such triangle exists.",
            "30\u00b0, 60\u00b0, 90\u00b0; right-angled.", "65\u00b0 each: the apex "
            "interior angle is 50\u00b0, so the base angles share 130\u00b0.",
            "Two right angles already total 180\u00b0, leaving 0\u00b0 for the third "
            "angle, which is impossible."],
    "7.3": ["70\u00b0.", "112\u00b0, 112\u00b0, 68\u00b0.", "(a) 540\u00b0 "
            "(b) 720\u00b0 (c) 1440\u00b0.",
            "Interior 120\u00b0; exterior 60\u00b0.", "1080\u00b0.", "15 sides.",
            "135\u00b0.", "9 sides.", "8 sides; interior 135\u00b0.",
            "No: the exterior angle would be 50\u00b0 and 360 \u00f7 50 = 7.2, not a "
            "whole number.", "15 sides.", "3240\u00b0.",
            "Walking round the polygon you turn through the exterior angle at each "
            "vertex and return facing the same way, a total turn of 360\u00b0."],
    "7.4": ["(a) 31.4 cm (b) 75.36 m.", "(a) 50.24 cm\u00b2 (b) 314 m\u00b2.",
            "C = 43.96 cm; A = 153.86 cm\u00b2.", "Area 56.52 cm\u00b2; perimeter "
            "30.84 cm.", "5 cm.",
            "C = 2.198 m, so 100 turns cover 219.8 m.",
            "3.14 \u00d7 (10\u00b2 \u2212 6\u00b2) = 200.96 cm\u00b2.",
            "Area 50.24 cm\u00b2; perimeter 28.56 cm.", "`r` = 10 cm; A = 314 "
            "cm\u00b2.",
            "One circle: 314 cm\u00b2 against 2 \u00d7 78.5 = 157 cm\u00b2, so the "
            "single large circle is twice the area.",
            "Two lengths of 60 m plus a full circle of diameter 30 m: 120 + 94.2 = "
            "214.2 m.",
            "Area 88.36 cm\u00b2; curved edge 11.78 cm.",
            "Area depends on `r`\u00b2, so doubling `r` multiplies area by 2\u00b2 = "
            "4, while circumference depends on `r` only."],
    "7.5": ["40 + 16 = 56 cm\u00b2.", "71.74 m\u00b2.", "27 cm\u00b2.", "108 cm\u00b2.",
            "12 112 cm\u00b2.", "24 m\u00b2; perimeter 22 m.",
            "120 + 94.2 = 214.2 m.", "144 \u2212 50.24 = 93.76 m\u00b2.",
            "Internal edges are not part of the outside boundary, so they are counted "
            "twice and must be removed.",
            "Area 40 + 39.25 = 79.25 m\u00b2; perimeter 4 + 10 + 4 + 15.7 = 33.7 m.",
            "64 \u2212 50.24 = 13.76 cm\u00b2.",
            "Outer 12 m by 8 m is 96 m\u00b2; the garden is 60 m\u00b2; so the path is 36 m\u00b2."],
    "7.M": ["133\u00b0.", "73\u00b0.", "900\u00b0.", "21.98 cm.", "314 cm\u00b2.",
            "24 sides.", "42\u00b0 each.", "17.42 cm\u00b2.",
            "The exterior angle is 36\u00b0, so the interior angle is 144\u00b0.",
            "3.14 \u00d7 (35\u00b2 \u2212 30\u00b2) = 1020.5 cm\u00b2.",
            "9 sides; exterior angle 40\u00b0.",
            "5`x` + 20 = 180 gives `x` = 32, so the angles are 108\u00b0 and 72\u00b0."],
}
