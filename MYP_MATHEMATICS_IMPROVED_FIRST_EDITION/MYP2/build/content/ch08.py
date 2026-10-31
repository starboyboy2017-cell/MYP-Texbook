"""Chapter 8 - 3D geometry (Geometry and space)."""
from chbase import *

PLATE = dict(
    part="Part III \u00b7 Geometry and space", part_numeral="III", chapter_no=8,
    kicker="Geometry and space", motif="geometry",
    title_lines=["3D geometry"],
    lead_lines=["A solid is a surface you could wrap and a space you could fill.",
                "This chapter separates those two questions \u2014 how much",
                "material, and how much room \u2014 because they are answered",
                "by different formulas."],
    key_concept="Form", related=["Space", "Measurement"],
    context="Globalisation and sustainability",
    inquiry_lines=["How much material and how much capacity does a container",
                   "really need, and who decides which matters more?"])

TITLE = "3D geometry"
SHORT = "3D geometry"

BLOCKS = [
    ST("01", "MYP UNIT PLANNER",
       "From describing a solid to measuring its skin and its interior."),
    GAP(10),
    STATEMENT("Statement of inquiry",
              "The form of a three-dimensional object determines both the material "
              "needed to make it and the space it can hold, so design is a "
              "negotiation between surface and volume."),
    GAP(6),
    BOX("keyidea", "Key and related concepts",
        "**Key concept \u00b7 Form.** A solid is defined by its faces, edges and "
        "vertices, and by the shape that is swept to make it.\n"
        "**Related \u00b7 Space.** Volume measures the room inside; surface area "
        "measures the boundary.\n"
        "**Related \u00b7 Measurement.** Both quantities are computed from a few "
        "lengths, with units that must be tracked carefully."),
    BOX("note", "Global context \u00b7 Globalisation and sustainability",
        "Exploration: packaging, storage and water tanks. Material cost follows "
        "surface area; transport and storage cost follows volume. Every container is "
        "a compromise between the two."),
    GAP(8),
    H("Inquiry questions"),
    UL(["**Factual:** How do you find the volume of a prism?",
        "**Conceptual:** Why can two solids have the same volume but very different "
        "surface areas?",
        "**Debatable:** Should packaging be designed to minimise material, or to sell "
        "the product?"]),
    GAP(6),
    TABLE(["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii",
         "Use the surface-area and volume formulas for prisms and cylinders."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate how volume and surface area change with scale."],
        ["C \u00b7 Communicating", "ii, iii, iv",
         "Draw and interpret nets, and record units correctly."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv, v",
         "Design and cost packaging for a stated volume."],
    ], widths=[1.25, 0.55, 2.55]),
    GAP(6),
    ATL("In order for a student to model a real container, students must decide which "
        "measurement the question asks for \u2014 material or capacity \u2014 and "
        "justify the formula chosen."),
    GAP(10),
    ST("02", "LEARNING INTENTIONS AND SUCCESS CRITERIA"),
    GAP(6),
    TABLE(["You are learning to", "You have succeeded when you can"], [
        ["Count faces, edges and vertices.",
         "Describe a cuboid, a prism and a pyramid correctly."],
        ["Use Euler's relationship.",
         "Check `V` \u2212 `E` + `F` = 2 on any solid you meet."],
        ["Find the surface area of a prism or cylinder.",
         "Use a net and state the answer in square units."],
        ["Find the volume of a prism or cylinder.",
         "Use area of cross-section \u00d7 length."],
        ["Convert between cm\u00b3, m\u00b3 and litres.",
         "Convert 1570 cm\u00b3 to 1.57 litres without error."],
        ["Find the volume and surface area of a composite solid.",
         "Split it, calculate the parts, and remove hidden faces."],
    ], widths=[1.6, 1.8]),
    GAP(8),
    BOX("note", "Prerequisite check \u00b7 10 minutes, no calculator",
        None, ["Calculate \u00a0 6 \u00d7 4 \u00d7 3.",
               "Calculate \u00a0 2 \u00d7 (5 \u00d7 4 + 5 \u00d7 3 + 4 \u00d7 3).",
               "Calculate \u00a0 3.14 \u00d7 5\u00b2.",
               "Find the area of a triangle with base 6 cm and height 4 cm.",
               "How many cm\u00b3 are in 1 litre?",
               "Name a solid with 6 square faces."]),
    P("If three or more answers are wrong, revisit area work in chapter 7 before "
      "continuing."),

    # ------------------------------------------------------------------ 8.1
    S("8.1", "Solids, faces and nets", "A \u00b7 I  \u00b7  C \u00b7 II",
      ["Space", "Form"]),
    L("Every solid can be described by its flat faces, its edges and its corners, and "
      "by the flat pattern \u2014 the net \u2014 that folds into it."),
    ST("03", "ENGAGE",
       "The problem with a stack of boxes."),
    P("A stockroom is filled with identical cartons. The manager measures one carton, "
      "writes the number on the outside, and claims that the whole stockroom's storage "
      "capacity can be found from that one number. Before reading on, decide what that "
      "number is, and what else the manager would need to know."),
    PHOTO("ch08_boxes.jpg", 1.05,
          "Stacked cartons. One measured volume, repeated, predicts the space a whole "
          "stack occupies \u2014 but not the material used to make it.",
          "Photograph: Pexels, free to use under the Pexels licence.", 0.66),
    ST("04", "EXPLORE",
       "Count, record, conjecture."),
    DIAG(200, "cuboid",
         "A cuboid with length, width and height marked. Its six faces come in three "
         "pairs of equal rectangles.", dims=("length", "width", "height")),
    TABLE(["Solid", "Faces `F`", "Edges `E`", "Vertices `V`", "`V` \u2212 `E` + "
           "`F`"], [
        ["Cube", "6", "12", "8", "2"],
        ["Triangular prism", "5", "9", "6", "2"],
        ["Square-based pyramid", "5", "8", "5", "2"],
        ["Triangular pyramid (tetrahedron)", "4", "6", "4", "2"],
    ], widths=[1.7, 0.6, 0.6, 0.6, 0.7]),
    OL(["Copy and complete the table for two more solids of your own choosing.",
        "What do you notice about the last column?",
        "Write the relationship as an equation.",
        "Test it on the box in the photograph: count faces, edges and vertices.",
        "Which solids have all faces the same shape?",
        "Sketch a net for a cuboid and count the rectangles. How many different "
        "rectangles are there?"]),
    ST("05", "EXPLAIN"),
    DEF("A `face` is a flat surface, an `edge` is where two faces meet, and a "
        "`vertex` is a corner where edges meet. A `net` is a flat pattern that folds "
        "to make the solid. For any convex polyhedron, `V` \u2212 `E` + `F` = 2 "
        "(Euler's relationship)."),
    H("Naming solids"),
    TABLE(["Solid", "Defining property", "Examples"], [
        ["Prism", "uniform cross-section, flat ends", "cuboid, triangular prism"],
        ["Cylinder", "uniform circular cross-section", "tin, pipe, tank"],
        ["Pyramid", "flat base, triangular faces meeting at an apex", "Egyptian "
         "pyramid"],
        ["Cone", "circular base, curved surface to an apex", "ice-cream cone"],
        ["Sphere", "every point the same distance from the centre", "ball, globe"],
    ], widths=[0.8, 1.7, 1.5], fs=8.6),
    WE("8.1.1", "Using Euler's relationship",
       "A solid has 12 faces and 30 edges. How many vertices does it have?",
       ["Euler's relationship is `V` \u2212 `E` + `F` = 2.",
        "Substitute: `V` \u2212 30 + 12 = 2.",
        "So `V` \u2212 18 = 2 and `V` = 20.",
        "Check: 20 \u2212 30 + 12 = 2, as required."],
       "20 vertices",
       "Substitute before rearranging; the arithmetic is less error-prone."),
    WE("8.1.2", "Counting a prism",
       "A prism has a hexagonal cross-section. Find its number of faces, edges and "
       "vertices, and check Euler's relationship.",
       ["A hexagon has 6 sides, so the ends are 2 faces and the sides are 6 rectangles: "
        "`F` = 8.",
        "Count the edges in three groups: 6 round the top, 6 round the bottom and 6 "
        "vertical, so `E` = 18.",
        "Each end has 6 vertices: `V` = 12.",
        "Check: 12 \u2212 18 + 8 = 2, as Euler requires."],
       "`F` = 8, `E` = 18, `V` = 12",
       "Counting in a system \u2014 all top edges, then all bottom, then all vertical "
       "\u2014 prevents double counting."),
    ERR("\u201cA cylinder has 2 faces, 0 edges and 0 vertices, so Euler's relationship "
        "fails.\u201d Euler's relationship applies to polyhedra, solids with flat "
        "faces only. A cylinder's curved surface is not a face in this sense, so the "
        "relationship is simply not being claimed here."),
    PRAC("8.1", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("State the number of faces, edges and vertices of (a) a cuboid (b) a "
          "triangular prism (c) a square-based pyramid.", "F"),
        Q("Check Euler's relationship for a cube.", "F"),
        Q("A solid has 12 faces and 30 edges. Find its number of vertices.", "F"),
        Q("How many squares are in the net of a cube?", "F"),
        Q("Name a solid with a uniform triangular cross-section.", "F"),
        Q("A hexagonal prism is cut along an edge and opened flat. How many rectangles "
          "and how many hexagons does the net contain?", "P"),
        Q("A tetrahedron has 4 faces. Find its edges and vertices and check Euler's "
          "relationship.", "P"),
        Q("Sketch a net for a cuboid 4 cm by 3 cm by 2 cm and label each rectangle "
          "with its dimensions.", "P"),
        Q("Two different solids both have 6 faces. Name them.", "R"),
        Q("A prism has an `n`-sided cross-section. Write expressions for its faces, "
          "edges and vertices, and show that Euler's relationship holds for every "
          "`n`.", "E"),
        Q("A solid has 5 faces and 8 edges. Identify it and find its vertices.", "E"),
        Q("Explain why a sphere cannot be unfolded into a net of flat faces.", "E"),
    ]),

    # ------------------------------------------------------------------ 8.2
    S("8.2", "Surface area", "A \u00b7 II  \u00b7  D \u00b7 II", ["Measurement",
      "Models"]),
    L("Surface area is the total area of the outside of a solid: the material you "
      "would need to make it. A net makes the calculation visible."),
    DIAG(200, "prism_net",
         "The net of a triangular prism. Each face appears exactly once, so the "
         "surface area is the sum of five flat areas."),
    KEY("**Prism or cuboid:** surface area = sum of the areas of all faces.\n"
        "**Cylinder (closed):** `S` = 2\u03c0`r`\u00b2 + 2\u03c0`r``h` \u2014 two "
        "circles plus the curved rectangle.\n**Cylinder (open top):** omit one circle, "
        "`S` = \u03c0`r`\u00b2 + 2\u03c0`r``h`."),
    DIAG(190, "cylinder_net",
         "The curved surface of a cylinder unrolls into a rectangle of width 2\u03c0r "
         "and height h, which is why the curved area is 2\u03c0rh."),
    WE("8.2.1", "A cuboid",
       "Find the surface area of a cuboid measuring 8 cm by 5 cm by 3 cm.",
       ["The three pairs of faces have areas 8\u00d75 = 40, 8\u00d73 = 24 and "
        "5\u00d73 = 15 cm\u00b2.",
        "Each area occurs twice: 2(40 + 24 + 15).",
        "= 2 \u00d7 79 = 158 cm\u00b2.",
        "Check by imagining the net: six rectangles, three sizes, each repeated."],
       "158 cm\u00b2",
       "Adding the three different face areas first, then doubling, is faster than six "
       "separate calculations."),
    WE("8.2.2", "A closed cylinder",
       "Find the surface area of a closed cylinder of radius 5 cm and height 12 cm, "
       "using \u03c0 = 3.14.",
       ["Two circular ends: 2 \u00d7 3.14 \u00d7 5\u00b2 = 157 cm\u00b2.",
        "Curved surface: 2\u03c0`r``h` = 2 \u00d7 3.14 \u00d7 5 \u00d7 12 = 376.8 "
        "cm\u00b2.",
        "Total = 157 + 376.8 = 533.8 cm\u00b2.",
        "Check the curved area as a rectangle 31.4 cm by 12 cm: 376.8 cm\u00b2."],
       "533.8 cm\u00b2",
       "If the cylinder has no lid, subtract one circle \u2014 that is 78.5 cm\u00b2 "
       "less."),
    WE("8.2.3", "A triangular prism",
       "A triangular prism has a right-angled triangular cross-section with legs 3 cm "
       "and 4 cm, and length 10 cm. Find its surface area.",
       ["Cross-section area = \u00bd \u00d7 3 \u00d7 4 = 6 cm\u00b2; two ends give 12 "
        "cm\u00b2.",
        "The hypotenuse is 5 cm (3-4-5 triangle), so the perimeter of the end is 3 + 4 "
        "+ 5 = 12 cm.",
        "The three rectangular sides have total area 12 \u00d7 10 = 120 cm\u00b2.",
        "Surface area = 12 + 120 = 132 cm\u00b2."],
       "132 cm\u00b2",
       "The perimeter of the cross-section \u00d7 length gives all the rectangular "
       "faces at once."),
    ERR("\u201cThe surface area of a cylinder is 2\u03c0`r``h`, because that is the "
        "only curved part.\u201d The two circular ends are also surface: omitting them "
        "loses 2\u03c0`r`\u00b2, which for `r` = 5 cm is 157 cm\u00b2 \u2014 nearly a "
        "third of the total."),
    PRAC("8.2", "SUPPORT 1\u20135  \u00b7  CORE 6\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Find the surface area of a cuboid 8 cm by 5 cm by 3 cm.", "F"),
        Q("Find the surface area of a cube of edge 7 cm.", "F"),
        Q("Find the surface area of a closed cylinder with `r` = 5 cm and `h` = 12 cm.",
          "F"),
        Q("Find the surface area of a closed cylinder with `r` = 7 cm and `h` = 10 "
          "cm.", "F"),
        Q("An open cylinder (no lid) has `r` = 4 cm and `h` = 9 cm. Find its surface "
          "area.", "F"),
        Q("A triangular prism has a right-angled end with legs 3 cm and 4 cm, and "
          "length 10 cm. Find its surface area.", "P"),
        Q("Find the surface area of a cuboid 12 cm by 7 cm by 4 cm.", "P"),
        Q("A water tank is an open cylinder of radius 0.5 m and height 2 m. Find the "
          "area of metal used.", "P"),
        Q("A cube has surface area 150 cm\u00b2. Find its edge length and its volume.",
          "P"),
        Q("Two cylinders have the same height. One has twice the radius of the other. "
          "How many times greater is its curved surface area? Justify your answer.",
          "R"),
        Q("A cylinder is twice as tall as its radius. Write its surface area in terms "
          "of `r` only.", "E"),
        Q("A box with no lid is made from a single sheet of card 20 cm square by "
          "cutting 4 cm squares from each corner and folding up the sides. Find its "
          "surface area.", "E"),
    ]),

    # ------------------------------------------------------------------ 8.3
    S("8.3", "Volume of prisms and cylinders", "A \u00b7 III  \u00b7  D \u00b7 III",
      ["Measurement", "Form"]),
    L("Volume measures the space inside a solid. For any prism, one multiplication of "
      "the cross-section by the length settles it."),
    KEY("**Prism:** `V` = area of cross-section \u00d7 length.\n**Cuboid:** `V` = "
        "`l`\u00d7`w`\u00d7`h`. **Cylinder:** `V` = \u03c0`r`\u00b2`h`.\n**Cone:** "
        "`V` = \u2153\u03c0`r`\u00b2`h`. **Sphere:** `V` = \u2154\u03c0`r`\u00b3.\n"
        "**Capacity:** 1 litre = 1000 cm\u00b3 = 0.001 m\u00b3."),
    DIAG(190, "tank_sketch",
         "A rectangular tank partly filled. The capacity in litres is the volume in "
         "cubic centimetres divided by 1000."),
    PHOTO("ch08_tank.jpg", 0.78,
          "A cylindrical storage tank. Its capacity is \u03c0r\u00b2h; its material "
          "cost is the surface area of the same cylinder.",
          "Photograph: Pexels, free to use under the Pexels licence.", 0.68),
    WE("8.3.1", "Cuboid and prism",
       "Find the volume of (a) a cuboid 6 cm by 4 cm by 2 cm and (b) a prism whose "
       "cross-section has area 12 cm\u00b2 and whose length is 7 cm.",
       ["(a) Volume = 6 \u00d7 4 \u00d7 2 = 48 cm\u00b3.",
        "(b) Volume = cross-section \u00d7 length = 12 \u00d7 7 = 84 cm\u00b3.",
        "Both answers are in cubic centimetres: three lengths were multiplied.",
        "Check (b) by imagining seven slices each 12 cm\u00b2 thick."],
       "(a) 48 cm\u00b3 (b) 84 cm\u00b3",
       "Slice-and-stack is the meaning of volume; the formula is just the shortcut."),
    WE("8.3.2", "A cylinder, and a capacity",
       "A cylindrical tank has diameter 1 m and height 2 m. Find its volume in cubic "
       "metres and its capacity in litres, using \u03c0 = 3.14.",
       ["Radius = 0.5 m.",
        "Volume = \u03c0`r`\u00b2`h` = 3.14 \u00d7 0.25 \u00d7 2 = 1.57 m\u00b3.",
        "1 m\u00b3 = 1000 litres, so the capacity is 1570 litres.",
        "Check: 0.5 m radius gives a cross-section of 0.785 m\u00b2, and two metres of "
        "depth doubles it."],
       "1.57 m\u00b3 = 1570 litres",
       "Convert after computing; converting first multiplies the chance of error."),
    WE("8.3.3", "Working backwards",
       "A cylinder of radius 5 cm has volume 314 cm\u00b3. Find its height.",
       ["`V` = \u03c0`r`\u00b2`h`, so 314 = 3.14 \u00d7 25 \u00d7 `h`.",
        "3.14 \u00d7 25 = 78.5, so `h` = 314 \u00f7 78.5 = 4.",
        "The height is 4 cm.",
        "Check: 78.5 \u00d7 4 = 314, as given."],
       "4 cm",
       "Divide by the area of the base: height = volume \u00f7 base area."),
    ERR("\u201cA tank 1 m by 1 m by 1 m holds 100 litres.\u201d It holds 1000 litres: "
        "1 m\u00b3 = 100 \u00d7 100 \u00d7 100 cm\u00b3 = 1 000 000 cm\u00b3, and each "
        "litre is 1000 cm\u00b3. Volume units convert by cubes of the length "
        "conversion, not by the conversion itself."),
    PRAC("8.3", "SUPPORT 1\u20135  \u00b7  CORE 6\u201310  \u00b7  EXTENSION "
                "11\u201313", [
        Q("Find the volume of a cuboid 6 cm by 4 cm by 2 cm.", "F"),
        Q("Find the volume of a cube of edge 5 cm.", "F"),
        Q("Find the volume of a prism with cross-section area 12 cm\u00b2 and length 7 "
          "cm.", "F"),
        Q("Find the volume of a cylinder with `r` = 3 cm and `h` = 10 cm.", "F"),
        Q("Find the volume of a cylinder with diameter 14 cm and height 20 cm.", "F"),
        Q("A cylinder of radius 5 cm has volume 314 cm\u00b3. Find its height.", "P"),
        Q("A tank is a cylinder of radius 0.5 m and height 2 m. Find its capacity in "
          "litres.", "P"),
        Q("A prism has a trapezium cross-section with parallel sides 6 cm and 4 cm and "
          "height 3 cm. Its length is 8 cm. Find its volume.", "P"),
        Q("A cuboid has volume 240 cm\u00b3, length 8 cm and width 5 cm. Find its "
          "height.", "P"),
        Q("A cube has the same numerical value for its volume and its surface area. "
          "Find its edge length.", "R"),
        Q("Find the volume of a cone with `r` = 3 cm and `h` = 7 cm.", "E"),
        Q("Find the volume of a sphere of radius 6 cm.", "E"),
        Q("A tap fills a 3-litre container every minute. How long does it take to fill "
          "a cylinder of radius 20 cm and height 50 cm? Give your answer in minutes "
          "and seconds.", "E"),
    ]),

    # ------------------------------------------------------------------ 8.4
    S("8.4", "Composite solids", "C \u00b7 III  \u00b7  D \u00b7 IV", ["Form",
      "Models"]),
    L("Most manufactured objects are combinations of simple solids. Splitting them "
      "correctly decides whether the answer is right."),
    DIAG(180, "composite_solid",
         "An L-shaped solid treated as two prisms. Adding the parts works for volume; "
         "for surface area the shared faces must be removed."),
    P("Volumes add without complication, because the parts do not overlap. Surface "
      "areas do not: where two solids are joined, the faces that touch disappear from "
      "the surface, and both must be subtracted."),
    WE("8.4.1", "Two cuboids",
       "A solid is made by stacking a cuboid 8 cm by 5 cm by 3 cm on a cuboid 8 cm by "
       "5 cm by 2 cm. Find its volume and its surface area.",
       ["Volumes add: 8\u00d75\u00d73 = 120 and 8\u00d75\u00d72 = 80, total 200 "
        "cm\u00b3.",
        "Surface areas separately: 2(40 + 24 + 15) = 158 and 2(40 + 16 + 10) = 132, "
        "total 290 cm\u00b2.",
        "The joined faces are two 8 \u00d7 5 rectangles, 40 cm\u00b2 each, and both "
        "disappear: subtract 80.",
        "Surface area = 290 \u2212 80 = 210 cm\u00b2."],
       "200 cm\u00b3; 210 cm\u00b2",
       "Only the contact faces vanish, not the whole of each solid's base."),
    WE("8.4.2", "A hole through a solid",
       "A cuboid 20 cm by 10 cm by 6 cm has a cylindrical hole of radius 2 cm drilled "
       "right through it. Find the volume of material remaining.",
       ["Cuboid volume = 20 \u00d7 10 \u00d7 6 = 1200 cm\u00b3.",
        "Cylinder volume = \u03c0 \u00d7 2\u00b2 \u00d7 6 = 3.14 \u00d7 4 \u00d7 6 = "
        "75.36 cm\u00b3.",
        "Remaining = 1200 \u2212 75.36 = 1124.64 cm\u00b3.",
        "The hole is 6 cm long because it goes through the 6 cm thickness."],
       "1124.64 cm\u00b3",
       "The length of the hole equals the dimension it passes through, not the "
       "largest dimension."),
    WE("8.4.3", "A swimming pool",
       "A pool is 25 m long, 10 m wide and 2 m deep, filled to 10 cm below the top. "
       "Find the volume of water in litres.",
       ["Water depth = 2 \u2212 0.1 = 1.9 m.",
        "Volume = 25 \u00d7 10 \u00d7 1.9 = 475 m\u00b3.",
        "1 m\u00b3 = 1000 litres, so the water is 475 000 litres.",
        "Check the full capacity: 500 m\u00b3 = 500 000 litres, and 475 000 is "
        "plausibly less."],
       "475 000 litres",
       "Read the depth given, not the depth of the pool: the question says how full it "
       "is."),
    ERR("\u201cThe surface area of the stacked solid is the sum of the two surface "
        "areas, because stacking does not change either one.\u201d Stacking hides two "
        "rectangles \u2014 one from each solid \u2014 so the total falls. Only volume "
        "is unaffected by joining."),
    PRAC("8.4", "SUPPORT 1\u20134  \u00b7  CORE 5\u20139  \u00b7  EXTENSION "
                "10\u201312", [
        Q("Two cuboids measure 8\u00d75\u00d73 cm and 8\u00d75\u00d72 cm and are "
          "stacked. Find the total volume.", "F"),
        Q("A cuboid 20\u00d710\u00d76 cm has a cylindrical hole of radius 2 cm through "
          "its 6 cm thickness. Find the remaining volume.", "F"),
        Q("Two cubes of edge 4 cm are glued face to face. Find the total surface "
          "area.", "F"),
        Q("A pool is 25 m by 10 m by 2 m. Find its volume in litres.", "F"),
        Q("A solid is a cuboid 12 cm by 6 cm by 4 cm with a 6 cm by 3 cm by 4 cm notch "
          "removed. Find its volume.", "P"),
        Q("A cylindrical tank of radius 30 cm and height 100 cm is half full. Find the "
          "volume of water in litres.", "P"),
        Q("A room is 5 m by 4 m by 2.5 m. Find the area of its four walls, excluding "
          "floor and ceiling.", "P"),
        Q("Paint covers 10 m\u00b2 per litre. How many litres are needed for two coats "
          "on the four walls of the room in question 7?", "P"),
        Q("A student says doubling every dimension of a cuboid doubles its volume. Test "
          "the claim with a 2\u00d73\u00d74 cm cuboid.", "R"),
        Q("A capsule is a cylinder of radius 2 cm and length 6 cm with a hemisphere "
          "added at each end. Find its total volume.", "E"),
        Q("A garden water butt is a cylinder of diameter 80 cm and height 1.1 m. How "
          "many litres does it hold when full?", "E"),
        Q("A concrete step is 1.2 m wide, 30 cm deep and 15 cm high. A path needs 12 "
          "identical steps. Find the total volume of concrete, in m\u00b3.", "E"),
    ]),

    CARD_D("The packaging brief", [
        ("p", "A small business sells tea in 250 g packs. Each pack must hold 250 "
              "cm\u00b3, and the box must be a cuboid with a square base of side `x` "
              "cm and height `h` cm. Card costs \u00a30.004 per cm\u00b2."),
        ("ol", ["Write `h` in terms of `x`, given that the volume is 250 cm\u00b3.",
                "Write the surface area of the closed box in terms of `x`.",
                "Complete a table of surface area for `x` = 4, 5, 6, 7 and 8 cm.",
                "Which of these sizes uses least card? What is the cost per box?",
                "Explain why the surface area does not keep falling as `x` "
                "increases.",
                "Recommend a size, and state one practical reason for choosing a size "
                "that is not the mathematical minimum."]),
    ]),

    # ----------------------------------------------------------- investigate
    ST("06", "INVESTIGATE AND APPLY",
       "Scaling, and the shape that saves material."),
    CARD_I("Doubling everything", [
        ("p", "A model is built at twice the size of the original. Only some of its "
              "measurements double."),
        ("ol", ["Take a cube of edge 1 cm and record its surface area and volume.",
                "Repeat for edges 2, 3 and 4 cm.",
                "Record the ratios of surface area and volume to the original.",
                "Write each measurement as a formula in the edge length `s`.",
                "Explain why volume grows eightfold when the edge doubles.",
                "A 30 cm pizza is sold for \u00a39 and a 40 cm pizza for \u00a314. "
                "Which is better value per cm\u00b2 of pizza?",
                "Write one sentence on why large animals need thicker legs relative to "
                "their size."]),
    ]),
    CARD_I("The cheapest can", [
        ("p", "A drinks can must hold 330 cm\u00b3. Its radius and height can vary, but "
              "the volume is fixed."),
        ("ol", ["Write `h` in terms of `r` for a fixed volume of 330 cm\u00b3.",
                "Write the surface area of the closed can in terms of `r`.",
                "Complete a table of surface area for `r` = 2.5, 3, 3.5, 4 and 4.5 "
                "cm.",
                "Identify the radius that gives the least surface area.",
                "Measure a real 330 cm\u00b3 can and compare its dimensions with your "
                "answer.",
                "Explain one reason manufacturers might not use the "
                "material-minimising shape.",
                "Describe what your table shows about the shape of the graph of "
                "surface area against radius."]),
    ]),

    # --------------------------------------------------------------- review
    ST("07", "REFLECT AND CONSOLIDATE"),
    S("8.6", "Summary, revision and reflection", None, []),
    H("What this chapter established"),
    UL(["Solids are described by faces, edges and vertices; `V` \u2212 `E` + `F` = 2 "
        "for polyhedra.",
        "A net shows every face once, so it turns surface area into a sum of flat "
        "areas.",
        "Surface area of a closed cylinder is 2\u03c0`r`\u00b2 + 2\u03c0`r``h`; an "
        "open one loses a circle.",
        "Volume of any prism is cross-section \u00d7 length; a cylinder is the same "
        "rule with a circular cross-section.",
        "1 litre = 1000 cm\u00b3 and 1 m\u00b3 = 1000 litres.",
        "Volumes of joined solids add; surface areas do not, because contact faces are "
        "hidden."]),
    VOCAB("**face** \u00b7 **edge** \u00b7 **vertex** \u00b7 **net** \u00b7 "
          "**prism** \u00b7 **cross-section** \u00b7 **surface area** \u00b7 "
          "**volume** \u00b7 **capacity** \u00b7 **composite solid** \u00b7 "
          "**Euler's relationship**"),
    H("Misconceptions to close"),
    TABLE(["The mistake", "What is really happening"], [
        ["Forgetting the two circular ends of a cylinder.",
         "They are surface too; only an open top removes one circle."],
        ["Using the diameter in \u03c0`r`\u00b2.",
         "Halve it first; otherwise the answer is four times too large."],
        ["Adding surface areas of joined solids.",
         "Contact faces are no longer on the surface and must be subtracted twice."],
        ["Converting m\u00b3 to litres by multiplying by 100.",
         "1 m\u00b3 = 1000 litres; volume conversions use cubes of the length "
         "conversion."],
    ], widths=[1.55, 1.95]),
    H("Revision questions"),
    OL(["Find the surface area of a cube of edge 9 cm.",
        "Find the volume of a cylinder with `r` = 4 cm and `h` = 15 cm.",
        "A cuboid has volume 180 cm\u00b3, length 9 cm and width 5 cm. Find its "
        "height.",
        "A tank holds 2.4 m\u00b3. How many litres is that?",
        "Two cubes of edge 5 cm are joined face to face. Find the surface area of the "
        "result."]),
    GAP(6),
    H("Before you move on"),
    P("Four things you should be able to do without help before the next "
      "chapter. If one of them is not yet secure, reread the section that "
      "taught it before attempting the mixed practice again.", 4),
    UL([
        "Count faces, edges and vertices and check Euler's relationship.",
        "Unfold a solid into a net and use the net to find surface area.",
        "Find the volume of a prism, cylinder, cone or sphere.",
        "Handle a composite solid by adding or subtracting the parts.",
    ]),
    KEY("Surface area is a two-dimensional measurement of a three-dimensional object; volume is the space it encloses."),
    H("Self-assessment"),
    TABLE(["I can \u2026", "Not yet", "Getting there", "Confident"], [
        ["count faces, edges and vertices and use Euler's relationship", "\u25a1",
         "\u25a1", "\u25a1"],
        ["find the surface area of a prism from its net", "\u25a1", "\u25a1",
         "\u25a1"],
        ["find the surface area of a closed or open cylinder", "\u25a1", "\u25a1",
         "\u25a1"],
        ["find the volume of a prism, cylinder, cone or sphere", "\u25a1", "\u25a1",
         "\u25a1"],
        ["convert between cm\u00b3, m\u00b3 and litres", "\u25a1", "\u25a1",
         "\u25a1"],
        ["handle a composite solid's volume and surface area", "\u25a1", "\u25a1",
         "\u25a1"],
    ], widths=[2.6, 0.55, 0.65, 0.65], font_size=8.6),
    GAP(8),
    MYP("**Criterion A:** which formula can you now choose without prompting?\n"
        "**Criterion B:** what did the scaling investigation show you about powers?\n"
        "**Criterion C:** did your units and diagrams communicate the method?\n"
        "**Criterion D:** how did a calculation change a design decision?",
        "Reflect on the criteria"),
    ATL("In order for a student to model a container, students must decide whether the "
        "question asks for material or capacity, then justify the formula and the "
        "units.", "ATL \u00b7 Transfer skills"),
    H("Mixed practice \u00b7 consolidate and extend"),
    PRAC("8.M", "MIXED 1\u201312", [
        Q("State the number of edges of a triangular prism.", "F"),
        Q("Find the volume of a cuboid 9 cm by 6 cm by 5 cm.", "F"),
        Q("Find the surface area of a cube of edge 7 cm.", "F"),
        Q("Find the volume of a cylinder with `r` = 5 cm and `h` = 8 cm.", "F"),
        Q("How many litres are in 2.5 m\u00b3?", "F"),
        Q("A cylinder has volume 942 cm\u00b3 and height 12 cm. Find its radius.",
          "P"),
        Q("A cuboid 15 cm by 8 cm by 5 cm is painted on all faces. Find the painted "
          "area.", "P"),
        Q("A cylinder with no lid has `r` = 10 cm and `h` = 14 cm. Find its surface "
          "area.", "P"),
        Q("A student says a cube of edge 2 cm has twice the volume of a cube of edge 1 "
          "cm. Correct the statement.", "R"),
        Q("A fish tank is 60 cm long, 30 cm wide and 40 cm deep, filled to 5 cm below "
          "the top. How many litres of water does it hold?", "E"),
        Q("A cone and a cylinder have the same radius and height. How many cones fill "
          "the cylinder? Justify with the formulas.", "E"),
        Q("A cylindrical pipe has outer diameter 10 cm and inner diameter 8 cm, and is "
          "1 m long. Find the volume of metal in the pipe.", "E"),
    ]),
]

