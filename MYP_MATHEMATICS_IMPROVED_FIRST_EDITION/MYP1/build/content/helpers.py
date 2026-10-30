"""Shared composition helpers used by every chapter module.

Keeping these terse keeps the chapter sources readable as manuscripts, which is
also what the DOCX exporter consumes.
"""
from bookkit import spec
from bookkit.blocks import (SectionHead, H3, H4, Lead, Body, ListBlock, Panel,
                            WorkedExample, PracticeSplit, Practice, Figure,
                            Diagram, DataTable, MarginNote)
from bookkit.flow import Flow, Spacer, Rule

IMG = "/home/user/MYP-Texbook/MYP_MATHEMATICS_IMPROVED_FIRST_EDITION/MYP1/images/"

FIGN = [0]
TABN = [0]


def reset_counters(chapter):
    FIGN[0] = 0
    TABN[0] = 0


def _next(kind):
    if kind == "figure":
        FIGN[0] += 1
        return f"Figure {FIGN[0]}"
    TABN[0] += 1
    return f"Table {TABN[0]}"


def section(p, num, title, crit=None, rel=None):
    p.add(SectionHead(num, title, crit, rel))
    reg("section", f"{num}  {title}")


def lead(p, text):
    p.add(Lead(text))


def body(p, text, space=0):
    p.add(Body(text, space_before=space))


def h3(p, text):
    p.add(H3(text))


def h4(p, text):
    p.add(H4(text))


def lst(p, items, ordered=False, space=5):
    p.add(ListBlock(items, ordered=ordered, space_before=space))


def panel(p, kind, text=None, title=None, items=None, ordered=False, space=None):
    kw = {} if space is None else {"space_before": space}
    p.add(Panel(kind, text=text, title=title, items=items, ordered=ordered, **kw))


def atl(p, text, title="ATL \u00b7 Thinking skills"):
    panel(p, "atl", text, title)


def we(p, ref, title, problem, steps, answer=None, check=None, prompt=None):
    p.add(WorkedExample(ref, title, problem, steps, answer, check, prompt=prompt))


def practice(p, ref, ranges, items):
    p.add(PracticeSplit(ref, ranges, items))


def q(text, tag=None, tag2=None):
    d = {"q": text}
    if tag:
        d["tag"] = tag
    if tag2:
        d["tag2"] = tag2
    return d


def fig(p, name, caption, width=None, credit=None, wide=False, max_h=None):
    p.add(Figure(IMG + name, caption, width=width, number=_next("figure"),
                 credit=credit or "Original illustration created for this edition.",
                 max_height=max_h or (spec.TEXT_H - 96),
                 align="center" if wide else "left"),
          wide=wide)
    reg("figure", caption)


def diag(p, height, fn, caption=None, wide=False, args=(), kwargs=None):
    p.add(Diagram(height, fn, caption, number=_next("figure"), args=args,
                  kwargs=kwargs or {}), wide=wide)


def table(p, head, rows, widths=None, caption=None, wide=False, fs=None,
          first_col_bold=True):
    p.add(DataTable(head, rows, widths=widths, caption=caption, number=_next("table"),
                    font_size=fs, first_col_bold=first_col_bold), wide=wide)


def note(p, title, text):
    p.note(MarginNote(text, title=title))


def gap(p, h=6):
    p.add(Spacer(h))


def rule(p, space_before=8, space_after=8):
    p.add(Rule(space_before=space_before, space_after=space_after))


def criteria_panel(p, a="", b="", c="", d=""):
    items = []
    for k, txt in (("A", a), ("B", b), ("C", c), ("D", d)):
        if txt:
            items.append(f"**Criterion {k} \u00b7 {spec.CRITERIA[k][0]}** \u2014 {txt}")
    p.add(Panel("criteria", title="Criteria and strands developed", items=items,
                space_before=10))


# --------------------------------------------------------------- registry glue
REG = None
CHNUM = [0]


def set_registry(r, chapter):
    global REG
    REG = r
    CHNUM[0] = chapter


def reg(kind, title):
    if REG is not None:
        REG.record(kind, CHNUM[0], title, _CURRENT_BOOK[0].page_label if _CURRENT_BOOK else "")


_CURRENT_BOOK = [None]


def bind_book(bk):
    _CURRENT_BOOK[0] = bk


class WritingSpace(Flow):
    """Ruled lines that fill what is left of the column without overflowing it."""

    def __init__(self, lines=4, pitch=26.0, space_before=8):
        self.lines = max(2, lines)
        self.pitch = pitch
        self.space_before = space_before
        self.h = self.lines * self.pitch

    def wrap(self, w):
        return self.h

    def draw(self, c, x, top, w):
        c.saveState()
        c.setStrokeColor(spec.RULE_SOFT)
        c.setLineWidth(0.5)
        for i in range(self.lines):
            y = top - self.pitch * (i + 1) + self.pitch * 0.35
            c.line(x, y, x + w, y)
        c.restoreState()


def assessment_close(p, rows, atl_text, next_title=None, criteria_items=None):
    """Close a review with a roomy self-assessment page.

    A review spreads over two pages in this book: the first carries what the
    chapter established, its vocabulary and its misconceptions; this second page
    carries the self-assessment, a criterion-linked reflection and the ATL note,
    with room to write on.
    """
    from bookkit.flow import Pager
    p.break_page()
    h3(p, "Self-assessment")
    p.add(DataTable(["I can \u2026", "Not yet", "Getting there", "Confident"], rows,
                    widths=[2.0, 0.55, 0.65, 0.65], first_col_bold=False,
                    font_size=9.0, space_before=6))
    gap(p, 10)
    panel(p, "criteria", title="Reflect on the criteria",
          items=criteria_items or [
              "**Criterion A:** which calculation in this chapter would you now do "
              "without checking?",
              "**Criterion C:** where did notation or a diagram carry an argument for you?",
              "**Criterion D:** which real context changed how you understood the "
              "mathematics?"])
    gap(p, 8)
    panel(p, "atl", title="ATL \u00b7 Reflection", text=atl_text)
    if next_title:
        body(p, "**Looking ahead \u00b7 " + next_title + "** takes these ideas further. "
                "The self-assessment above tells you which to revisit first.", space=8)
    gap(p, 4)
    h3(p, "A note to your teacher")
    body(p, "Two sentences: what you can now do that you could not do at the start of "
            "the chapter, and which single idea you would still like explained.")
    avail = p.frame.remaining - 16
    lines = max(2, min(9, int(avail // 30)))
    p.add(WritingSpace(lines=lines, pitch=avail / lines, space_before=8))
