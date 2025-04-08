"""Tests for `gfwapiclient.resources.events.stats.endpoints`."""

from typing import Any, Dict, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.events.stats.endpoints import EventStatsEndPoint
from gfwapiclient.resources.events.stats.models.request import EventStatsBody
from gfwapiclient.resources.events.stats.models.response import (
    EventStatsItem,
    EventStatsResult,
)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_stats_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_event_stats_request_body: Dict[str, Any],
    mock_raw_event_stats_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventStatsEndPoint` request succeeds with a valid response."""
    mock_responsex.post("/events/stats").respond(200, json=mock_raw_event_stats_item)
    request_body: EventStatsBody = EventStatsBody(**mock_raw_event_stats_request_body)
    endpoint: EventStatsEndPoint = EventStatsEndPoint(
        request_body=request_body,
        http_client=mock_http_client,
    )
    result: EventStatsResult = await endpoint.request()
    data = cast(EventStatsItem, result.data())
    assert isinstance(result, EventStatsResult)
    assert isinstance(data, EventStatsItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_event_stats_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_raw_event_stats_request_body: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EventStatsEndPoint` request fails with an invalid response."""
    mock_responsex.post("/events/stats").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    request_body: EventStatsBody = EventStatsBody(**mock_raw_event_stats_request_body)
    endpoint: EventStatsEndPoint = EventStatsEndPoint(
        request_body=request_body,
        http_client=mock_http_client,
    )
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
