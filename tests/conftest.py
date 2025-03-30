"""Test configurations for `gfwapiclient`."""

import os

from typing import Final

import pytest
import respx

from respx.patterns import parse_url_patterns

from gfwapiclient.http.client import HTTPClient


MOCK_GFW_API_BASE_URL: Final[str] = (
    "https://gateway.api.mocking.globalfishingwatch.org/v3/"
)
MOCK_GFW_API_ACCESS_TOKEN: Final[str] = "mocking_GoXcgX1YFRRph48Rv6w9aGIDQzQd7zaB"


@pytest.fixture
def mock_base_url(monkeypatch: pytest.MonkeyPatch) -> str:
    """Sets a mock base URL for the Global Fishing Watch (GFW) API.

    This fixture overrides the `GFW_API_BASE_URL` environment variable,
    ensuring that tests interact with a mocked API instead of the real one.

    Args:
        monkeypatch (pytest.MonkeyPatch):
            Pytest's built-in fixture for modifying environment variables.

    Returns:
        str:
            The mocked base URL.

    Example:
        ```python
        def test_example(mock_base_url: object):

            # Perform test
            # ...

        ```
    """
    monkeypatch.setenv("GFW_API_BASE_URL", MOCK_GFW_API_BASE_URL)
    return MOCK_GFW_API_BASE_URL


@pytest.fixture
def mock_access_token(monkeypatch: pytest.MonkeyPatch) -> str:
    """Sets a mock access token for the Global Fishing Watch (GFW) API.

    This fixture overrides the `GFW_API_ACCESS_TOKEN` environment variable,
    preventing tests from requiring real authentication credentials.

    Args:
        monkeypatch (pytest.MonkeyPatch):
            Pytest's built-in fixture for modifying environment variables.

    Returns:
        str:
            The mocked access token.

    Example:
        ```python
        def test_example(mock_access_token: object):

            # Perform test
            # ...

        ```
    """
    monkeypatch.setenv("GFW_API_ACCESS_TOKEN", MOCK_GFW_API_ACCESS_TOKEN)
    return MOCK_GFW_API_ACCESS_TOKEN


@pytest.fixture
def mock_responsex(
    mock_base_url: str,
    mock_access_token: str,
    respx_mock: respx.MockRouter,
) -> respx.MockRouter:
    """Configures `respx` to intercept and mock HTTP requests to the API.

    This fixture ensures that all outgoing HTTP requests matching the
    `GFW_API_BASE_URL` pattern are intercepted by `respx`, allowing tests
    to define expected responses.

    Args:
        mock_base_url (str):
            Ensures the base URL environment variable is set before mocking.

        mock_access_token (str):
            Ensures the access token environment variable is set before mocking.

        respx_mock (respx.MockRouter):
            The `respx` mock router fixture.

    Returns:
        respx.MockRouter:
            The configured mock router for HTTP request interception.

    Example:
        ```python
        @pytest.mark.asyncio
        @pytest.mark.respx
        async def test_example(mock_responsex: respx.MockRouter) -> None:
            # Mock an API response
            mock_responsex.get("/example").respond(200, json={"message": "success"})

            # Perform test that makes an HTTP request
            # ...
        ```
    """
    # Configure `respx` to match requests with the mock base URL
    mock_url: str = os.environ.get("GFW_API_BASE_URL", MOCK_GFW_API_BASE_URL)

    respx_mock._bases = parse_url_patterns(mock_url, exact=False)
    assert respx_mock._bases is not None, "Failed to set mock base URL in `respx`"

    return respx_mock


@pytest.fixture
def mock_http_client(mock_base_url: str, mock_access_token: str) -> HTTPClient:
    """Fixture for creating a mock HTTP client.

    Returns:
        HTTPClient:
            An instance of `HTTPClient` configured with a base URL and access token.
    """
    return HTTPClient(base_url=mock_base_url, access_token=mock_access_token)


def pytest_configure(config: pytest.Config) -> None:
    """Perform initial pytest configuration.

    Registers custom markers for integration tests.

    Args:
        config (pytest.Config):
            The pytest configuration object.

    See: https://docs.pytest.org/en/stable/reference/reference.html#pytest.hookspec.pytest_configure
    """
    config.addinivalue_line(
        "markers",
        "integration: mark a test to run against the staging or production Global Fishing Watch (GFW) API.",
    )


def pytest_runtest_setup(item: pytest.Item) -> None:
    """Perform test setup, skipping integration tests if not configured.

    Automatically skips integration tests if the required environment variables
    (`GFW_API_BASE_URL` and `GFW_API_ACCESS_TOKEN`) are not set or are invalid.

    Args:
        item (pytest.Item):
            The pytest test item.

    Usage Examples:

    1. Mark a test as an integration test:

       ```python
       @pytest.mark.integration
       def test_example():

           # Perform integration test
           # ...

       ```

    2. Run integration tests only (if configured):

       ```bash
       pytest -m "integration"
       ```

    3. Run tests that are NOT integration:

       ```bash
       pytest -m "not integration"
       ```

    See: https://docs.pytest.org/en/stable/reference/reference.html#pytest.hookspec.pytest_runtest_setup
    """
    base_url = os.environ.get("GFW_API_BASE_URL", "").strip()
    access_token = os.environ.get("GFW_API_ACCESS_TOKEN", "").strip()
    is_integration_env = (
        bool(base_url)
        and bool(access_token)
        and "mock" not in base_url
        and "mock" not in access_token
    )

    if "integration" in item.keywords and not is_integration_env:
        pytest.skip(
            "Skipping: `GFW_API_BASE_URL` or `GFW_API_ACCESS_TOKEN` is missing or invalid."
        )
