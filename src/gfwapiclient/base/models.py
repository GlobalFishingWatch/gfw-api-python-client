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
    - Use `camelCase` for API requests and responses.
    - Strip whitespace from string fields automatically.
    - Use `value` property of enums
    - Validate default values.
    - Allow additional (unexpected) fields.

    Attributes:
        model_config (ClassVar[ConfigDict]):
            Configuration settings for Pydantic models.

            - `alias_generator`: Generates aliases for serialization/deserialization.
              - `serialization_alias`: Serializes Python's `snake_case` fields to `camelCase`.
              - `validation_alias`: Deserializes `camelCase` to Python's `snake_case` fields.
            - `extra="allow"`: Allows additional fields not explicitly defined in the model.
            - `populate_by_name=True`: Enables populate aliased field by `model attribute` or `alias`.
            - `str_strip_whitespace=True`: Trims whitespace from string fields.
            - `use_enum_values=True`: Enables populate models with the `value` property of enums.
            - `validate_default=True`: Ensures default values are validated.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(
        alias_generator=AliasGenerator(
            serialization_alias=to_camel,
            validation_alias=to_camel,
        ),
        extra="allow",
        populate_by_name=True,
        str_strip_whitespace=True,
        use_enum_values=True,
        validate_default=True,
    )
