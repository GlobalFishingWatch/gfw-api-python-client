"""Test configurations for `gfwapiclient.http`."""

import pytest

from gfwapiclient.http.client import HTTPClient


@pytest.fixture
def mock_http_client(mock_base_url: str, mock_access_token: str) -> HTTPClient:
    """Fixture for creating a mock HTTP client.

    Returns:
        HTTPClient:
            An instance of `HTTPClient` configured with a base URL and access token.
    """
    return HTTPClient(base_url=mock_base_url, access_token=mock_access_token)
