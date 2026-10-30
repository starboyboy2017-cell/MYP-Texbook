"""Full-bleed plates: cover, chapter openers, back cover.

The composition follows the original first edition page for page: a deep navy
field, letterspaced cream sans labels, one oversized copper numeral, a thin
line-art motif, a high-contrast display serif for the title, boxed concept
chips and a terracotta-ruled inquiry block.

Refinements only: every plate shares one optical margin (85 pt) and one
vertical rhythm, the display setting is properly kerned and letterspaced, the
motif is now a line diagram of the chapter's actual mathematics (the original
repeated one decorative construction on all eleven openers), and the label
hierarchy has been reduced to two weights.
"""
from . import spec, typeset
from .markup import plain

T = typeset.draw


# --------------------------------------------------------------------- motifs
def _line(c, x1, y1, x2, y2, w=0.7, alpha=0.55, dash=None, colour=None):
    c.saveState()
    c.setStrokeColor(colour or spec.GOLD)
    c.setLineWidth(w)
    try:
        c.setStrokeAlpha(alpha)
    except Exception:
        pass
    if dash:
        c.setDash(*dash)
    c.line(x1, y1, x2, y2)
    c.restoreState()


def _dot(c, x, y, r=1.8, alpha=0.8):
    c.saveState()
    c.setFillColor(spec.GOLD)
    try:
        c.setFillAlpha(alpha)
    except Exception:
        pass
    c.circle(x, y, r, stroke=0, fill=1)
    c.restoreState()


def _box(x, y, w, h):
    return x, y, w, h


def motif_ratio(c, x, y, w, h):
    """Two tape bars in the ratio 3 : 5, with tick marks."""
    bh = h * 0.16
    for k, (a, b) in enumerate(((3, 5), (2, 3), (1, 2))):
        yy = y + h - (k + 0.7) * (h * 0.28)
        tot = a + b
        xa = x + w * 0.06
        w1, w2 = (w * 0.86) * a / tot, (w * 0.86) * b / tot
        c.saveState()
        c.setStrokeColor(spec.GOLD)
        c.setLineWidth(0.8)
        try:
            c.setStrokeAlpha(0.55)
        except Exception:
            pass
        c.rect(xa, yy, w1 + w2, bh, stroke=1, fill=0)
        c.line(xa + w1, yy, xa + w1, yy + bh)
        c.restoreState()
        for t in range(tot + 1):
            _line(c, xa + (w1 + w2) * t / tot, yy - 3, xa + (w1 + w2) * t / tot,
                  yy + bh + 3, 0.4, 0.35)


def motif_proportion(c, x, y, w, h):
    """Two similar triangles joined by a scale ray."""
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    try:
        c.setStrokeAlpha(0.55)
    except Exception:
        pass
    c.setLineWidth(0.8)
    p1 = (x + w * 0.10, y + h * 0.16)
    p2 = (x + w * 0.10, y + h * 0.52)
    p3 = (x + w * 0.44, y + h * 0.16)
    c.line(*p1, *p2)
    c.line(*p1, *p3)
    c.line(*p2, *p3)
    q1 = (x + w * 0.10, y + h * 0.86)
    q2 = (x + w * 0.78, y + h * 0.16)
    c.line(*p1, *q1)
    c.line(*p1, *q2)
    c.line(*q1, *q2)
    c.setDash(1.2, 4.0)
    c.line(x + w * 0.10, y + h * 0.52, x + w * 0.78, y + h * 0.52)
    c.restoreState()
    for pt in (p1, p2, p3, q1):
        _dot(c, *pt, 1.6, 0.7)


def motif_rates(c, x, y, w, h):
    """A distance-time line with a slope triangle."""
    base = y + h * 0.14
    _line(c, x + w * 0.08, base, x + w * 0.92, base, 0.7, 0.5)
    _line(c, x + w * 0.08, base, x + w * 0.08, y + h * 0.9, 0.7, 0.5)
    for i in range(1, 5):
        _line(c, x + w * 0.08, base + (h * 0.76) * i / 5, x + w * 0.92,
              base + (h * 0.76) * i / 5, 0.3, 0.18)
        _line(c, x + w * 0.08 + (w * 0.84) * i / 5, base, x + w * 0.08 + (w * 0.84) * i / 5,
              y + h * 0.9, 0.3, 0.18)
    _line(c, x + w * 0.08, base, x + w * 0.90, y + h * 0.82, 1.0, 0.7)
    _line(c, x + w * 0.68, base, x + w * 0.68, base + (h * 0.76) * 3 / 5, 0.5, 0.5,
          dash=(1.2, 3.0))
    _line(c, x + w * 0.68, base + (h * 0.76) * 3 / 5, x + w * 0.90,
          base + (h * 0.76) * 3 / 5, 0.5, 0.5, dash=(1.2, 3.0))
    _dot(c, x + w * 0.90, y + h * 0.82, 1.8, 0.85)


