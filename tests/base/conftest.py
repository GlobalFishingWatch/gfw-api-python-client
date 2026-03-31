"""Test configurations for `gfwapiclient.base`."""

from typing import Any, Callable, Dict, List

import pytest


@pytest.fixture
def mock_raw_geojson_feature(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw geojson feature.

    This fixture loads sample JSON data representing a
    `GeoJson` feature from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `GeoJson` sample data as a dictionary.
    """
    raw_geojson_feature: Dict[str, Any] = load_json_fixture(
        "base/geojson/geojson_feature.json"
    )
    return raw_geojson_feature


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
def mock_raw_geojson_geometrycollection(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw geojson geometry collection.

    This fixture loads sample JSON data representing a
    `GeoJson` geojson geometry collection from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `GeoJson` sample data as a dictionary.
    """
    raw_geojson_geometrycollection: Dict[str, Any] = load_json_fixture(
        "base/geojson/geojson_geometrycollection.json"
    )
    return raw_geojson_geometrycollection


@pytest.fixture
def mock_raw_geojson_linestring(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw geojson linestring.

    This fixture loads sample JSON data representing a
    `GeoJson` linestring from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `GeoJson` sample data as a dictionary.
    """
    raw_geojson_linestring: Dict[str, Any] = load_json_fixture(
        "base/geojson/geojson_linestring.json"
    )
    return raw_geojson_linestring


@pytest.fixture
def mock_raw_geojson_multilinestring(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw geojson multilinestring.

    This fixture loads sample JSON data representing a
    `GeoJson` multilinestring from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `GeoJson` sample data as a dictionary.
    """
    raw_geojson_multilinestring: Dict[str, Any] = load_json_fixture(
        "base/geojson/geojson_multilinestring.json"
    )
    return raw_geojson_multilinestring


@pytest.fixture
def mock_raw_geojson_multipoint(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw geojson multipoint.

    This fixture loads sample JSON data representing a
    `GeoJson` multipoint from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `GeoJson` sample data as a dictionary.
    """
    raw_geojson_multipoint: Dict[str, Any] = load_json_fixture(
        "base/geojson/geojson_multipoint.json"
    )
    return raw_geojson_multipoint


@pytest.fixture
def mock_raw_geojson_multipolygon(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw geojson multipolygon.

    This fixture loads sample JSON data representing a
    `GeoJson` multipolygon from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `GeoJson` sample data as a dictionary.
    """
    raw_geojson_multipolygon: Dict[str, Any] = load_json_fixture(
        "base/geojson/geojson_multipolygon.json"
    )
    return raw_geojson_multipolygon


@pytest.fixture
def mock_raw_geojson_point(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw geojson point.

    This fixture loads sample JSON data representing a
    `GeoJson` point from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `GeoJson` sample data as a dictionary.
    """
    raw_geojson_point: Dict[str, Any] = load_json_fixture(
        "base/geojson/geojson_point.json"
    )
    return raw_geojson_point


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
def mock_raw_geojson_features(
    mock_raw_geojson_geometrycollection: Dict[str, Any],
    mock_raw_geojson_linestring: Dict[str, Any],
    mock_raw_geojson_multilinestring: Dict[str, Any],
    mock_raw_geojson_multipoint: Dict[str, Any],
    mock_raw_geojson_multipolygon: Dict[str, Any],
    mock_raw_geojson_point: Dict[str, Any],
    mock_raw_geojson_polygon: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """Fixture for a mock raw geojson features.

    This fixture create sample JSON data representing a
    list of `GeoJSON` features.

    Returns:
        List[Dict[str, Any]]:
            Raw `GeoJSON` sample features data as a list of dictionaries.
    """
    raw_geojson_features: List[Dict[str, Any]] = [
        {
            "type": "Feature",
            "geometry": {**mock_raw_geojson_feature},
            "properties": None,
        }
        for mock_raw_geojson_feature in [
            mock_raw_geojson_geometrycollection,  # GeometryCollection
            mock_raw_geojson_linestring,  # LineString
            mock_raw_geojson_multilinestring,  # MultiLineString
            mock_raw_geojson_multipoint,  # MultiPoint
            mock_raw_geojson_multipolygon,  # MultiPolygon
            mock_raw_geojson_point,  # Point
            mock_raw_geojson_polygon,  # Polygon
        ]
    ]
    return raw_geojson_features


@pytest.fixture
def mock_raw_geojson_feature_collections(
    mock_raw_geojson_features: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Fixture for a mock raw geojson feature collections.

    This fixture create sample JSON data representing a
    list of `GeoJSON` feature collections.

    Returns:
        List[Dict[str, Any]]:
            Raw `GeoJSON` sample feature collections data as a list of dictionaries.
    """
    raw_geojson_feature_collections: List[Dict[str, Any]] = [
        {
            "type": "FeatureCollection",
            "features": mock_raw_features,  # At least 2 features
        }
        for mock_raw_features in [
            mock_raw_geojson_features[-idx:]
            for idx in range(2, len(mock_raw_geojson_features) + 1)
        ]
    ]
    return raw_geojson_feature_collections
