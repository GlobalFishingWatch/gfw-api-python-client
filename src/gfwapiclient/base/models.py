"""Global Fishing Watch (GFW) API Python Client - Base Models."""

from enum import Enum
from typing import Any, ClassVar, Optional

from pydantic import AliasGenerator, ConfigDict, Field, field_validator
from pydantic import BaseModel as PydanticBaseModel
from pydantic.alias_generators import to_camel


__all__ = ["BaseModel", "Region", "RegionDataset"]


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


class RegionDataset(str, Enum):
    """Regions API dataset.

    For more details on the Regions API supported datasets, please refer
    to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#regions

    Attributes:
        PUBLIC_EEZ_AREAS (str):
            Exclusive Economic Zone (EEZ) regions dataset.

        PUBLIC_MPA_ALL (str):
            Marine Protected Area (MPA) regions dataset.

        PUBLIC_RFMO (str):
            Regional Fisheries Management Organization (RFMO) regions dataset.
    """

    PUBLIC_EEZ_AREAS = "public-eez-areas"
    PUBLIC_MPA_ALL = "public-mpa-all"
    PUBLIC_RFMO = "public-rfmo"


class Region(BaseModel):
    """Region of interest.

    Represents a predefined region (or area) of interest from:

    - Exclusive Economic Zones (EEZ)
    - Marine Protected Areas (MPA)
    - Regional Fisheries Management Organizations (RFMO)

    For more details on the predefined region (or area) of interest, please refer
    to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#regions

    Attributes:
        dataset (Optional[str]):
            Dataset name (or ID) containing the region of interest (e.g.,
            `"public-eez-areas"`).

        id (Optional[str]):
            Unique identifier (ID) for the region of interest (e.g., `"8466"`).
    """

    dataset: Optional[RegionDataset] = Field(None, alias="dataset")
    id: Optional[str] = Field(None, alias="id")

    @field_validator(
        "id",
        mode="before",
    )
    @classmethod
    def normalize_id(cls, value: Any) -> Optional[Any]:
        """Normalize the unique region identifier to a string.

        Ensures the ``id`` field is consistently represented as a string.
        Empty or whitespace-only values are normalized to ``None``.

        Args:
            value (Any):
                The raw `id` value to validate.

        Returns:
            Optional[Any]:
                The normalized string identifier, or ``None`` if the value
                is empty or missing.
        """
        if isinstance(value, int):
            return str(value)

        if isinstance(value, str) and value.strip() == "":
            return None

        return value
