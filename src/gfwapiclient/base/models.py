"""Global Fishing Watch (GFW) API Python Client - Base Models."""

from enum import Enum
from pathlib import Path
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Protocol,
    Self,
    Union,
    cast,
    runtime_checkable,
)

import geopandas as gpd

from geojson_pydantic.features import Feature, FeatureCollection
from geojson_pydantic.geometries import Geometry, GeometryCollection
from pydantic import (
    AliasGenerator,
    ConfigDict,
    Field,
    FilePath,
    Json,
    TypeAdapter,
    ValidationError,
    field_validator,
    model_validator,
)
from pydantic import BaseModel as PydanticBaseModel
from pydantic.alias_generators import to_camel


__all__ = ["BaseModel", "GeoJson", "Geometry", "OnInvalid", "Region", "RegionDataset"]


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


class OnInvalid(str, Enum):
    """Error handling strategy.

    Attributes:
        RAISE (str):
            Raise the underlying exception immediately.

        IGNORE (str):
            Suppress the underlying exception and return `None`.
    """

    RAISE = "raise"
    IGNORE = "ignore"


@runtime_checkable
class SupportsGeoJsonInterface(Protocol):
    """Protocol for objects exposing a GeoJSON interface.

    For more details on `GeoJSON` and `__geo_interface__`, please refer
    to the official documentations:

    See: https://geojson.org/

    See: https://gist.github.com/sgillies/2217756
    """

    @property
    def __geo_interface__(self) -> Dict[str, Any]: ...  # pragma: no cover