ANSWERS = {
    "8.1": ["(a) 6, 12, 8 (b) 5, 9, 6 (c) 5, 8, 5.", "8 \u2212 12 + 6 = 2, so it "
            "holds.", "20.", "Six.", "A triangular prism.",
            "Six rectangles and two hexagons: eight faces in the net.",
            "`E` = 6, `V` = 4, and 4 \u2212 6 + 4 = 2.",
            "A cross of six rectangles; the two 4\u00d73 faces, two 4\u00d72 and two "
            "3\u00d72.",
            "A cuboid and a square-based pyramid (both have 6 faces).",
            "`F` = `n` + 2, `E` = 3`n`, `V` = 2`n`, and 2`n` \u2212 3`n` + `n` + 2 = "
            "2.",
            "A square-based pyramid; `V` = 5.",
            "A sphere has no flat faces and no edges, so it cannot be unfolded into a "
            "net of polygons."],
    "8.2": ["158 cm\u00b2.", "294 cm\u00b2.", "533.8 cm\u00b2.", "747.32 cm\u00b2.",
            "276.32 cm\u00b2.", "132 cm\u00b2.", "320 cm\u00b2.", "7.065 m\u00b2.",
            "Edge 5 cm; volume 125 cm\u00b3.",
            "Twice: the curved area is 2\u03c0`r``h`, which is proportional to `r`.",
            "`S` = 2\u03c0`r`\u00b2 + 4\u03c0`r`\u00b2 = 6\u03c0`r`\u00b2.",
            "The base is 12 cm by 12 cm and the four sides are 12 cm by 4 cm: 144 + "
            "192 = 336 cm\u00b2."],
    "8.3": ["48 cm\u00b3.", "125 cm\u00b3.", "84 cm\u00b3.", "282.6 cm\u00b3.",
            "3077.2 cm\u00b3.", "4 cm.", "1570 litres.", "120 cm\u00b3.",
            "6 cm.", "6 cm, since 6\u00b3 = 216 and 6 \u00d7 6\u00b2 = 216.",
            "65.94 cm\u00b3.", "904.32 cm\u00b3.",
            "Volume = 62 800 cm\u00b3 \u2248 62.8 litres, so 20.9 minutes, about 20 "
            "minutes 56 seconds."],
    "8.4": ["200 cm\u00b3.", "1124.64 cm\u00b3.", "160 cm\u00b2.",
            "500 000 litres.", "216 cm\u00b3.", "141.3 litres.", "45 m\u00b2.",
            "9 litres.", "Volume becomes 8 times: 192 cm\u00b3 against 24 cm\u00b3.",
            "Cylinder 3.14 \u00d7 4 \u00d7 6 = 75.36 cm\u00b3; the two hemispheres make "
            "one sphere, \u2154 \u00d7 3.14 \u00d7 8 = 33.49 cm\u00b3; total "
            "108.85 cm\u00b3.",
            "\u03c0 \u00d7 40\u00b2 \u00d7 110 = 552 640 cm\u00b3 \u2248 553 "
            "litres.",
            "0.054 m\u00b3 per step, so 0.648 m\u00b3 for twelve steps."],
    "8.M": ["9.", "270 cm\u00b3.", "294 cm\u00b2.", "628 cm\u00b3.", "2500 litres.",
            "`r` = 5 cm.", "470 cm\u00b2.", "1193.2 cm\u00b2.",
            "It has 8 times the volume, because 2\u00b3 = 8.",
            "60 \u00d7 30 \u00d7 35 = 63 000 cm\u00b3 = 63 litres.",
            "Three: the cone is \u2153\u03c0`r`\u00b2`h` and the cylinder "
            "\u03c0`r`\u00b2`h`.",
            "3.14 \u00d7 (25 \u2212 16) \u00d7 100 = 2826 cm\u00b3."],
}
