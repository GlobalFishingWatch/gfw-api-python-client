"""Global Fishing Watch (GFW) API Python Client - Base Models."""

from typing import ClassVar

from pydantic import AliasGenerator, ConfigDict
from pydantic import BaseModel as PydanticBaseModel
from pydantic.alias_generators import to_camel


__all__ = ["BaseModel"]


class BaseModel(PydanticBaseModel):
    """Base model for domain data models.

    This class extends `pydantic.BaseModel` to:

    - Use `snake_case` for Python attributes.
    - Uses `camelCase` for API requests and responses.
    - Strip whitespace from string fields automatically.
    - Allow additional (unexpected) fields.

    Attributes:
        model_config (ClassVar[ConfigDict]): Configuration settings for Pydantic models.

            - `serialization_alias`: Converts field names to `camelCase` for serialization.
            - `validation_alias`: Allows deserialization from `camelCase` to Python's `snake_case` fields.
            - `populate_by_name=True`: Enables field access using either `snake_case` or `camelCase`.
            - `str_strip_whitespace=True`: Trims whitespace from string fields.
            - `extra="allow"`: Permits additional fields.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(
        alias_generator=AliasGenerator(
            serialization_alias=to_camel,
            validation_alias=to_camel,
        ),
        populate_by_name=True,
        str_strip_whitespace=True,
        extra="allow",
    )
