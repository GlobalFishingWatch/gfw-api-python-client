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

from gfwapiclient.exceptions.base import (
    APIConnectionError,
    APIResponseValidationError,
    APIStatusError,
    GFWError,
)
from gfwapiclient.exceptions.client import AccessTokenError, BaseUrlError
from gfwapiclient.exceptions.http import (
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
)


__all__ = [
    "APIConnectionError",
    "APIResponseValidationError",
    "APIStatusError",
    "APITimeoutError",
    "AccessTokenError",
    "AuthenticationError",
    "BadRequestError",
    "BaseUrlError",
    "ConflictError",
    "GFWError",
    "GFWError",
    "InternalServerError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "UnprocessableEntityError",
]
