import pytest
from wiktionary.document import Document, Section, Style


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
            + sections["sub"].to_wikitext(style)
            + "\n"
            + sections["another"].to_wikitext(style)
        )
        assert str(document) == expected_output

    def test_document_with_no_sections(self):
        empty_doc = Document()
        assert str(empty_doc) == ""
