"""Tests for `gfwapiclient.resources.vessels.detail.models.response`."""

from typing import Any, Dict, cast

from gfwapiclient.resources.vessels.detail.models.response import (
    VesselDetailItem,
    VesselDetailResult,
)


def test_vessel_detail_item_deserializes_all_fields(
    mock_raw_vessel_detail_item: Dict[str, Any],
) -> None:
    """Test that `VesselDetailItem` deserializes all fields correctly."""
    vessel_detail_item: VesselDetailItem = VesselDetailItem(
        **mock_raw_vessel_detail_item
    )
    assert vessel_detail_item.registry_info_total_records is not None
    assert vessel_detail_item.registry_info is not None
    assert vessel_detail_item.registry_owners is not None
    assert vessel_detail_item.registry_public_authorizations is not None
    assert vessel_detail_item.combined_sources_info is not None
    assert vessel_detail_item.self_reported_info is not None
    assert vessel_detail_item.dataset is not None


# def test_vessel_detail_item_vessel_ids_yields_correctly(
#     mock_raw_vessel_detail_item: Dict[str, Any],
# ) -> None:
#     """Test that `VesselDetailItem` yields vessel ids correctly."""
#     vessel_detail_item: VesselDetailItem = VesselDetailItem(
#         **mock_raw_vessel_detail_item
#     )
#     assert vessel_detail_item.vessel_ids is not None
#     assert isinstance(vessel_detail_item.vessel_ids, Iterator)
#     assert len(list(vessel_detail_item.vessel_ids)) >= 1


def test_vessel_detail_result_deserializes_all_fields(
    mock_raw_vessel_detail_item: Dict[str, Any],
) -> None:
    """Test that `VesselDetailResult` deserializes all fields correctly."""
    data: VesselDetailItem = VesselDetailItem(**mock_raw_vessel_detail_item)
    result = VesselDetailResult(data=data)
    assert cast(VesselDetailItem, result.data()) == data


def test_vessel_detail_result_vessel_ids_returns_correctly(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselDetailResult` returns list of vessel ids correctly."""
    data: VesselDetailItem = VesselDetailItem(**mock_raw_vessel_list_item)
    result = VesselDetailResult(data=data)
    assert result.vessel_ids is not None
    assert isinstance(result.vessel_ids, list)
    assert len(result.vessel_ids) >= 1
