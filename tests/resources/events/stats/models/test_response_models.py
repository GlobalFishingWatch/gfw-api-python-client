"""Tests for `gfwapiclient.resources.events.stats.models.response`."""

from typing import Any, Dict, cast

from gfwapiclient.resources.events.stats.models.response import (
    EventStatsItem,
    EventStatsResult,
)


def test_event_stats_item_deserializes_all_fields(
    mock_raw_event_stats_item: Dict[str, Any],
) -> None:
    """Test that `EventStatsItem` deserializes all fields correctly."""
    event_stats_item: EventStatsItem = EventStatsItem(**mock_raw_event_stats_item)
    assert event_stats_item.num_events is not None
    assert event_stats_item.num_flags is not None
    assert event_stats_item.num_vessels is not None
    assert event_stats_item.flags is not None
    assert event_stats_item.timeseries is not None


def test_event_stats_result_deserializes_all_fields(
    mock_raw_event_stats_item: Dict[str, Any],
) -> None:
    """Test that `EventStatsResult` deserializes all fields correctly."""
    data: EventStatsItem = EventStatsItem(**mock_raw_event_stats_item)
    result = EventStatsResult(data=data)
    assert cast(EventStatsItem, result.data()) == data
