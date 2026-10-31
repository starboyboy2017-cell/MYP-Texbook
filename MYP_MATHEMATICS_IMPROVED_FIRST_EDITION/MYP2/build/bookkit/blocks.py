"""Composed page blocks: headings, panels, worked examples, practice, figures."""
import os

from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Paragraph

from . import spec, typeset
from .flow import Flow, Stack, Spacer, Rule
from .markup import inline, plain, style


# --------------------------------------------------------------------- helpers
def chip(c, x, y, letter, colour, size=9.0, filled=False):
    c.saveState()
    c.setLineWidth(0.55)
    c.setStrokeColor(colour)
    if filled:
        c.setFillColor(colour)
        c.rect(x, y, size, size, stroke=0, fill=1)
    else:
        c.rect(x, y, size, size, stroke=1, fill=0)
    c.setFillColor(spec.PAPER if filled else colour)
    typeset.draw(c, x + size / 2, y + size * 0.27, letter, "Inter-Semi", size * 0.70,
                 spec.PAPER if filled else colour, 0, "center")
    c.restoreState()


def label(c, x, y, text, colour=spec.GOLD_DEEP, size=spec.SZ_LABEL, font="Inter-Semi",
          tracking=1.45, align="left"):
    return typeset.draw(c, x, y, plain(text).upper(), font, size, colour, tracking, align)


def wrap_plain(text, width, font, size):
    words = plain(text).split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if typeset.width(trial, font, size) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- section head
class SectionHead(Flow):
    """Section title set like the original: hairline, inline number, title,
    criterion strip, closing hairline."""

    def __init__(self, num, title, criterion=None, related=None, space_before=19,
                 space_after=4):
        self.num, self.title = num, title
        self.criterion = criterion
        self.related = related or []
        self.space_before = space_before
        self.space_after = space_after
        self.h = 0

    @property
    def _wordy(self):
        """A worded label ("Real-life application") is set as an eyebrow."""
        return " " in self.num or len(self.num) > 4

    def wrap(self, w):
        if self._wordy:
            numw = 0.0
            tw = w
        else:
            numw = typeset.width(self.num, "SourceSerif-Semi", 12.4) + 13
            tw = w - numw
        trial = self.title
        self._line = None
        if typeset.width(trial, "Playfair-Med", spec.SZ_H2) <= tw:
            self._line = trial
            self._th = 22
        else:
            self._par = Paragraph(inline(self.title),
                                  style("h2", fontName="Playfair-Med", fontSize=spec.SZ_H2,
                                        leading=spec.SZ_H2 * 1.15, textColor=spec.GREEN,
                                        alignment=0, hyphenationLang="",
                                        embeddedHyphenation=0))
            self._th = self._par.wrap(tw, 1e6)[1]
            if self._th > spec.SZ_H2 * 1.4:
                self._th += 4.0      # two-line title needs a little more air
        self._numw = numw
        self._eyebrow = 15 if self._wordy else 0
        strip = 0
        if self.criterion or self.related:
            strip = 15
        self.h = 15 + self._eyebrow + self._th + strip + 8
        return self.h

    def draw(self, c, x, top, w):
        c.saveState()
        c.setStrokeColor(spec.GOLD_PALE)
        c.setLineWidth(0.55)
        c.line(x, top, x + w, top)
        c.restoreState()
        numw = self._numw
        if self._wordy:
            typeset.draw(c, x, top - 12.0, self.num.upper(), "Inter-Semi", 6.8,
                         spec.TERRACOTTA, 1.5)
            ty = top - 15.2 - self._eyebrow
        else:
            typeset.draw(c, x, top - 14.4, self.num, "SourceSerif-Semi", 12.4,
                         spec.TERRACOTTA)
            ty = top - 15.2
        if self._line:
            typeset.draw(c, x + numw, ty, self._line, "Playfair-Med", spec.SZ_H2,
                         spec.GREEN)
        else:
            self._par.drawOn(c, x + numw, ty - self._par.height)
        yy = ty - self._th
        if self.criterion or self.related:
            bits = []
            if self.criterion:
                bits.append(("CRITERION " + self.criterion, spec.SAGE))
            for r in self.related:
                bits.append((r.upper(), spec.GOLD_DEEP))
            cx = x
            for text, col in bits:
                wd = typeset.draw(c, cx, yy - 9, text, "Inter-Semi", 6.3, col, 1.35)
                cx += wd + 9
                if (text, col) != bits[-1]:
                    typeset.draw(c, cx, yy - 9, "\u25c6", "Sym", 4.4, spec.GOLD, 0)
                    cx += 9
            yy -= 15
        c.saveState()
        c.setStrokeColor(spec.RULE)
        c.setLineWidth(0.5)
        c.line(x, yy - 5, x + w, yy - 5)
        c.restoreState()


class H3(Flow):
    keep_with_next = True
    keep_room = 150

    def __init__(self, text, space_before=10, colour=spec.GREEN, rule=True):
        self._text = text
        self.par = Paragraph(inline(text), style("h3", fontName="SourceSerif-Semi",
                                                 fontSize=spec.SZ_H3, leading=15.0,
                                                 textColor=colour, alignment=0))
        self.space_before = space_before
        self.rule = rule
        self.h = 0

    def wrap(self, w):
        self.h = self.par.wrap(w, 1e6)[1] + 4
        return self.h

    def draw(self, c, x, top, w):
        self.par.drawOn(c, x, top - self.par.height)
        if self.rule:
            c.saveState()
            c.setStrokeColor(spec.RULE_SOFT)
            c.setLineWidth(0.5)
            c.line(x, top - self.h + 0.8, x + w, top - self.h + 0.8)
            c.restoreState()


