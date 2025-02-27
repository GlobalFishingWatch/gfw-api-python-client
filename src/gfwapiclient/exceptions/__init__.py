"""Global Fishing Watch (GFW) API Python Client - Exceptions.

This module defines exception classes for errors raised by the GFW API client.
These exceptions provide structured error handling when interacting with the API.

Available Exceptions:
    - `GFWError`: Base exception for all GFW API client errors.
    - `BaseUrlError`: Raised when no `base_url` is provided.

Example:
    ```python
    from gfwapiclient.exceptions import GFWError

    try:
        raise GFWError("An unexpected error occurred.")
    except GFWError as exc:
        print(f"GFW Exception: {exc}")
    ```
"""

from gfwapiclient.exceptions.base import GFWError
from gfwapiclient.exceptions.client import BaseUrlError


__all__ = ["BaseUrlError", "GFWError"]
