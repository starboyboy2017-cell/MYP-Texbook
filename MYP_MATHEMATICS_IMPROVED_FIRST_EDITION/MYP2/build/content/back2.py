"""Back matter: answers, formula bank, glossary, index, references."""
import importlib

from bookkit import spec, typeset
from bookkit.blocks import (PageTitle, DataTable, Panel, H3, Body, ListBlock, Lead,
                            AnswerLabel, AnswerEntry)
from bookkit.flow import Pager, Spacer, Rule
from bookkit.markup import plain
from bookkit.plates import _line

T = typeset.draw
L, R = spec.MARGIN_OUTER, spec.PAGE_W - spec.MARGIN_OUTER

ROMAN = {"R1": "I", "R2": "II", "R3": "III", "R4": "IV"}

CHAPTERS = [("ch01", "Ratios and equivalent ratios"),
            ("ch02", "Proportional reasoning"),
            ("ch03", "Rates and unit rates"),
            ("ch04", "Integers and operations"),
            ("ch05", "Algebraic expressions and equations"),
            ("ch06", "Numerical patterns and generalisation"),
            ("ch07", "2D geometry: angles, perimeter and area"),
            ("ch08", "3D geometry: solids, surface area and volume"),
            ("ch09", "Transformations and symmetry"),
            ("ch10", "Probability and simulation"),
            ("ch11", "Univariate data")]

