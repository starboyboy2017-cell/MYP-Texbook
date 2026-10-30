"""Export the same block sources to an editable DOCX.

Structure follows the printed book: part and chapter headings, the planner,
the teaching sections, worked examples, practice and answers. Figures are
rendered from the vector sources at print resolution, so the Word file is a
complete manuscript rather than a text dump.
"""
import importlib
import io
import os
import re
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "content"))

import diagrams2  # noqa: E402
from bookkit import fonts  # noqa: E402

CHAPTERS = [
    ("ch01", 1, "Ratios and equivalent ratios"),
    ("ch02", 2, "Proportional reasoning"),
    ("ch03", 3, "Rates and unit rates"),
    ("ch04", 4, "Integers and operations"),
    ("ch05", 5, "Algebraic expressions and equations"),
    ("ch06", 6, "Numerical patterns and generalisation"),
    ("ch07", 7, "2D geometry: angles, perimeter and area"),
    ("ch08", 8, "3D geometry: solids, surface area and volume"),
    ("ch09", 9, "Transformations and symmetry"),
    ("ch10", 10, "Probability and simulation"),
    ("ch11", 11, "Univariate data"),
]

INK = RGBColor(0x15, 0x26, 0x3A)
TERRA = RGBColor(0xA6, 0x4B, 0x27)
MUTE = RGBColor(0x66, 0x71, 0x7A)
GREEN = RGBColor(0x42, 0x60, 0x4F)

PHOTOS = os.path.abspath(os.path.join(HERE, "..", "images", "photos"))
CROPS = os.path.abspath(os.path.join(HERE, "..", "images", "diagrams", "_crop"))


def plain(text):
    if text is None:
        return ""
    return re.sub(r"`([^`]*)`", r"\1", str(text))


def add_inline(par, text, size=10.0, colour=INK, italic=False):
    """Render **bold** and *italic* runs inside one paragraph."""
    text = plain(text)
    tokens = re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text)
    for tok in tokens:
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**"):
            run = par.add_run(tok[2:-2])
            run.bold = True
        elif tok.startswith("*") and tok.endswith("*"):
            run = par.add_run(tok[1:-1])
            run.italic = True
        else:
            run = par.add_run(tok)
        run.font.size = Pt(size)
        run.font.color.rgb = colour
        if italic:
            run.italic = True
    return par


def para(doc, text, size=10.0, colour=INK, space_after=6, italic=False,
         align=None, indent=None, style=None):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    if indent:
        p.paragraph_format.left_indent = Cm(indent)
    if align == "center":
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_inline(p, text, size=size, colour=colour, italic=italic)
    return p


def heading(doc, text, level=1, colour=INK, size=None, space_before=14):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(space_before)
    h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(plain(text))
    run.bold = level <= 2
    run.font.color.rgb = colour
    run.font.size = Pt(size or {1: 20, 2: 15, 3: 12, 4: 10.5}.get(level, 10))
    return h


def kicker(doc, text, colour=TERRA):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(plain(text).upper())
    run.bold = True
    run.font.size = Pt(8)
    run.font.color.rgb = colour
    return p


def render_diagram(name, height_pt, kwargs):
    """Draw one vector diagram to a transparent PNG at 200 dpi."""
    from reportlab.pdfgen import canvas as rl_canvas
    width_pt = 470.0
    buf = io.BytesIO()
    c = rl_canvas.Canvas(buf, pagesize=(width_pt, height_pt))
    fn = diagrams2.DIAGRAMS[name]
    fn(c, 0, 0, width_pt, height_pt, **(kwargs or {}))
    c.showPage()
    c.save()
    buf.seek(0)
    import pymupdf
    doc = pymupdf.open(stream=buf.read(), filetype="pdf")
    pix = doc[0].get_pixmap(dpi=220, alpha=False)
    out = os.path.join(CROPS, f"exp_{name}_{int(height_pt)}.png")
    os.makedirs(CROPS, exist_ok=True)
    pix.save(out)
    return out, width_pt / 72.0