class GeoJson(FeatureCollection[Feature[Geometry, Union[Dict[str, Any], BaseModel]]]):
    """Custom GeoJSON-compatible region (or area) of interest.

    Represents a GeoJSON-compatible custom geographic region (or area) of interest
    supported by the Global Fishing Watch APIs.

    The GeoJSON-compatible custom geographic regions (areas of interest) are used
    in other Global Fishing Watch API endpoints when:

    - Create a report of a specified region.
    See: https://globalfishingwatch.org/our-apis/documentation#create-a-report-of-a-specified-region

    - Get All Events:
    See: https://globalfishingwatch.org/our-apis/documentation#get-all-events-post-endpoint

    - Create a Bulk Report.
    See https://globalfishingwatch.org/our-apis/documentation#create-a-bulk-report

    For more details on `GeoJSON` and `__geo_interface__`, please refer
    to the official documentations:

    See: https://geojson.org/

    See: https://gist.github.com/sgillies/2217756

    Attributes:
        type (Literal["FeatureCollection"]):
            The GeoJSON object type. Always set to `"FeatureCollection"`.

        features (List[Feature[Geometry, Union[Dict[str, Any], BaseModel]]]):
            A list of GeoJSON Feature objects contained in this collection.
            Each feature consists of a geometry object and an optional
            properties object.
    """

    _file_path_adapter: ClassVar[Optional[TypeAdapter[FilePath]]] = None
    _json_dict_adapter: ClassVar[Optional[TypeAdapter[Json[Dict[str, Any]]]]] = None

    def to_geometry(self) -> Geometry:
        """Convert a `GeoJson` object into into a single or collection of geometry.

        This method extracts and aggregates all geometries contained within the
        features of `GeoJson` object. The resulting `Geometry` represents the
        union of all geometries contained in the `GeoJson`:

        - Multiple features are converted into a `GeometryCollection`.
        - Individual features return their geometry directly i.e., `Point`,
        `MultiPoint`, `LineString`, `MultiLineString`, `Polygon`, or `MultiPolygon`.
        - Features without geometries (`geometry=None`) are ignored.

        Returns:
            Geometry:
                A single or collection of geometry representing all geometries contained in the `GeoJson` object.

        Raises:
            ValueError:
                If the `GeoJson` object contains no valid geometries.
        """
        geometries: List[Geometry] = []
        for feature in self.features or []:
            if feature.geometry:
                if isinstance(feature.geometry, GeometryCollection):
                    for geometry in feature.geometry.geometries or []:
                        geometries.append(geometry)
                else:
                    geometries.append(feature.geometry)

        if not geometries:
            raise ValueError(
                f"Expected `GeoJson` object with valid geometries but received {self!r}"
            )

        if len(geometries) == 1:
            return geometries[0]

        return GeometryCollection.create(
            geometries=geometries,
        )

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

            # Wrap a GeoJSON Feature into a FeatureCollection
            if geojson_type == "Feature":
                return {
                    "type": "FeatureCollection",
                    "features": [value],
                }

            # Wrap a GeoJSON Geometry/GeometryCollection into a FeatureCollection
            if geojson_type and ("coordinates" in value or "geometries" in value):
                return {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "properties": None,
                            "geometry": value,
                        }
                    ],
                }

        return value

    @classmethod
    def from_file_or_geojson(
        cls,
        *,
        source: Union[str, Path, Dict[str, Any], SupportsGeoJsonInterface],
        **kwargs: Dict[str, Any],
    ) -> Self:
        """Create a `GeoJson` instance from a spatial data source.

        Reads a spatial file (e.g., GeoJSON, Shapefile, etc.), GeoJSON-string,
        GeoJSON-dictionary, GeoDataFrame, or an object implementing `__geo_interface__`
        and converts it into a `GeoJson` instance.

        For more details on `GeoJSON` and `__geo_interface__`, please refer
        to the official documentations:

        See: https://geojson.org/

        See: https://gist.github.com/sgillies/2217756

        When `source` is a filesystem path, the file is read using `geopandas.read_file`.

        Supported formats depend on the underlying GDAL installation,
        commonly including:

        - GeoJSON (.geojson, .json)
        - ESRI Shapefile (.shp)
        - GeoPackage (.gpkg)
        - FlatGeobuf (.fgb)
        - KML / KMZ (if enabled)
        - many additional OGR-supported formats

        See: https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html

        See: https://gdal.org/drivers/vector/index.html

        A properly configured GDAL installation is required.

        Args:
            source (Union[str, Path, Dict[str, Any], SupportsGeoJsonInterface]):
                Spatial input source.

                Path to a spatial file (e.g., GeoJSON, Shapefile, etc.).
                Example: `"path/to/your/spatial/file.shp"` or
                `"path/to/your/spatial/file.json"`.

                GeoJSON-compatible object provided as a JSON-string, Python dictionary,
                `geopandas.GeoDataFrame`, `shapely`, or an object implementing
                `__geo_interface__`.
                Example: `'{"type": "Polygon", "coordinates": [...]}'` or
                `{"type": "Polygon", "coordinates": [...]}`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments passed to `geopandas.read_file()`
                when reading from a file.

        Returns:
            GeoJson:
                A fully populated `GeoJson` instance.

        Raises:
            ValueError:
                If the source cannot be interpreted as a valid spatial input source.

            ValidationError:
                If `GeoJson` validation fails.
        """
        # Normalize `str` source to `Path` or `Dict`
        _source: Optional[Union[Path, Dict[str, Any], SupportsGeoJsonInterface]] = (
            cls.parse_file_path(value=source) or cls.parse_geojson_json(value=source)
            if isinstance(source, str)
            else source
        )
        if not isinstance(_source, (Path, dict, SupportsGeoJsonInterface)):
            raise ValueError(
                f"Expected a non-empty GeoJSON-compatible source `(Path, dict, SupportsGeoJsonInterface)` but received {type(source)}: {source!r}"
            )

        # Create from a spatial file e.g., GeoJSON file, Shapefile etc.
        _geojson: Union[gpd.GeoDataFrame, Dict[str, Any] | SupportsGeoJsonInterface] = (
            cast(gpd.GeoDataFrame, gpd.read_file(_source, **kwargs))
            if isinstance(_source, Path)
            else _source
        )

        # Create from an object implementing `__geo_interface__`
        # e.g., GeoDataFrame, shapely etc.
        if isinstance(_geojson, SupportsGeoJsonInterface):
            _geojson = _geojson.__geo_interface__

        return cls(**_geojson)

    @classmethod
    def parse_file_path(
        cls, *, value: str, on_invalid: OnInvalid = OnInvalid.IGNORE
    ) -> Optional[Path]:
        """Parse, validate and convert a filesystem path into `Path`.

        Attempts to interpret a string as a valid existing file path using
        Pydantic's `TypeAdapter` and `FilePath` validator.

        Args:
            value (str):
                Candidate filesystem path.

            on_invalid (OnInvalid, default=OnInvalid.IGNORE):
                Behaviour when parsing or validation fails.

        Returns:
            Optional[Path]:
                Validated path if successful, otherwise `None`.

        Raises:
            ValidationError:
                If validation fails and `on_invalid=OnInvalid.RAISE`.

            OSError:
                If filesystem access fails and `on_invalid=OnInvalid.RAISE`.
        """
        try:
            if not cls._file_path_adapter:
                cls._file_path_adapter = TypeAdapter(FilePath)

            return cls._file_path_adapter.validate_python(value)
        except (ValidationError, OSError) as exc:
            if on_invalid == "raise":
                raise exc
            return None

    @classmethod
    def parse_geojson_json(
        cls, *, value: str, on_invalid: OnInvalid = OnInvalid.IGNORE
    ) -> Optional[Dict[str, Any]]:
        """Parse, validate and convert a GeoJSON JSON-string into `dict`.

        Args:
            value (str):
                JSON string expected to represent a GeoJSON object.

            on_invalid (OnInvalid, default=OnInvalid.IGNORE):
                Behaviour when parsing or validation fails.

        Returns:
            Optional[Dict[str, Any]]:
                Parsed GeoJSON dictionary or `None`.

        Raises:
            ValidationError:
                If JSON parsing or validation fails and `on_invalid=OnInvalid.RAISE`.

        """
        try:
            if not cls._json_dict_adapter:
                cls._json_dict_adapter = TypeAdapter(Json[Dict[str, Any]])

            return cls._json_dict_adapter.validate_python(value)
        except ValidationError as exc:
            if on_invalid == "raise":
                raise exc
            return None
