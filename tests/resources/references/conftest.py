"""Test configurations for `gfwapiclient.resources.references`."""

from typing import Any, Dict

import pytest


@pytest.fixture
def mock_raw_eez_region_item() -> Dict[str, Any]:
    """Fixture for mock raw EEZ region item.

    Returns:
        Dict[str, Any]:
            Raw `EEZRegionItem` sample data.
    """
    raw_eez_region_item: Dict[str, Any] = {
        "id": 8371,
        "label": "Senegal",
        "iso3": "SEN",
    }
    return raw_eez_region_item


@pytest.fixture
def mock_raw_mpa_region_item() -> Dict[str, Any]:
    """Fixture for mock raw MPA region item.

    Returns:
        Dict[str, Any]:
            Raw `MPARegionItem` sample data.
    """
    raw_mpa_region_item: Dict[str, Any] = {
        "label": "Dorsal de Nasca - Reserva Nacional",
        "id": "555745302",
        "NAME": "Dorsal de Nasca",
    }
    return raw_mpa_region_item


@pytest.fixture
def mock_raw_rfmo_region_item() -> Dict[str, Any]:
    """Fixture for mock raw RFMO region item.

    Returns:
        Dict[str, Any]:
            Raw `RFMORegionItem` sample data.
    """
    raw_rfmo_region_item: Dict[str, Any] = {
        "label": "ICCAT",
        "id": "ICCAT",
        "RFB": "ICCAT",
    }
    return raw_rfmo_region_item
