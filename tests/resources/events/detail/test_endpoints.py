"""Tests for `gfwapiclient.resources.events.detail.endpoints`."""

from typing import Any, Dict, Final, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.events.detail.endpoints import EventDetailEndPoint
from gfwapiclient.resources.events.detail.models.request import EventDetailParams
from gfwapiclient.resources.events.detail.models.response import (
    EventDetailItem,
    EventDetailResult,
)


event_id: Final[str] = "3ca9b73aee21fbf278a636709e0f8f03"


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_detail_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_event_detail_request_params: Dict[str, Any],
    mock_raw_event_detail_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventDetailEndPoint` request succeeds with a valid response."""
    mock_responsex.get(f"/events/{event_id}").respond(
        200, json=mock_raw_event_detail_item
    )
    request_params: EventDetailParams = EventDetailParams(
        **mock_raw_event_detail_request_params
    )
    endpoint: EventDetailEndPoint = EventDetailEndPoint(
        event_id=event_id,
        request_params=request_params,
        http_client=mock_http_client,
    )
    result: EventDetailResult = await endpoint.request()
    data = cast(EventDetailItem, result.data())
    assert isinstance(result, EventDetailResult)
    assert isinstance(data, EventDetailItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_detail_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_raw_event_detail_request_params: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventDetailEndPoint` request fails with an invalid response."""
    mock_responsex.get(f"/events/{event_id}").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    request_params: EventDetailParams = EventDetailParams(
        **mock_raw_event_detail_request_params
    )
    endpoint: EventDetailEndPoint = EventDetailEndPoint(
        event_id=event_id,
        request_params=request_params,
        http_client=mock_http_client,
    )
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
