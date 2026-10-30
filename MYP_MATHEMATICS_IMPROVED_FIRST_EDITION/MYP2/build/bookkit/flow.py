"""A small, predictable page-composition engine.

reportlab's platypus flows paragraphs well but cannot compose the spreads a
textbook needs (full-width blocks interrupting a narrow reading column, margin
notes aligned to the paragraph that mentions them, panels that must never
orphan).  This module provides the minimum machinery to do that: frames, a
pager, and flow objects that wrap, draw and split.
"""
from reportlab.platypus import Paragraph

from . import spec


class Frame:
    __slots__ = ("x", "y", "w", "h", "cursor", "index")

    def __init__(self, x, y, w, h, index=0):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.cursor = y + h
        self.index = index

    @property
    def remaining(self):
        return self.cursor - self.y

    def take(self, h):
        top = self.cursor
        self.cursor -= h
        return top


# ------------------------------------------------------------------ primitives
class Flow:
    splittable = False
    space_before = 0.0
    space_after = 0.0

    def wrap(self, w):
        raise NotImplementedError

    def draw(self, c, x, top, w):
        raise NotImplementedError

    def split(self, w, avail):
        return None

    def min_split(self):
        return 1e9


class Spacer(Flow):
    def __init__(self, h):
        self.h = h

    def wrap(self, w):
        return self.h

    def draw(self, c, x, top, w):
        pass


class Rule(Flow):
    def __init__(self, colour=spec.RULE, weight=0.5, space_before=6, space_after=6,
                 dash=None, width=None):
        self.colour, self.weight = colour, weight
        self.space_before, self.space_after = space_before, space_after
        self.dash = dash
        self.width = width

    def wrap(self, w):
        return self.space_before + self.weight + self.space_after

    def draw(self, c, x, top, w):
        y = top - self.space_before - self.weight / 2
        c.saveState()
        c.setStrokeColor(self.colour)
        c.setLineWidth(self.weight)
        if self.dash:
            c.setDash(self.dash)
        c.line(x, y, x + (self.width or w), y)
        c.restoreState()


class ParaFlow(Flow):
    """Adapter so a raw reportlab Paragraph can live inside a Stack."""
    splittable = True

    def __init__(self, p):
        self.p = p
        self.h = 0

    def wrap(self, w):
        self.h = self.p.wrap(w, 1e6)[1]
        return self.h

    def draw(self, c, x, top, w):
        self.p.drawOn(c, x, top - self.h)

    def split(self, w, avail):
        parts = self.p.split(w, avail)
        if len(parts) < 2:
            return None
        if parts[0].wrap(w, avail)[1] <= 0.1:
            return None
        return ParaFlow(parts[0]), ParaFlow(parts[1])


class Stack(Flow):
    """Vertical stack that can split between (and inside) its children."""
    splittable = True

    def __init__(self, flows, gap=0.0):
        self.flows = [ParaFlow(f) if isinstance(f, Paragraph) else f
                      for f in flows if f is not None]
        self.gap = gap
        self.h = 0
        self._heights = None

    def _measure(self, w):
        hs = [f.wrap(w) for f in self.flows]
        self._heights = hs
        self.h = sum(hs) + self.gap * max(0, len(hs) - 1)
        return hs

    def wrap(self, w):
        self._measure(w)
        return self.h

    def draw(self, c, x, top, w):
        if self._heights is None:
            self._measure(w)
        y = top
        for f, h in zip(self.flows, self._heights):
            f.draw(c, x, y, w)
            y -= h + self.gap

    def split(self, w, avail):
        hs = self._measure(w)
        used = 0.0
        for i, (f, h) in enumerate(zip(self.flows, hs)):
            if used + h <= avail + 0.01:
                used += h + (self.gap if i else 0)
                continue
            if i == 0:
                if f.splittable and avail > f.min_split():
                    res = f.split(w, avail)
                    if res:
                        return Stack([res[0]]), Stack([res[1]] + self.flows[1:])
                return None
            if f.splittable and (avail - used) > f.min_split():
                res = f.split(w, avail - used)
                if res:
                    return (Stack(self.flows[:i] + [res[0]]),
                            Stack([res[1]] + self.flows[i + 1:]))
            return Stack(self.flows[:i]), Stack(self.flows[i:])
        return None