class H4(Flow):
    def __init__(self, text, space_before=8):
        self.par = Paragraph(inline(text), style("h4", fontName="Inter-Semi",
                                                 fontSize=spec.SZ_H4, leading=12,
                                                 textColor=spec.GOLD_DEEP, alignment=0))
        self.space_before = space_before
        self.h = 0

    def wrap(self, w):
        self.h = self.par.wrap(w, 1e6)[1] + 2
        return self.h

    def draw(self, c, x, top, w):
        self.par.drawOn(c, x, top - self.par.height)


class Lead(Flow):
    def __init__(self, text, space_before=3):
        self.par = Paragraph(inline(text), style("lead"))
        self.space_before = space_before
        self.h = 0

    def wrap(self, w):
        self.h = self.par.wrap(w, 1e6)[1]
        return self.h

    def draw(self, c, x, top, w):
        self.par.drawOn(c, x, top - self.par.height)


class Body(Flow):
    splittable = True

    def __init__(self, text, space_before=0, style_name="body", **kw):
        self.par = Paragraph(inline(text), style(style_name, **kw))
        self.space_before = space_before
        self.h = 0

    def wrap(self, w):
        self.h = self.par.wrap(w, 1e6)[1]
        return self.h

    def draw(self, c, x, top, w):
        self.par.drawOn(c, x, top - self.par.height)

    def split(self, w, avail):
        parts = self.par.split(w, avail)
        if len(parts) < 2:
            return None
        head, tail = parts
        if head.wrap(w, avail)[1] <= 0.1:
            return None
        a = Body("", style_name="body"); a.par = head
        b = Body("", style_name="body"); b.par = tail
        return a, b

    def min_split(self):
        return 2.2 * self.par.style.leading


class MarginNote(Flow):
    """Small note for the outer margin column."""

    def __init__(self, text, title=None, rule=True, colour=spec.GOLD_DEEP):
        self.text = text
        self.title = title
        self.rule = rule
        self.colour = colour
        self.h = 0

    def wrap(self, w):
        self._p = Paragraph(inline(self.text), style("mn", fontName="SourceSerif",
                                                     fontSize=8.0, leading=11.4,
                                                     textColor=spec.INK_SOFT, alignment=0))
        hh = self._p.wrap(w - 9, 1e6)[1]
        th = 0
        if self.title:
            self._t = Paragraph(inline(self.title), style("mnt", fontName="Inter-Semi",
                                                          fontSize=6.5, leading=9,
                                                          textColor=self.colour, alignment=0))
            th = self._t.wrap(w - 9, 1e6)[1] + 3
        self.h = hh + th + 4
        return self.h

    def draw(self, c, x, top, w):
        c.saveState()
        if self.rule:
            c.setFillColor(self.colour)
            c.rect(x, top - self.h, 1.6, self.h - 2, stroke=0, fill=1)
        c.restoreState()
        y = top - 1
        if self.title:
            self._t.drawOn(c, x + 9, y - self._t.height)
            y -= self._t.height + 3
        self._p.drawOn(c, x + 9, y - self._p.height)


class ListBlock(Flow):
    splittable = True

    def __init__(self, items, ordered=False, marker_colour=spec.TERRACOTTA,
                 space_before=4, style_name="body", gap=2.6, bullet=None, start=1):
        self.items = items
        self.ordered = ordered
        self.marker_colour = marker_colour
        self.space_before = space_before
        self.style_name = style_name
        self.gap = gap
        self.bullet = bullet
        self.start = start
        self.h = 0
        self._pars = None

    def _ind(self):
        return 14.0

    def _measure(self, w):
        self._pars, self._heights = [], []
        for it in self.items:
            p = Paragraph(inline(it), style(self.style_name, leftIndent=self._ind(),
                                            firstLineIndent=0, bulletIndent=0))
            self._pars.append(p)
            self._heights.append(p.wrap(w, 1e6)[1])
        self.h = sum(self._heights) + self.gap * max(0, len(self.items) - 1)
        return self.h

    def wrap(self, w):
        if self.style_name == "item":
            self.gap = 4.2
        return self._measure(w)

    def draw(self, c, x, top, w):
        if self._pars is None:
            self._measure(w)
        y = top
        for i, (p, h) in enumerate(zip(self._pars, self._heights)):
            marker = f"{i + self.start}." if self.ordered else (self.bullet or "\u2013")
            if self.ordered:
                typeset.draw(c, x + 1.0, y - p.style.fontSize * 0.86, marker, "Inter-Semi",
                             7.3, self.marker_colour)
            else:
                typeset.draw(c, x + 2.0, y - p.style.fontSize * 0.86, marker,
                             "SourceSerif", 9.0, self.marker_colour)
            p.drawOn(c, x, y - h)
            y -= h + self.gap

    def min_split(self):
        return 2.4 * spec.LD_BODY

    def split(self, w, avail):
        self._measure(w)
        used, cut = 0.0, 0
        for h in self._heights:
            if used + h > avail:
                break
            used += h + self.gap
            cut += 1
        if cut == 0:
            return None
        a = ListBlock(self.items[:cut], self.ordered, self.marker_colour, 0,
                      self.style_name, self.gap, self.bullet, self.start)
        b = ListBlock(self.items[cut:], self.ordered, self.marker_colour, 0,
                      self.style_name, self.gap, self.bullet, self.start)
        b.start = self.start + cut
        return a, b


