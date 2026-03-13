"""Tests for `gfwapiclient.base.models.BaseModel`."""

import json

from pathlib import Path
from typing import Any, Dict, Union

import geopandas as gpd
import pytest
import shapely

from geojson_pydantic.features import Feature, FeatureCollection
from pydantic import ValidationError

from gfwapiclient.base.models import GeoJson, OnInvalid, SupportsGeoJsonInterface


def assert_valid_geojson(geojson: GeoJson) -> None:
    """Assert that an object is a valid `GeoJson`.

    Its checks:
        - Object is a `GeoJson` instance
        - Object is a GeoJSON `FeatureCollection``
        - Supports `__geo_interface__`
        - Contains at least one Feature

    Args:
        geojson (GeoJson):
            Object to validate.
    """
    assert isinstance(geojson, GeoJson)
    assert isinstance(geojson, FeatureCollection)
    assert isinstance(geojson, SupportsGeoJsonInterface)
    assert hasattr(geojson, "__geo_interface__")
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert geojson.length >= 1
    assert len(geojson.features) >= 1
    assert isinstance(geojson.features[0], Feature) is True
    assert hasattr(geojson.features[0], "__geo_interface__")


def test_geojson_model_serializes_feature_to_feature_collection(
    mock_raw_geojson_feature: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes feature correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_feature)

    assert_valid_geojson(geojson)
    assert geojson.features[0].model_dump(mode="json") == mock_raw_geojson_feature


def test_geojson_model_serializes_feature_collection(
    mock_raw_geojson_feature_collection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_feature_collection)

    assert_valid_geojson(geojson)
    assert geojson.model_dump(mode="json") == mock_raw_geojson_feature_collection


def test_geojson_model_serializes_geometrycollection_to_feature_collection(
    mock_raw_geojson_geometrycollection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes geometrycollection to feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_geometrycollection)

    assert_valid_geojson(geojson)

    feature_model_dump: Dict[str, Any] = geojson.features[0].model_dump(mode="json")
    assert (
        feature_model_dump["geometry"]["type"]
        == mock_raw_geojson_geometrycollection["type"]
    )
    assert (
        feature_model_dump["geometry"]["geometries"]
        == mock_raw_geojson_geometrycollection["geometries"]
    )


def test_geojson_model_serializes_linestring_to_feature_collection(
    mock_raw_geojson_linestring: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes linestring to feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_linestring)

    assert_valid_geojson(geojson)

    feature_model_dump: Dict[str, Any] = geojson.features[0].model_dump(mode="json")
    assert feature_model_dump["geometry"]["type"] == mock_raw_geojson_linestring["type"]
    assert (
        feature_model_dump["geometry"]["coordinates"]
        == mock_raw_geojson_linestring["coordinates"]
    )


def test_geojson_model_serializes_multilinestring_to_feature_collection(
    mock_raw_geojson_multilinestring: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes multilinestring to feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_multilinestring)

    assert_valid_geojson(geojson)

    feature_model_dump: Dict[str, Any] = geojson.features[0].model_dump(mode="json")
    assert (
        feature_model_dump["geometry"]["type"]
        == mock_raw_geojson_multilinestring["type"]
    )
    assert (
        feature_model_dump["geometry"]["coordinates"]
        == mock_raw_geojson_multilinestring["coordinates"]
    )


def test_geojson_model_serializes_multipoint_to_feature_collection(
    mock_raw_geojson_multipoint: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes multipoint to feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_multipoint)

    assert_valid_geojson(geojson)

    feature_model_dump: Dict[str, Any] = geojson.features[0].model_dump(mode="json")
    assert feature_model_dump["geometry"]["type"] == mock_raw_geojson_multipoint["type"]
    assert (
        feature_model_dump["geometry"]["coordinates"]
        == mock_raw_geojson_multipoint["coordinates"]
    )


def test_geojson_model_serializes_multipolygon_to_feature_collection(
    mock_raw_geojson_multipolygon: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes multipolygon to feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_multipolygon)

    assert_valid_geojson(geojson)

    feature_model_dump: Dict[str, Any] = geojson.features[0].model_dump(mode="json")
    assert (
        feature_model_dump["geometry"]["type"] == mock_raw_geojson_multipolygon["type"]
    )
    assert (
        feature_model_dump["geometry"]["coordinates"]
        == mock_raw_geojson_multipolygon["coordinates"]
    )


