"""Global Fishing Watch (GFW) API Python Client - HTTP Exceptions."""

from typing import Literal

import httpx

from gfwapiclient.exceptions.base import APIConnectionError, APIStatusError


__all__ = [
    "APITimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "InternalServerError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitError",
    "UnprocessableEntityError",
]


class APITimeoutError(APIConnectionError):
    """Raised when a request times out."""

    def __init__(self, request: httpx.Request) -> None:
        """Initialize a new `APITimeoutError` exception."""
        super().__init__(message="Request timed out.", request=request)


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

    pass
