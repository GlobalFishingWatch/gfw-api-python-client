"""Tests for `gfwapiclient.http.client.HttpClient`."""

import os

import httpx
import pytest

from gfwapiclient.exceptions.base import GFWError
from gfwapiclient.http.client import HttpClient


MOCK_BASE_URL = "https://gateway.api.mocking.globalfishingwatch.org/v3/"


@pytest.fixture
def mock_base_url(monkeypatch: pytest.MonkeyPatch) -> None:
    """Set a mock base URL for testing by modifying the environment variable."""
    monkeypatch.setenv("GFW_API_BASE_URL", MOCK_BASE_URL)


def test_http_client_initialization_with_base_url() -> None:
    """Test successful initialization with an explicitly provided base URL."""
    client = HttpClient(base_url=MOCK_BASE_URL)
    assert isinstance(client, HttpClient)
    assert str(client.base_url) == MOCK_BASE_URL


def test_http_client_initialization_with_env_var(mock_base_url: object) -> None:
    """Test successful initialization using the environment variable."""
    client = HttpClient()
    assert isinstance(client, HttpClient)
    assert str(client.base_url) == MOCK_BASE_URL


def test_http_client_initialization_without_base_url() -> None:
    """Test that initializing without a base_url or environment variable raises GFWError."""
    os.environ.pop("GFW_API_BASE_URL", None)
    with pytest.raises(GFWError, match="The `base_url` must be provided"):
        HttpClient()


def test_http_client_timeout_config(mock_base_url: object) -> None:
    """Test that timeout settings are correctly applied."""
    client = HttpClient(timeout=30, connect_timeout=10)
    assert isinstance(client.timeout, httpx.Timeout)
    assert client.timeout.read == 30
    assert client.timeout.write == 30
    assert client.timeout.pool == 30
    assert client.timeout.connect == 10


def test_http_client_connection_limits(mock_base_url: object) -> None:
    """Test that connection limits are correctly applied."""
    client = HttpClient(max_connections=50, max_keepalive_connections=25)
    assert isinstance(client._transport, httpx.AsyncHTTPTransport)
    assert client._transport._pool._max_connections == 50
    assert client._transport._pool._max_keepalive_connections == 25


def test_http_client_follow_redirects(mock_base_url: object) -> None:
    """Test that HttpClient respects the `follow_redirects` parameter."""
    client = HttpClient(follow_redirects=False)
    assert client.follow_redirects is False

    client_with_redirects = HttpClient(follow_redirects=True)
    assert client_with_redirects.follow_redirects is True


def test_http_client_max_redirects(mock_base_url: object) -> None:
    """Test that HttpClient correctly applies `max_redirects`."""
    client = HttpClient(max_redirects=5)
    assert client.max_redirects == 5

    client_with_default_redirects = HttpClient()
    assert client_with_default_redirects.max_redirects == 2  # Default value
