"""Tests for `gfwapiclient.http.endpoints.abc.BaseEndPoint`."""

import http

from typing import Any, Callable, Dict, List, Type, cast

import httpx
import pandas as pd
import pytest
import respx

from gfwapiclient.exceptions.http import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadGatewayError,
    BadRequestError,
    ConflictError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    RequestTimeoutError,
    ServiceUnavailableError,
    UnprocessableEntityError,
)
from gfwapiclient.exceptions.validation import (
    ResultItemValidationError,
    ResultValidationError,
)
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints.base import BaseEndPoint
from tests.http.endpoints.conftest import (
    MockListResult,
    MockRequestBody,
    MockRequestParams,
    MockResultItem,
)


class MockBaseEndPoint(
    BaseEndPoint[MockRequestParams, MockRequestBody, MockResultItem, MockListResult]
):
    """A sample base endpoint for testing `BaseEndPoint` and HTTP endpoints behavior."""

    pass


@pytest.fixture
def mock_base_endpoint(
    mock_http_client: HTTPClient,
    mock_request_params: MockRequestParams,
    mock_request_body: MockRequestBody,
) -> BaseEndPoint[MockRequestParams, MockRequestBody, MockResultItem, MockListResult]:
    """Fixture for mock `BaseEndPoint`.

    Returns:
        A `BaseEndPoint` instance for testing purposes.
    """
    return MockBaseEndPoint(
        method=http.HTTPMethod.POST,
        path="/200",
        request_params=mock_request_params,
        request_body=mock_request_body,
        result_item_class=MockResultItem,
        result_class=MockListResult,
        http_client=mock_http_client,
    )


def test_base_endpoint_get_instance(
    mock_http_client: HTTPClient,
    mock_request_params: MockRequestParams,
) -> None:
    """Test that `BaseEndPoint` can be instantiated as `GET` endpoint."""
    endpoint = MockBaseEndPoint(
        method=http.HTTPMethod.GET,
        path="/200",
        request_params=mock_request_params,
        request_body=None,
        result_item_class=MockResultItem,
        result_class=MockListResult,
        http_client=mock_http_client,
    )

    assert endpoint._method == http.HTTPMethod.GET
    assert endpoint._path == "/200"
    assert endpoint._request_params is not None
    assert isinstance(endpoint._request_params, MockRequestParams)
    assert endpoint._request_params == mock_request_params
    assert endpoint._request_body is None
    assert endpoint._result_item_class == MockResultItem
    assert endpoint._result_class == MockListResult
    assert endpoint._http_client is not None
    assert isinstance(endpoint._http_client, HTTPClient)
    assert endpoint._http_client == mock_http_client


def test_base_endpoint_post_instance(
    mock_http_client: HTTPClient,
    mock_request_params: MockRequestParams,
    mock_request_body: MockRequestBody,
) -> None:
    """Test that `BaseEndPoint` can be instantiated as `POST` endpoint."""
    endpoint = MockBaseEndPoint(
        method=http.HTTPMethod.POST,
        path="/200",
        request_params=mock_request_params,
        request_body=mock_request_body,
        result_item_class=MockResultItem,
        result_class=MockListResult,
        http_client=mock_http_client,
    )

    assert endpoint._method == http.HTTPMethod.POST
    assert endpoint._path == "/200"
    assert endpoint._request_params is not None
    assert isinstance(endpoint._request_params, MockRequestParams)
    assert endpoint._request_params == mock_request_params
    assert endpoint._request_body is not None
    assert isinstance(endpoint._request_body, MockRequestBody)
    assert endpoint._request_body == mock_request_body
    assert endpoint._result_item_class == MockResultItem
    assert endpoint._result_class == MockListResult
    assert endpoint._http_client is not None
    assert isinstance(endpoint._http_client, HTTPClient)
    assert endpoint._http_client == mock_http_client


def test_base_endpoint_parse_response_json_data_success(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_raw_result_item: Dict[str, Any],
) -> None:
    """Test that `BaseEndPoint` can parse response json data successfully."""
    response = httpx.Response(
        status_code=200,
        json=mock_raw_result_item,
        headers={"content-type": "application/json"},
    )
    assert (
        mock_base_endpoint._parse_response_data(response=response)
        == mock_raw_result_item
    )


def test_base_endpoint_parse_response_mvt_data_success(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    load_mvt_fixture: Callable[[str], bytes],
) -> None:
    """Test that `BaseEndPoint` can parse response mvt data successfully."""
    mvt_data: bytes = load_mvt_fixture("datasets/sar_fixed_infrastructure.mvt")
    response = httpx.Response(
        status_code=200,
        content=mvt_data,
        headers={"Content-Type": "application/vnd.mapbox-vector-tile"},
    )
    response_data: List[Dict[str, Any]] = cast(
        List[Dict[str, Any]], mock_base_endpoint._parse_response_data(response=response)
    )
    assert response_data is not None
    assert isinstance(response_data, list) is True
    assert len(response_data) >= 1

    response_item: Dict[str, Any] = response_data[-1]
    assert response_item is not None
    assert isinstance(response_item, dict)
    assert "structure_id" in response_item
    assert "lon" in response_item
    assert "lat" in response_item
    assert "label" in response_item
    assert "label_confidence" in response_item
    assert "structure_start_date" in response_item
    assert "structure_end_date" in response_item


def test_base_endpoint_parse_response_mvt_data_failure(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    load_mvt_fixture: Callable[[str], bytes],
) -> None:
    """Test that `BaseEndPoint` can not parse response with invalid mvt data."""
    mvt_data: bytes = load_mvt_fixture("datasets/sar_fixed_infrastructure_item.json")
    response = httpx.Response(
        status_code=200,
        content=mvt_data,
        headers={"Content-Type": "application/vnd.mapbox-vector-tile"},
    )
    with pytest.raises(ResultValidationError):
        mock_base_endpoint._parse_response_data(response=response)


