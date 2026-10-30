"""Full-bleed plates: front cover, part dividers, chapter openers, back cover.

These pages carry the book's identity, so their composition follows the original
first edition closely: deep green field, letterspaced cream sans labels, gold
hairlines, a high-contrast display serif, one oversized numeral, and a thin
line-art motif in the outer corner.

Improvements are refinements only: kerning and true letterspacing in the
display type, one optical margin for all plates, a quieter motif, and a
strict vertical rhythm shared by every opener.
"""
from . import spec, typeset
from .markup import plain

T = typeset.draw


def _motif(c, x, y, w, h, colour, alpha=0.30, grid=24, arcs=True):
    c.saveState()
    c.setStrokeColor(colour)
    c.setFillColor(colour)
    try:
        c.setStrokeAlpha(alpha)
        c.setFillAlpha(alpha)
    except Exception:
        pass
    c.setLineWidth(0.30)
    gx = x
    while gx <= x + w:
        c.line(gx, y, gx, y + h)
        gx += grid
    gy = y
    while gy <= y + h:
        c.line(x, gy, x + w, gy)
        gy += grid
    if arcs:
        cx, cy = x + w * 0.02, y - h * 0.10
        for r, lw_ in ((h * 0.92, 0.7), (h * 1.16, 0.45), (h * 1.40, 0.45)):
            c.setLineWidth(lw_)
            c.arc(cx - r, cy - r, cx + r, cy + r, startAng=6, extent=78)
        c.setLineWidth(0.9)
        c.setDash(1.0, 5.0)
        c.arc(cx - h * 1.04, cy - h * 1.04, cx + h * 1.04, cy + h * 1.04,
              startAng=10, extent=70)
        c.setDash()
        c.circle(x + w * 0.30, y + h * 0.30, 1.9, stroke=0, fill=1)
    c.restoreState()


def _motif_axes(c, x, y, w, h, colour, alpha=0.26):
    c.saveState()
    c.setStrokeColor(colour)
    try:
        c.setStrokeAlpha(alpha)
    except Exception:
        pass
    c.setLineWidth(0.7)
    c.line(x, y + h * 0.18, x + w, y + h * 0.18)
    c.line(x + w * 0.12, y, x + w * 0.12, y + h)
    c.setLineWidth(0.45)
    pts = [(0.20, 0.30), (0.30, 0.46), (0.40, 0.52), (0.52, 0.68), (0.66, 0.74),
           (0.80, 0.88)]
    for i in range(len(pts) - 1):
        c.line(x + w * pts[i][0], y + h * pts[i][1], x + w * pts[i + 1][0],
               y + h * pts[i + 1][1])
    c.restoreState()


