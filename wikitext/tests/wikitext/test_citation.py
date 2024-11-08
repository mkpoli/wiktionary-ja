from wikitext.citation import Citation, CiteBook, Ref


def test_citation_basic():
    citation = Citation(author="John Doe", title="Test Book")
    assert str(citation) == "{{citation|author=John Doe|title=Test Book}}"


def test_citation_underscore_conversion():
    citation = Citation(first_author="John Doe", page_number="42")
    assert str(citation) == "{{citation|first-author=John Doe|page-number=42}}"


def test_citation_equality():
    citation1 = Citation(author="John Doe", year="2023")
    citation2 = Citation(author="John Doe", year="2023")
    citation3 = Citation(author="Jane Doe", year="2023")

    assert citation1 == citation2
    assert citation1 != citation3
    assert hash(citation1) == hash(citation2)


def test_cite_book():
    book = CiteBook(
        author="Jane Smith",
        title="Python Testing",
        year="2023",
        publisher="Tech Books",
        isbn="123-456-789",
        location="New York",
        chapter="Unit Testing",
    )
    expected = (
        "{{citation|author=Jane Smith|title=Python Testing|year=2023|"
        "publisher=Tech Books|isbn=123-456-789|location=New York|chapter=Unit Testing}}"
    )
    assert str(book) == expected


def test_ref_empty():
    ref = Ref()
    assert str(ref) == "<ref/>"


def test_ref_with_name():
    ref = Ref(name="test1")
    assert str(ref) == '<ref name="test1"/>'


def test_ref_with_content():
    ref = Ref(content="Some reference content")
    assert str(ref) == "<ref>Some reference content</ref>"


def test_ref_with_name_and_content():
    ref = Ref(name="test2", content="Some reference content")
    assert str(ref) == '<ref name="test2">Some reference content</ref>'
