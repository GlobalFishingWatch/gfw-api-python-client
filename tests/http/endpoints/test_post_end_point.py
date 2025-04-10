"""Tests for `gfwapiclient.http.endpoints.post.PostEndPoint`."""

import http

from typing import Any, Dict, List, cast

import pandas as pd
import pytest
import respx

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints.post import PostEndPoint
from tests.http.endpoints.conftest import (
    MockListResult,
    MockRequestBody,
    MockRequestParams,
    MockResultItem,
)


class MockPostEndPoint(
    PostEndPoint[MockRequestParams, MockRequestBody, MockResultItem, MockListResult]
):
    """A sample post endpoint for testing `PostEndPoint` and HTTP endpoints behavior."""

    pass


@pytest.fixture
def mock_post_endpoint(
    mock_http_client: HTTPClient,
    mock_request_params: MockRequestParams,
    mock_request_body: MockRequestBody,
) -> PostEndPoint[MockRequestParams, MockRequestBody, MockResultItem, MockListResult]:
    """Fixture for mock `PostEndPoint`.

    Returns:
        A `PostEndPoint` instance for testing purposes.
    """
    return MockPostEndPoint(
        path="/200",
        request_params=mock_request_params,
        request_body=mock_request_body,
        result_item_class=MockResultItem,
        result_class=MockListResult,
        http_client=mock_http_client,
    )


def test_post_endpoint_instance(
    mock_http_client: HTTPClient,
    mock_request_params: MockRequestParams,
    mock_request_body: MockRequestBody,
) -> None:
    """Test that `PostEndPoint` can be instantiated and its attributes are correctly set."""
    endpoint = MockPostEndPoint(
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


@pytest.mark.asyncio
@pytest.mark.respx
async def test_post_endpoint_request_success(
    mock_post_endpoint: PostEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_responsex: respx.MockRouter,
    mock_raw_result_item: Dict[str, Any],
) -> None:
    """Test `PostEndPoint` request success.

    This test verifies that the `PostEndPoint` correctly processes a successful POST request
    and returns the expected result.
    """
    mock_responsex.post("/200").respond(200, json=[mock_raw_result_item])

    result: MockListResult = await mock_post_endpoint.request()
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
