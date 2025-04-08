"""Tests for `gfwapiclient.resources.insights.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.insights.models.request import VesselInsightBody


def test_vessel_insight_request_body_serializes_all_fields(
    mock_raw_vessel_insight_request_body: Dict[str, Any],
) -> None:
    """Test that `VesselInsightBody` serializes all fields correctly."""
    vessel_insight_body: VesselInsightBody = VesselInsightBody(
        **mock_raw_vessel_insight_request_body
    )
    assert vessel_insight_body.includes is not None
    assert vessel_insight_body.start_date is not None
    assert vessel_insight_body.end_date is not None
    assert vessel_insight_body.vessels is not None
    assert vessel_insight_body.to_json_body() == mock_raw_vessel_insight_request_body
