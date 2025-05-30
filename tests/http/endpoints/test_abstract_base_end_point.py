"""Tests for `gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint`."""

import http

from typing import Any, Dict, Optional

import httpx
import pytest

from typing_extensions import override

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints.abc import AbstractBaseEndPoint

from .conftest import (
    MockListResult,
    MockRequestBody,
    MockRequestParams,
    MockResultItem,
    confidences,
    datasets,
    duration,
    fields,
    gap_intentional_disabling,
    geometry,
    limit,
    mock_raw_result_item,
    sort,
    start_date,
    time_series_interval,
)


class MockAbstractBaseEndPoint(
    AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ]
):
    """A sample endpoint for testing `AbstractBaseEndPoint` and HTTP endpoints behavior."""

    @override
    async def request(self, **kwargs: Any) -> MockListResult:
        """Send an HTTP request for this endpoint."""
        raw_item: Dict[str, Any] = mock_raw_result_item()
        item: MockResultItem = MockResultItem(**raw_item)
        return MockListResult(data=[item])


@pytest.fixture
def mock_abstract_base_endpoint(
    mock_http_client: HTTPClient,
    mock_request_params: MockRequestParams,
    mock_request_body: MockRequestBody,
) -> AbstractBaseEndPoint[
    MockRequestParams, MockRequestBody, MockResultItem, MockListResult
]:
    """Fixture for mock `AbstractBaseEndPoint`.

    Returns:
        An `AbstractBaseEndPoint` instance for testing purposes.
    """
    return MockAbstractBaseEndPoint(
        method=http.HTTPMethod.GET,
        path="/200",
        request_params=mock_request_params,
        request_body=mock_request_body,
        result_item_class=MockResultItem,
        result_class=MockListResult,
        http_client=mock_http_client,
    )


def test_abstract_base_endpoint_instance(
    mock_abstract_base_endpoint: AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
) -> None:
    """Test that `AbstractBaseEndPoint` can be instantiated and its attributes are correctly set."""
    assert mock_abstract_base_endpoint._method == http.HTTPMethod.GET
    assert mock_abstract_base_endpoint._path == "/200"
    assert mock_abstract_base_endpoint._request_params is not None
    assert isinstance(mock_abstract_base_endpoint._request_params, MockRequestParams)
    assert mock_abstract_base_endpoint._request_body is not None
    assert isinstance(mock_abstract_base_endpoint._request_body, MockRequestBody)
    assert mock_abstract_base_endpoint._result_item_class == MockResultItem
    assert mock_abstract_base_endpoint._result_class == MockListResult
    assert mock_abstract_base_endpoint._http_client is not None
    assert isinstance(mock_abstract_base_endpoint._http_client, HTTPClient)


def test_abstract_base_endpoint_custom_headers(
    mock_abstract_base_endpoint: AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
) -> None:
    """Test that `AbstractBaseEndPoint` can have custom headers."""
    assert mock_abstract_base_endpoint.headers == {}


def test_abstract_base_endpoint_prepare_request_method(
    mock_abstract_base_endpoint: AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
) -> None:
    """Test that `AbstractBaseEndPoint` can prepare request method."""
    assert mock_abstract_base_endpoint._prepare_request_method() == str(
        mock_abstract_base_endpoint._method
    )


def test_abstract_base_endpoint_prepare_request_path(
    mock_abstract_base_endpoint: AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
) -> None:
    """Test that `AbstractBaseEndPoint` can prepare request path."""
    assert mock_abstract_base_endpoint._prepare_request_path() == "/200"


def test_abstract_base_endpoint_prepare_request_url(
    mock_abstract_base_endpoint: AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_base_url: str,
) -> None:
    """Test that `AbstractBaseEndPoint` can prepare request URL."""
    request_url: httpx.URL = mock_abstract_base_endpoint._prepare_request_url()
    assert str(request_url) == f"{mock_base_url}200"


