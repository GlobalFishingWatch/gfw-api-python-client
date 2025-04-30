"""Tests for `gfwapiclient.client.client.Client`."""

import httpx
import pytest

from gfwapiclient.client.client import GFW_API_BASE_URL, Client
from gfwapiclient.exceptions.client import AccessTokenError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.datasets.resources import DatasetResource
from gfwapiclient.resources.events.resources import EventResource
from gfwapiclient.resources.fourwings.resources import FourWingsResource
from gfwapiclient.resources.insights.resources import InsightResource
from gfwapiclient.resources.references.resources import ReferenceResource
from gfwapiclient.resources.vessels.resources import VesselResource

from ..conftest import MOCK_GFW_API_ACCESS_TOKEN, MOCK_GFW_API_BASE_URL


def test_client_initialization_with_explicit_base_url_and_access_token() -> None:
    """Test that `Client` initializes with a provided `base_url` and `access_token`."""
    client = Client(
        base_url=MOCK_GFW_API_BASE_URL,
        access_token=MOCK_GFW_API_ACCESS_TOKEN,
    )
    assert isinstance(client, Client)
    assert isinstance(client._http_client, HTTPClient)
    assert isinstance(client.references, ReferenceResource)
    assert str(client._http_client._base_url) == MOCK_GFW_API_BASE_URL
    assert str(client._http_client._access_token) == MOCK_GFW_API_ACCESS_TOKEN


def test_client_initialization_with_env_vars(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test that `Client` initializes using environment variables."""
    client = Client()
    assert isinstance(client, Client)
    assert isinstance(client._http_client, HTTPClient)
    assert isinstance(client.references, ReferenceResource)
    assert str(client._http_client._base_url) == mock_base_url
    assert str(client._http_client._access_token) == mock_access_token


def test_client_initialization_with_default_base_url(
    mock_access_token: str,
) -> None:
    """Test that initializing `Client` with missing `base_url` uses default."""
    client = Client()
    assert isinstance(client, Client)
    assert isinstance(client._http_client, HTTPClient)
    assert isinstance(client.references, ReferenceResource)
    assert str(client._http_client._base_url) == GFW_API_BASE_URL
    assert str(client._http_client._access_token) == mock_access_token


def test_client_initialization_without_access_token(
    mock_base_url: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test that initializing `Client` with missing `access_token` raises `AccessTokenError`."""
    monkeypatch.delenv("GFW_API_ACCESS_TOKEN", raising=False)
    with pytest.raises(AccessTokenError, match="The `access_token` must be provided"):
        Client(base_url=mock_base_url)


def test_client_initialization_with_custom_http_client_parameters(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test `Client` initialization with custom HTTP client parameters."""
    client = Client(
        follow_redirects=False,
        timeout=30.0,
        connect_timeout=2.0,
        max_connections=50,
        max_keepalive_connections=10,
        max_redirects=1,
    )
    assert isinstance(client, Client)
    assert isinstance(client._http_client, HTTPClient)
    assert client._http_client._base_url == mock_base_url
    assert client._http_client._access_token == mock_access_token
    assert client._http_client.follow_redirects is False
    assert client._http_client.timeout.read == 30.0
    assert client._http_client.timeout.connect == 2.0
    assert isinstance(client._http_client._transport, httpx.AsyncHTTPTransport)
    assert client._http_client._transport._pool._max_connections == 50
    assert client._http_client._transport._pool._max_keepalive_connections == 10
    assert client._http_client.max_redirects == 1


def test_client_fourwings_property_returns_fourwing_resource_and_is_cached(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test `Client.fourwings` returns `FourWingsResource` and caches the instance."""
    client = Client()
    assert isinstance(client.fourwings, FourWingsResource)
    # Test that the property is cached
    assert client.fourwings is client.fourwings


def test_client_vessels_property_returns_vessels_resource_and_is_cached(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test `Client.vessels` returns `VesselResource` and caches the instance."""
    client = Client()
    assert isinstance(client.vessels, VesselResource)
    # Test that the property is cached
    assert client.vessels is client.vessels


def test_client_events_property_returns_vessels_resource_and_is_cached(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test `Client.events` returns `EventResource` and caches the instance."""
    client = Client()
    assert isinstance(client.events, EventResource)
    # Test that the property is cached
    assert client.events is client.events


def test_client_insights_property_returns_insight_resource_and_is_cached(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test `Client.insights` returns `InsightResource` and caches the instance."""
    client = Client()
    assert isinstance(client.insights, InsightResource)
    # Test that the property is cached
    assert client.insights is client.insights


def test_client_datasets_property_returns_dataset_resource_and_is_cached(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test `Client.datasets` returns `DatasetResource` and caches the instance."""
    client = Client()
    assert isinstance(client.datasets, DatasetResource)
    # Test that the property is cached
    assert client.datasets is client.datasets


def test_client_references_property_returns_reference_resource_and_is_cached(
    mock_base_url: str,
    mock_access_token: str,
) -> None:
    """Test `Client.references` returns `ReferenceResource` and caches the instance."""
    client = Client()
    assert isinstance(client.references, ReferenceResource)
    # Test that the property is cached
    assert client.references is client.references
