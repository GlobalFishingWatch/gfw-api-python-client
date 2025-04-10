"""Tests for `gfwapiclient.http.client.HTTPClient`."""

from typing import Type

import httpx
import pytest
import respx

from pytest_mock import MockerFixture

from gfwapiclient.__version__ import __version__
from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.exceptions.client import AccessTokenError, BaseUrlError
from gfwapiclient.http.client import HTTPClient

from ..conftest import MOCK_GFW_API_ACCESS_TOKEN, MOCK_GFW_API_BASE_URL


def test_http_client_initialization_with_explicit_base_url_and_access_token() -> None:
    """Test that `HTTPClient` initializes with a provided `base_url` and `access_token`."""
    client = HTTPClient(
        base_url=MOCK_GFW_API_BASE_URL,
        access_token=MOCK_GFW_API_ACCESS_TOKEN,
    )
    assert isinstance(client, HTTPClient)
    assert str(client._base_url) == MOCK_GFW_API_BASE_URL
    assert str(client._access_token) == MOCK_GFW_API_ACCESS_TOKEN
    assert client.headers["Accept"] == "application/json"
    assert client.headers["Content-Type"] == "application/json"
    assert client.headers["User-Agent"].startswith("gfw-api-python-client/")
    assert __version__ in client.headers["User-Agent"]
    assert client.headers["Authorization"] == f"Bearer {MOCK_GFW_API_ACCESS_TOKEN}"


def test_http_client_initialization_with_env_vars(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test that `HTTPClient` initializes using environment variables."""
    client = HTTPClient()
    assert isinstance(client, HTTPClient)
    assert str(client._base_url) == mock_base_url
    assert str(client._access_token) == mock_access_token


def test_http_client_initialization_without_base_url(
    mock_access_token: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test that initializing `HTTPClient` with missing `base_url` raises `BaseUrlError`."""
    monkeypatch.delenv("GFW_API_BASE_URL", raising=False)
    with pytest.raises(BaseUrlError, match="The `base_url` must be provided"):
        HTTPClient()


def test_http_client_initialization_without_access_token(
    mock_base_url: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test that initializing `HTTPClient` with missing `access_token` raises `AccessTokenError`."""
    monkeypatch.delenv("GFW_API_ACCESS_TOKEN", raising=False)
    with pytest.raises(AccessTokenError, match="The `access_token` must be provided"):
        HTTPClient()


def test_http_client_apply_timeouts(
    mock_base_url: str,
    mock_access_token: str,
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
    mock_base_url: str,
    mock_access_token: str,
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
    mock_base_url: str,
    mock_access_token: str,
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
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test that `HTTPClient` `max_redirects` is correctly applied."""
    client = HTTPClient(max_redirects=5)
    assert client.max_redirects == 5

    # Defaults
    client_with_default_redirects = HTTPClient()
    assert client_with_default_redirects.max_redirects == 2


@pytest.mark.asyncio
async def test_http_client_aenter(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test that `__aenter__` returns the `HTTPClient` instance."""
    async with HTTPClient() as client:
        assert isinstance(client, HTTPClient)


@pytest.mark.asyncio
async def test_http_client_aexit_calls_aclose(
    mock_base_url: str,
    mock_access_token: str,
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
    mock_base_url: str,
    mock_access_token: str,
    mocker: MockerFixture,
) -> None:
    """Test that `__aexit__` calls `aclose()` even when an exception occurs."""
    client = HTTPClient()
    mock_aclose = mocker.patch.object(client, "aclose", autospec=True)

    with pytest.raises(GFWAPIClientError):
        async with client:
            raise GFWAPIClientError("Connection error")  # Force exception

    mock_aclose.assert_awaited_once()


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
async def test_http_client_timeout_errors(
    mock_responsex: respx.MockRouter,
    timeout_error: Type[httpx.TimeoutException],
) -> None:
    """Test that `HTTPClient` handle timeout errors."""
    async with HTTPClient() as client:
        with pytest.raises(timeout_error):
            mock_responsex.get("/200").mock(side_effect=timeout_error)

            await client.get("/200")


@pytest.mark.asyncio
@pytest.mark.respx
@pytest.mark.parametrize(
    "network_error",
    [
        httpx.ConnectError,  # Connect error
        httpx.ReadError,  # Read error
        httpx.WriteError,  # Write error
        httpx.CloseError,  # Close error
    ],
)
async def test_http_client_network_errors(
    mock_responsex: respx.MockRouter,
    network_error: Type[httpx.NetworkError],
) -> None:
    """Test that `HTTPClient` handle network errors."""
    async with HTTPClient() as client:
        with pytest.raises(network_error):
            mock_responsex.get("/200").mock(side_effect=network_error)

            await client.get("/200")


@pytest.mark.asyncio
async def test_http_client_follow_redirects(
    mock_responsex: respx.MockRouter,
) -> None:
    """Test that `HTTPClient` follows redirects."""
    async with HTTPClient() as client:
        mock_responsex.get("/200").respond(200, json={"message": "success"})
        mock_responsex.get("/301").respond(
            301, headers={"Location": f"{client._merge_url('/200')}"}
        )

        response = await client.get("/301")

        assert response.status_code == 200
        assert response.json() == {"message": "success"}


@pytest.mark.asyncio
@pytest.mark.respx
async def test_http_client_max_redirects_exceeded(
    mock_responsex: respx.MockRouter,
) -> None:
    """Test that `HTTPClient` enforces `max_redirects` limit."""
    async with HTTPClient(max_redirects=0) as client:
        with pytest.raises(httpx.TooManyRedirects):
            mock_location = f"{client._merge_url('/200')}"
            mock_responsex.get("/301").respond(
                301, headers={"Location": f"{mock_location}"}
            )

            await client.get("/301")


@pytest.mark.asyncio
async def test_http_client_infinite_redirects(
    mock_responsex: respx.MockRouter,
) -> None:
    """Test that `HTTPClient` enforces `max_redirects` limit when there is infinite redirects."""
    async with HTTPClient() as client:
        with pytest.raises(httpx.TooManyRedirects):
            mock_location = f"{client._merge_url('/301')}"  # Infinite loop
            mock_responsex.get("/301").respond(
                301, headers={"Location": f"{mock_location}"}
            )

            await client.get("/301")


@pytest.mark.asyncio
@pytest.mark.respx
async def test_http_client_issue_get_request(
    mock_responsex: respx.MockRouter,
) -> None:
    """Test that `HTTPClient` can issue GET request."""
    async with HTTPClient() as client:
        mock_responsex.get("/200").respond(200, json={"message": "success"})

        response = await client.get("/200")

        assert response.status_code == 200
        assert response.json() == {"message": "success"}


@pytest.mark.asyncio
@pytest.mark.respx
async def test_http_client_issue_post_request(
    mock_responsex: respx.MockRouter,
) -> None:
    """Test that `HTTPClient` can issue POST request."""
    async with HTTPClient() as client:
        mock_responsex.post("/201").respond(201, json={"message": "success"})

        response = await client.post("/201")

        assert response.status_code == 201
        assert response.json() == {"message": "success"}