def test_base_endpoint_process_response_data_content_type_error(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_raw_result_item: Dict[str, Any],
) -> None:
    """Test that `BaseEndPoint` can not process response with invalid content type."""
    response = httpx.Response(
        status_code=200,
        json=mock_raw_result_item,
        headers={"content-type": "text/html"},
    )

    with pytest.raises(ResultValidationError):
        mock_base_endpoint._process_response_data(response=response)


def test_base_endpoint_process_response_data_item_validation_error(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_raw_result_item: Dict[str, Any],
) -> None:
    """Test that `BaseEndPoint` can not process response data with invalid items."""
    _mock_raw_result_item = {**mock_raw_result_item}
    _mock_raw_result_item.pop("id", None)
    response = httpx.Response(
        status_code=200,
        json=_mock_raw_result_item,
        headers={"content-type": "application/json"},
    )

    with pytest.raises(ResultItemValidationError):
        mock_base_endpoint._process_response_data(response=response)


def test_base_endpoint_process_api_status_error_on_closed_stream(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
) -> None:
    """Test that `BaseEndPoint` can process api status error with a closed and unconsumed stream."""
    request = mock_base_endpoint._build_request()
    response = httpx.Response(status_code=400, content=b"Bad Request", request=request)
    # Simulate a closed and unconsumed stream
    response.is_closed = True
    response.is_stream_consumed = False

    error = mock_base_endpoint._process_api_status_error(response=response)

    assert isinstance(error, APIStatusError)
    assert error.message == "Error code: 400"
    assert error.body is None
    assert error.response == response


def test_base_endpoint_process_api_status_error_invalid_json(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
) -> None:
    """Test that `BaseEndPoint` can process api status error with invalid JSON response."""
    request = mock_base_endpoint._build_request()
    response = httpx.Response(
        status_code=500, text="Internal Server Error", request=request
    )

    error = mock_base_endpoint._process_api_status_error(response=response)

    assert isinstance(error, APIStatusError)
    assert error.message == "Internal Server Error"
    assert error.body == "Internal Server Error"
    assert error.response == response


@pytest.mark.asyncio
@pytest.mark.respx
async def test_base_endpoint_request_success(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_responsex: respx.MockRouter,
    mock_raw_result_item: Dict[str, Any],
) -> None:
    """Test `BaseEndPoint` request success."""
    mock_responsex.post("/200").respond(200, json=[mock_raw_result_item])

    result: MockListResult = await mock_base_endpoint.request()
    assert result is not None
    assert isinstance(result, MockListResult)

    data: List[MockResultItem] = cast(List[MockResultItem], result.data())
    assert data is not None
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[-1].id == mock_raw_result_item["id"]

    df: pd.DataFrame = cast(pd.DataFrame, result.df())

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert list(df.columns) == list(dict(data[-1]).keys())


@pytest.mark.asyncio
@pytest.mark.respx
@pytest.mark.parametrize(
    "timeout_error",
    [
        httpx.ConnectTimeout,  # Connection timeout
        httpx.ReadTimeout,  # Read timeout
        httpx.WriteTimeout,  # Write timeout
        httpx.PoolTimeout,  # Connection pool exhaustion
    ],
)
async def test_base_endpoint_request_timeout_error(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_responsex: respx.MockRouter,
    timeout_error: Type[httpx.TimeoutException],
) -> None:
    """Test `BaseEndPoint` request timeout error."""
    mock_responsex.post("/200").mock(side_effect=timeout_error)

    with pytest.raises(APITimeoutError):
        await mock_base_endpoint.request()


@pytest.mark.asyncio
@pytest.mark.respx
@pytest.mark.parametrize(
    "connect_error",
    [
        Exception,  # Common exceptions
    ],
)
async def test_base_endpoint_request_connection_error(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_responsex: respx.MockRouter,
    connect_error: Type[httpx.TimeoutException],
) -> None:
    """Test `BaseEndPoint` request connection error."""
    mock_responsex.post("/200").mock(side_effect=connect_error)

    with pytest.raises(APIConnectionError):
        await mock_base_endpoint.request()


@pytest.mark.asyncio
@pytest.mark.respx
@pytest.mark.parametrize(
    "error_class, error_status_code, error_message",
    [
        (BadRequestError, 400, "400 Bad Request"),
        (AuthenticationError, 401, "401 Authentication Error"),
        (PermissionDeniedError, 403, "403 Permission Denied Error"),
        (NotFoundError, 404, "404 Not Found Error"),
        (RequestTimeoutError, 408, "408 Request Timeout Error"),
        (ConflictError, 409, "409 Conflict Error"),
        (UnprocessableEntityError, 422, "422 Unprocessable Entity Error"),
        (RateLimitError, 429, "429 Too Many Requests"),
        (InternalServerError, 500, "500 Internal Server Error"),
        (BadGatewayError, 502, "502 Bad Gateway Error"),
        (ServiceUnavailableError, 503, "503 Service Unavailable Error"),
        (GatewayTimeoutError, 504, "504 Gateway Timeout Error"),
        (APIStatusError, 501, "501 Not Implemented"),
    ],
)
async def test_base_endpoint_request_http_status_error(
    mock_base_endpoint: BaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_responsex: respx.MockRouter,
    error_class: Type[APIStatusError],
    error_status_code: int,
    error_message: str,
) -> None:
    """Test `BaseEndPoint` request http status error."""
    mock_responsex.post("/200").mock(
        return_value=httpx.Response(
            status_code=error_status_code, json={"error": error_message}
        )
    )

    with pytest.raises(error_class):
        await mock_base_endpoint.request()
