"""Tests for `gfwapiclient.resources.events.base.models.response`."""

from typing import Any, Dict, List

import pytest

from gfwapiclient.resources.events.base.models.response import (
    EventItem,
    EventResult,
)


def test_event_result_vessel_ids_returns_correctly(
    mock_raw_event_list_item: Dict[str, Any],
) -> None:
    """Test that `EventResult` returns list of vessel ids correctly."""
    data: List[EventItem] = [EventItem(**mock_raw_event_list_item)]
    result = EventResult(data=data)
    assert result.vessel_ids is not None
    assert isinstance(result.vessel_ids, list)
    assert len(result.vessel_ids) >= 1


@pytest.mark.parametrize(
    "update",
    [
        {"vessel": None},
        {"vessel": {"id": None}},
        {"vessel": {"id": ""}},
        {"vessel": {"id": " "}},
    ],
)
def test_event_result_vessel_ids_returns_empty_list_when_vessel_or_id_missing(
    mock_raw_event_list_item: Dict[str, Any],
    update: Dict[str, Any],
) -> None:
    """Test that `EventResult` vessel ids returns empty list when vessel or id missing."""
    mocked_raw_event_list_item: Dict[str, Any] = {**mock_raw_event_list_item}
    for k, v in update.items():
        mocked_raw_event_list_item[k] = v

    data: List[EventItem] = [EventItem(**mocked_raw_event_list_item)]
    result = EventResult(data=data)
    assert result.vessel_ids is not None
    assert isinstance(result.vessel_ids, list)
    assert len(result.vessel_ids) == 0


def test_event_result_start_dates_returns_correctly(
    mock_raw_event_list_item: Dict[str, Any],
) -> None:
    """Test that `EventResult` start dates returns list of start dates correctly."""
    data: List[EventItem] = [EventItem(**mock_raw_event_list_item)]
    result = EventResult(data=data)
    assert result.start_dates is not None
    assert isinstance(result.start_dates, list)
    assert len(result.start_dates) >= 1


def test_event_result_end_dates_returns_correctly(
    mock_raw_event_list_item: Dict[str, Any],
) -> None:
    """Test that `EventResult` end dates to returns list of end dates correctly."""
    data: List[EventItem] = [EventItem(**mock_raw_event_list_item)]
    result = EventResult(data=data)
    assert result.end_dates is not None
    assert isinstance(result.end_dates, list)
    assert len(result.end_dates) == 0
