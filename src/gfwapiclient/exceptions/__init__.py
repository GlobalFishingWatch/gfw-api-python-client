"""Global Fishing Watch (GFW) API Python Client - Exceptions.

This module defines exception classes for errors raised by the GFW API client.
These exceptions provide structured error handling when interacting with the API.

Available Exceptions:
    - `GFWAPIClientError`: Base exception for all GFW API client errors.
    - `BaseUrlError`: Raised when no `base_url` is provided.

Example:
    ```python
    from gfwapiclient.exceptions import GFWAPIClientError

    try:
        raise GFWAPIClientError("An unexpected error occurred.")
    except GFWAPIClientError as exc:
        print(f"GFW Exception: {exc}")
    ```
"""

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.exceptions.client import BaseUrlError


__all__ = ["BaseUrlError", "GFWAPIClientError"]
