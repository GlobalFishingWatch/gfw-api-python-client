"""Global Fishing Watch (GFW) API Python Client - Client Exceptions."""

from typing import Final

from gfwapiclient.exceptions.base import GFWAPIClientError


__all__ = ["AccessTokenError", "BaseUrlError"]


BASE_URL_ERROR_MESSAGE: Final[str] = (
    "The `base_url` must be provided either as an argument "
    "or set via the `GFW_API_BASE_URL` environment variable."
)


ACCESS_TOKEN_ERROR_MESSAGE: Final[str] = (
    "The `access_token` must be provided either as an argument "
    "or set via the `GFW_API_ACCESS_TOKEN` environment variable."
)


class BaseUrlError(GFWAPIClientError):
    """Exception raised when no `base_url` is provided for the API client.

    This error occurs if the `base_url` is not explicitly provided
    during `HTTPClient` initialization and is also missing from the
    environment variable `GFW_API_BASE_URL`.

    Example:
        ```python
        from gfwapiclient.exceptions import BaseUrlError

        try:
            raise BaseUrlError()
        except BaseUrlError as exc:
            print(f"GFW Exception: {exc}")
        ```
    """

    def __init__(self) -> None:
        """Initialize a new `BaseUrlError` with a predefined error message."""
        super().__init__(BASE_URL_ERROR_MESSAGE)


class AccessTokenError(GFWAPIClientError):
    """Exception raised when no `access_token` is provided for the API client.

    This error occurs if the `access_token` is not explicitly provided
    during `HTTPClient` initialization and is also missing from the
    environment variable `GFW_API_ACCESS_TOKEN`.

    Example:
        ```python
        from gfwapiclient.exceptions import AccessTokenError

        try:
            raise AccessTokenError()
        except AccessTokenError as exc:
            print(f"GFW Exception: {exc}")
        ```
    """

    def __init__(self) -> None:
        """Initialize a new `AccessTokenError` with a predefined error message."""
        super().__init__(ACCESS_TOKEN_ERROR_MESSAGE)
