from wikitext.list import OrderedList, UnorderedList


def test_ordered_list_str():
    items = ["First item", "Second item", "Third item"]
    ol = OrderedList(items)
    expected = "# First item\n# Second item\n# Third item"
    assert str(ol) == expected


def test_ordered_list_from_str():
    text = "# First item\n# Second item\n# Third item"
    ol = OrderedList.from_str(text)
    assert len(ol) == 3
    assert ol[0] == "# First item"
    assert ol[1] == "# Second item"
    assert ol[2] == "# Third item"


def test_ordered_list_from_str_with_continuation():
    text = "# First item\n# Second item\ncontinuation\n# Third item"
    ol = OrderedList.from_str(text)
    assert len(ol) == 3
    assert ol[0] == "# First item"
    assert ol[1] == "# Second item continuation"
    assert ol[2] == "# Third item"


def test_unordered_list_str():
    items = ["Apple", "Banana", "Orange"]
    ul = UnorderedList(items)
    expected = "* Apple\n* Banana\n* Orange"
    assert str(ul) == expected


def test_unordered_list_from_str():
    text = "* Apple\n* Banana\n* Orange"
    ul = UnorderedList.from_str(text)
    assert len(ul) == 3
    assert ul[0] == "* Apple"
    assert ul[1] == "* Banana"
    assert ul[2] == "* Orange"


def test_unordered_list_from_str_with_continuation():
    text = "* First point\n* Second point\nwith more detail\n* Third point"
    ul = UnorderedList.from_str(text)
    assert len(ul) == 3
    assert ul[0] == "* First point"
    assert ul[1] == "* Second point with more detail"
    assert ul[2] == "* Third point"


def test_empty_lists():
    ol = OrderedList([])
    ul = UnorderedList([])
    assert str(ol) == ""
    assert str(ul) == ""


def test_list_with_empty_lines():
    text = "\n# First item\n\n# Second item\n\n"
    ol = OrderedList.from_str(text)
    assert len(ol) == 2
    assert ol[0] == "# First item"
    assert ol[1] == "# Second item"
