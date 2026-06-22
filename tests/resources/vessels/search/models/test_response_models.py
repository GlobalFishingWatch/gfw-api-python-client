"""Tests for `gfwapiclient.resources.vessels.search.models`."""

from typing import Any, Dict, List, cast

from gfwapiclient.resources.vessels.search.models.response import (
    VesselSearchItem,
    VesselSearchResult,
)


def test_vessel_search_item_deserializes_all_fields(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselSearchItem` deserializes all fields correctly."""
    vessel_search_item: VesselSearchItem = VesselSearchItem(**mock_raw_vessel_list_item)
    assert vessel_search_item.registry_info_total_records is not None
    assert vessel_search_item.registry_info is not None
    assert vessel_search_item.registry_owners is not None
    assert vessel_search_item.registry_public_authorizations is not None
    assert vessel_search_item.combined_sources_info is not None
    assert vessel_search_item.self_reported_info is not None
    assert vessel_search_item.dataset is not None


def test_vessel_search_result_deserializes_all_fields(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselSearchResult` deserializes all fields correctly."""
    data: List[VesselSearchItem] = [VesselSearchItem(**mock_raw_vessel_list_item)]
    result = VesselSearchResult(data=data)
    assert cast(List[VesselSearchItem], result.data()) == data


def test_vessel_search_result_vessel_ids_returns_correctly(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselSearchResult` returns list of vessel ids correctly."""
    data: List[VesselSearchItem] = [VesselSearchItem(**mock_raw_vessel_list_item)]
    result = VesselSearchResult(data=data)
    assert result.vessel_ids is not None
    assert isinstance(result.vessel_ids, list)
    assert len(result.vessel_ids) >= 1


def test_vessel_search_result_transmission_dates_from_returns_correctly(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselSearchResult` transmission dates from returns list of transmission start dates correctly."""
    data: List[VesselSearchItem] = [VesselSearchItem(**mock_raw_vessel_list_item)]
    result = VesselSearchResult(data=data)
    assert result.transmission_dates_from is not None
    assert isinstance(result.transmission_dates_from, list)
    assert len(result.transmission_dates_from) >= 1


def test_vessel_search_result_transmission_dates_to_returns_correctly(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselSearchResult` transmission dates to returns list of transmission end dates correctly."""
    data: List[VesselSearchItem] = [VesselSearchItem(**mock_raw_vessel_list_item)]
    result = VesselSearchResult(data=data)
    assert result.transmission_dates_to is not None
    assert isinstance(result.transmission_dates_to, list)
    assert len(result.transmission_dates_to) >= 1