# ---------------------------------------------------------------------- panels
PANEL_STYLES = {
    "definition": dict(fill=spec.SAND, edge=spec.SAGE, text=spec.INK,
                       label="DEFINITION"),
    "keyidea": dict(fill=spec.BLUSH, edge=spec.TERRACOTTA, text=spec.INK,
                    label="KEY IDEA"),
    "error": dict(fill=spec.BLUSH, edge=spec.RUST, text=spec.INK,
                  label="COMMON ERROR"),
    "atl": dict(fill=spec.MIST, edge=spec.SAGE, text=spec.INK, label="ATL SKILL"),
    "note": dict(fill=spec.CREAM_SOFT, edge=spec.GOLD_DEEP, text=spec.INK_SOFT,
                 label="NOTE"),
    "inquiry": dict(fill=spec.PAPER, edge=spec.TERRACOTTA, text=spec.INK,
                    label="INQUIRY"),
    "criteria": dict(fill=spec.SLATE_PALE, edge=spec.SLATE, text=spec.INK,
                     label="CRITERION"),
    "vocab": dict(fill=spec.STONE, edge=spec.SLATE, text=spec.INK,
                  label="VOCABULARY"),
    "misconception": dict(fill=spec.BLUSH, edge=spec.RUST, text=spec.INK,
                          label="MISCONCEPTION"),
}


class Panel(Flow):
    def __init__(self, kind, text=None, title=None, items=None, ordered=False,
                 space_before=spec.PANEL_GAP, flows=None, label_text=None,
                 fill=None, edge=None, compact=False):
        cfg = PANEL_STYLES[kind]
        self.cfg = cfg
        self.fill = fill or cfg["fill"]
        self.edge = edge or cfg["edge"]
        self.label_text = label_text or cfg["label"]
        self.title = title
        self.space_before = space_before
        self.space_after = 5.5
        self.compact = compact
        self.flows = list(flows or [])
        if text:
            chunks = [t for t in text.split("\n")]
            for chunk in chunks:
                self.flows.append(Paragraph(inline(chunk), style(
                    "pn", fontName="SourceSerif", fontSize=spec.SZ_SMALL + 0.4,
                    leading=spec.LD_SMALL + 1.6, textColor=cfg["text"],
                    alignment=0)))
        if items:
            self.flows.append(ListBlock(items, ordered=ordered, style_name="item",
                                        marker_colour=cfg["edge"], gap=3.2))
        self.content = Stack(self.flows, gap=5)
        self.single = len(self.flows) == 1
        self.h = 0

    def wrap(self, w):
        px = 9.0 if self.compact else spec.PANEL_PAD_X
        inner = w - 2 * px - spec.PANEL_RULE
        self._px = px
        h = (self.content.flows[0].wrap(inner) if self.single
             else self.content.wrap(inner))
        head = 0
        if self.title:
            self._tp = Paragraph(inline(self.title), style("pt", fontName="SourceSerif-Semi",
                                                           fontSize=11.0, leading=14.0,
                                                           textColor=spec.GREEN, alignment=0))
            head = self._tp.wrap(inner, 1e6)[1] + 5
        self.h = h + head + 2 * (7.5 if self.compact else spec.PANEL_PAD_Y) + 12
        return self.h

    def draw(self, c, x, top, w):
        h = self.h
        c.saveState()
        c.setFillColor(self.fill)
        c.rect(x, top - h, w, h, stroke=0, fill=1)
        c.setFillColor(self.edge)
        c.rect(x, top - h, spec.PANEL_RULE, h, stroke=0, fill=1)
        c.restoreState()
        tx = x + spec.PANEL_RULE + self._px
        tw = w - 2 * self._px - spec.PANEL_RULE
        y = top - (7.5 if self.compact else spec.PANEL_PAD_Y)
        label(c, tx, y - 5.2, self.label_text, self.edge, 6.4, tracking=1.4)
        y -= 12.5
        if self.title:
            self._tp.drawOn(c, tx, y - self._tp.height)
            y -= self._tp.height + 5
        self.content.wrap(tw)
        self.content.draw(c, tx, y, tw)


