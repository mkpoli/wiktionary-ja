# ==English==

# ===Noun===
# {{en-noun}}

# # Noun sense.

# ====Synonyms====
# * synonym

# ==Portuguese==

# (...)

from dataclasses import dataclass


@dataclass
class Style:
    space_in_headings: bool = True
    empty_line_after_headings: bool = True


STYLE_WIKTIONARY_ENGLISH = Style(
    space_in_headings=False, empty_line_after_headings=False
)

STYLE_PRESETS = {
    "wten": STYLE_WIKTIONARY_ENGLISH,
}
