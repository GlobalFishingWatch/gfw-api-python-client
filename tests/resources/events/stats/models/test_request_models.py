"""Tests for `gfwapiclient.resources.events.stats.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.events.stats.models.request import EventStatsBody


def test_event_stats_request_body_serializes_all_fields(
    mock_raw_event_stats_request_body: Dict[str, Any],
) -> None:
    """Test that `EventStatsBody` serializes all fields correctly."""
    event_stats_request_body: EventStatsBody = EventStatsBody(
        **mock_raw_event_stats_request_body
    )
    assert event_stats_request_body.datasets is not None
    assert event_stats_request_body.timeseries_interval is not None
    assert event_stats_request_body.vessels is not None
    assert event_stats_request_body.types is not None
    assert event_stats_request_body.start_date is not None
    assert event_stats_request_body.end_date is not None
    assert event_stats_request_body.confidences is not None
    assert event_stats_request_body.encounter_types is not None
    assert event_stats_request_body.geometry is not None
    assert event_stats_request_body.region is not None
    assert event_stats_request_body.vessel_types is not None
    assert event_stats_request_body.vessel_groups is not None
    assert event_stats_request_body.flags is not None
    assert event_stats_request_body.duration is not None
    assert event_stats_request_body.gap_intentional_disabling is not None
    assert event_stats_request_body.includes is not None
    assert event_stats_request_body.to_json_body() is not None