# ---------------------------------------------------------------------- covers
def cover(c, meta=None):
    c.saveState()
    c.setFillColor(spec.GREEN)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()

    L, R = 62, spec.PAGE_W - 62
    # hairline frame, top and bottom
    c.saveState()
    c.setStrokeColor(spec.GOLD_DEEP)
    c.setLineWidth(0.55)
    c.line(L, spec.PAGE_H - 44, R, spec.PAGE_H - 44)
    c.line(L, 40, R, 40)
    c.restoreState()

    _motif(c, R - 246, 44, 246, 246, spec.GOLD, 0.30, 24)

    # top labels
    T(c, L, spec.PAGE_H - 66, "MIDDLE YEARS PROGRAMME", "Inter-Semi", 6.9, spec.CREAM, 2.3)
    T(c, L, spec.PAGE_H - 78, "YEAR 1  \u00b7  MATHEMATICS", "Inter-Semi", 6.9,
      spec.CREAM, 2.3)
    T(c, R, spec.PAGE_H - 66, "IMPROVED FIRST EDITION", "Inter-Semi", 6.4, spec.GOLD,
      2.3, "right")
    T(c, R, spec.PAGE_H - 78, "2026", "Inter-Semi", 6.4, spec.GOLD, 2.3, "right")

    # eyebrow
    T(c, L, 566, "MYP", "Inter-Semi", 8.4, spec.GOLD, 3.2)

    # title, optically fitted to the measure
    title = "MATHEMATICS"
    size = typeset.fit(title, "Playfair-Display", 64, R - L)
    T(c, L - 2, 508, title, "Playfair-Display", size, spec.CREAM, 0.6)

    # oversized year numeral
    c.saveState()
    c.setFont("Playfair-Display", 128)
    c.setFillColor(spec.GOLD)
    c.drawString(L - 3, 394, "1")
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(1.3)
    c.line(L, 384, L + 76, 384)
    c.restoreState()

    T(c, L + 98, 452, "Student", "SourceSerif", 21.5, spec.CREAM)
    T(c, L + 98, 427, "Coursebook", "SourceSerif", 21.5, spec.CREAM)
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(0.8)
    c.line(L + 98, 410, L + 98 + 62, 410)
    c.restoreState()
    T(c, L + 98, 393, "A concept-driven inquiry course in number,", "SourceSerifItalic",
      9.8, spec.CREAM)
    T(c, L + 98, 381, "proportion, algebra, shape and data.", "SourceSerifItalic", 9.8,
      spec.CREAM)

    # contents band
    c.saveState()
    c.setStrokeColor(spec.GOLD_DEEP)
    c.setLineWidth(0.55)
    c.line(L, 252, R, 252)
    c.restoreState()
    lines = [
        "Number systems \u00b7 Place value and powers \u00b7 Factors and primes",
        "Fractions and decimals \u00b7 Percentages \u00b7 Patterns and equations",
        "Lines, angles and constructions \u00b7 Sets \u00b7 Perimeter, area and volume \u00b7 Data and graphs",
    ]
    y = 236
    for ln in lines:
        T(c, L, y, ln, "SourceSerif", 8.7, spec.GOLD_PALE)
        y -= 13.6

    # author block
    c.saveState()
    c.setStrokeColor(spec.GOLD_DEEP)
    c.setLineWidth(0.55)
    c.line(L, 104, R, 104)
    c.restoreState()
    T(c, L, 84, "SADIKOU MOUKODDIM", "SourceSerif-Semi", 13.6, spec.CREAM, 0.5)
    T(c, L, 68, "AUTHOR", "Inter-Semi", 6.2, spec.GOLD, 2.4)


def back_cover(c, meta=None):
    c.saveState()
    c.setFillColor(spec.GREEN)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    L, R = 62, spec.PAGE_W - 62
    _motif(c, R - 230, 470, 230, 230, spec.GOLD, 0.14, 22)

    T(c, L, spec.PAGE_H - 150, "Mathematics is a way of seeing,", "Playfair-Display",
      26, spec.CREAM)
    T(c, L, spec.PAGE_H - 182, "not a list of rules.", "Playfair-Display", 26,
      spec.CREAM)

    body = [
        "Ten chapters build Year 1 mathematics from the ground up: how our",
        "number system encodes quantity; why fractions, decimals and",
        "percentages describe the same wholes in different ways; how algebra",
        "compresses a pattern into a rule; how shape and measurement answer",
        "practical questions; and how data becomes evidence \u2014 or misleading",
        "noise \u2014 depending on how it is displayed.",
    ]
    y = spec.PAGE_H - 236
    for ln in body:
        T(c, L, y, ln, "SourceSerif", 10.0, spec.GOLD_PALE)
        y -= 15.4

    y -= 12
    body2 = [
        "Every chapter moves through one rhythm: engage, explore, explain,",
        "work through examples, practise, investigate, and reflect. Each",
        "section names the MYP criterion it develops, and each chapter closes",
        "with a review, mixed practice and a criterion-mapped mini-task.",
    ]
    for ln in body2:
        T(c, L, y, ln, "SourceSerif", 10.0, spec.GOLD_PALE)
        y -= 15.4

    c.saveState()
    c.setStrokeColor(spec.GOLD_DEEP)
    c.setLineWidth(0.55)
    c.line(L, 214, R, 214)
    c.restoreState()
    T(c, L, 192, "SADIKOU MOUKODDIM", "SourceSerifItalic", 11.0, spec.CREAM)
    T(c, L, 178, "AUTHOR  \u00b7  HEAD OF MATHEMATICS DEPARTMENT", "Inter-Semi", 6.2,
      spec.GOLD, 2.1)
    T(c, L, 118, "An independent educational publication. Not published by, sponsored by,",
      "Inter", 6.4, spec.GOLD_PALE)
    T(c, L, 108, "endorsed by or affiliated with the International Baccalaureate Organization.",
      "Inter", 6.4, spec.GOLD_PALE)
    T(c, L, 78, "MYP MATHEMATICS 1  \u00b7  IMPROVED FIRST EDITION", "Inter-Semi", 6.6,
      spec.GOLD, 2.0)


