"""Tests for `gfwapiclient.exceptions.client`."""

import pytest

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.exceptions.client import (
    ACCESS_TOKEN_ERROR_MESSAGE,
    BASE_URL_ERROR_MESSAGE,
    AccessTokenError,
    BaseUrlError,
)


# BaseUrlError


def test_base_url_error_inheritance() -> None:
    """Test that `BaseUrlError` is a subclass of `GFWAPIClientError`."""
    assert issubclass(BaseUrlError, GFWAPIClientError)
    assert issubclass(BaseUrlError, Exception)


def test_base_url_error_instance() -> None:
    """Test that `BaseUrlError` can be instantiated."""
    error = BaseUrlError()
    assert isinstance(error, BaseUrlError)
    assert isinstance(error, GFWAPIClientError)
    assert isinstance(error, Exception)
    assert str(error) == BASE_URL_ERROR_MESSAGE
    assert repr(error) == f"BaseUrlError('{BASE_URL_ERROR_MESSAGE}')"


def test_base_url_error_raises() -> None:
    """Test that `BaseUrlError` raises properly."""
    with pytest.raises(BaseUrlError, match="The `base_url` must be provided"):
        raise BaseUrlError()


# AccessTokenError


def test_access_token_error_inheritance() -> None:
    """Test that `AccessTokenError` is a subclass of `GFWAPIClientError`."""
    assert issubclass(AccessTokenError, GFWAPIClientError)
    assert issubclass(AccessTokenError, Exception)


def test_access_token_error_instance() -> None:
    """Test that `AccessTokenError` can be instantiated."""
    error = AccessTokenError()
    assert isinstance(error, AccessTokenError)
    assert isinstance(error, GFWAPIClientError)
    assert isinstance(error, Exception)
    assert str(error) == ACCESS_TOKEN_ERROR_MESSAGE
    assert repr(error) == f"AccessTokenError('{ACCESS_TOKEN_ERROR_MESSAGE}')"


def test_access_token_error_raises() -> None:
    """Test that `AccessTokenError` raises properly."""
    with pytest.raises(AccessTokenError, match="The `access_token` must be provided"):
        raise AccessTokenError()
