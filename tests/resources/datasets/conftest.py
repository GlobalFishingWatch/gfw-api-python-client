"""Test configurations for `gfwapiclient.resources.datasets`."""

from typing import Any, Callable, Dict, Final

import pytest


z: Final[int] = 1
x: Final[int] = 0
y: Final[int] = 1
geometry: Dict[str, Any] = {
    "type": "Polygon",
    "coordinates": [
        [
            [-180.0, -85.0511287798066],
            [-180.0, 0.0],
            [0.0, 0.0],
            [0.0, -85.0511287798066],
            [-180.0, -85.0511287798066],
        ]
    ],
}


@pytest.fixture
def mock_raw_sar_fixed_infrastructure_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for a mock raw SAR fixed infrastructure item.

    This fixture loads sample JSON data representing a single
    `SARFixedInfrastructureItem` from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `SARFixedInfrastructureItem` sample data as a dictionary.
    """
    raw_sar_fixed_infrastructure_item: Dict[str, Any] = load_json_fixture(
        "datasets/sar_fixed_infrastructure_item.json"
    )
    return raw_sar_fixed_infrastructure_item


@pytest.fixture
def mock_raw_sar_fixed_infrastructure_mvt(
    load_mvt_fixture: Callable[[str], bytes],
) -> bytes:
    """Fixture for mock raw SAR fixed infrastructure MVT data.

    This fixture loads sample binary Mapbox Vector Tile (MVT) data
    representing SAR fixed infrastructure from a fixture file.

    Returns:
        bytes:
            Raw binary MVT data for SAR fixed infrastructure.
    """
    raw_sar_fixed_infrastructure_mvt_data: bytes = load_mvt_fixture(
        "datasets/sar_fixed_infrastructure.mvt"
    )
    return raw_sar_fixed_infrastructure_mvt_data
