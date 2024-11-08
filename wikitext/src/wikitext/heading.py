import re
from typing import Self


class Heading:
    def __init__(self, level: int, title: str, space: bool = True):
        self.level = level
        self.title = title
        self.space = space

    def __str__(self) -> str:
        return f"{'=' * self.level}{' ' if self.space else ''}{self.title}{' ' if self.space else ''}{'=' * self.level}"

    @classmethod
    def from_str(cls, text: str) -> Self:
        match = re.match(r"^(=+)(\s*)([^=]*?)\s*(=+)$", text)
        if match:
            return cls(len(match.group(1)), match.group(3), len(match.group(2)) > 0)
        raise ValueError(f"Invalid heading: {text}")


def match_section_heading(text: str, level: int) -> re.Match | None:
    return re.match(
        rf"^={{{level},{level}}}\s*([^=]*?)\s*={{{level},{level}}}[^=]*$", text
    )


def get_heading_lines(text: str, level: int) -> dict[int, str]:
    return {
        i: m.group(0)
        for i, line in enumerate(text.splitlines())
        if (m := match_section_heading(line, level))
    }