def motif_integers(c, x, y, w, h):
    """A number line across zero with signed arrows."""
    base = y + h * 0.5
    _line(c, x + w * 0.05, base, x + w * 0.95, base, 0.9, 0.6)
    for i in range(-4, 5):
        cx = x + w * 0.5 + i * w * 0.09
        _line(c, cx, base - 4, cx, base + 4, 0.6, 0.45)
    _line(c, x + w * 0.95, base, x + w * 0.95 - w * 0.03, base + 3, 0.9, 0.6)
    _line(c, x + w * 0.95, base, x + w * 0.95 - w * 0.03, base - 3, 0.9, 0.6)
    _dot(c, x + w * 0.5 - w * 0.18, base, 2.2, 0.85)
    _dot(c, x + w * 0.5 + w * 0.27, base, 2.2, 0.85)


def motif_algebra(c, x, y, w, h):
    """A balance beam, level, with equal weights."""
    beam = y + h * 0.62
    cx = x + w * 0.5
    _line(c, cx, y + h * 0.10, cx, beam, 1.0, 0.65)
    _line(c, x + w * 0.12, beam, x + w * 0.88, beam, 1.1, 0.7)
    _line(c, x + w * 0.12, beam, x + w * 0.20, y + h * 0.30, 0.7, 0.5)
    _line(c, x + w * 0.20, y + h * 0.30, x + w * 0.04, y + h * 0.30, 0.7, 0.5)
    _line(c, x + w * 0.88, beam, x + w * 0.80, y + h * 0.30, 0.7, 0.5)
    _line(c, x + w * 0.80, y + h * 0.30, x + w * 0.96, y + h * 0.30, 0.7, 0.5)
    c.saveState()
    c.setFillColor(spec.GOLD)
    try:
        c.setFillAlpha(0.45)
    except Exception:
        pass
    c.rect(x + w * 0.06, y + h * 0.30, w * 0.10, h * 0.10, stroke=0, fill=1)
    c.rect(x + w * 0.84, y + h * 0.30, w * 0.10, h * 0.10, stroke=0, fill=1)
    c.restoreState()


def motif_patterns(c, x, y, w, h):
    """A growing staircase: n, 2n + 1."""
    n = 6
    step = w * 0.86 / n
    hstep = h * 0.72 / n
    for i in range(1, n + 1):
        _line(c, x + w * 0.07 + (i - 1) * step, y + h * 0.12, x + w * 0.07 + (i - 1) * step,
              y + h * 0.12 + i * hstep, 0.7, 0.5)
        _line(c, x + w * 0.07 + (i - 1) * step, y + h * 0.12 + i * hstep,
              x + w * 0.07 + i * step, y + h * 0.12 + i * hstep, 0.7, 0.5)
    _line(c, x + w * 0.07, y + h * 0.12, x + w * 0.07 + n * step, y + h * 0.12, 0.9, 0.6)
    for i in range(1, n + 1):
        _dot(c, x + w * 0.07 + (i - 0.5) * step, y + h * 0.12 + i * hstep + 4, 1.5, 0.7)


def motif_angles(c, x, y, w, h):
    """A triangle with its angle arcs and a parallel construction."""
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    try:
        c.setStrokeAlpha(0.6)
    except Exception:
        pass
    c.setLineWidth(0.9)
    p = [(x + w * 0.10, y + h * 0.14), (x + w * 0.90, y + h * 0.14),
         (x + w * 0.38, y + h * 0.80)]
    c.line(*p[0], *p[1])
    c.line(*p[1], *p[2])
    c.line(*p[2], *p[0])
    c.setLineWidth(0.55)
    for (a, b, cc) in (p,):
        pass
    c.arc(x + w * 0.10 - 16, y + h * 0.14 - 16, x + w * 0.10 + 16,
          y + h * 0.14 + 16, startAng=0, extent=38)
    c.arc(x + w * 0.90 - 14, y + h * 0.14 - 14, x + w * 0.90 + 14,
          y + h * 0.14 + 14, startAng=152, extent=40)
    c.restoreState()
    _line(c, x + w * 0.20, y + h * 0.92, x + w * 0.96, y + h * 0.92, 0.8, 0.45)


