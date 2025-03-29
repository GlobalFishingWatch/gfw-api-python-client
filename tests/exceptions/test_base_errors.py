"""Tests for `gfwapiclient.exceptions.base.GFWAPIClientError`."""

import pytest

from gfwapiclient.exceptions.base import GFW_API_CLIENT_ERROR_MESSAGE, GFWAPIClientError


def test_gfw_api_client_error_inheritance() -> None:
    """Test that `GFWAPIClientError` is a subclass of `Exception`."""
    assert issubclass(GFWAPIClientError, Exception)


def test_gfw_api_client_error_instance_with_message() -> None:
    """Test that `GFWAPIClientError` can be instantiated with a custom error message."""
    error = GFWAPIClientError("Connection error.")
    assert isinstance(error, GFWAPIClientError)
    assert isinstance(error, Exception)
    assert str(error) == "Connection error."
    assert repr(error) == "GFWAPIClientError('Connection error.')"


def test_gfw_api_client_error_instance_with_no_message() -> None:
    """Test that `GFWAPIClientError` can be instantiated with no custom error message."""
    error = GFWAPIClientError()
    assert isinstance(error, GFWAPIClientError)
    assert isinstance(error, Exception)
    assert str(error) == GFW_API_CLIENT_ERROR_MESSAGE
    assert repr(error) == f"GFWAPIClientError('{GFW_API_CLIENT_ERROR_MESSAGE}')"


def test_gfw_api_client_error_raises() -> None:
    """Test that `GFWAPIClientError` raises properly."""
    with pytest.raises(GFWAPIClientError, match="Connection error"):
        raise GFWAPIClientError("Connection error")
