"""Back matter: answers, formula bank, glossary, index, acknowledgements."""
import importlib

from bookkit import spec, typeset
from bookkit.blocks import Panel, DataTable, H3, Body, ListBlock, Lead, SectionHead
from bookkit.flow import Pager, Spacer
from bookkit.markup import inline, style
from bookkit.plates import _motif

T = typeset.draw

CHAPTER_MODULES = ["ch01", "ch02", "ch03", "ch04", "ch05", "ch06", "ch07", "ch08",
                   "ch09", "ch10"]

GLOSSARY = [
    ("Acute angle", "An angle smaller than 90\u00b0."),
    ("Algebraic expression", "A combination of numbers, letters and operations with no "
                             "equals sign."),
    ("Alternate angles", "Equal angles on opposite sides of a transversal crossing two "
                         "parallel lines."),
    ("Angle", "The amount of turn between two lines that meet at a point."),
    ("Approximation", "A value used in place of an exact value, close enough for the "
                      "purpose."),
    ("Area", "The amount of surface enclosed by a boundary, measured in square units."),
    ("Average", "A single value used to summarise a set; mean, median and mode are the "
                "averages used in this course."),
    ("Bar chart", "A display in which the height of each bar represents the frequency of a "
                  "category."),
    ("Base", "In a power, the number being multiplied repeatedly; in a place-value system, "
             "the number of digits used."),
    ("Capacity", "The volume a container can hold, often measured in litres."),
    ("Composite shape", "A shape made by joining simpler shapes."),
    ("Congruent", "Exactly the same shape and size."),
    ("Constant", "A quantity whose value does not change in a given expression."),
    ("Coordinate", "A pair of numbers locating a point relative to two axes."),
    ("Cross-section", "The face revealed by cutting a solid with a plane."),
    ("Cube", "A solid with six congruent square faces; also a number multiplied by itself "
             "twice."),
    ("Cumulative frequency", "A running total of frequencies."),
    ("Decimal", "A number written using place value to the right of a decimal point."),
    ("Denominator", "The number below the line in a fraction: the number of equal parts in "
                    "the whole."),
    ("Diameter", "A straight line through the centre of a circle, joining two points on the "
                 "circumference."),
    ("Difference", "The result of subtracting one number from another."),
    ("Digit", "One of the ten symbols 0\u20139 used to write numbers in base ten."),
    ("Divisible", "A whole number a is divisible by b if a \u00f7 b has no remainder."),
    ("Equation", "A statement that two expressions are equal."),
    ("Equivalent", "Having the same value, however written."),
    ("Estimate", "A deliberately simplified calculation used to judge size."),
    ("Expanded form", "A number written as the sum of its place values."),
    ("Exponent", "The number that shows how many copies of the base are multiplied."),
    ("Expression", "A mathematical phrase that can be evaluated but is not a statement of "
                   "equality."),
    ("Factor", "A whole number that divides another exactly."),
    ("Formula", "A rule written as an equation relating quantities."),
    ("Fraction", "A number written as one integer divided by another."),
    ("Frequency", "The number of times a value occurs."),
    ("Generalise", "To state a rule that covers every case, not just the ones examined."),
    ("Highest common factor", "The largest number that divides two or more numbers "
                              "exactly."),
    ("Histogram", "A display of continuous data in which bars touch, because the classes "
                  "are continuous."),
    ("Improper fraction", "A fraction whose numerator is greater than or equal to its "
                          "denominator."),
    ("Index", "Another name for exponent."),
    ("Integer", "A whole number or the negative of a whole number."),
    ("Intersection", "The set of elements belonging to both of two sets."),
    ("Investigation", "A structured exploration of cases leading to a conjecture and a "
                      "general rule."),
    ("Lowest common multiple", "The smallest number that is a multiple of two or more "
                               "given numbers."),
    ("Mean", "The sum of the values divided by the number of values."),
    ("Median", "The middle value when the data are in order."),
    ("Mode", "The value that occurs most often."),
    ("Multiple", "The result of multiplying a number by a whole number."),
    ("Natural number", "A counting number: 1, 2, 3, \u2026"),
    ("Net", "A flat arrangement of faces that folds to make a solid."),
    ("Numerator", "The number above the line in a fraction: how many equal parts are "
                  "taken."),
    ("Order of operations", "The agreed sequence for evaluating expressions: brackets, "
                            "indices, multiplication and division, addition and "
                            "subtraction."),
    ("Parallel", "Lines in the same plane that never meet."),
    ("Percentage", "A fraction or ratio expressed as a number of hundredths."),
    ("Perimeter", "The distance around a closed shape."),
    ("Perpendicular", "Meeting at a right angle."),
    ("Pi (\u03c0)", "The ratio of a circle's circumference to its diameter, approximately "
                    "3.142."),
    ("Place value", "The value a digit carries because of its position."),
    ("Power", "A product of equal factors, written with a base and an exponent."),
    ("Prime number", "A whole number greater than 1 with exactly two factors: 1 and "
                     "itself."),
    ("Prime factorisation", "A number written as a product of prime factors."),
    ("Prism", "A solid with a constant cross-section and flat faces."),
    ("Proportion", "A statement that two ratios are equal."),
    ("Radius", "The distance from the centre of a circle to its circumference."),
    ("Range", "The difference between the largest and smallest values in a set."),
    ("Ratio", "A comparison of two quantities by division."),
    ("Reciprocal", "The number you multiply by to get 1; the reciprocal of a/b is b/a."),
    ("Recurring decimal", "A decimal with a repeating pattern of digits."),
    ("Rounding", "Replacing a number with a nearby value at a stated precision."),
    ("Set", "A collection of objects, called elements."),
    ("Simplify", "To write in an equivalent but shorter form."),
    ("Solution", "A value that makes an equation true."),
    ("Square number", "The product of a number with itself."),
    ("Square root", "A number which, multiplied by itself, gives the given number."),
    ("Standard form", "A number written with a single digit before the decimal point and "
                      "a power of ten."),
    ("Statement of inquiry", "A sentence expressing the conceptual understanding a unit "
                             "develops."),
    ("Subset", "A set every element of which belongs to another set."),
    ("Substitution", "Replacing a letter in an expression with a number and evaluating."),
    ("Surface area", "The total area of all the faces of a solid."),
    ("Term", "A single number, letter or product in an expression."),
    ("Transversal", "A line that crosses two or more other lines."),
    ("Union", "The set of elements belonging to either or both of two sets."),
    ("Variable", "A letter standing for a number that can change or is not yet known."),
    ("Venn diagram", "A diagram using overlapping regions to represent sets."),
    ("Volume", "The amount of space a solid occupies."),
    ("Whole number", "A natural number or zero."),
]

