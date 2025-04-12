"""Tests for `gfwapiclient.resources.datasets.endpoints`."""

from typing import List, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.datasets.endpoints import SARFixedInfrastructureEndPoint
from gfwapiclient.resources.datasets.models.response import (
    SARFixedInfrastructureItem,
    SARFixedInfrastructureResult,
)

from .conftest import x, y, z


@pytest.mark.asyncio
@pytest.mark.respx
async def test_sar_fixed_infrastructure_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_sar_fixed_infrastructure_mvt: bytes,
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `SARFixedInfrastructureEndPoint` request succeeds with valid response."""
    mock_responsex.get(
        f"datasets/public-fixed-infrastructure-filtered:latest/context-layers/{z}/{x}/{y}"
    ).respond(
        200,
        content=mock_raw_sar_fixed_infrastructure_mvt,
        headers={"Content-Type": "application/vnd.mapbox-vector-tile"},
    )

    endpoint: SARFixedInfrastructureEndPoint = SARFixedInfrastructureEndPoint(
        z=z, x=x, y=y, http_client=mock_http_client
    )

    result: SARFixedInfrastructureResult = await endpoint.request()
    data: List[SARFixedInfrastructureItem] = cast(
        List[SARFixedInfrastructureItem], result.data()
    )
    assert isinstance(result, SARFixedInfrastructureResult)
    assert isinstance(data[0], SARFixedInfrastructureItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_sar_fixed_infrastructure_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `SARFixedInfrastructureEndPoint` request fails with invalid response."""
    mock_responsex.get(
        f"datasets/public-fixed-infrastructure-filtered:latest/context-layers/{z}/{x}/{y}"
    ).mock(return_value=httpx.Response(status_code=400, json={"error": "Bad Request"}))

    endpoint: SARFixedInfrastructureEndPoint = SARFixedInfrastructureEndPoint(
        z=z, x=x, y=y, http_client=mock_http_client
    )

    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
