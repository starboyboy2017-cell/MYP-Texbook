"""Original vector diagrams for the improved first edition.

Every diagram is drawn with reportlab primitives, so it stays sharp at any
output size and prints without halftone artefacts. Each function receives
(canvas, x, y, w, h) where (x, y) is the *bottom* left of the artwork box.

Coordinates inside a diagram are written on a unit grid: u runs 0 -> 1 left to
right, v runs 0 -> 1 top to bottom. That keeps the drawings independent of the
page and lets them be re-proportioned by changing one number.
"""
from reportlab.lib.colors import HexColor

from bookkit import spec, typeset

INK = spec.INK
SOFT = spec.INK_LABEL
MUTE = spec.INK_MUTE
SAGE = spec.SAGE
SLATE = spec.SLATE
TERRA = spec.TERRACOTTA
GOLD = spec.GOLD_DEEP
COPPER = spec.GOLD
MIST = spec.MIST
SAND = spec.SAND
BLUSH = spec.BLUSH
PALE = HexColor("#DCE4EC")
INTER_TXT = HexColor("#3B4A57")
RUST = spec.TERRACOTTA


class Pen:
    def __init__(self, c, x, y, w, h):
        self.c, self.x, self.y, self.w, self.h = c, x, y, w, h

    # -- geometry ----------------------------------------------------------
    def X(self, u):
        return self.x + u * self.w

    def Y(self, v):
        return self.y + self.h - v * self.h

    def line(self, u1, v1, u2, v2, lw=0.8, colour=INK, dash=None, alpha=None):
        c = self.c
        c.saveState()
        c.setStrokeColor(colour)
        c.setLineWidth(lw)
        if dash:
            c.setDash(*dash)
        if alpha is not None:
            try:
                c.setStrokeAlpha(alpha)
            except Exception:
                pass
        c.line(self.X(u1), self.Y(v1), self.X(u2), self.Y(v2))
        c.restoreState()

    def rect(self, u, v, wu, hv, lw=0.8, colour=INK, fill=None, dash=None,
             alpha=None, radius=None):
        c = self.c
        c.saveState()
        c.setLineWidth(lw)
        if colour is not None:
            c.setStrokeColor(colour)
        if dash:
            c.setDash(*dash)
        if fill is not None:
            c.setFillColor(fill)
        if alpha is not None:
            try:
                c.setStrokeAlpha(alpha)
                c.setFillAlpha(alpha)
            except Exception:
                pass
        wpx, hpx = wu * self.w, hv * self.h
        if radius:
            c.roundRect(self.X(u), self.Y(v + hv), wpx, hpx, radius,
                        stroke=1 if colour else 0, fill=1 if fill is not None else 0)
        else:
            c.rect(self.X(u), self.Y(v + hv), wpx, hpx,
                   stroke=1 if colour else 0, fill=1 if fill is not None else 0)
        c.restoreState()

    def poly(self, pts, lw=0.9, colour=INK, fill=None, close=True, dash=None):
        c = self.c
        c.saveState()
        c.setStrokeColor(colour)
        c.setLineWidth(lw)
        if dash:
            c.setDash(*dash)
        p = c.beginPath()
        p.moveTo(self.X(pts[0][0]), self.Y(pts[0][1]))
        for u, v in pts[1:]:
            p.lineTo(self.X(u), self.Y(v))
        if close:
            p.close()
        if fill is not None:
            c.setFillColor(fill)
        c.drawPath(p, stroke=1 if colour else 0, fill=1 if fill is not None else 0)
        c.restoreState()

    def circle(self, u, v, r, lw=0.8, colour=INK, fill=None):
        c = self.c
        c.saveState()
        c.setLineWidth(lw)
        if colour is not None:
            c.setStrokeColor(colour)
        if fill is not None:
            c.setFillColor(fill)
        c.circle(self.X(u), self.Y(v), r, stroke=1 if colour is not None else 0,
                 fill=1 if fill is not None else 0)
        c.restoreState()

    def dot(self, u, v, r=2.0, colour=INK):
        self.circle(u, v, r, colour=None, fill=colour)

    def arrow(self, u1, v1, u2, v2, lw=1.0, colour=INK, head=4.2, dash=None):
        import math
        self.line(u1, v1, u2, v2, lw=lw, colour=colour, dash=dash)
        ang = math.atan2(self.Y(v2) - self.Y(v1), self.X(u2) - self.X(u1))
        for s in (+1, -1):
            a = ang + s * 0.42
            self.c.saveState()
            self.c.setStrokeColor(colour)
            self.c.setLineWidth(lw)
            self.c.line(self.X(u2), self.Y(v2),
                        self.X(u2) - head * math.cos(a) / self.w * 1.0,
                        self.Y(v2) - head * math.sin(a) / self.h * 1.0)
            self.c.restoreState()

    def arc(self, u, v, r, start, extent, lw=0.8, colour=INK, dash=None):
        c = self.c
        c.saveState()
        c.setStrokeColor(colour)
        c.setLineWidth(lw)
        if dash:
            c.setDash(*dash)
        cx, cy = self.X(u), self.Y(v)
        c.arc(cx - r, cy - r, cx + r, cy + r, startAng=start, extent=extent)
        c.restoreState()

    def text(self, u, v, s, size=7.0, font="Inter", colour=INK, anchor="c",
             track=0.0, bold=False):
        name = font
        w = typeset.width(s, name, size, track)
        px = self.X(u)
        if anchor == "c":
            px -= w / 2
        elif anchor == "r":
            px -= w
        typeset.draw(self.c, px, self.Y(v) - size * 0.34, s, name, size, colour, track)

    def tsize(self, s, size=7.0, font="Inter", track=0.0):
        return typeset.width(s, font, size, track)


# --------------------------------------------------------------------- helpers
def _box(pen, u, v, wu, hv, label, fill=None, colour=INK, lw=0.9, size=7.2,
         lab_colour=None):
    pen.rect(u, v, wu, hv, lw=lw, colour=colour, fill=fill)
    pen.text(u + wu / 2, v + hv / 2, label, size=size, colour=lab_colour or colour,
             font="Inter-Semi")


def _axis(pen, u0, v0, u1, v1, xlab=None, ylab=None, tickv=(), ticku=(),
          lab_size=6.4):
    pen.arrow(u0, v0, u1, v0, 0.9, INK, head=4.5)
    pen.arrow(u0, v0, u0, v1, 0.9, INK, head=4.5)
    for t in tickv:
        pen.line(u0, t, u0 + 0.012, t, 0.7, INK)
    for t in ticku:
        pen.line(t, v0, t, v0 - 0.02, 0.7, INK)
    if xlab:
        pen.text((u0 + u1) / 2, v0 + 0.055, xlab, lab_size, colour=MUTE)
    if ylab:
        pen.text(u0 - 0.005, (v0 + v1) / 2 - 0.06, ylab, lab_size, colour=MUTE,
                 anchor="r")


def _grid(pen, u0, v0, u1, v1, n_x=10, n_y=10, colour=PALE, lw=0.4):
    for i in range(n_x + 1):
        u = u0 + (u1 - u0) * i / n_x
        pen.line(u, v0, u, v1, lw, colour)
    for j in range(n_y + 1):
        v = v0 + (v1 - v0) * j / n_y
        pen.line(u0, v, u1, v, lw, colour)


# ======================================================= 1 · ratios
def ratio_tape(c, x, y, w, h, parts=(3, 5), labels=("blue", "yellow"),
               colours=None):
    p = Pen(c, x, y, w, h)
    cols = colours or (BLUSH, MIST)
    u0, v0, hh = 0.03, 0.30, 0.34
    tot = sum(parts)
    uu = u0
    for i, n in enumerate(parts):
        wu = 0.92 * n / tot
        p.rect(uu, v0, wu, hh, lw=1.0, colour=INK, fill=cols[i % len(cols)])
        p.text(uu + wu / 2, v0 + hh / 2, str(n), size=9.0, font="Inter-Semi",
               colour=INK)
        p.text(uu + wu / 2, v0 + hh + 0.13, labels[i], size=7.0, colour=MUTE,
               font="SourceSerifItalic")
        uu += wu
    # bracket under the whole bar
    p.line(u0, v0 - 0.13, u0 + 0.92, v0 - 0.13, 0.6, MUTE)
    p.line(u0, v0 - 0.10, u0, v0 - 0.16, 0.6, MUTE)
    p.line(u0 + 0.92, v0 - 0.10, u0 + 0.92, v0 - 0.16, 0.6, MUTE)
    p.text(u0 + 0.46, v0 - 0.055, f"{tot} equal parts in the whole",
           size=6.8, colour=MUTE)


def double_number_line(c, x, y, w, h, top=(0, 3, 6, 9), bot=(0, 5, 10, 15),
                       toplab="cups of lemon juice", botlab="cups of water",
                       colour_top=TERRA, colour_bot=SAGE):
    p = Pen(c, x, y, w, h)
    u0, u1 = 0.06, 0.94
    vtop, vbot = 0.30, 0.72
    for v, vals, lab, col, above in ((vtop, top, toplab, colour_top, True),
                                     (vbot, bot, botlab, colour_bot, False)):
        p.line(u0, v, u1, v, 1.0, INK)
        p.arrow(u1 - 0.02, v, u1 + 0.03, v, 1.0, INK, head=4.5)
        top_val = max(vals)
        for val in vals:
            uu = u0 + (u1 - u0) * val / top_val
            p.line(uu, v - 0.055, uu, v + 0.055, 1.0, INK)
            p.text(uu, v - 0.085 if above else v + 0.085, str(val), 7.0,
                   font="Inter-Semi", colour=col)
        p.text(u0, v - 0.10 if above else v + 0.10, "", 6.4)
        p.text(u1 + 0.02, v + 0.10 if above else v - 0.10, lab, 6.6,
               colour=MUTE, anchor="r", font="SourceSerifItalic")
    # pairing arrows
    for a, b in zip(top, bot):
        uu = u0 + (u1 - u0) * a / max(top)
        p.line(uu, vtop + 0.06, uu, vbot - 0.06, 0.45, MUTE, dash=(1.2, 2.6))


