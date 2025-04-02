"""Tests for `gfwapiclient.resources.events.detail.models.response`."""

from typing import Any, Dict, cast

from gfwapiclient.resources.events.detail.models.response import (
    EventDetailItem,
    EventDetailResult,
)


def test_event_detail_item_deserializes_all_fields(
    mock_raw_event_detail_item: Dict[str, Any],
) -> None:
    """Test that `EventDetailItem` deserializes all fields correctly."""
    event_detail_item: EventDetailItem = EventDetailItem(**mock_raw_event_detail_item)
    assert event_detail_item.start is not None
    assert event_detail_item.id is not None
    assert event_detail_item.type is not None
    assert event_detail_item.position is not None
    assert event_detail_item.regions is not None
    assert event_detail_item.bounding_box is not None
    assert event_detail_item.distances is not None
    assert event_detail_item.vessel is not None
    assert event_detail_item.encounter is not None
    assert event_detail_item.fishing is not None
    assert event_detail_item.gap is not None
    assert event_detail_item.loitering is not None
    assert event_detail_item.port_visit is not None


def test_event_detail_result_deserializes_all_fields(
    mock_raw_event_detail_item: Dict[str, Any],
) -> None:
    """Test that `EventDetailResult` deserializes all fields correctly."""
    data: EventDetailItem = EventDetailItem(**mock_raw_event_detail_item)
    result = EventDetailResult(data=data)
    assert cast(EventDetailItem, result.data()) == data
