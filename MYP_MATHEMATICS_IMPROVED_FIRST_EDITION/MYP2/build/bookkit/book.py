"""The Book object: pages, frames, running heads and folios.

Layout grid
-----------
One continuous reading column of 425 pt inside 85 pt margins, exactly as the
original first edition sets its pages. What changes is the discipline around it:
the column sits on a 14.2 pt baseline, the running head and the folio always
fall on the *outer* edge (they do not in the original, where both are pinned to
the left of every page), and every plate shares one vertical rhythm.
"""
from reportlab.pdfgen import canvas as rl_canvas

from . import spec, typeset
from .markup import plain
from .flow import Frame

ROMAN = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi",
         "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx"]

WORDMARK = "MYP MATHEMATICS 2  \u00b7  STUDENT COURSEBOOK"


class Book:
    def __init__(self, path, title="", author="", subject="", wordmark=None):
        self.c = rl_canvas.Canvas(path, pagesize=(spec.PAGE_W, spec.PAGE_H))
        self.canvas = self.c
        self.c.setTitle(title)
        self.c.setAuthor(author)
        self.c.setSubject(subject)
        self.c.setCreator("MYP Mathematics 2 - Improved First Edition")
        self.c.setKeywords("MYP mathematics Year 2 student coursebook inquiry "
                           "ratio proportion algebra geometry probability statistics")
        self.wordmark = wordmark or WORDMARK
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
        """Folios run as one sequence across the whole book (cover = page 1)."""
        self.numbering = "arabic"

    def label_for(self, physical=None):
        p = physical if physical is not None else self.pages
        return str(p)

    def _margins(self):
        return spec.MARGIN_INNER, spec.MARGIN_OUTER

    def apply_layout(self, template):
        self.template = template
        left, right = self.left, self.right
        top = spec.PAGE_H - spec.MARGIN_TOP
        bottom = spec.MARGIN_BOTTOM
        h = top - bottom
        self.margin_frame = None
        if template in ("body", "body1", "wide", "plain"):
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

        if template in ("body", "body1", "wide"):
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
        recto = self.pages % 2 == 1
        outer = spec.PAGE_W - self.right
        c.saveState()
        if self.chapter_label:
            typeset.draw(c, spec.PAGE_W - self.right if recto else self.left, base,
                         plain(self.chapter_label), "SourceSerifItalic", 8.1,
                         spec.INK_MUTE, 0, "right" if recto else "left")
        if self.part_label:
            typeset.draw(c, self.left if recto else outer, base,
                         plain(self.part_label).upper(), "Inter-Semi", 6.3,
                         spec.RULE if False else spec.INK_MUTE, 1.5,
                         "left" if recto else "right")
        c.restoreState()
        self._folio()

    def _folio(self):
        c = self.c
        self.page_empty = False
        recto = self.pages % 2 == 1
        c.saveState()
        if recto:
            typeset.draw(c, spec.PAGE_W - self.right, spec.FOLIO_Y, self.page_label,
                         "Inter-Semi", 7.8, spec.TERRACOTTA, 0, "right")
            typeset.draw(c, self.left, spec.FOLIO_Y, self.wordmark,
                         "Inter", 6.3, spec.INK_MUTE, 1.15)
        else:
            typeset.draw(c, self.left, spec.FOLIO_Y, self.page_label,
                         "Inter-Semi", 7.8, spec.TERRACOTTA, 0)
            typeset.draw(c, spec.PAGE_W - self.right, spec.FOLIO_Y, self.wordmark,
                         "Inter", 6.3, spec.INK_MUTE, 1.15, "right")
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
