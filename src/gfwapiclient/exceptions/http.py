"""Global Fishing Watch (GFW) API Python Client - HTTP Exceptions.

This module defines custom exception classes for handling errors that occur
when interacting with the Global Fishing Watch API.

It includes:
- `APIError`: Base exception for general API errors.
- `APIStatusError`: Exception for HTTP 4xx and 5xx responses.
- `APIConnectionError`: Exception for network connection issues.
- `APITimeoutError`: Exception for request timeouts.
- Subclasses for specific HTTP status codes (e.g., `NotFoundError`, `RateLimitError`).
"""

from typing import Any, Final, Literal, Optional

import httpx

from gfwapiclient.exceptions.base import GFWAPIClientError


__all__ = [
    "APIConnectionError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "AuthenticationError",
    "BadGatewayError",
    "BadRequestError",
    "ConflictError",
    "GatewayTimeoutError",
    "InternalServerError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "RequestTimeoutError",
    "ServiceUnavailableError",
    "UnprocessableEntityError",
]

API_CONNECTION_ERROR_MESSAGE: Final[str] = "Connection error."
API_TIMEOUT_ERROR_MESSAGE: Final[str] = "Request timed out."


class APIError(GFWAPIClientError):
    """Base exception for general API errors.

    This exception represents general errors encountered while interacting
    with the Global Fishing Watch (GFW) API.

    Attributes:
        request (httpx.Request):
            The HTTP request that triggered the error.

        body (Optional[Any]):
            The API response body, if available.

            - If the API response is valid JSON, `body` contains the decoded JSON object.
            - If the response is not valid JSON, `body` contains the raw response content.
            - If no response is associated with the error, `body` is `None`.

    See Also:
        GFW API documentation on error codes:
        <https://globalfishingwatch.org/our-apis/documentation#errors-codes>
    """

    request: httpx.Request
    body: Optional[Any] = None

    def __init__(
        self,
        message: str,
        request: httpx.Request,
        *,
        body: Optional[Any] = None,
    ) -> None:
        """Initialize a new `APIError` exception.

        Args:
            message (str):
                The error message.

            request (httpx.Request):
                The HTTP request that caused the error.

            body (Optional[Any], default=None):
                The API response body, if available.
        """
        super().__init__(message)
        self.request = request
        self.body = body

    def __str__(self) -> str:
        """Return a string representation of the error."""
        _message: str = super().__str__()
        if self.body:
            _message = f"{_message} \nBody: {self.body}"
        return _message

    def __repr__(self) -> str:
        """Return the canonical string representation of the error."""
        return (
            f"{self.__class__.__name__}(message={self.message!r}, "
            f"request={self.request!r}, body={self.body!r})"
        )


class APIStatusError(APIError):
    """Exception raised for API HTTP response errors (4xx or 5xx).

    Attributes:
        response (httpx.Response):
            The HTTP response that caused the error.

        status_code (int):
            The HTTP status code of the response.
    """

    response: httpx.Response
    status_code: int

    def __init__(
        self,
        message: str,
        *,
        response: httpx.Response,
        body: Optional[Any] = None,
    ) -> None:
        """Initialize a new `APIStatusError` exception.

        Args:
            message (str):
                The error message.

            response (httpx.Response):
                The HTTP response that caused the error.

            body (Optional[Any], default=None):
                The API response body, if available.
        """
        super().__init__(message, response.request, body=body)
        self.response = response
        self.status_code = response.status_code

    def __repr__(self) -> str:
        """Return the canonical string representation of the error."""
        return (
            f"{self.__class__.__name__}(message={self.message!r}, "
            f"response={self.response!r}, body={self.body!r})"
        )


class APIConnectionError(APIError):
    """Exception raised when a connection error occurs."""

    def __init__(
        self,
        *,
        message: str = API_CONNECTION_ERROR_MESSAGE,
        request: httpx.Request,
    ) -> None:
        """Initialize a new `APIConnectionError` exception.

        Args:
            message (str):
                The error message.

            request (httpx.Request):
                The HTTP request that caused the error.
        """
        super().__init__(message, request, body=None)


class APITimeoutError(APIConnectionError):
    """Exception raised when a request times out."""

    def __init__(self, request: httpx.Request) -> None:
        """Initialize a new `APITimeoutError` exception.

        Args:
            request (httpx.Request):
                The HTTP request that timed out.
        """
        super().__init__(message=API_TIMEOUT_ERROR_MESSAGE, request=request)


class BadRequestError(APIStatusError):
    """400 Bad Request Error."""

    status_code: Literal[400] = 400


class AuthenticationError(APIStatusError):
    """401 Authentication Error."""

    status_code: Literal[401] = 401


class PermissionDeniedError(APIStatusError):
    """403 Permission Denied Error."""

    status_code: Literal[403] = 403


class NotFoundError(APIStatusError):
    """404 Not Found Error."""

    status_code: Literal[404] = 404


class RequestTimeoutError(APIStatusError):
    """408 Request Timeout Error."""

    status_code: Literal[408] = 408  # FIXME: is it same as httpx.TimeoutException


class ConflictError(APIStatusError):
    """409 Conflict Error."""

    status_code: Literal[409] = 409


class UnprocessableEntityError(APIStatusError):
    """422 Unprocessable Entity Error."""

    status_code: Literal[422] = 422


class RateLimitError(APIStatusError):
    """429 Too Many Requests (Rate Limit) Error."""

    status_code: Literal[429] = 429


class InternalServerError(APIStatusError):
    """500 Internal Server Error."""

    status_code: Literal[500] = 500


class BadGatewayError(APIStatusError):
    """502 Bad Gateway Error."""

    status_code: Literal[502] = 502


class ServiceUnavailableError(APIStatusError):
    """503 Service Unavailable Error."""

    status_code: Literal[503] = 503


class GatewayTimeoutError(APIStatusError):
    """504 Gateway Timeout Error."""

    status_code: Literal[504] = 504