# ------------------------------------------------------------------- glossary
GLOSSARY = [
    ("Absolute value", "The distance of a number from zero on the number line; it is "
                       "never negative."),
    ("Acute angle", "An angle smaller than 90\u00b0."),
    ("Algebraic expression", "A combination of numbers, letters and operations with "
                             "no equals sign."),
    ("Alternate angles", "Equal angles on opposite sides of a transversal crossing two "
                         "parallel lines."),
    ("Angle", "The amount of turn between two lines that meet at a point."),
    ("Arc", "A part of a circle's circumference."),
    ("Area", "The amount of surface enclosed by a boundary, measured in square units."),
    ("Average", "A single value used to summarise a set; mean, median and mode are the "
                "averages used here."),
    ("Bar chart", "A display in which the height of each bar shows the frequency of a "
                  "category."),
    ("Base (of a power)", "The number that is multiplied repeatedly."),
    ("Bias", "A systematic tendency in a sample or a question that makes a result "
             "unrepresentative."),
    ("Box plot", "A display of the five-figure summary: minimum, lower quartile, "
                 "median, upper quartile, maximum."),
    ("Capacity", "The volume a container can hold, often measured in litres."),
    ("Circumference", "The perimeter of a circle."),
    ("Common factor", "A number that divides two or more numbers exactly."),
    ("Complement (of an event)", "All the outcomes that are not in the event."),
    ("Composite shape", "A shape made by joining or removing simpler shapes."),
    ("Cone", "A solid with a circular base and a single vertex."),
    ("Congruent", "Exactly the same shape and size."),
    ("Constant", "A quantity whose value does not change in a given expression."),
    ("Constant of proportionality", "The fixed multiplier `k` in `y` = `k x`."),
    ("Coordinate", "A pair of numbers locating a point relative to two axes."),
    ("Corresponding angles", "Angles in the same position at each intersection of a "
                             "transversal with two lines."),
    ("Cross-product test", "Checking `a` : `b` = `c` : `d` by comparing `a d` with "
                           "`b c`."),
    ("Cube", "A solid with six congruent square faces; also a number multiplied by "
             "itself twice."),
    ("Cylinder", "A solid with two parallel circular faces joined by a curved "
                 "surface."),
    ("Decimal", "A number written using place value to the right of a decimal point."),
    ("Denominator", "The number below the line in a fraction: the number of equal "
                    "parts in the whole."),
    ("Density", "Mass per unit volume."),
    ("Diameter", "A straight line through the centre of a circle, joining two points "
                 "on the circumference."),
    ("Difference", "The result of subtracting one number from another."),
    ("Direct proportion", "A relationship in which one quantity is a constant "
                          "multiple of the other."),
    ("Enlargement", "A transformation that scales a shape by a factor from a centre."),
    ("Equation", "A statement that two expressions are equal."),
    ("Equivalent ratios", "Ratios related by multiplying or dividing both terms by "
                          "the same non-zero number."),
    ("Estimate", "A deliberately simplified calculation used to judge size."),
    ("Event", "A set of outcomes in a probability experiment."),
    ("Expand", "To multiply out brackets."),
    ("Exponent", "The number that shows how many copies of the base are multiplied."),
    ("Expression", "A mathematical phrase that can be evaluated but is not a "
                   "statement of equality."),
    ("Factor", "A whole number that divides another exactly; also, in algebra, one of "
               "the quantities multiplied."),
    ("Formula", "A rule written as an equation relating quantities."),
    ("Fraction", "A number written as one integer divided by another."),
    ("Frequency", "The number of times a value occurs."),
    ("Function machine", "A diagram showing a rule that turns an input into one "
                         "output."),
    ("Generalise", "To state a rule that covers every case, not just the ones "
                   "examined."),
    ("Highest common factor (HCF)", "The largest number that divides two or more "
                                    "numbers exactly."),
    ("Hypotenuse", "The side opposite the right angle in a right-angled triangle."),
    ("Improper fraction", "A fraction whose numerator is greater than its "
                          "denominator."),
    ("Integer", "A whole number, positive, negative or zero."),
    ("Interquartile range (IQR)", "The difference between the upper and lower "
                                  "quartiles."),
    ("Inverse operation", "An operation that undoes another."),
    ("Isosceles triangle", "A triangle with two equal sides and two equal angles."),
    ("Like terms", "Terms with the same letters raised to the same powers."),
    ("Lowest common multiple (LCM)", "The smallest number that is a multiple of two or "
                                     "more numbers."),
    ("Mean", "The total of the values divided by how many there are."),
    ("Median", "The middle value when the data are in order."),
    ("Mode", "The most frequent value."),
    ("Multiple", "The result of multiplying a number by an integer."),
    ("Negative number", "A number less than zero."),
    ("Net", "A flat pattern that folds to make a solid."),
    ("Outcome", "A single possible result of an experiment."),
    ("Parallel lines", "Lines in the same plane that never meet; their gradients are "
                       "equal."),
    ("Part-to-part ratio", "A ratio comparing two parts of a group."),
    ("Part-to-whole ratio", "A ratio comparing one part with the whole group."),
    ("Percentage", "A quantity expressed as a fraction of 100."),
    ("Perimeter", "The distance around the boundary of a shape."),
    ("Perpendicular", "Meeting at a right angle."),
    ("Pi (\u03c0)", "The constant ratio of a circle's circumference to its diameter, "
                    "approximately 3.14159."),
    ("Polygon", "A closed plane shape made of straight sides."),
    ("Prime number", "A whole number greater than 1 with exactly two factors."),
    ("Prism", "A solid with a constant cross-section."),
    ("Probability", "A number from 0 to 1 describing how likely an event is."),
    ("Proportion", "An equation stating that two ratios are equal."),
    ("Protractor", "An instrument for measuring angles in degrees."),
    ("Quadrilateral", "A polygon with four sides."),
    ("Quartile", "A value that divides an ordered data set into quarters."),
    ("Range (of data)", "The largest value minus the smallest."),
    ("Rate", "A ratio comparing quantities with different units."),
    ("Ratio", "A multiplicative comparison of two or more quantities."),
    ("Reciprocal", "The result of dividing 1 by a number."),
    ("Reflection", "A transformation that flips a shape over a line."),
    ("Relative frequency", "The number of times an event occurred divided by the "
                           "number of trials."),
    ("Rotation", "A transformation that turns a shape about a centre through an "
                 "angle."),
    ("Rounding", "Replacing a number by a nearby value with fewer significant "
                 "figures."),
    ("Sample space", "The set of all possible outcomes."),
    ("Scale drawing", "A drawing in which every length is a fixed multiple of the "
                      "real length."),
    ("Scale factor", "The multiplier linking corresponding lengths in similar "
                     "figures."),
    ("Scalene triangle", "A triangle with three unequal sides."),
    ("Simplify", "To write in an equivalent form with fewer terms or smaller "
                 "numbers."),
    ("Simultaneous", "Occurring together; not used for equations at this level."),
    ("Solid", "A three-dimensional figure enclosing volume."),
    ("Solve", "To find the value or values that make an equation true."),
    ("Speed", "Distance travelled per unit time."),
    ("Substitute", "To replace a letter with a number."),
    ("Surface area", "The total area of all the faces of a solid."),
    ("Symmetry", "A property of a shape that is unchanged by a reflection or "
                 "rotation."),
    ("Tally", "A count recorded in groups, usually of five."),
    ("Term", "One part of an expression, or one number in a ratio or sequence."),
    ("Tessellation", "A tiling of the plane by shapes with no gaps or overlaps."),
    ("Translation", "A transformation that slides a shape without turning it."),
    ("Transversal", "A line that crosses two or more other lines."),
    ("Unit rate", "A rate expressed for one unit of the first quantity."),
    ("Variable", "A letter standing for a number that may change."),
    ("Variable (in data)", "A quantity that is measured or recorded for each "
                           "individual."),
    ("Vertex", "A corner point of a shape or solid; plural vertices."),
    ("Volume", "The amount of space a solid occupies, in cubic units."),
    ("Whole number", "A number in the set 0, 1, 2, 3, \u2026"),
]

