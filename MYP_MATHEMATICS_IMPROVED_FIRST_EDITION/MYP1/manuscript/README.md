# Manuscript — text extracts

One file per chapter, plus `front_matter.md` and `back_matter.md`. Each file is a plain
text extract of the typeset pages, in reading order, with an HTML comment marking the
printed page number before every page:

```
<!-- printed page 42 -->
```

What the extract contains: all running text, definitions, key ideas, common errors,
worked-example steps, questions, captions, table cells, answers, glossary and index
entries. Word totals are ≈ 75 000 across the book.

What the extract does not contain:

* **Letter-spaced display labels** (part name, chapter number, stage kicker, panel
  kicker). They are part of the page design, not the reading text, and they would extract
  as one letter per space.
* **Vector artwork.** Figures and diagrams are drawn into the PDF and have no text layer;
  their captions are present, so every figure is still identifiable.
* **Typesetting detail.** Line breaks in the extract are the line breaks of the typeset
  page, so paragraphs are wrapped, not reflowed.

The PDF in `../final/` is the authoritative edition. These files exist so that the text can
be searched, counted and quoted without opening the PDF.
