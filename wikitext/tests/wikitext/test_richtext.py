from wikitext.richtext import Bold, Italic


def test_bold_str():
    """Test Bold class string representation"""
    bold = Bold("test text")
    assert str(bold) == "'''test text'''"


def test_bold_from_str():
    """Test Bold.from_str class method"""
    bold = Bold.from_str("test text")
    assert isinstance(bold, Bold)
    assert bold.text == "test text"


def test_italic_str():
    """Test Italic class string representation"""
    italic = Italic("test text")
    assert str(italic) == "''test text''"


def test_italic_from_str():
    """Test Italic.from_str class method"""
    italic = Italic.from_str("test text")
    assert isinstance(italic, Italic)
    assert italic.text == "test text"


def test_empty_bold():
    """Test Bold class with empty string"""
    bold = Bold("")
    assert str(bold) == "''''''"


def test_empty_italic():
    """Test Italic class with empty string"""
    italic = Italic("")
    assert str(italic) == "''''"
