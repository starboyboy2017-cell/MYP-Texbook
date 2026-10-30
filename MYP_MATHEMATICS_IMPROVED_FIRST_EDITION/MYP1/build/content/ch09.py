"""Chapter 9 - Perimeter, area, surface area and volume."""
from bookkit.blocks import Stage, DataTable, Panel
from bookkit.flow import Spacer, Pager
import diagrams as dg
from helpers import (section, lead, body, h3, lst, panel, atl, we, practice, q, fig,
                     diag, table, note, gap, criteria_panel, reset_counters,
                     assessment_close)

PLATE = dict(
    part="Part IV \u00b7 Describing space and belonging", part_numeral="IV", chapter_no=9,
    kicker="Describing space and belonging",
    title_lines=["Perimeter, area and", "the space inside"],
    lead_lines=["Perimeter is a length, area is a surface, volume is a space.",
                "Mixing them up is the most common error in measurement, and",
                "the units are what keep them apart: one dimension, two,",
                "three."],
    key_concept="Relationships", related=["Quantity", "Space"],
    context="Orientation in space and time",
    inquiry_lines=["How do the units of a measurement show what kind of quantity is being",
                   "measured?"])

TITLE = "Perimeter, area, surface area and volume"
SHORT = "Perimeter, area and volume"


