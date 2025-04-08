"""Test configurations for `gfwapiclient.resources.events`."""

from typing import Any, Callable, Dict

import pytest


@pytest.fixture
def mock_raw_event_detail_request_params(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw event detail request params.

    Returns:
        Dict[str, Any]:
            Raw `EventDetailParams` sample data.
    """
    raw_event_detail_request_params: Dict[str, Any] = load_json_fixture(
        "events/event_detail_request_params.json"
    )
    return raw_event_detail_request_params


@pytest.fixture
def mock_raw_event_list_request_params(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw event list request params.

    Returns:
        Dict[str, Any]:
            Raw `EventListParams` sample data.
    """
    raw_event_list_request_params: Dict[str, Any] = load_json_fixture(
        "events/event_list_request_params.json"
    )
    return raw_event_list_request_params


@pytest.fixture
def mock_raw_event_list_request_body(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw event list request body.

    Returns:
        Dict[str, Any]:
            Raw `EventListBody` sample data.
    """
    raw_event_list_request_body: Dict[str, Any] = load_json_fixture(
        "events/event_list_request_body.json"
    )
    return raw_event_list_request_body


@pytest.fixture
def mock_raw_event_stats_request_body(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw event stats request body.

    Returns:
        Dict[str, Any]:
            Raw `EventStatsEndPoint` sample data.
    """
    raw_event_stats_request_body: Dict[str, Any] = load_json_fixture(
        "events/event_stats_request_body.json"
    )
    return raw_event_stats_request_body


@pytest.fixture
def mock_raw_event_detail_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw event detail item.

    Returns:
        Dict[str, Any]:
            Raw `EventDetailItem` sample data.
    """
    raw_event_detail_item: Dict[str, Any] = load_json_fixture("events/event_item.json")
    return raw_event_detail_item


@pytest.fixture
def mock_raw_event_list_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw event list item.

    Returns:
        Dict[str, Any]:
            Raw `EventListItem` sample data.
    """
    raw_event_list_item: Dict[str, Any] = load_json_fixture("events/event_item.json")
    return raw_event_list_item


@pytest.fixture
def mock_raw_event_stats_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw event stats item.

    Returns:
        Dict[str, Any]:
            Raw `EventStatsItem` sample data.
    """
    raw_event_stats_item: Dict[str, Any] = load_json_fixture(
        "events/event_stats_item.json"
    )
    return raw_event_stats_item