class Group(Flow):
    """Atomic wrapper: never splits."""
    def __init__(self, flow):
        self.flow = flow
        self.h = 0

    def wrap(self, w):
        self.h = self.flow.wrap(w)
        return self.h

    def draw(self, c, x, top, w):
        self.flow.draw(c, x, top, w)


# ----------------------------------------------------------------------- pager
class Pager:
    """Flows objects down the reading column, with margin notes and full-width
    interruptions."""

    def __init__(self, book):
        self.book = book
        if not book.frames:
            book.new_page("wide")
        self.frame = book.frames[0]
        self.margin = book.margin_frame
        self._page_notes = False

    # -- page management ----------------------------------------------------
    def _new_page(self, wide=None):
        if wide is None:
            wide = getattr(self, "_wide_mode", False)
        kind = "wide" if wide else "body"
        if getattr(self.book, "page_empty", False):
            self.book.apply_layout(kind)
        else:
            self.book.new_page(kind)
        self.frame = self.book.frames[0]
        self.margin = self.book.margin_frame
        self._wide_mode = wide
        self._page_notes = False

    def break_page(self):
        self._new_page(wide=False)

    # -- placement ----------------------------------------------------------
    def add(self, flow, wide=False):
        if flow is None:
            return
        self._wide_mode = wide
        guard = 0
        while True:
            guard += 1
            if guard > 300:
                raise RuntimeError("pagination did not converge")
            fr = self.frame
            w = self.book.full_width if wide else fr.w
            h = flow.wrap(w)
            sb = getattr(flow, "space_before", 0)
            self.book.page_empty = False
            if wide:
                # a full-width block always spans the page measure, whatever
                # the reading column happens to be doing on this page
                wx = self.book.left
                fr = self.frame
                floor = self._wide_floor()
                room = floor - fr.y
                if h + sb <= room + 0.01:
                    top = floor
                    flow.draw(self.book.canvas, wx, top - sb, w)
                    newc = top - sb - h - getattr(flow, "space_after", 0)
                    self.frame.cursor = newc
                    if self.margin is not None:
                        self.margin.cursor = newc
                    return
                if flow.splittable and room - sb > flow.min_split():
                    res = flow.split(w, room - sb)
                    if res:
                        head, tail = res
                        hh = head.wrap(w)
                        top = floor
                        head.draw(self.book.canvas, wx, top - sb, w)
                        newc = top - sb - hh
                        self.frame.cursor = newc
                        if self.margin is not None:
                            self.margin.cursor = newc
                        self._new_page(wide=True)
                        flow = tail
                        continue
                self._new_page(wide=True)
                continue
            if h + sb <= fr.remaining + 0.01:
                if (getattr(flow, "keep_with_next", False)
                        and fr.remaining - (h + sb) < getattr(flow, "keep_room", 0)
                        and fr.remaining < fr.h - 1):
                    self._new_page(wide=False)
                    continue
                top = fr.take(h + sb + getattr(flow, "space_after", 0))
                flow.draw(self.book.canvas, fr.x, top - sb, w)
                return
            if flow.splittable and (fr.remaining - sb) > flow.min_split():
                res = flow.split(w, fr.remaining - sb)
                if res:
                    head, tail = res
                    hh = head.wrap(w)
                    top = fr.take(hh + sb)
                    head.draw(self.book.canvas, fr.x, top - sb, w)
                    self._new_page(wide=False)
                    flow = tail
                    continue
            self._new_page(wide=False)

    def _wide_floor(self):
        if self.margin is None:
            return self.frame.cursor
        return min(self.frame.cursor, self.margin.cursor)

    def note(self, flow, gap=8):
        """Place a note in the outer margin, aligned with the current line."""
        if self.margin is None:
            return
        h = flow.wrap(self.margin.w)
        if h > self.margin.remaining - 2:
            return
        top = self.margin.take(h + gap)
        self._page_notes = True
        flow.draw(self.book.canvas, self.margin.x, top - gap, self.margin.w)

    def add_all(self, flows):
        for f in flows:
            self.add(f)
