"""Tests for `gfwapiclient.resources.references.regions.models.response`."""

from typing import Any, Dict, List, cast

from gfwapiclient.resources.references.regions.models.response import (
    EEZRegionItem,
    EEZRegionResult,
    MPARegionItem,
    MPARegionResult,
    RFMORegionItem,
    RFMORegionResult,
)


def test_eez_region_item_deserializes_all_fields(
    mock_raw_eez_region_item: Dict[str, Any],
) -> None:
    """Test that `EEZRegionItem` deserializes all fields correctly."""
    eez_region_item = EEZRegionItem(**mock_raw_eez_region_item)
    assert eez_region_item.id == mock_raw_eez_region_item["id"]
    assert eez_region_item.label == mock_raw_eez_region_item["label"]
    assert eez_region_item.iso3 == mock_raw_eez_region_item["iso3"]
    assert eez_region_item.dataset == "public-eez-areas"


def test_mpa_region_item_deserializes_all_fields(
    mock_raw_mpa_region_item: Dict[str, Any],
) -> None:
    """Test that `MPARegionItem` deserializes all fields correctly."""
    mpa_region_item = MPARegionItem(**mock_raw_mpa_region_item)
    assert mpa_region_item.id == mock_raw_mpa_region_item["id"]
    assert mpa_region_item.label == mock_raw_mpa_region_item["label"]
    assert mpa_region_item.name == mock_raw_mpa_region_item["NAME"]
    assert mpa_region_item.dataset == "public-mpa-all"


def test_rfmo_region_item_deserializes_all_fields(
    mock_raw_rfmo_region_item: Dict[str, Any],
) -> None:
    """Test that `RFMORegionItem` deserializes all fields correctly."""
    rfmo_region_item = RFMORegionItem(**mock_raw_rfmo_region_item)
    assert rfmo_region_item.id == mock_raw_rfmo_region_item["id"]
    assert rfmo_region_item.label == mock_raw_rfmo_region_item["label"]
    assert rfmo_region_item.rfb == mock_raw_rfmo_region_item["RFB"]
    assert rfmo_region_item.dataset == "public-rfmo"


def test_eez_region_result_deserializes_all_fields(
    mock_raw_eez_region_item: Dict[str, Any],
) -> None:
    """Test that `EEZRegionResult` deserializes all fields correctly."""
    data: List[EEZRegionItem] = [EEZRegionItem(**mock_raw_eez_region_item)]
    result = EEZRegionResult(data=data)
    assert cast(List[EEZRegionItem], result.data()) == data


def test_mpa_region_result_deserializes_all_fields(
    mock_raw_mpa_region_item: Dict[str, Any],
) -> None:
    """Test that `MPARegionResult` deserializes all fields correctly."""
    data: List[MPARegionItem] = [MPARegionItem(**mock_raw_mpa_region_item)]
    result = MPARegionResult(data=data)
    assert cast(List[MPARegionItem], result.data()) == data


def test_rfmo_region_result_deserializes_all_fields(
    mock_raw_rfmo_region_item: Dict[str, Any],
) -> None:
    """Test that `RFMORegionResult` deserializes all fields correctly."""
    data: List[RFMORegionItem] = [RFMORegionItem(**mock_raw_rfmo_region_item)]
    result = RFMORegionResult(data=data)
    assert cast(List[RFMORegionItem], result.data()) == data
