import regex as re
from typing import Optional
from wikitext.citation import Citation
from wikitext.richtext import Bold
from wikitext.template import Template
from wikitext.list import OrderedList


class L(Template):
    def __init__(self, lang, text):
        super().__init__("l", lang, text)


class DefinitionList(OrderedList):
    def __init__(self, items: list[str]):
        super().__init__(items)

    def __str__(self) -> str:
        return "\n".join(
            [f"#{item}" if item.startswith("*") else f"# {item}" for item in self]
        )


# ic.configureOutput(includeContext=True)


# def format_katakana(sentence: str, latin: str) -> str:
#     ic(latn2kana(latin))

#     return sentence


def apply_highlight(text: str, part: str) -> str:
    part = re.sub(r"\p{P}", "", part)

    if part not in text:
        raise ValueError(f"Part '{part}' not in text '{text}'")

    return re.sub(rf"({part})", r"'''\1'''", text)

    # splited = text.split(part)
    # return f"{''.join(splited[:1])}{Bold(part)}{''.join(splited[1:])}"


def find_highlight(text: str) -> str | None:
    return text.split("'''")[1] if "'''" in text else None