# ------------------------------------------------------------------ part plate
def part_plate(c, numeral, title, subtitle, chapters, motif=None):
    c.saveState()
    c.setFillColor(spec.GREEN)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    (motif or _motif)(c, spec.PAGE_W - 330, 400, 330, 330, spec.GOLD, 0.26)
    L = 62
    T(c, L, spec.PAGE_H - 96, "PART", "Inter-Semi", 7.4, spec.GOLD, 3.2)
    c.saveState()
    c.setFont("Playfair-Display", 144)
    c.setFillColor(spec.GOLD)
    c.drawString(L - 5, 436, numeral)
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(1.4)
    c.line(L, 416, L + 186, 416)
    c.restoreState()

    y = 350
    for ln in title:
        T(c, L, y, ln, "Playfair-Med", spec.SZ_PART_TITLE, spec.CREAM)
        y -= 45
    y -= 6
    for ln in subtitle:
        T(c, L, y, ln, "SourceSerifItalic", 11.4, spec.GOLD_PALE)
        y -= 16.5
    y -= 20
    c.saveState()
    c.setStrokeColor(spec.GOLD_DEEP)
    c.setLineWidth(0.55)
    c.line(L, y, spec.PAGE_W - 62, y)
    c.restoreState()
    y -= 22
    for num, name in chapters:
        T(c, L, y, num, "Inter-Semi", 7.2, spec.GOLD, 2.0)
        T(c, L + 36, y, name, "SourceSerif", 10.4, spec.CREAM)
        y -= 21
    T(c, L, 56, "SADIKOU MOUKODDIM", "Inter-Semi", 6.2, spec.GOLD, 2.2)
    T(c, spec.PAGE_W - 62, 56, "MYP MATHEMATICS 1", "Inter-Semi", 6.2, spec.GOLD, 2.2,
      "right")


