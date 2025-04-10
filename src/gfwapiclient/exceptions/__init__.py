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
from gfwapiclient.exceptions.http import (
    APIConnectionError,
    APIError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadGatewayError,
    BadRequestError,
    ConflictError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    RequestTimeoutError,
    ServiceUnavailableError,
    UnprocessableEntityError,
)
from gfwapiclient.exceptions.validation import (
    ModelValidationError,
    RequestBodyValidationError,
    RequestParamsValidationError,
    ResultItemValidationError,
    ResultValidationError,
)


__all__ = [
    "APIConnectionError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "AccessTokenError",
    "AuthenticationError",
    "BadGatewayError",
    "BadRequestError",
    "BaseUrlError",
    "ConflictError",
    "GFWAPIClientError",
    "GatewayTimeoutError",
    "InternalServerError",
    "ModelValidationError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "RequestBodyValidationError",
    "RequestParamsValidationError",
    "RequestTimeoutError",
    "ResultItemValidationError",
    "ResultItemValidationError",
    "ResultValidationError",
    "ServiceUnavailableError",
    "UnprocessableEntityError",
]
