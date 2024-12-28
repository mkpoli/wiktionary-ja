import pytest
from wiktionary.document import Section, Document
from wiktionary.style import Style


def test_section_from_wikitext_basic():
    text = "== Title ==\nContent here"
    section = Section.from_wikitext(text)
    assert section.title == "Title"
    assert section.level == 2
    assert section.content == "Content here"


def test_section_from_wikitext_empty():
    with pytest.raises(ValueError, match="Empty text"):
        Section.from_wikitext("")


def test_section_from_wikitext_invalid():
    with pytest.raises(ValueError, match="Invalid heading"):
        Section.from_wikitext("Not a heading\nContent")


def test_section_from_wikitext_multiline():
    text = "=== Title ===\nLine 1\nLine 2\nLine 3"
    section = Section.from_wikitext(text)
    assert section.title == "Title"
    assert section.level == 3
    assert section.content == "Line 1\nLine 2\nLine 3"


def test_document_from_wikitext():
    text = """
= Main =
Main content

== Sub 1 ==
Sub content 1

== Sub 2 ==
Sub content 2

= Other =
Other content
"""
    doc = Document.from_wikitext(text)
    assert len(doc.sections) == 2  # Main and Other
    assert doc.sections[0].title == "Main"
    assert len(doc.sections[0].subsections) == 2  # Sub 1 and Sub 2
    assert doc.sections[0].subsections[0].title == "Sub 1"
    assert doc.sections[0].subsections[1].title == "Sub 2"
    assert doc.sections[1].title == "Other"


def test_document_from_wikitext_nested_levels():
    text = """
= Level 1 =
Content 1

== Level 2 ==
Content 2

=== Level 3 ===
Content 3

== Level 2b ==
Content 2b
"""
    doc = Document.from_wikitext(text)
    assert len(doc.sections) == 1
    main_section = doc.sections[0]
    assert main_section.title == "Level 1"
    assert len(main_section.subsections) == 2
    assert main_section.subsections[0].title == "Level 2"
    assert len(main_section.subsections[0].subsections) == 1
    assert main_section.subsections[0].subsections[0].title == "Level 3"
    assert main_section.subsections[1].title == "Level 2b"


def test_document_to_string():
    style = Style(space_in_headings=True, empty_line_after_headings=True)
    doc = Document(style=style)

    main = Section("Main", 1, "Main content")
    sub1 = Section("Sub 1", 2, "Sub content 1")
    sub2 = Section("Sub 2", 2, "Sub content 2")

    main.add_subsection(sub1)
    main.add_subsection(sub2)
    doc.add_section(main)

    expected = """= Main =

Main content

== Sub 1 ==

Sub content 1

== Sub 2 ==

Sub content 2
"""
    assert str(doc) == expected


def test_section_to_string():
    section = Section("Test", 2, "Content")
    expected = "== Test ==\n\nContent\n"  # Note the extra newline
    assert str(section) == expected


def test_document_with_preamble():
    text = """
Hi, I'm a preamble!
= Main =
== Sub 1 ==
== Sub 2 ==
= Other =
"""
    doc = Document.from_wikitext(text)
    assert len(doc.sections) == 2
    assert doc.sections[0].title == "Main"
    assert len(doc.sections[0].subsections) == 2
