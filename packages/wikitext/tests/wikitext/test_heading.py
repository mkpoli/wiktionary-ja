from wikitext.heading import Heading


def test_heading_basic():
    heading = Heading(2, "Test Section")
    assert str(heading) == "== Test Section =="

    heading = Heading.from_str("== Test Section ==")
    assert heading.level == 2
    assert heading.title == "Test Section"
    assert heading.space is True


def test_heading_no_space():
    heading = Heading(2, "Test Section", space=False)
    assert str(heading) == "==Test Section=="

    heading = Heading.from_str("==Test Section==")
    assert heading.level == 2
    assert heading.title == "Test Section"
    assert heading.space is False


def test_heading_different_levels():
    heading = Heading(1, "Main Section")
    assert str(heading) == "= Main Section ="

    heading = Heading(3, "Subsection")
    assert str(heading) == "=== Subsection ==="


def test_heading_from_str_different_levels():
    heading = Heading.from_str("= Main Section =")
    assert heading.level == 1
    assert heading.title == "Main Section"

    heading = Heading.from_str("=== Subsection ===")
    assert heading.level == 3
    assert heading.title == "Subsection"


def test_heading_attributes():
    heading = Heading(2, "Test", space=True)
    assert heading.level == 2
    assert heading.title == "Test"
    assert heading.space is True

    heading = Heading.from_str("== Test ==")
    assert heading.level == 2
    assert heading.title == "Test"
    assert heading.space is True


def test_heading_with_extra_spaces():
    heading = Heading.from_str("==  Multiple Spaces  ==")
    assert heading.level == 2
    assert heading.title == "Multiple Spaces"
    assert heading.space is True


def test_heading_invalid():
    try:
        Heading.from_str("Not a heading")
        assert False, "Should raise ValueError"
    except ValueError:
        pass