FORMULAE = [
    ("Number and proportion", [
        ("A value in expanded form", "digit \u00d7 place value, summed over all columns"),
        ("Percentage of a quantity", "percentage \u00f7 100 \u00d7 quantity"),
        ("Percentage change", "(change \u00f7 original) \u00d7 100 %"),
        ("Adding fractions", "a/b + c/d = (ad + bc) \u00f7 bd"),
        ("Multiplying fractions", "a/b \u00d7 c/d = ac \u00f7 bd"),
        ("Dividing fractions", "a/b \u00f7 c/d = a/b \u00d7 d/c"),
        ("Simplifying a ratio", "divide every part by the same common factor"),
        ("Unitary method", "find the value of one unit, then multiply"),
        ("Order of operations", "brackets, indices, multiplication and division, then "
                                "addition and subtraction"),
        ("Dividing by a decimal", "multiply both numbers by the same power of ten first"),
    ]),
    ("Algebra", [
        ("nth term of a linear sequence", "term = first term + (n \u2212 1) \u00d7 "
                                          "common difference"),
        ("Expanding", "a(b + c) = ab + ac"),
        ("Solving two-step equations", "undo addition or subtraction first, then "
                                       "multiplication or division"),
        ("Collecting like terms", "add or subtract the coefficients of matching terms"),
        ("Substituting", "replace each letter with its value, then evaluate"),
        ("Linear sequence", "constant difference between consecutive terms"),
    ]),
    ("Shape and space", [
        ("Angles on a straight line", "sum to 180\u00b0"),
        ("Angles at a point", "sum to 360\u00b0"),
        ("Angle sum of a triangle", "180\u00b0"),
        ("Angle sum of an n-sided polygon", "(n \u2212 2) \u00d7 180\u00b0"),
        ("Area of a rectangle", "A = length \u00d7 width"),
        ("Area of a triangle", "A = \u00bd \u00d7 base \u00d7 perpendicular height"),
        ("Area of a parallelogram", "A = base \u00d7 perpendicular height"),
        ("Area of a trapezium", "A = \u00bd \u00d7 (a + b) \u00d7 h"),
        ("Circumference of a circle", "C = \u03c0d = 2\u03c0r"),
        ("Area of a circle", "A = \u03c0r^{2}"),
        ("Volume of a prism", "V = area of cross-section \u00d7 length"),
        ("Volume of a cuboid", "V = length \u00d7 width \u00d7 height"),
        ("Surface area of a cuboid", "S = 2(lw + lh + wh)"),
        ("Capacity", "1 litre = 1 000 cm^{3}"),
        ("Angles in parallel lines", "corresponding and alternate angles are equal"),
        ("Perimeter", "the sum of all side lengths"),
        ("Units of area", "1 m^{2} = 10 000 cm^{2}"),
    ]),
    ("Data", [
        ("Mean", "sum of values \u00f7 number of values"),
        ("Range", "largest value \u2212 smallest value"),
        ("Median", "middle value of an ordered set"),
        ("Mode", "the value that occurs most often"),
        ("Frequency", "the number of times a value occurs"),
        ("Angle of a pie-chart sector", "frequency \u00f7 total \u00d7 360\u00b0"),
        ("Comparing averages", "use the mean with the range, and the median when "
                                "outliers are present"),
    ]),
]