# ------------------------------------------------------------- worked examples
class WorkedExample(Flow):
    def __init__(self, ref, title, problem, steps, answer=None, check=None,
                 space_before=11, prompt=None):
        self.ref, self.title = ref, title
        self.problem = problem
        self.steps = steps
        self.answer = answer
        self.check = check
        self.prompt = prompt
        self.space_before = space_before
        self.space_after = 6
        self.h = 0

    def wrap(self, w):
        pw = w - 26
        self._p = Paragraph(inline(self.problem), style("wp", fontSize=9.5, leading=13.4,
                                                        alignment=0))
        self._ph = self._p.wrap(pw, 1e6)[1]
        self._steps = [Paragraph(inline(s), style("ws", fontSize=9.3, leading=13.0,
                                                  alignment=0)) for s in self.steps]
        self._sh = [p.wrap(pw - 15, 1e6)[1] for p in self._steps]
        h = 20 + 8 + self._ph + 8 + sum(self._sh) + 5.0 * (len(self._sh) - 1)
        if self.answer:
            self._a = Paragraph(inline(self.answer), style("wa", fontSize=9.3,
                                                           leading=13.0, alignment=0))
            h += 12 + self._a.wrap(pw - 46, 1e6)[1]
        if self.check:
            self._c = Paragraph(inline(self.check), style("wc",
                                                          fontName="SourceSerifItalic",
                                                          fontSize=8.8, leading=12,
                                                          textColor=spec.INK_SOFT,
                                                          alignment=0))
            h += 7 + self._c.wrap(pw, 1e6)[1]
        self.h = h + 16
        return self.h

    def draw(self, c, x, top, w):
        h = self.h
        c.saveState()
        c.setFillColor(spec.CREAM_SOFT)
        c.rect(x, top - h, w, h, stroke=0, fill=1)
        c.setFillColor(spec.BAR)
        c.rect(x, top - 20, w, 20, stroke=0, fill=1)
        c.setFillColor(spec.CREAM)
        typeset.draw(c, x + 11, top - 13.4, f"WORKED EXAMPLE {self.ref}", "Inter-Semi",
                     6.5, spec.CREAM, 1.5)
        if self.title:
            typeset.draw(c, x + w - 11, top - 13.4, plain(self.title).upper(), "Inter",
                         6.4, spec.GOLD_PALE, 1.3, "right")
        c.setStrokeColor(spec.RULE)
        c.setLineWidth(0.5)
        c.rect(x, top - h, w, h, stroke=1, fill=0)
        c.restoreState()

        y = top - 20 - 8
        pw = w - 26
        label(c, x + 13, y - 5, "PROBLEM", spec.GOLD_DEEP, 6.3)
        y -= 9
        self._p.drawOn(c, x + 13, y - self._ph)
        y -= self._ph + 8
        for i, (p, ph) in enumerate(zip(self._steps, self._sh)):
            c.saveState()
            c.setFillColor(spec.TERRACOTTA)
            c.circle(x + 21, y - 4.4, 5.3, stroke=0, fill=1)
            c.restoreState()
            typeset.draw(c, x + 21, y - 6.6, str(i + 1), "Inter-Semi", 6.0, spec.PAPER,
                         0, "center")
            p.drawOn(c, x + 28, y - ph)
            y -= ph + 5.0
        if self.answer:
            y -= 3
            c.saveState()
            c.setStrokeColor(spec.RULE)
            c.setLineWidth(0.5)
            c.line(x + 13, y + 4, x + 13 + pw, y + 4)
            c.restoreState()
            y -= 9
            typeset.draw(c, x + 13, y - 6, "ANSWER", "Inter-Semi", 6.3, spec.GREEN, 1.4)
            self._a.drawOn(c, x + 58, y - self._a.height)
            y -= self._a.height + 5
        if self.check:
            self._c.drawOn(c, x + 13, y - self._c.height - 2)


# -------------------------------------------------------------------- practice
class Practice(Flow):
    def __init__(self, ref, ranges, items, space_before=13, intro=None, cols=1):
        self.ref, self.ranges, self.items = ref, ranges, items
        self.space_before = space_before
        self.space_after = 4
        self.intro = intro
        self.cols = cols
        self.h = 0

    def _par(self, it):
        return Paragraph(inline(it["q"]), style("pi", fontSize=spec.SZ_ITEM,
                                                leading=spec.LD_ITEM, leftIndent=17,
                                                firstLineIndent=0, alignment=0))

    def wrap(self, w):
        self._ps = [self._par(it) for it in self.items]
        self._hs = []
        for p in self._ps:
            self._hs.append(p.wrap(w - 18, 1e6)[1])
        self.h = 20 + sum(self._hs) + 4.6 * max(0, len(self._hs) - 1) + 9
        if self.intro:
            self._intro = Paragraph(inline(self.intro), style("pii", fontSize=8.9,
                                                              leading=12.4,
                                                              textColor=spec.INK_SOFT,
                                                              alignment=0))
            self.h += self._intro.wrap(w, 1e6)[1] + 6
        return self.h

    def draw(self, c, x, top, w):
        c.saveState()
        c.setStrokeColor(spec.GREEN)
        c.setLineWidth(0.95)
        c.line(x, top - 1, x + w, top - 1)
        c.restoreState()
        typeset.draw(c, x, top - 12.4, f"PRACTICE {self.ref}", "Inter-Semi", 7.0,
                     spec.GREEN, 1.55)
        if self.ranges:
            typeset.draw(c, x + w, top - 12.4, plain(self.ranges).upper(), "Inter", 6.2,
                         spec.INK_MUTE, 1.15, "right")
        y = top - 20
        if self.intro:
            self._intro.drawOn(c, x, y - self._intro.height)
            y -= self._intro.height + 6
        for i, (it, p, h) in enumerate(zip(self.items, self._ps, self._hs)):
            typeset.draw(c, x + 1.0, y - 7.7, f"{it.get('n', i + 1)}.", "Inter-Semi",
                         7.3, spec.TERRACOTTA)
            p.drawOn(c, x, y - h)
            tags = [t for t in (it.get("tag"), it.get("tag2")) if t]
            for k, tag in enumerate(tags):
                chip(c, x + w - 9.8 - k * 11.8, y - 10.6, tag, spec.TAGS[tag][1], 9.8)
            y -= h + 4.6


class PracticeSplit(Flow):
    """A practice list that may continue on the next page."""
    splittable = True

    def __init__(self, ref, ranges, items, space_before=13):
        self.ref, self.ranges, self.items = ref, ranges, items
        self.space_before = space_before
        self.h = 0

    def wrap(self, w):
        self._inner = Practice(self.ref, self.ranges, self.items)
        self.h = self._inner.wrap(w)
        return self.h

    def draw(self, c, x, top, w):
        self._inner.draw(c, x, top, w)

    def min_split(self):
        return 70

    def split(self, w, avail):
        inner = Practice(self.ref, self.ranges, self.items)
        inner.wrap(w)
        used, cut = 20.0, 0
        for h in inner._hs:
            if used + h + 4.6 > avail:
                break
            used += h + 4.6
            cut += 1
        if cut < 1:
            return None
        return (Practice(self.ref, self.ranges, self.items[:cut]),
                Practice(self.ref + " continued", self.ranges, self.items[cut:]))


