"""Tests for `gfwapiclient.resources.events.list.models.response`."""

from typing import Any, Dict, List, cast

from gfwapiclient.resources.events.list.models.response import (
    EventListItem,
    EventListResult,
)


def test_event_list_item_deserializes_all_fields(
    mock_raw_event_list_item: Dict[str, Any],
) -> None:
    """Test that `EventListItem` deserializes all fields correctly."""
    event_list_item: EventListItem = EventListItem(**mock_raw_event_list_item)
    assert event_list_item.start is not None
    assert event_list_item.id is not None
    assert event_list_item.type is not None
    assert event_list_item.position is not None
    assert event_list_item.regions is not None
    assert event_list_item.bounding_box is not None
    assert event_list_item.distances is not None
    assert event_list_item.vessel is not None
    assert event_list_item.encounter is not None
    assert event_list_item.fishing is not None
    assert event_list_item.gap is not None
    assert event_list_item.loitering is not None
    assert event_list_item.port_visit is not None


def test_event_list_result_deserializes_all_fields(
    mock_raw_event_list_item: Dict[str, Any],
) -> None:
    """Test that `EventListResult` deserializes all fields correctly."""
    data: List[EventListItem] = [EventListItem(**mock_raw_event_list_item)]
    result = EventListResult(data=data)
    assert cast(List[EventListItem], result.data()) == data
