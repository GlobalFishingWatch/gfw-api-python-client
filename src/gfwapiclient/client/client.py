"""Global Fishing Watch (GFW) API Python Client - Client."""

import os

from typing import Any, Final, Optional, Union

import httpx

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources import ReferenceResource


__all__ = ["Client"]


GFW_API_BASE_URL: Final[str] = "https://gateway.api.globalfishingwatch.org/v3/"


class Client:
    """Global Fishing Watch (GFW) API Client.

    This class serves as the main entry point for interacting with the GFW API.
    It encapsulates the HTTP client and resources, providing a unified interface
    for accessing GFW's data.

    For more details on the GFW API and available data, please refer to the
    official documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#introduction

    See: https://globalfishingwatch.org/our-apis/documentation#data-available

    Attributes:
        references (ReferenceResource):
            Access to the reference data resources.
    """

    _references: ReferenceResource

    def __init__(
        self,
        *,
        access_token: Optional[str] = None,
        base_url: Optional[str] = None,
        follow_redirects: Optional[bool] = True,
        timeout: Optional[float] = 60.0,
        connect_timeout: Optional[float] = 5.0,
        max_connections: Optional[int] = 100,
        max_keepalive_connections: Optional[int] = 20,
        max_redirects: Optional[int] = 2,
        **kwargs: Any,
    ) -> None:
        """Initializes a new Global Fishing Watch (GFW) API `Client` with specified configurations.

        Args:
            base_url (Optional[Union[str, httpx.URL]], default="https://gateway.api.globalfishingwatch.org/v3/"):
                The base URL for API requests. If not provided, the value is taken from
                the `GFW_API_BASE_URL` environment variable. Default to `"https://gateway.api.globalfishingwatch.org/v3/"`.

            access_token (Optional[str], default=None):
                The access token for API request authentication. If not provided, the value is taken from
                the `GFW_API_ACCESS_TOKEN` environment variable. Raises `AccessTokenError` if neither is set.

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
            AccessTokenError:
                If `access_token` is not provided and the `GFW_API_ACCESS_TOKEN` environment
                variable is also not set.
        """
        # Ensure a base URL is set, either via argument or environment variable
        # or use default.
        _base_url: Union[str, httpx.URL] = (
            base_url
            if base_url is not None
            else os.environ.get(
                "GFW_API_BASE_URL",
                GFW_API_BASE_URL,
            )
        )

        self._http_client = HTTPClient(
            base_url=_base_url,
            access_token=access_token,
            follow_redirects=follow_redirects,
            timeout=timeout,
            connect_timeout=connect_timeout,
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
            max_redirects=max_redirects,
            **kwargs,
        )

    @property
    def references(self) -> ReferenceResource:
        """References data API resource.

        Provides access to the reference data resources, specifically regions.

        Regions provide geographic data, such as Exclusive Economic Zones (EEZs),
        Marine Protected Areas (MPAs), and Regional Fisheries Management
        Organizations (RFMOs).

        For more details on the Regions API, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#regions

        Returns:
            ReferenceResource:
                The reference data resource instance.
        """
        if not hasattr(self, "_references"):
            self._references = ReferenceResource(http_client=self._http_client)
        return self._references