def recipe_bars(c, x, y, w, h, recipes=((2, 5), (4, 10), (6, 15), (3, 8)),
                names=("A", "B", "C", "D")):
    p = Pen(c, x, y, w, h)
    base, tall = 0.88, 0.62
    n = len(recipes)
    slot = 0.94 / n
    mx = max(sum(r) for r in recipes)
    for i, (a, b) in enumerate(recipes):
        uu = 0.03 + i * slot
        wa = slot * 0.44 * a / mx * 2.2
        wb = slot * 0.44 * b / mx * 2.2
        p.rect(uu, base - wa, 0.14, wa, lw=0.8, colour=INK, fill=BLUSH)
        p.rect(uu + 0.16, base - wb, 0.14, wb, lw=0.8, colour=INK, fill=MIST)
        p.text(uu + 0.07, base - wa - 0.055, str(a), 6.6, font="Inter-Semi", colour=TERRA)
        p.text(uu + 0.23, base - wb - 0.055, str(b), 6.6, font="Inter-Semi", colour=SAGE)
        p.text(uu + 0.15, base + 0.075, f"Recipe {names[i]}", 6.8, colour=INK)
    p.line(0.03, base, 0.97, base, 0.8, INK)
    p.text(0.03, base + 0.16, "lemon juice (shaded) and water (tinted), in cups",
           6.4, colour=MUTE, anchor="l", font="SourceSerifItalic")
    p.rect(0.03, base + 0.20, 0.02, 0.02, colour=None, fill=BLUSH)
    p.rect(0.03, base + 0.20, 0.02, 0.02, colour=None, fill=MIST)


def ratio_grid(c, x, y, w, h, a=3, b=5):
    """A rectangle shown as a x b unit squares: the ratio in space."""
    p = Pen(c, x, y, w, h)
    cell = min(0.72 / (a + b), 0.7 / max(a, b))
    u0 = 0.5 - (a + b) * cell / 2
    v0 = 0.42 - 0.0
    for i in range(a):
        for j in range(b):
            p.rect(u0 + i * cell, v0 + j * cell, cell, cell, lw=0.5, colour=MUTE,
                   fill=BLUSH if i < a else MIST)
    p.text(u0 + cell * 0.5, v0 + b * cell + 0.07, "3", 7.0, font="Inter-Semi",
           colour=TERRA)
    p.text(u0 + a * cell + 0.035, v0 + cell * 0.5, "5", 7.0, font="Inter-Semi",
           colour=SAGE, anchor="l")
    p.text(u0 + (a + b) * cell / 2, v0 - 0.10,
           "a 3 : 5 ratio is a 3-by-5 block: 15 equal parts", 6.6, colour=MUTE)


def share_bars(c, x, y, w, h, parts=(2, 3, 4), labels=("A", "B", "C"),
               total=360):
    p = Pen(c, x, y, w, h)
    tot = sum(parts)
    u0, v0, hh = 0.04, 0.42, 0.30
    uu = u0
    cols = (BLUSH, MIST, MAND := HexColor("#ECEFF3"))
    for i, n in enumerate(parts):
        wu = 0.90 * n / tot
        p.rect(uu, v0, wu, hh, lw=0.9, colour=INK, fill=cols[i % 3])
        p.text(uu + wu / 2, v0 + hh / 2 + 0.02, f"{n} parts", 7.4, colour=INK)
        p.text(uu + wu / 2, v0 + hh / 2 - 0.075,
               str(round(total * n / tot)), 9.4, font="Inter-Semi", colour=TERRA)
        p.text(uu + wu / 2, v0 - 0.075, labels[i], 7.4, colour=MUTE,
               font="SourceSerifItalic")
        uu += wu
    p.text(0.04, v0 + hh + 0.10, f"total {total}, shared in the ratio "
                                 + " : ".join(str(n) for n in parts),
           6.8, colour=MUTE, anchor="l", font="SourceSerifItalic")


def scale_pair(c, x, y, w, h):
    """A small and a large similar rectangle with the scale factor marked."""
    p = Pen(c, x, y, w, h)
    p.rect(0.08, 0.52, 0.24, 0.30, lw=0.9, colour=INK, fill=MIST)
    p.text(0.20, 0.67, "model", 6.6, colour=SLATE)
    p.text(0.20, 0.78, "3 cm", 6.4, colour=MUTE)
    p.rect(0.52, 0.22, 0.44, 0.60, lw=0.9, colour=INK, fill=BLUSH)
    p.text(0.74, 0.52, "the real thing", 7.2, colour=TERRA)
    p.text(0.74, 0.14, "45 cm", 6.6, colour=MUTE)
    p.arrow(0.34, 0.66, 0.50, 0.50, 1.0, GOLD, head=5)
    p.text(0.44, 0.44, "\u00d7 15", 7.0, font="Inter-Semi", colour=GOLD, anchor="l")


# ======================================================= 2 · proportional reasoning
def prop_graph(c, x, y, w, h, k=3, xmax=8):
    p = Pen(c, x, y, w, h)
    u0, v0, u1, v1 = 0.10, 0.86, 0.94, 0.10
    _grid(p, u0, v0, u1, v1, 8, 8, PALE)
    _axis(p, u0, v0, u1, v1, "litres of paint", "cost  (\u00a3)")
    uu = u0 + (u1 - u0) * xmax / 9.2
    vv = v0 - (v0 - v1) * (k * xmax) / (k * 9.2)
    p.line(u0, v0, uu, vv, 1.3, TERRA)
    for xx in range(1, xmax + 1):
        px = u0 + (u1 - u0) * xx / 9.2
        py = v0 - (v0 - v1) * (k * xx) / (k * 9.2)
        p.dot(px, py, 2.0, TERRA)
    p.text(u0 + 0.30, v1 + 0.10, "a straight line through the origin: "
                                 "cost \u00f7 litres is constant", 6.6, colour=MUTE,
           anchor="l", font="SourceSerifItalic")
    p.line(u0 + 0.30, v0 - 0.16, u0 + 0.30 + 0.13, v0 - 0.16, 1.0, TERRA)
    p.text(u0 + 0.45, v0 - 0.20, f"gradient = {k}", 6.6, colour=TERRA, anchor="l")


def proportion_table_shade(c, x, y, w, h, rows=(("paint (L)", 2, 3, 5, 8),
                                                ("cost (\u00a3)", 6, 9, 15, 24))):
    p = Pen(c, x, y, w, h)
    n = len(rows[0]) - 1
    cw = 0.68 / n
    rh = 0.34
    v = 0.14
    for r, row in enumerate(rows):
        p.rect(0.04, v + r * rh, 0.20, rh, lw=0.6, colour=RULE_C, fill=STONE_C)
        p.text(0.26, v + r * rh + rh / 2, row[0], 7.0, colour=INK, anchor="l")
        for i in range(n):
            p.rect(0.26 + i * cw, v + r * rh, cw, rh, lw=0.5, colour=RULE_C)
            p.text(0.26 + i * cw + cw / 2, v + r * rh + rh / 2, str(row[i + 1]), 7.4,
                   colour=INK, font="Inter-Semi")
    # arrows between columns
    for i in range(n - 1):
        p.text(0.26 + (i + 1) * cw, v + rh * 2 + 0.05, "\u00d7", 6.4,
               colour=TERRA, anchor="r")


RULE_C = spec.RULE
STONE_C = spec.STONE


