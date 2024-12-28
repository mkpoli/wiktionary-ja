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

        # Extract title, handling HTML comments
        title_line = heading.strip("= ")
        comment = ""
        if "<!--" in title_line:
            parts = title_line.split("<!--", 1)
            title = parts[0].strip()  # Get everything before the comment
            comment = "<!--" + parts[1]
        else:
            title = title_line

        # Remove any trailing equals signs from the title
        title = title.rstrip("= ")

        # Everything after heading is content, prepending any comment from the heading
        content_lines = lines[1:]
        if comment:
            content_lines.insert(0, comment)
        content = "\n".join(content_lines).strip()

        return cls(title=title, level=level, content=content)

    def to_wikitext(self, style: Style) -> str:
        equal_signs = "=" * self.level
        space = " " if style.space_in_headings else ""
        heading = f"{equal_signs}{space}{self.title}{space}{equal_signs}"
        # Only add empty line if both style requires it and there is content
        empty_line = "\n" if style.empty_line_after_headings and self.content else ""

        parts = []
        parts.append(f"{heading}\n{empty_line}{self.content}")

        if self.subsections:
            subsections_text = "\n\n".join(
                subsection.to_wikitext(style).rstrip()
                for subsection in self.subsections
            )
            parts.append(subsections_text)

        result = "\n\n".join(parts)
        return result + "\n"  # Ensure there's always a trailing newline

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
    content: str
    sections: list[Section]

    def __init__(self, content=None, sections=None, style=None):
        self.style = Style() if style is None else style
        self.content = content or ""
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
        content = ""
        current_section_text = ""

        # Skip initial empty lines
        lines = [line for line in text.split("\n") if line.strip()]

        # Collect content before first heading
        for i, line in enumerate(lines):
            if line.strip().startswith("="):
                break
            content += line + "\n"

        # Remove content lines from lines list
        lines = lines[len(content.splitlines()) :]

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

        return cls(content=content.strip(), sections=root_sections, style=style)

    def add_section(self, section: Section) -> None:
        self.sections.append(section)

    def __str__(self):
        parts = []
        if self.content:
            parts.append(self.content)

        # Only include top-level sections, their subsections are handled by to_wikitext
        section_texts = []
        for section in self.sections:
            text = section.to_wikitext(self.style)
            if text.strip():
                section_texts.append(
                    text.rstrip()
                )  # Remove trailing newlines before joining

        # Join with double newlines and ensure there's a final newline
        if section_texts:
            parts.extend(section_texts)
            return "\n\n".join(parts) + "\n"
        return "\n".join(parts) + "\n"

    def __repr__(self) -> str:
        return f"Document(content={self.content!r}, sections={self.sections})"
