from typing import Self


class Link:
    """
    Represents an internal link in wikitext format.

    Attributes:
        target (str): The target page of the link.
        text (str | None): The display text of the link. If None, the target is used as the display text.
    """

    target: str
    text: str | None

    def __init__(self, target: str, text: str | None = None):
        """
        Initializes a Link object.

        Args:
            target (str): The target page of the link.
            text (str, optional): The display text of the link. Defaults to None.
        """
        self.target = target
        self.text = text

    def __str__(self) -> str:
        """
        Returns the wikitext representation of the link.

        Returns:
            str: The wikitext representation of the link.
        """
        return f"[[{self.target}|{self.text}]]" if self.text else f"[[{self.target}]]"

    @classmethod
    def from_str(cls, target: str) -> Self:
        """
        Creates a Link object from a wikitext string.

        Args:
            target (str): The wikitext string representing the link.

        Returns:
            Link: A Link object.

        Raises:
            ValueError: If the string does not start with [[ and end with ]].
        """
        if not target.startswith("[[") and not target.endswith("]]"):
            raise ValueError("Invalid link format, must start with [[ and end with ]]")
        target = target[2:-2]
        if "|" in target:
            target, text = target.split("|", 1)
        else:
            text = None
        return cls(target, text)


class ExternalLink:
    """
    Represents an external link in wikitext format.

    Attributes:
        target (str): The URL of the external link.
        text (str | None): The display text of the link. If None, the URL is used as the display text.
    """

    target: str
    text: str | None

    def __init__(self, target: str, text: str | None = None):
        """
        Initializes an ExternalLink object.

        Args:
            target (str): The URL of the external link.
            text (str, optional): The display text of the link. Defaults to None.
        """
        self.target = target
        self.text = text

    def __str__(self) -> str:
        """
        Returns the wikitext representation of the external link.

        Returns:
            str: The wikitext representation of the external link.
        """
        return f"[{self.target} {self.text}]" if self.text else f"[{self.target}]"

    @classmethod
    def from_str(cls, target: str) -> Self:
        """
        Creates an ExternalLink object from a wikitext string.

        Args:
            target (str): The wikitext string representing the external link.

        Returns:
            ExternalLink: An ExternalLink object.

        Raises:
            ValueError: If the string does not start with [ and end with ].
        """
        if not target.startswith("[") and not target.endswith("]"):
            raise ValueError("Invalid link format, must start with [ and end with ]")
        target = target[1:-1]
        if " " in target:
            target, text = target.split(" ", 1)
        else:
            text = None
        return cls(target, text)