def motif_3d(c, x, y, w, h):
    """An isometric cuboid with its hidden edges dashed."""
    dx, dy = w * 0.20, h * 0.13
    fx, fy = x + w * 0.12, y + h * 0.18
    bw, bh = w * 0.48, h * 0.40
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    try:
        c.setStrokeAlpha(0.6)
    except Exception:
        pass
    c.setLineWidth(0.9)
    for (ox, oy) in ((0, 0), (dx, dy)):
        c.rect(fx + ox, fy + oy, bw, bh, stroke=1, fill=0)
    c.line(fx, fy, fx + dx, fy + dy)
    c.line(fx + bw, fy, fx + bw + dx, fy + dy)
    c.line(fx, fy + bh, fx + dx, fy + bh + dy)
    c.line(fx + bw, fy + bh, fx + bw + dx, fy + bh + dy)
    c.setDash(1.4, 3.4)
    c.setLineWidth(0.6)
    c.line(fx + dx, fy, fx + bw + dx, fy)
    c.restoreState()


def motif_transform(c, x, y, w, h):
    """A shape, its mirror image and a mirror line."""
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    try:
        c.setStrokeAlpha(0.55)
    except Exception:
        pass
    c.setLineWidth(0.9)
    ax = x + w * 0.5
    c.setDash(1.6, 4.0)
    c.line(ax, y + h * 0.08, ax, y + h * 0.92)
    c.setDash()
    pts = [(0.06, 0.20), (0.34, 0.20), (0.34, 0.44), (0.20, 0.44), (0.20, 0.72),
           (0.06, 0.72)]
    for sign in (-1, 1):
        p = c.beginPath()
        for i, (px, py) in enumerate(pts):
            X = ax + sign * (px * w)
            Y = y + py * h
            if i == 0:
                p.moveTo(X, Y)
            else:
                p.lineTo(X, Y)
        p.close()
        c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def motif_probability(c, x, y, w, h):
    """A two-stage probability tree."""
    root = (x + w * 0.16, y + h * 0.5)
    a = (x + w * 0.52, y + h * 0.78)
    b = (x + w * 0.52, y + h * 0.22)
    ends = [(x + w * 0.90, y + h * 0.92), (x + w * 0.90, y + h * 0.62),
            (x + w * 0.90, y + h * 0.38), (x + w * 0.90, y + h * 0.08)]
    for p in (a, b):
        _line(c, root[0], root[1], p[0], p[1], 0.9, 0.6)
    _line(c, a[0], a[1], ends[0][0], ends[0][1], 0.7, 0.45)
    _line(c, a[0], a[1], ends[1][0], ends[1][1], 0.7, 0.45)
    _line(c, b[0], b[1], ends[2][0], ends[2][1], 0.7, 0.45)
    _line(c, b[0], b[1], ends[3][0], ends[3][1], 0.7, 0.45)
    for p in [root, a, b] + ends:
        _dot(c, p[0], p[1], 1.8, 0.8)


def motif_data(c, x, y, w, h):
    """A dot plot above a box plot on a shared scale."""
    base = y + h * 0.62
    _line(c, x + w * 0.06, base, x + w * 0.94, base, 0.8, 0.5)
    heights = [1, 2, 3, 3, 4, 3, 2, 2, 1]
    for i, k in enumerate(heights):
        for j in range(k):
            _dot(c, x + w * 0.12 + i * w * 0.09, base + 8 + j * 8, 1.7, 0.7)
    by = y + h * 0.20
    q1, med, q3 = x + w * 0.26, x + w * 0.50, x + w * 0.70
    lo, hi = x + w * 0.12, x + w * 0.86
    _line(c, lo, by, hi, by, 0.7, 0.5)
    _line(c, lo, by - 5, lo, by + 5, 0.7, 0.5)
    _line(c, hi, by - 5, hi, by + 5, 0.7, 0.5)
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(0.9)
    try:
        c.setStrokeAlpha(0.65)
    except Exception:
        pass
    c.rect(q1, by - 9, q3 - q1, 18, stroke=1, fill=0)
    c.line(med, by - 9, med, by + 9)
    c.restoreState()


