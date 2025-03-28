"""Global Fishing Watch (GFW) API Python Client - Exceptions.

This module defines exception classes for errors raised by the GFW API client.
These exceptions provide structured error handling when interacting with the API.

Available Exceptions:
    - `GFWAPIClientError`: Base exception for all GFW API client errors.
    - `BaseUrlError`: Raised when no `base_url` is provided.
    - `AccessTokenError`: Raised when no `access_token` is provided.

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
from gfwapiclient.exceptions.client import AccessTokenError, BaseUrlError
from gfwapiclient.exceptions.validation import (
    ModelValidationError,
    RequestBodyValidationError,
    RequestParamsValidationError,
    ResultItemValidationError,
)


__all__ = [
    "AccessTokenError",
    "BaseUrlError",
    "GFWAPIClientError",
    "ModelValidationError",
    "RequestBodyValidationError",
    "RequestParamsValidationError",
    "ResultItemValidationError",
]
