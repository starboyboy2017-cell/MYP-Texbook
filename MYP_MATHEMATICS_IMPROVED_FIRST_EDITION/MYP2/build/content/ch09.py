"""Chapter 9 - Transformations and symmetry (Geometry and space)."""
from chbase import *

PLATE = dict(
    part="Part III \u00b7 Geometry and space", part_numeral="III", chapter_no=9,
    kicker="Geometry and space", motif="geometry",
    title_lines=["Transformations", "and symmetry"],
    lead_lines=["A transformation moves a shape without arguing about it:",
                "every point obeys the same rule. Symmetry is what you get",
                "when the rule leaves the shape looking unchanged."],
    key_concept="Relationships", related=["Patterns", "Movement"],
    context="Personal and cultural expression",
    inquiry_lines=["Why do the same four moves describe tilework, fabric",
                   "and the way a wheel turns?"])

TITLE = "Transformations and symmetry"
SHORT = "Transformations and symmetry"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "Four moves, one coordinate grid, and the patterns they generate."),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "A small set of transformations generates every repeating pattern, so "
              "the symmetry of a design can be described as precisely as its "
              "geometry."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Relationships.** Each transformation is a rule linking "
        "every point to exactly one image point.\n"
        "**Related \u00b7 Patterns.** Repetition is the visible result of a "
        "transformation applied again and again.\n"
        "**Related \u00b7 Movement.** Translation, reflection, rotation and "
        "enlargement are the four ways a figure can be moved."),
    BOX("note", "Global context \u00b7 Personal and cultural expression",
        "Exploration: symmetry in textile design, mosaic and architecture. A pattern "
        "is a cultural statement made with mathematical operations."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** What are the four types of transformation?",
        "**Conceptual:** Why does reflection change orientation while rotation does "
        "not?",
        "**Debatable:** Can a design be both original and fully symmetrical?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii",
         "Perform and describe the four transformations on a grid."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate symmetry orders and which shapes tile."],
        ["C \u00b7 Communicating", "ii, iii, iv",
         "Describe a transformation fully, with centre, angle or vector."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Design a repeat pattern and justify the transformations used."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to describe a transformation completely, students must "
        "state its type and every detail it requires \u2014 vector, mirror line, centre "
        "and angle, or centre and scale factor."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Translate a shape using a column vector.",
         "Move a point by (\u22123, 4) and give the new coordinates."],
        ["Reflect a shape in a given line.",
         "Reflect in the `x`-axis, the `y`-axis, `y` = `x` and `y` = \u2212`x`."],
        ["Rotate a shape about a point.",
         "Rotate 90\u00b0 or 180\u00b0 and state the direction."],
        ["Enlarge a shape from a centre.",
         "Apply scale factors greater or less than 1, including negative ones."],
        ["Identify lines and orders of symmetry.",
         "Count them for regular polygons and for a design."],
        ["Describe a transformation fully.",
         "Say \u201creflection in the line `y` = `x`\u201d, not just "
         "\u201creflection\u201d."],
    ], widths=[1.6, 1.8]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Plot the points (2, 3) and (\u22121, 4).",
               "Write the coordinates of the point 4 units right and 2 down from "
               "(1, 5).",
               "Calculate \u00a0 3 \u00d7 4\u00b2.",
               "Name a shape with 4 lines of symmetry.",
               "How many degrees in a quarter turn?",
               "Calculate \u00a0 \u00bd \u00d7 8."]),
    P("If three or more answers are wrong, revisit coordinates and ratio before "
      "continuing."),

    # ------------------------------------------------------------------ 9.1
    S("9.1", "Translation", "A \u00b7 I  \u00b7  C \u00b7 II", ["Movement",
      "Patterns"]),
    L("A translation slides a shape without turning it. Every point moves by the same "
      "amount in the same direction, so the shape's size and orientation are "
      "unchanged."),
    ST("03", "ENGAGE",
       "One tile, repeated."),
    P("A wall of identical tiles is built by placing each tile beside the last. Before "
      "reading on, describe in words, as precisely as you can, the movement from one "
      "tile to the next \u2014 and explain why a builder only needs to be told the "
      "first tile and that movement."),
    ST("04", "EXPLORE",
       "Move, record, compare."),
    DIAG(200, "translation",
         "The same shape translated by the vector (5, \u22122). Every vertex moves 5 "
         "units right and 2 down; the image is congruent to the object."),
    OL(["Copy the diagram onto squared paper and record the coordinates of both "
        "shapes.",
        "Subtract the object's coordinates from the image's. What do you notice?",
        "Write the movement as a column vector.",
        "Translate the image again by the same vector and record the new "
        "coordinates.",
        "Describe the single translation equivalent to the two moves together.",
        "What happens if you apply the opposite vector to the image?"]),
    ST("05", "EXPLAIN"),
    DEF("A `translation` moves every point of a shape the same distance in the same "
        "direction. It is described by a `column vector` (\u2009`a` over `b`\u2009): "
        "`a` units right and `b` units up, with negative values meaning left and "
        "down. A translation produces a `congruent` image."),
    WE("9.1.1", "Translate a point",
       "Translate the point A(2, 3) by the vector (3, \u22121). State the image.",
       ["A move of 3 right adds 3 to the `x`-coordinate: 2 + 3 = 5.",
        "A move of 1 down subtracts 1 from the `y`-coordinate: 3 \u2212 1 = 2.",
        "The image is A\u2032(5, 2).",
        "Check the direction: the new point is right and below the original."],
       "A\u2032(5, 2)",
       "Add the vector to the coordinates; do not multiply."),
    WE("9.1.2", "Translate a triangle",
       "A triangle has vertices (1, 1), (4, 1) and (1, 3). Translate it by the vector "
       "(2, 3).",
       ["Apply the same vector to each vertex.",
        "(1, 1) \u2192 (3, 4); (4, 1) \u2192 (6, 4); (1, 3) \u2192 (3, 6).",
        "The image triangle has vertices (3, 4), (6, 4) and (3, 6).",
        "Check: each image vertex is 2 right and 3 above its object vertex."],
       "(3, 4), (6, 4), (3, 6)",
       "A translation keeps side lengths and angles, so the image is congruent."),
    WE("9.1.3", "Find the vector",
       "A translation maps (2, 5) to (2, 1). Find the vector and the image of (7, 3).",
       ["The `x`-coordinate does not change: the horizontal component is 0.",
        "The `y`-coordinate falls from 5 to 1: the vertical component is \u22124.",
        "The vector is (0, \u22124).",
        "Applying it to (7, 3) gives (7, \u22121)."],
       "(0, \u22124); image (7, \u22121)",
       "Subtract the object coordinates from the image coordinates to find the "
       "vector."),
    ERR("\u201cA translation changes the size of the shape if the vector is long.\u201d "
        "A translation only moves a shape; it never stretches it. The vector describes "
        "distance and direction, not scale."),
    PRAC("9.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Translate A(2, 3) by the vector (3, \u22121). State the image.", "F"),
        Q("Translate B(\u22121, 4) by the vector (2, 2).", "F"),
        Q("Describe the translation that maps (1, 1) to (4, 5).", "F"),
        Q("A triangle has vertices (1, 1), (4, 1), (1, 3). Translate it by (2, 3).",
          "F"),
        Q("A translation maps (2, 5) to (2, 1). Find the vector.", "F"),
        Q("A translation maps (2, 5) to (2, 1). Find the image of (7, 3).", "P"),
        Q("Apply the translation (2, 1) and then (\u22123, 4) to the point (0, 0). "
          "Describe the single equivalent translation.", "P"),
        Q("Translate the square with vertices (0, 0), (2, 0), (2, 2), (0, 2) by "
          "(\u22123, 1) and give all four image vertices.", "P"),
        Q("A student says \u201cthe image of a translation is similar but not "
          "congruent\u201d. Correct the statement.", "R"),
        Q("A translation maps A(\u22122, 3) to B(4, \u22121). Find the vector, and "
          "the point that maps to (0, 0).", "E"),
        Q("A translation maps (`x`, `y`) to (`x` + 3, `y` \u2212 2). Find the point "
          "whose image is (1, 1).", "E"),
        Q("Explain why applying a translation twice is the same as applying one vector, "
          "and write the resulting vector for (2, 1) followed by (2, 1).", "E"),
    ]),

    # ------------------------------------------------------------------ 9.2
    S("9.2", "Reflection and line symmetry", "A \u00b7 II  \u00b7  B \u00b7 I",
      ["Patterns", "Form"]),
    L("A reflection flips a shape across a mirror line. Distances from the line are "
      "preserved, but the shape's orientation is reversed."),
    DIAG(190, "reflection",
         "A reflection in the line `y` = `x`. Each point and its image are the same "
         "distance from the mirror line, measured perpendicular to it."),
    DIAG(196, "symmetry_shapes",
         "Lines and orders of symmetry for regular polygons. A regular `n`-gon has `n` "
         "lines of symmetry and rotational symmetry of order `n`."),
    TABLE(["Mirror line", "Rule for the image of (`x`, `y`)"], [
        ["the `x`-axis", "(`x`, \u2212`y`)"],
        ["the `y`-axis", "(\u2212`x`, `y`)"],
        ["the line `y` = `x`", "(`y`, `x`)"],
        ["the line `y` = \u2212`x`", "(\u2212`y`, \u2212`x`)"],
    ], widths=[1.2, 2.3], fs=8.8),
    DEF("A `line of symmetry` divides a shape into two halves that are mirror images. "
        "A shape's `order of rotational symmetry` is the number of positions in a full "
        "turn in which it looks unchanged. A circle has infinitely many lines of "
        "symmetry."),
    WE("9.2.1", "Reflect a point",
       "Reflect (3, 2) in (a) the `x`-axis, (b) the `y`-axis and (c) the line `y` = "
       "`x`.",
       ["(a) The `x`-axis flips vertically: (3, \u22122).",
        "(b) The `y`-axis flips horizontally: (\u22123, 2).",
        "(c) In `y` = `x` the coordinates swap: (2, 3).",
        "Check (c): the line `y` = `x` is the diagonal through (0, 0) and (1, 1)."],
       "(3, \u22122), (\u22123, 2) and (2, 3)",
       "Sketch the point and the mirror line before applying the rule."),
    WE("9.2.2", "Reflect a triangle",
       "A triangle has vertices (1, 1), (3, 1) and (2, 4). Reflect it in the "
       "`x`-axis.",
       ["Reflecting in the `x`-axis sends (`x`, `y`) to (`x`, \u2212`y`).",
        "(1, 1) \u2192 (1, \u22121); (3, 1) \u2192 (3, \u22121); (2, 4) \u2192 (2, "
        "\u22124).",
        "The image triangle is below the axis, with the same side lengths.",
        "The image is congruent but has been flipped: clockwise has become "
        "anticlockwise."],
       "(1, \u22121), (3, \u22121), (2, \u22124)",
       "All three vertices must move; a reflection is determined by its mirror "
       "line."),
    WE("9.2.3", "Symmetry of a shape",
       "How many lines of symmetry and what order of rotational symmetry does (a) a "
       "square and (b) a regular hexagon have?",
       ["(a) A square has 4 lines of symmetry: one vertical, one horizontal and two "
        "diagonals.",
        "Its rotational symmetry is of order 4, because a quarter turn returns it to "
        "itself.",
        "(b) A regular hexagon has 6 lines of symmetry and rotational symmetry of "
        "order 6.",
        "For a regular polygon both numbers equal the number of sides."],
       "(a) 4 lines, order 4 (b) 6 lines, order 6",
       "For a regular polygon, lines of symmetry = order of rotational symmetry = "
       "number of sides."),
    ERR("\u201cEvery quadrilateral has four lines of symmetry.\u201d Only a square "
        "does. A rectangle has two, a rhombus two, a parallelogram none \u2014 and a "
        "kite has one. Symmetry depends on the shape's actual proportions, not its "
        "name."),
    PRAC("9.2", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Reflect (3, 2) in the `x`-axis, then in the `y`-axis.", "F"),
        Q("Reflect (\u22124, 5) in the `x`-axis.", "F"),
        Q("Reflect (5, \u22122) in the `y`-axis.", "F"),
        Q("Reflect (2, 6) in the line `y` = `x`.", "F"),
        Q("How many lines of symmetry has (a) a square (b) a rectangle (c) an "
          "equilateral triangle (d) a circle?", "F"),
        Q("Reflect the triangle (1, 1), (3, 1), (2, 4) in the `x`-axis.", "P"),
        Q("Reflect (3, 1) in the line `y` = \u2212`x`.", "P"),
        Q("A shape has rotational symmetry of order 6 but no line of symmetry. Describe "
          "what such a shape might look like.", "R"),
        Q("Do the letters A, H, N and S have line symmetry? State how many lines each "
          "has.", "P"),
        Q("Reflect (5, 3) in the line `y` = 2. Describe a rule that works for any "
          "point reflected in a horizontal line.", "E"),
        Q("Explain why reflecting a shape twice in the same line returns it to its "
          "original position.", "E"),
        Q("Reflect (4, 1) in `y` = `x` and then in the `y`-axis. Describe the single "
          "transformation equivalent to the two reflections.", "E"),
    ]),

    # ------------------------------------------------------------------ 9.3
    S("9.3", "Rotation and rotational symmetry", "A \u00b7 III  \u00b7  C \u00b7 "
      "III", ["Movement", "Space"]),
    L("A rotation turns a shape about a fixed point. The centre, the angle and the "
      "direction together determine the image completely."),
    DIAG(190, "rotation",
         "A rotation of 90\u00b0 anticlockwise about the origin. Distances from the "
         "centre are preserved; only direction changes."),
    TABLE(["Rotation about the origin", "Rule for (`x`, `y`)"], [
        ["90\u00b0 clockwise", "(`y`, \u2212`x`)"],
        ["90\u00b0 anticlockwise", "(\u2212`y`, `x`)"],
        ["180\u00b0 (either direction)", "(\u2212`x`, \u2212`y`)"],
    ], widths=[1.4, 2.1], fs=8.8),
    PHOTO("ch09_wheel.jpg", 0.74,
          "A Ferris wheel. Each cabin is carried through the same rotation about the "
          "hub, so the wheel's rotational symmetry is of high order.",
          "Photograph: Pexels, free to use under the Pexels licence.", 0.6),
    DEF("A `rotation` turns a shape about a `centre` through a given `angle`, either "
        "clockwise or anticlockwise. Rotations preserve lengths and angles but change "
        "the direction a shape faces."),
    WE("9.3.1", "Rotate a point",
       "Rotate the point (3, 0) about the origin by (a) 90\u00b0 clockwise and (b) "
       "180\u00b0.",
       ["(a) 90\u00b0 clockwise sends (`x`, `y`) to (`y`, \u2212`x`): (0, \u22123).",
        "(b) 180\u00b0 sends (`x`, `y`) to (\u2212`x`, \u2212`y`): (\u22123, 0).",
        "Check: the distance from the origin is 3 in every case.",
        "The point has moved round the origin, not towards or away from it."],
       "(0, \u22123) and (\u22123, 0)",
       "The distance to the centre never changes under rotation, which is a quick "
       "check."),
    WE("9.3.2", "Find the rotation",
       "A rotation about the origin maps (5, 0) to (0, 5). Describe it.",
       ["The image is on the `y`-axis, so the turn is a quarter turn.",
        "Moving from the positive `x`-axis to the positive `y`-axis is "
        "anticlockwise.",
        "The rotation is 90\u00b0 anticlockwise about the origin.",
        "Check with the rule: (\u2212`y`, `x`) sends (5, 0) to (0, 5)."],
       "90\u00b0 anticlockwise about the origin",
       "A quarter turn clockwise would send (5, 0) to (0, \u22125)."),
    WE("9.3.3", "Order of rotational symmetry",
       "What is the order of rotational symmetry of a regular pentagon, and of the "
       "letter S?",
       ["A regular pentagon looks unchanged after each 360\u00b0 \u00f7 5 = 72\u00b0 "
        "turn.",
        "It returns to itself five times in a full turn, so the order is 5.",
        "The letter S is unchanged after a half turn, so its order is 2.",
        "A shape with no rotational symmetry other than 360\u00b0 has order 1."],
       "Pentagon 5; letter S 2",
       "Order counts the positions in a full turn where the shape looks the same, "
       "including the start."),
    ERR("\u201cA rotation changes the size of a shape, because the far corners travel "
        "further.\u201d Points further from the centre do move further, but every "
        "distance within the shape is unchanged, so the image is congruent. Only an "
        "enlargement changes size."),
    PRAC("9.3", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Rotate (3, 0) about the origin by 90\u00b0 clockwise.", "F"),
        Q("Rotate (3, 0) about the origin by 180\u00b0.", "F"),
        Q("Rotate (2, 1) about the origin by 90\u00b0 anticlockwise.", "F"),
        Q("State the order of rotational symmetry of (a) a square (b) a regular "
          "pentagon (c) a rectangle.", "F"),
        Q("What is the angle of rotation for a shape with rotational symmetry of order "
          "8?", "F"),
        Q("Rotate the triangle (1, 0), (0, 1), (1, 1) by 90\u00b0 anticlockwise about "
          "the origin.", "P"),
        Q("A rotation maps (5, 0) to (0, 5). Describe it fully.", "P"),
        Q("Rotate (4, 2) by 90\u00b0 clockwise about the origin, then by 90\u00b0 "
          "clockwise again. What single transformation is equivalent?", "P"),
        Q("Two students rotate a shape 90\u00b0 clockwise and 270\u00b0 "
          "anticlockwise. Do they get the same image? Explain.", "R"),
        Q("Rotate (2, 3) by 90\u00b0 clockwise about the centre (1, 1).", "E"),
        Q("Explain why the order of rotational symmetry of a regular `n`-gon is `n`.",
          "E"),
        Q("A square is rotated 45\u00b0 about its centre. Explain why the image is not "
          "the same square, and say what the order of symmetry tells you.", "E"),
    ]),

    # ------------------------------------------------------------------ 9.4
    S("9.4", "Enlargement", "A \u00b7 IV  \u00b7  D \u00b7 III", ["Movement",
      "Measurement"]),
    L("An enlargement changes size by a scale factor from a fixed centre. It is the "
      "only one of the four transformations that changes lengths."),
    DIAG(190, "enlargement",
         "An enlargement with scale factor 3 from a centre at one corner. Every "
         "distance from the centre triples, so lengths multiply by 3 and areas by 9."),
    DEF("An `enlargement` with centre C and `scale factor` `k` sends each point to a "
        "point `k` times as far from C, on the same line. Lengths multiply by `k`, "
        "areas by `k`\u00b2, volumes by `k`\u00b3. A negative `k` places the image on "
        "the opposite side of the centre."),
    WE("9.4.1", "Enlarge from the origin",
       "Enlarge the triangle with vertices (1, 1), (2, 1) and (1, 2) by scale factor 3 "
       "from the origin.",
       ["Multiply each coordinate by 3.",
        "(1, 1) \u2192 (3, 3); (2, 1) \u2192 (6, 3); (1, 2) \u2192 (3, 6).",
        "The image triangle is three times as far from the origin in both directions.",
        "Check a side length: 1 unit becomes 3 units, as the scale factor "
        "requires."],
       "(3, 3), (6, 3), (3, 6)",
       "For a centre at the origin, an enlargement is multiplication of both "
       "coordinates."),
    WE("9.4.2", "Centre not at the origin",
       "Enlarge the point (2, 3) by scale factor 2 from the centre (1, 1).",
       ["Find the vector from the centre to the point: (2 \u2212 1, 3 \u2212 1) = (1, "
        "2).",
        "Multiply it by the scale factor: 2 \u00d7 (1, 2) = (2, 4).",
        "Add it back to the centre: (1 + 2, 1 + 4) = (3, 5).",
        "Check: the image is twice as far from (1, 1) as the original."],
       "(3, 5)",
       "Subtract the centre first, multiply, then add the centre back."),
    WE("9.4.3", "Area and scale factor",
       "A photograph 6 cm by 4 cm is enlarged so that its longer side becomes 15 cm. "
       "Find the scale factor and the area of the enlargement.",
       ["Scale factor = 15 \u00f7 6 = 2.5.",
        "The shorter side becomes 4 \u00d7 2.5 = 10 cm.",
        "Area of the original is 24 cm\u00b2; the enlargement is 15 \u00d7 10 = 150 "
        "cm\u00b2.",
        "Check with the area scale factor: 24 \u00d7 2.5\u00b2 = 24 \u00d7 6.25 = "
        "150 cm\u00b2."],
       "`k` = 2.5; area 150 cm\u00b2",
       "Areas follow `k`\u00b2, so an area check is a strong test of a scale factor."),
    ERR("\u201cA shape enlarged by scale factor 2 has twice the area.\u201d Both "
        "lengths double, so the area multiplies by 2 \u00d7 2 = 4. A 3 cm square "
        "becomes 6 cm and its area grows from 9 to 36 cm\u00b2."),
    PRAC("9.4", "SUPPORT 1\u20135  \u00b7  CORE 6\u201310  \u00b7  EXTENSION "
                "11\u201313", [
        Q("Enlarge (2, 1) by scale factor 3 from the origin.", "F"),
        Q("Enlarge (4, 6) by scale factor 0.5 from the origin.", "F"),
        Q("Enlarge the triangle (1, 1), (2, 1), (1, 2) by scale factor 2 from the "
          "origin.", "F"),
        Q("What is the area scale factor for an enlargement of scale factor 3?", "F"),
        Q("Enlarge (1, 2) by scale factor \u22122 from the origin.", "F"),
        Q("Enlarge (2, 3) by scale factor 2 from the centre (1, 1).", "P"),
        Q("An enlargement maps a 5 cm length to 15 cm. Find the scale factor and the "
          "area scale factor.", "P"),
        Q("A shape of area 12 cm\u00b2 is enlarged by scale factor 2. Find the new "
          "area.", "P"),
        Q("A map uses a scale of 1 : 25 000. What real distance does 4 cm "
          "represent?", "P"),
        Q("A student says an enlargement with scale factor \u22121 is a reflection. Is "
          "the statement accurate? Explain what the transformation actually is.", "R"),
        Q("A cube of edge 2 cm is enlarged by scale factor 3. Find its new volume and "
          "compare with the original.", "E"),
        Q("An enlargement maps triangle A with area 18 cm\u00b2 to triangle B with area "
          "162 cm\u00b2. Find the scale factor and the ratio of a pair of corresponding "
          "sides.", "E"),
        Q("Explain why the area scale factor is `k`\u00b2 rather than `k`, using a "
          "rectangle as an example.", "E"),
    ]),

    # ------------------------------------------------------------------ 9.5
    S("9.5", "Tessellation and symmetry in design", "B \u00b7 II  \u00b7  D \u00b7 "
      "IV", ["Patterns", "Relationships"]),
    L("A tessellation covers the plane with no gaps and no overlaps. Which shapes can "
      "do it is decided by the angles at a point, and the design is decided by the "
      "transformations used."),
    DIAG(190, "tessellation",
         "A tessellation built by translation and rotation. Each copy is congruent to "
         "the original tile."),
    PHOTO("ch09_mosaic.jpg", 0.95,
          "Mosaic tiles laid on a diagonal grid. The pattern is generated by "
          "translations along two directions, with reflections across the seams.",
          "Photograph: Pexels, free to use under the Pexels licence.", 0.62),
    P("Three regular hexagons meet at a vertex because 3 \u00d7 120\u00b0 = 360\u00b0. "
      "Four squares meet because 4 \u00d7 90\u00b0 = 360\u00b0. A regular pentagon "
      "cannot tile on its own because 108\u00b0 does not divide 360\u00b0 exactly "
      "\u2014 three pentagons leave a gap of 36\u00b0."),
    WE("9.5.1", "Why a shape tiles",
       "Explain why a regular octagon does not tessellate on its own.",
       ["Each interior angle of a regular octagon is (8 \u2212 2) \u00d7 180 \u00f7 8 = "
        "135\u00b0.",
        "At a point the angles must total 360\u00b0: 360 \u00f7 135 = 2.67.",
        "Two octagons give 270\u00b0, leaving a 90\u00b0 gap; three give 405\u00b0, "
        "which overlaps.",
        "So octagons need another shape \u2014 a square fits the 90\u00b0 gap, which "
        "is why octagons and squares tile together."],
       "135\u00b0 does not divide 360\u00b0",
       "The test is always: does the interior angle divide 360 exactly?"),
    WE("9.5.2", "Describing a pattern",
       "A border design repeats a single motif every 6 cm along a strip, with each "
       "motif also reflected in the centre line. Name the transformations used.",
       ["Repeating along the strip is a translation by 6 cm each time.",
        "The reflection across the centre line creates the mirror version.",
        "The two operations together give a pattern with translation symmetry and a "
        "line of symmetry.",
        "No rotation or enlargement is needed to describe the design."],
       "Translation and reflection",
       "A complete description names the vector and the mirror line, not only the "
       "types."),
    WE("9.5.3", "Symmetry of a logo",
       "A logo is a regular hexagon divided into six identical triangles, three shaded "
       "and three white, alternating. State its symmetry.",
       ["The hexagon returns to itself after every 60\u00b0 turn, so the order of "
        "rotational symmetry is 6.",
        "Alternating shading also returns after each 60\u00b0, because shading is "
        "unchanged by another sixth of a turn.",
        "The three lines joining opposite vertices are lines of symmetry.",
        "The three lines joining midpoints of opposite sides are not, because they "
        "swap shaded with white."],
       "Order 6; three lines of symmetry",
       "Check symmetry on the colouring, not only on the outline."),
    ERR("\u201cAny shape that fits around a point tiles the plane.\u201d Meeting at "
        "one point is not enough: the arrangement must continue across the whole "
        "plane. Pentagons of the right kind can tile, but regular pentagons "
        "cannot."),
    PRAC("9.5", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("How many squares meet at a point in a square tessellation?", "F"),
        Q("Find each interior angle of a regular octagon.", "F"),
        Q("Explain why regular hexagons tessellate.", "F"),
        Q("Name the transformation that slides a shape without turning it.", "F"),
        Q("Explain why a regular pentagon does not tessellate on its own.", "P"),
        Q("Show that regular octagons and squares can tile together.", "P"),
        Q("A pattern repeats a motif every 4 cm along a strip. Name the transformation "
          "and state its vector.", "P"),
        Q("A design has rotational symmetry of order 4 and 4 lines of symmetry. Name a "
          "shape it could be based on.", "P"),
        Q("A student says a circle has rotational symmetry of order 1. Correct the "
          "statement.", "R"),
        Q("Design a border 12 cm long using one motif, translations and reflections. "
          "Describe every transformation you used.", "E"),
        Q("Two squares and three equilateral triangles meet at a point. Show that the "
          "angles fit and describe the resulting tiling.", "E"),
        Q("Explain how a designer could produce a pattern with translation symmetry "
          "but no reflection symmetry.", "E"),
    ]),

    CARD_D("The textile commission", [
        ("p", "A workshop is commissioned to print a repeat pattern on a 2 m length of "
              "cloth. The printer charges \u00a318 per square metre, and a repeat motif "
              "costs \u00a30.40 to prepare for each transformation applied to it."),
        ("ol", ["Design a motif and describe it on a grid with coordinates.",
                "Apply a translation to repeat it four times and state the vector.",
                "Apply a reflection and state the mirror line.",
                "Calculate the area of cloth printed and the cost of printing.",
                "Cost the transformations used, and compare with a design that uses "
                "one fewer transformation.",
                "Recommend a final design, justifying both the symmetry and the "
                "cost."]),
    ]),

    # ----------------------------------------------------------- investigate
    ST("06", "INVESTIGATE AND APPLY",
       "Which shapes tile, and which designs are symmetric."),
    CARD_I("The tiling test", [
        ("p", "Whether a shape tiles the plane depends on the angles that meet at a "
              "point."),
        ("ol", ["Find the interior angle of a regular triangle, square, pentagon, "
                "hexagon and octagon.",
                "For each, test whether 360\u00b7 is a whole-number multiple of the "
                "interior angle.",
                "Record your results in a table and identify which shapes tile.",
                "Test combinations: square and triangle, hexagon and triangle, octagon "
                "and square.",
                "Write a rule for a pair of shapes that will tile together.",
                "Design a tiling of your own using two shapes and verify the angles at "
                "every vertex.",
                "Explain why the rule must hold at every vertex, not only the ones you "
                "drew."]),
    ]),
    CARD_I("Symmetry audit of a design", [
        ("p", "Choose a design you can see in the room or in the photograph: a tile "
              "layout, a window grille or a fabric."),
        ("ol", ["Sketch the design and mark any lines of symmetry.",
                "State the order of rotational symmetry.",
                "Describe the translations that generate the repeat.",
                "Identify any reflections or rotations used in the design.",
                "Decide whether the design's symmetry was likely deliberate or "
                "accidental, and give a reason.",
                "Redesign the pattern to increase its symmetry, and describe what you "
                "changed.",
                "Write a paragraph on what the symmetry contributes to the design's "
                "effect."]),
    ]),

    # --------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("9.6", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["A translation slides by a column vector and leaves size and orientation "
        "unchanged.",
        "A reflection flips across a mirror line; distances from the line are "
        "preserved but orientation is reversed.",
        "A rotation turns about a centre through an angle in a stated direction.",
        "An enlargement multiplies lengths by `k`, areas by `k`\u00b2 and volumes by "
        "`k`\u00b3.",
        "Regular polygons have as many lines of symmetry as sides, and rotational "
        "symmetry of the same order.",
        "A shape tiles the plane when its angles fit exactly round a point and the "
        "arrangement continues without gaps."]),
    VOCAB("**translation** \u00b7 **column vector** \u00b7 **reflection** \u00b7 "
          "**mirror line** \u00b7 **rotation** \u00b7 **centre of rotation** \u00b7 "
          "**enlargement** \u00b7 **scale factor** \u00b7 **congruent** \u00b7 "
          "**similar** \u00b7 **tessellation** \u00b7 **order of symmetry**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["Giving a transformation's type but no details.",
         "Every transformation needs its vector, line, centre and angle, or centre "
         "and scale factor."],
        ["Thinking an enlargement of scale factor 2 doubles the area.",
         "Area scales by `k`\u00b2, so it quadruples."],
        ["Assuming a parallelogram has lines of symmetry.",
         "It has none: a half turn maps it to itself, but no mirror does."],
        ["Believing a long translation vector stretches the shape.",
         "A translation never changes size; only enlargement does."],
    ], widths=[1.5, 2.0]),
    H("Revision questions"),
    OL(["Translate (3, \u22122) by the vector (\u22121, 5).",
        "Reflect (\u22122, 7) in the `x`-axis.",
        "Rotate (0, 4) 90\u00b0 clockwise about the origin.",
        "Enlarge (3, 2) by scale factor \u22122 from the origin.",
        "A regular nonagon: state its order of rotational symmetry and its number of "
        "lines of symmetry."]),
    GAP(6),
    H("Before you move on"),
    P("Four things you should be able to do without help before the next "
      "chapter. If one of them is not yet secure, reread the section that "
      "taught it before attempting the mixed practice again.", 4),
    UL([
        "Carry out a translation, reflection, rotation and enlargement on a grid.",
        "Describe a transformation completely: type, centre or line, and amount.",
        "Combine two transformations and name the single equivalent one.",
        "Use the area and volume scale factors of an enlargement, not just the length factor.",
    ]),
    KEY("A transformation is a rule that moves every point; describing it fully is the mathematical work."),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["translate a shape using a column vector", "\u25a1", "\u25a1", "\u25a1"],
        ["reflect a shape in a named line", "\u25a1", "\u25a1", "\u25a1"],
        ["rotate a shape about a centre", "\u25a1", "\u25a1", "\u25a1"],
        ["enlarge a shape, including from a centre not at the origin", "\u25a1",
         "\u25a1", "\u25a1"],
        ["count lines and orders of symmetry", "\u25a1", "\u25a1", "\u25a1"],
        ["explain why a shape does or does not tile", "\u25a1", "\u25a1", "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], font_size=8.6),
    GAP(8),
    MYP("**Criterion A:** which transformation can you now perform without a rule "
        "sheet?\n"
        "**Criterion B:** what did the tiling test let you predict?\n"
        "**Criterion C:** did your description of each transformation include every "
        "detail?\n"
        "**Criterion D:** how did cost and symmetry compete in your design?",
        "Reflect on the criteria"),
    ATL("In order for a student to justify a design, students must name the "
        "transformation, state its parameters, and show that the pattern's symmetry "
        "follows from them.", "ATL \u00b7 Critical thinking"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("9.M", "MIXED 1\u201312", [
        Q("Translate (5, 1) by (\u22122, \u22123).", "F"),
        Q("Reflect (6, \u22123) in the `y`-axis.", "F"),
        Q("Rotate (2, 0) 180\u00b0 about the origin.", "F"),
        Q("Enlarge (2, 5) by scale factor 2 from the origin.", "F"),
        Q("How many lines of symmetry has a regular pentagon?", "F"),
        Q("Describe fully the translation mapping (4, 2) to (\u22121, 6).", "P"),
        Q("Reflect (4, 1) in the line `y` = `x`.", "P"),
        Q("Enlarge (3, 4) by scale factor 0.5 from the centre (1, 0).", "P"),
        Q("A student enlarges a rectangle 3 cm by 5 cm by scale factor 4 and says the "
          "area is 4 times as large. Correct the error.", "R"),
        Q("A regular polygon has 12 lines of symmetry. Name it and give its order of "
          "rotational symmetry.", "E"),
        Q("A map scale is 1 : 50 000. Find the real length represented by 6 cm, in "
          "kilometres.", "E"),
        Q("A design has one line of symmetry and rotational symmetry of order 1. "
          "Describe a motif that would produce it and one change that would raise its "
          "order of symmetry to 2.", "E"),
    ]),
]

ANSWERS = {
    "9.1": ["(5, 2).", "(1, 6).", "A translation by (3, 4).",
            "(3, 4), (6, 4), (3, 6).", "(0, \u22124).", "(7, \u22121).",
            "(\u22121, 5).", "(\u22123, 1), (\u22121, 1), (\u22121, 3), (\u22123, "
            "3).",
            "The image is congruent, not merely similar: lengths and angles are "
            "unchanged.",
            "Vector (6, \u22124); working backwards from (0, 0) gives the pre-image "
            "(\u22126, 4).",
            "(\u22122, 3).",
            "Two translations add: (2, 1) + (2, 1) = (4, 2), a single translation by "
            "(4, 2)."],
    "9.2": ["(3, \u22122) then (\u22123, \u22122).", "(\u22124, \u22125).",
            "(\u22125, \u22122).", "(6, 2).", "(a) 4 (b) 2 (c) 3 (d) infinitely "
            "many.",
            "(1, \u22121), (3, \u22121), (2, \u22124).", "(\u22121, \u22123).",
            "For example, a pinwheel of six identical arms; a half turn leaves it "
            "unchanged but no mirror does.",
            "A: 1, H: 2, N: 0, S: 0.",
            "(5, 1); reflecting in `y` = `c` sends (`x`, `y`) to (`x`, 2`c` \u2212 "
            "`y`).",
            "The first reflection produces the mirror image, and reflecting that image "
            "in the same line returns every point to where it started.",
            "(\u22121, 4); the two reflections together are equivalent to a 90\u00b0 "
            "anticlockwise rotation about the origin."],
    "9.3": ["(0, \u22123).", "(\u22123, 0).", "(\u22121, 2).",
            "(a) 4 (b) 5 (c) 2.", "45\u00b0.",
            "(0, 1), (\u22121, 0), (\u22121, 1).",
            "90\u00b0 anticlockwise about the origin.",
            "(2, \u22124) then (\u22124, \u22122); equivalent to a 180\u00b0 "
            "rotation about the origin.",
            "Yes: 270\u00b0 anticlockwise is the same as 90\u00b0 clockwise.",
            "Relative vector (1, 2) rotates clockwise to (2, \u22121), so the image is "
            "(3, 0).",
            "A rotation of 360\u00b0 \u00f7 `n` maps the polygon onto itself, and "
            "there are `n` such positions before returning to the start.",
            "A 45\u00b0 turn puts vertices where edges were, so the image occupies a "
            "different region; the order 4 tells you only 90\u00b0 turns map it to "
            "itself."],
    "9.4": ["(6, 3).", "(2, 3).", "(2, 2), (4, 2), (2, 4).", "9.",
            "(\u22122, \u22124).", "(3, 5).", "`k` = 3; area factor 9.", "48 "
            "cm\u00b2.", "1 km.",
            "Not accurate: a scale factor of \u22121 is a half turn about the centre "
            "(a rotation of 180\u00b0), which looks like a reflection only for "
            "symmetric shapes.",
            "Old volume 8 cm\u00b3, new volume 216 cm\u00b3, which is 27 times larger "
            "since 3\u00b3 = 27.",
            "`k` = 3; corresponding sides are in the ratio 3 : 1.",
            "A rectangle `l` \u00d7 `w` becomes `k``l` \u00d7 `k``w`, so its area "
            "multiplies by `k` \u00d7 `k` = `k`\u00b2."],
    "9.5": ["Four.", "135\u00b0.", "Each interior angle is 120\u00b0 and 3 \u00d7 "
            "120\u00b0 = 360\u00b0, so three hexagons meet at every vertex.",
            "A translation.",
            "Each interior angle is 108\u00b0 and 360 \u00f7 108 is not a whole "
            "number: three leave a 36\u00b0 gap.",
            "135 + 135 + 90 = 360, so two octagons and a square meet at each vertex.",
            "A translation with vector 4 cm along the strip.",
            "A square, or any design with fourfold symmetry.",
            "A circle has infinitely many rotational positions in which it looks "
            "unchanged, so its order is not 1.",
            "Answers vary; the description must name the vector and the mirror "
            "line.",
            "60 + 60 + 60 + 90 + 90 = 360, so the angles fit; the tiling alternates "
            "squares and triangles.",
            "Use only translations of an asymmetric motif, so that no mirror line "
            "exists."],
    "9.M": ["(3, \u22122).", "(\u22126, \u22123).", "(\u22122, 0).", "(4, 10).",
            "Five.", "A translation by (\u22125, 4).", "(1, 4).", "(2, 2).",
            "The area is 16 times as large, since 4\u00b2 = 16.",
            "A regular dodecagon; order 12.", "3 km.",
            "Answers vary; a motif with a single mirror line has order 1, and adding "
            "a copy rotated by 180\u00b0 raises the order to 2."],
}


# ------------------------------------------------------------------ part review
BLOCKS += [
    GAP(14),
    ("head", "Part III review"),
    ("pagetitle", "Part III review", "Consolidation \u00b7 chapters 7\u20139"),
    L("Ten questions on shape, space and movement. Take \u03c0 = 3.14. Draw a "
      "sketch before you calculate: in Part III an unlabelled figure is the most "
      "common cause of a wrong value."),
    P("Questions 7\u20139 ask for a transformation. Give the single transformation "
      "that maps the object onto the image, with every number it needs.", 6),
    PRAC("R3", "SUPPORT 1\u20133  \u00b7  CORE 4\u20137  \u00b7  EXTENSION 8\u201310", [
        Q("Two angles on a straight line are (2`x` + 15)\u00b0 and (3`x` + 10)\u00b0. "
          "Find `x` and both angles.", "F"),
        Q("A regular polygon has an exterior angle of 20\u00b0. Find its number of "
          "sides and each interior angle.", "F"),
        Q("Find the area and the circumference of a circle of diameter 18 cm "
          "(\u03c0 = 3.14).", "F"),
        Q("A semicircle of radius 7 cm sits on a rectangle 14 cm by 5 cm. Find the "
          "total area.", "P"),
        Q("A cuboid is 9 cm by 6 cm by 4 cm. Find its surface area and its volume.",
          "P"),
        Q("A cylinder has radius 6 cm and height 10 cm. Find its volume "
          "(\u03c0 = 3.14).", "P"),
        Q("Translate the point (3, \u22125) by the vector (\u22124, 7).", "F"),
        Q("Reflect (6, \u22122) in the line `y` = `x`, then in the `x`-axis. Give "
          "both images.", "R"),
        Q("Enlarge (3, 4) by scale factor 2 from the centre (1, 2).", "R"),
        Q("A shape of area 15 cm\u00b2 is enlarged by scale factor 4. Find the new "
          "area, and explain why it is not 4 times 15 cm\u00b2.", "E"),
    ]),
    GAP(8),
]

ANSWERS["R3"] = [
    "5`x` + 25 = 180, so `x` = 31; the angles are 77\u00b0 and 103\u00b0.",
    "18 sides, since 360 \u00f7 20 = 18; each interior angle is 180 \u2212 20 = "
    "160\u00b0.",
    "Area 3.14 \u00d7 9\u00b2 = 254.34 cm\u00b2; circumference 3.14 \u00d7 18 = "
    "56.52 cm.",
    "146.93 cm\u00b2: the semicircle is 3.14 \u00d7 49 \u00f7 2 = 76.93 cm\u00b2 "
    "and the rectangle is 70 cm\u00b2.",
    "Surface area 228 cm\u00b2; volume 216 cm\u00b3.",
    "3.14 \u00d7 36 \u00d7 10 = 1 130.4 cm\u00b3.",
    "(\u22121, 2).",
    "In `y` = `x` the image is (\u22122, 6); reflecting that in the `x`-axis gives "
    "(\u22122, \u22126).",
    "(5, 6): the vector from the centre is (2, 2), which doubles to (4, 4), and "
    "(1, 2) + (4, 4) = (5, 6).",
    "240 cm\u00b2. Under an enlargement every length multiplies by 4, and an area "
    "is a product of two lengths, so the area multiplies by 4\u00b2 = 16.",
]
