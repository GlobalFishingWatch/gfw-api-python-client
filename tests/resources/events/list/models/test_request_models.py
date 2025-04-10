"""Tests for `gfwapiclient.resources.events.list.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.events.list.models.request import (
    EventListBody,
    EventListParams,
)


def test_event_list_request_params_serializes_all_fields(
    mock_raw_event_list_request_params: Dict[str, Any],
) -> None:
    """Test that `EventListParams` serializes all fields correctly."""
    event_list_request_params: EventListParams = EventListParams(
        **mock_raw_event_list_request_params
    )
    assert event_list_request_params.offset is not None
    assert event_list_request_params.limit is not None
    assert event_list_request_params.sort is not None
    assert event_list_request_params.to_query_params() is not None


def test_event_list_request_body_serializes_all_fields(
    mock_raw_event_list_request_body: Dict[str, Any],
) -> None:
    """Test that `EventListBody` serializes all fields correctly."""
    event_list_request_body: EventListBody = EventListBody(
        **mock_raw_event_list_request_body
    )
    assert event_list_request_body.datasets is not None
    assert event_list_request_body.vessels is not None
    assert event_list_request_body.types is not None
    assert event_list_request_body.start_date is not None
    assert event_list_request_body.end_date is not None
    assert event_list_request_body.confidences is not None
    assert event_list_request_body.encounter_types is not None
    assert event_list_request_body.geometry is not None
    assert event_list_request_body.region is not None
    assert event_list_request_body.vessel_types is not None
    assert event_list_request_body.vessel_groups is not None
    assert event_list_request_body.flags is not None
    assert event_list_request_body.duration is not None
    assert event_list_request_body.gap_intentional_disabling is not None
    assert event_list_request_body.to_json_body() is not None
