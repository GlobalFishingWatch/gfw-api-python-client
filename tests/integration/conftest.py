"""Integration test configurations for `gfwapiclient`."""

import pytest

import gfwapiclient as gfw


@pytest.fixture
def gfw_client() -> gfw.Client:
    """Fixture for creating a `gfw.Client` instance for integration tests.

    This fixture initializes a `gfw.Client` instance, ensuring that it is
    configured with valid base URL and access token from environment variables.

    Returns:
        gfw.Client:
            An instance of `gfw.Client` ready for integration testing.

    Raises:
        AssertionError:
            If the base URL or access token is not set in environment variables.

    Example:
        ```python
        @pytest.mark.integration
        @pytest.mark.asyncio
        def test_integration_example(gfw_client: gfw.Client):

            # Use the gfw_client for integration testing
            # ...

        ```
    """
    gfw_client = gfw.Client()
    assert gfw_client._http_client.base_url is not None
    assert gfw_client._http_client._access_token is not None
    return gfw_client
