"""Global Fishing Watch (GFW) API Python Client - HTTP Resource."""

from gfwapiclient.http.client import HTTPClient


__all__ = ["BaseResource"]


class BaseResource:
    """Base class for API resources.

    This class provides a foundation for interacting with specific API resources,
    encapsulating the endpoints and offering methods to define and execute
    API requests.
    """

    _http_client: HTTPClient

    def __init__(
        self,
        *,
        http_client: HTTPClient,
    ) -> None:
        """Initialize a new `BaseResource`.

        Args:
            http_client (HTTPClient):
                The HTTP client to send requests.
        """
        self._http_client = http_client
