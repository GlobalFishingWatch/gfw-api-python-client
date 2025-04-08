"""Tests for `gfwapiclient.resources.references.resources`."""

from typing import Any, Dict, List, cast

import pytest
import respx

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.references.regions.models.response import (
    EEZRegionItem,
    EEZRegionResult,
    MPARegionItem,
    MPARegionResult,
    RFMORegionItem,
    RFMORegionResult,
)
from gfwapiclient.resources.references.resources import ReferenceResource


@pytest.mark.asyncio
@pytest.mark.respx
async def test_reference_resource_get_eez_regions_success(
    mock_http_client: HTTPClient,
    mock_raw_eez_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `ReferenceResource` get eez regions succeeds with valid response."""
    mock_responsex.get("/datasets/public-eez-areas/context-layers").respond(
        200, json=[mock_raw_eez_region_item]
    )
    resource = ReferenceResource(http_client=mock_http_client)
    result = await resource.get_eez_regions()
    data = cast(List[EEZRegionItem], result.data())
    assert isinstance(result, EEZRegionResult)
    assert len(data) == 1
    assert isinstance(data[0], EEZRegionItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_reference_resource_get_mpa_regions_success(
    mock_http_client: HTTPClient,
    mock_raw_mpa_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `ReferenceResource` get mpa regions succeeds with valid response."""
    mock_responsex.get("/datasets/public-mpa-all/context-layers").respond(
        200, json=[mock_raw_mpa_region_item]
    )
    resource = ReferenceResource(http_client=mock_http_client)
    result = await resource.get_mpa_regions()
    data = cast(List[MPARegionItem], result.data())
    assert isinstance(result, MPARegionResult)
    assert len(data) == 1
    assert isinstance(data[0], MPARegionItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_reference_resource_get_rfmo_regions_success(
    mock_http_client: HTTPClient,
    mock_raw_rfmo_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `ReferenceResource` get rfmo regions succeeds with valid response."""
    mock_responsex.get("/datasets/public-rfmo/context-layers").respond(
        200, json=[mock_raw_rfmo_region_item]
    )
    resource = ReferenceResource(http_client=mock_http_client)
    result = await resource.get_rfmo_regions()
    data = cast(List[RFMORegionItem], result.data())
    assert isinstance(result, RFMORegionResult)
    assert len(data) == 1
    assert isinstance(data[0], RFMORegionItem)
