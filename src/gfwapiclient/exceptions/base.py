"""Global Fishing Watch (GFW) API Python Client - Base Exceptions."""

from typing import Optional

import httpx


__all__ = [
    "APIConnectionError",
    "APIError",
    "APIResponseValidationError",
    "APIStatusError",
    "GFWError",
]


class GFWError(Exception):
    """Base exception for errors related to the GFW API client.

    This exception serves as the parent class for all errors raised by the
    `gfwapiclient` package, making it useful for broad exception handling.

    Attributes:
        message (str):
            The error message.

    Example:
        ```python
        from gfwapiclient.exceptions import GFWError

        try:
            raise GFWError("An unexpected error occurred.")
        except GFWError as exc:
            print(f"GFW Exception: {exc}")
        ```
    """

    def __init__(self, message: Optional[str] = None) -> None:
        """Initialize a new `GFWError` exception.

        Args:
            message (Optional[str], default=None):
                Error message describing the exception.
        """
        super().__init__(message or "An error occurred")
        self.message: str = message or "An error occurred"

    def __str__(self) -> str:
        """Return a string representation of the error."""
        return self.message

    def __repr__(self) -> str:
        """Return the canonical string representation of the error."""
        return f"{self.__class__.__name__}({self.message!r})"


class APIError(GFWError):
    """Base class for general API errors.

    `body` is API response body.

    If the API responded with a valid JSON structure then `body` will be the
    decoded result.

    If it isn't a valid JSON structure then `body` will be the raw response.

    If there was no response associated with this error then it will be `None`.

    See: https://globalfishingwatch.org/our-apis/documentation#errors-codes
    """

    message: str
    request: httpx.Request
    body: Optional[object] = None

    def __init__(
        self,
        message: str,
        request: httpx.Request,
        *,
        body: Optional[object] = None,
    ) -> None:
        """Initialize a new `APIError` exception."""
        super().__init__(message)
        self.request = request
        self.message = message
        self.body = body


class APIConnectionError(APIError):
    """Raised when a connection error occurs."""

    def __init__(
        self,
        *,
        message: str = "Connection error.",
        request: httpx.Request,
    ) -> None:
        """Initialize a new `APIError` exception."""
        super().__init__(message, request, body=None)


class APIResponseValidationError(APIError):
    """Raised when an API response data is invalid for expected schema."""

    response: httpx.Response
    status_code: int

    def __init__(
        self,
        response: httpx.Response,
        body: Optional[object] = None,
        *,
        message: Optional[str] = None,
    ) -> None:
        """Initialize a new `APIResponseValidationError` exception."""
        super().__init__(
            message or "Data returned by API invalid for expected schema.",
            response.request,
            body=body,
        )
        self.response = response
        self.status_code = response.status_code


class APIStatusError(APIError):
    """Raised when an API response has a status code of 4xx or 5xx."""

    response: httpx.Response
    status_code: int

    def __init__(
        self,
        message: str,
        *,
        response: httpx.Response,
        body: Optional[object] = None,
    ) -> None:
        """Initialize a new `APIStatusError` exception."""
        super().__init__(message, response.request, body=body)
        self.response = response
        self.status_code = response.status_code
