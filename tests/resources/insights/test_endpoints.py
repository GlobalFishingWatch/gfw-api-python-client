"""Tests for `gfwapiclient.resources.insights.endpoints`."""

from typing import Any, Dict, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.insights.endpoints import VesselInsightEndPoint
from gfwapiclient.resources.insights.models.request import VesselInsightBody
from gfwapiclient.resources.insights.models.response import (
    VesselInsightItem,
    VesselInsightResult,
)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_insight_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_vessel_insight_request_body: Dict[str, Any],
    mock_raw_vessel_insight_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselInsightEndPoint` request succeeds with valid response."""
    mock_responsex.post("/insights/vessels").respond(
        200, json=mock_raw_vessel_insight_item
    )
    request_body: VesselInsightBody = VesselInsightBody(
        **mock_raw_vessel_insight_request_body
    )
    endpoint = VesselInsightEndPoint(
        request_body=request_body, http_client=mock_http_client
    )
    result = await endpoint.request()
    data = cast(VesselInsightItem, result.data())
    assert isinstance(result, VesselInsightResult)
    assert isinstance(data, VesselInsightItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_insight_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_raw_vessel_insight_request_body: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselInsightEndPoint` request fails with invalid response."""
    mock_responsex.post("/insights/vessels").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    request_body: VesselInsightBody = VesselInsightBody(
        **mock_raw_vessel_insight_request_body
    )
    endpoint = VesselInsightEndPoint(
        request_body=request_body, http_client=mock_http_client
    )
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
