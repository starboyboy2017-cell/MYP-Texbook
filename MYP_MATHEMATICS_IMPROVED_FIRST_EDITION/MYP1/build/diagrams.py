"""Original vector diagrams for the improved edition.

Every function signature is fn(canvas, x, y, w, h) and draws inside that box,
so diagrams stay resolution independent and always match the palette.
"""
import math

from reportlab.pdfbase.pdfmetrics import stringWidth

from bookkit import spec

INK = spec.INK
GREEN = spec.GREEN
GOLD = spec.GOLD
GOLD_D = spec.GOLD_DEEP
TERRA = spec.TERRACOTTA
SAGE = spec.SAGE
RULE = spec.RULE
SAND = spec.SAND
CREAM = spec.CREAM_SOFT


# --------------------------------------------------------------------- helpers
def txt(c, x, y, s, size=7.6, font="SourceSerif", col=INK, align="left"):
    c.setFont(font, size)
    c.setFillColor(col)
    w = stringWidth(s, font, size)
    if align == "center":
        x -= w / 2
    elif align == "right":
        x -= w
    c.drawString(x, y, s)
    return w


def line(c, x1, y1, x2, y2, col=INK, lw=0.8, dash=None):
    c.saveState()
    c.setStrokeColor(col)
    c.setLineWidth(lw)
    if dash:
        c.setDash(dash)
    c.line(x1, y1, x2, y2)
    c.restoreState()


def arrow(c, x1, y1, x2, y2, col=INK, lw=0.8, head=3.2):
    line(c, x1, y1, x2, y2, col, lw)
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (0.4, -0.4):
        c.saveState()
        c.setStrokeColor(col)
        c.setLineWidth(lw)
        c.line(x2, y2, x2 - head * math.cos(ang - s), y2 - head * math.sin(ang - s))
        c.restoreState()


def box(c, x, y, w, h, fill=None, stroke=RULE, lw=0.6, dash=None):
    c.saveState()
    if fill is not None:
        c.setFillColor(fill)
    if stroke is not None:
        c.setStrokeColor(stroke)
    c.setLineWidth(lw)
    if dash:
        c.setDash(dash)
    c.rect(x, y, w, h, stroke=1 if stroke else 0, fill=1 if fill is not None else 0)
    c.restoreState()


def hatched_rect(c, x, y, w, h, fill=SAND, stroke=GOLD_D):
    box(c, x, y, w, h, fill=fill, stroke=stroke, lw=0.6)


# ---------------------------------------------------------------- ch1 diagrams
def number_line(c, x, y, w, h, lo=-5, hi=5, marks=None, highlight=(), label_all=True,
                caption_marks=None):
    """Horizontal number line with optional highlighted integers."""
    mid = y + h * 0.42
    x0, x1 = x + 6, x + w - 6
    line(c, x0, mid, x1, mid, INK, 0.9)
    arrow(c, x1 - 8, mid, x1, mid, INK, 0.9)
    n = hi - lo
    step = (x1 - x0 - 8) / n
    for i in range(n + 1):
        v = lo + i
        px = x0 + i * step
        big = (v % 5 == 0)
        line(c, px, mid - (4.4 if big else 2.8), px, mid + (4.4 if big else 2.8), INK, 0.7)
        if label_all:
            txt(c, px, mid - 15, str(v).replace("-", "\u2212"), 7.6, "SourceSerif", INK, "center")
        if v in highlight:
            c.saveState()
            c.setFillColor(TERRA)
            c.circle(px, mid, 3.1, stroke=0, fill=1)
            c.restoreState()
    txt(c, x1 - 2, mid + 9, "\u2192", 9, "Sym", INK, "center")


def place_value_table(c, x, y, w, h, number="3 048. 7 6", headers=None):
    headers = headers or ["1000", "100", "10", "1", "\u00b7", "0.1", "0.01"]
    digits = [d for d in number if d.isdigit()]
    n = len(headers)
    cw = w / n
    top = y + h
    for i, hd in enumerate(headers):
        cx = x + i * cw
        if hd == "\u00b7":
            box(c, cx, top - 34, cw, 34, fill=None, stroke=None)
            c.saveState()
            c.setFillColor(TERRA)
            c.circle(cx + cw / 2, top - 17, 2.0, stroke=0, fill=1)
            c.restoreState()
            continue
        box(c, cx, top - 34, cw, 34, fill=CREAM, stroke=RULE, lw=0.5)
        txt(c, cx + cw / 2, top - 14, hd, 6.6, "Inter", GOLD_D, "center")
        box(c, cx, top - 64, cw, 30, fill=None, stroke=RULE, lw=0.5)
        idx = i if i < 4 else i - 1
        txt(c, cx + cw / 2, top - 54, digits[idx], 13, "Playfair", GREEN, "center")
        # place-value label
        txt(c, cx + cw / 2, top - 78, ["thousands", "hundreds", "tens", "ones", "",
                                       "tenths", "hundredths"][i], 5.6, "Inter",
            spec.INK_MUTE, "center")


def rounding_line(c, x, y, w, h, value=348, lower=340, upper=350, mid=345):
    mid_y = y + h * 0.5
    x0, x1 = x + 34, x + w - 34
    line(c, x0, mid_y, x1, mid_y, INK, 0.9)
    for v in (lower, mid, upper):
        if v == mid:
            continue
        px = x0 + (v - lower) / (upper - lower) * (x1 - x0)
        line(c, px, mid_y - 5, px, mid_y + 5, INK, 0.8)
        txt(c, px, mid_y - 16, str(v), 7.8, "SourceSerif", INK, "center")
    px = x0 + (mid - lower) / (upper - lower) * (x1 - x0)
    line(c, px, mid_y - 7, px, mid_y + 7, TERRA, 0, dash=(2, 3))
    c.saveState()
    c.setStrokeColor(TERRA)
    c.setLineWidth(0.9)
    c.setDash(2, 3)
    c.line(px, mid_y - 9, px, mid_y + 9)
    c.restoreState()
    txt(c, px, mid_y - 25, str(mid), 7.4, "SourceSerifItalic", TERRA, "center")
    # value marker
    vx = x0 + (value - lower) / (upper - lower) * (x1 - x0)
    arrow(c, vx, mid_y + 26, vx, mid_y + 4, GREEN, 0.9)
    txt(c, vx + 3, mid_y + 29, str(value), 8.2, "SourceSerif-Semi", GREEN)
    # rounding destinations
    txt(c, x0, mid_y + 20, f"round down \u2192 {lower}", 6.8, "Inter", SAGE)
    txt(c, x1, mid_y + 20, f"round up \u2192 {upper}", 6.8, "Inter", TERRA, "right")


def expanded_form_strip(c, x, y, w, h):
    parts = [("3", "\u00d7 1000", 3000), ("0", "\u00d7 100", 0),
             ("4", "\u00d7 10", 40), ("8", "\u00d7 1", 8)]
    cw = w / 4
    for i, (d, mult, val) in enumerate(parts):
        cx = x + i * cw
        box(c, cx + 3, y + h * 0.42, cw - 6, h * 0.5, fill=CREAM, stroke=RULE, lw=0.5)
        txt(c, cx + cw / 2, y + h * 0.62, d, 17, "Playfair", GREEN, "center")
        txt(c, cx + cw / 2, y + h * 0.48, mult, 7.2, "Inter", GOLD_D, "center")
        txt(c, cx + cw / 2, y + h * 0.24, f"= {val}", 8.0, "SourceSerif", INK, "center")
        if i < 3:
            txt(c, cx + cw - 1, y + h * 0.60, "+", 11, "SourceSerif", TERRA, "center")


def hundreds_grid(c, x, y, w, h, filled=100):
    """10x10 grid used for decimals / percentages."""
    cols, rows = 10, 10
    s = min(w / cols, h / rows)
    for r in range(rows):
        for q in range(cols):
            n = r * cols + q
            xx, yy = x + q * s, y + (rows - 1 - r) * s
            box(c, xx, yy, s, s, fill=(SAGE if n < filled else None), stroke=RULE, lw=0.4)


def bar_model(c, x, y, w, h, segments):
    """segments: list of (label, weight, colour)."""
    tot = sum(s[1] for s in segments)
    cx = x
    for lab, wt, col in segments:
        bw = w * wt / tot
        box(c, cx, y, bw, h, fill=col, stroke=None)
        txt(c, cx + bw / 2, y + h / 2 - 3, lab, 7.6, "Inter-Semi", spec.PAPER, "center")
        cx += bw
    c.saveState()
    c.setStrokeColor(spec.PAPER)
    c.setLineWidth(0.8)
    cx = x
    for lab, wt, col in segments[:-1]:
        cx += w * wt / tot
        c.line(cx, y, cx, y + h)
    c.restoreState()


def fraction_strips(c, x, y, w, h, rows):
    rh = h / len(rows)
    for i, (n, shaded, lab) in enumerate(rows):
        yy = y + h - (i + 1) * rh + rh * 0.16
        hh = rh * 0.68
        for k in range(n):
            sw = w / n
            fill = SAGE if k < shaded else None
            box(c, x + k * sw, yy, sw, hh, fill=fill, stroke=GREEN if fill else RULE,
                lw=0.5 if fill else 0.45)
        txt(c, x + w + 5, yy + hh / 2 - 2.4, lab, 7.0, "Inter", INK, "left")


def triangle_angle_diagram(c, x, y, w, h):
    A = (x + w * 0.12, y + h * 0.12)
    B = (x + w * 0.88, y + h * 0.12)
    C = (x + w * 0.46, y + h * 0.84)
    c.saveState()
    c.setStrokeColor(GREEN)
    c.setLineWidth(1.3)
    p = c.beginPath()
    p.moveTo(*A)
    p.lineTo(*B)
    p.lineTo(*C)
    p.close()
    c.setFillColor(spec.CREAM_SOFT)
    c.drawPath(p, stroke=1, fill=1)
    c.restoreState()
    for pt, lab, dx, dy in ((A, "A", -10, -4), (B, "B", 6, -4), (C, "C", -2, 9)):
        txt(c, pt[0] + dx, pt[1] + dy, lab, 8.4, "SourceSerifItalic", INK)
    # angle arcs
    for pt, a1, a2 in ((A, 0, 33), (B, 147, 180), (C, 250, 292)):
        c.saveState()
        c.setStrokeColor(TERRA)
        c.setLineWidth(0.7)
        c.arc(pt[0] - 18, pt[1] - 18, pt[0] + 18, pt[1] + 18, startAng=a1, extent=a2 - a1)
        c.restoreState()
    txt(c, A[0] + 24, A[1] + 8, "a", 7.4, "SourceSerifItalic", TERRA)
    txt(c, B[0] - 26, B[1] + 8, "b", 7.4, "SourceSerifItalic", TERRA)
    txt(c, C[0] + 8, C[1] - 16, "c", 7.4, "SourceSerifItalic", TERRA)


def parallel_lines(c, x, y, w, h):
    y1, y2 = y + h * 0.32, y + h * 0.72
    line(c, x + 4, y1, x + w - 4, y1, GREEN, 1.0)
    line(c, x + 4, y2, x + w - 4, y2, GREEN, 1.0)
    tx = x + w * 0.30
    bx = x + w * 0.62
    line(c, tx, y - 2, bx, y + h + 2, INK, 0.9)
    for lab, px, py, col in (("1", tx + 8, y1 + 8, TERRA), ("2", tx + 8, y1 - 12, SAGE),
                             ("3", tx + 32, y1 + 8, SAGE), ("4", tx + 32, y1 - 12, TERRA),
                             ("5", bx - 16, y2 + 8, TERRA), ("6", bx - 16, y2 - 12, SAGE)):
        txt(c, px, py, lab, 7.0, "Inter-Semi", col)