def photo_for(name, aspect):
    """Uses the same centre crop the book uses, so DOCX and PDF agree."""
    from PIL import Image
    src = os.path.join(PHOTOS, name)
    im = Image.open(src).convert("RGB")
    w, h = im.size
    if w / h > aspect:
        nw = int(h * aspect)
        box = ((w - nw) // 2, 0, (w + nw) // 2, h)
    else:
        nh = int(w / aspect)
        box = (0, (h - nh) // 3, w, (h - nh) // 3 + nh)
    im = im.crop(box)
    out = os.path.join(CROPS, f"exp_{os.path.splitext(name)[0]}_"
                              f"{str(aspect).replace('.', 'p')}.jpg")
    os.makedirs(CROPS, exist_ok=True)
    im.save(out, quality=92)
    return out


def pic(doc, path, width_cm=15.0, caption=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(path, width=Cm(width_cm))
    if caption:
        para(doc, caption, size=8.5, colour=MUTE, space_after=10, italic=True)


def table(doc, head, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(head))
    t.style = "Light Grid Accent 1"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0].cells
    for i, h in enumerate(head):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        run = p.add_run(plain(h))
        run.bold = True
        run.font.size = Pt(8.5)
    for r in rows:
        cells = t.add_row().cells
        for i, v in enumerate(r):
            cells[i].text = ""
            p = cells[i].paragraphs[0]
            run = p.add_run(plain(v))
            run.font.size = Pt(8.5)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


def render_blocks(doc, blocks):
    for b in blocks:
        kind = b[0]
        if kind == "stage":
            kicker(doc, f"{b[1]} \u00b7 {b[2]}")
            if len(b) > 3 and b[3]:
                para(doc, b[3], size=9, colour=MUTE, italic=True, space_after=4)
        elif kind == "section":
            crit = b[3] if len(b) > 3 else None
            rel = b[4] if len(b) > 4 else []
            kicker(doc, f"Section {b[1]}", colour=TERRA)
            heading(doc, f"{b[1]}  {b[2]}", level=2, space_before=2)
            meta = []
            if crit:
                meta.append("Criterion " + plain(crit).replace("  ", " "))
            if rel:
                meta.append("Related concepts: " + ", ".join(rel))
            if meta:
                para(doc, "  \u00b7  ".join(meta), size=8.5, colour=MUTE,
                     space_after=8)
        elif kind == "pagetitle":
            heading(doc, b[1], level=2)
        elif kind == "lead":
            para(doc, b[1], size=11, italic=True, space_after=8)
        elif kind == "p":
            para(doc, b[1], size=10)
        elif kind == "h3":
            heading(doc, b[1], level=3, space_before=10)
        elif kind == "h4":
            heading(doc, b[1], level=4, space_before=8)
        elif kind == "ul":
            for it in b[1]:
                p = doc.add_paragraph(style="List Bullet")
                p.paragraph_format.space_after = Pt(2)
                add_inline(p, it, size=9.5)
        elif kind == "ol":
            for it in b[1]:
                p = doc.add_paragraph(style="List Number")
                p.paragraph_format.space_after = Pt(2)
                add_inline(p, it, size=9.5)
        elif kind == "panel":
            text, title, items = b[2], b[3], b[4] if len(b) > 4 else None
            if title:
                heading(doc, title, level=4, colour=GREEN, space_before=8)
            if text:
                for chunk in str(text).split("\n"):
                    if chunk.strip():
                        para(doc, chunk, size=9.5, space_after=3)
            if items:
                for it in items:
                    p = doc.add_paragraph(style="List Bullet")
                    p.paragraph_format.space_after = Pt(1)
                    add_inline(p, it, size=9.5)
        elif kind == "we":
            ref, title, problem, steps = b[1], b[2], b[3], b[4]
            heading(doc, f"Worked example {ref} \u00b7 {title}", level=3,
                    colour=TERRA, space_before=12)
            para(doc, problem, size=9.8)
            for i, s in enumerate(steps, 1):
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.6)
                p.paragraph_format.space_after = Pt(2)
                run = p.add_run(f"{i}  ")
                run.bold = True
                run.font.size = Pt(9)
                run.font.color.rgb = TERRA
                add_inline(p, s, size=9.5)
            if len(b) > 5 and b[5]:
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(4)
                run = p.add_run("ANSWER   ")
                run.bold = True
                run.font.size = Pt(8)
                run.font.color.rgb = GREEN
                add_inline(p, b[5], size=9.5)
            if len(b) > 6 and b[6]:
                para(doc, b[6], size=9, colour=MUTE, italic=True, space_after=8)
        elif kind == "practice":
            heading(doc, f"Practice {b[1]}", level=4, colour=GREEN,
                    space_before=10)
            para(doc, b[2], size=8, colour=MUTE, space_after=4)
            for i, q in enumerate(b[3], 1):
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.7)
                p.paragraph_format.first_line_indent = Cm(-0.7)
                p.paragraph_format.space_after = Pt(3)
                run = p.add_run(f"{i}.  ")
                run.bold = True
                run.font.size = Pt(9)
                run.font.color.rgb = TERRA
                add_inline(p, q["q"], size=9.5)
                if q.get("tag"):
                    t = p.add_run(f"   [{q['tag']}]")
                    t.font.size = Pt(7.5)
                    t.font.color.rgb = MUTE
        elif kind == "table":
            head, rows = b[1], b[2]
            cap = b[4] if len(b) > 4 else None
            table(doc, head, rows)
            if cap:
                para(doc, cap, size=8.5, colour=MUTE, italic=True, space_after=8)
        elif kind == "diag":
            name, kwargs = b[2], b[3] or {}
            cap = b[4] if len(b) > 4 else None
            path, w_in = render_diagram(name, b[1], kwargs)
            pic(doc, path, width_cm=min(15.0, w_in * 2.54), caption=cap)
        elif kind == "photo":
            path = photo_for(b[1], b[2])
            cap = b[3] if len(b) > 3 else None
            credit = b[4] if len(b) > 4 else None
            pic(doc, path, width_cm=12.5, caption=cap)
            if credit:
                para(doc, credit, size=7.5, colour=MUTE, space_after=8)
        elif kind == "card":
            heading(doc, f"{b[1]}  ({b[2]})", level=3, colour=TERRA)
            render_blocks(doc, b[4])
        elif kind == "formula":
            para(doc, b[1], size=11, align="center", space_after=4)
        elif kind == "statement":
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(8)
            run = p.add_run(plain(b[1]).upper() + "  ")
            run.bold = True
            run.font.size = Pt(8)
            run.font.color.rgb = TERRA
            add_inline(p, b[2], size=10.5, italic=True)
        elif kind == "chips":
            table(doc, ["", ""], [[k, v] for k, v in b[1]])
        elif kind == "rule":
            doc.add_paragraph("_" * 40).alignment = WD_ALIGN_PARAGRAPH.CENTER


