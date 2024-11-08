from wikitext.template import Template


def test_template_basic():
    template = Template("Citation")
    assert str(template) == "{{Citation}}"

    template = Template.from_str("{{Citation}}")
    assert template.tag_name == "Citation"
    assert template.params == ()
    assert template.kwargs == {}


def test_template_with_params():
    template = Template("Citation", "required1", "required2")
    assert str(template) == "{{Citation|required1|required2}}"

    template = Template.from_str("{{Citation|required1|required2}}")
    assert template.tag_name == "Citation"
    assert template.params == ("required1", "required2")
    assert template.kwargs == {}


def test_template_with_kwargs():
    template = Template("Citation", author="John Doe", year=2021)
    assert str(template) == "{{Citation|author=John Doe|year=2021}}"

    template = Template.from_str("{{Citation|author=John Doe|year=2021}}")
    assert template.tag_name == "Citation"
    assert template.params == ()
    assert template.kwargs == {"author": "John Doe", "year": "2021"}


def test_template_with_params_and_kwargs():
    template = Template("Citation", "required1", author="John Doe", year=2021)
    assert str(template) == "{{Citation|required1|author=John Doe|year=2021}}"

    template = Template.from_str("{{Citation|required1|author=John Doe|year=2021}}")
    assert template.tag_name == "Citation"
    assert template.params == ("required1",)
    assert template.kwargs == {"author": "John Doe", "year": "2021"}


def test_template_with_none_values():
    template = Template("Citation", None, author="John Doe", optional=None)
    assert str(template) == "{{Citation|author=John Doe}}"

    template = Template.from_str("{{Citation|author=John Doe}}")
    assert template.tag_name == "Citation"
    assert template.params == ()
    assert template.kwargs == {"author": "John Doe"}


def test_template_empty_params():
    template = Template("Citation")
    assert str(template) == "{{Citation}}"

    template = Template.from_str("{{Citation}}")
    assert template.tag_name == "Citation"
    assert template.params == ()
    assert template.kwargs == {}


def test_template_special_characters():
    template = Template("Citation", author="John & Jane", title="Test: A Study")
    assert str(template) == "{{Citation|author=John & Jane|title=Test: A Study}}"

    template = Template.from_str("{{Citation|author=John & Jane|title=Test: A Study}}")
    assert template.tag_name == "Citation"
    assert template.params == ()
    assert template.kwargs == {"author": "John & Jane", "title": "Test: A Study"}
