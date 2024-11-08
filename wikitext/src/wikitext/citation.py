from typing import Optional
from .template import Template


class AbstractCitation(Template):
    """
    An abstract base class for citation templates.

    Inherits from the Template class and provides a base for specific citation types.
    """

    def __init__(self, tag_name, *params, **kwargs):
        """
        Initializes an AbstractCitation instance.

        :param tag_name: The name of the citation tag.
        :param params: Additional positional parameters for the template.
        :param kwargs: Additional keyword parameters for the template.
        """
        super().__init__(tag_name, *params, **kwargs)


class Citation(AbstractCitation):
    """
    A class representing a generic citation.

    Inherits from AbstractCitation and is used to create a citation with specific parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a Citation instance.

        :param kwargs: Keyword arguments representing citation parameters.
                       Underscores in keys are replaced with hyphens.
        """
        super().__init__(
            "citation",
            **{k.replace("_", "-"): v for k, v in kwargs.items() if v is not None},
        )

    def __hash__(self):
        """
        Returns the hash of the citation parameters.

        :return: Hash value of the citation parameters.
        """
        return hash(frozenset(self.kwargs.items()))

    def __eq__(self, other):
        """
        Checks equality between two Citation instances.

        :param other: Another Citation instance to compare with.
        :return: True if the parameters of both citations are equal, False otherwise.
        """
        return self.kwargs == other.kwargs


class CiteBook(Citation):
    """
    A class representing a book citation.

    Inherits from Citation and is used to create a citation for a book with specific attributes.
    """

    def __init__(
        self,
        author: Optional[str] = None,
        title: Optional[str] = None,
        year: Optional[str] = None,
        publisher: Optional[str] = None,
        isbn: Optional[str] = None,
        location: Optional[str] = None,
        chapter: Optional[str] = None,
        **kwargs,
    ):
        """
        Initializes a CiteBook instance.

        :param author: The author of the book.
        :param title: The title of the book.
        :param year: The year of publication.
        :param publisher: The publisher of the book.
        :param isbn: The ISBN of the book.
        :param location: The location of publication.
        :param chapter: The chapter of the book.
        :param kwargs: Additional keyword arguments for the citation.
        """
        super().__init__(
            author=author,
            title=title,
            year=year,
            publisher=publisher,
            isbn=isbn,
            location=location,
            chapter=chapter,
            **kwargs,
        )


class Ref:
    """
    A class representing a reference tag.

    Used to create a reference with an optional name and content.
    """

    name: Optional[str]
    content: Optional[str]

    def __init__(self, name=None, content=None):
        """
        Initializes a Ref instance.

        :param name: The name attribute of the reference.
        :param content: The content of the reference.
        """
        self.name = name
        self.content = content

    def __str__(self) -> str:
        """
        Returns the string representation of the reference.

        :return: A string representing the reference in XML format.
        """
        name_attr = f' name="{self.name}"' if self.name else ""
        if self.content is None:
            return f"<ref{name_attr}/>"
        else:
            return f"<ref{name_attr}>{self.content}</ref>"
