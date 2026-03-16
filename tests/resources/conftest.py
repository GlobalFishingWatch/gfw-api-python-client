"""Test configurations for `gfwapiclient.resources`."""

import json

from pathlib import Path
from typing import Any, Callable, Dict, List, Union

import geopandas as gpd
import pytest
import shapely

from gfwapiclient.base.models import GeoJson, SupportsGeoJsonInterface


@pytest.fixture
def mock_raw_geojson_feature_collection(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw geojson feature collection.

    This fixture loads sample JSON data representing a
    `GeoJson` feature collection from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `GeoJson` sample data as a dictionary.
    """
    raw_geojson_feature_collection: Dict[str, Any] = load_json_fixture(
        "base/geojson/geojson_featurecollection.json"
    )
    return raw_geojson_feature_collection


@pytest.fixture
def mock_raw_geojson_polygon(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw geojson polygon.

    This fixture loads sample JSON data representing a
    `GeoJson` polygon from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `GeoJson` sample data as a dictionary.
    """
    raw_geojson_polygon: Dict[str, Any] = load_json_fixture(
        "base/geojson/geojson_polygon.json"
    )
    return raw_geojson_polygon


@pytest.fixture
def mock_geojson_source_instances(
    mock_raw_geojson_feature_collection: Dict[str, Any],
    mock_raw_geojson_polygon: Dict[str, Any],
) -> List[Union[GeoJson, str, Path, Dict[str, Any], SupportsGeoJsonInterface]]:
    """Fixture for mocking `GeoJson` source instances.

    This fixture create sample objects data representing a
    list of possible `GeoJson.from_file_or_geojson` sources.

    Returns:
        List[Union[GeoJson, str, Path, Dict[str, Any], SupportsGeoJsonInterface]]:
            `GeoJson` source instances data as a list of objects.
    """
    geojson_source_instances: List[
        Union[GeoJson, str, Path, Dict[str, Any], SupportsGeoJsonInterface]
    ] = [
        GeoJson(**{**mock_raw_geojson_feature_collection}),  # GeoJson
        json.dumps({**mock_raw_geojson_feature_collection}),  # GeoJson JSON-string
        "tests/fixtures/base/geojson/geojson_featurecollection.json",  # str Path
        Path(
            "tests/fixtures/base/shapefiles/geojson_featurecollection.shp"
        ),  # Path instance
        {**mock_raw_geojson_feature_collection},  # GeoJson dictionary
        gpd.GeoDataFrame.from_features(
            {**mock_raw_geojson_feature_collection}
        ),  # GeoDataFrame from features
        gpd.read_file(
            "tests/fixtures/base/shapefiles/geojson_featurecollection.shp"
        ),  # GeoDataFrame from file
        shapely.geometry.shape({**mock_raw_geojson_polygon}),  # shapely geometry
    ]

    return geojson_source_instances
