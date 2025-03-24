"""Global Fishing Watch (GFW) API Python Client - HTTP Client."""

import os

from types import TracebackType
from typing import Any, Optional, Self, Type, Union

import httpx

from gfwapiclient.exceptions.client import BaseUrlError


__all__ = ["HTTPClient"]


class HTTPClient(httpx.AsyncClient):
    """Asynchronous HTTP client for interacting with the Global Fishing Watch (GFW) API.

    This client extends `httpx.AsyncClient` and provides:
    - Connection pooling with configurable limits.
    - HTTP/2 support for better performance.
    - Automatic redirects with max limits.
    - Fine-grained control over timeouts.

    Example:
        ```python
        async with HTTPClient() as client:
            response = await client.get("/vessels")
            data = response.json()
        ```
    """

    def __init__(
        self,
        base_url: Optional[Union[str, httpx.URL]] = None,
        *,
        follow_redirects: Optional[bool] = True,
        timeout: Optional[float] = 60.0,
        connect_timeout: Optional[float] = 5.0,
        max_connections: Optional[int] = 100,
        max_keepalive_connections: Optional[int] = 20,
        max_redirects: Optional[int] = 2,
        **kwargs: Any,
    ) -> None:
        """Initializes a new `HttpClient` with specified configurations.

        Args:
            base_url (Optional[Union[str, httpx.URL]], default=None):
                The base URL for API requests. If not provided, the value is taken from
                the `GFW_API_BASE_URL` environment variable. Raises `BaseUrlError` if neither is set.

            follow_redirects (Optional[bool], default=True):
                Whether the client should automatically follow redirects.
                Defaults to `True`.

            timeout (Optional[float], default=60.0):
                The default timeout (in seconds) for all operations (`connect`, `read`, `pool`, etc.).
                Defaults to `60.0` seconds.

            connect_timeout (Optional[float], default=5.0):
                Timeout (in seconds) for establishing a connection.
                Defaults to `5.0` seconds.

            max_connections (Optional[int], default=100):
                Maximum number of concurrent connections.
                Defaults to `100`.

            max_keepalive_connections (Optional[int], default=20):
                Maximum number of keep-alive connections in the connection pool.
                Should not exceed `max_connections`. Defaults to `20`.

            max_redirects (Optional[int], default=2):
                Maximum number of redirects to follow before raising an error.
                Defaults to `2`.

            **kwargs (Any):
                Additional parameters passed to `httpx.AsyncClient`.

        Raises:
            BaseUrlError:
                If `base_url` is not provided and the `GFW_API_BASE_URL` environment
                variable is also not set.
        """
        # Ensure a base URL is set, either via argument or environment variable
        _base_url: Optional[Union[str, httpx.URL]] = base_url or os.getenv(
            "GFW_API_BASE_URL",
            default=None,
        )
        if not _base_url:
            raise BaseUrlError()

        # Configure operations timeout settings
        _timeout: httpx.Timeout = httpx.Timeout(
            timeout=timeout, connect=connect_timeout
        )

        # Configure connection limits
        _limits: httpx.Limits = httpx.Limits(
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
        )

        # Set default arguments if not explicitly provided in **kwargs
        kwargs.setdefault("base_url", _base_url)
        kwargs.setdefault("follow_redirects", follow_redirects)
        kwargs.setdefault("timeout", _timeout)
        kwargs.setdefault("limits", _limits)
        kwargs.setdefault("max_redirects", max_redirects)

        super().__init__(**kwargs)

    async def __aenter__(self) -> Self:
        """Enter the async context and return the client instance."""
        await super().__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        """Exit the async context, ensuring the client session is properly closed."""
        await super().__aexit__(exc_type, exc_value, traceback)
        await self.aclose()
