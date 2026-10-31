"""Block renderer: turns each chapter's declarative block list into page flows.

A chapter module is a manuscript: a PLATE dict, a few tables of intentions and a
flat BLOCKS list of tuples. This module is the only place that knows how a
block becomes type, which keeps the chapter sources readable and keeps page
composition consistent across all eleven chapters.
"""
import os

from bookkit import spec
from bookkit.blocks import (SectionHead, H3, H4, Lead, Body, ListBlock, Panel,
                            WorkedExample, PracticeSplit, Photo, Diagram, DataTable,
                            Stage, Card, PageTitle, Statement, ChipRow, Formula)
from bookkit.flow import Spacer, Rule, Stack
from bookkit.markup import inline, style
from reportlab.platypus import Paragraph

IMG = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/images/"

FIGN = [0]
TABN = [0]
PAGE_NOTES = []

# ---------------------------------------------------------------- registry glue
SECTIONS = []          # [(chapter, section title, page label)]
INDEX_HITS = {}        # term -> [page labels]
_CAP = {"book": None, "chapter": 0, "section": None}
_TERMS = None


def reset(chapter):
    FIGN[0] = 0
    TABN[0] = 0


def next_fig():
    FIGN[0] += 1
    return f"Figure {_CAP['chapter']}.{FIGN[0]}"


def next_tab():
    TABN[0] += 1
    return f"Table {_CAP['chapter']}.{TABN[0]}"


def q(text, tag=None, tag2=None):
    d = {"q": text}
    if tag:
        d["tag"] = tag
    if tag2:
        d["tag2"] = tag2
    return d


def _flows(blocks, p):
    """Recursively build a nested flow list (used by cards)."""
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "p":
            out.append(Paragraph(inline(b[1]),
                                 style("cp", fontSize=9.3, leading=13.2, alignment=0)))
        elif kind == "h4":
            out.append(Paragraph(inline(b[1]),
                                 style("ch4", fontName="Inter-Semi", fontSize=8.6,
                                       leading=11.6, textColor=spec.GOLD_DEEP,
                                       alignment=0)))
        elif kind == "ul":
            out.append(ListBlock(list(b[1]), space_before=0))
        elif kind == "ol":
            out.append(ListBlock(list(b[1]), ordered=True, space_before=0))
        elif kind == "formula":
            out.append(Formula(b[1], b[2] if len(b) > 2 else None))
        elif kind == "table":
            out.append(DataTable(b[1], b[2], widths=b[3], caption=b[4] if len(b) > 4 else None,
                                 font_size=8.2))
        elif kind == "diag":
            out.append(Diagram(b[1], b[2], caption=b[4] if len(b) > 4 else None,
                               kwargs=b[3] or {}))
    return out


def begin_capture(chapter, book):
    global _TERMS
    _CAP["book"] = book
    _CAP["chapter"] = chapter
    _CAP["section"] = None
    if _TERMS is None:
        import back2
        _TERMS = [t.lower() for t in back2.INDEX_TERMS]


def _texts(b):
    """All strings inside a block, recursively."""
    out = []
    for x in b:
        if isinstance(x, str):
            out.append(x)
        elif isinstance(x, (list, tuple)):
            out.extend(_texts(x))
    return out


def _scan(b):
    if _CAP["book"] is None or _CAP["section"] is None:
        return
    label = _CAP["book"].page_label
    blob = " ".join(_texts(b)).lower()
    for term in _TERMS:
        if term in blob:
            lst = INDEX_HITS.setdefault(term, [])
            if label not in lst:
                lst.append(label)


def render(p, blocks, chapter_no=1):
    """Emit the blocks into the pager p."""
    for b in blocks:
        kind = b[0]
        if kind == "section":
            label = p.book.page_label
            _CAP["section"] = b[2]
            SECTIONS.append((chapter_no, f"{b[1]}  {b[2]}", label))
        else:
            _scan(b)
        if kind == "stage":
            p.add(Stage(b[1], b[2], b[3] if len(b) > 3 else None))
        elif kind == "section":
            crit = b[3] if len(b) > 3 else None
            rel = b[4] if len(b) > 4 else None
            p.add(SectionHead(b[1], b[2], crit, rel))
        elif kind == "lead":
            p.add(Lead(b[1]))
        elif kind == "p":
            p.add(Body(b[1], space_before=b[2] if len(b) > 2 else 0))
        elif kind == "h3":
            p.add(H3(b[1]))
        elif kind == "h4":
            p.add(H4(b[1]))
        elif kind == "ul":
            p.add(ListBlock(list(b[1])))
        elif kind == "ol":
            p.add(ListBlock(list(b[1]), ordered=True))
        elif kind == "panel":
            items = b[4] if len(b) > 4 else None
            p.add(Panel(b[1], text=b[2], title=b[3] if len(b) > 3 else None,
                        items=items))
        elif kind == "we":
            ref, title, problem, steps = b[1], b[2], b[3], b[4]
            answer = b[5] if len(b) > 5 else None
            check = b[6] if len(b) > 6 else None
            p.add(WorkedExample(ref, title, problem, steps, answer, check))
        elif kind == "practice":
            p.add(PracticeSplit(b[1], b[2], list(b[3])))
        elif kind == "table":
            cap = b[4] if len(b) > 4 else None
            p.add(DataTable(b[1], b[2], widths=b[3], caption=cap,
                            number=next_tab() if cap else None,
                            font_size=b[5] if len(b) > 5 else spec.SZ_TABLE))
        elif kind == "diag":
            import diagrams2
            height = b[1]
            fn = diagrams2.DIAGRAMS[b[2]] if isinstance(b[2], str) else b[2]
            kw = b[3] or {}
            cap = b[4] if len(b) > 4 else None
            p.add(Diagram(height, fn, caption=cap, number=next_fig() if cap else None,
                          kwargs=kw, width=b[5] if len(b) > 5 else None))
        elif kind == "photo":
            name, aspect = b[1], b[2]
            cap = b[3] if len(b) > 3 else None
            credit = b[4] if len(b) > 4 else "Photograph created for this edition."
            p.add(Photo(IMG + "photos/" + name, caption=cap,
                        number=next_fig() if cap else None, credit=credit,
                        aspect=aspect, width=b[5] if len(b) > 5 else None))
        elif kind == "card":
            title, chip, chip_col = b[1], b[2], b[3]
            chip_col = {"TERRA": spec.TERRACOTTA, "GOLD": spec.GOLD_DEEP,
                        "SAGE": spec.SAGE, "SLATE": spec.SLATE}.get(chip_col, chip_col)
            flows = _flows(b[4], p)
            p.add(Card(title, flows, chip_text=chip, chip_colour=chip_col))
        elif kind == "formula":
            p.add(Formula(b[1], b[2] if len(b) > 2 else None))
        elif kind == "statement":
            p.add(Statement(b[1], b[2]))
        elif kind == "chips":
            p.add(ChipRow(b[1]))
        elif kind == "head":
            p.book.chapter_label = b[1]
            SECTIONS.append((chapter_no, b[1], p.book.page_label))
        elif kind == "pagetitle":
            if str(b[1]).startswith("Part ") and "review" in str(b[1]):
                p.book.chapter_label = b[1]
            p.add(PageTitle(b[1], b[2] if len(b) > 2 else None))
        elif kind == "gap":
            p.add(Spacer(b[1]))
        elif kind == "rule":
            p.add(Rule())
        elif kind == "page":
            p.break_page()
        else:
            raise ValueError(f"unknown block {kind}")
