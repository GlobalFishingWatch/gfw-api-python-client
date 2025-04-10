"""Tests for `gfwapiclient.resources.vessels.detail.endpoints`."""

from typing import Any, Dict, Final, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.vessels.detail.endpoints import VesselDetailEndPoint
from gfwapiclient.resources.vessels.detail.models.request import VesselDetailParams
from gfwapiclient.resources.vessels.detail.models.response import (
    VesselDetailItem,
    VesselDetailResult,
)


vessel_id: Final[str] = "c54923e64-46f3-9338-9dcb-ff09724077a3"


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_detail_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_vessel_detail_request_params: Dict[str, Any],
    mock_raw_vessel_detail_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselDetailEndPoint` request succeeds with a valid response."""
    mock_responsex.get(f"/vessels/{vessel_id}").respond(
        200, json=mock_raw_vessel_detail_item
    )
    request_params: VesselDetailParams = VesselDetailParams(
        **mock_raw_vessel_detail_request_params
    )
    endpoint: VesselDetailEndPoint = VesselDetailEndPoint(
        vessel_id=vessel_id,
        request_params=request_params,
        http_client=mock_http_client,
    )
    result: VesselDetailResult = await endpoint.request()
    data = cast(VesselDetailItem, result.data())
    assert isinstance(result, VesselDetailResult)
    assert isinstance(data, VesselDetailItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_detail_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_raw_vessel_detail_request_params: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselDetailEndPoint` request fails with an invalid response."""
    mock_responsex.get(f"/vessels/{vessel_id}").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    request_params: VesselDetailParams = VesselDetailParams(
        **mock_raw_vessel_detail_request_params
    )
    endpoint: VesselDetailEndPoint = VesselDetailEndPoint(
        vessel_id=vessel_id,
        request_params=request_params,
        http_client=mock_http_client,
    )
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
