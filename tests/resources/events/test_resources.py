"""Tests for `gfwapiclient.resources.events.resources`."""

from typing import Any, Dict, Final, List, cast

import pytest
import respx

from gfwapiclient.exceptions.validation import (
    RequestBodyValidationError,
    RequestParamsValidationError,
)
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.events.detail.models.request import (
    EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.events.detail.models.response import (
    EventDetailItem,
    EventDetailResult,
)
from gfwapiclient.resources.events.list.models.request import (
    EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.events.list.models.response import (
    EventListItem,
    EventListResult,
)
from gfwapiclient.resources.events.resources import EventResource
from gfwapiclient.resources.events.stats.models.request import (
    EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.events.stats.models.response import (
    EventStatsItem,
    EventStatsResult,
)


event_id: Final[str] = "3ca9b73aee21fbf278a636709e0f8f03"


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_resource_get_all_events_request_success(
    mock_http_client: HTTPClient,
    mock_raw_event_list_request_params: Dict[str, Any],
    mock_raw_event_list_request_body: Dict[str, Any],
    mock_raw_event_list_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventResource` get all events succeeds with a valid response."""
    mock_responsex.post("/events").respond(
        200, json={"entries": [mock_raw_event_list_item, {}]}
    )
    resource = EventResource(http_client=mock_http_client)

    result: EventListResult = await resource.get_all_events(
        **{**mock_raw_event_list_request_body, **mock_raw_event_list_request_params}
    )
    data: List[EventListItem] = cast(List[EventListItem], result.data())
    assert isinstance(result, EventListResult)
    assert isinstance(data[0], EventListItem)


@pytest.mark.asyncio
async def test_event_resource_get_all_events_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
    mock_raw_event_list_request_body: Dict[str, Any],
) -> None:
    """Test `EventResource` get all events raises `RequestParamsValidationError` with invalid parameters."""
    resource = EventResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_all_events(
            datasets=mock_raw_event_list_request_body["datasets"], limit=-1
        )


@pytest.mark.asyncio
async def test_event_resource_get_all_events_request_body_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `EventResource` get all events raises `RequestBodyValidationError` with invalid bodies."""
    resource = EventResource(http_client=mock_http_client)

    with pytest.raises(
        RequestBodyValidationError,
        match=EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_all_events(datasets=["INVALID_DATASET"])


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_resource_get_event_by_id_request_success(
    mock_http_client: HTTPClient,
    mock_raw_event_detail_request_params: Dict[str, Any],
    mock_raw_event_detail_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventResource` get event by ID succeeds with a valid response."""
    mock_responsex.get(f"/events/{event_id}").respond(
        200, json=mock_raw_event_detail_item
    )
    resource = EventResource(http_client=mock_http_client)

    result: EventDetailResult = await resource.get_event_by_id(
        id=event_id,
        dataset=mock_raw_event_detail_request_params["dataset"],
    )
    data = cast(EventDetailItem, result.data())
    assert isinstance(result, EventDetailResult)
    assert isinstance(data, EventDetailItem)


@pytest.mark.asyncio
async def test_event_resource_get_event_by_id_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `EventResource` get event by ID raises `RequestParamsValidationError` with invalid parameters."""
    resource = EventResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_event_by_id(id=event_id, dataset="INVALID_DATASET")


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_resource_get_events_stats_request_success(
    mock_http_client: HTTPClient,
    mock_raw_event_stats_request_body: Dict[str, Any],
    mock_raw_event_stats_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventResource` get events stats succeeds with a valid response."""
    mock_responsex.post("/events/stats").respond(200, json=mock_raw_event_stats_item)
    resource = EventResource(http_client=mock_http_client)

    result: EventStatsResult = await resource.get_events_stats(
        **mock_raw_event_stats_request_body
    )
    data = cast(EventStatsItem, result.data())
    assert isinstance(result, EventStatsResult)
    assert isinstance(data, EventStatsItem)


@pytest.mark.asyncio
async def test_event_resource_get_events_stats_request_body_validation_error_raises(
    mock_http_client: HTTPClient,
    mock_raw_event_stats_request_body: Dict[str, Any],
) -> None:
    """Test `EventResource` get events stats raises `RequestBodyValidationError` with invalid bodies."""
    resource = EventResource(http_client=mock_http_client)

    with pytest.raises(
        RequestBodyValidationError,
        match=EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_events_stats(
            timeseries_interval=mock_raw_event_stats_request_body[
                "timeseries_interval"
            ],
            datasets=["INVALID_DATASET"],
        )
