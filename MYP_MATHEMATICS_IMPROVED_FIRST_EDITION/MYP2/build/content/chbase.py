"""Terse block-builders shared by every chapter manuscript.

Each helper returns one tuple from the declarative block vocabulary that
`render2.py` understands. Keeping the chapter sources as flat lists of these
calls means a chapter reads top to bottom like the printed page, and the same
list can be re-rendered at another measure without editing content.
"""

# ------------------------------------------------------------------ structure
def S(num, title, crit=None, rel=None):
    """Section head: 1.1 Understanding ratio language."""
    return ("section", num, title, crit, rel or [])


def ST(num, name, note=None):
    """Stage marker: 01 · ENGAGE."""
    return ("stage", num, name, note)


def TITLE(text, eyebrow=None):
    return ("pagetitle", text, eyebrow)


def P(text, space=0):
    return ("p", text, space)


def L(text):
    return ("lead", text)


def H(text):
    return ("h3", text)


def H4(text):
    return ("h4", text)


def UL(items):
    return ("ul", list(items))


def OL(items):
    return ("ol", list(items))


def GAP(h=8):
    return ("gap", h)


def RULE():
    return ("rule",)


def NEWPAGE():
    return ("page",)


# --------------------------------------------------------------------- panels
def DEF(text, title=None):
    return ("panel", "definition", text, title, None)


def KEY(text, title=None):
    return ("panel", "keyidea", text, title, None)


def ERR(text, title=None):
    return ("panel", "error", text, title, None)


def ATL(text, title="ATL \u00b7 Thinking skills"):
    return ("panel", "atl", text, title, None)


def NOTE(text, title=None):
    return ("panel", "note", text, title, None)


def VOCAB(text):
    return ("panel", "vocab", text, "Vocabulary to use precisely", None)


def MYP(text, title=None):
    return ("panel", "criteria", text, title, None)


def BOX(kind, title=None, text=None, items=None):
    return ("panel", kind, text, title, items)


# ------------------------------------------------------------------- examples
def WE(ref, title, problem, steps, answer=None, check=None):
    return ("we", ref, title, problem, list(steps), answer, check)


def PRAC(ref, ranges, items):
    return ("practice", ref, ranges, items)


def Q(text, tag=None, tag2=None):
    d = {"q": text}
    if tag:
        d["tag"] = tag
    if tag2:
        d["tag2"] = tag2
    return d


def TABLE(head, rows, widths=None, caption=None, fs=None, font_size=None):
    return ("table", head, rows, widths, caption, font_size or fs)


def DIAG(height, name, caption=None, width=None, **kwargs):
    return ("diag", height, name, kwargs, caption, width)


def PHOTO(name, aspect, caption, credit, width=None):
    return ("photo", name, aspect, caption, credit, width)


def CARD(title, chip, chip_colour, blocks):
    return ("card", title, chip, chip_colour, blocks)


def CARD_D(title, blocks):
    """A real-life application card in the original's 'CRITERION D' style."""
    return ("card", title, "Criterion D", "TERRA", blocks)


def CARD_I(title, blocks):
    """An investigation card in the original's 'INVESTIGATION' style."""
    return ("card", title, "Investigation", "GOLD", blocks)


def STATEMENT(label, text):
    return ("statement", label, text)


def CHIPS(pairs):
    return ("chips", list(pairs))


def FORMULA(text, note=None):
    return ("formula", text, note)


TAG_COLOURS = {"TERRA": "TERRACOTTA", "GOLD": "GOLD_DEEP", "SAGE": "SAGE",
               "SLATE": "SLATE"}