# --------------------------------------------------------------- formula bank
FORMULAS = [
    ("Ratio and proportion", [
        ("Ratio in simplest form", "`a` : `b` = `a`/\u00a0`k` : `b`/\u00a0`k`", None),
        ("Cross-product test", "`a` : `b` = `c` : `d` \u21d4 `a d` = `b c`", None),
        ("Sharing in a ratio", "one part = total \u00f7 (sum of the terms)", None),
        ("Direct proportion", "`y` = `k x`   (`k` constant)", None),
        ("Scale drawing", "real length = drawing length \u00d7 scale factor", None),
    ]),
    ("Rates", [
        ("Unit rate", "unit rate = quantity \u00f7 number of units", None),
        ("Speed", "`s` = `d`/\u00a0`t`", "distance \u00f7 time"),
        ("Distance", "`d` = `s t`", None),
        ("Time", "`t` = `d`/\u00a0`s`", None),
        ("Density", "density = mass \u00f7 volume", None),
        ("Flow rate", "time = capacity \u00f7 rate", None),
        ("Unit price", "unit price = price \u00f7 quantity", None),
    ]),
    ("Number and algebra", [
        ("Order of operations", "brackets, index, \u00d7 and \u00f7, + and \u2212",
         "left to right within a level"),
        ("Signed multiplication", "(+)(+) = +   (\u2212)(\u2212) = +   "
                                  "(+)(\u2212) = \u2212", None),
        ("Index laws", "`a`^{m} \u00d7 `a`^{n} = `a`^{m+n}", None),
        ("Expanding", "`a`(`b` + `c`) = `a b` + `a c`", None),
        ("Solving a linear equation", "do the same to both sides until the variable "
                                      "stands alone", None),
        ("Gradient of a line", "`m` = (\u0394`y`)/(\u0394`x`)", None),
        ("Linear sequence", "`n`th term = `a` + (`n` \u2212 1)`d`", "`a` first term, "
                                                                     "`d` common "
                                                                     "difference"),
        ("Percentage of an amount", "amount \u00d7 percentage \u00f7 100", None),
    ]),
    ("Geometry and measure", [
        ("Angles on a straight line", "sum to 180\u00b0", None),
        ("Angles at a point", "sum to 360\u00b0", None),
        ("Angle sum of a polygon", "(`n` \u2212 2) \u00d7 180\u00b0", None),
        ("Exterior angle of a polygon", "360\u00b0 \u00f7 `n`", None),
        ("Area of a rectangle", "`A` = `l w`", None),
        ("Area of a triangle", "`A` = \u00bd`b h`", None),
        ("Area of a parallelogram", "`A` = `b h`", None),
        ("Area of a trapezium", "`A` = \u00bd(`a` + `b`)`h`", None),
        ("Circumference of a circle", "`C` = \u03c0`d` = 2\u03c0`r`", None),
        ("Area of a circle", "`A` = \u03c0`r`\u00b2", None),
        ("Volume of a prism", "`V` = area of cross-section \u00d7 length", None),
        ("Volume of a cylinder", "`V` = \u03c0`r`\u00b2`h`", None),
        ("Surface area of a prism", "sum of the areas of all faces", None),
        ("Surface area of a cylinder", "2\u03c0`r`\u00b2 + 2\u03c0`r h`", None),
        ("Capacity", "1 litre = 1000 cm\u00b3", None),
    ]),
    ("Probability and statistics", [
        ("Theoretical probability", "`P`(`A`) = favourable outcomes \u00f7 total "
                                    "outcomes", None),
        ("Complement", "`P`(not `A`) = 1 \u2212 `P`(`A`)", None),
        ("Relative frequency", "`P`(`A`) \u2248 trials with `A` \u00f7 total trials",
         None),
        ("Independent events", "`P`(`A` then `B`) = `P`(`A`) \u00d7 `P`(`B`)", None),
        ("Mean", "mean = sum of values \u00f7 number of values", None),
        ("Range", "range = largest \u2212 smallest", None),
        ("Interquartile range", "IQR = upper quartile \u2212 lower quartile", None),
        ("Position of the median", "(\u2009`n` + 1\u2009) \u00f7 2 in an ordered "
                                  "list", None),
    ]),
]