def _grid(c, x, y, w, h, grid=22, alpha=0.16):
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(0.28)
    try:
        c.setStrokeAlpha(alpha)
    except Exception:
        pass
    gx = x
    while gx <= x + w + 0.1:
        c.line(gx, y, gx, y + h)
        gx += grid
    gy = y
    while gy <= y + h + 0.1:
        c.line(x, gy, x + w, gy)
        gy += grid
    c.restoreState()


MOTIFS = {
    "ratio": motif_ratio, "proportion": motif_proportion, "rates": motif_rates,
    "integers": motif_integers, "algebra": motif_algebra, "patterns": motif_patterns,
    "angles": motif_angles, "solid": motif_3d, "transform": motif_transform,
    "probability": motif_probability, "data": motif_data,
}


# ---------------------------------------------------------------------- covers
def cover(c, meta=None):
    c.saveState()
    c.setFillColor(spec.NAVY)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()

    L, R = spec.MARGIN_OUTER, spec.PAGE_W - spec.MARGIN_OUTER

    # left grid rule, foot rules: the original's plate lines
    _line(c, 66, 0, 66, spec.PAGE_H, 0.4, 0.10, colour=spec.CREAM)
    _line(c, 92, 0, 92, spec.PAGE_H, 0.3, 0.07, colour=spec.CREAM)
    for yy in (104, 132, 160, 188):
        _line(c, 0, yy, spec.PAGE_W, yy, 0.3, 0.06, colour=spec.CREAM)
        _line(c, 0, spec.PAGE_H - yy, spec.PAGE_W, spec.PAGE_H - yy, 0.3, 0.05,
              colour=spec.CREAM)

    # top labels
    T(c, L, spec.PAGE_H - 76, "MYP YEAR 2  \u00b7  STUDENT COURSEBOOK", "Inter-Semi",
      6.9, spec.CREAM, 2.55)
    T(c, R, spec.PAGE_H - 76, "IMPROVED FIRST EDITION", "Inter-Semi", 6.3, spec.GOLD,
      2.4, "right")

    # the copper construction: a spiral of squares, drawn to the page's own ratio
    gx, gy, gw, gh = R - 268, 470, 268, 300
    _line(c, gx, gy, gx, gy + gh, 1.0, 0.8)
    _line(c, gx, gy, gx + gw, gy, 1.0, 0.8)
    _line(c, gx + gw, gy, gx + gw, gy + gh * 0.62, 1.0, 0.55)
    _line(c, gx, gy + gh * 0.62, gx + gw * 0.46, gy + gh * 0.62, 1.0, 0.55)
    _line(c, gx + gw * 0.46, gy, gx + gw * 0.46, gy + gh * 0.62, 1.0, 0.55)
    _line(c, gx, gy + gh * 0.24, gx + gw * 0.46, gy + gh * 0.24, 0.8, 0.4)
    _line(c, gx + gw * 0.46 + gw * 0.30, gy, gx + gw * 0.46 + gw * 0.30,
          gy + gh * 0.62, 0.8, 0.35)
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(1.1)
    try:
        c.setStrokeAlpha(0.85)
    except Exception:
        pass
    c.bezier(gx, gy, gx, gy + gh * 0.45, gx + gw * 0.46, gy + gh * 0.62,
             gx + gw * 0.46, gy + gh * 0.62)
    c.bezier(gx + gw * 0.46, gy + gh * 0.62, gx + gw, gy + gh * 0.62,
             gx + gw, gy + gh * 0.30, gx + gw, gy)
    c.restoreState()
    for p in ((gx, gy), (gx + gw, gy), (gx, gy + gh * 0.62),
              (gx + gw * 0.46, gy + gh * 0.62), (gx + gw, gy + gh)):
        _dot(c, p[0], p[1], 2.2, 0.9)
    _line(c, gx + gw * 0.46, gy, gx + gw * 0.46, gy + gh * 0.62, 0.6, 0.4)

    # eyebrow and title
    T(c, L, 540, "MYP", "Inter-Semi", 8.6, spec.GOLD, 3.4)
    size = typeset.fit("MATHEMATICS", "Playfair-Display", 62, R - L - 10)
    T(c, L - 2, 484, "MATHEMATICS", "Playfair-Display", size, spec.CREAM, 0.4)

    # year numeral, optically aligned to the title's baseline
    c.saveState()
    c.setFont("Playfair-Display", 104)
    c.setFillColor(spec.GOLD)
    c.drawString(L - 4, 404, "2")
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(1.1)
    c.line(L, 392, L + 58, 392)
    c.restoreState()

    T(c, L + 82, 424, "STUDENT COURSEBOOK", "Inter-Semi", 7.4, spec.CREAM, 2.35)
    c.saveState()
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(0.7)
    c.line(L + 82, 410, L + 82 + 232, 410)
    c.restoreState()
    T(c, L, 356, "\u25c7", "Sym", 7.0, spec.GOLD)
    T(c, L + 30, 353, "A concept-driven inquiry course", "SourceSerifItalic", 14.2,
      spec.CREAM)

    T(c, L, 320, "Ratio and proportion \u00b7 Algebra and pattern", "SourceSerif", 9.6,
      spec.GOLD_PALE)
    T(c, L, 306, "Geometry and space \u00b7 Probability and data", "SourceSerif", 9.6,
      spec.GOLD_PALE)
    _line(c, L, 288, R, 288, 0.4, 0.30, colour=spec.GOLD)
    T(c, L, 272, "Complete worked solutions \u00b7 Investigations \u00b7 "
                "Criterion-mapped tasks", "Inter", 7.2, spec.CREAM, 0.9)

    # author block
    _line(c, L, 96, R, 96, 0.55, 0.55, colour=spec.GOLD)
    T(c, L, 74, "SADIKOU MOUKODDIM", "SourceSerif-Semi", 13.4, spec.CREAM, 0.4)
    T(c, L, 58, "HEAD OF MATHEMATICS DEPARTMENT  \u00b7  MATHEMATICS TEACHER  \u00b7  "
                "CATEGORY 1", "Inter", 6.2, spec.GOLD_PALE, 1.1)
    T(c, R, 74, "MIDDLE YEARS", "Inter-Semi", 6.4, spec.GOLD, 2.2, "right")
    T(c, R, 58, "PROGRAMME", "Inter-Semi", 6.4, spec.GOLD, 2.2, "right")


