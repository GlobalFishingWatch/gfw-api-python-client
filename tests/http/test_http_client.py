"""Tests for `gfwapiclient.http.client.HTTPClient`."""

import os

import httpx
import pytest

from pytest_mock import MockerFixture

from gfwapiclient.exceptions.base import GFWError
from gfwapiclient.exceptions.client import AccessTokenError, BaseUrlError
from gfwapiclient.http.client import HTTPClient


MOCK_BASE_URL = "https://gateway.api.mocking.globalfishingwatch.org/v3/"
MOCK_ACCESS_TOKEN = "mocking_GoXcgX1YFRRph48Rv6w9aGIDQzQd7zaB"


@pytest.fixture
def mock_base_url(monkeypatch: pytest.MonkeyPatch) -> None:
    """Fixture to set a mock base URL using an environment variable."""
    monkeypatch.setenv("GFW_API_BASE_URL", MOCK_BASE_URL)


@pytest.fixture
def mock_access_token(monkeypatch: pytest.MonkeyPatch) -> None:
    """Fixture to set a mock access token using an environment variable."""
    monkeypatch.setenv("GFW_API_ACCESS_TOKEN", MOCK_ACCESS_TOKEN)


@pytest.fixture
def mock_transport() -> httpx.MockTransport:
    """Fixture providing a mock HTTP transport for `HTTPClient`.

    This fixture simulates various HTTP responses, including:
    - `200 OK`
    - `301 Redirect`
    - `404 Not Found`
    - `500 Internal Server Error`
    - `400 Bad Request`
    """

    async def request_handler(request: httpx.Request) -> httpx.Response:
        """Handle mock HTTP requests based on the request path."""
        match request.url.path:
            case "/v3/ok":
                return httpx.Response(200, json={"message": "success"})
            case "/v3/redirect":
                return httpx.Response(301, headers={"Location": "/v3/ok"})
            case "/v3/notfound":
                return httpx.Response(404, json={"error": "Not Found"})
            case "/v3/server-error":
                return httpx.Response(500, json={"error": "Server Error"})
            case _:
                return httpx.Response(400, json={"error": "Bad Request"})

    return httpx.MockTransport(request_handler)


def test_http_client_initialization_with_explicit_base_url_and_access_token() -> None:
    """Test that `HTTPClient` initializes successfully when a `base_url` and `access_token` are explicitly provided."""
    client = HTTPClient(base_url=MOCK_BASE_URL, access_token=MOCK_ACCESS_TOKEN)
    assert isinstance(client, HTTPClient)
    assert str(client._base_url) == MOCK_BASE_URL
    assert str(client._access_token) == MOCK_ACCESS_TOKEN
    assert client.headers["Accept"] == "application/json"
    assert client.headers["Content-Type"] == "application/json"
    assert client.headers["User-Agent"].startswith("gfw-api-python-client/")
    assert client.headers["Authorization"] == f"Bearer {MOCK_ACCESS_TOKEN}"


def test_http_client_initialization_with_env_vars(
    mock_base_url: object,
    mock_access_token: object,
) -> None:
    """Test that `HTTPClient` initializes successfully using the `GFW_API_BASE_URL` and `GFW_API_ACCESS_TOKEN` environment variables."""
    client = HTTPClient()
    assert isinstance(client, HTTPClient)
    assert str(client._base_url) == MOCK_BASE_URL
    assert str(client._access_token) == MOCK_ACCESS_TOKEN


def test_http_client_initialization_without_base_url(
    mock_access_token: object,
) -> None:
    """Test that initializing `HTTPClient` without a `base_url` or `GFW_API_BASE_URL` environment variable raises a `BaseUrlError`."""
    os.environ.pop("GFW_API_BASE_URL", None)
    with pytest.raises(BaseUrlError, match="The `base_url` must be provided"):
        HTTPClient()


def test_http_client_initialization_without_access_token(
    mock_base_url: object,
) -> None:
    """Test that initializing `HTTPClient` without a `access_token` or `GFW_API_ACCESS_TOKEN` environment variable raises a `AccessTokenError`."""
    os.environ.pop("GFW_API_ACCESS_TOKEN", None)
    with pytest.raises(AccessTokenError, match="The `access_token` must be provided"):
        HTTPClient()


def test_http_client_apply_timeouts(
    mock_base_url: object,
    mock_access_token: object,
) -> None:
    """Test that `HTTPClient` operations `timeout` are correctly applied."""
    client = HTTPClient(timeout=30, connect_timeout=10)
    assert isinstance(client.timeout, httpx.Timeout)
    assert client.timeout.read == 30
    assert client.timeout.write == 30
    assert client.timeout.pool == 30
    assert client.timeout.connect == 10

    # Defaults
    client = HTTPClient()
    assert isinstance(client.timeout, httpx.Timeout)
    assert client.timeout.read == 60
    assert client.timeout.write == 60
    assert client.timeout.pool == 60
    assert client.timeout.connect == 5


