"""Global Fishing Watch (GFW) API Python Client - HTTP Client."""

import os

from typing import Any, Optional, Union

import httpx

from gfwapiclient.exceptions.base import GFWError


__all__ = ["HttpClient"]


class HttpClient(httpx.AsyncClient):
    """An asynchronous HTTP client for interacting with the GFW API.

    This client extends `httpx.AsyncClient` and provides features such as connection pooling,
    HTTP/2 support, automatic redirects, and configurable timeouts.
    """

    def __init__(
        self,
        base_url: Union[str, httpx.URL, None] = None,
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
            base_url (Union[str, httpx.URL, None]):
                The base URL for the API. If not provided, it will be taken from the `GFW_API_BASE_URL`
                environment variable. Raises `GFWError` if neither is set.

            follow_redirects (Optional[bool], default=True):
                Whether the client should automatically follow redirects.

            timeout (Optional[float], default=60.0):
                The total timeout (in seconds) for API requests.

            connect_timeout (Optional[float], default=5.0):
                Timeout (in seconds) for establishing a connection.

            max_connections (Optional[int], default=100):
                Maximum number of concurrent connections.

            max_keepalive_connections (Optional[int], default=20):
                Maximum number of keep-alive connections in the connection pool.
                Should not exceed `max_connections`.

            max_redirects (Optional[int], default=2):
                Maximum number of redirects to follow before raising an error.

            **kwargs (Any):
                Additional parameters passed to `httpx.AsyncClient`.

        Raises:
            GFWError: If `base_url` is not provided and is not set via the `GFW_API_BASE_URL` environment variable.
        """
        # Ensure a base URL is set, either via argument or environment variable
        _base_url = base_url or os.getenv("GFW_API_BASE_URL", default=None)
        if not _base_url:
            raise GFWError(
                "The `base_url` must be provided either as an argument "
                "or set via the `GFW_API_BASE_URL` environment variable."
            )

        # Configure timeout settings
        _timeout = httpx.Timeout(timeout=timeout, connect=connect_timeout)

        # Configure connection limits
        _limits = httpx.Limits(
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
        )

        # Set default arguments if not provided in **kwargs
        kwargs.setdefault("base_url", _base_url)
        kwargs.setdefault("follow_redirects", follow_redirects)
        kwargs.setdefault("timeout", _timeout)
        kwargs.setdefault("limits", _limits)
        kwargs.setdefault("max_redirects", max_redirects)

        super().__init__(**kwargs)