def build(bk, p):
    reset_counters(9)
    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("01", "MYP UNIT PLANNER"))
    p.add(Spacer(8))
    p.add(DataTable(["Statement of inquiry",
                     "Measurement converts shapes into numbers, and the relationship "
                     "between a shape and its dimensions determines which quantity is being "
                     "described."],
                    [], widths=[1, 3.2], font_size=9.2, stripe=False))
    gap(p, 10)
    p.add(Panel("keyidea", title="Key and related concepts",
                text="**Key concept \u00b7 Relationships.** Each formula relates dimensions "
                     "to a measured quantity; changing a dimension changes the quantity in "
                     "a predictable way.\n"
                     "**Related \u00b7 Quantity.** Length, area and volume are different "
                     "kinds of quantity, not different sizes of the same one.\n"
                     "**Related \u00b7 Space.** Area and volume describe how much space a "
                     "figure occupies."))
    p.add(Panel("note", title="Global context \u00b7 Orientation in space and time",
                text="Exploration: how a builder estimates material \u2014 paint by area, "
                     "edging by perimeter, concrete by volume \u2014 and what happens when "
                     "the three are confused."))
    gap(p, 8)
    h3(p, "Inquiry questions")
    lst(p, ["**Factual:** What are the units of length, area and volume, and how do they "
            "relate?",
            "**Conceptual:** Why does doubling a length multiply the area by four?",
            "**Debatable:** Should a price be quoted per unit length, per unit area or per "
            "unit volume?"])
    gap(p, 8)
    table(p, ["Criterion", "Strands", "Evidence in this chapter"], [
        ["A \u00b7 Knowing and understanding", "i, ii, iii",
         "Select and apply the correct formula with correct units."],
        ["B \u00b7 Investigating patterns", "i, ii, iii",
         "Investigate how area and volume change when dimensions change."],
        ["C \u00b7 Communicating", "i, ii, iii, iv",
         "Show working with units carried through every step."],
        ["D \u00b7 Applying mathematics", "i, ii, iii, iv",
         "Cost a real job and justify the estimate."],
    ], widths=[1.25, 0.55, 2.6])
    gap(p, 6)
    atl(p, "In order for a student to measure accurately, students must record the unit at "
           "every stage, not only at the end of a calculation.",
           "ATL \u00b7 Organisation skills")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("02", "ENGAGE", "Three questions, one shape."))
    body(p, "A rectangular courtyard is 8 m by 5 m. A tiler is asked how much edging is "
            "needed, how many square metres of paving are needed, and how much soil to fill "
            "a bed 30 cm deep over the whole area. The three answers use the same two "
            "numbers and are all different.")
    fig(p, "ch09_plate_banner.jpg",
        "A tiled courtyard: the same rectangle, measured three different ways, gives a "
        "length, an area and a volume.", wide=True)

    p.add(Stage("03", "EXPLORE", "Count the squares."))
    body(p, "Draw three rectangles on squared paper: 2 by 3, 4 by 3 and 4 by 6. Count the "
            "squares inside each and record the perimeter and area.")
    lst(p, ["Which rectangle has twice the perimeter of the first?",
            "Which has twice the area?",
            "Double both dimensions of the 2 by 3 rectangle. What happens to the "
            "perimeter, and what happens to the area?",
            "Write a sentence describing the difference."], ordered=True)
    diag(p, 96, dg.perimeter_area_grid, "Perimeter counts the edge; area counts the squares "
                                        "inside. Doubling both dimensions doubles the "
                                        "perimeter but quadruples the area.", wide=True)
    panel(p, "keyidea", title="The distinction that matters",
          text="Perimeter is measured in units of length. Area is measured in square units. "
               "Volume is measured in cubic units. The unit is not decoration; it is how you "
               "know which question you answered.")

    # --------------------------------------------------------------- 9.1
    section(p, "9.1", "Perimeter and circumference", "A \u00b7 i  \u00b7  C \u00b7 ii",
            ["Quantity", "Space"])
    panel(p, "definition", title="Perimeter",
          text="The **perimeter** of a shape is the total length of its boundary, measured "
               "in units of length. For a circle the boundary is called the "
               "**circumference**, and `C` = \u03c0`d` = 2\u03c0`r`.")
    table(p, ["Shape", "Perimeter"], [
        ["Rectangle", "`P` = 2(`l` + `w`)"],
        ["Square", "`P` = 4`s`"],
        ["Triangle", "`P` = `a` + `b` + `c`"],
        ["Circle", "`C` = \u03c0`d` = 2\u03c0`r`"],
    ], widths=[1.0, 1.6])
    diag(p, 104, dg.circle_parts_box, "The radius, diameter and circumference of a circle. "
                                  "Every point on the circle is the same distance from the "
                                  "centre.", wide=True)
    we(p, "9.1.1", "Perimeter of a rectangle",
       "Find the perimeter of a rectangle 8 m by 5 m.",
       ["`P` = 2(`l` + `w`)",
        "`P` = 2(8 + 5) = 2 \u00d7 13 = 26",
        "The unit is metres, because perimeter is a length."],
       answer="26 m",
       check="Adding all four sides gives 8 + 5 + 8 + 5 = 26 \u2713")
    we(p, "9.1.2", "Circumference",
       "Find the circumference of a circle with radius 7 cm, using \u03c0 \u2248 3.14.",
       ["`C` = 2\u03c0`r`",
        "`C` = 2 \u00d7 3.14 \u00d7 7",
        "`C` = 43.96 cm.",
        "Round sensibly: 44.0 cm to one decimal place."],
       answer="\u2248 44.0 cm",
       check="3.14 \u00d7 14 = 43.96, so the estimate 44 is reasonable \u2713")
    panel(p, "error", title="Using diameter where radius belongs",
          text="`C` = 2\u03c0`r` uses the radius. If the diameter is given, either halve it "
               "first or use `C` = \u03c0`d`. Using the diameter in the radius formula doubles "
               "the answer.")
    practice(p, "9.1", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Find the perimeter of a rectangle 12 cm by 7 cm.", "F"),
        q("Find the perimeter of a square of side 9 cm.", "F"),
        q("Find the circumference of a circle of diameter 10 cm (\u03c0 \u2248 3.14).", "F"),
        q("A triangle has sides 6 cm, 8 cm and 10 cm. Find its perimeter.", "F"),
        q("Explain how to find the perimeter of a shape with a missing side length.", "R"),
        q("A circular table has radius 60 cm. How much edging is needed to go round it?", "P"),
        q("A rectangular garden is 14 m by 9 m. Fencing costs 6.50 per metre. Find the cost "
          "of fencing the whole boundary.", "P"),
        q("Investigate: if you double every side of a rectangle, what happens to the "
          "perimeter? Explain why.", "E"),
    ])

    # --------------------------------------------------------------- 9.2
    section(p, "9.2", "Area of rectangles, triangles and parallelograms", "A \u00b7 ii  \u00b7  B \u00b7 i",
            ["Space", "Quantity"])
    panel(p, "definition", title="Area",
          text="**Area** is the amount of surface enclosed by a boundary, measured in "
               "square units. A square with side 1 cm has an area of 1 cm^{2}; 1 m^{2} "
               "contains 10 000 cm^{2}.")
    table(p, ["Shape", "Area", "Why"], [
        ["Rectangle", "`A` = `l` \u00d7 `w`", "Counting unit squares in a grid."],
        ["Parallelogram", "`A` = base \u00d7 perpendicular height",
         "A triangle cut from one end fits on the other, making a rectangle."],
        ["Triangle", "`A` = \u00bd \u00d7 base \u00d7 perpendicular height",
         "Two copies make a parallelogram."],
        ["Trapezium", "`A` = \u00bd \u00d7 (`a` + `b`) \u00d7 height",
         "Two copies make a parallelogram with base (`a` + `b`)."],
    ], widths=[0.9, 1.5, 1.6], fs=7.8)
    diag(p, 108, dg.area_formulae, "Each area formula is a rectangle in disguise: cut and "
                                    "rearrange, and the shape becomes `l` \u00d7 `w`.",
         wide=True)
    we(p, "9.2.1", "Area of a triangle",
       "Find the area of a triangle with base 9 cm and perpendicular height 4 cm.",
       ["`A` = \u00bd \u00d7 base \u00d7 height",
        "`A` = \u00bd \u00d7 9 \u00d7 4 = 18",
        "The unit is cm^{2}, because area is two-dimensional."],
       answer="18 cm^{2}",
       check="The triangle fits twice into a 9 \u00d7 4 rectangle of area 36 \u2713")
    we(p, "9.2.2", "A composite shape",
       "A shape is made from a 6 m by 4 m rectangle with a right-angled triangle of base "
       "6 m and height 3 m attached along the top. Find its area.",
       ["Rectangle: 6 \u00d7 4 = 24 m^{2}.",
        "Triangle: \u00bd \u00d7 6 \u00d7 3 = 9 m^{2}.",
        "Total: 24 + 9 = 33 m^{2}."],
       answer="33 m^{2}",
       check="Split the shape a different way and check the total is the same \u2713")
    panel(p, "error", title="Using a slant side as the height",
          text="The height in an area formula is always perpendicular to the base. In a "
               "parallelogram the slant side is longer than the height, so using it "
               "overestimates the area.")
    practice(p, "9.2", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Find the area of a rectangle 15 cm by 8 cm.", "F"),
        q("Find the area of a triangle with base 12 cm and height 5 cm.", "F"),
        q("Find the area of a parallelogram with base 7 m and height 4 m.", "F"),
        q("Convert 3 m^{2} to cm^{2}.", "F"),
        q("Explain why the area formula for a triangle contains a half.", "R"),
        q("A trapezium has parallel sides 6 cm and 10 cm and height 5 cm. Find its area.",
          "P"),
        q("A wall 4 m by 2.5 m has a window 1 m by 1 m. Find the area to be painted.", "P"),
        q("Investigate: if the sides of a rectangle are both doubled, by what factor does "
          "the area increase? Test with three examples and explain.", "E"),
    ])

    # --------------------------------------------------------------- 9.3
    section(p, "9.3", "Circles and composite shapes", "A \u00b7 iii  \u00b7  C \u00b7 iii",
            ["Space", "Relationships"])
    panel(p, "definition", title="Area of a circle",
          text="`A` = \u03c0`r`^{2}. The area depends on the square of the radius, so doubling "
               "the radius multiplies the area by four \u2014 not by two.")
    diag(p, 96, dg.circle_area, "A circle cut into many thin sectors and rearranged "
                                "approaches a rectangle of width \u03c0`r` and height `r`.",
         wide=True)
    we(p, "9.3.1", "Area of a circle",
       "Find the area of a circle of radius 5 cm, using \u03c0 \u2248 3.14.",
       ["`A` = \u03c0`r`^{2}",
        "`A` = 3.14 \u00d7 5^{2} = 3.14 \u00d7 25",
        "`A` = 78.5 cm^{2}."],
       answer="78.5 cm^{2}",
       check="The circle fits inside a 10 \u00d7 10 square of area 100 \u2713")
    we(p, "9.3.2", "A composite shape with a circle",
       "A circular pond of diameter 6 m sits in the centre of a square lawn 10 m by 10 m. "
       "Find the area of lawn visible.",
       ["Square: 10 \u00d7 10 = 100 m^{2}.",
        "Radius of pond: 3 m, so area = 3.14 \u00d7 9 = 28.26 m^{2}.",
        "Lawn: 100 \u2212 28.26 = 71.74 m^{2}."],
       answer="\u2248 71.7 m^{2}",
       check="The pond is under a third of the square, so the answer must be over 66 m^{2} "
             "\u2713")
    practice(p, "9.3", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Find the area of a circle of radius 4 cm (\u03c0 \u2248 3.14).", "F"),
        q("Find the area of a circle of diameter 10 cm.", "F"),
        q("Find the area of a semicircle of radius 6 cm.", "F"),
        q("A circle has area 50.24 cm^{2}. Estimate its radius.", "F"),
        q("Explain why doubling the radius of a circle multiplies the area by four.", "R"),
        q("A running track is a rectangle 60 m by 20 m with a semicircle at each end. Find "
          "the total area.", "P"),
        q("A circular flower bed of diameter 4 m is surrounded by a path 1 m wide. Find the "
          "area of the path.", "P"),
        q("Investigate: how does the area of a circle change if the radius is trebled? Give "
          "a general rule.", "E"),
    ])

    # --------------------------------------------------------------- 9.4
    section(p, "9.4", "Surface area and volume of prisms", "A \u00b7 ii, iii  \u00b7  D \u00b7 iii",
            ["Space", "Quantity"])
    panel(p, "definition", title="Surface area and volume",
          text="The **surface area** of a solid is the total area of all its faces, in "
               "square units. The **volume** of a prism is the area of its cross-section "
               "multiplied by its length, in cubic units: `V` = `A` \u00d7 `l`.")
    diag(p, 112, dg.prism, "A prism has the same cross-section all along its length, which "
                            "is why volume is cross-section area times length.", wide=True)
    table(p, ["Solid", "Volume", "Surface area"], [
        ["Cuboid", "`V` = `l` \u00d7 `w` \u00d7 `h`", "`S` = 2(`lw` + `lh` + `wh`)"],
        ["Cube", "`V` = `s`^{3}", "`S` = 6`s`^{2}"],
        ["Triangular prism", "`V` = \u00bd`bh` \u00d7 `l`",
         "Two triangles plus three rectangles"],
        ["Cylinder", "`V` = \u03c0`r`^{2}`h`", "`S` = 2\u03c0`r`^{2} + 2\u03c0`rh`"],
    ], widths=[0.9, 1.3, 1.8], fs=7.8)
    we(p, "9.4.1", "Volume of a cuboid",
       "Find the volume of a box 30 cm by 20 cm by 15 cm.",
       ["`V` = `l` \u00d7 `w` \u00d7 `h`",
        "`V` = 30 \u00d7 20 \u00d7 15 = 9 000",
        "The unit is cm^{3}, because volume is three-dimensional."],
       answer="9 000 cm^{3}",
       check="9 000 cm^{3} = 9 litres, which is a plausible size for a storage box \u2713")
    we(p, "9.4.2", "Surface area of a cube",
       "Find the total surface area of a cube of side 5 cm.",
       ["Each face is 5 \u00d7 5 = 25 cm^{2}.",
        "A cube has six congruent faces.",
        "`S` = 6 \u00d7 25 = 150 cm^{2}."],
       answer="150 cm^{2}",
       check="Six faces, all identical, so multiplying one face by six is exact \u2713")
    panel(p, "error", title="Mixing units across dimensions",
          text="1 m^{2} is 10 000 cm^{2}, not 100 cm^{2}; 1 m^{3} is 1 000 000 cm^{3}. The "
               "conversion factor is squared or cubed along with the unit.")
    practice(p, "9.4", "SUPPORT 1\u20134  \u00b7  CORE 3\u20137  \u00b7  EXTENSION 6\u20138", [
        q("Find the volume of a cuboid 8 cm by 5 cm by 4 cm.", "F"),
        q("Find the volume of a cube of side 6 cm.", "F"),
        q("Find the surface area of a cube of side 3 cm.", "F"),
        q("Convert 2 000 cm^{3} to litres.", "F"),
        q("Explain the difference between surface area and volume using a box as an "
          "example.", "R"),
        q("A cylindrical tank has radius 1 m and height 2 m. Find its volume in litres "
          "(\u03c0 \u2248 3.14).", "P"),
        q("A fish tank 60 cm by 30 cm by 40 cm is filled to 80 % of its height. How many "
          "litres does it hold?", "P"),
        q("Investigate: if every edge of a cube is doubled, by what factor do the surface "
          "area and the volume change? Explain.", "E"),
    ])

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("04", "INVESTIGATE"))
    section(p, "Investigation 9", "Same perimeter, different area", None, ["Space", "Pattern"])
    body(p, "Using whole-number sides, find every rectangle with a perimeter of 20 cm. "
            "Record each length, width and area, then look for the pattern.")
    table(p, ["Length (cm)", "Width (cm)", "Area (cm^{2})"], [
        ["9", "1", "\u2026"], ["8", "2", "\u2026"], ["7", "3", "\u2026"],
        ["6", "4", "\u2026"], ["5", "5", "\u2026"],
    ], widths=[0.9, 0.9, 1.0])
    h3(p, "Your investigation")
    lst(p, ["Complete the table.",
            "Which rectangle has the largest area? The smallest?",
            "Describe the pattern in the area column as the sides become more equal.",
            "What happens with a perimeter of 24 cm? Test your description.",
            "State the rule in words, and explain why a square gives the largest area."],
        ordered=True)
    panel(p, "keyidea", title="The result",
          text="Among all rectangles with a given perimeter, the square has the largest "
               "area. This is why a fixed length of fencing encloses most ground when the "
               "enclosure is square \u2014 and why natural cells and bubbles tend towards "
               "round shapes, which do the same thing without corners.")
    atl(p, "In order for a student to generalise, students must test the boundary of a "
           "pattern, not only its middle cases.", "ATL \u00b7 Critical thinking")
    p.break_page()
    p.add(Stage("05", "APPLY"))
    section(p, "Real-life application", "The courtyard repair", "D \u00b7 i\u2013iv",
            ["Quantity", "Relationships"])
    body(p, "A school courtyard measures 18 m by 12 m. It needs new edging along the whole "
            "boundary, new paving over the whole surface, and a raised planting bed 1.5 m "
            "wide along one 12 m side, filled to a depth of 40 cm.")
    h3(p, "Your task")
    lst(p, ["Find the length of edging required.",
            "Find the area to be paved, allowing for a planting bed of the size described.",
            "Find the volume of soil needed for the bed, in cubic metres.",
            "Convert the soil volume to litres and decide how many 50-litre bags to order.",
            "Cost the job given: edging 9.20 per metre, paving 24 per m^{2}, soil 4.80 per "
            "bag.",
            "State two assumptions and one reason the real cost may differ."],
        ordered=True)
    panel(p, "criteria", title="Criterion D \u00b7 strands i\u2013iv",
          items=["Identify which quantity each part of the job requires.",
                 "Select perimeter, area or volume deliberately, with units.",
                 "Apply correctly and convert units consistently.",
                 "Justify the assumptions and evaluate the estimate."])
    gap(p, 8)
    p.add(Stage("06", "CRITERION-MAPPED MINI-TASK"))
    section(p, "Mini-task", "The packaging problem", "C \u00b7 i\u2013iv  \u00b7  D \u00b7 ii", [])
    body(p, "**Context.** A small business packs soap in cuboids and wants to reduce "
            "cardboard without reducing the volume of the box.")
    lst(p, ["Choose a cuboid with volume 1 000 cm^{3} and find its surface area.",
            "Find two other cuboids with the same volume and compare surface areas.",
            "Which shape uses least cardboard? Relate this to the investigation.",
            "Sketch the chosen net, labelling every dimension.",
            "Calculate the cardboard saved compared with the first design, as a "
            "percentage.",
            "Evaluate: what practical reasons might stop the business using the "
            "best mathematical shape?"], ordered=True)
    criteria_panel(p, c="i\u2013iv: clear working, correct units, labelled diagram.",
                   d="ii\u2013iv: strategy choice, application and evaluation of the "
                     "packaging decision.")
    diag(p, 122, dg.net_cube, "A net is the flat pattern a box folds from. The surface area "
                              "of the box is the area of this net, and it is what the "
                              "cardboard has to cover.", wide=True)

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("07", "REFLECT AND CONSOLIDATE"))
    section(p, "Review", "Chapter review", None, [])
    h3(p, "What this chapter established")
    lst(p, ["Perimeter is a length; circumference is the perimeter of a circle.",
            "Area is measured in square units, and each formula can be derived by "
            "rearranging a rectangle.",
            "The area of a circle is \u03c0`r`^{2}, so it grows with the square of the "
            "radius.",
            "Volume of a prism is cross-section area times length.",
            "Doubling every dimension multiplies area by 4 and volume by 8."])
    h3(p, "Vocabulary")
    table(p, ["Term", "Meaning"], [
        ["perimeter", "Total length of a boundary."],
        ["area", "Surface enclosed, in square units."],
        ["volume", "Space occupied, in cubic units."],
        ["cross-section", "The shape you see when a solid is cut straight through."],
        ["prism", "A solid with the same cross-section all along its length."],
        ["surface area", "Total area of all the faces of a solid."],
        ["capacity", "The volume a container can hold, often in litres."],
    ], widths=[1.0, 2.2])
    h3(p, "Misconceptions to watch")
    panel(p, "error", title="Three that persist", items=[
        "**Bigger perimeter means bigger area.** A long thin rectangle can have a large "
        "perimeter and a small area.",
        "**Area and perimeter share units.** One is in cm, the other in cm^{2}.",
        "**1 m^{2} = 100 cm^{2}.** It is 10 000 cm^{2}, because both dimensions convert.",
    ])
    assessment_close(p, [
            ["find the perimeter of a shape", "\u25a1", "\u25a1", "\u25a1"],
            ["use the circumference formula", "\u25a1", "\u25a1", "\u25a1"],
            ["find the area of triangles and quadrilaterals", "\u25a1", "\u25a1", "\u25a1"],
            ["find the area of a circle", "\u25a1", "\u25a1", "\u25a1"],
            ["find the volume of a prism", "\u25a1", "\u25a1", "\u25a1"],
            ["keep the units correct throughout", "\u25a1", "\u25a1", "\u25a1"],
        
    ],
        "In order for a student to check a measurement answer, students must ask "
               "whether the size and the unit are both plausible for the object.",
        next_title="Chapter 10 · Data, tables and graphs")

    bk.new_page("wide")
    p = Pager(bk)
    p.add(Stage("08", "MIXED PRACTICE"))
    practice(p, "Mixed practice 9",
             "SUPPORT 1\u20135  \u00b7  CORE 4\u201311  \u00b7  EXTENSION 9\u201314", [
        q("Find the perimeter of a rectangle 11 cm by 6 cm.", "F"),
        q("Find the area of a triangle with base 14 cm and height 6 cm.", "F"),
        q("Find the area of a circle of radius 8 cm (\u03c0 \u2248 3.14).", "F"),
        q("Find the volume of a cuboid 9 cm by 4 cm by 5 cm.", "F"),
        q("Convert 5 m^{2} to cm^{2}.", "F"),
        q("Explain why the area of a circle quadruples when the radius doubles.", "R"),
        q("A semicircle has diameter 12 cm. Find its perimeter and its area.", "R"),
        q("A garden 15 m by 10 m has a path 1 m wide all round inside its boundary. Find "
          "the area of the path.", "P"),
        q("A cylindrical drum of radius 40 cm and height 1 m is half full. How many litres "
          "does it contain?", "P"),
        q("A cube has volume 64 cm^{3}. Find its surface area.", "P"),
        q("A room is 4 m by 3 m and 2.5 m high. Find the area of the four walls, and the "
          "volume of the room.", "P"),
        q("A tin of paint covers 12 m^{2} per litre. How many litres are needed for two "
          "coats on four walls measuring 6 m by 2.5 m?", "E"),
        q("Investigate: for a fixed volume, compare the surface area of a cube with that of "
          "a long thin cuboid. Which uses less material?", "E"),
        q("Design a raised bed of volume 2 m^{3} that fits in a 3 m by 2 m space. Justify "
          "the dimensions you chose.", "E"),
    ])
    gap(p, 8)
    p.add(Stage("09", "CHECK YOUR PROGRESS"))
    table(p, ["Question", "If you cannot do this \u2026"], [
        ["1\u20135", "Revisit 9.1 and 9.2: decide the dimension before choosing a formula."],
        ["6\u20137", "Revisit 9.3: the radius is squared, not doubled."],
        ["8\u201311", "Revisit 9.4 and the composite-shape examples."],
        ["12\u201314", "Revisit the investigation and the packaging task."],
    ], widths=[0.7, 2.6])


