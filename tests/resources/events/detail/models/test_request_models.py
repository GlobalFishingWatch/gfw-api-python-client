"""Tests for `gfwapiclient.resources.events.detail.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.events.detail.models.request import EventDetailParams


def test_event_detail_request_params_serializes_all_fields(
    mock_raw_event_detail_request_params: Dict[str, Any],
) -> None:
    """Test that `EventDetailParams` serializes all fields correctly."""
    event_detail_request_params: EventDetailParams = EventDetailParams(
        **mock_raw_event_detail_request_params
    )
    assert event_detail_request_params.dataset is not None
    assert event_detail_request_params.to_query_params() is not None
