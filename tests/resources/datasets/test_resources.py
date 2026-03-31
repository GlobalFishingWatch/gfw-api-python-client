"""Tests for `gfwapiclient.resources.datasets.resources`."""

from pathlib import Path
from typing import Any, Dict, List, Union, cast

import pytest
import respx

from gfwapiclient.base.models import GeoJson, SupportsGeoJsonInterface
from gfwapiclient.exceptions.validation import (
    RequestParamsValidationError,
)
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.datasets.models.request import (
    SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.datasets.models.response import (
    SARFixedInfrastructureItem,
    SARFixedInfrastructureResult,
)
from gfwapiclient.resources.datasets.resources import DatasetResource

from .conftest import geometry, url, x, y, z


@pytest.mark.asyncio
@pytest.mark.respx
async def test_dataset_resource_get_sar_fixed_infrastructure_xyz_request_success(
    mock_http_client: HTTPClient,
    mock_raw_sar_fixed_infrastructure_mvt: bytes,
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `DatasetResource` get sar fixed infrastructure with xyz request parameters succeeds with a valid response."""
    mock_responsex.get(url).respond(
        200,
        content=mock_raw_sar_fixed_infrastructure_mvt,
        headers={"Content-Type": "application/vnd.mapbox-vector-tile"},
    )
    resource: DatasetResource = DatasetResource(http_client=mock_http_client)

    result: SARFixedInfrastructureResult = await resource.get_sar_fixed_infrastructure(
        z=z, x=x, y=y
    )
    data: List[SARFixedInfrastructureItem] = cast(
        List[SARFixedInfrastructureItem], result.data()
    )
    assert isinstance(result, SARFixedInfrastructureResult)
    assert isinstance(data[0], SARFixedInfrastructureItem)
    assert data[0].structure_id is not None
    assert data[0].lat is not None
    assert data[0].lon is not None
    assert data[0].label is not None
    assert data[0].label_confidence is not None
    assert data[0].structure_start_date is not None
    assert data[0].structure_end_date is not None


@pytest.mark.asyncio
@pytest.mark.respx
async def test_dataset_resource_get_sar_fixed_infrastructure_geometry_request_success(
    mock_http_client: HTTPClient,
    mock_raw_sar_fixed_infrastructure_mvt: bytes,
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `DatasetResource` get sar fixed infrastructure with geometry request parameters succeeds with a valid response."""
    mock_responsex.get(url).respond(
        200,
        content=mock_raw_sar_fixed_infrastructure_mvt,
        headers={"Content-Type": "application/vnd.mapbox-vector-tile"},
    )
    resource: DatasetResource = DatasetResource(http_client=mock_http_client)

    result: SARFixedInfrastructureResult = await resource.get_sar_fixed_infrastructure(
        geometry=geometry
    )
    data: List[SARFixedInfrastructureItem] = cast(
        List[SARFixedInfrastructureItem], result.data()
    )
    assert isinstance(result, SARFixedInfrastructureResult)
    assert isinstance(data[0], SARFixedInfrastructureItem)
    assert data[0].structure_id is not None
    assert data[0].lat is not None
    assert data[0].lon is not None
    assert data[0].label is not None
    assert data[0].label_confidence is not None
    assert data[0].structure_start_date is not None
    assert data[0].structure_end_date is not None


@pytest.mark.asyncio
@pytest.mark.respx
async def test_dataset_resource_get_sar_fixed_infrastructure_geojson_request_body_success(
    mock_http_client: HTTPClient,
    mock_raw_sar_fixed_infrastructure_mvt: bytes,
    mock_geojson_source_instances: List[
        Union[GeoJson, str, Path, Dict[str, Any], SupportsGeoJsonInterface]
    ],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `DatasetResource` get sar fixed infrastructure with geojson request parameters succeeds with a valid response."""
    mock_responsex.get(url).respond(
        200,
        content=mock_raw_sar_fixed_infrastructure_mvt,
        headers={"Content-Type": "application/vnd.mapbox-vector-tile"},
    )
    resource: DatasetResource = DatasetResource(http_client=mock_http_client)

    for geojson_source_instance in [mock_geojson_source_instances[2]]:
        result: SARFixedInfrastructureResult = (
            await resource.get_sar_fixed_infrastructure(
                geometry=geojson_source_instance
            )
        )
        data: List[SARFixedInfrastructureItem] = cast(
            List[SARFixedInfrastructureItem], result.data()
        )
        assert isinstance(result, SARFixedInfrastructureResult)
        assert isinstance(data[0], SARFixedInfrastructureItem)
        assert data[0].structure_id is not None
        assert data[0].lat is not None
        assert data[0].lon is not None
        assert data[0].label is not None
        assert data[0].label_confidence is not None
        assert data[0].structure_start_date is not None
        assert data[0].structure_end_date is not None


@pytest.mark.asyncio
async def test_dataset_resource_get_sar_fixed_infrastructure_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `DatasetResource` get sar fixed infrastructure raises `RequestParamsValidationError` with invalid parameters."""
    resource = DatasetResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_sar_fixed_infrastructure(z=None)
