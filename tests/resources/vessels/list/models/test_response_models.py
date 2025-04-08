"""Tests for `gfwapiclient.resources.vessels.list.models.response`."""

from typing import Any, Dict, List, cast

from gfwapiclient.resources.vessels.list.models.response import (
    VesselListItem,
    VesselListResult,
)


def test_vessel_list_item_deserializes_all_fields(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselListItem` deserializes all fields correctly."""
    vessel_list_item: VesselListItem = VesselListItem(**mock_raw_vessel_list_item)
    assert vessel_list_item.registry_info_total_records is not None
    assert vessel_list_item.registry_info is not None
    assert vessel_list_item.registry_owners is not None
    assert vessel_list_item.registry_public_authorizations is not None
    assert vessel_list_item.combined_sources_info is not None
    assert vessel_list_item.self_reported_info is not None
    assert vessel_list_item.dataset is not None


def test_vessel_list_result_deserializes_all_fields(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselListResult` deserializes all fields correctly."""
    data: List[VesselListItem] = [VesselListItem(**mock_raw_vessel_list_item)]
    result = VesselListResult(data=data)
    assert cast(List[VesselListItem], result.data()) == data
