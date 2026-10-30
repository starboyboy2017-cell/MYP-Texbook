"""Export the chapter sources to Markdown for the manuscript folder.

The build reads Python block lists so that the printed pages and the editable
manuscript can never drift apart: this script is the second reader of the same
source.
"""
import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "content"))

OUT = os.path.abspath(os.path.join(HERE, "..", "manuscript"))

CHAPTERS = [
    ("ch01", 1, "Ratios and equivalent ratios"),
    ("ch02", 2, "Proportional reasoning"),
    ("ch03", 3, "Rates and unit rates"),
    ("ch04", 4, "Integers and operations"),
    ("ch05", 5, "Algebraic expressions and equations"),
    ("ch06", 6, "Numerical patterns and generalisation"),
    ("ch07", 7, "2D geometry: angles, perimeter and area"),
    ("ch08", 8, "3D solids, surface area and volume"),
    ("ch09", 9, "Transformations and symmetry"),
    ("ch10", 10, "Probability and simulation"),
    ("ch11", 11, "Univariate data"),
]


def plain(text):
    """Strip the inline markup used by the renderer down to readable markdown."""
    if text is None:
        return ""
    text = str(text)
    text = re.sub(r"`([^`]*)`", r"*\1*", text)
    text = text.replace("\\u00b7", "\u00b7")
    return text


def render_blocks(blocks, depth=0):
    out = []
    ind = ""
    for b in blocks:
        kind = b[0]
        if kind == "stage":
            num, name = b[1], b[2]
            note = b[3] if len(b) > 3 else None
            out.append(f"### {num} \u00b7 {name}\n")
            if note:
                out.append(f"*{plain(note)}*\n")
        elif kind == "section":
            num, title = b[1], b[2]
            crit = b[3] if len(b) > 3 else None
            rel = b[4] if len(b) > 4 else []
            out.append(f"## {num} {title}\n")
            meta = []
            if crit:
                meta.append(f"**Criterion {plain(crit).replace('  ', ' ')}**")
            if rel:
                meta.append("Related concepts: " + ", ".join(rel))
            if meta:
                out.append(" \u00b7 ".join(meta) + "\n")
        elif kind == "pagetitle":
            out.append(f"# {plain(b[1])}\n")
        elif kind == "lead":
            out.append(f"> {plain(b[1])}\n")
        elif kind == "p":
            out.append(plain(b[1]) + "\n")
        elif kind == "h3":
            out.append(f"### {plain(b[1])}\n")
        elif kind == "h4":
            out.append(f"#### {plain(b[1])}\n")
        elif kind == "ul":
            for it in b[1]:
                out.append(f"- {plain(it)}")
            out.append("")
        elif kind == "ol":
            for i, it in enumerate(b[1], 1):
                out.append(f"{i}. {plain(it)}")
            out.append("")
        elif kind == "panel":
            text, title, items = b[2], b[3], b[4]
            if title:
                out.append(f"**{plain(title)}**\n")
            if text:
                out.append(plain(text) + "\n")
            if items:
                for it in items:
                    out.append(f"- {plain(it)}")
                out.append("")
        elif kind == "we":
            ref, title, problem, steps = b[1], b[2], b[3], b[4]
            out.append(f"**Worked example {ref} \u2014 {plain(title)}**\n")
            out.append(plain(problem) + "\n")
            for i, s in enumerate(steps, 1):
                out.append(f"{i}. {plain(s)}")
            out.append("")
            if len(b) > 5 and b[5]:
                out.append(f"*Answer:* {plain(b[5])}\n")
            if len(b) > 6 and b[6]:
                out.append(f"*Check:* {plain(b[6])}\n")
        elif kind == "practice":
            out.append(f"**Practice {b[1]}** \u00b7 {plain(b[2])}\n")
            for i, q in enumerate(b[3], 1):
                tag = q.get("tag") or ""
                out.append(f"{i}. {plain(q['q'])}" + (f"  [{tag}]" if tag else ""))
            out.append("")
        elif kind == "table":
            head, rows = b[1], b[2]
            cap = b[4] if len(b) > 4 else None
            if cap:
                out.append(f"*{plain(b[4])}*\n")
            out.append("| " + " | ".join(plain(h) for h in head) + " |")
            out.append("|" + "|".join(["---"] * len(head)) + "|")
            for r in rows:
                out.append("| " + " | ".join(plain(c) for c in r) + " |")
            out.append("")
        elif kind == "diag":
            cap = b[4] if len(b) > 4 else None
            name = b[2] if isinstance(b[2], str) else "diagram"
            out.append(f"[Figure: {name}" + (f" \u2014 {plain(cap)}" if cap else "") + "]\n")
        elif kind == "photo":
            out.append(f"[Photograph: {b[1]} \u2014 {plain(b[3])}]\n")
        elif kind == "card":
            out.append(f"### {plain(b[1])}  ({plain(b[2])})\n")
            out.extend(render_blocks(b[4], depth + 1))
        elif kind == "formula":
            out.append(f"$$ {plain(b[1])} $$")
            if len(b) > 2 and b[2]:
                out.append(f"*{plain(b[2])}*")
            out.append("")
        elif kind == "statement":
            out.append(f"**{plain(b[1])}.** {plain(b[2])}\n")
        elif kind == "chips":
            for lab, val in b[1]:
                out.append(f"- {plain(lab)}: {plain(val)}")
            out.append("")
        elif kind == "gap":
            pass
        elif kind == "rule":
            out.append("---\n")
        elif kind == "page":
            out.append("\f\n")
    return out


