"""Test configurations for `gfwapiclient.http`."""

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
    """Fixture to set a mock base URL using an environment variable."""
    monkeypatch.setenv("GFW_API_BASE_URL", MOCK_GFW_API_BASE_URL)


@pytest.fixture
def mock_access_token(monkeypatch: pytest.MonkeyPatch) -> None:
    """Fixture to set a mock access token using an environment variable."""
    monkeypatch.setenv("GFW_API_ACCESS_TOKEN", MOCK_GFW_API_ACCESS_TOKEN)


@pytest.fixture
def mock_responsex(
    mock_base_url: object,
    respx_mock: respx.MockRouter,
) -> respx.MockRouter:
    """Fixture to set a `respx` with a `mock_base_url` for all tests."""
    _mock_base_url: str = os.environ.get(
        "GFW_API_BASE_URL", default=MOCK_GFW_API_BASE_URL
    )
    respx_mock._bases = parse_url_patterns(_mock_base_url, exact=False)
    assert respx_mock._bases is not None
    return respx_mock
