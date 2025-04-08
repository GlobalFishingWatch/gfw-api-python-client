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
    assert vessel_insight_item.coverage is not None
    assert vessel_insight_item.apparent_fishing is not None
    assert vessel_insight_item.vessel_identity is not None


def test_vessel_insight_result_deserializes_all_fields(
    mock_raw_vessel_insight_item: Dict[str, Any],
) -> None:
    """Test that `VesselInsightResult` deserializes all fields correctly."""
    data: VesselInsightItem = VesselInsightItem(**mock_raw_vessel_insight_item)
    result = VesselInsightResult(data=data)
    assert cast(VesselInsightItem, result.data()) == data