def test_geojson_model_serializes_point_to_feature_collection(
    mock_raw_geojson_point: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes point to feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_point)

    assert_valid_geojson(geojson)

    feature_model_dump: Dict[str, Any] = geojson.features[0].model_dump(mode="json")
    assert feature_model_dump["geometry"]["type"] == mock_raw_geojson_point["type"]
    assert (
        feature_model_dump["geometry"]["coordinates"]
        == mock_raw_geojson_point["coordinates"]
    )


def test_geojson_model_serializes_polygon_to_feature_collection(
    mock_raw_geojson_polygon: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes polygon to feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_polygon)

    assert_valid_geojson(geojson)

    feature_model_dump: Dict[str, Any] = geojson.features[0].model_dump(mode="json")
    assert feature_model_dump["geometry"]["type"] == mock_raw_geojson_polygon["type"]
    assert (
        feature_model_dump["geometry"]["coordinates"]
        == mock_raw_geojson_polygon["coordinates"]
    )


@pytest.mark.parametrize(
    "invalid_data",
    [
        {},
        {"type": "invalid_type"},
        {"type": "Point"},
        {"coordinates": []},
        {"geometries": []},
        {"features": []},
        {"geometry": []},
        {"type": "FeatureCollection", "features": None},
        {"type": "Feature", "geometry": None},
        {"type": "GeometryCollection", "geometries": None},
        {"type": "Point", "coordinates": None},
    ],
)
def test_geojson_model_serializes_invalid_data_raises_validation_error(
    invalid_data: Any,
) -> None:
    """Test that `GeoJson` serializes raises a `ValidationError` on invalid data."""
    with pytest.raises(ValidationError):
        GeoJson(**invalid_data)


@pytest.mark.parametrize(
    "invalid_source",
    [
        None,  # Unsupported type
        "null",  # None JSON-string
        12345,  # Unsupported type
        "not a path or json",  # Unsupported value
        "path/to/invalid/spatial/file.shp",  # Does not point to a file
        "path/to/invalid/spatial/file.json",  # Does not point to a file
    ],
)
def test_geojson_model_from_file_or_geojson_invalid_source_raises_value_error(
    invalid_source: Any,
) -> None:
    """Test that `GeoJson` from file or geojson raises a `ValueError` on invalid source."""
    with pytest.raises(ValueError):
        GeoJson.from_file_or_geojson(source=invalid_source)


@pytest.mark.parametrize(
    "invalid_geojson_source",
    [
        {},
        "{}",
        {"type": "invalid_type"},
        '{"type": "invalid_type"}',
        {"type": "Point"},
        '{"type": "Point"}',
        {"coordinates": []},
        '{"coordinates": []}',
        {"geometries": []},
        '{"geometries": []}',
        {"features": []},
        '{"features": []}',
        {"geometry": []},
        '{"geometry": []}',
        {"type": "FeatureCollection", "features": None},
        '{"type": "FeatureCollection", "features": null}',
        {"type": "Feature", "geometry": None},
        '{"type": "Feature", "geometry": null}',
        {"type": "GeometryCollection", "geometries": None},
        '{"type": "GeometryCollection", "geometries": null}',
        {"type": "Point", "coordinates": None},
        '{"type": "Point", "coordinates": null}',
    ],
)
def test_geojson_model_from_file_or_geojson_invalid_geojson_source_raises_validation_error(
    invalid_geojson_source: Any,
) -> None:
    """Test that `GeoJson` from file or geojson raises a `ValidationError` on invalid geojson source."""
    with pytest.raises(ValidationError):
        GeoJson.from_file_or_geojson(source=invalid_geojson_source)


@pytest.mark.parametrize(
    "filename",
    [
        "tests/fixtures/base/geojson/geojson_featurecollection.json",
        Path("tests/fixtures/base/geojson/geojson_featurecollection.json"),
        "tests/fixtures/base/shapefiles/geojson_featurecollection.shp",
        Path("tests/fixtures/base/shapefiles/geojson_featurecollection.shp"),
    ],
)
def test_geojson_model_create_from_valid_file_source(
    filename: Union[str, Path],
) -> None:
    """Test that `GeoJson` can be created from a valid file source correctly."""
    geojson: GeoJson = GeoJson.from_file_or_geojson(source=filename)

    assert_valid_geojson(geojson)


