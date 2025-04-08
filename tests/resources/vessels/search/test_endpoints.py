"""Tests for `gfwapiclient.resources.vessels.search.endpoints`."""

from typing import Any, Dict, List, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.exceptions.validation import ResultValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.vessels.search.endpoints import VesselSearchEndPoint
from gfwapiclient.resources.vessels.search.models.request import VesselSearchParams
from gfwapiclient.resources.vessels.search.models.response import (
    VesselSearchItem,
    VesselSearchResult,
)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_search_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_vessel_search_request_params: Dict[str, Any],
    mock_raw_vessel_search_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselSearchEndPoint` request succeeds with a valid response."""
    mock_responsex.get("/vessels/search").respond(
        200, json={"entries": [mock_raw_vessel_search_item, {}]}
    )
    request_params: VesselSearchParams = VesselSearchParams(
        **mock_raw_vessel_search_request_params
    )
    endpoint: VesselSearchEndPoint = VesselSearchEndPoint(
        request_params=request_params,
        http_client=mock_http_client,
    )
    result: VesselSearchResult = await endpoint.request()
    data = cast(List[VesselSearchItem], result.data())
    assert isinstance(result, VesselSearchResult)
    assert isinstance(data[0], VesselSearchItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_search_endpoint_request_invalid_response_body_failure(
    mock_http_client: HTTPClient,
    mock_raw_vessel_search_request_params: Dict[str, Any],
    mock_raw_vessel_search_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselSearchEndPoint` request fails with an invalid response body."""
    mock_responsex.get("/vessels/search").respond(
        200, json=[mock_raw_vessel_search_item]
    )
    request_params: VesselSearchParams = VesselSearchParams(
        **mock_raw_vessel_search_request_params
    )
    endpoint: VesselSearchEndPoint = VesselSearchEndPoint(
        request_params=request_params,
        http_client=mock_http_client,
    )
    with pytest.raises(ResultValidationError):
        await endpoint.request()


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_search_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_raw_vessel_search_request_params: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselSearchEndPoint` request fails with an invalid response."""
    mock_responsex.get("/vessels/search").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    request_params: VesselSearchParams = VesselSearchParams(
        **mock_raw_vessel_search_request_params
    )
    endpoint: VesselSearchEndPoint = VesselSearchEndPoint(
        request_params=request_params,
        http_client=mock_http_client,
    )
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