def back_cover(c, meta=None):
    c.saveState()
    c.setFillColor(spec.NAVY)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    L, R = spec.MARGIN_OUTER, spec.PAGE_W - spec.MARGIN_OUTER
    _grid(c, R - 210, spec.PAGE_H - 350, 210, 210, 22, 0.14)
    motif_data(c, R - 210, spec.PAGE_H - 350, 210, 210)

    T(c, L, spec.PAGE_H - 120, "Mathematics is a way of seeing,", "Playfair-Display", 25,
      spec.CREAM)
    T(c, L, spec.PAGE_H - 150, "not a list of rules.", "Playfair-Display", 25, spec.CREAM)

    body = [
        "Eleven chapters build Year 2 mathematics from comparison to conclusion:",
        "how a ratio holds a relationship steady while quantities change; how a",
        "constant of proportionality links a recipe to a banquet and a map to a",
        "journey; how negative numbers extend the number line in both directions;",
        "how a letter compresses a pattern into a rule; how angle, area and volume",
        "answer practical questions; and how probability and data turn uncertainty",
        "into a defensible claim.",
    ]
    y = spec.PAGE_H - 206
    for ln in body:
        T(c, L, y, ln, "SourceSerif", 10.0, spec.GOLD_PALE)
        y -= 15.2

    y -= 14
    body2 = [
        "Every chapter moves through one rhythm: engage, explore, explain, work",
        "through examples, practise, investigate and reflect. Each section names",
        "the MYP criterion it develops, and each chapter closes with a review, a",
        "mixed practice set and a criterion-mapped mini-task.",
    ]
    for ln in body2:
        T(c, L, y, ln, "SourceSerif", 10.0, spec.GOLD_PALE)
        y -= 15.2

    _line(c, L, 214, R, 214, 0.55, 0.5, colour=spec.GOLD)
    T(c, L, 192, "SADIKOU MOUKODDIM", "SourceSerifItalic", 11.0, spec.CREAM)
    T(c, L, 178, "AUTHOR  \u00b7  HEAD OF MATHEMATICS DEPARTMENT", "Inter-Semi", 6.2,
      spec.GOLD, 2.1)
    T(c, L, 118, "An independent educational publication. Not published by, sponsored by,",
      "Inter", 6.4, spec.GOLD_PALE)
    T(c, L, 108, "endorsed by or affiliated with the International Baccalaureate "
                "Organization.", "Inter", 6.4, spec.GOLD_PALE)
    T(c, L, 78, "MYP MATHEMATICS 2  \u00b7  IMPROVED FIRST EDITION  \u00b7  "
                "STUDENT COURSEBOOK", "Inter-Semi", 6.4, spec.GOLD, 1.8)