def venn(c, x, y, w, h, left_label="A", right_label="B", left_n="", right_n="",
         both_n="", outside_n=""):
    r = min(w, h) * 0.28
    cx1, cy = x + w / 2 - r * 0.62, y + h / 2
    cx2 = x + w / 2 + r * 0.62
    c.saveState()
    c.setStrokeColor(GREEN)
    c.setLineWidth(0.9)
    c.setFillColor(spec.MIST)
    try:
        c.setFillAlpha(0.55)
    except Exception:
        pass
    c.circle(cx1, cy, r, stroke=1, fill=1)
    c.setFillColor(spec.SAND)
    c.circle(cx2, cy, r, stroke=1, fill=1)
    c.restoreState()
    txt(c, cx1 - r * 0.55, cy + r + 8, left_label, 8.0, "SourceSerifItalic", SAGE, "center")
    txt(c, cx2 + r * 0.55, cy + r + 8, right_label, 8.0, "SourceSerifItalic", TERRA, "center")
    if left_n:
        txt(c, cx1 - r * 0.45, cy - 3, left_n, 8.4, "Inter-Semi", INK, "center")
    if right_n:
        txt(c, cx2 + r * 0.45, cy - 3, right_n, 8.4, "Inter-Semi", INK, "center")
    if both_n:
        txt(c, x + w / 2, cy - 3, both_n, 8.4, "Inter-Semi", INK, "center")
    if outside_n:
        txt(c, x + 8, y + 6, outside_n, 7.4, "Inter", spec.INK_MUTE, "left")


def prism(c, x, y, w, h, show_units=True):
    """A cuboid drawn inside the given box, with length, width and height labelled."""
    pw, ph = w * 0.58, h * 0.46
    dx, dy = w * 0.13, h * 0.20
    ox = x + w * 0.10
    oy = y + h * 0.20
    A = (ox, oy)                       # front bottom-left
    B = (ox + pw, oy)                  # front bottom-right
    C = (ox + pw, oy + ph)             # front top-right
    D = (ox, oy + ph)                  # front top-left
    A2 = (A[0] + dx, A[1] + dy)
    B2 = (B[0] + dx, B[1] + dy)
    C2 = (C[0] + dx, C[1] + dy)
    D2 = (D[0] + dx, D[1] + dy)
    c.saveState()
    c.setStrokeColor(GREEN)
    c.setLineWidth(0.9)
    # back face (top)
    p = c.beginPath(); p.moveTo(*D); p.lineTo(*C); p.lineTo(*C2); p.lineTo(*D2); p.close()
    c.setFillColor(spec.MIST); c.drawPath(p, stroke=1, fill=1)
    # right side face
    p = c.beginPath(); p.moveTo(*B); p.lineTo(*C); p.lineTo(*C2); p.lineTo(*B2); p.close()
    c.setFillColor(spec.BLUSH); c.drawPath(p, stroke=1, fill=1)
    # front face last, so it sits in front
    p = c.beginPath(); p.moveTo(*A); p.lineTo(*B); p.lineTo(*C); p.lineTo(*D); p.close()
    c.setFillColor(spec.SAND); c.drawPath(p, stroke=1, fill=1)
    c.restoreState()
    if show_units:
        txt(c, (A[0] + B[0]) / 2, oy - 11, "length", 6.8, "Inter", spec.INK_MUTE,
            "center")
        txt(c, A[0] - 5, (A[1] + D[1]) / 2 - 4, "height", 6.8, "Inter", spec.INK_MUTE,
            "right")
        txt(c, B2[0] + 4, (B[1] + B2[1]) / 2, "width", 6.8, "Inter", spec.INK_MUTE)


def pie(c, cx, cy, r, slices, label_inside=True):
    """slices: list of (value, colour, label)."""
    tot = sum(s[0] for s in slices)
    a = 90
    for val, col, lab in slices:
        ext = -360 * val / tot
        c.saveState()
        c.setFillColor(col)
        c.setStrokeColor(spec.PAPER)
        c.setLineWidth(0.9)
        c.wedge(cx - r, cy - r, cx + r, cy + r, a, ext, stroke=1, fill=1)
        c.restoreState()
        if label_inside and val / tot > 0.06:
            mid = math.radians(a + ext / 2)
            txt(c, cx + r * 0.62 * math.cos(mid), cy + r * 0.62 * math.sin(mid) - 3,
                lab, 6.8, "Inter-Semi", spec.PAPER, "center")
        a += ext


def barchart(c, x, y, w, h, data, ymax=None, colour=SAGE, gap=0.34, value_labels=True,
             horizontal_grid=True):
    """data: list of (label, value)."""
    n = len(data)
    ymax = ymax or max(v for _, v in data) * 1.18
    plot_h = h * 0.78
    if horizontal_grid:
        for i in range(1, 4):
            gy = y + plot_h * i / 3
            line(c, x, gy, x + w, gy, spec.RULE_SOFT, 0.4, dash=(1.5, 3))
    bw = w / n * (1 - gap)
    for i, (lab, v) in enumerate(data):
        cx = x + (i + 0.5) * (w / n) - bw / 2
        bh = plot_h * v / ymax
        box(c, cx, y, bw, bh, fill=colour, stroke=None)
        if value_labels:
            txt(c, cx + bw / 2, y + bh + 3, str(v), 6.4, "Inter-Semi", INK, "center")
        txt(c, cx + bw / 2, y - 9, lab, 6.4, "Inter", INK, "center")
    line(c, x, y, x + w, y, INK, 0.7)


def dotplot(c, x, y, w, h, values, lo=None, hi=None):
    lo = lo if lo is not None else min(values)
    hi = hi if hi is not None else max(values)
    n = hi - lo
    step = w / max(1, n)
    line(c, x, y, x + w, y, INK, 0.8)
    for i in range(n + 1):
        px = x + i * step
        line(c, px, y - 3, px, y + 3, INK, 0.6)
        txt(c, px, y - 12, str(lo + i).replace("-", "\u2212"), 6.2, "Inter", INK, "center")
    from collections import Counter
    cnt = Counter(values)
    for v, k in sorted(cnt.items()):
        px = x + (v - lo) * step
        for j in range(k):
            c.saveState()
            c.setFillColor(SAGE if j % 2 == 0 else spec.GREEN)
            c.circle(px, y + 7 + j * 8.4, 3.0, stroke=0, fill=1)
            c.restoreState()


def function_machine(c, x, y, w, h, rule="\u00d7 3 + 1", ins=("2", "5", "10"), outs=None):
    bw = w * 0.42
    bx = x + (w - bw) / 2
    box(c, bx, y + h * 0.28, bw, h * 0.44, fill=spec.MIST, stroke=GREEN)
    txt(c, bx + bw / 2, y + h * 0.47, rule, 10.0, "SourceSerif", GREEN, "center")
    txt(c, bx + bw / 2, y + h * 0.34, "INPUT \u2192 RULE \u2192 OUTPUT", 5.8, "Inter",
        spec.GOLD_DEEP, "center")
    step = w / (len(ins) + 1)
    for i, v in enumerate(ins):
        cx = x + (i + 1) * step
        arrow(c, cx, y + h * 0.86, cx, y + h * 0.74, GOLD, 0.8)
        txt(c, cx, y + h * 0.90, v, 8.4, "SourceSerif-Semi", INK, "center")
        if outs:
            arrow(c, cx, y + h * 0.26, cx, y + h * 0.14, GOLD, 0.8)
            txt(c, cx, y + h * 0.02, outs[i], 8.4, "SourceSerif-Semi", TERRA, "center")


def balance(c, x, y, w, h, left="3x + 2", right="11", left_w=0.52, right_w=0.30):
    cx = x + w / 2
    pivot = y + h * 0.62
    line(c, cx, y, cx, pivot, GREEN, 1.4)
    line(c, cx - 26, y, cx + 26, y, GREEN, 1.4)
    line(c, cx - w * 0.42, pivot, cx + w * 0.42, pivot, GREEN, 1.4)
    c.saveState()
    c.setFillColor(GREEN)
    c.circle(cx, pivot, 2.4, stroke=0, fill=1)
    c.restoreState()
    # pans
    for side, lab, ww in ((-1, left, left_w), (1, right, right_w)):
        px = cx + side * w * 0.30
        line(c, px, pivot, px, pivot - 16, RULE, 0.7)
        box(c, px - w * 0.11, pivot - 34, w * 0.22, 18, fill=CREAM, stroke=GOLD, lw=0.6)
        txt(c, px, pivot - 29, lab, 9.0, "SourceSerif", INK, "center")


def net_cube(c, x, y, w, h, labels=True):
    s = min(w / 4, h / 3)
    ox = x + (w - 4 * s) / 2
    oy = y + (h - 3 * s) / 2
    faces = [(1, 2), (0, 1), (1, 1), (2, 1), (3, 1), (1, 0)]
    names = ["4 cm", "6 cm", "6 cm", "6 cm", "4 cm", "6 cm"]
    for i, (cx, cy) in enumerate(faces):
        box(c, ox + cx * s, oy + cy * s, s, s, fill=CREAM if i % 2 == 0 else spec.MIST,
            stroke=GREEN, lw=0.6)


def circle_parts(c, cx, cy, r, show_radius=True, show_circumference=True):
    c.saveState()
    c.setStrokeColor(GREEN)
    c.setLineWidth(1.1)
    c.circle(cx, cy, r, stroke=1, fill=0)
    c.restoreState()
    if show_radius:
        line(c, cx, cy, cx + r * math.cos(math.radians(35)), cy + r * math.sin(math.radians(35)),
             TERRA, 0.9)
        txt(c, cx + r * 0.55, cy + r * 0.30, "r", 8.0, "SourceSerifItalic", TERRA)
        c.saveState()
        c.setFillColor(TERRA)
        c.circle(cx, cy, 1.7, stroke=0, fill=1)
        c.restoreState()
    if show_circumference:
        c.saveState()
        c.setStrokeColor(GOLD)
        c.setLineWidth(0.8)
        c.setDash(2.4, 3)
        c.circle(cx, cy, r + 4, stroke=1, fill=0)
        c.restoreState()


def angle_diagram(c, x, y, w, h, deg=120, label="120\u00b0"):
    ox, oy = x + w * 0.16, y + h * 0.22
    a = math.radians(deg)
    line(c, ox, oy, ox + w * 0.74, oy, GREEN, 1.1)
    line(c, ox, oy, ox + w * 0.72 * math.cos(a), oy + h * 0.72 * math.sin(a), GREEN, 1.1)
    rr = min(w, h) * 0.22
    c.saveState()
    c.setStrokeColor(TERRA)
    c.setLineWidth(0.8)
    c.arc(ox - rr, oy - rr, ox + rr, oy + rr, 0, deg)
    c.restoreState()
    txt(c, ox + rr * 1.25, oy + rr * 0.36, label, 7.6, "SourceSerifItalic", TERRA)


def coordinate_grid(c, x, y, w, h, points=(), xmax=6, ymax=5, labels=True):
    sx, sy = w / (xmax + 1), h / (ymax + 1)
    for i in range(xmax + 1):
        line(c, x + i * sx, y, x + i * sx, y + ymax * sy, spec.RULE_SOFT, 0.4)
    for j in range(ymax + 1):
        line(c, x, y + j * sy, x + xmax * sx, y + j * sy, spec.RULE_SOFT, 0.4)
    arrow(c, x, y, x + xmax * sx + 6, y, INK, 0.8)
    arrow(c, x, y, x, y + ymax * sy + 6, INK, 0.8)
    for (px, py) in points:
        c.saveState()
        c.setFillColor(TERRA)
        c.circle(x + px * sx, y + py * sy, 3.0, stroke=0, fill=1)
        c.restoreState()


