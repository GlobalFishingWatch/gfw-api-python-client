"""Tests for `gfwapiclient.base.models.BaseModel`."""

import json

from pathlib import Path
from typing import Any, Dict, Optional, Union

import pytest

from geojson_pydantic.features import Feature, FeatureCollection
from pydantic import ValidationError

from gfwapiclient.base.models import GeoJson


def test_geojson_model_serializes_feature_to_feature_collection(
    mock_raw_geojson_feature: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes feature correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_feature)

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1
    assert isinstance(geojson.features[0], Feature) is True

    assert geojson.features[0].model_dump(mode="json") == mock_raw_geojson_feature


def test_geojson_model_serializes_feature_collection(
    mock_raw_geojson_feature_collection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_feature_collection)

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1

    assert geojson.model_dump(mode="json") == mock_raw_geojson_feature_collection


def test_geojson_model_serializes_geometrycollection_to_feature_collection(
    mock_raw_geojson_geometrycollection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` serializes geometrycollection to feature collection correctly."""
    geojson: GeoJson = GeoJson(**mock_raw_geojson_geometrycollection)

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1
    assert isinstance(geojson.features[0], Feature) is True

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

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1
    assert isinstance(geojson.features[0], Feature) is True

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

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1
    assert isinstance(geojson.features[0], Feature) is True

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

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1
    assert isinstance(geojson.features[0], Feature) is True

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

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1
    assert isinstance(geojson.features[0], Feature) is True

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

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1
    assert isinstance(geojson.features[0], Feature) is True

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

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1
    assert isinstance(geojson.features[0], Feature) is True

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
    ],
)
def test_geojson_model_raises_validation_error_on_invalid_geojson_input_data(
    invalid_data: Any,
) -> None:
    """Tests that `GeoJson` raises a `ValidationError` on invalid geojson input data."""
    with pytest.raises(ValidationError):
        GeoJson(**invalid_data)


@pytest.mark.parametrize(
    "filename",
    [
        "tests/fixtures/base/geojson/geojson_featurecollection.json",
        "tests/fixtures/base/shapefiles/geojson_featurecollection.shp",
    ],
)
def test_geojson_model_create_from_file(filename: Optional[Union[str, Path]]) -> None:
    """Test that `GeoJson` can be created from a file correctly."""
    geojson: GeoJson = GeoJson.from_file_or_geojson(filename=filename)

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1


def test_geojson_model_create_from_geojson(
    mock_raw_geojson_feature_collection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` can be created from a geojson correctly."""
    geojson: GeoJson = GeoJson.from_file_or_geojson(
        geojson=mock_raw_geojson_feature_collection
    )

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1


def test_geojson_model_create_from_geojson_string(
    mock_raw_geojson_feature_collection: Dict[str, Any],
) -> None:
    """Test that `GeoJson` can be created from a geojson string correctly."""
    geojson: GeoJson = GeoJson.from_file_or_geojson(
        geojson=json.dumps(mock_raw_geojson_feature_collection)
    )

    assert isinstance(geojson, FeatureCollection)
    assert geojson.type == "FeatureCollection"
    assert geojson.features is not None
    assert len(geojson.features) == 1