def main(out_path):
    fonts.register()
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.2)
    sec.top_margin = sec.bottom_margin = Cm(2.0)
    style = doc.styles["Normal"]
    style.font.name = "Georgia"
    style.font.size = Pt(10)

    heading(doc, "MYP Mathematics 2", level=1, size=30)
    para(doc, "Student Coursebook \u00b7 Improved First Edition", size=13,
         colour=TERRA, space_after=4)
    para(doc, "SADIKOU MOUKODDIM", size=10, colour=MUTE, space_after=18)
    para(doc, "This Word file is generated from the same sources as the print "
              "edition, so every sentence, worked example, practice set and "
              "answer matches the PDF. Figures and photographs are embedded at "
              "print resolution. Edit the text freely; the pagination will "
              "differ from the PDF, which is expected.", size=9.5, colour=MUTE)

    for mod_name, cno, title in CHAPTERS:
        mod = importlib.import_module(mod_name)
        doc.add_page_break()
        plate = mod.PLATE
        kicker(doc, plate["part"])
        heading(doc, f"{cno}  {title}", level=1, size=24, space_before=4)
        para(doc, plate["kicker"] + "  \u00b7  key concept " +
             plate["key_concept"] + "  \u00b7  " +
             ", ".join(plate["related"]), size=8.5, colour=MUTE, space_after=8)
        for line in plate["lead_lines"]:
            para(doc, line, size=11, italic=True, space_after=2)
        para(doc, "Global context: " + plate["context"], size=9, colour=GREEN,
             space_after=10)
        render_blocks(doc, mod.BLOCKS)

        doc.add_page_break()
        heading(doc, f"Answers \u00b7 chapter {cno}", level=2)
        for sec_name, ans in mod.ANSWERS.items():
            kicker(doc, f"Practice {sec_name}", colour=GREEN)
            for i, a in enumerate(ans, 1):
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.7)
                p.paragraph_format.first_line_indent = Cm(-0.7)
                p.paragraph_format.space_after = Pt(2)
                run = p.add_run(f"{i}.  ")
                run.bold = True
                run.font.size = Pt(9)
                run.font.color.rgb = TERRA
                add_inline(p, a, size=9)

    doc.add_page_break()
    heading(doc, "Image credits", level=2)
    para(doc, "Photographs are used under the Pexels licence; each file's "
              "original listing is recorded in image_references/IMAGE_REGISTER.md. "
              "All diagrams are original vector artwork drawn for this edition.",
         size=9.5)
    doc.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../final/MYP2_Mathematics_"
                                                     "Improved_First_Edition.docx")