ANSWERS = [
    ("9.1", "1 38 cm.  2 36 cm.  3 31.4 cm.  4 24 cm.  6 377 cm (\u2248 3.77 m).  "
            "7 46 m, so 299.00."),
    ("9.2", "1 120 cm^{2}.  2 30 cm^{2}.  3 28 m^{2}.  4 30 000 cm^{2}.  "
            "6 40 cm^{2}.  7 9 m^{2}."),
    ("9.3", "1 50.24 cm^{2}.  2 78.5 cm^{2}.  3 56.52 cm^{2}.  4 4 cm.  "
            "6 1 200 + 314 = 1 514 m^{2}.  7 15.7 m^{2} (28.26 \u2212 12.56)."),
    ("9.4", "1 160 cm^{3}.  2 216 cm^{3}.  3 54 cm^{2}.  4 2 litres.  "
            "6 6 280 litres.  7 57.6 litres."),
    ("Investigation 9", "Areas with perimeter 20 cm: 9, 16, 21, 24, 25 cm^{2}. The square "
                        "gives the largest area; the flatter the rectangle, the smaller the "
                        "area."),
    ("Mixed 9", "1 34 cm.  2 42 cm^{2}.  3 200.96 cm^{2}.  4 180 cm^{3}.  "
                "5 50 000 cm^{2}.  7 30.84 cm; 56.52 cm^{2}.  8 46 m^{2}.  "
                "9 251.2 litres.  10 96 cm^{2}.  11 35 m^{2}; 30 m^{3}.  "
                "12 2.5 litres.  13 The cube."),
]
