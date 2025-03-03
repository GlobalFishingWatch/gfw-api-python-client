"""Global Fishing Watch (GFW) API Python Client - HTTP Resource."""

from gfwapiclient.http.client import HTTPClient


__all__ = ["BaseResource"]


class BaseResource:
    """Base API resource."""

    def __init__(
        self,
        http_client: HTTPClient,
    ) -> None:
        """Initialize an API endpoint.

        Args:
            http_client (HTTPClient):
                The HTTP client to send requests.
        """
        self._http_client = http_client
