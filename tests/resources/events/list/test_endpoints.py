"""Tests for `gfwapiclient.resources.events.list.endpoints`."""

from typing import Any, Dict, List, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.exceptions.validation import ResultValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.events.list.endpoints import EventListEndPoint
from gfwapiclient.resources.events.list.models.request import (
    EventListBody,
    EventListParams,
)
from gfwapiclient.resources.events.list.models.response import (
    EventListItem,
    EventListResult,
)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_list_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_event_list_request_params: Dict[str, Any],
    mock_raw_event_list_request_body: Dict[str, Any],
    mock_raw_event_list_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventListEndPoint` request succeeds with a valid response."""
    mock_responsex.post("/events").respond(
        200, json={"entries": [mock_raw_event_list_item, {}]}
    )
    request_params: EventListParams = EventListParams(
        **mock_raw_event_list_request_params
    )
    request_body: EventListBody = EventListBody(**mock_raw_event_list_request_body)
    endpoint: EventListEndPoint = EventListEndPoint(
        request_params=request_params,
        request_body=request_body,
        http_client=mock_http_client,
    )
    result: EventListResult = await endpoint.request()
    data: List[EventListItem] = cast(List[EventListItem], result.data())
    assert isinstance(result, EventListResult)
    assert isinstance(data[0], EventListItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_list_endpoint_invalid_response_body_failure(
    mock_http_client: HTTPClient,
    mock_raw_event_list_request_params: Dict[str, Any],
    mock_raw_event_list_request_body: Dict[str, Any],
    mock_raw_event_list_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventListEndPoint` request fails with an invalid response body."""
    mock_responsex.post("/events").respond(200, json=[mock_raw_event_list_item])
    request_params: EventListParams = EventListParams(
        **mock_raw_event_list_request_params
    )
    request_body: EventListBody = EventListBody(**mock_raw_event_list_request_body)
    endpoint: EventListEndPoint = EventListEndPoint(
        request_params=request_params,
        request_body=request_body,
        http_client=mock_http_client,
    )
    with pytest.raises(ResultValidationError):
        await endpoint.request()


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_list_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_raw_event_list_request_params: Dict[str, Any],
    mock_raw_event_list_request_body: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventListEndPoint` request fails with an invalid response."""
    mock_responsex.post("/events").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    request_params: EventListParams = EventListParams(
        **mock_raw_event_list_request_params
    )
    request_body: EventListBody = EventListBody(**mock_raw_event_list_request_body)
    endpoint: EventListEndPoint = EventListEndPoint(
        request_params=request_params,
        request_body=request_body,
        http_client=mock_http_client,
    )
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
