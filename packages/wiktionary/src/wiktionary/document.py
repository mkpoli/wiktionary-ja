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

    @classmethod
    def from_wikitext(cls, text: str) -> "Section":
        """Parse a section from wikitext.

        Args:
            text: The wikitext to parse

        Returns:
            A new Section instance
        """
        lines = text.strip().split("\n")
        if not lines:
            raise ValueError("Empty text")

        # Parse heading
        heading = lines[0].strip()
        if not heading:  # Check for empty heading after stripping
            raise ValueError("Empty text")
        if not heading.startswith("="):
            raise ValueError(f"Invalid heading: {heading}")

        # Count equal signs to determine level
        level = 0
        for char in heading:
            if char != "=":
                break
            level += 1

        # Extract title (strip equal signs and spaces)
        title = heading.strip("= ")

        # Everything after heading is content
        content = "\n".join(lines[1:]).strip()

        return cls(title=title, level=level, content=content)

    def to_wikitext(self, style: Style) -> str:
        equal_signs = "=" * self.level
        space = " " if style.space_in_headings else ""
        heading = f"{equal_signs}{space}{self.title}{space}{equal_signs}"
        # Only add empty line if both style requires it and there is content
        empty_line = "\n" if style.empty_line_after_headings and self.content else ""

        return f"{heading}\n{empty_line}{self.content}\n"

    def add_subsection(self, section: "Section") -> None:
        self.subsections.append(section)

    def __str__(self) -> str:
        return self.to_wikitext(Style())

    def __repr__(self) -> str:
        return (
            f"Section(title={self.title}, level={self.level}, content={self.content})"
        )


class Document:
    style: Style
    sections: list[Section]

    def __init__(self, sections=None, style=None):
        self.style = Style() if style is None else style
        self.sections = [] if sections is None else sections

    @classmethod
    def from_wikitext(cls, text: str, style: Style | None = None) -> "Document":
        """Parse a document from wikitext.

        Args:
            text: The wikitext to parse
            style: Optional Style instance to use

        Returns:
            A new Document instance
        """
        if style is None:
            style = Style()

        # Split text into sections based on headings
        sections = []
        current_section_text = ""

        # Skip initial empty lines
        lines = [line for line in text.split("\n") if line.strip()]

        for line in lines:
            if line.strip().startswith("="):
                if current_section_text.strip():  # Only process non-empty sections
                    sections.append(Section.from_wikitext(current_section_text))
                current_section_text = line + "\n"
            else:
                current_section_text += line + "\n"

        if current_section_text.strip():  # Only process non-empty final section
            sections.append(Section.from_wikitext(current_section_text))

        # Organize sections into hierarchy based on level
        root_sections = []
        section_stack = []

        for section in sections:
            while section_stack and section_stack[-1].level >= section.level:
                section_stack.pop()

            if section_stack:
                section_stack[-1].add_subsection(section)
            else:
                root_sections.append(section)

            section_stack.append(section)

        return cls(sections=root_sections, style=style)

    def add_section(self, section: Section) -> None:
        self.sections.append(section)

    def __str__(self):
        sections = []
        for section in self.sections:
            sections.append(section)
            sections.extend(section.subsections)
        return "\n".join([section.to_wikitext(self.style) for section in sections])

    def __repr__(self) -> str:
        return f"Document(sections={self.sections})"