# --------------------------------------------------------------------- figures
class Figure(Flow):
    def __init__(self, path, caption=None, width=None, space_before=10, space_after=6,
                 number=None, align="left", max_height=None, credit=None):
        self.path = path
        self.caption = caption
        self.width = width
        self.number = number
        self.align = align
        self.space_before = space_before
        self.space_after = space_after
        self.max_height = max_height
        self.credit = credit
        self.h = 0

    def wrap(self, w):
        iw = min(self.width or w, w)
        img = ImageReader(self.path)
        px_w, px_h = img.getSize()
        ih = iw * px_h / px_w
        if self.max_height and ih > self.max_height:
            scale = self.max_height / ih
            iw, ih = iw * scale, ih * scale
        self.iw, self.ih = iw, ih
        cap_h = 0
        self._cap = None
        if self.caption:
            self._cap = Paragraph(inline(self.caption),
                                  style("cap", fontName="Inter", fontSize=spec.SZ_CAPTION,
                                        leading=spec.LD_CAP, textColor=spec.INK_MUTE,
                                        alignment=0))
            cap_h = self._cap.wrap(iw - 50, 1e6)[1] + 8
        credit_h = 9 if self.credit else 0
        self.h = ih + cap_h + credit_h
        self._capoff = (typeset.width(self.number.upper(), "Inter-Semi", 6.3, 1.3) + 9
                        if self.number else 0)
        return self.h

    def draw(self, c, x, top, w):
        iw, ih = self.iw, self.ih
        ix = x + (w - iw) / 2 if self.align == "center" else x
        c.drawImage(self.path, ix, top - ih, iw, ih, mask="auto")
        y = top - ih - 9
        if self.number:
            label(c, ix, y, self.number, spec.GOLD_DEEP, 6.3, tracking=1.3)
        if self._cap:
            self._cap.drawOn(c, ix + self._capoff, y + 1 - self._cap.height)
        if self.credit:
            typeset.draw(c, ix, top - self.h + 1, plain(self.credit), "Inter", 5.7,
                         spec.INK_MUTE, 0.2)


class Diagram(Flow):
    """Vector artwork drawn by a callback, so it stays resolution independent."""
    def __init__(self, height, fn, caption=None, number=None, space_before=9,
                 space_after=6, width=None, credit=None, args=(), kwargs=None):
        self.height = height
        self.fn = fn
        self.caption = caption
        self.number = number
        self.space_before = space_before
        self.space_after = space_after
        self.width = width
        self.credit = credit
        self.args = args
        self.kwargs = kwargs or {}
        self.h = 0

    def wrap(self, w):
        self.iw = min(self.width or w, w)
        cap = 0
        self._cap = None
        if self.caption:
            self._cap = Paragraph(inline(self.caption),
                                  style("cap", fontName="Inter", fontSize=spec.SZ_CAPTION,
                                        leading=spec.LD_CAP, textColor=spec.INK_MUTE,
                                        alignment=0))
            self._capoff = (typeset.width(self.number.upper(), "Inter-Semi", 6.3, 1.3) + 9
                            if self.number else 0)
            cap = self._cap.wrap(self.iw - self._capoff, 1e6)[1] + 10
        self.h = self.height + cap + 6
        return self.h

    def draw(self, c, x, top, w):
        ix = x + (w - self.iw) / 2
        self.fn(c, ix, top - self.height, self.iw, self.height, *self.args, **self.kwargs)
        if self.number:
            label(c, ix, top - self.height - 10, self.number, spec.GOLD_DEEP, 6.3,
                  tracking=1.3)
        if self._cap:
            self._cap.drawOn(c, ix + getattr(self, "_capoff", 0),
                             top - self.height - 4 - self._cap.height)


