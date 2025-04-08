"""Tests for `gfwapiclient.resources.vessels.list.endpoints`."""

from typing import Any, Dict, List, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.exceptions.validation import ResultValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.vessels.list.endpoints import VesselListEndPoint
from gfwapiclient.resources.vessels.list.models.request import VesselListParams
from gfwapiclient.resources.vessels.list.models.response import (
    VesselListItem,
    VesselListResult,
)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_list_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_vessel_list_request_params: Dict[str, Any],
    mock_raw_vessel_list_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselListEndPoint` request succeeds with a valid response."""
    mock_responsex.get("/vessels").respond(
        200,
        json={"entries": [mock_raw_vessel_list_item, {}]},
    )
    request_params: VesselListParams = VesselListParams(
        **mock_raw_vessel_list_request_params
    )
    endpoint: VesselListEndPoint = VesselListEndPoint(
        request_params=request_params,
        http_client=mock_http_client,
    )
    result: VesselListResult = await endpoint.request()
    data = cast(List[VesselListItem], result.data())
    assert isinstance(result, VesselListResult)
    assert isinstance(data[0], VesselListItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_list_endpoint_request_invalid_response_body_failure(
    mock_http_client: HTTPClient,
    mock_raw_vessel_list_request_params: Dict[str, Any],
    mock_raw_vessel_list_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselListEndPoint` request fails with an invalid response body."""
    mock_responsex.get("/vessels").respond(200, json=[mock_raw_vessel_list_item])
    request_params: VesselListParams = VesselListParams(
        **mock_raw_vessel_list_request_params
    )
    endpoint: VesselListEndPoint = VesselListEndPoint(
        request_params=request_params,
        http_client=mock_http_client,
    )
    with pytest.raises(ResultValidationError):
        await endpoint.request()


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_list_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_raw_vessel_list_request_params: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselListEndPoint` request fails with an invalid response."""
    mock_responsex.get("/vessels").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    request_params: VesselListParams = VesselListParams(
        **mock_raw_vessel_list_request_params
    )
    endpoint: VesselListEndPoint = VesselListEndPoint(
        request_params=request_params,
        http_client=mock_http_client,
    )
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
