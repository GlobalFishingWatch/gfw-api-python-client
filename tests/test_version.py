"""Tests for `gfwapiclient.__version__`."""

import gfwapiclient


def test_version_exists() -> None:
    """Tests that `__version__` exists."""
    assert hasattr(gfwapiclient, "__version__")  # exists
    assert gfwapiclient.__version__ is not None  # not none
    assert isinstance(gfwapiclient.__version__, str)  # is string
    assert gfwapiclient.__version__  # not empty


def test_version_is_valid_semantic_version() -> None:
    """Tests that `__version__` is a valid semantic version."""
    version_parts = gfwapiclient.__version__.split(".")
    assert len(version_parts) == 3
    assert all(part.isdigit() for part in version_parts)

    major, minor, patch = map(int, version_parts)

    assert major >= 0
    assert minor >= 0
    assert patch >= 0


def test_version_is_consistent_across_imports() -> None:
    """Tests that `__version__` is consistent across multiple imports."""
    import gfwapiclient as gfw1
    import gfwapiclient as gfw2

    assert gfw1.__version__ == gfw2.__version__
