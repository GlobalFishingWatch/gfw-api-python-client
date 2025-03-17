"""Test configurations for `gfwapiclient`."""

import os

from typing import Final

import pytest
import respx

from respx.patterns import parse_url_patterns


MOCK_GFW_API_BASE_URL: Final[str] = (
    "https://gateway.api.mocking.globalfishingwatch.org/v3/"
)
MOCK_GFW_API_ACCESS_TOKEN: Final[str] = "mocking_GoXcgX1YFRRph48Rv6w9aGIDQzQd7zaB"


@pytest.fixture
def mock_base_url(monkeypatch: pytest.MonkeyPatch) -> None:
    """Sets a mock base URL for the Global Fishing Watch API.

    This fixture overrides the `GFW_API_BASE_URL` environment variable,
    ensuring that tests interact with a mocked API instead of the real one.

    Args:
        monkeypatch (pytest.MonkeyPatch):
            Pytest's built-in fixture for modifying environment variables.

    Example:
        ```python
        def test_example(mock_base_url: object):

            # Perform test
            # ...

        ```
    """
    monkeypatch.setenv("GFW_API_BASE_URL", MOCK_GFW_API_BASE_URL)


@pytest.fixture
def mock_access_token(monkeypatch: pytest.MonkeyPatch) -> None:
    """Sets a mock access token for the Global Fishing Watch API.

    This fixture overrides the `GFW_API_ACCESS_TOKEN` environment variable,
    preventing tests from requiring real authentication credentials.

    Args:
        monkeypatch (pytest.MonkeyPatch):
            Pytest's built-in fixture for modifying environment variables.

    Example:
        ```python
        def test_example(mock_access_token: object):

            # Perform test
            # ...

        ```
    """
    monkeypatch.setenv("GFW_API_ACCESS_TOKEN", MOCK_GFW_API_ACCESS_TOKEN)


@pytest.fixture
def mock_responsex(
    mock_base_url: object,
    mock_access_token: object,
    respx_mock: respx.MockRouter,
) -> respx.MockRouter:
    """Configures `respx` to intercept and mock HTTP requests to the API.

    This fixture ensures that all outgoing HTTP requests matching the
    `GFW_API_BASE_URL` pattern are intercepted by `respx`, allowing tests
    to define expected responses.

    Args:
        mock_base_url (object):
            Ensures the base URL environment variable is set before mocking.

        mock_access_token (object):
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
