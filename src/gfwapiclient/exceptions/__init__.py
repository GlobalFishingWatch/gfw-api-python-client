"""Global Fishing Watch (GFW) API Python Client - Exceptions.

This module defines the exception classes for errors raised by the GFW API client.
These exceptions provide structured error handling when interacting with the API.

Available Exceptions:
    - `GFWError`: Base exception for all GFW API client errors.

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


__all__ = ["GFWError"]