def factor_arrays(c, x, y, w, h, n=12):
    """Rectangular arrays showing factor pairs of n."""
    pairs = [(i, n // i) for i in range(1, n + 1) if n % i == 0 and i <= n // i]
    cols = len(pairs)
    cw = w / max(3, cols)
    for k, (a, b) in enumerate(pairs):
        ox = x + k * cw
        s = min(cw * 0.8 / b, (h * 0.72) / a)
        for i in range(a):
            for j in range(b):
                box(c, ox + j * s, y + h * 0.22 + i * s, s, s, fill=None, stroke=SAGE, lw=0.45)
        txt(c, ox + b * s / 2, y + h * 0.06, f"{a} \u00d7 {b}", 6.8, "Inter", GOLD_D, "center")


def sieve_grid(c, x, y, w, h, n=50, primes=None):
    if primes is None:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
    cols = 10
    rows = (n + cols - 1) // cols
    s = min(w / cols, h / rows)
    for k in range(1, n + 1):
        r, q = divmod(k - 1, cols)
        xx, yy = x + q * s, y + (rows - 1 - r) * s
        if k in primes:
            box(c, xx, yy, s, s, fill=spec.MIST, stroke=SAGE, lw=0.5)
            txt(c, xx + s / 2, yy + s * 0.30, str(k), 6.4, "Inter-Semi", SAGE, "center")
        else:
            box(c, xx, yy, s, s, fill=None, stroke=spec.RULE_SOFT, lw=0.35)
            txt(c, xx + s / 2, yy + s * 0.30, str(k), 6.2, "Inter", spec.INK_MUTE, "center")


def factor_tree(c, x, y, w, h, root=60):
    cx, top = x + w / 2, y + h
    nodes = {root: (cx, top - 8)}
    left = {"60": (36, 24), "36": (24, 12)}
    line(c, cx, top - 16, cx - w * 0.22, top - h * 0.55, RULE, 0.8)
    line(c, cx, top - 16, cx + w * 0.22, top - h * 0.55, RULE, 0.8)
    txt(c, cx, top - 12, "60", 10, "SourceSerif-Semi", GREEN, "center")
    txt(c, cx - w * 0.22, top - h * 0.62, "6", 10, "SourceSerif-Semi", GREEN, "center")
    txt(c, cx + w * 0.22, top - h * 0.62, "10", 10, "SourceSerif-Semi", GREEN, "center")
    for side, v in ((-1, "2"), (1, "2")):
        line(c, cx + side * w * 0.22, top - h * 0.68,
             cx + side * w * 0.33, top - h * 0.92, RULE, 0.8)
        txt(c, cx + side * w * 0.33, top - h * 0.99, v, 10, "SourceSerif-Semi", TERRA, "center")
    line(c, cx - w * 0.10, top - h * 0.68, cx - w * 0.06, top - h * 0.92, RULE, 0.8)
    line(c, cx - w * 0.10, top - h * 0.68, cx - w * 0.20, top - h * 0.92, RULE, 0.8)
    txt(c, cx - w * 0.06, top - h * 0.99, "2", 10, "SourceSerif-Semi", TERRA, "center")
    txt(c, cx - w * 0.20, top - h * 0.99, "3", 10, "SourceSerif-Semi", TERRA, "center")
    txt(c, cx - w * 0.22, top - h * 0.74, "6", 10, "SourceSerif-Semi", GREEN, "center")


# ---------------------------------------------------------------- ch2 diagrams
def power_stack(c, x, y, w, h, base=3, exp=4):
    n = exp
    bw = min(w * 0.16, h * 0.62)
    gap_ = (w - n * bw) / (n + 1)
    for i in range(n):
        bx = x + gap_ + i * (bw + gap_)
        box(c, bx, y + 12, bw, h * 0.52, fill=spec.SAND if i % 2 == 0 else CREAM,
            stroke=GOLD_D, lw=0.6)
        txt(c, bx + bw / 2, y + 12 + h * 0.20, str(base), 13, "Playfair", GREEN, "center")
        if i < n - 1:
            txt(c, bx + bw + gap_ / 2 + 1, y + 12 + h * 0.20, "\u00d7", 8, "SourceSerif",
                TERRA, "center")
    txt(c, x + w / 2, y + h * 0.80, f"{base}^{n} means {n} factors of {base}",
        6.8, "Inter", spec.INK_MUTE, "center")
    txt(c, x + w / 2, y + 2, f"{base} \u00d7 {base} \u00d7 {base} \u00d7 {base} = "
        f"{base ** n}", 8.2, "SourceSerif-Semi", GREEN, "center")


def powers_of_ten_ladder(c, x, y, w, h):
    steps = ["10^{4}", "10^{3}", "10^{2}", "10^{1}", "10^{0}", "10^{\u22121}",
             "10^{\u22122}"]
    vals = ["10 000", "1 000", "100", "10", "1", "0.1", "0.01"]
    n = len(steps)
    cw = w / n
    for i, (s, v) in enumerate(zip(steps, vals)):
        cx = x + i * cw
        shade = spec.MIST if i < 5 else spec.SAND
        box(c, cx + 2, y + h * 0.30, cw - 4, h * 0.52, fill=shade, stroke=RULE, lw=0.45)
        txt(c, cx + cw / 2, y + h * 0.60, s.replace("^{", "").replace("}", ""), 7.6,
            "SourceSerif", GREEN, "center")
        txt(c, cx + cw / 2, y + h * 0.40, v, 6.8, "Inter", INK, "center")
    arrow(c, x + 2, y + h * 0.18, x + w - 2, y + h * 0.18, GOLD_D, 0.7)
    txt(c, x + 4, y + h * 0.05, "\u00f7 10 at every step to the right", 6.2, "Inter",
        spec.INK_MUTE)
    txt(c, x + w - 4, y + h * 0.05, "\u00d7 10 at every step to the left", 6.2, "Inter",
        spec.INK_MUTE, "right")


def squares_and_cubes(c, x, y, w, h):
    # 4x4 square of counters
    s = min(w * 0.13, h * 0.16)
    ox, oy = x + w * 0.06, y + h * 0.30
    for i in range(4):
        for j in range(4):
            box(c, ox + j * s, oy + i * s, s * 0.92, s * 0.92,
                fill=spec.MIST if (i + j) % 2 == 0 else None, stroke=SAGE, lw=0.45)
    txt(c, ox + 2 * s, oy - 12, "4^{2} = 16", 8.0, "SourceSerif-Semi", SAGE, "center")
    txt(c, ox + 2 * s, oy - 24, "a square of 16 counters", 6.2, "Inter", spec.INK_MUTE,
        "center")
    # 3x3x3 cube stack (front, top, side)
    u = s * 0.86
    bx, by = x + w * 0.44, y + h * 0.20
    dx, dy = u * 2.6, u * 2.0
    for layer in range(3):
        for col in range(3):
            px = bx + col * u
            py = by + layer * u
            box(c, px, py, u * 0.96, u * 0.96, fill=CREAM if layer % 2 == 0 else spec.SAND,
                stroke=GOLD_D, lw=0.5)
    # simple 3D suggestion
    p = c.beginPath()
    p.moveTo(bx, by + 3 * u); p.lineTo(bx + dx, by + 3 * u + dy)
    p.lineTo(bx + 3 * u + dx, by + 3 * u + dy); p.lineTo(bx + 3 * u, by + 3 * u)
    c.saveState(); c.setStrokeColor(GOLD_D); c.setLineWidth(0.6)
    c.setFillColor(spec.MIST); c.drawPath(p, stroke=1, fill=1); c.restoreState()
    p = c.beginPath()
    p.moveTo(bx + 3 * u, by); p.lineTo(bx + 3 * u + dx, by + dy)
    p.lineTo(bx + 3 * u + dx, by + 3 * u + dy); p.lineTo(bx + 3 * u, by + 3 * u)
    c.saveState(); c.setStrokeColor(GOLD_D); c.setLineWidth(0.6)
    c.setFillColor(spec.BLUSH); c.drawPath(p, stroke=1, fill=1); c.restoreState()
    txt(c, bx + 3 * u + dx / 2, by - 12, "3^{3} = 27", 8.0, "SourceSerif-Semi", TERRA,
        "center")
    txt(c, bx + 3 * u + dx / 2, by - 24, "a cube of 27 small cubes", 6.2, "Inter",
        spec.INK_MUTE, "center")
    txt(c, x + w * 0.78, y + h * 0.52, "Square numbers count", 6.8, "Inter", spec.INK_MUTE)
    txt(c, x + w * 0.78, y + h * 0.44, "a flat square.", 6.8, "Inter", spec.INK_MUTE)
    txt(c, x + w * 0.78, y + h * 0.32, "Cube numbers count", 6.8, "Inter", spec.INK_MUTE)
    txt(c, x + w * 0.78, y + h * 0.24, "a solid cube.", 6.8, "Inter", spec.INK_MUTE)


# ---------------------------------------------------------------- ch3 diagrams
def factor_pairs(c, x, y, w, h, n=36):
    pairs = [(i, n // i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
    cols = len(pairs)
    cw = w / cols
    for k, (a, b) in enumerate(pairs):
        ox = x + k * cw + 6
        s = min((cw - 16) / 6, (h * 0.55) / 6)
        for i in range(a):
            for j in range(b):
                box(c, ox + j * s, y + h * 0.30 + i * s, s, s, fill=None, stroke=SAGE,
                    lw=0.4)
        txt(c, ox + b * s / 2, y + h * 0.14, f"{a} \u00d7 {b}", 7.0, "Inter", GOLD_D,
            "center")


def divisibility_rules(c, x, y, w, h):
    rows = [("2", "last digit is even"), ("3", "digit sum is a multiple of 3"),
            ("4", "last two digits form a multiple of 4"),
            ("5", "last digit is 0 or 5"), ("6", "divisible by 2 and by 3"),
            ("9", "digit sum is a multiple of 9"),
            ("10", "last digit is 0")]
    rh = h / len(rows)
    for i, (d, rule) in enumerate(rows):
        yy = y + h - (i + 1) * rh
        if i % 2 == 0:
            box(c, x, yy, w, rh, fill=CREAM, stroke=None)
        typeset_num = d
        txt(c, x + 12, yy + rh * 0.32, typeset_num, 8.6, "SourceSerif-Semi", TERRA,
            "center")
        txt(c, x + 30, yy + rh * 0.32, rule, 7.0, "Inter", INK)


def prime_sieve(c, x, y, w, h, n=60):
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59}
    cols = 10
    rows = (n + cols - 1) // cols
    s = min(w / cols, h / rows)
    for k in range(1, n + 1):
        r, q = divmod(k - 1, cols)
        xx, yy = x + q * s, y + (rows - 1 - r) * s
        if k in primes:
            box(c, xx, yy, s, s, fill=spec.MIST, stroke=SAGE, lw=0.5)
            txt(c, xx + s / 2, yy + s * 0.30, str(k), 6.2, "Inter-Semi", SAGE, "center")
        else:
            box(c, xx, yy, s, s, fill=None, stroke=spec.RULE_SOFT, lw=0.3)
            txt(c, xx + s / 2, yy + s * 0.30, str(k), 6.0, "Inter", spec.INK_MUTE,
                "center")


def hcf_lcm(c, x, y, w, h, a=12, b=18):
    def factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]
    fa, fb = factors(a), factors(b)
    r = min(w * 0.20, h * 0.24)
    c1 = (x + w * 0.32, y + h * 0.56)
    c2 = (x + w * 0.62, y + h * 0.56)
    c.saveState()
    c.setStrokeColor(SAGE); c.setLineWidth(0.8)
    c.setFillColor(spec.MIST)
    try: c.setFillAlpha(0.6)
    except Exception: pass
    c.circle(c1[0], c1[1], r, stroke=1, fill=1)
    c.setFillColor(spec.SAND)
    c.circle(c2[0], c2[1], r, stroke=1, fill=1)
    c.restoreState()
    txt(c, c1[0] - r * 0.62, c1[1], ", ".join(str(v) for v in fa if v not in fb), 6.4,
        "Inter", SAGE, "center")
    txt(c, c2[0] + r * 0.62, c2[1], ", ".join(str(v) for v in fb if v not in fa), 6.4,
        "Inter", TERRA, "center")
    txt(c, (c1[0] + c2[0]) / 2, c1[1], ", ".join(str(v) for v in fa if v in fb), 6.4,
        "Inter-Semi", GOLD_D, "center")
    txt(c, (c1[0] + c2[0]) / 2, y + h * 0.14, f"HCF({a}, {b}) = {max(set(fa) & set(fb))}",
        7.4, "SourceSerif-Semi", GREEN, "center")


# ---------------------------------------------------------------- ch4 diagrams
def fraction_bars(c, x, y, w, h, rows=None):
    rows = rows or [(2, 1, "1/2"), (4, 2, "2/4"), (8, 4, "4/8")]
    rh = h / len(rows)
    for i, (n, sh, lab) in enumerate(rows):
        yy = y + h - (i + 1) * rh + rh * 0.18
        hh = rh * 0.62
        for k in range(n):
            sw = (w * 0.80) / n
            box(c, x + k * sw, yy, sw, hh, fill=SAGE if k < sh else None,
                stroke=GREEN if k < sh else RULE, lw=0.45)
        txt(c, x + w * 0.82, yy + hh * 0.28, lab if lab else "", 7.2, "SourceSerif",
            spec.INK_SOFT)


def decimal_grid(c, x, y, w, h, shaded=37):
    s = min(w, h) / 10
    for r in range(10):
        for q in range(10):
            n = r * 10 + q
            box(c, x + q * s, y + (9 - r) * s, s, s,
                fill=SAGE if n < shaded else None, stroke=RULE, lw=0.35)


def fraction_ops(c, x, y, w, h):
    txt(c, x, y + h * 0.78, "1/2 + 1/3", 9.0, "SourceSerif-Semi", GREEN)
    txt(c, x, y + h * 0.60, "= 3/6 + 2/6", 9.0, "SourceSerif", INK)
    txt(c, x, y + h * 0.40, "= 5/6", 9.0, "SourceSerif-Semi", TERRA)


# ---------------------------------------------------------------- ch5 diagrams
def percent_bar(c, x, y, w, h, pct=35):
    box(c, x, y, w, h, fill=None, stroke=RULE, lw=0.6)
    box(c, x, y, w * pct / 100, h, fill=SAGE, stroke=None)
    for i in range(1, 10):
        line(c, x + w * i / 10, y, x + w * i / 10, y + h, spec.PAPER, 0.6)
    txt(c, x + w * pct / 200, y + h * 0.32, f"{pct} %", 8.0, "Inter-Semi", spec.PAPER,
        "center")
    txt(c, x + w / 2, y - 11, f"{100 - pct} % remains", 6.6, "Inter", spec.INK_MUTE,
        "center")


def price_tag(c, x, y, w, h, before=80, after=60):
    box(c, x + w * 0.18, y + h * 0.12, w * 0.64, h * 0.74, fill=CREAM, stroke=GOLD_D,
        lw=0.7)
    txt(c, x + w * 0.5, y + h * 0.60, f"{before}", 12, "SourceSerif-Semi",
        spec.INK_MUTE, "center")
    line(c, x + w * 0.40, y + h * 0.66, x + w * 0.60, y + h * 0.66, TERRA, 0.9)
    txt(c, x + w * 0.5, y + h * 0.32, f"{after}", 14, "SourceSerif-Semi", GREEN, "center")
    txt(c, x + w * 0.5, y + h * 0.18, "reduced by 25 %", 6.4, "Inter", GOLD_D, "center")


def factor_tree_full(c, x, y, w, h, n=60):
    def tree(ox, root, split, col):
        cx, top = ox, y + h - 8
        txt(c, cx, top - 4, str(root), 9.6, "SourceSerif-Semi", col, "center")
        if root in (2, 3, 5, 7):
            return
        a, b = split
        yy = top - h * 0.42
        line(c, cx, top - 10, cx - w * 0.075, yy + 10, RULE, 0.8)
        line(c, cx, top - 10, cx + w * 0.075, yy + 10, RULE, 0.8)
        txt(c, cx - w * 0.075, yy + 2, str(a), 9.6, "SourceSerif-Semi", col, "center")
        txt(c, cx + w * 0.075, yy + 2, str(b), 9.6, "SourceSerif-Semi", col, "center")
        # one level deeper for composites
        for dx, val in ((-w * 0.075, a), (w * 0.075, b)):
            if val in (2, 3, 5, 7):
                continue
            pair = {4: (2, 2), 6: (2, 3), 10: (2, 5), 12: (3, 4), 15: (3, 5),
                    9: (3, 3), 18: (3, 6), 30: (5, 6)}.get(val)
            if not pair:
                continue
            y2 = yy - h * 0.36
            line(c, cx + dx, yy - 6, cx + dx - w * 0.045, y2 + 8, RULE, 0.7)
            line(c, cx + dx, yy - 6, cx + dx + w * 0.045, y2 + 8, RULE, 0.7)
            txt(c, cx + dx - w * 0.045, y2, str(pair[0]), 9.0, "SourceSerif-Semi", TERRA,
                "center")
            txt(c, cx + dx + w * 0.045, y2, str(pair[1]), 9.0, "SourceSerif-Semi", TERRA,
                "center")
    tree(x + w * 0.24, 60, (6, 10), GREEN)
    tree(x + w * 0.72, 60, (12, 5), GREEN)
    txt(c, x, y + 4, "two routes, one result:  60 = 2 \u00d7 2 \u00d7 3 \u00d7 5",
        7.0, "Inter", GOLD_D)


# ---------------------------------------------------------------- ch4 extra
def fraction_strips_full(c, x, y, w, h):
    return fraction_bars(c, x + w * 0.04, y, w * 0.86, h,
                         rows=[(2, 1, "1/2"), (4, 2, "2/4"), (8, 4, "4/8"),
                               (16, 8, "8/16")])


def fraction_addition(c, x, y, w, h):
    # two strips of 6, aligned
    n = 6
    sw = (w * 0.82) / n
    for row, shade, lab in ((1, 3, "1/2 = 3/6"), (0, 2, "1/3 = 2/6")):
        yy = y + h * (0.46 if row == 1 else 0.12)
        for k in range(n):
            box(c, x + k * sw, yy, sw, h * 0.30, fill=SAGE if k < shade else None,
                stroke=GREEN if k < shade else RULE, lw=0.45)
        txt(c, x + w * 0.86, yy + h * 0.10, lab, 7.0, "SourceSerif", spec.INK_SOFT)
    # total strip
    yy = y + h * 0.46 - h * 0.40
    for k in range(n):
        fill = TERRA if k < 2 else (SAGE if k < 5 else None)
        box(c, x + k * sw, yy, sw, h * 0.30, fill=fill, stroke=GREEN if fill else RULE,
            lw=0.45)
    txt(c, x + w * 0.86, yy + h * 0.10, "5/6", 7.0, "SourceSerif-Semi", GREEN)
    txt(c, x + 2, yy - 10, "sum: 3/6 + 2/6 = 5/6", 6.6, "Inter", spec.INK_MUTE)


def fraction_multiplication(c, x, y, w, h):
    s = min(w * 0.5 / 3, h / 2)
    # a half, split into thirds
    ox, oy = x + w * 0.06, y + h * 0.30
    for i in range(2):
        for j in range(3):
            shaded = (i == 0 and j == 0)
            box(c, ox + j * s, oy + i * s, s, s,
                fill=TERRA if shaded else None, stroke=GREEN if shaded else RULE, lw=0.5)
    txt(c, ox + 1.5 * s, oy - 12, "1/3 of the shaded half = 1/6", 6.8, "Inter", spec.INK_MUTE,
        "center")
    # the general grid
    ox2 = x + w * 0.52
    for i in range(3):
        for j in range(4):
            shaded = (i < 1 and j < 3)
            box(c, ox2 + j * s, oy + i * s, s, s,
                fill=SAGE if shaded else None, stroke=GREEN if shaded else RULE, lw=0.5)
    txt(c, ox2 + 2 * s, oy - 12, "3/4 \u00d7 1/3 = 3/12 = 1/4", 6.8, "Inter",
        spec.INK_MUTE, "center")


def decimal_grid_shaded(c, x, y, w, h):
    s = min(w * 0.30, h * 0.9) * 0.9
    return decimal_grid(c, x + w * 0.06, y + h * 0.05, s, s * 0.9, shaded=37)


# ---------------------------------------------------------------- ch5 extra
def percent_hundred(c, x, y, w, h, pct=35):
    s = min(w * 0.34, h * 0.92) / 10
    ox, oy = x + w * 0.04, y + h * 0.04
    for r in range(10):
        for q in range(10):
            n = r * 10 + q
            box(c, ox + q * s, oy + (9 - r) * s, s, s,
                fill=SAGE if n < pct else None, stroke=RULE, lw=0.3)
    # annotations
    ax = x + w * 0.46
    txt(c, ax, y + h * 0.74, "35 cells shaded out of 100", 7.4, "Inter", INK)
    for i, (lab, val) in enumerate((("fraction", "35/100"), ("decimal", "0.35"),
                                    ("percentage", "35 %"))):
        yy = y + h * 0.56 - i * 15
        txt(c, ax, yy, lab, 6.6, "Inter", spec.INK_MUTE)
        txt(c, ax + 62, yy, val, 8.4, "SourceSerif-Semi", GREEN)
    txt(c, ax, y + h * 0.04, "one region, three names", 6.4, "Inter", GOLD_D)


def percent_of_quantity(c, x, y, w, h):
    line(c, x + 6, y + h * 0.40, x + w - 6, y + h * 0.40, RULE, 0.8)
    marks = [("0", 0.0), ("10 %", 0.10), ("15 %", 0.15), ("100 %", 1.0)]
    for lab, frac in marks:
        px = x + 6 + frac * (w - 12)
        line(c, px, y + h * 0.33, px, y + h * 0.47, INK, 0.7)
        txt(c, px, y + h * 0.16, lab, 6.4, "Inter", INK, "center")
    txt(c, x + 6 + 0.10 * (w - 12), y + h * 0.58, "26", 7.4, "SourceSerif-Semi", SAGE,
        "center")
    txt(c, x + 6 + 0.15 * (w - 12), y + h * 0.58, "39", 7.4, "SourceSerif-Semi", TERRA,
        "center")
    txt(c, x + w - 6, y + h * 0.58, "260", 7.4, "SourceSerif-Semi", GREEN, "center")
    txt(c, x + 6 + 0.10 * (w - 12), y + h * 0.80, "10 % = 26", 6.4, "Inter",
        spec.INK_MUTE, "center")
    txt(c, x + 6 + 0.15 * (w - 12), y + h * 0.70, "15 % = 26 + 13 = 39", 6.4, "Inter",
        spec.INK_MUTE, "center")


# ---------------------------------------------------------------- ch6 extra
def linear_sequence(c, x, y, w, h, start=3, diff=2, n=6):
    sx = (w * 0.86) / n
    base = y + h * 0.18
    for i in range(n):
        v = start + i * diff
        bh = (h * 0.62) * v / (start + (n - 1) * diff)
        box(c, x + 12 + i * sx, base, sx * 0.34, bh, fill=SAGE if i % 2 == 0 else spec.GREEN,
            stroke=None)
        txt(c, x + 12 + i * sx + sx * 0.17, base + bh + 4, str(v), 7.0, "Inter-Semi",
            INK, "center")
        txt(c, x + 12 + i * sx + sx * 0.17, base - 10, f"n={i + 1}", 6.0, "Inter",
            spec.INK_MUTE, "center")
    line(c, x + 12, base, x + w * 0.92, base, INK, 0.7)
    txt(c, x + w * 0.94, y + h * 0.60, f"+{diff}", 7.4, "SourceSerif-Semi", TERRA)
    txt(c, x + w * 0.94, y + h * 0.50, "each step", 6.2, "Inter", spec.INK_MUTE)
    txt(c, x + w * 0.94, y + h * 0.34, f"nth term", 6.2, "Inter", spec.INK_MUTE)
    txt(c, x + w * 0.94, y + h * 0.24, f"{diff}n + {start - diff}", 7.4, "SourceSerif-Semi",
        GREEN)


def balance_scale(c, x, y, w, h):
    cx = x + w / 2
    pivot = y + h * 0.62
    line(c, cx, y + h * 0.10, cx, pivot, GREEN, 1.4)
    line(c, cx - w * 0.05, y + h * 0.10, cx + w * 0.05, y + h * 0.10, GREEN, 1.4)
    line(c, cx - w * 0.34, pivot, cx + w * 0.34, pivot, GREEN, 1.6)
    c.saveState(); c.setFillColor(GREEN); c.circle(cx, pivot, 2.6, stroke=0, fill=1)
    c.restoreState()
    for side, lab, sub in ((-1, "3x + 2", "left side"), (1, "11", "right side")):
        px = cx + side * w * 0.24
        line(c, px, pivot, px, pivot - 14, RULE, 0.8)
        box(c, px - w * 0.10, pivot - 32, w * 0.20, 16, fill=CREAM, stroke=GOLD, lw=0.6)
        txt(c, px, pivot - 27.5, lab, 8.6, "SourceSerif-Semi", INK, "center")
        txt(c, px, pivot - 44, sub, 6.0, "Inter", spec.INK_MUTE, "center")
    txt(c, cx, y + h * 0.82, "the same operation on both sides keeps the balance", 6.4,
        "Inter", GOLD_D, "center")


def matchstick_chain(c, x, y, w, h, squares=4):
    s = min((w * 0.8) / squares, h * 0.62)
    ox, oy = x + (w - squares * s) / 2, y + h * 0.22
    for i in range(squares + 1):
        line(c, ox + i * s, oy, ox + i * s, oy + s, SAGE, 2.0)
    line(c, ox, oy, ox + squares * s, oy, SAGE, 2.0)
    line(c, ox, oy + s, ox + squares * s, oy + s, SAGE, 2.0)
    # highlight shared sides
    for i in range(1, squares):
        line(c, ox + i * s, oy, ox + i * s, oy + s, TERRA, 2.6)
    txt(c, ox + s * 0.5, oy - 10, "4", 7.4, "Inter-Semi", GOLD_D, "center")
    txt(c, ox + s * 1.5, oy - 10, "7", 7.4, "Inter-Semi", GOLD_D, "center")
    txt(c, ox + s * 2.5, oy - 10, "10", 7.4, "Inter-Semi", GOLD_D, "center")
    txt(c, ox + s * 3.5, oy - 10, "13", 7.4, "Inter-Semi", GOLD_D, "center")
    txt(c, ox + squares * s + 8, oy + s * 0.4, "shared sides", 6.2, "Inter", TERRA)


# ------------------------------------------------------- chapter 7 geometry set
def _arc(c, cx, cy, r, a1, a2, col=TERRA, lw=0.7, dash=None):
    c.saveState()
    c.setStrokeColor(col)
    c.setLineWidth(lw)
    if dash:
        c.setDash(dash)
    c.arc(cx - r, cy - r, cx + r, cy + r, startAng=a1, extent=a2 - a1)
    c.restoreState()


def _sector(c, cx, cy, r, a1, a2, fill=None, stroke=None, lw=0.6):
    n = max(8, int(abs(a2 - a1) / 4))
    c.saveState()
    p = c.beginPath()
    p.moveTo(cx, cy)
    for i in range(n + 1):
        a = math.radians(a1 + (a2 - a1) * i / n)
        p.lineTo(cx + r * math.cos(a), cy + r * math.sin(a))
    p.close()
    if fill is not None:
        c.setFillColor(fill)
    if stroke is not None:
        c.setStrokeColor(stroke)
        c.setLineWidth(lw)
    c.drawPath(p, stroke=1 if stroke else 0, fill=1 if fill else 0)
    c.restoreState()


def _poly(c, pts, fill=spec.CREAM_SOFT, stroke=GREEN, lw=1.1):
    c.saveState()
    c.setStrokeColor(stroke)
    c.setLineWidth(lw)
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    p.close()
    if fill is not None:
        c.setFillColor(fill)
    c.drawPath(p, stroke=1, fill=1 if fill is not None else 0)
    c.restoreState()


def dot(c, x, y, r=1.5, col=INK):
    c.saveState()
    c.setFillColor(col)
    c.circle(x, y, r, stroke=0, fill=1)
    c.restoreState()


def _chevron(c, x, y, col=SAGE, size=4.2):
    for k in (0, 1):
        ox = x + k * size * 0.9
        line(c, ox, y - size, ox + size * 0.6, y, col, 0.8)
        line(c, ox + size * 0.6, y, ox, y + size, col, 0.8)


def angle_types(c, x, y, w, h):
    kinds = [("acute", 42, "40\u00b0"), ("right", 90, "90\u00b0"),
             ("obtuse", 132, "130\u00b0"), ("straight", 180, "180\u00b0"),
             ("reflex", 288, "288\u00b0")]
    cw = w / 5.0
    r = min(cw * 0.30, h * 0.34)
    cy = y + h * 0.56
    for i, (name, deg, lab) in enumerate(kinds):
        cx = x + cw * (i + 0.26)
        a = math.radians(deg)
        line(c, cx, cy, cx + r * 1.4, cy, INK, 0.9)
        line(c, cx, cy, cx + r * 1.4 * math.cos(a), cy + r * 1.4 * math.sin(a), INK, 0.9)
        if deg > 180:
            _sector(c, cx, cy, r * 0.58, 0, deg, fill=spec.MIST, stroke=TERRA, lw=0.5)
        elif deg == 90:
            box(c, cx, cy, r * 0.34, r * 0.34, fill=None, stroke=TERRA, lw=0.7)
        else:
            _arc(c, cx, cy, r * 0.52, 0, deg, TERRA, 0.8)
        txt(c, cx + r * 0.62, y + h * 0.17, name, 6.4, "Inter", INK, "center")
        txt(c, cx + r * 0.62, y + h * 0.05, lab, 6.6, "SourceSerifItalic", GOLD_D, "center")


def parallel_lines(c, x, y, w, h):
    y1, y2 = y + h * 0.30, y + h * 0.72
    line(c, x + 12, y1, x + w - 12, y1, GREEN, 1.0)
    line(c, x + 12, y2, x + w - 12, y2, GREEN, 1.0)
    _chevron(c, x + w - 46, y1, SAGE)
    _chevron(c, x + w - 46, y2, SAGE)
    tx, bx = x + w * 0.30, x + w * 0.58
    line(c, tx, y - 4, bx, y + h + 4, INK, 0.9)
    # alternate pair, highlighted
    _sector(c, tx, y1, 15, 204, 250, fill=spec.MIST, stroke=TERRA, lw=0.5)
    _sector(c, bx, y2, 15, 24, 70, fill=spec.MIST, stroke=TERRA, lw=0.5)
    txt(c, tx - 30, y1 + 2, "alternate", 6.2, "Inter-Semi", TERRA)
    txt(c, bx + 18, y2 - 2, "alternate", 6.2, "Inter-Semi", TERRA)
    # co-interior pair
    _sector(c, tx, y1, 17, 30, 76, fill=spec.CREAM_SOFT, stroke=SAGE, lw=0.5)
    _sector(c, bx, y2, 17, 30, 76, fill=spec.CREAM_SOFT, stroke=SAGE, lw=0.5)
    txt(c, tx + 20, y1 + 12, "co-interior", 6.2, "Inter-Semi", SAGE)
    txt(c, bx + 20, y2 + 12, "co-interior", 6.2, "Inter-Semi", SAGE)
    txt(c, x + 12, y + 3, "the two marked co-interior angles add to 180\u00b0", 6.4,
        "Inter", INK)


def triangle_tear(c, x, y, w, h):
    A = (x + w * 0.05, y + h * 0.16)
    B = (x + w * 0.34, y + h * 0.16)
    C = (x + w * 0.15, y + h * 0.76)
    _poly(c, [A, B, C])
    # corner sectors, coloured
    def ang(P, Q, R):
        a1 = math.degrees(math.atan2(Q[1] - P[1], Q[0] - P[0]))
        a2 = math.degrees(math.atan2(R[1] - P[1], R[0] - P[0]))
        d = (a2 - a1) % 360
        return a1, d
    for P, Q, R, col in ((A, B, C, SAGE), (B, C, A, TERRA), (C, A, B, GOLD_D)):
        a1, d = ang(P, Q, R)
        _sector(c, P[0], P[1], 13, a1, a1 + d, fill=spec.CREAM_SOFT, stroke=col, lw=0.6)
    txt(c, A[0] - 4, A[1] - 11, "A", 7.2, "SourceSerifItalic", INK)
    txt(c, B[0] + 4, B[1] - 11, "B", 7.2, "SourceSerifItalic", INK)
    txt(c, C[0] - 2, C[1] + 6, "C", 7.2, "SourceSerifItalic", INK)
    # arrow
    arrow(c, x + w * 0.40, y + h * 0.46, x + w * 0.50, y + h * 0.46, GOLD_D, 0.9)
    # assembled angles on a straight line
    P = (x + w * 0.55, y + h * 0.34)
    Rr = min(w * 0.20, h * 0.42)
    a1, dA = ang(A, B, C)
    b1, dB = ang(B, C, A)
    c1, dC = ang(C, A, B)
    start = 0.0
    for d, col, lab in ((dA, SAGE, "a"), (dB, TERRA, "b"), (dC, GOLD_D, "c")):
        _sector(c, P[0], P[1], Rr, start, start + d, fill=spec.CREAM_SOFT, stroke=col, lw=0.7)
        mid = math.radians(start + d / 2)
        txt(c, P[0] + Rr * 0.62 * math.cos(mid), P[1] + Rr * 0.62 * math.sin(mid),
            lab, 7.0, "SourceSerifItalic", col, "center")
        start += d
    line(c, P[0] - 6, P[1], P[0] + Rr + 8, P[1], INK, 0.9)
    txt(c, P[0] + Rr + 10, P[1] - 3, "straight line = 180\u00b0", 6.4, "Inter", INK)


def triangle_parallel_proof(c, x, y, w, h):
    A = (x + w * 0.13, y + h * 0.22)
    B = (x + w * 0.87, y + h * 0.22)
    C = (x + w * 0.42, y + h * 0.78)
    _poly(c, [A, B, C])
    # parallel through C
    line(c, x + w * 0.04, C[1], x + w * 0.96, C[1], GOLD_D, 0.9, dash=(3, 2))
    _chevron(c, x + w * 0.075, C[1] + 7, GOLD_D)
    _chevron(c, x + w * 0.075, A[1] - 15, GOLD_D)
    line(c, A[0], A[1], B[0], B[1], GREEN, 1.3)

    def ang(P, Q, R):
        a1 = math.degrees(math.atan2(Q[1] - P[1], Q[0] - P[0]))
        a2 = math.degrees(math.atan2(R[1] - P[1], R[0] - P[0]))
        return a1, (a2 - a1) % 360

    # apex: three sectors across the parallel line
    L = (C[0] - 1, C[1])
    a1, d1 = ang(C, L, A)
    _sector(c, C[0], C[1], 22, a1, a1 + d1, fill=spec.MIST, stroke=TERRA, lw=0.6)
    a2, d2 = ang(C, A, B)
    _sector(c, C[0], C[1], 30, a2, a2 + d2, fill=spec.CREAM_SOFT, stroke=SAGE, lw=0.6)
    a3, d3 = ang(C, B, L)
    _sector(c, C[0], C[1], 22, a3, a3 + d3, fill=spec.CREAM_SOFT, stroke=GOLD_D, lw=0.6)
    # base angle marks
    aA, dA = ang(A, B, C)
    _sector(c, A[0], A[1], 16, aA, aA + dA, fill=spec.MIST, stroke=TERRA, lw=0.6)
    aB, dB = ang(B, C, A)
    _sector(c, B[0], B[1], 16, aB, aB + dB, fill=spec.CREAM_SOFT, stroke=GOLD_D, lw=0.6)
    txt(c, C[0] - 34, C[1] + 12, "alternate", 6.2, "Inter-Semi", TERRA)
    txt(c, C[0] - 10, C[1] - 26, "co-interior", 6.2, "Inter-Semi", SAGE)
    txt(c, C[0] + 34, C[1] + 12, "alternate", 6.2, "Inter-Semi", GOLD_D)
    txt(c, A[0] + 26, A[1] + 12, "a", 7.2, "SourceSerifItalic", TERRA)
    txt(c, B[0] - 30, B[1] + 12, "b", 7.2, "SourceSerifItalic", GOLD_D)
    txt(c, x + w * 0.04, y + 2, "a + b + c = 180\u00b0, the angles of the triangle", 6.4,
        "Inter", INK)


def polygon_dissection(c, x, y, w, h):
    for i, n in enumerate((4, 5, 6)):
        cw = w / 3.0
        cx = x + cw * (i + 0.5)
        cy = y + h * 0.56
        r = min(cw * 0.30, h * 0.36)
        pts = []
        for k in range(n):
            a = math.radians(90 + 360.0 * k / n)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        _poly(c, pts)
        for k in range(2, n - 1):
            line(c, pts[0][0], pts[0][1], pts[k][0], pts[k][1], GOLD_D, 0.7,
                 dash=(2.5, 2))
        txt(c, cx, y + h * 0.16, "%d triangles" % (n - 2), 6.6, "Inter-Semi", GREEN,
            "center")
        txt(c, cx, y + h * 0.04, "= %d\u00b0" % ((n - 2) * 180), 7.0, "SourceSerifItalic",
            GOLD_D, "center")


def constructions(c, x, y, w, h):
    cw = w / 3.0
    tops = y + h * 0.80
    # ---- 1 perpendicular bisector
    ax, bx = x + cw * 0.18, x + cw * 0.72
    ay = by = y + h * 0.34
    line(c, ax, ay, bx, by, GREEN, 1.2)
    r = (bx - ax) * 0.78
    cy = (ay + by) / 2
    mx = (ax + bx) / 2
    _arc(c, ax, ay, r, 24, 156, TERRA, 0.7, dash=(2, 2))
    _arc(c, bx, by, r, 24, 156, TERRA, 0.7, dash=(2, 2))
    _arc(c, ax, ay, r, 204, 156, SAGE, 0.7, dash=(2, 2))
    _arc(c, bx, by, r, 204, 156, SAGE, 0.7, dash=(2, 2))
    top = ay + math.sqrt(max(r * r - (r * 0.5) ** 2, 1))
    line(c, mx, cy - h * 0.16, mx, top, INK, 0.9)
    dot(c, ax, ay); dot(c, bx, by)
    txt(c, ax - 6, ay - 11, "A", 7.0, "SourceSerifItalic")
    txt(c, bx + 2, by - 11, "B", 7.0, "SourceSerifItalic")
    txt(c, x + cw * 0.5, tops, "Perpendicular bisector", 6.8, "Inter-Semi", INK, "center")

    # ---- 2 angle bisector
    vx, vy = x + cw * 1.16, y + h * 0.30
    L = cw * 0.62
    a2 = 52
    line(c, vx, vy, vx + L, vy, GREEN, 1.2)
    line(c, vx, vy, vx + L * math.cos(math.radians(a2)),
         vy + L * math.sin(math.radians(a2)), GREEN, 1.2)
    rr = L * 0.52
    _arc(c, vx, vy, rr, 0, a2, TERRA, 0.7)
    p1 = (vx + rr, vy)
    p2 = (vx + rr * math.cos(math.radians(a2)), vy + rr * math.sin(math.radians(a2)))
    r2 = rr * 0.72
    _arc(c, p1[0], p1[1], r2, 100, 120, SAGE, 0.7, dash=(2, 2))
    _arc(c, p2[0], p2[1], r2, -70, 120, SAGE, 0.7, dash=(2, 2))
    mx2 = (p1[0] + p2[0]) / 2
    my2 = (p1[1] + p2[1]) / 2
    line(c, vx, vy, vx + (mx2 - vx) * 1.9, vy + (my2 - vy) * 1.9, INK, 0.9)
    dot(c, vx, vy); dot(c, p1[0], p1[1]); dot(c, p2[0], p2[1])
    txt(c, vx - 8, vy - 10, "V", 7.0, "SourceSerifItalic")
    txt(c, x + cw * 1.5, tops, "Angle bisector", 6.8, "Inter-Semi", INK, "center")

    # ---- 3 triangle from three sides
    bx3 = x + cw * 2.16
    px = (bx3 + x + cw * 2.80) / 2
    py = y + h * 0.30
    b = cw * 0.64
    line(c, px - b / 2, py, px + b / 2, py, GREEN, 1.2)
    s1, s2 = b * 0.66, b * 0.56
    dx = (s1 * s1 - s2 * s2) / (2 * b)
    hh = math.sqrt(max(s1 * s1 - (b / 2 + dx) ** 2, 1))
    apex = (px - b / 2 + b / 2 + dx, py + hh)
    _arc(c, px - b / 2, py, s1, 20, 140, TERRA, 0.7, dash=(2, 2))
    _arc(c, px + b / 2, py, s2, 40, 160, SAGE, 0.7, dash=(2, 2))
    _poly(c, [(px - b / 2, py), (px + b / 2, py), apex], fill=None, stroke=INK, lw=1.0)
    dot(c, px - b / 2, py); dot(c, px + b / 2, py)
    txt(c, x + cw * 2.5, tops, "Triangle from three sides", 6.8, "Inter-Semi", INK,
        "center")


def guide_layout(c, x, y, w, h):
    """Wireframe of the one-page student guide asked for in Mini-task 7."""
    bw, bh = w * 0.92, h * 0.86
    ox, oy = x + (w - bw) / 2, y + (h - bh) / 2 + 2
    box(c, ox, oy, bw, bh, fill=CREAM, stroke=RULE, lw=0.7)
    txt(c, ox + 8, oy + bh - 13, "ANGLE PAIRS \u2014 one page", 6.6, "Inter-Semi", GREEN)
    line(c, ox + 8, oy + bh - 18, ox + bw - 8, oy + bh - 18, spec.GOLD_PALE, 0.5)
    # left panel: the diagram
    pw = bw * 0.44
    box(c, ox + 8, oy + 8, pw, bh - 34, fill=None, stroke=RULE, lw=0.5, dash=(2, 2))
    y1 = oy + 8 + (bh - 34) * 0.62
    y2 = oy + 8 + (bh - 34) * 0.30
    line(c, ox + 16, y1, ox + pw - 2, y1, GREEN, 0.9)
    line(c, ox + 16, y2, ox + pw - 2, y2, GREEN, 0.9)
    line(c, ox + pw * 0.34, y1 + 14, ox + pw * 0.66, y2 - 14, INK, 0.8)
    _sector(c, ox + pw * 0.34, y1, 12, 205, 250, fill=spec.MIST, stroke=TERRA, lw=0.5)
    _sector(c, ox + pw * 0.66, y2, 12, 25, 70, fill=spec.MIST, stroke=TERRA, lw=0.5)
    txt(c, ox + 14, oy + 13, "one diagram, two colours", 5.8, "Inter", INK)
    # right panel: three labelled lines of text
    tx = ox + pw + 16
    for i, (lab, col) in enumerate((("Fact 1", TERRA), ("Fact 2", SAGE),
                                    ("Warning", GOLD_D))):
        yy = oy + bh - 42 - i * (bh - 60) / 3.0
        txt(c, tx, yy, lab, 6.0, "Inter-Semi", col)
        for k in range(2):
            line(c, tx, yy - 6 - k * 4.4, tx + bw * 0.34 - k * 18, yy - 6 - k * 4.4,
                 RULE, 1.1)


# ------------------------------------------------------- chapter 8 sets set
def _venn_pair(c, cx, cy, r, sep=0.62, fill_left=None, fill_right=None, fill_both=None,
               labels=("A", "B")):
    c.saveState()
    c.setStrokeColor(GREEN)
    c.setLineWidth(0.9)
    c.setFillColor(spec.MIST)
    c.circle(cx - r * sep, cy, r, stroke=1, fill=1)
    c.circle(cx + r * sep, cy, r, stroke=1, fill=1)
    c.restoreState()
    txt(c, cx - r * sep - r * 0.55, cy + r * 1.18, labels[0], 8.0, "SourceSerifItalic",
        GREEN)
    txt(c, cx + r * sep + r * 0.45, cy + r * 1.18, labels[1], 8.0, "SourceSerifItalic",
        GREEN)


def set_sort_grid(c, x, y, w, h):
    cols, rows = 5, 4
    cw, ch2 = w / (cols + 1.4), h / (rows + 1.2)
    ox, oy = x + cw * 1.1, y + ch2 * 0.5
    txt(c, ox - 6, oy + rows * ch2 + 6, "1\u201320 by two rules", 6.6, "Inter-Semi", GREEN)
    line(c, ox + cw * 0.5, oy + rows * ch2, ox + cw * 3.5, oy + rows * ch2, GOLD_D, 0.7,
         dash=(2, 2))
    n = 1
    for r in range(rows):
        for k in range(cols):
            if n > 20:
                break
            cx = ox + k * cw
            cy = oy + (rows - 1 - r) * ch2
            both = n % 2 == 0 and n % 3 == 0
            even = n % 2 == 0
            fill = CREAM if both else (spec.MIST if even else None)
            box(c, cx, cy, cw * 0.78, ch2 * 0.72, fill=fill,
                stroke=TERRA if both else RULE, lw=0.7 if both else 0.45)
            txt(c, cx + cw * 0.39, cy + ch2 * 0.24, str(n), 7.2, "Inter-Semi",
                TERRA if both else INK, "center")
            n += 1
    txt(c, ox - 4, oy - 12, "shaded: even \u00b7 outlined: multiple of 3 \u00b7 both: "
                            "darker", 6.2, "Inter", INK)


def complement_venn(c, x, y, w, h):
    r = min(w * 0.16, h * 0.30)
    cx, cy = x + w * 0.42, y + h * 0.48
    box(c, x + w * 0.06, y + h * 0.06, w * 0.88, h * 0.84, fill=None, stroke=RULE, lw=0.7)
    c.saveState()
    c.setFillColor(spec.CREAM_SOFT)
    c.setStrokeColor(GREEN)
    c.setLineWidth(0.9)
    c.circle(cx, cy, r, stroke=1, fill=1)
    c.restoreState()
    # complement hatching
    for k in range(9):
        yy = y + h * 0.12 + k * h * 0.09
        line(c, x + w * 0.09, yy, x + w * 0.91, yy, spec.MIST, 2.6)
    c.saveState()
    c.setFillColor(spec.CREAM_SOFT)
    c.setStrokeColor(GREEN)
    c.setLineWidth(0.9)
    c.circle(cx, cy, r, stroke=1, fill=1)
    c.restoreState()
    txt(c, cx, cy - 3, "A", 9.0, "SourceSerifItalic", GREEN, "center")
    txt(c, x + w * 0.09, y + h * 0.90, "\u03be", 8.6, "SourceSerifItalic", INK)
    txt(c, cx + r * 1.25, cy + r * 0.55, "A\u2032", 8.4, "SourceSerifItalic", TERRA)


def _venn_outline(c, cx, cy, r, sep):
    c.saveState()
    c.setStrokeColor(GREEN)
    c.setLineWidth(0.9)
    c.circle(cx - r * sep, cy, r, stroke=1, fill=0)
    c.circle(cx + r * sep, cy, r, stroke=1, fill=0)
    c.restoreState()


def _venn_fill(c, cx, cy, r, sep, fill):
    c.saveState()
    c.setFillColor(fill)
    c.circle(cx - r * sep, cy, r, stroke=0, fill=1)
    c.circle(cx + r * sep, cy, r, stroke=0, fill=1)
    c.restoreState()


def set_operations(c, x, y, w, h):
    r = min(w * 0.115, h * 0.30)
    for i, kind in enumerate(("union", "intersection")):
        cx = x + w * (0.27 + 0.46 * i)
        cy = y + h * 0.52
        sep = 0.55
        _venn_fill(c, cx, cy, r, sep, spec.CREAM_SOFT)
        c.saveState()
        c.setFillColor(spec.GOLD_PALE)
        if kind == "union":
            c.circle(cx - r * sep, cy, r, stroke=0, fill=1)
            c.circle(cx + r * sep, cy, r, stroke=0, fill=1)
        else:
            n = 60
            p = c.beginPath()
            dy = r * math.sqrt(1 - sep ** 2)
            p.moveTo(cx, cy + dy)
            for k in range(n + 1):
                a = math.radians(60 + 240.0 * k / n)
                p.lineTo(cx - r * sep + r * math.cos(a), cy + r * math.sin(a))
            p.close()
            c.drawPath(p, stroke=0, fill=1)
        c.restoreState()
        _venn_outline(c, cx, cy, r, sep)
        txt(c, cx - r * sep - r * 0.42, cy + r * 1.16, "A", 7.8, "SourceSerifItalic",
            GREEN)
        txt(c, cx + r * sep + r * 0.30, cy + r * 1.16, "B", 7.8, "SourceSerifItalic",
            GREEN)
        op = "\u222a" if kind == "union" else "\u2229"
        word = "everything in either" if kind == "union" else "only what is in both"
        # measure so the whole label is centred as one line
        wA = stringWidth("A ", "Inter-Semi", 7.2)
        wB = stringWidth(" B   " + word, "Inter-Semi", 7.2)
        wO = stringWidth(op, "Sym", 7.6)
        total = wA + wO + wB
        lx = cx - total / 2
        txt(c, lx, y + h * 0.10, "A ", 7.2, "Inter-Semi", GREEN)
        txt(c, lx + wA, y + h * 0.10, op, 7.6, "Sym", GREEN)
        txt(c, lx + wA + wO, y + h * 0.10, " B   " + word, 7.2, "Inter-Semi", GREEN)


def number_system_tree(c, x, y, w, h):
    bands = [("Real numbers", 0.06, 0.94), ("Rational", 0.16, 0.74),
             ("Integer", 0.28, 0.60), ("Whole", 0.40, 0.50), ("Natural", 0.52, 0.40)]
    bw = w * 0.84
    ox = x + w * 0.08
    for i, (name, a, b) in enumerate(bands):
        yy = y + h * 0.82 - i * h * 0.155
        box(c, ox + bw * a, yy - h * 0.11, bw * (b - a), h * 0.115,
            fill=spec.CREAM_SOFT if i % 2 == 0 else spec.MIST, stroke=GREEN, lw=0.7)
        txt(c, ox + bw * a + 6, yy - h * 0.065, name, 7.0, "Inter-Semi", GREEN)
    txt(c, ox + bw * 0.80, y + h * 0.80, "irrational numbers", 6.4, "SourceSerifItalic",
        TERRA)
    arrow(c, ox - 10, y + h * 0.20, ox - 10, y + h * 0.80, SAGE, 0.7)
    txt(c, ox - 16, y + h * 0.48, "nested subsets", 6.2, "Inter", SAGE, "right")


def sorting_table(c, x, y, w, h):
    """A two-way table from the chapter 8 mini-task: a class library of 28 items,
    sorted by one property down the side and another across the top."""
    cols = ["Fiction", "Not fiction"]
    rows = ["Hardback", "Paperback"]
    cells = [["12 novels", "4 atlases"],
             ["9 short-story collections", "3 dictionaries"]]

    tw = w * 0.52
    ox = x + w * 0.16
    th = h * 0.44
    oy = y + h * 0.34                      # bottom edge of the table
    hh = th * 0.26                         # header band
    rh = (th - hh) / 2.0
    cw = tw / 2.0
    top = oy + th

    # which property runs which way
    txt(c, ox, top + 16, "One property runs across the top, the other runs down the "
        "side.", 6.2, "Inter", GOLD_D)

    # header band
    box(c, ox, top - hh, tw, hh, fill=spec.MIST, stroke=RULE, lw=0.6)
    for k, name in enumerate(cols):
        txt(c, ox + cw * (k + 0.5), top - hh + hh * 0.36, name, 7.0, "Inter-Semi",
            GREEN, "center")
    line(c, ox + cw, top - hh, ox + cw, oy, col=RULE, lw=0.6)

    # body rows
    for i, name in enumerate(rows):
        cy = top - hh - (i + 1) * rh
        for k in range(2):
            box(c, ox + k * cw, cy, cw, rh, fill=CREAM if i == 0 else None,
                stroke=RULE, lw=0.6)
            txt(c, ox + cw * (k + 0.5), cy + rh * 0.40, cells[i][k], 6.6,
                "SourceSerifItalic", INK, "center")
        txt(c, ox - 28, cy + rh * 0.40, name, 6.8, "Inter-Semi", GREEN, "right")

    # reading the table
    txt(c, ox, oy - 18, "Each cell is the intersection of the two properties. Every one "
        "of the 28 items", 6.3, "Inter", INK)
    txt(c, ox, oy - 27, "lands in exactly one cell; an item that fits none tells you the "
        "rule needs revising.", 6.3, "Inter", INK)


# -------------------------------------------------- chapter 9 measurement set
def perimeter_area_grid(c, x, y, w, h):
    specs = [(2, 3, "6 squares"), (4, 3, "12 squares"), (4, 6, "24 squares")]
    cw = w / 3.0
    u = min(cw * 0.085, h * 0.115)
    for i, (cols, rows, area) in enumerate(specs):
        ox = x + cw * (i + 0.10)
        oy = y + h * 0.30
        for r in range(rows):
            for k in range(cols):
                box(c, ox + k * u, oy + r * u, u, u, fill=spec.MIST if (r + k) % 2 == 0
                    else CREAM, stroke=GREEN, lw=0.35)
        c.saveState()
        c.setStrokeColor(TERRA)
        c.setLineWidth(1.4)
        c.rect(ox, oy, cols * u, rows * u, stroke=1, fill=0)
        c.restoreState()
        txt(c, ox, oy - 9, "%d \u00d7 %d" % (cols, rows), 6.8, "Inter-Semi", INK)
        txt(c, ox, y + h * 0.10, area, 6.4, "SourceSerifItalic", GOLD_D)
        txt(c, ox, y + h * 0.02, "P = %d units" % (2 * (cols + rows)), 6.2, "Inter",
            TERRA)
    txt(c, x + w * 0.94, y + h * 0.90, "darker outline = perimeter", 6.2, "Inter", TERRA,
        "right")


def circle_parts_box(c, x, y, w, h):
    r = min(w * 0.17, h * 0.34)
    cx, cy = x + w * 0.30, y + h * 0.55
    circle_parts(c, cx, cy, r)
    txt(c, x + w * 0.60, cy + 6, "radius = half the diameter", 6.6, "Inter", INK)
    txt(c, x + w * 0.60, cy - 6, "C = \u03c0 d = 2 \u03c0 r", 7.2, "SourceSerifItalic",
        GOLD_D)
    txt(c, x + w * 0.60, cy - 18, "every point on the circle is r from the centre",
        6.2, "Inter", INK)


def area_formulae(c, x, y, w, h):
    # parallelogram: rectangle sheared
    ox = x + w * 0.03
    bw, bh = w * 0.20, h * 0.46
    by = y + h * 0.30
    _poly(c, [(ox, by), (ox + bw, by), (ox + bw * 1.28, by + bh), (ox + bw * 0.28, by + bh)],
          fill=spec.MIST, stroke=GREEN)
    line(c, ox + bw * 0.28, by + bh, ox + bw * 0.28, by, TERRA, 0.8, dash=(2.5, 2))
    line(c, ox, by, ox + bw * 0.28, by, TERRA, 1.2)
    txt(c, ox + bw * 0.14, by - 10, "base", 6.0, "Inter-Semi", TERRA)
    txt(c, ox + bw * 0.28 + 4, by + bh * 0.45, "h", 7.0, "SourceSerifItalic", TERRA)
    txt(c, ox, y + h * 0.10, "parallelogram", 6.4, "Inter", INK)
    txt(c, ox, y + h * 0.02, "A = b \u00d7 h", 7.0, "SourceSerifItalic", GOLD_D)

    # triangle in a rectangle
    ox2 = x + w * 0.30
    box(c, ox2, by, bw, bh, fill=CREAM, stroke=RULE, lw=0.5, dash=(2, 2))
    _poly(c, [(ox2, by), (ox2 + bw, by), (ox2 + bw * 0.62, by + bh)],
          fill=spec.MIST, stroke=GREEN)
    line(c, ox2 + bw * 0.62, by + bh, ox2 + bw * 0.62, by, TERRA, 0.8, dash=(2.5, 2))
    txt(c, ox2 + bw * 0.20, by - 10, "base", 6.0, "Inter-Semi", TERRA)
    txt(c, ox2 + bw * 0.62 + 4, by + bh * 0.45, "h", 7.0, "SourceSerifItalic", TERRA)
    txt(c, ox2, y + h * 0.10, "triangle (half the rectangle)", 6.4, "Inter", INK)
    txt(c, ox2, y + h * 0.02, "A = \u00bd b \u00d7 h", 7.0, "SourceSerifItalic", GOLD_D)

    # trapezium: two copies
    ox3 = x + w * 0.66
    tw1 = bw * 0.66
    _poly(c, [(ox3, by), (ox3 + tw1, by), (ox3 + tw1 * 0.78, by + bh),
              (ox3 + tw1 * 0.22, by + bh)], fill=spec.MIST, stroke=GREEN)
    _poly(c, [(ox3 + tw1, by), (ox3 + tw1 * 1.28, by), (ox3 + tw1 * 1.28, by + bh * 0.0),
              (ox3 + tw1 * 0.78, by + bh)], fill=CREAM, stroke=SAGE)
    line(c, ox3, by + bh, ox3 + tw1 * 0.22, by + bh, TERRA, 1.2)
    line(c, ox3, by, ox3 + tw1, by, TERRA, 1.2)
    txt(c, ox3 + tw1 * 0.5, by - 10, "a + b", 6.0, "Inter-Semi", TERRA, "center")
    txt(c, ox3, y + h * 0.10, "trapezium (two copies)", 6.4, "Inter", INK)
    txt(c, ox3, y + h * 0.02, "A = \u00bd (a + b) h", 7.0, "SourceSerifItalic", GOLD_D)


def circle_area(c, x, y, w, h):
    cx, cy = x + w * 0.20, y + h * 0.50
    r = min(w * 0.13, h * 0.40)
    c.saveState()
    c.setFillColor(spec.MIST)
    c.setStrokeColor(GREEN)
    c.setLineWidth(0.8)
    c.circle(cx, cy, r, stroke=1, fill=1)
    for k in range(24):
        a = math.radians(360.0 * k / 24)
        line(c, cx, cy, cx + r * math.cos(a), cy + r * math.sin(a), CREAM, 0.5)
    c.restoreState()
    line(c, cx, cy, cx + r, cy, TERRA, 0.9)
    txt(c, cx + r * 0.5, cy + 4, "r", 7.0, "SourceSerifItalic", TERRA, "center")
    txt(c, cx, y + h * 0.06, "A = \u03c0r", 8.0, "SourceSerifItalic", GOLD_D, "center")
    txt(c, cx + 20, y + h * 0.06 + 4, "2", 5.6, "SourceSerifItalic", GOLD_D)
    arrow(c, x + w * 0.36, cy, x + w * 0.46, cy, GOLD_D, 0.9)
    # rearranged sectors -> near rectangle
    rx, ry = x + w * 0.52, y + h * 0.34
    rw, rh = w * 0.40, r * 1.05
    for k in range(12):
        tri = [(rx + rw * k / 12.0, ry), (rx + rw * (k + 1) / 12.0, ry)]
        _poly(c, tri + [(rx + rw * (k + 0.5) / 12.0, ry + rh)],
              fill=spec.MIST if k % 2 == 0 else CREAM, stroke=GREEN, lw=0.4)
    line(c, rx, ry - 8, rx + rw, ry - 8, TERRA, 0.9)
    txt(c, rx + rw * 0.5, ry - 17, "half the circumference \u2248 \u03c0r", 6.2, "Inter-Semi",
        TERRA, "center")
    txt(c, rx + rw + 4, ry + rh * 0.5, "r", 7.0, "SourceSerifItalic", TERRA)
    txt(c, rx + rw * 0.5, y + h * 0.10, "rearranged: a rectangle \u03c0r by r",
        6.2, "Inter", INK, "center")


# ------------------------------------------------------- chapter 10 data set
def _tally(c, cx, cy, n, col=None, unit=2.7, hgt=5.4):
    """Draw n tally marks in groups of five, centred on cx with baseline cy."""
    col = col or spec.SAGE
    c.saveState()
    c.setStrokeColor(col)
    c.setLineWidth(0.9)
    c.setLineCap(0)
    group_w = 4 * unit
    gap = unit * 1.9
    total = (n // 5) * (group_w + gap) + (n % 5) * unit - (unit if n % 5 else 0)
    if total < 0:
        total = 0
    sx = cx - total / 2.0
    i = 0
    while i < n:
        take = min(5, n - i)
        gx = sx
        for k in range(take):
            c.line(gx + k * unit, cy, gx + k * unit, cy + hgt)
        if take == 5:
            c.line(gx - 1.2, cy + 1.0, gx + group_w + 1.2, cy + hgt - 1.0)
        sx = gx + (group_w + gap if take == 5 else take * unit)
        i += take
    c.restoreState()


def data_table_tally(c, x, y, w, h):
    """A frequency table with hand-style tally marks in the middle column."""
    vals = [("3", 3, 3), ("4", 5, 5), ("5", 4, 4), ("6", 2, 2), ("7", 1, 1)]
    tx = x + w * 0.10
    tw = w * 0.72
    top = y + h * 0.92
    rows = len(vals) + 1
    rh = h * 0.80 / rows
    box(c, tx, top - rh * rows, tw, rh * rows, fill=CREAM, stroke=RULE, lw=0.7)
    for i in range(1, rows):
        line(c, tx, top - rh * i, tx + tw, top - rh * i, RULE, 0.4)
    line(c, tx + tw * 0.26, top - rh * rows, tx + tw * 0.26, top, RULE, 0.4)
    line(c, tx + tw * 0.64, top - rh * rows, tx + tw * 0.64, top, RULE, 0.4)
    heads = ["Value", "Tally", "Frequency"]
    for k, hd in enumerate(heads):
        txt(c, tx + tw * (0.06 + 0.32 * k), top - rh * 0.70, hd, 6.6, "Inter-Semi",
            GREEN)
    for i, (v, tal, f) in enumerate(vals, start=1):
        yy = top - rh * (i + 0.68)
        txt(c, tx + tw * 0.14, yy, v, 7.2, "Inter-Semi", INK, "center")
        _tally(c, tx + tw * 0.45, yy - 1.2, tal)
        txt(c, tx + tw * 0.82, yy, str(f), 7.2, "Inter-Semi", TERRA, "center")
    txt(c, tx + tw + 14, top - rh * 2.2, "the list becomes a", 6.2, "Inter", INK)
    txt(c, tx + tw + 14, top - rh * 3.2, "shape you can see", 6.2, "Inter", INK)
    txt(c, tx + tw + 14, top - rh * 4.2, "at once", 6.2, "Inter", INK)
    txt(c, tx, top - rh * rows - 11, "total = 15 observations", 6.2, "SourceSerifItalic",
        GOLD_D)


def averages_compare(c, x, y, w, h):
    """Seven values as bars, with mean / median / mode marked on a scale beneath."""
    data = [4, 7, 7, 9, 13]
    n = len(data)
    span = w * 0.76
    ox = x + w * 0.12
    base = y + h * 0.52
    plot_h = h * 0.40
    slot = span / n
    bw = slot * 0.56
    for i, v in enumerate(data):
        bh = plot_h * v / 14.0
        bx = ox + i * slot + (slot - bw) / 2
        box(c, bx, base, bw, bh, fill=spec.SAND if v == 7 else spec.MIST, stroke=GREEN,
            lw=0.6)
        txt(c, bx + bw / 2, base + bh + 3, str(v), 7.0, "Inter-Semi", INK, "center")
    line(c, ox - 6, base, ox + span + 6, base, INK, 0.7)
    txt(c, ox - 10, base - 3, "values", 6.4, "Inter", spec.INK_MUTE, "right")
    # number line under the bars, 0..14 across the same span
    nl = base - h * 0.20
    line(c, ox, nl, ox + span, nl, INK, 0.6)
    for k in range(0, 15, 2):
        px = ox + span * k / 14.0
        line(c, px, nl - 2.5, px, nl + 2.5, INK, 0.5)
        txt(c, px, nl - 11, str(k), 5.8, "Inter", spec.INK_MUTE, "center")
    marks = [(8.0, TERRA, "mean 8", h * 0.34, "left"),
             (7.0, GOLD_D, "median 7 = mode", h * 0.18, "right")]
    for val, col, lab, rise, side in marks:
        px = ox + span * val / 14.0
        line(c, px, nl, px, nl + rise, col, 0.9, dash=(2.5, 2))
        if side == "right":
            txt(c, px - 4, nl + rise, lab, 6.6, "Inter-Semi", col, "right")
        else:
            txt(c, px + 4, nl + rise, lab, 6.6, "Inter-Semi", col)
    txt(c, ox, y + h * 0.03, "range 13 \u2212 4 = 9", 6.6, "SourceSerifItalic", SAGE)


def piechart_share(c, x, y, w, h):
    r = min(w * 0.13, h * 0.36)
    cx, cy = x + w * 0.20, y + h * 0.52
    pie(c, cx, cy, r, [(25, spec.SAND, ""), (40, spec.MIST, ""), (20, spec.BLUSH, ""),
                       (15, CREAM, "")])
    labels = [("walk 25 %", spec.SAND), ("bus 40 %", spec.MIST),
              ("car 20 %", spec.BLUSH), ("cycle 15 %", CREAM)]
    for i, (lab, col) in enumerate(labels):
        yy = y + h * 0.78 - i * h * 0.16
        box(c, x + w * 0.44, yy - 3, 9, 9, fill=col, stroke=RULE, lw=0.4)
        txt(c, x + w * 0.44 + 15, yy - 2, lab, 6.8, "Inter", INK)
    txt(c, cx, y + h * 0.06, "480 students in total", 6.4, "SourceSerifItalic", GOLD_D,
        "center")


def misleading_axes(c, x, y, w, h):
    def chart(ox, zero, title):
        cw, chh = w * 0.34, h * 0.56
        oy = y + h * 0.18
        box(c, ox, oy, cw, chh, fill=CREAM, stroke=RULE, lw=0.6)
        base = 0 if zero else 90
        top = 120
        for k in range(4):
            val = 100 + k * 5
            frac = (val - base) / (top - base)
            bh = chh * 0.86 * frac
            box(c, ox + cw * (0.12 + 0.22 * k), oy + chh * 0.08, cw * 0.14, bh,
                fill=spec.MIST, stroke=GREEN, lw=0.6)
        line(c, ox + cw * 0.08, oy + chh * 0.08, ox + cw * 0.08, oy + chh * 0.94,
             INK, 0.7)
        txt(c, ox + cw * 0.08, oy + chh * 0.98, "120", 6.0, "Inter", INK, "center")
        txt(c, ox + cw * 0.08, oy + chh * 0.02, ("0" if zero else "90"), 6.0, "Inter",
            INK, "center")
        txt(c, ox + cw * 0.5, oy - 12, title, 6.6, "Inter-Semi",
            GREEN if zero else TERRA, "center")

    chart(x + w * 0.05, True, "axis from zero: a steady rise")
    chart(x + w * 0.52, False, "axis from 90: a dramatic rise")
    txt(c, x + w * 0.50, y + h * 0.05, "same four values, twice", 6.2, "Inter", INK,
        "center")


def honest_panel(c, x, y, w, h):
    def sheet(ox, zero, caption, col):
        sw, sh = w * 0.38, h * 0.66
        oy = y + h * 0.20
        box(c, ox, oy, sw, sh, fill=CREAM, stroke=RULE, lw=0.6)
        line(c, ox + 10, oy + sh * 0.18, ox + sw - 10, oy + sh * 0.18, INK, 0.7)
        pts = []
        for k in range(5):
            val = 40 + k * 6
            base = 0 if zero else 30
            top = 80
            frac = (val - base) / (top - base)
            pts.append((ox + 16 + k * (sw - 32) / 4.0, oy + sh * 0.18 + sh * 0.62 * frac))
        for i in range(len(pts) - 1):
            line(c, pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], col, 1.3)
        for px, py in pts:
            dot(c, px, py, 1.7, col)
        txt(c, ox + sw / 2, oy - 12, caption, 6.4, "Inter-Semi", col, "center")

    sheet(x + w * 0.08, True, "year 1\u20135, axis from zero", SAGE)
    sheet(x + w * 0.54, False, "the same five figures, axis from 30", TERRA)


def barchart_box(c, x, y, w, h, data):
    barchart(c, x, y + h * 0.20, w, h * 0.74, data)


def dotplot_box(c, x, y, w, h, values):
    dotplot(c, x, y + h * 0.26, w, h * 0.60, values)
