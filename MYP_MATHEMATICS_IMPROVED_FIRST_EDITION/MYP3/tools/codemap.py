"""The byte code -> character table the MYP3 book was drawn with.

The shipped PDF lost its font programs and its ToUnicode maps, but it kept the
one thing that could not be faked: every /Widths array.  Each face was matched
against its upstream release (tools/fetch_fonts.py) and reproduces its advance
widths to 1/1000 em, so a code's advance usually names its character.

The book was built with a different subset per face, so each face has its own
code line.  Three readings were used and they agree:

  * advance - the /Widths entry for a code equals the advance of a character in
              that face (371/2, 653/4, 635 only the therefore sign, 1172 only
              the triangle);
  * legend  - page 12 prints a symbol table naming 21 maths signs, and every one
              of their codes resolves to that character's advance;
  * context - the damaged line aligned against the same sentence in the DOCX,
              which kept most of these characters ("the symbols ±∞ never take a
              square bracket", "√5, π and −7/3").

Codes 32..126 are the ASCII characters themselves.  A code a face does not use
keeps an empty glyph, which is what the builder's own placeholder did.
"""

# Inter Regular: used for criterion bands and running text.
INTER_REGULAR = {
    0x01: "\u2014",   # em dash
    0x02: "\u2013",   # en dash
    0x03: "\u201c",
    0x04: "\u201d",
}

# Inter Medium: running heads and support lines.
INTER_MEDIUM = {
    0x01: "\u00b7",   # middle dot in "PART II · RELATIONSHIPS"
    0x02: "\u2026",   # ellipsis
    0x03: "\u2013",
}

# Inter SemiBold: headings, practice bands, criterion labels.
INTER_SEMIBOLD = {
    0x01: "\u00b7",
    0x02: "\u2014",
    0x03: "\u00b2",   # cm squared
    0x04: "\u00b3",   # cm cubed
    0x05: "\u2013",
}

# Playfair Regular: chapter plate numerals and title ornaments.
PLAYFAIR_REGULAR = {
}

# Playfair SemiBold: theorem and box headings.
PLAYFAIR_SEMIBOLD = {
    0x01: "\u2014",
    0x02: "\u221a",   # radical in "Irrationality of √2"
    0x03: "\u00b7",
    0x04: "\u201c",
    0x05: "\u201d",
}

# Playfair Italic: the plate standfirsts and running heads.
PLAYFAIR_ITALIC = {
    0x01: "\u00b7",   # the middle dot in every running head "1 \u00b7 The real number system"
}

# STIX Two Text Regular: body text.  Codes 27..31 and 127 hold only the
# builder's placeholder here, so they stay empty.
STIX_TEXT_REGULAR = {
    0x00: "\u221a",   # radical: the only 605-advance character
    0x01: "\u2014",
    0x02: "\u00b7",
    0x03: "\u00a9",
    0x04: "\u201c",
    0x05: "\u201d",
    0x06: "\u2013",
    0x07: "\u2026",
    0x08: "\u2022",
    0x09: "\u03b5",   # epsilon, in "Rigorous \u03b5-\u03b4 arguments"
    0x0A: "\u0305",   # combining macron: the repeating-digit bar, zero advance
    0x0B: "\u211d",
    0x0C: "\u211a",
    0x0D: "\u2124",
    0x0E: "\u2115",
    0x0F: "\u00b3",
    0x10: "\u207f",
    0x11: "\u2074",
    0x12: "\u00b2",
    0x13: "\u00bd",
    0x14: "\u2081",
    0x15: "\u2082",
    0x16: "\u2153",
    0x17: "\u2154",
    0x18: "\u2044",   # fraction slash
    0x1A: "\u03c1",   # rho
}

STIX_TEXT_ITALIC = {
    0x00: "\u221a",
    0x01: "\u201c",
    0x02: "\u201d",
    0x03: "\u03c0",
    0x04: "\u2014",
    0x05: "\u03b8",
}

STIX_TEXT_SEMIBOLD = {
    0x01: "\u2026",
    0x02: "\u00b7",
    0x03: "\u2013",
}

# The maths face carries one sign per code.  Page 12 of the book prints a
# symbol table naming 21 of them, and each of those resolves to the advance of
# the character its row names; the rest are read from their use in the book.
STIX_MATH = {
    0x01: "\u00b7",
    0x02: "\u2208",   # is an element of
    0x03: "\u2209",   # is not an element of
    0x04: "\u221a",   # radical
    0x05: "\u211a",
    0x06: "\u2282",   # is a subset of
    0x07: "\u2115",
    0x08: "\u2124",
    0x09: "\u21d2",   # implies
    0x0A: "\u21d4",   # if and only if
    0x0B: "\u2234",   # therefore
    0x0C: "\u2260",   # is not equal to
    0x0D: "\u2248",   # is approximately equal to
    0x0E: "\u03c0",   # pi
    0x0F: "\u2245",   # is congruent to
    0x10: "\u25b3",   # triangle
    0x11: "\u223c",   # is similar to
    0x12: "\u2220",   # angle
    0x13: "\u00b0",   # degree
    0x14: "\u22a5",   # perpendicular to
    0x15: "\u2225",   # parallel to
    0x16: "\u00d7",   # multiplication sign: every exponent product in the book
    0x17: "\u2212",   # minus sign, in "\u22127/3" and every negative number
    0x18: "\u03b4",   # delta, in "Rigorous \u03b5-\u03b4 arguments" (479 advance)
    0x19: "\u00f7",   # division sign (720)
    0x1A: "\u2265",   # greater than or equal (720)
    0x1B: "<",        # comparison (720)
    0x1C: "\u221e",   # infinity, "the symbols \u00b1\u221e" (953)
    0x1D: "\u2264",   # less than or equal: the builder drew LE here and
                      # the outline came from the plus slot (720)
    0x1E: "\u211d",   # "\u211a \u2282 \u211d" (729)
    0x1F: "\u03b8",   # theta, "sin \u03b8" (514)
    0x80: "\u2192",   # right arrow, sequence table (948)
    0x81: "\u03a3",   # capital sigma, mean formula (604)
    0x82: "\u222a",   # union, P(A \u222a B) (636)
    0x83: "\u2229",   # intersection, P(A \u2229 B) (636)
}

CODES = {
    "Inter-Regular": INTER_REGULAR,
    "Inter-Medium": INTER_MEDIUM,
    "Inter-SemiBold": INTER_SEMIBOLD,
    "PlayfairDisplay-Regular": PLAYFAIR_REGULAR,
    "PlayfairDisplay-SemiBold": PLAYFAIR_SEMIBOLD,
    "PlayfairDisplay-Italic": PLAYFAIR_ITALIC,
    "STIXTwoText-Regular": STIX_TEXT_REGULAR,
    "STIXTwoText-Italic": STIX_TEXT_ITALIC,
    "STIXTwoText-SemiBold": STIX_TEXT_SEMIBOLD,
    "STIXTwoMath-Regular": STIX_MATH,
}


def table(face):
    """The full code map for a face, ASCII included."""
    m = {c: chr(c) for c in range(32, 127)}
    m.update(CODES.get(face, {}))
    return m


def decode(face, code):
    return table(face).get(code, "\ufffd")


def codes(face):
    """Character -> code, the inverse of `table`."""
    return {ch: code for code, ch in table(face).items()}
