"""Tests for `gfwapiclient.exceptions.base.GFWError`."""

import pytest

from gfwapiclient.exceptions.base import GFWError


def test_gfw_error_inheritance() -> None:
    """Test that GFWError is a subclass of Exception."""
    assert issubclass(GFWError, Exception)


def test_gfw_error_instance() -> None:
    """Test that GFWError can be instantiated."""
    error = GFWError("Connection error")
    assert isinstance(error, GFWError)
    assert isinstance(error, Exception)
    assert str(error) == "Connection error"


def test_gfw_error_raises() -> None:
    """Test that GFWError raises properly."""
    with pytest.raises(GFWError, match="Connection error"):
        raise GFWError("Connection error")
