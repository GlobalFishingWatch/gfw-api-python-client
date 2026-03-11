"""Global Fishing Watch (GFW) API Python Client - Base Models."""

import json

from enum import Enum
from pathlib import Path
from typing import Any, ClassVar, Dict, Optional, Self, Union, cast

import geopandas as gpd

from geojson_pydantic.features import Feature, FeatureCollection
from geojson_pydantic.geometries import Geometry
from pydantic import AliasGenerator, ConfigDict, Field, field_validator, model_validator
from pydantic import BaseModel as PydanticBaseModel
from pydantic.alias_generators import to_camel


__all__ = ["BaseModel", "GeoJson", "Region", "RegionDataset"]


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

    Represents a predefined geographic region (or area) of interest supported by
    the Global Fishing Watch APIs, including:

    - Exclusive Economic Zones (EEZ)
    - Marine Protected Areas (MPA)
    - Regional Fisheries Management Organizations (RFMO)

    The predefined region (or area) of interest are used in other
    Global Fishing Watch API endpoints when:

    - Create a report of a specified region.
    See: https://globalfishingwatch.org/our-apis/documentation#create-a-report-of-a-specified-region

    - Get All Events:
    See: https://globalfishingwatch.org/our-apis/documentation#get-all-events-post-endpoint

    - Create a Bulk Report.
    See https://globalfishingwatch.org/our-apis/documentation#create-a-bulk-report

    For more details on the predefined region (or area) of interest, please refer
    to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#regions

    For more details on the predefined region (or area) of interest data caveats,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definition

    See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition

    See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

    See: https://globalfishingwatch.org/our-apis/documentation#how-does-gfw-calculate-that-an-event-has-a-publicly-listed-authorization

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-rfmo-iuu-vessel-list

    See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definitions

    See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition-2

    Attributes:
        dataset (Optional[RegionDataset]):
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
        """Normalize the region identifier (ID) to a string.

        Ensures the `id` field is consistently represented as a string.
        Empty or whitespace-only values are normalized to `None`.

        Args:
            value (Any):
                The raw region `id` value to validate.

        Returns:
            Optional[Any]:
                The normalized region string `id`, or `None` if the value
                is empty or missing.
        """
        if isinstance(value, int):
            return str(value)

        if isinstance(value, str) and value.strip() == "":
            return None

        return value


class GeoJson(FeatureCollection[Feature[Geometry, Union[Dict[str, Any], BaseModel]]]):
    """Custom GeoJSON-compatible region (or area) of interest.

    Represents a GeoJSON-compatible custom geographic region (or area) of interest
    supported by the Global Fishing Watch APIs.

    The GeoJSON-compatible custom geographic region (or area) of interest are used
    in other Global Fishing Watch API endpoints when:

    - Create a report of a specified region.
    See: https://globalfishingwatch.org/our-apis/documentation#create-a-report-of-a-specified-region

    - Get All Events:
    See: https://globalfishingwatch.org/our-apis/documentation#get-all-events-post-endpoint

    - Create a Bulk Report.
    See https://globalfishingwatch.org/our-apis/documentation#create-a-bulk-report

    Attributes:
        type (Literal["FeatureCollection"]):
            The GeoJSON object type. Always set to `"FeatureCollection"`.

        features (List[Feature[Geometry, Union[Dict[str, Any], BaseModel]]]):
            A list of GeoJSON Feature objects contained in this collection.
            Each feature consists of a geometry object and an optional
            properties object.
    """

    @model_validator(mode="before")
    @classmethod
    def normalize_geojson(cls, value: Any) -> Optional[Any]:
        """Normalize arbitrary input into a GeoJSON FeatureCollection.

        Converts different forms of GeoJSON-compatible input into a standard
        FeatureCollection format, which is the internal representation used by
        `GeoJson`.

        Args:
            value (Any):
                The value to normalize.

        Returns:
            Optional[Any]:
                The normalized GeoJSON FeatureCollection, otherwise the input
                is returned as-is.
        """
        # Normalize GeoJSON-compatible dict inputs
        if isinstance(value, dict) and "type" in value:
            geojson_type: Optional[str] = value.get("type")

            if geojson_type == "FeatureCollection":
                return value

            if geojson_type == "Feature":
                return cls._wrap_geojson_feature(feature=value)

            if geojson_type and ("coordinates" in value or "geometries" in value):
                return cls._wrap_geojson_geometry(geometry=value)

        return value

    @classmethod
    def _wrap_geojson_feature(cls, *, feature: Any) -> Dict[str, Any]:
        """Wrap a GeoJSON Feature into a FeatureCollection.

        Converts a bare GeoJSON Feature object into a FeatureCollection object
        containing a provided Feature as its only member.

        Args:
            feature (Any):
                A valid GeoJSON Feature object.

        Returns:
            Dict[str, Any]:
                A GeoJSON FeatureCollection object.
        """
        return {
            "type": "FeatureCollection",
            "features": [feature],
        }

    @classmethod
    def _wrap_geojson_geometry(cls, *, geometry: Any) -> Dict[str, Any]:
        """Wrap a GeoJSON Geometry into a FeatureCollection.

        Converts a bare GeoJSON Geometry object (e.g., Point, Polygon etc.) into a
        FeatureCollection object containing a single Feature with null properties.

        Args:
            geometry (Any):
                A valid GeoJSON Geometry object.

        Returns:
            Dict[str, Any]:
                A GeoJSON FeatureCollection object.
        """
        return {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": None,
                    "geometry": geometry,
                }
            ],
        }

    @classmethod
    def from_file_or_geojson(
        cls,
        *,
        filename: Optional[Union[str, Path]] = None,
        geojson: Optional[Union[str, Dict[str, Any]]] = None,
        **kwargs: Dict[str, Any],
    ) -> Self:
        """Create a `GeoJson` instance from a spatial file or a GeoJSON object.

        Reads a GeoJSON-compatible object from a file, JSON-string, or dictionary and
        converts it into a `GeoJson` instance.

        If both `filename` and `geojson` are provided, `filename` takes precedence.

        Args:
            filename(Optional[Union[str, Path]]):
                Path to a spatial file (e.g., GeoJSON, Shapefile, etc.).
                Supported formats depend on the GeoPandas/GDAL installation.
                Example: `"path/to/your/spatial/file.shp"` or
                `"path/to/your/spatial/file.json"`.

            geojson (Optional[Union[str, Dict[str, Any]]]):
                A GeoJSON-compatible object provided as a JSON string or
                Python dictionary.
                Example: `'{"type": "Polygon", "coordinates": [...]}'` or
                `{"type": "Polygon", "coordinates": [...]}`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments passed to `geopandas.read_file()`
                when reading from a file.

        Returns:
            GeoJson:
                A fully populated `GeoJson` instance.
        """
        raw_geojson: Union[str, Dict[str, Any]] = geojson or {}

        # Read GeoJson from a spatial file
        if filename:
            gdf: gpd.GeoDataFrame = gpd.read_file(filename, **kwargs)
            raw_geojson = gdf.to_json(
                na="drop", show_bbox=True, drop_id=True, to_wgs84=True
            )

        if isinstance(raw_geojson, str):
            raw_geojson = json.loads(raw_geojson)
        raw_geojson = cast(Dict[str, Any], raw_geojson)

        return cls(**raw_geojson)