def test_geojson_model_create_from_valid_geojson_dict_source(
    mock_raw_geojson_feature_collection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` can be created from a valid geojson source correctly."""
    geojson: GeoJson = GeoJson.from_file_or_geojson(
        source=mock_raw_geojson_feature_collection
    )

    assert_valid_geojson(geojson)


def test_geojson_model_create_from_valid_geojson_string_source(
    mock_raw_geojson_feature_collection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` can be created from a valid geojson string source correctly."""
    geojson: GeoJson = GeoJson.from_file_or_geojson(
        source=json.dumps(mock_raw_geojson_feature_collection)
    )

    assert_valid_geojson(geojson)


def test_geojson_model_create_from_valid_geojson_protocol_source(
    mock_raw_geojson_feature_collection: Dict[str, Any],
    mock_raw_geojson_polygon: Dict[str, Any],
) -> None:
    """Test that `GeoJson` can be created from a valid geojson protocol source correctly."""
    sources = [
        GeoJson(**mock_raw_geojson_feature_collection),  # GeoJson
        gpd.GeoDataFrame.from_features(
            {**mock_raw_geojson_feature_collection}
        ),  # GeoDataFrame
        shapely.geometry.shape({**mock_raw_geojson_polygon}),  # shapely geometry
    ]

    for source in sources:
        geojson: GeoJson = GeoJson.from_file_or_geojson(source=source)

        assert_valid_geojson(geojson)


def test_geojson_model_serialize_deserialize_roundtrips(
    mock_raw_geojson_feature_collection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` can be serialized and deserialized without loss."""
    original: GeoJson = GeoJson(**mock_raw_geojson_feature_collection)
    reconstructed: GeoJson = GeoJson(**original.model_dump(mode="json"))

    assert_valid_geojson(original)
    assert_valid_geojson(reconstructed)
    assert original.model_dump(mode="json") == reconstructed.model_dump(mode="json")


def test_geojson_model_geo_interface_roundtrips(
    mock_raw_geojson_feature_collection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` can be serialized and deserialized from `__geo_interface__` without loss."""
    original: GeoJson = GeoJson(**mock_raw_geojson_feature_collection)
    reconstructed: GeoJson = GeoJson(**original.__geo_interface__)

    assert_valid_geojson(original)
    assert_valid_geojson(reconstructed)
    assert original.__geo_interface__ == reconstructed.__geo_interface__


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,  # Unsupported type
        "null",  # None JSON-string
        12345,  # Unsupported type
        "not a path or json",  # Unsupported value
        "path/to/invalid/spatial/file.shp",  # Does not point to a file
        "path/to/invalid/spatial/file.json",  # Does not point to a file
    ],
)
def test_geojson_model_parse_filename_invalid_value_raises_validation_error(
    invalid_value: Any,
) -> None:
    """Test that `GeoJson` parse filename raises a `ValidationError` on invalid file path."""
    with pytest.raises(ValidationError):
        GeoJson.parse_file_path(value=invalid_value, on_invalid=OnInvalid.RAISE)


@pytest.mark.parametrize(
    "invalid_value",
    [
        None,  # Unsupported type
        "null",  # None JSON-string
        12345,  # Unsupported type
        "not a path or json",  # Unsupported value
        "path/to/invalid/spatial/file.shp",  # Does not point to a file
        "path/to/invalid/spatial/file.json",  # Does not point to a file
    ],
)
def test_geojson_model_parse_geojson_str_invalid_value_raises_validation_error(
    invalid_value: Any,
) -> None:
    """Test that `GeoJson` parse geojson string raises a `ValidationError` on invalid geojson value."""
    with pytest.raises(ValidationError):
        GeoJson.parse_geojson_json(value=invalid_value, on_invalid=OnInvalid.RAISE)


def test_geojson_model_supports_geo_interface_protocol_isinstance_runtime_check() -> (
    None
):
    """Test that `SupportsGeoJsonInterface` supports isinstance runtime check correctly."""

    class SampleGeo:
        """A sample model for testing `SupportsGeoJsonInterface` behavior."""

        @property
        def __geo_interface__(self) -> Dict[str, Any]:
            return {"type": "Point", "coordinates": [0, 0]}

    sample_geo: SampleGeo = SampleGeo()
    assert isinstance(sample_geo, SupportsGeoJsonInterface)
    assert sample_geo.__geo_interface__ is not None
