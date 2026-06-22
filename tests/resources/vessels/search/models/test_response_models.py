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


# def test_vessel_search_item_vessel_ids_yields_correctly(
#     mock_raw_vessel_list_item: Dict[str, Any],
# ) -> None:
#     """Test that `VesselSearchItem` yields vessel ids correctly."""
#     vessel_search_item: VesselSearchItem = VesselSearchItem(**mock_raw_vessel_list_item)
#     assert vessel_search_item.vessel_ids is not None
#     assert isinstance(vessel_search_item.vessel_ids, Iterator)
#     assert len(list(vessel_search_item.vessel_ids)) >= 1


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
