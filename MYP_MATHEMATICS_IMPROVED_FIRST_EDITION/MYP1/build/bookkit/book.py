"""The Book object: pages, frames, running heads and folios.

Layout grid
-----------
A recto page puts the reading column at the inner (left) margin and the note
column at the outer (right) edge; a verso page mirrors it. Full-width blocks
span both. This keeps the original edition's single continuous reading column
while shortening the measure to a comfortable 318 pt (about 68 characters) and
giving definitions, figures and asides a proper home in the margin.
"""
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas as rl_canvas

from . import spec, typeset
from .markup import plain
from .flow import Frame

ROMAN = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi",
         "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx"]


class Book:
    def __init__(self, path, title="", author="", subject=""):
        self.c = rl_canvas.Canvas(path, pagesize=(spec.PAGE_W, spec.PAGE_H))
        self.canvas = self.c
        self.c.setTitle(title)
        self.c.setAuthor(author)
        self.c.setSubject(subject)
        self.c.setCreator("MYP Mathematics 1 - Improved First Edition")
        self.pages = 0
        self.numbering = "roman"
        self.arabic_start = 0
        self.part_label = ""
        self.chapter_label = ""
        self.frames = []
        self.margin_frame = None
        self.full_width = spec.TEXT_W
        self.main_w = spec.MAIN_W
        self.page_label = ""
        self.page_empty = False
        self.labels = {}
        self.suppress_marks = False

    # ------------------------------------------------------------------ pages
    def start_body(self):
        self.numbering = "arabic"
        self.arabic_start = self.pages + 1

    def label_for(self, physical=None):
        p = physical if physical is not None else self.pages
        if self.numbering == "arabic":
            return str(p - self.arabic_start + 1)
        return ROMAN[p] if p < len(ROMAN) else str(p)

    def _margins(self):
        """recto (odd): inner margin on the left; verso: mirrored."""
        if self.pages % 2 == 1:
            return spec.MARGIN_INNER, spec.MARGIN_OUTER
        return spec.MARGIN_OUTER, spec.MARGIN_INNER

    def apply_layout(self, template):
        """Set the column layout of the current page without drawing furniture."""
        self.template = template
        left, right = self.left, self.right
        top = spec.PAGE_H - spec.MARGIN_TOP
        bottom = spec.MARGIN_BOTTOM
        h = top - bottom
        self.margin_frame = None
        if template in ("body", "body1"):
            self.full_width = spec.TEXT_W
            self.main_w = spec.MAIN_W
            if self.pages % 2 == 1:
                mx = left
                nx = left + spec.MAIN_W + spec.GUTTER
            else:
                nx = left + spec.MARGIN_W + spec.GUTTER
                mx = left
            self.frames = [Frame(mx, bottom, spec.MAIN_W, h, 0)]
            self.margin_frame = Frame(nx, bottom, spec.MARGIN_W, h, 1)
        elif template == "wide":
            self.full_width = spec.TEXT_W
            self.main_w = spec.TEXT_W
            self.frames = [Frame(left, bottom, spec.TEXT_W, h, 0)]
        elif template == "plain":
            self.full_width = spec.TEXT_W
            self.main_w = spec.TEXT_W
            self.frames = [Frame(left, bottom, spec.TEXT_W, h, 0)]
        else:
            self.frames = []
        return self

    def new_page(self, template="body"):
        if self.pages:
            self.c.showPage()
        self.pages += 1
        self.page_empty = True
        self.page_label = self.label_for()
        self.labels[self.pages] = self.page_label
        left, right = self._margins()
        self.left, self.right = left, right
        top = spec.PAGE_H - spec.MARGIN_TOP
        bottom = spec.MARGIN_BOTTOM
        h = top - bottom
        self.template = template
        self.margin_frame = None

        if template in ("body", "body1"):
            self.full_width = spec.TEXT_W
            self.main_w = spec.MAIN_W
            if self.pages % 2 == 1:
                mx = left
                nx = left + spec.MAIN_W + spec.GUTTER
            else:
                nx = left
                mx = left + spec.MARGIN_W + spec.GUTTER
            self.frames = [Frame(mx, bottom, spec.MAIN_W, h, 0)]
            self.margin_frame = Frame(nx, bottom, spec.MARGIN_W, h, 1)
            self._running_head()
        elif template == "wide":
            self.full_width = spec.TEXT_W
            self.main_w = spec.TEXT_W
            self.frames = [Frame(left, bottom, spec.TEXT_W, h, 0)]
            self._running_head()
        elif template == "plain":
            self.full_width = spec.TEXT_W
            self.main_w = spec.TEXT_W
            self.frames = [Frame(left, bottom, spec.TEXT_W, h, 0)]
        elif template == "none":
            self.frames = []
        return self

    # --------------------------------------------------------------- furniture
    def _running_head(self):
        if self.suppress_marks:
            return
        c = self.c
        base = spec.HEAD_TEXT_Y
        c.saveState()
        if self.part_label:
            typeset.draw(c, self.left, base, plain(self.part_label).upper(),
                         "Inter-Semi", 6.3, spec.INK_MUTE, 1.45)
        if self.chapter_label:
            c.setFillColor(spec.INK_MUTE)
            typeset.draw(c, spec.PAGE_W - self.right, base, plain(self.chapter_label),
                         "SourceSerifItalic", 7.7, spec.INK_MUTE, 0, "right")
        c.setStrokeColor(spec.RULE_SOFT)
        c.setLineWidth(0.5)
        c.line(self.left, spec.HEAD_RULE_Y + 3, spec.PAGE_W - self.right,
               spec.HEAD_RULE_Y + 3)
        c.restoreState()
        self._folio()

    def _folio(self):
        c = self.c
        recto = self.pages % 2 == 1
        c.saveState()
        if recto:
            typeset.draw(c, spec.PAGE_W - self.right, spec.FOLIO_Y, self.page_label,
                         "Inter-Semi", 7.8, spec.TERRACOTTA, 0, "right")
            typeset.draw(c, self.left, spec.FOLIO_Y,
                         "MYP MATHEMATICS 1  \u00b7  STUDENT COURSEBOOK",
                         "Inter", 6.3, spec.INK_MUTE, 1.15)
        else:
            typeset.draw(c, self.left, spec.FOLIO_Y, self.page_label,
                         "Inter-Semi", 7.8, spec.TERRACOTTA, 0)
            typeset.draw(c, spec.PAGE_W - self.right, spec.FOLIO_Y,
                         "MYP MATHEMATICS 1  \u00b7  STUDENT COURSEBOOK",
                         "Inter", 6.3, spec.INK_MUTE, 1.15, "right")
        c.setStrokeColor(spec.RULE_SOFT)
        c.setLineWidth(0.5)
        c.line(self.left, spec.FOLIO_Y + 11, spec.PAGE_W - self.right,
               spec.FOLIO_Y + 11)
        c.restoreState()

    # ------------------------------------------------------------------- utils
    def fill_page(self, colour):
        c = self.c
        c.saveState()
        c.setFillColor(colour)
        c.rect(0, 0, spec.PAGE_W, spec.PAGE_H, stroke=0, fill=1)
        c.restoreState()

    def save(self):
        self.c.showPage()
        self.c.save()
