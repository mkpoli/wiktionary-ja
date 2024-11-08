class Template:
    """
    Represents a template in wikitext format.

    Attributes:
        tag_name (str): The name of the template tag.
        params (tuple): Positional parameters for the template.
        kwargs (dict): Keyword parameters for the template, with None values filtered out.
    """

    def __init__(self, tag_name: str, *params, **kwargs):
        """
        Initializes a Template object.

        Args:
            tag_name (str): The name of the template tag.
            *params: Positional parameters for the template.
            **kwargs: Keyword parameters for the template.
        """
        self.tag_name = tag_name
        self.params = params
        self.kwargs = {k: v for k, v in kwargs.items() if v is not None}

    def __str__(self) -> str:
        """
        Returns the wikitext representation of the template.

        Returns:
            str: The wikitext representation of the template.
        """
        params_str = "".join(
            [f"|{param}" for param in self.params if param is not None]
        )
        params_str += "".join([f"|{key}={value}" for key, value in self.kwargs.items()])
        return f"{{{{{self.tag_name}{params_str}}}}}"

    @classmethod
    def from_str(cls, template_str: str) -> "Template":
        """
        Creates a Template object from a wikitext string.

        Args:
            template_str (str): The wikitext string representing the template.

        Returns:
            Template: A Template object.

        Raises:
            ValueError: If the string does not start with {{ and end with }}.
        """
        if not template_str.startswith("{{") and not template_str.endswith("}}"):
            raise ValueError(
                "Invalid template format, must start with {{ and end with }}"
            )

        template_str = template_str[2:-2]
        parts = template_str.split("|")
        tag_name = parts[0]
        params = []
        kwargs = {}

        for part in parts[1:]:
            if "=" in part:
                key, value = part.split("=", 1)
                kwargs[key] = value
            else:
                params.append(part)

        return cls(tag_name, *params, **kwargs)
