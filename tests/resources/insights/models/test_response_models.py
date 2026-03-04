"""Tests for `gfwapiclient.resources.insights.models.response`."""

from typing import Any, Dict, cast

from gfwapiclient.resources.insights.models.response import (
    VesselInsightItem,
    VesselInsightResult,
)


def test_vessel_insight_item_derializes_all_fields(
    mock_raw_vessel_insight_item: Dict[str, Any],
) -> None:
    """Test that `VesselInsightBody` serializes all fields correctly."""
    vessel_insight_item: VesselInsightItem = VesselInsightItem(
        **mock_raw_vessel_insight_item
    )
    assert vessel_insight_item.period is not None

    assert vessel_insight_item.gap is not None
    assert vessel_insight_item.gap.datasets is not None
    assert vessel_insight_item.gap.historical_counters is not None
    assert vessel_insight_item.gap.period_selected_counters is not None
    assert vessel_insight_item.gap.ais_off is not None

    assert vessel_insight_item.coverage is not None
    assert vessel_insight_item.coverage.blocks is not None
    assert vessel_insight_item.coverage.blocks_with_positions is not None
    assert vessel_insight_item.coverage.percentage is not None

    assert vessel_insight_item.apparent_fishing is not None
    assert vessel_insight_item.apparent_fishing.datasets is not None
    assert vessel_insight_item.apparent_fishing.historical_counters is not None
    assert vessel_insight_item.apparent_fishing.period_selected_counters is not None
    assert (
        vessel_insight_item.apparent_fishing.events_in_rfmo_without_known_authorization
        is not None
    )
    assert vessel_insight_item.apparent_fishing.events_in_no_take_mpas is not None

    assert vessel_insight_item.vessel_identity is not None
    assert vessel_insight_item.vessel_identity.datasets is not None
    assert vessel_insight_item.vessel_identity.flag_changes is not None
    assert vessel_insight_item.vessel_identity.iuu_vessel_list is not None
    assert vessel_insight_item.vessel_identity.mou_list is not None


def test_vessel_insight_result_deserializes_all_fields(
    mock_raw_vessel_insight_item: Dict[str, Any],
) -> None:
    """Test that `VesselInsightResult` deserializes all fields correctly."""
    data: VesselInsightItem = VesselInsightItem(**mock_raw_vessel_insight_item)
    result = VesselInsightResult(data=data)
    assert cast(VesselInsightItem, result.data()) == data
