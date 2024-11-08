class Bold:
    """
    Represents bold text in wikitext format.

    Attributes:
        text (str): The text to be bolded.
    """

    def __init__(self, text: str):
        """
        Initializes a Bold object.

        Args:
            text (str): The text to be bolded.
        """
        self.text = text

    def __str__(self) -> str:
        """
        Returns the wikitext representation of the bold text.

        Returns:
            str: The wikitext representation of the bold text.
        """
        return f"'''{self.text}'''"

    @classmethod
    def from_str(cls, text: str) -> "Bold":
        """
        Creates a Bold object from a wikitext string.

        Args:
            text (str): The wikitext string representing the bold text.

        Returns:
            Bold: A Bold object.
        """
        return cls(text)


class Italic:
    """
    Represents italic text in wikitext format.

    Attributes:
        text (str): The text to be italicized.
    """

    def __init__(self, text: str):
        """
        Initializes an Italic object.

        Args:
            text (str): The text to be italicized.
        """
        self.text = text

    def __str__(self) -> str:
        """
        Returns the wikitext representation of the italic text.

        Returns:
            str: The wikitext representation of the italic text.
        """
        return f"''{self.text}''"

    @classmethod
    def from_str(cls, text: str) -> "Italic":
        """
        Creates an Italic object from a wikitext string.

        Args:
            text (str): The wikitext string representing the italic text.

        Returns:
            Italic: An Italic object.
        """
        return cls(text)
