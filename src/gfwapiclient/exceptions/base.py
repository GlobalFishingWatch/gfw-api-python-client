"""Global Fishing Watch (GFW) API Python Client - Base Exceptions."""

from typing import Final, Optional


__all__ = [
    "GFWAPIClientError",
]

GFW_API_CLIENT_ERROR_MESSAGE: Final[str] = "An error occurred."


class GFWAPIClientError(Exception):
    """Base exception for errors related to the GFW API client.

    This exception serves as the parent class for all errors raised by the
    `gfwapiclient` package, making it useful for broad exception handling.

    Attributes:
        message (str):
            The error message.

    Example:
        ```python
        from gfwapiclient.exceptions import GFWAPIClientError

        try:
            raise GFWAPIClientError("An unexpected error occurred.")
        except GFWAPIClientError as exc:
            print(f"GFW Exception: {exc}")
        ```
    """

    def __init__(self, message: Optional[str] = None) -> None:
        """Initialize a new `GFWAPIClientError` exception.

        Args:
            message (Optional[str], default=None):
                Error message describing the exception.
        """
        _message: str = message or GFW_API_CLIENT_ERROR_MESSAGE
        super().__init__(_message)
        self.message: str = _message

    def __str__(self) -> str:
        """Return a string representation of the error."""
        return self.message

    def __repr__(self) -> str:
        """Return the canonical string representation of the error."""
        return f"{self.__class__.__name__}({self.message!r})"
