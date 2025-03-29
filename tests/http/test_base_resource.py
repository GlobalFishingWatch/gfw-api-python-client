"""Tests for `gfwapiclient.resources.base.BaseResource`."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.resources import BaseResource


def test_base_resource_instance(mock_http_client: HTTPClient) -> None:
    """Test that `BaseResource` can be instantiated and its attributes are correctly set."""
    resource = BaseResource(http_client=mock_http_client)
    assert resource._http_client == mock_http_client
