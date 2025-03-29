"""Tests for `gfwapiclient.http.endpoints.get.GetEndPoint`."""

import http

from typing import Any, Dict, List, cast

import pandas as pd
import pytest
import respx

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints.get import GetEndPoint
from tests.http.endpoints.conftest import (
    MockListResult,
    MockRequestBody,
    MockRequestParams,
    MockResultItem,
)


class MockGetEndPoint(
    GetEndPoint[MockRequestParams, MockRequestBody, MockResultItem, MockListResult]
):
    """A sample get endpoint for testing `GetEndPoint` and HTTP endpoints behavior."""

    pass


@pytest.fixture
def mock_get_endpoint(
    mock_http_client: HTTPClient,
    mock_request_params: MockRequestParams,
) -> GetEndPoint[MockRequestParams, MockRequestBody, MockResultItem, MockListResult]:
    """Fixture for mock `GetEndPoint`.

    Returns:
        A `GetEndPoint` instance for testing purposes.
    """
    return MockGetEndPoint(
        path="/200",
        request_params=mock_request_params,
        result_item_class=MockResultItem,
        result_class=MockListResult,
        http_client=mock_http_client,
    )


def test_get_endpoint_instance(
    mock_http_client: HTTPClient,
    mock_request_params: MockRequestParams,
) -> None:
    """Test that `GetEndPoint` can be instantiated and its attributes are correctly set."""
    endpoint = MockGetEndPoint(
        path="/200",
        request_params=mock_request_params,
        result_item_class=MockResultItem,
        result_class=MockListResult,
        http_client=mock_http_client,
    )

    assert endpoint._method == http.HTTPMethod.GET
    assert endpoint._path == "/200"
    assert endpoint._request_params is not None
    assert isinstance(endpoint._request_params, MockRequestParams)
    assert endpoint._request_params == mock_request_params
    assert endpoint._result_item_class == MockResultItem
    assert endpoint._result_class == MockListResult
    assert endpoint._http_client is not None
    assert isinstance(endpoint._http_client, HTTPClient)
    assert endpoint._http_client == mock_http_client


@pytest.mark.asyncio
@pytest.mark.respx
async def test_get_endpoint_request_success(
    mock_get_endpoint: GetEndPoint[
        MockRequestParams, MockRequestBody, MockResultItem, MockListResult
    ],
    mock_responsex: respx.MockRouter,
    mock_raw_result_item: Dict[str, Any],
) -> None:
    """Test `GetEndPoint` request success.

    This test verifies that the `GetEndPoint` correctly processes a successful GET request
    and returns the expected result.
    """
    mock_responsex.get("/200").respond(200, json=[mock_raw_result_item])

    result: MockListResult = await mock_get_endpoint.request()
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
