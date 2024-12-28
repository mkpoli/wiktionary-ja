import pytest
from wiktionary.document import Document, Section, Style
from wiktionary.style import (
    STYLE_WIKTIONARY_ENGLISH,
    STYLE_PRESETS,
)


@pytest.fixture
def style():
    return Style()


@pytest.fixture
def basic_section():
    return Section(
        title="Introduction", level=1, content="This is the introduction section."
    )


@pytest.fixture
def document(style):
    return Document(style=style)


@pytest.fixture
def sections():
    return {
        "main": Section(title="Introduction", level=1, content="Intro content."),
        "another": Section(title="Background", level=1, content="Background content."),
        "sub": Section(title="Details", level=2, content="Detailed info."),
    }


class TestSection:
    def test_section_initialization(self, basic_section):
        assert basic_section.title == "Introduction"
        assert basic_section.level == 1
        assert basic_section.content == "This is the introduction section."
        assert basic_section.subsections == []

    def test_add_subsection(self, basic_section):
        subsection = Section("Background", 2, "Background content.")
        basic_section.add_subsection(subsection)
        assert subsection in basic_section.subsections

    def test_to_wikitext(self, basic_section, style):
        expected_heading = "= Introduction ="
        expected_output = f"{expected_heading}\n\n{basic_section.content}\n"
        assert basic_section.to_wikitext(style) == expected_output

    def test_str_representation(self, basic_section):
        expected_output = basic_section.to_wikitext(Style())
        assert str(basic_section) == expected_output


class TestDocument:
    def test_document_initialization(self):
        doc = Document()
        assert isinstance(doc.style, Style)
        assert doc.sections == []

    def test_add_section(self, document, sections):
        document.add_section(sections["main"])
        assert sections["main"] in document.sections

    def test_add_subsections_to_sections(self, document, sections):
        sections["main"].add_subsection(sections["sub"])
        document.add_section(sections["main"])
        document.add_section(sections["another"])
        assert sections["sub"] in document.sections[0].subsections

    def test_document_str(self, document, sections, style):
        sections["main"].add_subsection(sections["sub"])
        document.add_section(sections["main"])
        document.add_section(sections["another"])

        expected_output = (
            sections["main"].to_wikitext(style)
            + "\n"
            + sections["another"].to_wikitext(style)
        )
        assert str(document) == expected_output

    def test_document_with_no_sections(self):
        empty_doc = Document()
        assert str(empty_doc) == "\n"


class TestStyle:
    def test_style_default_values(self):
        style = Style()
        assert style.space_in_headings is True
        assert style.empty_line_after_headings is True

    def test_style_custom_values(self):
        style = Style(space_in_headings=False, empty_line_after_headings=False)
        assert style.space_in_headings is False
        assert style.empty_line_after_headings is False

    def test_wiktionary_english_preset(self):
        assert STYLE_WIKTIONARY_ENGLISH.space_in_headings is False
        assert STYLE_WIKTIONARY_ENGLISH.empty_line_after_headings is False

    def test_style_presets_contain_wten(self):
        assert "wten" in STYLE_PRESETS
        assert STYLE_PRESETS["wten"] is STYLE_WIKTIONARY_ENGLISH

    @pytest.mark.parametrize(
        "style,heading,expected",
        [
            (
                Style(space_in_headings=True, empty_line_after_headings=True),
                Section("Test", 2, "Content"),
                "== Test ==\n\nContent\n",
            ),
            (
                Style(space_in_headings=False, empty_line_after_headings=True),
                Section("Test", 2, "Content"),
                "==Test==\n\nContent\n",
            ),
            (
                Style(space_in_headings=True, empty_line_after_headings=False),
                Section("Test", 2, "Content"),
                "== Test ==\nContent\n",
            ),
            (
                Style(space_in_headings=False, empty_line_after_headings=False),
                Section("Test", 2, "Content"),
                "==Test==\nContent\n",
            ),
        ],
    )
    def test_style_formatting(self, style, heading, expected):
        assert heading.to_wikitext(style) == expected

    def test_style_equality(self):
        style1 = Style(space_in_headings=True, empty_line_after_headings=True)
        style2 = Style(space_in_headings=True, empty_line_after_headings=True)
        style3 = Style(space_in_headings=False, empty_line_after_headings=True)

        assert style1 == style2
        assert style1 != style3

    def test_wiktionary_english_formatting(self):
        section = Section("Test", 2, "Content")
        expected = "==Test==\nContent\n"
        assert section.to_wikitext(STYLE_WIKTIONARY_ENGLISH) == expected