INDEX_TERMS = [
    ("Acute angle", [(7, "7.1")]),
    ("Angle facts", [(7, "7.1")]),
    ("Area", [(9, "9.2")]),
    ("Average", [(10, "10.2")]),
    ("Bar chart", [(10, "10.3")]),
    ("Base", [(2, "2.1")]),
    ("Capacity", [(9, "9.4")]),
    ("Circle", [(9, "9.1"), (9, "9.3")]),
    ("Circumference", [(9, "9.1")]),
    ("Complement (sets)", [(8, "8.2")]),
    ("Composite shape", [(9, "9.2")]),
    ("Congruence", [(7, "7.4")]),
    ("Continuous data", [(10, "10.1")]),
    ("Cuboid", [(9, "9.4")]),
    ("Decimal", [(4, "4.5"), (4, "4.6")]),
    ("Denominator", [(4, "4.1")]),
    ("Diameter", [(9, "9.1")]),
    ("Discrete data", [(10, "10.1")]),
    ("Divisibility", [(3, "3.2")]),
    ("Dot plot", [(10, "10.3")]),
    ("Equation", [(6, "6.4")]),
    ("Equivalent fractions", [(4, "4.1")]),
    ("Estimation", [(1, "1.5")]),
    ("Expanded form", [(1, "1.3")]),
    ("Exponent", [(2, "2.1")]),
    ("Factor", [(3, "3.1")]),
    ("Factorisation", [(3, "3.4")]),
    ("Formula", [(6, "6.4")]),
    ("Frequency", [(10, "10.1")]),
    ("Frequency table", [(10, "10.1")]),
    ("Generalisation", [(6, "6.1")]),
    ("Highest common factor", [(3, "3.5")]),
    ("Index notation", [(2, "2.1")]),
    ("Integer", [(1, "1.1")]),
    ("Intersection", [(8, "8.3")]),
        ("Linear sequence", [(6, "6.1")]),
    ("Lowest common multiple", [(3, "3.5")]),
    ("Mean", [(10, "10.2")]),
    ("Median", [(10, "10.2")]),
    ("Misleading graph", [(10, "10.4")]),
    ("Mode", [(10, "10.2")]),
    ("Multiple", [(3, "3.1")]),
    ("Net", [(9, "9.4")]),
    ("Number line", [(1, "1.1")]),
    ("Order of operations", [(2, "2.4")]),
    ("Outlier", [(10, "10.2"), (10, "Investigation 10")]),
    ("Parallel lines", [(7, "7.1")]),
    ("Percentage", [(5, "5.1")]),
    ("Percentage change", [(5, "5.3")]),
    ("Perimeter", [(9, "9.1")]),
    ("Pi", [(9, "9.1")]),
    ("Pie chart", [(10, "10.3")]),
    ("Place value", [(1, "1.2")]),
    ("Polygon", [(7, "7.3")]),
    ("Power", [(2, "2.1")]),
    ("Prime factorisation", [(3, "3.4")]),
    ("Prime number", [(3, "3.3")]),
    ("Prism", [(9, "9.4")]),
    ("Reciprocal", [(4, "4.4")]),
    ("Recurring decimal", [(4, "4.6")]),
    ("Rounding", [(1, "1.4")]),
    ("Set notation", [(8, "8.1")]),
    ("Simplification", [(6, "6.3")]),
    ("Square root", [(2, "2.3")]),
    ("Subset", [(8, "8.2")]),
    ("Substitution", [(6, "6.2")]),
    ("Surface area", [(9, "9.4")]),
    ("Symbols", [(1, "1.1")]),
    ("Term of a sequence", [(6, "6.1")]),
    ("Transversal", [(7, "7.1")]),
    ("Triangle inequality", [(7, "Investigation 7")]),
    ("Union", [(8, "8.3")]),
    ("Universal set", [(8, "8.2")]),
    ("Variable", [(6, "6.2"), (10, "10.1")]),
    ("Venn diagram", [(8, "8.3")]),
    ("Volume", [(9, "9.4")]),
    ("Algebraic expression", [(6, "6.2")]),
    ("Brackets", [(2, "2.4")]),
    ("Composite number", [(3, "3.3")]),
    ("Corresponding angles", [(7, "7.2")]),
    ("Cube number", [(2, "2.3")]),
    ("Cube root", [(2, "2.3")]),
    ("Decimal place", [(4, "4.5")]),
    ("Discount", [(5, "5.4")]),
    ("Element (of a set)", [(8, "8.1")]),
    ("Equilateral triangle", [(7, "7.3")]),
    ("Even number", [(3, "3.2")]),
    ("Expanding brackets", [(6, "6.3")]),
    ("Forming an equation", [(6, "6.4")]),
    ("Hexagon", [(7, "7.3")]),
    ("Improper fraction", [(4, "4.1")]),
    ("Index laws", [(2, "2.2")]),
    ("Inequality", [(1, "1.1")]),
    ("Inverse operation", [(6, "6.4")]),
    ("Isosceles triangle", [(7, "7.3")]),
    ("Mixed number", [(4, "4.1")]),
    ("Negative number", [(1, "1.1")]),
    ("Numerator", [(4, "4.1")]),
    ("Obtuse angle", [(7, "7.1")]),
    ("Odd number", [(3, "3.2")]),
    ("Power of ten", [(2, "2.2")]),
    ("Profit", [(5, "5.4")]),
    ("Proportion", [(5, "5.1")]),
    ("Radius", [(9, "9.1")]),
    ("Right angle", [(7, "7.1")]),
    ("Sector", [(10, "10.3")]),
    ("Square number", [(2, "2.3")]),
    ("Standard form", [(1, "1.3")]),
    ("Tally", [(10, "10.1")]),
    ("Tax", [(5, "5.4")]),
    ("Three-dimensional shape", [(9, "9.4")]),
    ("Vertically opposite angles", [(7, "7.1")]),
    ("Whole number", [(1, "1.1")]),
    ("Zero", [(1, "1.2")]),
]