# --------------------------------------------------------------------- index
INDEX_TERMS = [
    "absolute value", "acute angle", "algebraic expression", "alternate angles",
    "angle", "arc", "area", "average", "bar chart", "base", "bias", "box plot",
    "capacity", "circumference", "common factor", "complement", "composite shape",
    "congruent", "constant", "constant of proportionality", "coordinate",
    "corresponding angles", "cross-product", "cube", "cylinder", "decimal",
    "denominator", "density", "diameter", "direct proportion", "double number line",
    "enlargement", "equation", "equivalent ratio", "estimate", "event", "expand",
    "exponent", "expression", "factor", "formula", "fraction", "frequency",
    "function machine", "generalise", "gradient", "highest common factor",
    "integer", "interquartile range", "inverse operation", "isosceles",
    "like terms", "lowest common multiple", "mean", "median", "mode", "multiple",
    "net", "outcome", "parallel", "part-to-part", "part-to-whole", "percentage",
    "perimeter", "perpendicular", "pi", "polygon", "prime", "prism", "probability",
    "proportion", "protractor", "quadrilateral", "quartile", "range", "rate",
    "ratio", "ratio table", "reciprocal", "reflection", "relative frequency",
    "rotation", "rounding", "sample space", "scale drawing", "scale factor",
    "scalene", "simplest form", "solid", "speed", "substitute", "surface area",
    "symmetry", "tally", "term", "tessellation", "translation", "transversal",
    "unit rate", "variable", "vertex", "volume", "whole number",
]


def build_answers(bk, chapters):
    bk.new_page("body")
    p = Pager(bk)
    p.add(PageTitle("Answers and worked solutions", "Reference"))
    p.add(Lead("These are answers, with the method where the method is the point. "
               "A numerical answer on its own tells you only whether you finished; "
               "the reason tells you whether you understood."))
    p.add(Spacer(6))
    p.add(Panel("note", title="How to use this section",
                text="Each chapter's answers begin on a new page, and every answer "
                     "stands on its own line under its practice heading, so an "
                     "answer can be found without reading past the one before it. "
                     "Compare the first line that differs, not the last. If your "
                     "answer is right but the route was different, that is worth "
                     "noting: two correct methods are evidence of understanding, "
                     "not a problem. If the answer is wrong, find the first wrong "
                     "line before reading on."))
    for n, (mod_name, title) in enumerate(chapters):
        mod = importlib.import_module(mod_name)
        if n and p.frame.remaining < 120:
            p.break_page()
        p.add(H3(f"{title}"))
        for ref, answers in mod.ANSWERS.items():
            if ref.startswith("R"):
                p.add(AnswerLabel(f"Part review {ROMAN.get(ref, ref)}"))
            else:
                p.add(AnswerLabel(f"Practice {ref}"))
            for i, a in enumerate(answers, start=1):
                p.add(AnswerEntry(i, a))
        p.add(Spacer(10))


def build_formula_bank(bk):
    bk.new_page("body")
    p = Pager(bk)
    p.add(PageTitle("Formula bank", "Reference \u00b7 formulas"))
    p.add(Lead("Every formula in this course, grouped by the kind of question it "
               "answers. Symbols are defined where they first appear in a chapter."))
    p.add(Spacer(4))
    for group, rows in FORMULAS:
        p.add(H3(group))
        p.add(DataTable(["Rule", "Form", "Note"],
                        [[name, form, note or ""] for name, form, note in rows],
                        widths=[1.25, 1.6, 0.85], font_size=8.2))
        p.add(Spacer(4))
    return bk


