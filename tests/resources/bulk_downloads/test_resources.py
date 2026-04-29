"""Tests for `gfwapiclient.resources.bulk_downloads.resources`."""

from pathlib import Path
from typing import Any, Dict, List, Union, cast

import pytest
import respx

from gfwapiclient.base.models import GeoJson, SupportsGeoJsonInterface
from gfwapiclient.exceptions.validation import (
    RequestBodyValidationError,
    RequestParamsValidationError,
)
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.bulk_downloads.create.models.request import (
    BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.bulk_downloads.create.models.response import (
    BulkReportCreateItem,
    BulkReportCreateResult,
)
from gfwapiclient.resources.bulk_downloads.detail.models.response import (
    BulkReportDetailItem,
    BulkReportDetailResult,
)
from gfwapiclient.resources.bulk_downloads.file.models.request import (
    BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.bulk_downloads.file.models.response import (
    BulkReportFileItem,
    BulkReportFileResult,
)
from gfwapiclient.resources.bulk_downloads.list.models.request import (
    BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.bulk_downloads.list.models.response import (
    BulkReportListItem,
    BulkReportListResult,
)
from gfwapiclient.resources.bulk_downloads.query.models.base.request import (
    BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response import (
    BulkFixedInfrastructureDataQueryItem,
    BulkFixedInfrastructureDataQueryResult,
)
from gfwapiclient.resources.bulk_downloads.resources import BulkDownloadResource

from .conftest import bulk_report_id


@pytest.mark.asyncio
@pytest.mark.respx
async def test_bulk_download_resource_create_bulk_report_request_success(
    mock_http_client: HTTPClient,
    mock_raw_bulk_report_create_request_body: Dict[str, Any],
    mock_raw_bulk_report_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `BulkDownloadResource`create bulk report succeeds with a valid response."""
    mock_responsex.post("/bulk-reports").respond(201, json=mock_raw_bulk_report_item)
    resource = BulkDownloadResource(http_client=mock_http_client)

    result: BulkReportCreateResult = await resource.create_bulk_report(
        **mock_raw_bulk_report_create_request_body
    )
    data = cast(BulkReportCreateItem, result.data())
    assert isinstance(result, BulkReportCreateResult)
    assert isinstance(data, BulkReportCreateItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_bulk_download_resource_create_bulk_report_geojson_request_body_success(
    mock_http_client: HTTPClient,
    mock_raw_bulk_report_create_request_body: Dict[str, Any],
    mock_raw_bulk_report_item: Dict[str, Any],
    mock_geojson_source_instances: List[
        Union[GeoJson, str, Path, Dict[str, Any], SupportsGeoJsonInterface]
    ],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `BulkDownloadResource`create bulk report succeeds with valid geojson request bodies."""
    mock_responsex.post("/bulk-reports").respond(201, json=mock_raw_bulk_report_item)
    resource = BulkDownloadResource(http_client=mock_http_client)

    for geojson_source_instance in [*mock_geojson_source_instances, None]:
        result: BulkReportCreateResult = await resource.create_bulk_report(
            **{
                **mock_raw_bulk_report_create_request_body,
                "geojson": geojson_source_instance,
            },  # geojson source
        )

        data = cast(BulkReportCreateItem, result.data())
        assert isinstance(result, BulkReportCreateResult)
        assert isinstance(data, BulkReportCreateItem)


@pytest.mark.asyncio
async def test_bulk_download_resource_create_bulk_report_request_body_validation_error_raises(
    mock_http_client: HTTPClient,
    mock_raw_bulk_report_create_request_body: Dict[str, Any],
) -> None:
    """Test `BulkDownloadResource`create bulk report raises `RequestBodyValidationError` with invalid bodies."""
    resource = BulkDownloadResource(http_client=mock_http_client)

    with pytest.raises(
        RequestBodyValidationError,
        match=BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.create_bulk_report(
            **{
                **mock_raw_bulk_report_create_request_body,
                "dataset": "INVALID_DATASET",
            }
        )


@pytest.mark.asyncio
@pytest.mark.respx
async def test_bulk_download_resource_get_bulk_report_by_id_request_success(
    mock_http_client: HTTPClient,
    mock_raw_bulk_report_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `BulkDownloadResource` get bulk report by ID succeeds with a valid response."""
    mock_responsex.get(f"/bulk-reports/{bulk_report_id}").respond(
        200, json=mock_raw_bulk_report_item
    )
    resource = BulkDownloadResource(http_client=mock_http_client)

    result: BulkReportDetailResult = await resource.get_bulk_report_by_id(
        id=bulk_report_id,
    )
    data = cast(BulkReportDetailItem, result.data())
    assert isinstance(result, BulkReportDetailResult)
    assert isinstance(data, BulkReportDetailItem)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_bulk_download_resource_get_all_bulk_reports_request_success(
    mock_http_client: HTTPClient,
    mock_raw_bulk_report_list_request_params: Dict[str, Any],
    mock_raw_bulk_report_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `BulkDownloadResource` get all bulk reports succeeds with a valid response."""
    mock_responsex.get("/bulk-reports").respond(
        200, json={"entries": [mock_raw_bulk_report_item, {}]}
    )
    resource = BulkDownloadResource(http_client=mock_http_client)
    result: BulkReportListResult = await resource.get_all_bulk_reports(
        **mock_raw_bulk_report_list_request_params
    )
    data = cast(List[BulkReportListItem], result.data())
    assert isinstance(result, BulkReportListResult)
    assert isinstance(data[0], BulkReportListItem)


@pytest.mark.asyncio
async def test_bulk_download_resource_get_all_bulk_reports_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `BulkDownloadResource` get all bulk reports raises `RequestParamsValidationError` with invalid parameters."""
    resource = BulkDownloadResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_all_bulk_reports(limit=-1, offset=-1)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_bulk_download_resource_get_bulk_report_file_download_url_request_success(
    mock_http_client: HTTPClient,
    mock_raw_bulk_report_file_request_params: Dict[str, Any],
    mock_raw_bulk_report_file_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `BulkDownloadResource` get bulk report file download url succeeds with a valid response."""
    mock_responsex.get(f"bulk-reports/{bulk_report_id}/download-file-url").respond(
        200, json=mock_raw_bulk_report_file_item
    )
    resource = BulkDownloadResource(http_client=mock_http_client)
    result: BulkReportFileResult = await resource.get_bulk_report_file_download_url(
        **{
            **mock_raw_bulk_report_file_request_params,
            "id": bulk_report_id,
        }
    )
    data = cast(BulkReportFileItem, result.data())
    assert isinstance(result, BulkReportFileResult)
    assert isinstance(data, BulkReportFileItem)


@pytest.mark.asyncio
async def test_bulk_download_resource_get_bulk_report_file_download_url_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `BulkDownloadResource` get bulk report file download url raises `RequestParamsValidationError` with invalid parameters."""
    resource = BulkDownloadResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_bulk_report_file_download_url(
            id=bulk_report_id, file="INVALID_FILE_TYPE"
        )


@pytest.mark.asyncio
@pytest.mark.respx
async def test_bulk_download_resource_query_bulk_fixed_infrastructure_data_report_request_success(
    mock_http_client: HTTPClient,
    mock_raw_bulk_report_query_request_params: Dict[str, Any],
    mock_raw_bulk_fixed_infrastructure_data_query_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `BulkDownloadResource` query bulk fixed infrastructure data report succeeds with a valid response."""
    mock_responsex.get(f"bulk-reports/{bulk_report_id}/query").respond(
        200, json={"entries": [mock_raw_bulk_fixed_infrastructure_data_query_item, {}]}
    )
    resource = BulkDownloadResource(http_client=mock_http_client)
    result: BulkFixedInfrastructureDataQueryResult = (
        await resource.query_bulk_fixed_infrastructure_data_report(
            **{
                **mock_raw_bulk_report_query_request_params,
                "id": bulk_report_id,
            }
        )
    )
    data = cast(List[BulkFixedInfrastructureDataQueryItem], result.data())
    assert isinstance(result, BulkFixedInfrastructureDataQueryResult)
    assert isinstance(data[0], BulkFixedInfrastructureDataQueryItem)


@pytest.mark.asyncio
async def test_bulk_download_resource_query_bulk_fixed_infrastructure_data_report_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `BulkDownloadResource` query bulk fixed infrastructure data report raises `RequestParamsValidationError` with invalid parameters."""
    resource = BulkDownloadResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.query_bulk_fixed_infrastructure_data_report(
            id=bulk_report_id, limit=-1, offset=-1
        )