def map_scale(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    p.rect(0.04, 0.20, 0.62, 0.62, lw=0.7, colour=MUTE, fill=HexColor("#F2F5F1"))
    for i in range(1, 6):
        p.line(0.04 + 0.62 * i / 6, 0.20, 0.04 + 0.62 * i / 6, 0.82, 0.3, RULE_C)
        p.line(0.04, 0.20 + 0.62 * i / 6, 0.66, 0.20 + 0.62 * i / 6, 0.3, RULE_C)
    # a "river" and a path
    p.line(0.06, 0.66, 0.66, 0.44, 1.4, HexColor("#8FA9BC"))
    p.line(0.10, 0.30, 0.38, 0.50, 0.8, SLATE, dash=(1.5, 2.5))
    p.line(0.38, 0.50, 0.60, 0.74, 0.8, SLATE, dash=(1.5, 2.5))
    p.dot(0.10, 0.30, 2.2, TERRA)
    p.dot(0.60, 0.74, 2.2, TERRA)
    p.text(0.10, 0.26, "start", 6.2, colour=TERRA, anchor="l")
    p.text(0.60, 0.70, "finish", 6.2, colour=TERRA, anchor="c")
    # scale bar
    p.line(0.72, 0.72, 0.94, 0.72, 1.2, INK)
    p.line(0.72, 0.70, 0.72, 0.74, 1.0, INK)
    p.line(0.94, 0.70, 0.94, 0.74, 1.0, INK)
    p.text(0.83, 0.65, "2 km", 6.4, colour=INK)
    for i, txt in enumerate(("1 cm on the map represents", "0.5 km on the ground.",
                             "", "Scale 1 : 50 000")):
        p.text(0.72, 0.52 + i * 0.09, txt, 6.4, colour=MUTE, anchor="l")
    p.text(0.72, 0.52 + 3 * 0.09, "Scale 1 : 50 000", 6.4, colour=INK, anchor="l",
           font="Inter-Semi")


def proportional_recipe(c, x, y, w, h, base=(12, 600, 450, 90), people=(12, 45)):
    p = Pen(c, x, y, w, h)
    p.rect(0.04, 0.16, 0.42, 0.62, lw=0.7, colour=RULE_C, fill=CREAM_C)
    p.text(0.25, 0.24, f"serves {people[0]}", 7.4, colour=INK, font="Inter-Semi")
    items = ("rice", "lentils", "oil")
    for i, (lab, qty) in enumerate(zip(items, base[1:])):
        p.text(0.08, 0.36 + i * 0.12, f"{lab}  {qty} g", 6.8, colour=SOFT, anchor="l")
    p.arrow(0.50, 0.47, 0.58, 0.47, 1.2, GOLD, head=5)
    p.text(0.54, 0.36, "\u00d7 3.75", 7.2, font="Inter-Semi", colour=GOLD)
    p.rect(0.60, 0.16, 0.36, 0.62, lw=0.7, colour=RULE_C, fill=BLUSH)
    p.text(0.78, 0.24, f"serves {people[1]}", 7.4, colour=INK, font="Inter-Semi")
    for i, (lab, qty) in enumerate(zip(items, base[1:])):
        p.text(0.64, 0.36 + i * 0.12, f"{lab}  {round(qty * 3.75)} g", 6.8,
               colour=SOFT, anchor="l")


CREAM_C = spec.CREAM_SOFT


# ======================================================= 3 · rates
def speed_graph(c, x, y, w, h, pts=((0, 0), (1, 12), (2, 24), (3, 36), (4, 48))):
    p = Pen(c, x, y, w, h)
    u0, v0, u1, v1 = 0.11, 0.84, 0.95, 0.14
    _grid(p, u0, v0, u1, v1, 8, 8, PALE)
    _axis(p, u0, v0, u1, v1, "time (h)", "distance (km)")
    for i in range(5):
        p.text(u0 + (u1 - u0) * i / 4.2, v0 + 0.045, str(i), 6.0, colour=MUTE)
    for i in range(0, 49, 12):
        p.text(u0 - 0.01, v0 - (v0 - v1) * i / 54, str(i), 6.0, colour=MUTE, anchor="r")
    for (t, d) in pts:
        px = u0 + (u1 - u0) * t / 4.2
        py = v0 - (v0 - v1) * d / 54
        p.dot(px, py, 2.1, TERRA)
    px = u0 + (u1 - u0) * 4 / 4.2
    py = v0 - (v0 - v1) * 48 / 54
    p.line(u0, v0, px, py, 1.2, TERRA)
    # slope triangle
    p.line(px - 0.22, py, px, py, 0.7, SLATE, dash=(1.4, 2.6))
    p.line(px - 0.22, py, px - 0.22, v0, 0.7, SLATE, dash=(1.4, 2.6))
    p.text(px - 0.24, (py + v0) / 2, "3 h", 6.2, colour=SLATE, anchor="r")
    p.text(px - 0.11, py - 0.055, "36 km", 6.2, colour=SLATE)
    p.text(0.13, v1 + 0.055, "the gradient is the speed: 12 km per hour", 6.6,
           colour=MUTE, anchor="l", font="SourceSerifItalic")


def price_bars(c, x, y, w, h, packs=(("250 g", 1.60), ("500 g", 2.80),
                                    ("1 kg", 5.20), ("2 kg", 9.20))):
    p = Pen(c, x, y, w, h)
    base = 0.80
    mx = 6.0
    for i, (lab, price) in enumerate(packs):
        uu = 0.12 + i * 0.21
        hh = 0.54 * price / mx
        p.rect(uu, base - hh, 0.13, hh, lw=0.7, colour=INK, fill=MIST)
        p.text(uu + 0.065, base - hh - 0.06, f"\u00a3{price:.2f}", 6.6,
               font="Inter-Semi", colour=TERRA)
        p.text(uu + 0.065, base + 0.06, lab, 6.6, colour=INK)
    p.line(0.10, base, 0.96, base, 0.8, INK)
    p.text(0.10, 0.14, "price of the pack, not the unit price \u2014 "
                       "compare \u00a3 per 100 g", 6.6, colour=MUTE, anchor="l",
           font="SourceSerifItalic")


def flow_rate(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    p.rect(0.06, 0.24, 0.22, 0.52, lw=0.8, colour=INK, fill=PALE)
    p.rect(0.06, 0.24, 0.22, 0.16, lw=0.0, colour=None, fill=HexColor("#C3D3E0"))
    p.text(0.17, 0.62, "tank", 7.0, colour=SLATE)
    p.text(0.17, 0.32, "60 L", 7.4, font="Inter-Semi", colour=SLATE)
    p.arrow(0.30, 0.50, 0.44, 0.50, 1.4, TERRA, head=5)
    p.text(0.37, 0.42, "12 L/min", 6.8, colour=TERRA)
    p.text(0.48, 0.52, "time = capacity \u00f7 rate = 60 \u00f7 12 = 5 minutes",
           7.2, colour=INK, anchor="l")
    p.text(0.48, 0.44, "a rate pairs two different units", 6.6, colour=MUTE,
           anchor="l", font="SourceSerifItalic")


# ======================================================= 4 · integers
def signed_line(c, x, y, w, h, lo=-5, hi=5, marks=(-3, 2), arrows=True):
    p = Pen(c, x, y, w, h)
    v = 0.52
    u0, u1 = 0.06, 0.96
    p.line(u0, v, u1, v, 1.1, INK)
    p.arrow(u1 - 0.03, v, u1 + 0.02, v, 1.1, INK, head=4.5)
    n = hi - lo
    for k in range(lo, hi + 1):
        uu = u0 + (u1 - u0) * (k - lo) / n
        p.line(uu, v - 0.05, uu, v + 0.05, 0.9, INK)
        p.text(uu, v + 0.11, str(k), 6.6, colour=INK if k else TERRA,
               font="Inter-Semi")
    if arrows:
        a, b = marks
        ua = u0 + (u1 - u0) * (a - lo) / n
        ub = u0 + (u1 - u0) * (b - lo) / n
        p.arrow(min(ua, ub), v + 0.26, max(ua, ub), v + 0.26, 1.0, TERRA, head=4.6)
        p.text((ua + ub) / 2, v + 0.34, f"{b - a} steps", 6.4, colour=TERRA)


def thermometer(c, x, y, w, h, temps=(-12, -4, 0, 6, 18)):
    p = Pen(c, x, y, w, h)
    cx = 0.20
    p.rect(cx - 0.022, 0.14, 0.044, 0.70, lw=0.7, colour=INK, fill=CREAM_C, radius=6)
    p.circle(cx, 0.90, 6, colour=INK, fill=CREAM_C)
    for t in range(-20, 41, 10):
        vv = 0.14 + 0.70 * (t + 20) / 60
        p.line(cx + 0.022, vv, cx + 0.038, vv, 0.7, INK)
        p.text(cx + 0.055, vv, f"{t}\u00b0C", 6.2, colour=MUTE, anchor="l")
    for t in temps:
        vv = 0.14 + 0.70 * (t + 20) / 60
        p.line(cx - 0.05, vv, cx - 0.03, vv, 0.9, TERRA)
        p.text(cx - 0.06, vv, f"{t}", 6.6, colour=TERRA, anchor="r",
               font="Inter-Semi")
    p.text(0.52, 0.24, "Above zero the reading rises;", 6.8, colour=SOFT, anchor="l")
    p.text(0.52, 0.32, "below zero it falls further from zero.", 6.8, colour=SOFT,
           anchor="l")
    p.text(0.52, 0.44, "A change from \u22124 to \u221212 is", 6.8, colour=SOFT,
           anchor="l")
    p.text(0.52, 0.52, "a fall of 8 degrees, not a rise.", 6.8, colour=SOFT,
           anchor="l")


def neg_mult_explain(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    # pattern table
    rows = [("\u22122 \u00d7 3", "\u22126"), ("\u22122 \u00d7 2", "\u22124"),
            ("\u22122 \u00d7 1", "\u22122"), ("\u22122 \u00d7 0", "0"),
            ("\u22122 \u00d7 \u22121", "2"), ("\u22122 \u00d7 \u22122", "4")]
    for i, (a, b) in enumerate(rows):
        vv = 0.16 + i * 0.115
        p.text(0.16, vv, a, 7.2, colour=INK, anchor="r")
        p.text(0.20, vv, "=", 7.2, colour=MUTE, anchor="l")
        p.text(0.26, vv, b, 7.2, colour=TERRA if i > 3 else INK, anchor="l",
               font="Inter-Semi")
    p.line(0.10, 0.79, 0.38, 0.79, 0.6, RULE_C)
    p.text(0.40, 0.20, "as the second factor falls by 1,", 6.8, colour=SOFT, anchor="l")
    p.text(0.40, 0.28, "the product rises by 2.", 6.8, colour=SOFT, anchor="l")
    p.text(0.40, 0.40, "Continuing the pattern past zero", 6.8, colour=INK, anchor="l")
    p.text(0.40, 0.48, "forces \u22122 \u00d7 \u22121 = +2: the only value", 6.8,
           colour=INK, anchor="l")
    p.text(0.40, 0.56, "that keeps the step size constant.", 6.8, colour=INK,
           anchor="l")


def integer_chips(c, x, y, w, h, pos=3, neg=5):
    p = Pen(c, x, y, w, h)
    p.text(0.06, 0.20, "Three +1 chips and five \u22121 chips:", 6.8, colour=SOFT,
           anchor="l")
    r = 5.2
    for i in range(pos):
        p.circle(0.14 + i * 0.055, 0.44, r, colour=INK, fill=BLUSH)
        p.text(0.14 + i * 0.055, 0.44, "+", 6.0, colour=TERRA)
    for i in range(neg):
        p.circle(0.44 + i * 0.055, 0.44, r, colour=INK, fill=MIST)
        p.text(0.44 + i * 0.055, 0.44, "\u2212", 6.0, colour=SAGE)
    p.text(0.06, 0.60, "each +1 cancels one \u22121: the pair disappears", 6.8,
           colour=SOFT, anchor="l")
    p.text(0.06, 0.72, "3 + (\u22125) = \u22122", 8.6, font="Inter-Semi", colour=INK,
           anchor="l")


# ======================================================= 5 · algebra
def balance(c, x, y, w, h, left=("x", "x", "x"), right=("6",), mark=None):
    p = Pen(c, x, y, w, h)
    cx, beam = 0.5, 0.30
    p.line(cx, 0.86, cx, beam, 1.2, INK)
    p.poly([(cx - 0.06, 0.94), (cx + 0.06, 0.94), (cx, 0.86)], lw=0.8, colour=INK,
           fill=PALE)
    p.line(0.08, beam, 0.92, beam, 1.4, INK)
    p.circle(cx, beam, 2.0, colour=None, fill=INK)
    for side, items in ((-1, left), (1, right)):
        ex = cx + side * 0.40
        p.line(cx, beam, ex, beam + 0.06, 0.7, INK)
        p.line(ex - 0.10, beam + 0.06, ex + 0.10, beam + 0.06, 1.0, INK)
        n = len(items)
        for i, it in enumerate(items):
            uu = ex - (n - 1) * 0.037 + i * 0.074
            p.rect(uu - 0.030, beam + 0.10, 0.060, 0.13, lw=0.7, colour=INK,
                   fill=BLUSH if it == "x" else MIST)
            p.text(uu, beam + 0.165, it, 7.2, colour=TERRA if it == "x" else SLATE,
                   font="SourceSerifItalic" if it == "x" else "Inter-Semi")
    p.text(cx, beam - 0.10, "the beam is level, so the two pans balance", 6.6,
           colour=MUTE, font="SourceSerifItalic")
    if mark:
        p.text(cx, 0.10, mark, 7.2, colour=INK)


def function_machine(c, x, y, w, h, rule="\u00d7 3 + 1",
                     ins=("1", "2", "3", "4", "5")):
    p = Pen(c, x, y, w, h)
    p.text(0.08, 0.16, "input", 6.4, colour=MUTE)
    p.text(0.44, 0.16, "rule", 6.4, colour=MUTE)
    p.text(0.80, 0.16, "output", 6.4, colour=MUTE)
    p.rect(0.05, 0.24, 0.90, 0.56, lw=0.6, colour=RULE_C, fill=None)
    p.rect(0.36, 0.44, 0.26, 0.20, lw=1.0, colour=INK, fill=BLUSH)
    p.text(0.49, 0.54, rule, 9.0, font="Inter-Semi", colour=TERRA)
    for i, s in enumerate(ins):
        vv = 0.32 + i * 0.09
        p.text(0.13, vv, s, 7.0, colour=INK)
        out = i + 1
        p.text(0.80, vv, str(3 * out + 1), 7.0, colour=SLATE, font="Inter-Semi")
        p.arrow(0.18, vv, 0.35, 0.54, 0.5, MUTE, head=3.2)
        p.arrow(0.63, 0.54, 0.76, vv, 0.5, MUTE, head=3.2)


def algebra_tiles(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    p.text(0.05, 0.12, "collection of tiles", 6.4, colour=MUTE, anchor="l")
    uu = 0.05
    for i in range(3):
        p.rect(uu, 0.30, 0.10, 0.34, lw=0.8, colour=INK, fill=BLUSH)
        p.text(uu + 0.05, 0.47, "x", 8.4, colour=TERRA, font="SourceSerifItalic")
        uu += 0.105
    for i in range(4):
        p.rect(uu, 0.30, 0.055, 0.055, lw=0.8, colour=INK, fill=MIST)
        p.text(uu + 0.0275, 0.328, "1", 6.4, colour=SAGE)
        uu += 0.062
    for i in range(2):
        p.rect(uu, 0.52, 0.10, 0.34, lw=0.8, colour=INK, fill=BLUSH, dash=(2, 2))
        p.text(uu + 0.05, 0.69, "\u2212x", 7.6, colour=RUST)
        uu += 0.105
    p.text(0.05, 0.84, "3x + 4 \u2212 2x  =  x + 4", 9.4, font="Inter-Semi", colour=INK,
           anchor="l")
    p.text(0.05, 0.94, "like tiles cancel: the collection simplifies without changing "
                       "its value", 6.4, colour=MUTE, anchor="l")


def number_trick(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    steps = ["Think of a number", "Add 5", "Double it", "Subtract 4",
             "Halve it", "Subtract your number"]
    for i, s in enumerate(steps):
        vv = 0.12 + i * 0.145
        p.rect(0.05, vv - 0.05, 0.44, 0.11, lw=0.6, colour=RULE_C, fill=STONE_C)
        p.text(0.08, vv + 0.005, s, 6.8, colour=INK, anchor="l")
        p.text(0.55, vv + 0.005, ["n", "n + 5", "2n + 10", "2n + 6", "n + 3", "3"][i],
               7.2, colour=TERRA, anchor="l", font="SourceSerifItalic")
    p.line(0.52, 0.10, 0.52, 0.94, 0.5, RULE_C)
    p.text(0.60, 0.10, "the answer is always 3", 7.0, colour=MUTE, anchor="l",
           font="SourceSerifItalic")


# ======================================================= 6 · patterns
def staircase(c, x, y, w, h, ns=(1, 2, 3, 4, 5)):
    p = Pen(c, x, y, w, h)
    side = 11.0
    su, sv = side / w, side / h
    gap = 15.0 / w
    total = sum(n * su for n in ns) + gap * (len(ns) - 1)
    u = (1.0 - total) / 2.0
    base = 0.70
    for n in ns:
        for r in range(n):
            for k in range(r + 1):
                p.rect(u + k * su, base - n * sv + r * sv, su, sv, lw=0.6,
                       colour=MUTE, fill=BLUSH if (r + k) % 2 else MIST)
        p.text(u + n * su / 2.0, 0.765, str((n * (n + 1)) // 2), 6.8,
               colour=TERRA, font="Inter-Semi")
        p.text(u + n * su / 2.0, 0.805, f"n = {n}", 6.0, colour=MUTE)
        u += n * su + gap
    p.text(0.5, 0.11, "each staircase adds one more square than the last",
           6.5, colour=SOFT, font="SourceSerifItalic")


def matchstick_pattern(c, x, y, w, h, ns=(1, 2, 3, 4)):
    p = Pen(c, x, y, w, h)
    side = 12.0
    su, sv = side / w, side / h
    gap = 20.0 / w
    total = sum(n * su for n in ns) + gap * (len(ns) - 1)
    u = (1.0 - total) / 2.0
    base = 0.72
    for n in ns:
        for k in range(n):
            p.rect(u + k * su, base - sv, su, sv, lw=1.0, colour=INK)
        cx = u + n * su / 2.0
        p.text(cx, base + 0.085, f"{4 + 3 * (n - 1)} sticks", 6.6, colour=TERRA,
               font="Inter-Semi")
        p.text(cx, base + 0.14, f"n = {n}", 6.0, colour=MUTE)
        u += n * su + gap
    p.text(0.5, 0.10, "4 sticks for the first square, 3 more for each extra square",
           6.5, colour=SOFT, font="SourceSerifItalic")


def sequence_graph(c, x, y, w, h, terms=(4, 7, 10, 13, 16, 19)):
    p = Pen(c, x, y, w, h)
    u0, v0, u1, v1 = 0.13, 0.82, 0.95, 0.14
    p.line(u0, v0, u1, v0, 0.9, INK)
    p.line(u0, v0, u0, v1, 0.9, INK)
    p.line(u1 - 0.03, v0, u1, v0, 0.9, INK)
    p.text((u0 + u1) / 2.0, v0 + 0.115, "term number, n", 6.4, colour=MUTE)
    p.text(u0 - 0.02, v1 - 0.055, "term value", 6.4, colour=MUTE, anchor="l")
    nmax = len(terms) + 0.7
    ymax = max(terms) * 1.12
    for i, t in enumerate(terms):
        px = u0 + (u1 - u0) * ((i + 1) / nmax)
        py = v0 - (v0 - v1) * (t / ymax)
        p.dot(px, py, 2.4, TERRA)
        p.text(px - 0.016, py + 0.012, str(t), 6.0, colour=MUTE, anchor="r")
        p.text(px, v0 + 0.055, str(i + 1), 6.0, colour=MUTE)
    p.line(u0 + (u1 - u0) * (1 / nmax), v0 - (v0 - v1) * (terms[0] / ymax),
           u0 + (u1 - u0) * (len(terms) / nmax),
           v0 - (v0 - v1) * (terms[-1] / ymax), 0.6, TERRA, dash=(1.6, 3.0))
    p.text(u0 + 0.03, 0.955, "the points lie on a straight line: each step adds the "
                             "same amount", 6.4, colour=SOFT, anchor="l",
           font="SourceSerifItalic")


def lantern_arch(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    base = 0.86
    p.line(0.02, base, 0.98, base, 1.0, INK)
    pts = []
    for i in range(0, 41):
        t = i / 40
        uu = 0.06 + t * 0.88
        vv = 0.30 + 0.52 * (2 * t - 1) ** 2
        pts.append((uu, vv))
    for i in range(len(pts) - 1):
        p.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], 1.1, TERRA)
    for k in range(1, 9):
        t = k / 9
        uu = 0.06 + t * 0.88
        vv = 0.30 + 0.52 * (2 * t - 1) ** 2
        p.line(uu, vv, uu, base, 0.5, MUTE, dash=(1.2, 2.6))
        p.circle(uu, vv + 0.045, 3.2, colour=GOLD, fill=BLUSH)
    p.text(0.50, 0.14, "the arch is a curve, but the lantern posts stand at equally "
                       "spaced points", 6.4, colour=MUTE, font="SourceSerifItalic")


# ======================================================= 7 · 2D geometry
def parallel_transversal(c, x, y, w, h):
    """Two parallel lines cut by a transversal, with the eight angles labelled."""
    p = Pen(c, x, y, w, h)
    v1, v2 = 0.34, 0.68
    u1 = 0.30 + 0.34 * v1
    u2 = 0.30 + 0.34 * v2
    p.line(0.04, v1, 0.94, v1, 1.1, INK)
    p.line(0.04, v2, 0.94, v2, 1.1, INK)
    p.line(0.30 + 0.34 * 0.14, 0.14, 0.30 + 0.34 * 0.86, 0.86, 1.0, SLATE)
    p.text(0.86, v1 - 0.045, "\u2113", 7.4, colour=INK, font="SourceSerifItalic")
    p.text(0.86, v2 - 0.045, "m", 7.4, colour=INK, font="SourceSerifItalic")
    p.text(0.30 + 0.34 * 0.86 + 0.02, 0.85, "t", 7.4, colour=SLATE,
           font="SourceSerifItalic")
    dx, dy = 0.062, 0.075
    lab = [("a", u1, v1, -1, -1), ("b", u1, v1, +1, -1),
           ("c", u1, v1, -1, +1), ("d", u1, v1, +1, +1),
           ("e", u2, v2, -1, -1), ("f", u2, v2, +1, -1),
           ("g", u2, v2, -1, +1), ("h", u2, v2, +1, +1)]
    for name, u, v, sx, sy in lab:
        p.text(u + sx * dx, v + sy * dy, name, 7.2, colour=TERRA,
               font="SourceSerifItalic")
    p.text(0.5, 0.965, "a, d, e, h are equal   \u00b7   b, c, f, g are equal   "
                       "\u00b7   a + b = 180\u00b0", 6.4, colour=MUTE)


def triangle_angles(c, x, y, w, h, a=52, b=61, c_=67):
    import math
    p = Pen(c, x, y, w, h)
    A = (0.12, 0.80)
    B = (0.86, 0.80)
    # place C using the base angles
    ra = math.radians(a)
    rb = math.radians(180 - b)
    # lines from A and B at angles a and 180-b
    x1, y1 = A
    x2, y2 = B
    m1 = -math.tan(ra) * (w / h)
    m2 = math.tan(math.radians(b)) * (w / h)
    xc = (y2 - y1 + m1 * x1 - m2 * x2 * (h / h)) / (m1 - m2) if False else 0
    # simpler: solve in unit space with y upward
    Ay = 1 - A[1]
    By = 1 - B[1]
    t1 = math.tan(ra)
    t2 = math.tan(math.radians(b))
    xc = (t1 * x1 + t2 * x2 + (By - Ay)) / (t1 + t2)
    yc = Ay + t1 * (xc - x1)
    C = (xc, 1 - yc)
    p.poly([A, B, C], lw=1.1, colour=INK, fill=HexColor("#FAF7EF"))
    p.text(A[0] + 0.075, A[1] - 0.055, f"{a}\u00b0", 6.8, colour=TERRA)
    p.text(B[0] - 0.075, B[1] - 0.055, f"{b}\u00b0", 6.8, colour=TERRA)
    p.text(C[0], C[1] + 0.075, f"{c_}\u00b0", 6.8, colour=TERRA)
    p.arc(A[0], A[1], 16, -a, a, 0.6, TERRA)
    p.arc(B[0], B[1], 16, 180, b, 0.6, TERRA)
    p.arc(C[0], C[1], 14, 200, c_, 0.6, TERRA)
    p.text(0.5, 0.94, "the three angles of a triangle always total 180\u00b0", 6.4,
           colour=MUTE, font="SourceSerifItalic")


def polygon_dissection(c, x, y, w, h, n=6):
    import math
    p = Pen(c, x, y, w, h)
    cx, cy, r = 0.5, 0.52, 0.36
    pts = []
    for i in range(n):
        ang = math.pi / 2 + 2 * math.pi * i / n
        pts.append((cx + r * math.cos(ang) * (w / h if False else 1.0),
                    cy - r * math.sin(ang)))
    p.poly(pts, lw=1.2, colour=INK, fill=HexColor("#FAF7EF"))
    for pt in pts[1:]:
        p.line(cx, cy, pt[0], pt[1], 0.6, SLATE, dash=(1.4, 2.6))
    for pt in pts:
        p.dot(pt[0], pt[1], 1.8, INK)
    p.text(0.5, 0.08, f"a hexagon splits into {n - 2} triangles: "
                      f"{n - 2} \u00d7 180\u00b0 = {(n - 2) * 180}\u00b0", 6.4,
           colour=MUTE, font="SourceSerifItalic")


def circle_parts(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    cx, cy, r = 0.44, 0.50, 0.30
    p.circle(cx, cy, r * w, colour=INK, lw=1.1, fill=HexColor("#FAF7EF"))
    p.circle(cx, cy, 1.6, colour=None, fill=INK)
    p.line(cx, cy, cx + r, cy, 0.8, TERRA)
    p.text(cx + r / 2, cy - 0.05, "r", 7.6, colour=TERRA, font="SourceSerifItalic")
    p.line(cx - r, cy, cx + r, cy, 0.7, SLATE, dash=(1.6, 3.0))
    p.text(cx - r - 0.02, cy - 0.05, "d = 2r", 6.8, colour=SLATE, anchor="r")
    p.arc(cx, cy, r * w * 0.55, 10, 66, 0.9, GOLD)
    p.text(cx + 0.17, cy - 0.20, "arc", 6.4, colour=GOLD, anchor="l")
    p.text(0.06, 0.10, "C = \u03c0d = 2\u03c0r", 7.2, colour=INK, anchor="l",
           font="SourceSerifItalic")
    p.text(0.06, 0.19, "A = \u03c0r\u00b2", 7.2, colour=INK, anchor="l",
           font="SourceSerifItalic")
    p.text(0.06, 0.88, "circumference and area both depend", 6.4,
           colour=MUTE, anchor="l")
    p.text(0.06, 0.94, "on the radius alone", 6.4, colour=MUTE, anchor="l")


def composite_area(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    pts = [(0.10, 0.24), (0.62, 0.24), (0.62, 0.52), (0.86, 0.52), (0.86, 0.78),
           (0.10, 0.78)]
    p.poly(pts, lw=1.1, colour=INK, fill=HexColor("#FAF7EF"))
    p.line(0.10, 0.52, 0.62, 0.52, 0.6, SLATE, dash=(2.0, 3.0))
    p.text(0.36, 0.86, "9 m", 6.8, colour=INK)
    p.text(0.36, 0.47, "5 m", 6.6, colour=SLATE)
    p.text(0.06, 0.50, "4 m", 6.6, colour=INK, anchor="r")
    p.text(0.70, 0.62, "3 m", 6.6, colour=INK, anchor="l")
    p.text(0.10, 0.16, "split it into rectangles, or subtract the missing rectangle",
           6.4, colour=MUTE, anchor="l", font="SourceSerifItalic")


def quadrilateral_row(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    shapes = [
        ("square", [(0, 0), (1, 0), (1, 1), (0, 1)]),
        ("rectangle", [(0, 0), (1.3, 0), (1.3, 0.8), (0, 0.8)]),
        ("parallelogram", [(0.15, 0), (1.35, 0), (1.2, 0.8), (0, 0.8)]),
        ("trapezium", [(0.10, 0), (1.10, 0), (1.35, 0.8), (-0.05, 0.8)]),
        ("kite", [(0.5, 0), (1.05, 0.45), (0.5, 1.0), (-0.05, 0.45)]),
        ("rhombus", [(0.5, 0), (1.15, 0.5), (0.5, 1.0), (-0.15, 0.5)]),
    ]
    slot = 0.165
    for i, (name, pts) in enumerate(shapes):
        u0 = 0.03 + i * slot
        sc = 0.11
        v0 = 0.46
        pp = [(u0 + a * sc, v0 + b * sc * 0.9) for a, b in pts]
        p.poly(pp, lw=0.9, colour=INK, fill=HexColor("#FAF7EF"))
        p.text(u0 + 0.055, v0 + 0.30, name, 6.2, colour=INK)
    p.text(0.03, 0.90, "one family, different constraints: every one of these has four "
                       "sides", 6.4, colour=MUTE, anchor="l",
           font="SourceSerifItalic")


def angle_sum_demo(c, x, y, w, h):
    """The three angles of a triangle laid along a straight line."""
    p = Pen(c, x, y, w, h)
    p.line(0.05, 0.70, 0.95, 0.70, 1.0, INK)
    cols = (BLUSH, MIST, HexColor("#EDE6F0"))
    labels = ("a", "b", "c")
    u = 0.14
    for i, ang in enumerate((62, 54, 64)):
        uu = u
        p.arc(uu, 0.70, 0.17, 180 - ang if i == 0 else 180 - ang, ang, 0.9, INK)
        p.text(uu - 0.02, 0.60, labels[i], 7.0, colour=INK)
        u += 0.26
    p.text(0.05, 0.86, "the three angles, placed side by side, make a straight line: "
                       "180\u00b0", 6.4, colour=MUTE, anchor="l",
           font="SourceSerifItalic")
    p.poly([(0.62, 0.86), (0.80, 0.86), (0.74, 0.76)], lw=0.8, colour=INK,
           fill=HexColor("#FAF7EF"))


# ======================================================= 8 · solids
def cuboid(c, x, y, w, h, dims=("l", "w", "h")):
    p = Pen(c, x, y, w, h)
    dx, dy = 0.16, 0.13
    u0, v0, wu, hv = 0.14, 0.62, 0.48, 0.34
    front = [(u0, v0), (u0 + wu, v0), (u0 + wu, v0 - hv), (u0, v0 - hv)]
    p.poly(front, lw=1.0, colour=INK, fill=HexColor("#FAF7EF"))
    p.poly([(u0 + dx, v0 - dy), (u0 + dx + wu, v0 - dy),
            (u0 + dx + wu, v0 - dy - hv), (u0 + dx, v0 - dy - hv)], lw=0.7,
           colour=MUTE, dash=(2.2, 3.0))
    p.line(u0, v0, u0 + dx, v0 - dy, 0.9, INK)
    p.line(u0 + wu, v0, u0 + wu + dx, v0 - dy, 0.9, INK)
    p.line(u0, v0 - hv, u0 + dx, v0 - hv - dy, 0.9, INK)
    p.line(u0 + wu, v0 - hv, u0 + wu + dx, v0 - hv - dy, 0.9, INK)
    p.poly([(u0, v0 - hv), (u0 + dx, v0 - hv - dy), (u0 + dx + wu, v0 - hv - dy),
            (u0 + wu, v0 - hv)], lw=0.9, colour=INK, fill=MIST)
    p.poly([(u0 + wu, v0), (u0 + wu + dx, v0 - dy),
            (u0 + wu + dx, v0 - dy - hv), (u0 + wu, v0 - hv)], lw=0.9, colour=INK,
           fill=BLUSH)
    p.text(u0 + wu / 2, v0 + 0.06, dims[0], 7.0, colour=INK)
    p.text(u0 - 0.03, v0 - hv / 2, dims[2], 7.0, colour=INK, anchor="r")
    p.text(u0 + wu + dx + 0.03, v0 - hv / 2 - dy / 2, dims[1], 7.0, colour=INK,
           anchor="l")


def prism_net(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    u0, v0 = 0.10, 0.30
    a, b, cw = 0.20, 0.16, 0.30
    # central rectangle (side), then top/bottom (b x cw) and two ends
    p.rect(u0, v0, cw, a, lw=0.9, colour=INK, fill=HexColor("#FAF7EF"))
    p.rect(u0, v0 - b, cw, b, lw=0.9, colour=INK, fill=MIST)
    p.rect(u0, v0 + a, cw, b, lw=0.9, colour=INK, fill=MIST)
    p.rect(u0 - b, v0, b, a, lw=0.9, colour=INK, fill=BLUSH)
    p.rect(u0 + cw, v0, b, a, lw=0.9, colour=INK, fill=BLUSH)
    p.text(u0 + cw / 2, v0 + a / 2, "side", 6.6, colour=INK)
    p.text(u0 + cw / 2, v0 - b / 2, "top", 6.6, colour=SLATE)
    p.text(u0 + cw / 2, v0 + a + b / 2, "base", 6.6, colour=SLATE)
    p.text(u0 - b / 2, v0 + a / 2, "end", 6.4, colour=TERRA)
    p.text(u0 + cw + b / 2, v0 + a / 2, "end", 6.4, colour=TERRA)
    p.text(0.10, 0.90, "the net shows every face once: add their areas for the surface "
                       "area", 6.4, colour=MUTE, anchor="l", font="SourceSerifItalic")


def cylinder_net(c, x, y, w, h):
    """The net of a cylinder: one curved rectangle and two circular ends."""
    p = Pen(c, x, y, w, h)
    u0, v0, rw, rh = 0.14, 0.42, 0.56, 0.26
    p.rect(u0, v0, rw, rh, lw=1.0, colour=INK, fill=HexColor("#FAF7EF"))
    p.text(u0 + rw / 2, v0 + rh / 2 - 0.02, "curved surface", 6.8, colour=INK)
    p.text(u0 + rw / 2, v0 + rh / 2 + 0.055, "2\u03c0r \u00d7 h", 6.8, colour=INTER_TXT)
    rad = min(0.075 * w, 0.11 * h)
    p.circle(u0 + 0.045, v0 - 0.16, rad, colour=INK, lw=0.9, fill=MIST)
    p.circle(u0 + rw - 0.045, v0 - 0.16, rad, colour=INK, lw=0.9, fill=MIST)
    p.text(u0 + rw / 2, v0 - 0.15, "two circular ends", 6.4, colour=SOFT)
    p.line(u0, v0 + rh + 0.05, u0 + rw, v0 + rh + 0.05, 0.5, MUTE)
    p.text(u0 + rw / 2, v0 + rh + 0.085, "2\u03c0r", 6.4, colour=MUTE)
    p.line(u0 + rw + 0.04, v0, u0 + rw + 0.04, v0 + rh, 0.5, MUTE)
    p.text(u0 + rw + 0.06, v0 + rh / 2, "h", 6.8, colour=MUTE, anchor="l")


def composite_solid(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    p.rect(0.10, 0.62, 0.50, 0.24, lw=1.0, colour=INK, fill=HexColor("#FAF7EF"))
    p.rect(0.36, 0.38, 0.24, 0.48, lw=1.0, colour=INK, fill=MIST)
    p.text(0.22, 0.74, "2 m", 6.4, colour=INK)
    p.text(0.30, 0.50, "1 m", 6.2, colour=INK, anchor="l")
    p.text(0.10, 0.86, "an L-shaped solid = two prisms added, then overlaps removed",
           6.4, colour=MUTE, anchor="l", font="SourceSerifItalic")


def tank_sketch(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    p.rect(0.16, 0.24, 0.34, 0.52, lw=1.0, colour=INK, fill=HexColor("#FAF7EF"))
    p.rect(0.16, 0.24, 0.34, 0.36, lw=0.0, colour=None, fill=HexColor("#CFDDE8"))
    p.text(0.33, 0.42, "water", 6.6, colour=SLATE)
    p.text(0.33, 0.90, "60 cm", 6.6, colour=INK)
    p.text(0.13, 0.50, "40 cm", 6.4, colour=INK, anchor="r")
    p.text(0.33, 0.16, "capacity in litres = volume in cm\u00b3 \u00f7 1000", 6.4,
           colour=MUTE)


# ======================================================= 9 · transformations
def grid_square(c, x, y, w, h, n=8):
    p = Pen(c, x, y, w, h)
    _grid(p, 0.04, 0.06, 0.96, 0.94, n, n, PALE, 0.5)
    p.line(0.04, 0.06, 0.96, 0.06, 0.8, INK)
    p.line(0.04, 0.06, 0.04, 0.94, 0.8, INK)
    return p


def translation_demo(c, x, y, w, h):
    p = grid_square(c, x, y, w, h, 10)
    sq = [(0.14, 0.66), (0.30, 0.66), (0.30, 0.82), (0.14, 0.82)]
    p.poly(sq, lw=1.1, colour=INK, fill=BLUSH)
    d = (0.40, 0.14)
    sq2 = [(a + d[0], b + d[1]) for a, b in sq]
    p.poly(sq2, lw=1.1, colour=TERRA, fill=MIST)
    for a, b in zip(sq, sq2):
        p.arrow(a[0] + 0.005, a[1] - 0.005, b[0] - 0.005, b[1] + 0.005, 0.6, GOLD,
                head=3.4, dash=(1.4, 2.4))
    p.text(0.46, 0.28, "translation: every point moves the same distance", 6.4,
           colour=MUTE, font="SourceSerifItalic")


def reflection_demo(c, x, y, w, h):
    p = grid_square(x=x, y=y, w=w, h=h, c=c, n=10) if False else grid_square(c, x, y, w, h, 10)
    p.line(0.50, 0.06, 0.50, 0.94, 1.0, SLATE, dash=(2.4, 3.0))
    p.text(0.52, 0.90, "mirror line", 6.2, colour=SLATE, anchor="l")
    tri = [(0.16, 0.70), (0.38, 0.70), (0.16, 0.40)]
    p.poly(tri, lw=1.1, colour=INK, fill=BLUSH)
    tri2 = [(1.0 - a, b) for a, b in tri]
    p.poly(tri2, lw=1.1, colour=TERRA, fill=MIST)
    for a, b in zip(tri, tri2):
        p.line(a[0], a[1], b[0], b[1], 0.45, GOLD, dash=(1.2, 2.4))
    p.text(0.22, 0.30, "each vertex is as far behind the mirror as in front", 6.2,
           colour=MUTE)


def rotation_demo(c, x, y, w, h):
    p = grid_square(c, x, y, w, h, 10)
    cx, cy = 0.50, 0.50
    p.dot(cx, cy, 2.4, TERRA)
    p.text(cx + 0.02, cy + 0.055, "centre", 6.2, colour=TERRA, anchor="l")
    tri = [(0.56, 0.50), (0.80, 0.50), (0.56, 0.30)]
    p.poly(tri, lw=1.1, colour=INK, fill=BLUSH)
    tri2 = [(cx + (cy - b), cy + (a - cx)) for a, b in tri]
    p.poly(tri2, lw=1.1, colour=TERRA, fill=MIST)
    p.arc(cx, cy, 0.28 * w, 0, 90, 0.8, GOLD)
    p.text(cx + 0.20, cy - 0.20, "90\u00b0", 6.4, colour=GOLD)


def enlargement_demo(c, x, y, w, h):
    p = grid_square(c, x, y, w, h, 10)
    small = [(0.16, 0.76), (0.32, 0.76), (0.32, 0.62), (0.16, 0.62)]
    p.poly(small, lw=1.0, colour=INK, fill=BLUSH)
    big = [(0.16, 0.76), (0.64, 0.76), (0.64, 0.20), (0.16, 0.20)]
    p.poly(big, lw=1.0, colour=TERRA, fill=None, dash=(2.2, 3.0))
    p.dot(0.16, 0.76, 2.4, GOLD)
    p.text(0.18, 0.80, "centre of enlargement", 6.2, colour=GOLD, anchor="l")
    for a, b in ((0.32, 0.76), (0.32, 0.62)):
        p.line(0.16, 0.76, a + (a - 0.16) * 2.0, 0.76 + (b - 0.76) * 3.0, 0.5, GOLD,
               dash=(1.2, 2.4))
    p.text(0.66, 0.40, "scale factor 3:", 6.2, colour=TERRA, anchor="l")
    p.text(0.66, 0.46, "sides \u00d7 3,", 6.2, colour=TERRA, anchor="l")
    p.text(0.66, 0.52, "area \u00d7 9", 6.2, colour=TERRA, anchor="l")


def tessellation(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    import math
    s = 0.075
    for row in range(7):
        for col in range(13):
            u0 = 0.03 + col * s * 2 + (s if row % 2 else 0)
            v0 = 0.10 + row * s * 1.74
            p.poly([(u0, v0), (u0 + s, v0 - s * 0.58), (u0 + 2 * s, v0),
                    (u0 + s, v0 + s * 0.58)], lw=0.55,
                   colour=SLATE if (row + col) % 3 else TERRA,
                   fill=[MIST, BLUSH, HexColor("#F2F4F7")][(row * 2 + col) % 3])


def symmetry_shapes(c, x, y, w, h):
    """Six quadrilaterals and polygons in two rows, mirror lines dashed."""
    import math
    p = Pen(c, x, y, w, h)
    W = float(w)
    H = float(h)
    cw, ch = W / 3.0, H / 2.0
    size = min(44.0, cw * 0.42)
    shapes = ["square", "equilateral triangle", "regular pentagon",
              "isosceles trapezium", "kite", "parallelogram"]
    counts = {"square": 4, "equilateral triangle": 3, "regular pentagon": 5,
              "isosceles trapezium": 1, "kite": 1, "parallelogram": 0}
    for i, name in enumerate(shapes):
        col, row = i % 3, i // 3
        cx = col * cw + cw / 2.0
        cy = row * ch + 12.0 + size / 2.0
        if name == "square":
            pts = [(cx - size / 2, cy - size / 2), (cx + size / 2, cy - size / 2),
                   (cx + size / 2, cy + size / 2), (cx - size / 2, cy + size / 2)]
        elif name == "equilateral triangle":
            pts = [(cx, cy - size / 1.7),
                   (cx + size / 1.55, cy + size / 3.0),
                   (cx - size / 1.55, cy + size / 3.0)]
        elif name == "regular pentagon":
            pts = [(cx + size * 0.62 * math.cos(math.pi / 2 + 2 * math.pi * k / 5),
                    cy - size * 0.62 * math.sin(math.pi / 2 + 2 * math.pi * k / 5))
                   for k in range(5)]
        elif name == "isosceles trapezium":
            pts = [(cx - size * 0.55, cy + size * 0.35),
                   (cx + size * 0.55, cy + size * 0.35),
                   (cx + size * 0.30, cy - size * 0.35),
                   (cx - size * 0.30, cy - size * 0.35)]
        elif name == "kite":
            pts = [(cx, cy - size * 0.55), (cx + size * 0.40, cy),
                   (cx, cy + size * 0.55), (cx - size * 0.40, cy)]
        else:
            pts = [(cx - size * 0.35, cy + size * 0.35),
                   (cx + size * 0.55, cy + size * 0.35),
                   (cx + size * 0.35, cy - size * 0.35),
                   (cx - size * 0.55, cy - size * 0.35)]
        p.poly([(u / W, v / H) for u, v in pts], lw=0.9, colour=INK,
               fill=HexColor("#FAF7EF"))
        n = counts[name]
        for k in range(n):
            ang = math.pi * k / n + (math.pi / 2 if n % 2 else 0) * 0
            dx = math.cos(ang) * size * 0.78
            dy = math.sin(ang) * size * 0.78
            p.line((cx - dx) / W, (cy - dy) / H, (cx + dx) / W, (cy + dy) / H,
                   0.5, TERRA, dash=(1.4, 2.4))
        lab = ("no line of symmetry" if n == 0 else
               ("1 line of symmetry" if n == 1 else f"{n} lines of symmetry"))
        p.text(cx / W, (cy + size * 0.62 + 13) / H, name, 6.0, colour=INK)
        p.text(cx / W, (cy + size * 0.62 + 22) / H, lab, 5.7, colour=TERRA)


# ======================================================= 10 · probability
def tree_diagram(c, x, y, w, h, first=("H", "T"), second=("H", "T")):
    p = Pen(c, x, y, w, h)
    root = (0.08, 0.50)
    mids = [(0.42, 0.24), (0.42, 0.76)]
    ends = [(0.86, 0.12), (0.86, 0.36), (0.86, 0.64), (0.86, 0.88)]
    p.dot(*root, 2.6, INK)
    p.text(root[0] - 0.01, root[1] - 0.07, "start", 6.2, colour=MUTE, anchor="l")
    for i, m in enumerate(mids):
        p.line(root[0], root[1], m[0], m[1], 0.9, INK)
        p.text((root[0] + m[0]) / 2, (root[1] + m[1]) / 2 - 0.05, first[i], 7.2,
               colour=TERRA, font="Inter-Semi")
        p.dot(*m, 2.2, INK)
    for i, m in enumerate(mids):
        for j in range(2):
            e = ends[i * 2 + j]
            p.line(m[0], m[1], e[0], e[1], 0.8, INK)
            p.text((m[0] + e[0]) / 2, (m[1] + e[1]) / 2 - 0.05, second[j], 7.2,
                   colour=SAGE, font="Inter-Semi")
            p.dot(*e, 2.0, INK)
            p.text(e[0] + 0.02, e[1], f"{first[i]}{second[j]}", 7.2, colour=INK,
                   anchor="l", font="Inter-Semi")
    p.text(0.02, 0.94, "two independent events: multiply along the branches, add the "
                       "outcomes you want", 6.4, colour=MUTE, anchor="l",
           font="SourceSerifItalic")


def sample_grid(c, x, y, w, h, n=6):
    """A 6 x 6 sample-space grid for two dice, one cell per pair of scores."""
    p = Pen(c, x, y, w, h)
    cell = min(26.0, 0.74 * w / n, 0.72 * h / n)
    cw, chh = cell / w, cell / h
    grid_w, grid_h = n * cw, n * chh
    u0 = (1.0 - grid_w) / 2.0
    v0 = 0.14
    for i in range(n):
        p.text(u0 + i * cw + cw / 2, v0 - 0.045, str(i + 1), 6.2, colour=MUTE)
        p.text(u0 - 0.018, v0 + i * chh + chh / 2, str(i + 1), 6.2, colour=MUTE,
               anchor="r")
        for j in range(n):
            tot = i + j + 2
            p.rect(u0 + i * cw, v0 + j * chh, cw, chh, lw=0.4, colour=RULE_C,
                   fill=MIST if tot == 7 else None)
            p.text(u0 + i * cw + cw / 2, v0 + j * chh + chh / 2, str(tot), 6.0,
                   colour=TERRA if tot == 7 else SOFT)
    p.text(u0 + grid_w / 2, 0.975,
           "die 1 across, die 2 down \u00b7 the six ways to make 7 are shaded",
           6.2, colour=MUTE, font="SourceSerifItalic")


def spinner(c, x, y, w, h, sectors=(("red", 3), ("blue", 2), ("gold", 1))):
    import math
    p = Pen(c, x, y, w, h)
    cx, cy, r = 0.38, 0.50, 0.30
    total = sum(n for _, n in sectors)
    a0 = 90
    for name, n in sectors:
        ext = 360 * n / total
        c.saveState()
        c.setStrokeColor(INK)
        c.setLineWidth(0.8)
        col = {"red": BLUSH, "blue": MIST, "gold": SAND}.get(name, MIST)
        c.setFillColor(col)
        c.wedge(cx * w + x - r * w, cy * h + y - r * h, cx * w + x + r * w,
                cy * h + y + r * h, a0, ext, stroke=1, fill=1)
        c.restoreState()
        mid = math.radians(a0 + ext / 2)
        p.text(cx + 0.17 * math.cos(mid), cy - 0.17 * math.sin(mid) * (h / w) * (w / h),
               name, 6.2, colour=INK)
        a0 += ext
    p.dot(cx, cy, 2.2, INK)
    ly = 0.14
    for name, n in sectors:
        p.text(0.74, ly, f"{name}: {n}/{total}", 6.4, colour=SOFT, anchor="l")
        ly -= 0.10


def bar_frequency(c, x, y, w, h, labels=("1", "2", "3", "4", "5", "6"),
                  values=(7, 9, 6, 8, 10, 10)):
    p = Pen(c, x, y, w, h)
    base = 0.86
    mx = max(values) * 1.15
    bw = 0.80 / len(values)
    for i, (lab, v) in enumerate(zip(labels, values)):
        hh = 0.62 * v / mx
        p.rect(0.08 + i * bw + 0.012, base - hh, bw - 0.024, hh, lw=0.7, colour=INK,
               fill=MIST)
        p.text(0.08 + i * bw + bw / 2, base - hh - 0.05, str(v), 6.2, colour=TERRA,
               font="Inter-Semi")
        p.text(0.08 + i * bw + bw / 2, base + 0.055, lab, 6.2, colour=MUTE)
    p.line(0.08, base, 0.90, base, 0.8, INK)
    p.line(0.08, base, 0.08, 0.16, 0.8, INK)
    p.text(0.065, 0.13, "frequency", 6.2, colour=MUTE, anchor="r")
    p.text(0.49, 0.99, "score on the die", 6.2, colour=MUTE)


# ======================================================= 11 · data
def dot_plot(c, x, y, w, h, data=(3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 9),
             lo=2, hi=10):
    p = Pen(c, x, y, w, h)
    base = 0.78
    p.line(0.05, base, 0.95, base, 0.9, INK)
    counts = {}
    for d in data:
        counts[d] = counts.get(d, 0) + 1
    for k in range(lo, hi + 1):
        uu = 0.05 + 0.90 * (k - lo) / (hi - lo)
        p.line(uu, base, uu, base - 0.04, 0.6, INK)
        p.text(uu, base + 0.055, str(k), 6.2, colour=MUTE)
        for j in range(counts.get(k, 0)):
            p.dot(uu, base - 0.07 - j * 0.062, 2.4, SLATE)
    p.text(0.5, 0.12, "each dot is one value; the shape shows where the data cluster",
           6.4, colour=MUTE, font="SourceSerifItalic")


def box_plot_pair(c, x, y, w, h, a=(2, 4, 6, 9, 12), b=(5, 7, 9, 12, 18)):
    p = Pen(c, x, y, w, h)
    mx = max(a[-1], b[-1]) * 1.10
    rows = (("class A", a, MIST, SAGE, 0.34), ("class B", b, BLUSH, TERRA, 0.64))
    for name, q, fill, col, v in rows:
        lo, q1, med, q3, hi = q
        u = lambda t: 0.22 + 0.70 * t / mx
        p.line(u(lo), v, u(hi), v, 0.8, INK)
        p.line(u(lo), v - 0.045, u(lo), v + 0.045, 0.8, INK)
        p.line(u(hi), v - 0.045, u(hi), v + 0.045, 0.8, INK)
        p.rect(u(q1), v - 0.075, u(q3) - u(q1), 0.15, lw=0.9, colour=INK, fill=fill)
        p.line(u(med), v - 0.075, u(med), v + 0.075, 1.3, col)
        p.text(0.18, v, name, 6.6, colour=INK, anchor="r")
        p.text(u(lo), v + 0.10, f"{lo}", 5.8, colour=MUTE)
        p.text(u(q1), v + 0.10, f"{q1}", 5.8, colour=MUTE)
        p.text(u(med), v + 0.10, f"{med}", 5.8, colour=col, font="Inter-Semi")
        p.text(u(q3), v + 0.10, f"{q3}", 5.8, colour=MUTE)
        p.text(u(hi), v + 0.10, f"{hi}", 5.8, colour=MUTE)
    p.text(0.22, 0.16, "same scale, two distributions: compare the boxes and the whiskers",
           6.4, colour=MUTE, anchor="l", font="SourceSerifItalic")


def frequency_table_sketch(c, x, y, w, h, rows=(("1", 4), ("2", 6), ("3", 9),
                                                ("4", 7), ("5", 3), ("6", 1))):
    p = Pen(c, x, y, w, h)
    cell_w, cell_h = 0.22, 0.10
    u0, v0 = 0.24, 0.14
    p.rect(u0, v0, cell_w * 2, cell_h, lw=0.6, colour=INK, fill=MIST)
    p.text(u0 + cell_w / 2, v0 + cell_h / 2, "score", 6.2, colour=HexColor("#3B4A57"))
    p.text(u0 + cell_w * 1.5, v0 + cell_h / 2, "frequency", 6.2, colour=HexColor("#3B4A57"))
    for i, (s, f) in enumerate(rows):
        vv = v0 + (i + 1) * cell_h
        p.rect(u0, vv, cell_w * 2, cell_h, lw=0.5, colour=RULE_C,
               fill=STONE_C if i % 2 else None)
        p.text(u0 + cell_w / 2, vv + cell_h / 2, s, 6.4, colour=INK)
        p.text(u0 + cell_w * 1.5, vv + cell_h / 2, str(f), 6.4, colour=INK,
               font="Inter-Semi")
    tot = sum(f for _, f in rows)
    p.text(u0 + cell_w, v0 + 7 * cell_h + 0.05, f"total {tot}", 6.4, colour=TERRA,
           font="Inter-Semi")
    p.text(0.70, 0.40, "a frequency", 6.4, colour=SOFT, anchor="l")
    p.text(0.70, 0.48, "table counts how", 6.4, colour=SOFT, anchor="l")
    p.text(0.70, 0.56, "often each value", 6.4, colour=SOFT, anchor="l")
    p.text(0.70, 0.64, "occurs; the total", 6.4, colour=SOFT, anchor="l")
    p.text(0.70, 0.72, "of the frequencies", 6.4, colour=SOFT, anchor="l")
    p.text(0.70, 0.80, "is n, the number", 6.4, colour=SOFT, anchor="l")
    p.text(0.70, 0.88, "of values", 6.4, colour=SOFT, anchor="l")


def mean_balance(c, x, y, w, h):
    p = Pen(c, x, y, w, h)
    vals = [3, 4, 4, 6, 8]
    base = 0.72
    for i, v in enumerate(vals):
        uu = 0.12 + i * 0.15
        p.rect(uu, base - v * 0.055, 0.09, v * 0.055, lw=0.7, colour=INK, fill=MIST)
        p.text(uu + 0.045, base - v * 0.055 - 0.05, str(v), 6.2, colour=INK)
    p.line(0.06, base, 0.88, base, 0.8, INK)
    m = 5
    p.line(0.06, base - m * 0.055, 0.88, base - m * 0.055, 0.9, TERRA, dash=(2.4, 3.0))
    p.text(0.90, base - m * 0.055, "mean 5", 6.6, colour=TERRA, anchor="l",
           font="Inter-Semi")
    p.text(0.06, 0.14, "the mean is the level the data would reach if every value were "
                       "equal", 6.4, colour=MUTE, anchor="l",
           font="SourceSerifItalic")


DIAGRAMS = {
    "ratio_tape": ratio_tape, "double_number_line": double_number_line,
    "recipe_bars": recipe_bars, "ratio_grid": ratio_grid, "share_bars": share_bars,
    "scale_pair": scale_pair, "prop_graph": prop_graph,
    "proportion_table": proportion_table_shade, "map_scale": map_scale,
    "proportional_recipe": proportional_recipe, "speed_graph": speed_graph,
    "price_bars": price_bars, "flow_rate": flow_rate, "signed_line": signed_line,
    "thermometer": thermometer, "neg_mult": neg_mult_explain,
    "integer_chips": integer_chips, "balance": balance,
    "function_machine": function_machine, "algebra_tiles": algebra_tiles,
    "number_trick": number_trick, "staircase": staircase,
    "matchstick": matchstick_pattern, "sequence_graph": sequence_graph,
    "lantern_arch": lantern_arch, "parallel_transversal": parallel_transversal,
    "triangle_angles": triangle_angles, "polygon_dissection": polygon_dissection,
    "circle_parts": circle_parts, "composite_area": composite_area,
    "quadrilateral_row": quadrilateral_row, "angle_sum_demo": angle_sum_demo,
    "cuboid": cuboid, "prism_net": prism_net, "cylinder_net": cylinder_net,
    "composite_solid": composite_solid, "tank_sketch": tank_sketch,
    "translation": translation_demo, "reflection": reflection_demo,
    "rotation": rotation_demo, "enlargement": enlargement_demo,
    "tessellation": tessellation, "symmetry_shapes": symmetry_shapes,
    "tree_diagram": tree_diagram, "sample_grid": sample_grid, "spinner": spinner,
    "bar_frequency": bar_frequency, "dot_plot": dot_plot, "box_plot": box_plot_pair, "box_plot_pair": box_plot_pair,
    "frequency_table": frequency_table_sketch, "mean_balance": mean_balance,
}
