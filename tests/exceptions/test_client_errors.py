"""Tests for `gfwapiclient.exceptions.client`."""

import pytest

from gfwapiclient.exceptions.base import GFWError
from gfwapiclient.exceptions.client import BASE_URL_ERROR_MESSAGE, BaseUrlError


def test_base_url_error_inheritance() -> None:
    """Test that `BaseUrlError` is a subclass of `GFWError`."""
    assert issubclass(BaseUrlError, GFWError)
    assert issubclass(BaseUrlError, Exception)


def test_base_url_error_instance() -> None:
    """Test that `BaseUrlError` can be instantiated."""
    error = BaseUrlError()
    assert isinstance(error, BaseUrlError)
    assert isinstance(error, GFWError)
    assert isinstance(error, Exception)
    assert str(error) == BASE_URL_ERROR_MESSAGE
    assert repr(error) == f"BaseUrlError('{BASE_URL_ERROR_MESSAGE}')"


def test_base_url_error_raises() -> None:
    """Test that `BaseUrlError` raises properly."""
    with pytest.raises(BaseUrlError, match="The `base_url` must be provided"):
        raise BaseUrlError()
