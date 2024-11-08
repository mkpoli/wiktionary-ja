from wikitext.link import Link, ExternalLink


def test_link_without_text():
    link = Link("Main Page")
    assert str(link) == "[[Main Page]]"

    link = Link.from_str("[[Main Page]]")
    assert link.target == "Main Page"
    assert link.text is None


def test_link_with_text():
    link = Link("Main Page", "Visit Main")
    assert str(link) == "[[Main Page|Visit Main]]"

    link = Link.from_str("[[Main Page|Visit Main]]")
    assert link.target == "Main Page"
    assert link.text == "Visit Main"


def test_link_with_empty_text():
    link = Link("Main Page", "")
    assert str(link) == "[[Main Page]]"

    link = Link.from_str("[[Main Page]]")
    assert link.target == "Main Page"
    assert link.text is None


def test_interwiki_link():
    link = Link("ja:Main Page")
    assert str(link) == "[[ja:Main Page]]"

    link = Link.from_str("[[ja:Main Page]]")
    assert link.target == "ja:Main Page"
    assert link.text is None


def test_external_link_without_text():
    link = ExternalLink("https://example.com")
    assert str(link) == "[https://example.com]"

    link = ExternalLink.from_str("[https://example.com]")
    assert link.target == "https://example.com"
    assert link.text is None


def test_external_link_with_text():
    link = ExternalLink("https://example.com", "Example Website")
    assert str(link) == "[https://example.com Example Website]"

    link = ExternalLink.from_str("[https://example.com Example Website]")
    assert link.target == "https://example.com"
    assert link.text == "Example Website"


def test_external_link_with_empty_text():
    link = ExternalLink("https://example.com", "")
    assert str(link) == "[https://example.com]"

    link = ExternalLink.from_str("[https://example.com]")
    assert link.target == "https://example.com"
    assert link.text is None


def test_link_attributes():
    link = Link("Target", "Text")
    assert link.target == "Target"
    assert link.text == "Text"

    link = Link.from_str("[[Target|Text]]")
    assert link.target == "Target"
    assert link.text == "Text"


def test_external_link_attributes():
    link = ExternalLink("https://example.com", "Text")
    assert link.target == "https://example.com"
    assert link.text == "Text"

    link = ExternalLink.from_str("[https://example.com Text]")
    assert link.target == "https://example.com"
    assert link.text == "Text"
