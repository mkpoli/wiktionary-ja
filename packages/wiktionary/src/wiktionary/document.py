from .style import Style


class Section:
    title: str
    level: int
    content: str
    subsections: list["Section"]

    def __init__(self, title, level, content="", subsections=None):
        self.title = title
        self.level = level
        self.content = content
        self.subsections = list(subsections) if subsections else []

    def to_wikitext(self, style: Style) -> str:
        equal_signs = "=" * self.level
        space = " " if style.space_in_headings else ""
        heading = f"{equal_signs}{space}{self.title}{space}{equal_signs}"
        empty_line = "\n" if style.empty_line_after_headings else ""

        return f"{heading}\n{empty_line}{self.content}\n"

    def add_subsection(self, section: "Section") -> None:
        self.subsections.append(section)

    def __str__(self) -> str:
        return self.to_wikitext(Style())


class Document:
    style: Style
    sections: list[Section]

    def __init__(self, sections=None, style=None):
        self.style = Style() if style is None else style
        self.sections = [] if sections is None else sections

    def add_section(self, section: Section) -> None:
        self.sections.append(section)

    def __str__(self):
        # return "\n".join([section.to_wikitext(self.style) for section in self.sections])

        # expand subsections as [section, subsection, subsection, section, subsection, subsection, ...]
        sections = []
        for section in self.sections:
            sections.append(section)
            sections.extend(section.subsections)
        return "\n".join([section.to_wikitext(self.style) for section in sections])