def build_glossary(bk):
    bk.new_page("body")
    p = Pager(bk)
    p.add(PageTitle("Glossary", "Reference \u00b7 vocabulary"))
    p.add(Lead("Definitions as they are used in this book. Where a word has a "
               "different meaning in everyday language, the mathematical meaning is "
               "the one that applies here."))
    p.add(Spacer(4))
    rows = [[f"**{t}**", d] for t, d in GLOSSARY]
    p.add(DataTable(["Term", "Meaning"], rows, widths=[0.85, 2.6], font_size=8.0,
                    caption="The vocabulary of the course, alphabetically."))
    return bk


def build_index(bk, index_map):
    bk.new_page("body")
    p = Pager(bk)
    p.add(PageTitle("Index", "Reference \u00b7 index"))
    p.add(Lead("Page numbers refer to the printed folios. Index entries are keyed to "
               "the page where an idea is introduced or most fully used."))
    p.add(Spacer(6))
    rows = []
    for term in INDEX_TERMS:
        pages = index_map.get(term.lower(), [])
        rows.append([f"**{term}**", ", ".join(str(x) for x in pages[:6])])
    p.add(DataTable(["Entry", "Pages"], rows, widths=[1.0, 2.4], font_size=8.0))
    return bk


def build_references(bk):
    bk.new_page("plain")
    c = bk.c
    T(c, L, spec.PAGE_H - 120, "REFERENCE \u00b7 SOURCES AND ACKNOWLEDGEMENTS",
      "Inter-Semi", 6.4, spec.TERRACOTTA, 2.2)
    T(c, L, spec.PAGE_H - 152, "References and acknowledgements", "Playfair", 24,
      spec.INK)
    _line(c, L, spec.PAGE_H - 168, R, spec.PAGE_H - 168, 0.8, 1.0, colour=spec.GOLD)

    from reportlab.platypus import Paragraph
    from bookkit.markup import inline, style
    blocks = [
        ("Framework", "International Baccalaureate Organization. MYP: From principles "
                      "into practice (current edition). References to key concepts, "
                      "related concepts, global contexts, statements of inquiry, "
                      "approaches to learning and the four assessment criteria follow "
                      "the framework as published by the IB. This book is an "
                      "independent publication and is not endorsed by the IB."),
        ("Pedagogical inspiration", "The inquiry-led sequence of engage, explore, "
                                    "explain, apply and reflect, and the practice of "
                                    "naming criteria and strands within a chapter, are "
                                    "informed by the Oxford MYP Mathematics series and "
                                    "by the wider IB mathematics community. No text, "
                                    "example, exercise or design from that series has "
                                    "been reproduced here."),
        ("Mathematical content", "Definitions, results and conventions are standard "
                                 "school mathematics for Year 2, expressed in the "
                                 "author's own words. Where a convention varies (for "
                                 "example the treatment of quartiles), the method used "
                                 "is stated in the chapter and applied consistently."),
        ("Typefaces", "Source Serif 4 by Frank Grie\u00dfhammer; Playfair Display by "
                      "Claus Eggers S\u00f8rensen; Inter by Rasmus Andersson; DejaVu "
                      "Sans (subset) by the DejaVu project. All are used under the SIL "
                      "Open Font License 1.1."),
        ("Illustrations", "All diagrams are original vector drawings created for this "
                          "edition and are drawn directly into the page, so they "
                          "remain sharp at any size. Photographs are listed with "
                          "their sources and licensing in the image register "
                          "supplied with the edition."),
        ("Statement", "This is an improved first edition of MYP Mathematics 2. The "
                      "curriculum scope, topic sequence, learning objectives and level "
                      "of difficulty are those of the first edition. No ISBN, "
                      "publisher, barcode or official endorsement is claimed."),
    ]
    y = spec.PAGE_H - 200
    for head, text in blocks:
        T(c, L, y, head.upper(), "Inter-Semi", 6.4, spec.GOLD_DEEP, 2.0)
        y -= 16
        par = Paragraph(inline(text), style("rf", fontSize=8.8, leading=13.2,
                                            textColor=spec.INK_SOFT, alignment=0))
        h = par.wrap(R - L, 1e6)[1]
        par.drawOn(c, L, y - h)
        y -= h + 18
    _line(c, L, 110, R, 110, 0.6, 1.0, colour=spec.RULE)
    T(c, L, 92, "SADIKOU MOUKODDIM  \u00b7  MYP MATHEMATICS 2  \u00b7  IMPROVED FIRST "
                "EDITION", "Inter-Semi", 6.2, spec.INK_MUTE, 1.7)
    return bk
