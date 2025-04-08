"""Tests for `gfwapiclient.resources.vessels.resources`."""

from typing import Any, Dict, Final, List, cast

import pytest
import respx

from gfwapiclient.exceptions.validation import RequestParamsValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.vessels.detail.models.request import (
    VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.vessels.detail.models.response import (
    VesselDetailItem,
    VesselDetailResult,
)
from gfwapiclient.resources.vessels.list.models.request import (
    VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.vessels.list.models.response import (
    VesselListItem,
    VesselListResult,
)
from gfwapiclient.resources.vessels.resources import VesselResource
from gfwapiclient.resources.vessels.search.models.request import (
    VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.vessels.search.models.response import (
    VesselSearchItem,
    VesselSearchResult,
)


vessel_id: Final[str] = "c54923e64-46f3-9338-9dcb-ff09724077a3"


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_resource_search_vessels_request_success(
    mock_http_client: HTTPClient,
    mock_raw_vessel_search_request_params: Dict[str, Any],
    mock_raw_vessel_search_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselResource` search vessels succeeds with a valid response."""
    mock_responsex.get("/vessels/search").respond(
        200, json={"entries": [mock_raw_vessel_search_item]}
    )
    resource = VesselResource(http_client=mock_http_client)
    result: VesselSearchResult = await resource.search_vessels(
        **mock_raw_vessel_search_request_params
    )
    data = cast(List[VesselSearchItem], result.data())
    assert isinstance(result, VesselSearchResult)
    assert isinstance(data[0], VesselSearchItem)


@pytest.mark.asyncio
async def test_vessel_resource_search_vessels_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `VesselResource` search vessels raises `RequestParamsValidationError` with invalid parameters."""
    resource = VesselResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.search_vessels(datasets=["INVALID_DATASET"])


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_resource_get_vessels_by_ids_request_success(
    mock_http_client: HTTPClient,
    mock_raw_vessel_list_request_params: Dict[str, Any],
    mock_raw_vessel_list_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselResource` get vessels by IDs succeeds with a valid response."""
    mock_responsex.get("/vessels").respond(
        200, json={"entries": [mock_raw_vessel_list_item]}
    )
    resource = VesselResource(http_client=mock_http_client)
    result: VesselListResult = await resource.get_vessels_by_ids(
        **mock_raw_vessel_list_request_params
    )
    data = cast(List[VesselListItem], result.data())
    assert isinstance(result, VesselListResult)
    assert isinstance(data[0], VesselListItem)


@pytest.mark.asyncio
async def test_vessel_resource_get_vessels_by_ids_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `VesselResource` get vessels by IDs raises `RequestParamsValidationError` with invalid parameters."""
    resource = VesselResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_vessels_by_ids(ids=[vessel_id], datasets=["INVALID_DATASET"])


@pytest.mark.asyncio
@pytest.mark.respx
async def test_vessel_resource_get_vessel_by_id_request_success(
    mock_http_client: HTTPClient,
    mock_raw_vessel_detail_request_params: Dict[str, Any],
    mock_raw_vessel_detail_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `VesselResource` get vessel by ID succeeds with a valid response."""
    mock_responsex.get(f"/vessels/{vessel_id}").respond(
        200, json=mock_raw_vessel_detail_item
    )
    resource = VesselResource(http_client=mock_http_client)

    result: VesselDetailResult = await resource.get_vessel_by_id(
        id=vessel_id,
        **mock_raw_vessel_detail_request_params,
    )
    data = cast(VesselDetailItem, result.data())
    assert isinstance(result, VesselDetailResult)
    assert isinstance(data, VesselDetailItem)


@pytest.mark.asyncio
async def test_vessel_resource_get_vessel_by_id_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `VesselResource` get vessel by ID raises `RequestParamsValidationError` with invalid parameters."""
    resource = VesselResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_vessel_by_id(id=vessel_id, dataset="INVALID_DATASET")
