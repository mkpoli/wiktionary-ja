from abc import ABC, abstractmethod
from typing import Self


class List(list, ABC):
    """
    A base class for lists in wikitext.

    Attributes:
        items (list[str]): A list of string items.
    """

    def __init__(self, items: list[str]):
        """
        Initialize the List with items.

        Args:
            items (list[str]): A list of string items.
        """
        super().__init__(items)

    @abstractmethod
    def from_str(cls, text: str) -> Self:
        """
        Create a List from a string.
        """
        pass


class OrderedList(List):
    """
    A class representing an ordered list in wikitext.
    """

    def __str__(self) -> str:
        """
        Return the string representation of the ordered list.

        Returns:
            str: The string representation of the ordered list with each item prefixed by '# '.
        """
        return "\n".join(f"# {item}" for item in self)

    @classmethod
    def from_str(cls, text: str) -> Self:
        """
        Create an OrderedList from a string.
        """
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        for i in range(len(lines) - 1, 0, -1):
            if not lines[i].startswith("#"):
                lines[i - 1] += " " + lines[i]
                lines.pop(i)
        return cls(lines)


class UnorderedList(List):
    """
    A class representing an unordered list in wikitext.
    """

    def __str__(self) -> str:
        """
        Return the string representation of the unordered list.

        Returns:
            str: The string representation of the unordered list with each item prefixed by '* '.
        """
        return "\n".join([f"* {item}" for item in self])

    @classmethod
    def from_str(cls, text: str) -> Self:
        """
        Create an UnorderedList from a string.
        """
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        for i in range(len(lines) - 1, 0, -1):
            if not lines[i].startswith("*"):
                lines[i - 1] += " " + lines[i]
                lines.pop(i)
        return cls(lines)
