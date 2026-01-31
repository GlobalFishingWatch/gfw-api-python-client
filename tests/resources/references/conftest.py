"""Test configurations for `gfwapiclient.resources.references`."""

from typing import Any, Callable, Dict

import pytest


@pytest.fixture
def mock_raw_eez_region_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw EEZ region item.

    This fixture loads sample JSON data representing a single
    `EEZRegionItem` from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `EEZRegionItem` sample data as a dictionary.
    """
    raw_eez_region_item: Dict[str, Any] = load_json_fixture(
        "references/eez_region_item.json"
    )
    return raw_eez_region_item


@pytest.fixture
def mock_raw_mpa_region_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw MPA region item.

    This fixture loads sample JSON data representing a single
    `MPARegionItem` from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `MPARegionItem` sample data as a dictionary.
    """
    raw_mpa_region_item: Dict[str, Any] = load_json_fixture(
        "references/mpa_region_item.json"
    )
    return raw_mpa_region_item


@pytest.fixture
def mock_raw_rfmo_region_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw RFMO region item.

    This fixture loads sample JSON data representing a single
    `RFMORegionItem` from a fixture file.

    Returns:
        Dict[str, Any]:
            Raw `RFMORegionItem` sample data as a dictionary.
    """
    raw_rfmo_region_item: Dict[str, Any] = load_json_fixture(
        "references/rfmo_region_item.json"
    )
    return raw_rfmo_region_item