def build_back(bk, reg):
    # section/page lookup for the index
    sec_pages = {}
    for kind, ch, title, label in reg.entries:
        if kind == "section":
            ref = title.split("  ")[0]
            sec_pages[(ch, ref)] = label

    import front
    # ---------------------------------------------------------- answers
    bk.new_page("plain")
    p = Pager(bk)
    p.add(front.Heading("Reference", "Answers and brief solutions"))
    p.add(Lead("An answer ends a calculation; a solution records a decision. Where a "
               "question asks for reasoning, the entry below names the idea that earns the "
               "mark rather than reproducing a full response."))
    for i, mod_name in enumerate(CHAPTER_MODULES, start=1):
        mod = importlib.import_module(mod_name)
        answers = getattr(mod, "ANSWERS", [])
        if not answers:
            continue
        head = H3(f"Chapter {i} \u00b7 {mod.SHORT}", space_before=11)
        head.keep_room = 190          # never strand a chapter heading above its table
        p.add(head)
        p.add(DataTable(["Ref", "Answer"], [[r, a] for r, a in answers],
                        widths=[0.42, 2.9], font_size=8.0, first_col_bold=True))

    # ------------------------------------------------------- formula bank
    bk.new_page("plain")
    p = Pager(bk)
    p.add(front.Heading("Reference", "Formula bank"))
    p.add(Lead("Every formula used in the course, grouped by part. A formula is not a fact "
               "to memorise: each one can be rebuilt from a diagram or a definition."))
    for group, rows in FORMULAE:
        head = H3(group, space_before=10)
        head.keep_room = 120
        p.add(head)
        p.add(DataTable(["Rule", "Statement"], [[a, b] for a, b in rows],
                        widths=[0.85, 2.0], font_size=8.3))

    # ----------------------------------------------------------- glossary
    bk.new_page("plain")
    p = Pager(bk)
    p.add(front.Heading("Reference", "Glossary"))
    p.add(Lead("Definitions in the form the course uses them. Where a word has a different "
               "meaning outside mathematics, the mathematical meaning is the one given."))
    letters = {}
    for term, meaning in GLOSSARY:
        letters.setdefault(term[0].upper(), []).append((term, meaning))
    for letter in sorted(letters):
        p.add(DataTable([letter, ""], [[t, m] for t, m in letters[letter]],
                        widths=[0.42, 2.9], font_size=8.2, first_col_bold=False))

    # -------------------------------------------------------------- index
    bk.new_page("plain")
    p = Pager(bk)
    p.add(front.Heading("Reference", "Index"))
    p.add(Lead("Page numbers refer to the printed page numbers at the foot of each page."))
    rows = []
    for term, refs in INDEX_TERMS:
        labels = []
        for ch, sec in refs:
            lab = sec_pages.get((ch, sec))
            if lab:
                labels.append(lab)
        rows.append([term, ", ".join(labels) if labels else "\u2014"])
    rows.sort(key=lambda r: r[0].lower())
    # two terms per row across the wide page, so the index holds on one page
    half = (len(rows) + 1) // 2
    left, right = rows[:half], rows[half:]
    right += [["", ""]] * (len(left) - len(right))
    paired = [l + r for l, r in zip(left, right)]
    dt = DataTable(["Term", "Page", "Term", "Page"], paired,
                   widths=[1.35, 0.40, 1.35, 0.40], font_size=8.0,
                   first_col_bold=False)
    dt.splittable = True
    p.add(dt)

    # ------------------------------------------------- acknowledgements
    bk.new_page("plain")
    p = Pager(bk)
    p.add(front.Heading("Reference", "References and acknowledgements"))
    p.add(Lead("Sources consulted for framework alignment, and the provenance of every "
               "asset in this edition."))
    p.add(H3("Curriculum framework"))
    p.add(ListBlock([
        "International Baccalaureate Organization. *MYP: From principles into practice.* "
        "Consulted for the structure of key and related concepts, global contexts, "
        "statements of inquiry and approaches to learning. This book is not published or "
        "endorsed by the IB.",
        "International Baccalaureate Organization. *Mathematics guide: Middle Years "
        "Programme.* Consulted for the four assessment criteria and their strands and for "
        "the Year 1 scope of number, algebra, geometry and statistics.",
        "Oxford University Press, *MYP Mathematics* series. Consulted as pedagogical "
        "inspiration only: the sequence of inquiry, the balance of representation and the "
        "emphasis on conceptual framing. No text, exercise, diagram or layout has been "
        "copied.",
    ]))
    p.add(H3("Mathematical content"))
    p.add(Body("All mathematical statements in this book are standard results of school "
               "mathematics and are stated in the author's own words. Worked examples, "
               "exercises, investigations and answers were written for this edition and "
               "checked in a full editorial and mathematical review; the check sheet is "
               "published with the manuscript."))
    p.add(H3("Typefaces"))
    p.add(ListBlock([
        "Playfair Display, by Claus Eggers S\u00f8rensen \u2014 SIL Open Font License 1.1.",
        "Source Serif 4, by Frank Grie\u00dfhammer \u2014 SIL Open Font License 1.1.",
        "Inter, by Rasmus Andersson \u2014 SIL Open Font License 1.1.",
        "Symbols not carried by these families are set in a DejaVu Sans subset "
        "(Bitstream Vera licence, free to redistribute).",
    ]))
    p.add(H3("Illustration and diagrams"))
    p.add(Body("Every diagram in this book is original vector artwork drawn for this "
               "edition: number lines, place-value tables, fraction strips, angle and "
               "parallel-line figures, nets, prisms, circle diagrams, Venn diagrams and "
               "statistical displays. The contextual illustrations are original artwork "
               "created for this edition and carry no third-party rights. No stock "
               "photograph, publisher image or web image is reproduced. The image register "
               "that accompanies the manuscript records each asset, its purpose and its "
               "licence position."))
    p.add(Panel("note", title="A note on the illustrations",
                text="The illustrations in this edition are drawn rather than photographed. "
                     "They were made to a single palette so that they sit inside the page "
                     "design instead of interrupting it, and every one of them depicts a "
                     "situation in which the chapter's mathematics is actually used.",
                space_before=8))
