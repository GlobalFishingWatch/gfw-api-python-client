"""Tests for `gfwapiclient.resources.fourwings.resources`."""

from typing import Any, Dict, List, cast

import pytest
import respx

from gfwapiclient.exceptions.validation import (
    RequestBodyValidationError,
    RequestParamsValidationError,
)
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.fourwings.report.models.request import (
    FOURWINGS_REPORT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    FOURWINGS_REPORT_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.fourwings.report.models.response import (
    FourWingsReportItem,
    FourWingsReportResult,
)
from gfwapiclient.resources.fourwings.resources import FourWingsResource


@pytest.mark.asyncio
@pytest.mark.respx
async def test_fourwings_resource_create_report(
    mock_http_client: HTTPClient,
    mock_raw_fourwings_report_request_params: Dict[str, Any],
    mock_raw_fourwings_report_request_body: Dict[str, Any],
    mock_raw_fourwings_report_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `FourWingsResource` create report succeeds with valid response."""
    mock_responsex.post("4wings/report").respond(
        200,
        json={
            "entries": [
                {
                    mock_raw_fourwings_report_item["report_dataset"]: [
                        mock_raw_fourwings_report_item
                    ]
                }
            ]
        },
    )
    resource: FourWingsResource = FourWingsResource(http_client=mock_http_client)
    result: FourWingsReportResult = await resource.create_report(
        **{
            **mock_raw_fourwings_report_request_params,
            **mock_raw_fourwings_report_request_body,
            **{"start_date": "2021-01-01", "end_date": "2021-01-15"},
        }
    )
    data = cast(List[FourWingsReportItem], result.data())
    assert isinstance(result, FourWingsReportResult)
    assert isinstance(data[0], FourWingsReportItem)


@pytest.mark.asyncio
async def test_fourwings_resource_create_report_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `FourWingsResource` create report raises `RequestParamsValidationError` with invalid parameters."""
    resource = FourWingsResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=FOURWINGS_REPORT_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.create_report(datasets=["INVALID_DATASET"])


@pytest.mark.asyncio
async def test_fourwings_resource_create_report_dates_request_params_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `FourWingsResource` create report raises `RequestParamsValidationError` with invalid dates parameters."""
    resource = FourWingsResource(http_client=mock_http_client)

    with pytest.raises(
        RequestParamsValidationError,
        match=FOURWINGS_REPORT_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.create_report(start_date="INVALID_DATE", end_date="INVALID_DATE")


@pytest.mark.asyncio
async def test_fourwings_resource_create_report_request_body_validation_error_raises(
    mock_http_client: HTTPClient,
) -> None:
    """Test `FourWingsResource` create report raises `RequestBodyValidationError` with invalid parameters."""
    resource = FourWingsResource(http_client=mock_http_client)

    with pytest.raises(
        RequestBodyValidationError,
        match=FOURWINGS_REPORT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.create_report(region={"buffer_unit": "INVALID_BUFFER_UNIT"})
