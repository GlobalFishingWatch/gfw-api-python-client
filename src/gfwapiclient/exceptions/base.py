"""Global Fishing Watch (GFW) API Python Client - Base Exceptions."""

from typing import Optional


__all__ = [
    "GFWAPIClientError",
]


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
        super().__init__(message or "An error occurred")
        self.message: str = message or "An error occurred."

    def __str__(self) -> str:
        """Return a string representation of the error."""
        return self.message

    def __repr__(self) -> str:
        """Return the canonical string representation of the error."""
        return f"{self.__class__.__name__}({self.message!r})"