def test_http_client_apply_connection_limits(
    mock_base_url: object,
    mock_access_token: object,
) -> None:
    """Test that `HTTPClient` connection `limits` are correctly applied."""
    client = HTTPClient(max_connections=50, max_keepalive_connections=25)
    assert isinstance(client._transport, httpx.AsyncHTTPTransport)
    assert client._transport._pool._max_connections == 50
    assert client._transport._pool._max_keepalive_connections == 25

    # Defaults
    client = HTTPClient()
    assert isinstance(client._transport, httpx.AsyncHTTPTransport)
    assert client._transport._pool._max_connections == 100
    assert client._transport._pool._max_keepalive_connections == 20


def test_http_client_apply_follow_redirects(
    mock_base_url: object,
    mock_access_token: object,
) -> None:
    """Test that `HTTPClient` `follow_redirects` is correctly applied."""
    client = HTTPClient(follow_redirects=False)
    assert client.follow_redirects is False

    client_with_redirects = HTTPClient(follow_redirects=True)
    assert client_with_redirects.follow_redirects is True

    # Defaults
    client_with_redirects = HTTPClient()
    assert client_with_redirects.follow_redirects is True


def test_http_client_apply_max_redirects(
    mock_base_url: object,
    mock_access_token: object,
) -> None:
    """Test that `HTTPClient` `max_redirects` is correctly applied."""
    client = HTTPClient(max_redirects=5)
    assert client.max_redirects == 5

    # Defaults
    client_with_default_redirects = HTTPClient()
    assert client_with_default_redirects.max_redirects == 2


@pytest.mark.asyncio
async def test_http_client_aenter(
    mock_base_url: object,
    mock_access_token: object,
) -> None:
    """Test that `__aenter__` returns the `HTTPClient` instance."""
    async with HTTPClient() as client:
        assert isinstance(client, HTTPClient)


@pytest.mark.asyncio
async def test_http_client_aexit_calls_aclose(
    mock_base_url: object,
    mock_access_token: object,
    mocker: MockerFixture,
) -> None:
    """Test that `__aexit__` calls `aclose()` to clean up resources."""
    client = HTTPClient()
    mock_aclose = mocker.patch.object(client, "aclose", autospec=True)

    async with client:
        pass  # No operation, just testing context management

    mock_aclose.assert_awaited_once()


@pytest.mark.asyncio
async def test_http_client_aexit_on_exception(
    mock_base_url: object,
    mock_access_token: object,
    mocker: MockerFixture,
) -> None:
    """Test that `__aexit__` calls `aclose()` even when an exception occurs."""
    client = HTTPClient()
    mock_aclose = mocker.patch.object(client, "aclose", autospec=True)

    with pytest.raises(GFWError):
        async with client:
            raise GFWError("Connection error")  # Force exception

    mock_aclose.assert_awaited_once()


@pytest.mark.asyncio
async def test_http_client_follow_redirects(
    mock_base_url: object,
    mock_access_token: object,
    mock_transport: httpx.MockTransport,
) -> None:
    """Test that `HTTPClient` follows redirects."""
    async with HTTPClient(transport=mock_transport) as client:
        response = await client.get("/redirect")
        assert response.status_code == 200
        assert response.json() == {"message": "success"}


@pytest.mark.asyncio
async def test_http_client_max_redirects_exceeded(
    mock_base_url: object,
    mock_access_token: object,
    mock_transport: httpx.MockTransport,
) -> None:
    """Test that `HTTPClient` enforces `max_redirects` limit."""
    async with HTTPClient(transport=mock_transport, max_redirects=0) as client:
        with pytest.raises(httpx.TooManyRedirects):
            await client.get("/redirect")


@pytest.mark.asyncio
async def test_http_client_issue_get_request(
    mock_base_url: object,
    mock_access_token: object,
    mock_transport: httpx.MockTransport,
) -> None:
    """Test that `HTTPClient` can issue GET request."""
    async with HTTPClient(transport=mock_transport) as client:
        response = await client.get("/ok")
        assert response.status_code == 200
        assert response.json() == {"message": "success"}


@pytest.mark.asyncio
async def test_http_client_issue_post_request(
    mock_base_url: object,
    mock_access_token: object,
    mock_transport: httpx.MockTransport,
) -> None:
    """Test that `HTTPClient` can issue POST request."""
    async with HTTPClient(transport=mock_transport) as client:
        response = await client.post("/ok")
        assert response.status_code == 200
        assert response.json() == {"message": "success"}