# ---------------------------------------------------------------------- tables
class DataTable(Flow):
    splittable = True

    def __init__(self, head, rows, widths=None, caption=None, space_before=10,
                 number=None, first_col_bold=True, font_size=None, stripe=True,
                 align_right=None):
        self.head, self.rows = head, rows
        self.widths = widths
        self.caption = caption
        self.number = number
        self.space_before = space_before
        self.first_col_bold = first_col_bold
        self.font_size = font_size or spec.SZ_TABLE
        self.stripe = stripe
        self.align_right = align_right or []
        self.space_after = 4
        self.splittable = len(rows) > 9
        self.h = 0

    def wrap(self, w):
        n = len(self.head)
        if self.widths:
            tot = sum(self.widths)
            self.colw = [w * x / tot for x in self.widths]
        else:
            self.colw = [w / n] * n
        fs = self.font_size
        self._hp = [Paragraph(inline(h), style("th", fontName="Inter-Semi",
                                               fontSize=fs - 0.4, leading=fs * 1.32,
                                               textColor=spec.GREEN, alignment=0))
                    for h in self.head]
        self._hh = [p.wrap(cw - 9, 1e6)[1] for p, cw in zip(self._hp, self.colw)]
        self.head_h = max(self._hh) + 10
        self._rows, self._rowh = [], []
        for row in self.rows:
            ps, hs = [], []
            for i, cell in enumerate(row):
                bold = self.first_col_bold and i == 0
                p = Paragraph(inline(cell), style(
                    "td", fontName="SourceSerif-Semi" if bold else "SourceSerif",
                    fontSize=fs, leading=fs * 1.36, textColor=spec.INK,
                    alignment=0))
                ps.append(p)
                hs.append(p.wrap(self.colw[i] - 9, 1e6)[1])
            self._rows.append(ps)
            self._rowh.append(max(hs) + 8)
        cap = 0
        self._cap = None
        if self.caption:
            self._cap = Paragraph(inline(self.caption),
                                  style("cap", fontName="Inter", fontSize=spec.SZ_CAPTION,
                                        leading=spec.LD_CAP, textColor=spec.INK_MUTE,
                                        alignment=0))
            self._capoff = (typeset.width(self.number.upper(), "Inter-Semi", 6.3, 1.3) + 9
                            if self.number else 0)
            cap = self._cap.wrap(w - self._capoff, 1e6)[1] + 8
        self.h = self.head_h + sum(self._rowh) + cap + 7
        return self.h

    def draw(self, c, x, top, w):
        y = top
        c.saveState()
        c.setStrokeColor(spec.GREEN)
        c.setLineWidth(0.95)
        c.line(x, y - 1, x + w, y - 1)
        c.restoreState()
        cx = x
        for p, cw in zip(self._hp, self.colw):
            p.drawOn(c, cx + 5, y - 6 - p.height)
            cx += cw
        y -= self.head_h
        c.saveState()
        c.setStrokeColor(spec.RULE)
        c.setLineWidth(0.5)
        c.line(x, y + 4, x + w, y + 4)
        c.restoreState()
        for i, (ps, rh) in enumerate(zip(self._rows, self._rowh)):
            if self.stripe and i % 2 == 1:
                c.saveState()
                c.setFillColor(spec.CREAM_SOFT)
                c.rect(x, y - rh, w, rh, stroke=0, fill=1)
                c.restoreState()
            cx = x
            for k, (p, cw) in enumerate(zip(ps, self.colw)):
                p.drawOn(c, cx + 5, y - 5 - p.height)
                cx += cw
            y -= rh
            c.saveState()
            c.setStrokeColor(spec.RULE_SOFT)
            c.setLineWidth(0.4)
            c.line(x, y + 4, x + w, y + 4)
            c.restoreState()
        if self._cap:
            if self.number:
                label(c, x, y - 10, self.number, spec.GOLD_DEEP, 6.3, tracking=1.3)
            self._cap.drawOn(c, x + getattr(self, "_capoff", 0),
                             y - 5 - self._cap.height)


    # -- continuation -------------------------------------------------------
    def min_split(self):
        return self.head_h + self._rowh[0] * 2 if self._rowh else 60

    def split(self, w, avail):
        self.wrap(w)
        used, cut = self.head_h, 0
        for rh in self._rowh:
            if used + rh > avail:
                break
            used += rh
            cut += 1
        if cut == 0 or len(self.rows) - cut < 2:
            return None
        a = DataTable(self.head, self.rows[:cut], self.widths, None, 0, self.number,
                      self.first_col_bold, self.font_size, self.stripe)
        b = DataTable(self.head, self.rows[cut:], self.widths, self.caption, 0, None,
                      self.first_col_bold, self.font_size, self.stripe)
        return a, b


class Stage(Flow):
    """A numbered inquiry-stage marker: 01 \u00b7 ENGAGE."""

    keep_with_next = True
    keep_room = 86

    def __init__(self, num, name, note=None, space_before=15):
        self.num, self.name, self.note = num, name, note
        self.space_before = space_before
        self.h = 0

    def wrap(self, w):
        h = 15
        self._note = None
        if self.note:
            self._note = Paragraph(inline(self.note), style(
                "stg", fontName="SourceSerifItalic", fontSize=8.6, leading=11.6,
                textColor=spec.INK_MUTE, alignment=0))
            h += self._note.wrap(w, 1e6)[1] + 3
        self.h = h
        return self.h

    def draw(self, c, x, top, w):
        typeset.draw(c, x, top - 7, f"{self.num}  \u00b7  {self.name}", "Inter-Semi",
                     6.8, spec.TERRACOTTA, 1.7)
        nw = typeset.width(f"{self.num}  \u00b7  {self.name}", "Inter-Semi", 6.8, 1.7)
        c.saveState()
        c.setStrokeColor(spec.GOLD_PALE)
        c.setLineWidth(0.5)
        c.line(x + nw + 10, top - 4.5, x + w, top - 4.5)
        c.restoreState()
        if self._note:
            self._note.drawOn(c, x, top - 15 - self._note.height)