def test_abstract_base_endpoint_prepare_request_headers(
    mock_abstract_base_endpoint: AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_access_token: str,
) -> None:
    """Test that `AbstractBaseEndPoint` can prepare request headers."""
    request_headers = mock_abstract_base_endpoint._prepare_request_headers()
    assert isinstance(request_headers, httpx.Headers)
    assert request_headers["Accept"] == "application/json"
    assert request_headers["Content-Type"] == "application/json"
    assert request_headers["User-Agent"].startswith("gfw-api-python-client/")
    assert request_headers["Authorization"] == f"Bearer {mock_access_token}"


def test_abstract_base_endpoint_prepare_request_query_params(
    mock_abstract_base_endpoint: AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
) -> None:
    """Test that `AbstractBaseEndPoint` can prepare request query parameters."""
    expected: Dict[str, Any] = {
        "datasets[0]": datasets[0],
        "datasets[1]": datasets[1],
        "fields": ",".join(fields),
        "start-date": start_date.isoformat(),
        "confidences": str(confidences[0]),
        "limit": str(limit),
        "gap-intentional-disabling": str(gap_intentional_disabling).lower(),
        "sort": sort.value,
    }

    query_params: Optional[httpx.QueryParams] = (
        mock_abstract_base_endpoint._prepare_request_query_params()
    )
    assert isinstance(query_params, httpx.QueryParams)

    output: Dict[str, Any] = dict(query_params)
    assert output == expected


def test_abstract_base_endpoint_prepare_no_request_query_params(
    mock_http_client: HTTPClient,
) -> None:
    """Test that `AbstractBaseEndPoint` can prepare no request query parameters."""
    mock_abstract_base_endpoint = MockAbstractBaseEndPoint(
        method=http.HTTPMethod.GET,
        path="/200",
        request_params=None,
        request_body=None,
        result_item_class=MockResultItem,
        result_class=MockListResult,
        http_client=mock_http_client,
    )

    query_params = mock_abstract_base_endpoint._prepare_request_query_params()
    assert query_params is None
    assert not isinstance(query_params, httpx.QueryParams)


def test_abstract_base_endpoint_prepare_request_json_body(
    mock_abstract_base_endpoint: AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
) -> None:
    """Test that `AbstractBaseEndPoint` can prepare request JSON body."""
    request_json_body: Optional[Dict[str, Any]] = (
        mock_abstract_base_endpoint._prepare_request_json_body()
    )
    assert isinstance(request_json_body, dict)

    expected: Dict[str, Any] = {
        "datasets": datasets,
        "startDate": start_date.isoformat(),
        "confidences": confidences,
        "geometry": geometry,
        "duration": duration,
        "gapIntentionalDisabling": gap_intentional_disabling,
        "timeseriesInterval": time_series_interval.value,
    }

    assert request_json_body == expected


def test_abstract_base_endpoint_prepare_no_request_json_body(
    mock_http_client: HTTPClient,
) -> None:
    """Test that `AbstractBaseEndPoint` can prepare no request JSON body."""
    mock_abstract_base_endpoint = MockAbstractBaseEndPoint(
        method=http.HTTPMethod.GET,
        path="/200",
        request_params=None,
        request_body=None,
        result_item_class=MockResultItem,
        result_class=MockListResult,
        http_client=mock_http_client,
    )

    request_json_body = mock_abstract_base_endpoint._prepare_request_json_body()
    assert request_json_body is None
    assert not isinstance(request_json_body, dict)


def test_abstract_base_endpoint_build_request(
    mock_abstract_base_endpoint: AbstractBaseEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
) -> None:
    """Test that `AbstractBaseEndPoint` can build a request."""
    request: httpx.Request = mock_abstract_base_endpoint._build_request()
    assert isinstance(request, httpx.Request)
    assert request.method == str(mock_abstract_base_endpoint._method)
    assert str(request.url).startswith(
        str(mock_abstract_base_endpoint._prepare_request_url())
    )