def answers_md(mod, cno):
    lines = [f"## Answers \u00b7 chapter {cno}\n"]
    for sec, ans in mod.ANSWERS.items():
        lines.append(f"**{sec}**\n")
        for i, a in enumerate(ans, 1):
            lines.append(f"{i}. {plain(a)}")
        lines.append("")
    return lines


def _letterspaced(line):
    toks = line.split()
    if len(toks) >= 2 and all(len(t) == 1 and t.isupper() for t in toks):
        return True
    if len(toks) < 4:
        return False
    single = sum(1 for t in toks if len(t) == 1 and t.isalnum())
    return single / len(toks) > 0.55


def _page_text(page):
    lines = []
    for raw in page.get_text().splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            lines.append("")
            continue
        if s.isdigit() or _letterspaced(s):
            continue
        lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"-\n(?=[a-z])", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def export_matter(pdf_path):
    """Front and back matter are drawn page by page rather than as block lists,
    so their Markdown extract is read back from the delivered PDF."""
    import pymupdf
    doc = pymupdf.open(pdf_path)
    total = doc.page_count
    runs = [("front_matter", range(0, 15), "Front matter"),
            ("back_matter", range(224, total), "Back matter")]
    for name, pages, title in runs:
        out = [f"# {title}\n"]
        out.append("*Text extract of the typeset pages, in reading order. The PDF in "
                   "`../final/` is the authoritative edition; letter-spaced display "
                   "labels, running heads and folios are omitted.*\n")
        for i in pages:
            out.append(f"<!-- printed page {i + 1} -->")
            out.append(_page_text(doc[i]) + "\n")
        path = os.path.join(OUT, name + ".md")
        with open(path, "w") as fh:
            fh.write("\n".join(out))
        print("wrote", path)


def main():
    os.makedirs(OUT, exist_ok=True)
    for mod_name, cno, title in CHAPTERS:
        mod = importlib.import_module(mod_name)
        plate = mod.PLATE
        lines = [f"# Chapter {cno} \u00b7 {title}\n"]
        lines.append(f"*{plate['part']}* \u00b7 key concept **{plate['key_concept']}** "
                     f"\u00b7 related concepts: {', '.join(plate['related'])}\n")
        lines.append(f"Global context: {plate['context']}\n")
        lines.append("\n".join(plain(x) for x in plate["lead_lines"]) + "\n")
        lines.extend(render_blocks(mod.BLOCKS))
        lines.extend(answers_md(mod, cno))
        path = os.path.join(OUT, f"chapter_{cno:02d}.md")
        with open(path, "w") as fh:
            fh.write("\n".join(lines).replace("\n\n\n", "\n\n"))
        print("wrote", path)
    pdf = os.path.abspath(os.path.join(HERE, "..", "final",
          "MYP2_Mathematics_Improved_First_Edition.pdf"))
    if os.path.exists(pdf):
        export_matter(pdf)


if __name__ == "__main__":
    main()
