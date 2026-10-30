"""High quality text drawing with true pair kerning and letterspacing.

reportlab draws strings with the font's advance widths only. For display sizes
that is visibly loose ("MATHEMATICS", "AV", "To"), so this module reads the
GPOS kerning table of the shipped faces and applies it while drawing, and it
implements real letterspacing in points rather than faking it with spaces.
"""
import os

from fontTools.ttLib import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth

from . import spec

FONT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "fonts")

_FACE_FILES = {
    "Playfair": "pf-400-60.ttf", "Playfair-Med": "pf-500-60.ttf",
    "Playfair-Semi": "pf-600-60.ttf", "Playfair-Bold": "pf-700-60.ttf",
    "Playfair-Display": "pf-400-96.ttf", "Playfair-DisplayMed": "pf-500-96.ttf",
    "PlayfairItalic": "pfi-400-60.ttf", "PlayfairItalic-Med": "pfi-500-60.ttf",
    "SourceSerif": "ss-400-17.ttf", "SourceSerif-Semi": "ss-600-17.ttf",
    "SourceSerif-Bold": "ss-700-17.ttf", "SourceSerifItalic": "ssi-400-17.ttf",
    "Inter": "in-400-14.ttf", "Inter-Med": "in-500-14.ttf",
    "Inter-Semi": "in-600-14.ttf", "Inter-Bold": "in-700-14.ttf",
}

_cache = {}


class Face:
    def __init__(self, path):
        f = TTFont(path, lazy=False)
        self.upem = f["head"].unitsPerEm
        self.cmap = {}
        for t in f["cmap"].tables:
            self.cmap.update(t.cmap)
        self.hmtx = f["hmtx"]
        self.kern = {}
        if "GPOS" in f:
            try:
                self._load_gpos(f["GPOS"].table)
            except Exception:
                pass

    def _load_gpos(self, gpos):
        for lookup in gpos.LookupList.Lookup:
            if lookup.LookupType == 2:
                for st in lookup.SubTable:
                    self._load_pair(st)
            elif lookup.LookupType == 9:
                for st in lookup.SubTable:
                    for sub in getattr(st, "ExtSubTable", []) or []:
                        self._load_pair(sub)

    def _load_pair(self, st):
        if st.Format == 1:
            cov = st.Coverage.glyphs
            for first, pset in zip(cov, st.PairSet):
                d = self.kern.setdefault(first, {})
                for pv in pset.PairValueRecord:
                    if pv.Value1 and getattr(pv.Value1, "XAdvance", 0):
                        d[pv.SecondGlyph] = pv.Value1.XAdvance
        elif st.Format == 2:
            cov = st.Coverage.glyphs
            c1 = st.ClassDef1.classDefs
            c2 = st.ClassDef2.classDefs
            recs = st.Class1Record
            for first in cov:
                a = c1.get(first, 0)
                if a >= len(recs):
                    continue
                d = self.kern.setdefault(first, {})
                for glyph in cov:
                    b = c2.get(glyph, 0)
                    if b >= len(recs[a].Class2Record):
                        continue
                    v = recs[a].Class2Record[b].Value1
                    if v and getattr(v, "XAdvance", 0):
                        d[glyph] = v.XAdvance

    def adv(self, ch):
        g = self.cmap.get(ord(ch))
        if g is None:
            return 0.5 * self.upem
        return self.hmtx[g][0]

    def kern_pts(self, a, b, size):
        ga = self.cmap.get(ord(a))
        gb = self.cmap.get(ord(b))
        if ga is None or gb is None:
            return 0.0
        d = self.kern.get(ga)
        if not d:
            return 0.0
        return d.get(gb, 0) / self.upem * size


def face(name):
    if name not in _cache:
        _cache[name] = Face(os.path.join(FONT_DIR, _FACE_FILES[name]))
    return _cache[name]


def width(text, name, size, tracking=0.0):
    """Advance width in points, with kerning and tracking."""
    try:
        f = face(name)
    except KeyError:
        return stringWidth(text, name, size)
    w = 0.0
    prev = None
    for ch in text:
        if prev is not None:
            w += f.kern_pts(prev, ch, size)
        w += f.adv(ch) / f.upem * size + tracking
        prev = ch
    return w - tracking if text else 0.0


def draw(c, x, y, text, name, size, colour, tracking=0.0, align="left"):
    """Draw kerned (and optionally letterspaced) text. Returns the width."""
    if not text:
        return 0.0
    try:
        f = face(name)
    except KeyError:
        f = None
    w = width(text, name, size, tracking)
    if align == "right":
        x -= w
    elif align == "center":
        x -= w / 2
    c.saveState()
    c.setFillColor(colour)
    c.setFont(name, size)
    if f is None or (not f.kern and abs(tracking) < 0.001):
        c.drawString(x, y, text)
        c.restoreState()
        return w

    cur_x = x
    prev = None
    buf = ""

    def flush(px, b):
        if b:
            c.drawString(px, y, b)
            return width(b, name, size)
        return 0.0

    for ch in text:
        k = f.kern_pts(prev, ch, size) if prev else 0.0
        if k:
            cur_x += flush(cur_x, buf)
            buf = ""
            cur_x += k
        buf += ch
        prev = ch
        if abs(tracking) > 0.001:
            cur_x += flush(cur_x, buf)
            buf = ""
            cur_x += tracking
    flush(cur_x, buf)
    c.restoreState()
    return w


def fit(text, name, size, max_w, min_size=8):
    """Largest size <= size that fits max_w."""
    s = size
    while s > min_size and width(text, name, s) > max_w:
        s -= 0.5
    return s