# --------------------------------------------------------------- chapter plate
def chapter_plate(c, meta, motif=None):
    """Full-bleed chapter opener."""
    c.saveState()
    c.setFillColor(spec.GREEN)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    (motif or _motif)(c, spec.PAGE_W - 250, 520, 220, 220, spec.GOLD, 0.30, 22)
    L = 62
    T(c, L, spec.PAGE_H - 84, plain(meta["part"]).upper(), "Inter-Semi", 6.5,
      spec.GOLD_PALE, 2.2)
    T(c, L, spec.PAGE_H - 96, "MYP YEAR 1", "Inter-Semi", 6.5, spec.GOLD_PALE, 2.2)
    T(c, spec.PAGE_W - 62, spec.PAGE_H - 84, "CHAPTER " + str(meta["chapter_no"]).zfill(2),
      "Inter-Semi", 6.5, spec.GOLD_PALE, 2.2, "right")
    T(c, spec.PAGE_W - 62, spec.PAGE_H - 96, "PART " + meta["part_numeral"],
      "Inter-Semi", 6.5, spec.GOLD_PALE, 2.2, "right")

    c.saveState()
    c.setFont("Playfair-Display", 100)
    c.setFillColor(spec.GOLD)
    c.drawString(L - 3, 640, str(meta["chapter_no"]))
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(1.0)
    c.line(L, 630, L + 64, 630)
    c.restoreState()

    T(c, L, 600, plain(meta["kicker"]).upper(), "Inter-Semi", 7.0, spec.TERRACOTTA, 2.4)
    y = 570
    for ln in meta["title_lines"]:
        T(c, L, y, ln, "Playfair-Med", spec.SZ_CH_TITLE, spec.CREAM)
        y -= 39
    y -= 6
    for ln in meta["lead_lines"]:
        T(c, L, y, ln, "SourceSerifItalic", 12.1, spec.GOLD_PALE)
        y -= 18.2

    y -= 14
    cx = L
    chips = [("KEY CONCEPT", meta["key_concept"])] + \
            [("RELATED", r) for r in meta["related"]] + \
            [("CONTEXT", meta["context"])]
    for lab, val in chips:
        txt = f"{lab} \u00b7 {val}".upper()
        wdt = typeset.width(txt, "Inter-Semi", 6.1, 1.25) + 18
        if cx + wdt > spec.PAGE_W - 62:
            cx = L
            y -= 26
        c.saveState()
        c.setStrokeColor(spec.GOLD_DEEP)
        c.setLineWidth(0.55)
        c.rect(cx, y - 5, wdt, 17, stroke=1, fill=0)
        c.restoreState()
        T(c, cx + 9, y - 0.5, txt, "Inter-Semi", 6.1, spec.CREAM, 1.25)
        cx += wdt + 8

    iy = 208
    c.saveState()
    c.setFillColor(spec.TERRACOTTA)
    c.rect(L, iy - 62, 1.8, 78, stroke=0, fill=1)
    c.restoreState()
    T(c, L + 14, iy + 2, "INQUIRY", "Inter-Semi", 6.4, spec.TERRACOTTA, 2.2)
    yy = iy - 15
    for ln in meta["inquiry_lines"]:
        T(c, L + 14, yy, ln, "SourceSerif", 10.6, spec.CREAM)
        yy -= 15.2

    c.saveState()
    c.setStrokeColor(spec.GOLD_DEEP)
    c.setLineWidth(0.55)
    c.line(L, 78, spec.PAGE_W - 62, 78)
    c.restoreState()
    T(c, L, 62, "SADIKOU MOUKODDIM", "Inter-Semi", 6.3, spec.GOLD_PALE, 2.1)
    T(c, spec.PAGE_W - 62, 62, "MYP MATHEMATICS 1", "Inter-Semi", 6.3, spec.GOLD_PALE,
      2.1, "right")


# --------------------------------------------------------------- part divider
def part_open(c, numeral, title_lines, subtitle_lines, meta_lines=None, motif=None):
    c.saveState()
    c.setFillColor(spec.GREEN)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    (motif or _motif_axes)(c, 300, 120, 280, 280, spec.GOLD, 0.22)
    L = 62
    T(c, L, spec.PAGE_H - 96, "PART " + numeral, "Inter-Semi", 7.4, spec.GOLD, 3.2)
    y = 560
    for ln in title_lines:
        T(c, L, y, ln, "Playfair-Display", 46, spec.CREAM, 0.3)
        y -= 56
    y -= 14
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(0.8)
    c.line(L, y, L + 120, y)
    c.restoreState()
    y -= 24
    for ln in subtitle_lines:
        T(c, L, y, ln, "SourceSerifItalic", 12.2, spec.GOLD_PALE)
        y -= 18
    if meta_lines:
        y -= 26
        for ln in meta_lines:
            T(c, L, y, ln, "SourceSerif", 9.8, spec.GOLD_PALE)
            y -= 15
    T(c, L, 56, "SADIKOU MOUKODDIM", "Inter-Semi", 6.2, spec.GOLD, 2.2)
    T(c, spec.PAGE_W - 62, 56, "MYP MATHEMATICS 1", "Inter-Semi", 6.2, spec.GOLD, 2.2,
      "right")