# --------------------------------------------------------------- chapter plate
def chapter_plate(c, meta):
    c.saveState()
    c.setFillColor(spec.NAVY)
    c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
    c.restoreState()
    L, R = spec.MARGIN_OUTER, spec.PAGE_W - spec.MARGIN_OUTER

    # top labels
    T(c, L, spec.PAGE_H - 70, plain(meta["part"]).upper(), "Inter-Semi", 6.5,
      spec.GOLD_PALE, 2.2)
    T(c, L, spec.PAGE_H - 82, "MYP YEAR 2", "Inter-Semi", 6.5, spec.GOLD_PALE, 2.2)
    T(c, R, spec.PAGE_H - 70, "CHAPTER " + str(meta["chapter_no"]).zfill(2),
      "Inter-Semi", 6.5, spec.GOLD_PALE, 2.2, "right")
    T(c, R, spec.PAGE_H - 82, "PART " + meta["part_numeral"], "Inter-Semi", 6.5,
      spec.GOLD_PALE, 2.2, "right")

    # motif, upper right, on its own faint grid
    mx, my = R - 216, spec.PAGE_H - 344
    _grid(c, mx, my, 216, 216, 24, 0.13)
    MOTIFS.get(meta.get("motif", "ratio"), motif_ratio)(c, mx, my, 216, 216)

    # oversized numeral
    c.saveState()
    c.setFont("Playfair-Display", 96)
    c.setFillColor(spec.GOLD)
    c.drawString(L - 3, 604, str(meta["chapter_no"]))
    c.setStrokeColor(spec.GOLD)
    c.setLineWidth(1.0)
    c.line(L, 592, L + 62, 592)
    c.restoreState()

    T(c, L, 556, plain(meta["kicker"]).upper(), "Inter-Semi", 6.9, spec.TERRACOTTA, 2.4)
    y = 522
    for ln in meta["title_lines"]:
        T(c, L, y, ln, "Playfair-Med", spec.SZ_CH_TITLE, spec.CREAM)
        y -= 41
    y -= 4
    for ln in meta["lead_lines"]:
        T(c, L, y, ln, "SourceSerifItalic", 12.0, spec.GOLD_PALE)
        y -= 18.0

    # concept chips
    y -= 16
    cx = L
    chips = [("KEY CONCEPT", meta["key_concept"])] + \
            [("RELATED", r) for r in meta["related"]] + \
            [("CONTEXT", meta["context"])]
    for lab, val in chips:
        txt = f"{lab} \u00b7 {val}".upper()
        wdt = typeset.width(txt, "Inter-Semi", 6.1, 1.25) + 20
        if cx + wdt > R:
            cx = L
            y -= 26
        c.saveState()
        c.setStrokeColor(spec.GOLD)
        c.setLineWidth(0.5)
        try:
            c.setStrokeAlpha(0.75)
        except Exception:
            pass
        c.rect(cx, y - 5, wdt, 17, stroke=1, fill=0)
        c.restoreState()
        T(c, cx + 10, y - 0.5, txt, "Inter-Semi", 6.1, spec.CREAM, 1.25)
        cx += wdt + 8

    # inquiry block
    iy = 236
    c.saveState()
    c.setFillColor(spec.TERRACOTTA)
    c.rect(L, iy - 60, 1.8, 76, stroke=0, fill=1)
    c.restoreState()
    T(c, L + 15, iy + 2, "INQUIRY", "Inter-Semi", 6.4, spec.TERRACOTTA, 2.2)
    yy = iy - 16
    for ln in meta["inquiry_lines"]:
        T(c, L + 15, yy, ln, "SourceSerif", 10.6, spec.CREAM)
        yy -= 15.4

    _line(c, L, 78, R, 78, 0.55, 0.5, colour=spec.GOLD)
    T(c, L, 62, "SADIKOU MOUKODDIM", "Inter-Semi", 6.3, spec.GOLD_PALE, 2.1)
    T(c, R, 62, "MYP MATHEMATICS 2", "Inter-Semi", 6.3, spec.GOLD_PALE, 2.1, "right")
