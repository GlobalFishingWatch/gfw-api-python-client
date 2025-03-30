"""Tests for `gfwapiclient.resources.references.regions.endpoints`."""

from typing import Any, Dict, List, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.references.regions.endpoints import (
    EEZRegionEndPoint,
    MPARegionEndPoint,
    RFMORegionEndPoint,
)
from gfwapiclient.resources.references.regions.models.response import (
    EEZRegionItem,
    EEZRegionResult,
    MPARegionItem,
    MPARegionResult,
    RFMORegionItem,
    RFMORegionResult,
)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_eez_region_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_eez_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EEZRegionEndPoint` request succeeds with valid response."""
    mock_responsex.get("/datasets/public-eez-areas/context-layers").respond(
        200, json=[mock_raw_eez_region_item]
    )
    endpoint = EEZRegionEndPoint(http_client=mock_http_client)
    result = await endpoint.request()
    data = cast(List[EEZRegionItem], result.data())
    assert isinstance(result, EEZRegionResult)
    assert len(data) == 1
    assert isinstance(data[0], EEZRegionItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_eez_region_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `EEZRegionEndPoint` request fails with invalid response."""
    mock_responsex.get("/datasets/public-eez-areas/context-layers").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    endpoint = EEZRegionEndPoint(http_client=mock_http_client)
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()


@pytest.mark.asyncio
@pytest.mark.respx
async def test_mpa_region_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_mpa_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `MPARegionEndPoint` request succeeds with valid response."""
    mock_responsex.get("/datasets/public-mpa-all/context-layers").respond(
        200, json=[mock_raw_mpa_region_item]
    )
    endpoint = MPARegionEndPoint(http_client=mock_http_client)
    result = await endpoint.request()
    data = cast(List[MPARegionItem], result.data())
    assert isinstance(result, MPARegionResult)
    assert len(data) == 1
    assert isinstance(data[0], MPARegionItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_mpa_region_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `MPARegionEndPoint` request fails with invalid response."""
    mock_responsex.get("/datasets/public-mpa-all/context-layers").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    endpoint = MPARegionEndPoint(http_client=mock_http_client)
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()


@pytest.mark.asyncio
@pytest.mark.respx
async def test_rfmo_region_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_rfmo_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `RFMORegionEndPoint` request succeeds with valid response."""
    mock_responsex.get("/datasets/public-rfmo/context-layers").respond(
        200, json=[mock_raw_rfmo_region_item]
    )
    endpoint = RFMORegionEndPoint(http_client=mock_http_client)
    result = await endpoint.request()
    data = cast(List[RFMORegionItem], result.data())
    assert isinstance(result, RFMORegionResult)
    assert len(data) == 1
    assert isinstance(data[0], RFMORegionItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_rfmo_region_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `RFMORegionEndPoint` request fails with invalid response."""
    mock_responsex.get("/datasets/public-rfmo/context-layers").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    endpoint = RFMORegionEndPoint(http_client=mock_http_client)
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