# ------------------------------------------------------------------- additions
class Photo(Flow):
    """A photograph, cropped to a fixed aspect, framed by a hairline.

    The original edition carried no photographs at all. Here every chapter
    carries two or three, cropped to one of two aspect ratios so that the
    picture block behaves like a figure and never breaks the page rhythm.
    """
    def __init__(self, path, caption=None, number=None, credit=None,
                 aspect=1.5, width=None, space_before=12, space_after=8,
                 align="left", tone=None):
        self.path = path
        self.caption = caption
        self.number = number
        self.credit = credit
        self.aspect = aspect
        self.width = width
        self.space_before = space_before
        self.space_after = space_after
        self.align = align
        self.tone = tone
        self.h = 0

    def _cropped(self):
        from PIL import Image
        import tempfile, os
        if not hasattr(self, "_crop_path"):
            im = Image.open(self.path).convert("RGB")
            w, h = im.size
            target = self.aspect
            if w / h > target:
                nw = int(h * target)
                box = ((w - nw) // 2, 0, (w + nw) // 2, h)
            else:
                nh = int(w / target)
                box = (0, (h - nh) // 3, w, (h - nh) // 3 + nh)
            im = im.crop(box)
            base = os.path.splitext(os.path.basename(self.path))[0]
            out = os.path.join(os.path.dirname(self.path), "_crop",
                               f"{base}_{str(self.aspect).replace('.', 'p')}.jpg")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            im.save(out, quality=92)
            self._crop_path = out
        return self._crop_path

    def wrap(self, w):
        if self.width and self.width <= 1.0:          # a fraction of the measure
            self.iw = self.width * w
        else:
            self.iw = min(self.width or w, w)
        self.ih = self.iw / self.aspect
        self._cap = None
        cap = 0
        if self.caption:
            self._cap = Paragraph(inline(self.caption),
                                  style("cap", fontName="Inter", fontSize=spec.SZ_CAPTION,
                                        leading=spec.LD_CAP, textColor=spec.INK_MUTE,
                                        alignment=0))
            self._capoff = (typeset.width(self.number.upper(), "Inter-Semi", 6.3, 1.3) + 9
                            if self.number else 0)
            cap = self._cap.wrap(max(60.0, self.iw - self._capoff), 1e6)[1] + 11
        cr = 9 if self.credit else 0
        self.h = self.ih + cap + cr
        return self.h

    def draw(self, c, x, top, w):
        ix = x + (w - self.iw) / 2 if self.align == "center" else x
        c.drawImage(self._cropped(), ix, top - self.ih, self.iw, self.ih, mask=None)
        c.saveState()
        c.setStrokeColor(spec.RULE)
        c.setLineWidth(0.4)
        c.rect(ix, top - self.ih, self.iw, self.ih, stroke=1, fill=0)
        c.restoreState()
        y = top - self.ih - 10
        if self.number:
            label(c, ix, y, self.number, spec.GOLD_DEEP, 6.3, tracking=1.3)
        if self._cap:
            self._cap.drawOn(c, ix + self._capoff, y + 1 - self._cap.height)
        if self.credit:
            typeset.draw(c, ix, top - self.h + 1, plain(self.credit), "Inter", 5.9,
                         spec.INK_MUTE, 0.2)


class Card(Flow):
    """A bordered card: the original's investigation and task boxes.

    Title in the display serif, a boxed chip on the right ('INVESTIGATION',
    'CRITERION D'), a hairline under the title, then the body.
    """
    keep_with_next = False

    def __init__(self, title, body_flows, chip_text=None, chip_colour=None,
                 fill=spec.CREAM_SOFT, edge=spec.RULE, rule_colour=None,
                 space_before=12, space_after=8):
        self.title = title
        self.flows = list(body_flows)
        self.chip_text = chip_text
        self.chip_colour = chip_colour or spec.GOLD_DEEP
        self.fill = fill
        self.edge = edge
        self.rule_colour = rule_colour or spec.RULE
        self.space_before = space_before
        self.space_after = space_after
        self.content = Stack(self.flows, gap=7)
        self.h = 0

    def wrap(self, w):
        pad = 15
        self._pad = pad
        inner = w - 2 * pad
        self._tp = Paragraph(inline(self.title),
                             style("ct", fontName="Playfair-Med", fontSize=16.5,
                                   leading=20, textColor=spec.INK, alignment=0))
        self._th = self._tp.wrap(inner - 92, 1e6)[1]
        self._bh = self.content.wrap(inner)
        self.h = pad + max(self._th, 18) + 13 + self._bh + pad - 2
        return self.h

    def draw(self, c, x, top, w):
        h = self.h
        pad = self._pad
        c.saveState()
        c.setFillColor(self.fill)
        c.setStrokeColor(self.edge)
        c.setLineWidth(0.6)
        c.rect(x, top - h, w, h, stroke=1, fill=1)
        c.restoreState()
        if self.chip_text:
            txt = self.chip_text.upper()
            cw = typeset.width(txt, "Inter-Semi", 5.9, 1.3) + 16
            c.saveState()
            c.setStrokeColor(self.chip_colour)
            c.setLineWidth(0.55)
            c.rect(x + w - pad - cw, top - pad - 12, cw, 15, stroke=1, fill=0)
            c.restoreState()
            typeset.draw(c, x + w - pad - cw / 2, top - pad - 8.4, txt, "Inter-Semi",
                         5.9, self.chip_colour, 1.3, "center")
        self._tp.drawOn(c, x + pad, top - pad - self._tp.height + 1)
        yy = top - pad - max(self._th, 18) - 7
        c.saveState()
        c.setStrokeColor(self.rule_colour)
        c.setLineWidth(0.55)
        c.line(x + pad, yy, x + w - pad, yy)
        c.restoreState()
        self.content.wrap(w - 2 * pad)
        self.content.draw(c, x + pad, yy - 8, w - 2 * pad)


class PageTitle(Flow):
    """Front-matter page title: letterspaced eyebrow, large display title, rule."""

    keep_with_next = True
    keep_room = 120

    def __init__(self, title, eyebrow=None, space_before=0, right=None):
        self.title = title
        self.eyebrow = eyebrow
        self.right = right
        self.space_before = space_before
        self.h = 0

    def wrap(self, w):
        self._p = Paragraph(inline(self.title),
                            style("pt", fontName="Playfair", fontSize=spec.SZ_FM_TITLE,
                                  leading=spec.SZ_FM_TITLE * 1.12, textColor=spec.INK,
                                  alignment=0))
        self._th = self._p.wrap(w, 1e6)[1]
        self.h = (14 if self.eyebrow else 0) + self._th + 26
        return self.h

    def draw(self, c, x, top, w):
        y = top
        if self.eyebrow:
            label(c, x, y - 6, self.eyebrow, spec.TERRACOTTA, 6.3, tracking=2.1)
            y -= 14
        self._p.drawOn(c, x, y - self._th)
        y -= self._th + 12
        c.saveState()
        c.setStrokeColor(spec.GOLD)
        c.setLineWidth(0.8)
        c.line(x, y, x + w, y)
        c.restoreState()


class Statement(Flow):
    """The statement of inquiry: a navy field, cream display serif."""

    def __init__(self, label_text, text, space_before=10):
        self.label_text = label_text
        self.text = text
        self.space_before = space_before
        self.space_after = 8
        self.h = 0

    def wrap(self, w):
        self._p = Paragraph(inline(self.text),
                            style("stq", fontName="Playfair", fontSize=14.2,
                                  leading=19.6, textColor=spec.CREAM, alignment=0))
        self._ph = self._p.wrap(w - 44, 1e6)[1]
        self.h = self._ph + 44
        return self.h

    def draw(self, c, x, top, w):
        c.saveState()
        c.setFillColor(spec.NAVY)
        c.rect(x, top - self.h, w, self.h, stroke=0, fill=1)
        c.restoreState()
        label(c, x + 22, top - 19, self.label_text, spec.GOLD_PALE, 6.2, tracking=1.9)
        self._p.drawOn(c, x + 22, top - 32 - self._ph)


class ChipRow(Flow):
    """Boxed label chips, as on the original's chapter plates and planner pages."""

    def __init__(self, chips, space_before=8, gap=8):
        self.chips = chips          # [(label, value)]
        self.space_before = space_before
        self.gap = gap
        self.h = 0

    def wrap(self, w):
        self.lines, cur, cw = [], [], 0.0
        for lab, val in self.chips:
            txt = f"{lab} \u00b7 {val}".upper()
            wd = typeset.width(txt, "Inter-Semi", 5.9, 1.2) + 18
            if cur and cw + wd > w:
                self.lines.append(cur)
                cur, cw = [], 0.0
            cur.append((txt, wd))
            cw += wd + self.gap
        if cur:
            self.lines.append(cur)
        self.h = len(self.lines) * 24
        return self.h

    def draw(self, c, x, top, w):
        y = top
        for row in self.lines:
            cx = x
            for txt, wd in row:
                c.saveState()
                c.setStrokeColor(spec.RULE)
                c.setLineWidth(0.55)
                c.rect(cx, y - 17, wd, 17, stroke=1, fill=0)
                c.restoreState()
                typeset.draw(c, cx + 9, y - 12.2, txt, "Inter-Semi", 5.9, spec.INK_LABEL,
                             1.2)
                cx += wd + self.gap
            y -= 24


class Formula(Flow):
    """A centred display formula in the italic text face."""

    def __init__(self, text, note=None, space_before=8, space_after=8,
                 colour=spec.INK):
        self.text = text
        self.note = note
        self.space_before = space_before
        self.space_after = space_after
        self.colour = colour
        self.h = 0

    def wrap(self, w):
        self._p = Paragraph(inline(self.text),
                            style("fml", fontName="SourceSerifItalic-Med", fontSize=11.4,
                                  leading=16, textColor=self.colour, alignment=1))
        self._ph = self._p.wrap(w - 24, 1e6)[1]
        self._n = None
        nh = 0
        if self.note:
            self._n = Paragraph(inline(self.note),
                                style("fmn", fontName="Inter", fontSize=6.6,
                                      leading=9.2, textColor=spec.INK_MUTE, alignment=1))
            nh = self._n.wrap(w - 24, 1e6)[1] + 3
        self.h = self._ph + nh + 8
        return self.h

    def draw(self, c, x, top, w):
        self._p.drawOn(c, x + 12, top - 4 - self._ph)
        if self._n:
            self._n.drawOn(c, x + 12, top - 6 - self._ph - self._n.height)


# ------------------------------------------------------------- answer setting
class AnswerLabel(Flow):
    """A tracked practice label above a block of answers."""

    def __init__(self, text, space_before=11.0, colour=None):
        self.text = text
        self.space_before = space_before
        self.colour = colour or spec.TERRACOTTA
        self.h = 15.0

    def wrap(self, w):
        return 15.0

    def draw(self, c, x, top, w):
        y = top - 6.4
        label(c, x, y, self.text, self.colour, 6.3, "Inter-Semi", 1.35)
        tw = typeset.width(plain(self.text).upper(), "Inter-Semi", 6.3,
                           tracking=1.35)
        c.saveState()
        c.setStrokeColor(spec.RULE_SOFT)
        c.setLineWidth(0.5)
        c.line(x + tw + 12, y + 2.0, x + w, y + 2.0)
        c.restoreState()


class AnswerEntry(Flow):
    """One numbered answer on its own line, with a hanging indent."""

    splittable = True

    def __init__(self, number, text, space_before=0.0):
        self.number = number
        self.text = text
        self.space_before = space_before
        self.par = self._make(inline(text))
        self.h = 0

    def _make(self, body):
        num = ('<font name="Inter-Semi" size="6.9" color="#A64B27">'
               f"{self.number}.</font>" + "\u2002")
        return Paragraph(num + body, style(
            "ans", fontName="SourceSerif", fontSize=8.5, leading=11.5,
            textColor=spec.INK, alignment=0, leftIndent=15.5,
            firstLineIndent=-15.5))

    def wrap(self, w):
        self.par = self._make(inline(self.text)) if getattr(self, "_split", False) is False else self.par
        self.h = self.par.wrap(w, 1e6)[1] + 1.0
        return self.h

    def draw(self, c, x, top, w):
        self.par.drawOn(c, x, top - self.par.height)

    def split(self, w, avail):
        parts = self.par.split(w, avail)
        if len(parts) < 2:
            return None
        head, tail = parts
        if head.wrap(w, avail)[1] <= 0.1:
            return None
        a = AnswerEntry(self.number, "")
        a.par = head
        b = AnswerEntry("", "")
        b.par = tail
        b._split = True
        return a, b
