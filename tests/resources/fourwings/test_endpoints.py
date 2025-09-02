"""Tests for `gfwapiclient.resources.fourwings.report.endpoints`."""

from typing import Any, Dict, List, cast

import httpx
import pytest
import respx

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.exceptions.validation import ResultValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.fourwings.report.endpoints import FourWingsReportEndPoint
from gfwapiclient.resources.fourwings.report.models.request import (
    FourWingsReportBody,
    FourWingsReportParams,
)
from gfwapiclient.resources.fourwings.report.models.response import (
    FourWingsReportItem,
    FourWingsReportResult,
)


@pytest.mark.asyncio
@pytest.mark.respx
async def test_fourwings_report_endpoint_request_success(
    mock_http_client: HTTPClient,
    mock_raw_fourwings_report_request_params: Dict[str, Any],
    mock_raw_fourwings_report_request_body: Dict[str, Any],
    mock_raw_fourwings_report_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `FourWingsReportEndPoint` request succeeds with valid response."""
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
    request_params: FourWingsReportParams = FourWingsReportParams(
        **mock_raw_fourwings_report_request_params
    )
    request_body: FourWingsReportBody = FourWingsReportBody(
        **mock_raw_fourwings_report_request_body
    )
    endpoint: FourWingsReportEndPoint = FourWingsReportEndPoint(
        request_params=request_params,
        request_body=request_body,
        http_client=mock_http_client,
    )
    result: FourWingsReportResult = await endpoint.request()
    data: List[FourWingsReportItem] = cast(List[FourWingsReportItem], result.data())
    assert isinstance(result, FourWingsReportResult)
    assert isinstance(data[0], FourWingsReportItem)


@pytest.mark.asyncio
@pytest.mark.respx
@pytest.mark.parametrize(
    "mock_invalid_response_body",
    [
        None,  # Not a dict
        [],  # Not a dict
        {},  # Missing 'entries'
    ],
)
async def test_fourwings_report_endpoint_request_invalid_response_body_failure(
    mock_invalid_response_body: Any,
    mock_http_client: HTTPClient,
    mock_raw_fourwings_report_request_params: Dict[str, Any],
    mock_raw_fourwings_report_request_body: Dict[str, Any],
    mock_raw_fourwings_report_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `FourWingsReportEndPoint` request fails with invalid response body."""
    mock_responsex.post("4wings/report").respond(200, json=mock_invalid_response_body)
    request_params: FourWingsReportParams = FourWingsReportParams(
        **mock_raw_fourwings_report_request_params
    )
    request_body: FourWingsReportBody = FourWingsReportBody(
        **mock_raw_fourwings_report_request_body
    )
    endpoint: FourWingsReportEndPoint = FourWingsReportEndPoint(
        request_params=request_params,
        request_body=request_body,
        http_client=mock_http_client,
    )
    with pytest.raises(ResultValidationError):
        await endpoint.request()


@pytest.mark.asyncio
@pytest.mark.respx
@pytest.mark.parametrize(
    "mock_invalid_response_body",
    [
        {"entries": []},  # Empty entries list
        {"entries": [{}, None]},  # Non-dict entries in the list
        {
            "entries": [{"public-global-vessel-identity:v3.0": None}]
        },  # Dataset value is not a list
        {
            "entries": [{"public-global-vessel-identity:v3.0": [None]}]
        },  # Dataset item is not a dict
    ],
)
async def test_fourwings_report_endpoint_request_invalid_response_body_entries_ignores(
    mock_invalid_response_body: Any,
    mock_http_client: HTTPClient,
    mock_raw_fourwings_report_request_params: Dict[str, Any],
    mock_raw_fourwings_report_request_body: Dict[str, Any],
    mock_raw_fourwings_report_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `FourWingsReportEndPoint` request ignores invalid response body entries."""
    mock_responsex.post("4wings/report").respond(200, json=mock_invalid_response_body)
    request_params: FourWingsReportParams = FourWingsReportParams(
        **mock_raw_fourwings_report_request_params
    )
    request_body: FourWingsReportBody = FourWingsReportBody(
        **mock_raw_fourwings_report_request_body
    )
    endpoint: FourWingsReportEndPoint = FourWingsReportEndPoint(
        request_params=request_params,
        request_body=request_body,
        http_client=mock_http_client,
    )
    result: FourWingsReportResult = await endpoint.request()
    data: List[FourWingsReportItem] = cast(List[FourWingsReportItem], result.data())
    assert isinstance(result, FourWingsReportResult)
    assert len(data) == 0


@pytest.mark.asyncio
@pytest.mark.respx
async def test_fourwings_report_endpoint_request_failure(
    mock_http_client: HTTPClient,
    mock_raw_fourwings_report_request_params: Dict[str, Any],
    mock_raw_fourwings_report_request_body: Dict[str, Any],
    mock_raw_fourwings_report_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `FourWingsReportEndPoint` request fails with invalid response."""
    mock_responsex.post("4wings/report").mock(
        return_value=httpx.Response(status_code=400, json={"error": "Bad Request"})
    )
    request_params: FourWingsReportParams = FourWingsReportParams(
        **mock_raw_fourwings_report_request_params
    )
    request_body: FourWingsReportBody = FourWingsReportBody(
        **mock_raw_fourwings_report_request_body
    )
    endpoint: FourWingsReportEndPoint = FourWingsReportEndPoint(
        request_params=request_params,
        request_body=request_body,
        http_client=mock_http_client,
    )
    with pytest.raises(GFWAPIClientError):
        await endpoint.request()
