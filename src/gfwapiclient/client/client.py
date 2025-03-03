"""Global Fishing Watch (GFW) API Python Client - Base Client."""

from typing import Any, Optional

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.events.resources import EventResource
from gfwapiclient.resources.insights.resources import InsightResource
from gfwapiclient.resources.references.resources import ReferenceResource


__all__ = ["Client"]


class Client:
    """Global Fishing Watch (GFW) API client."""

    _events: EventResource
    _insights: InsightResource
    _references: ReferenceResource

    def __init__(
        self,
        api_base_url: Optional[str] = None,
        api_access_token: Optional[str] = None,
        *,
        follow_redirects: Optional[bool] = True,
        timeout: Optional[float] = 60.0,
        connect_timeout: Optional[float] = 5.0,
        max_connections: Optional[int] = 100,
        max_keepalive_connections: Optional[int] = 20,
        max_redirects: Optional[int] = 2,
        **kwargs: Any,
    ) -> None:
        """Construct a new `BaseClient` instance."""
        self._http_client = HTTPClient(
            base_url=api_base_url,
            access_token=api_access_token,
            follow_redirects=follow_redirects,
            timeout=timeout,
            connect_timeout=connect_timeout,
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
            max_redirects=max_redirects,
            **kwargs,
        )

    @property
    def events(self) -> EventResource:
        """Events data API resource."""
        if not hasattr(self, "_events"):
            self._events = EventResource(http_client=self._http_client)
        return self._events

    @property
    def insights(self) -> InsightResource:
        """Insights data API resource."""
        if not hasattr(self, "_insights"):
            self._insights = InsightResource(http_client=self._http_client)
        return self._insights

    @property
    def references(self) -> ReferenceResource:
        """References data API resource."""
        if not hasattr(self, "_references"):
            self._references = ReferenceResource(http_client=self._http_client)
        return self._references

    # TODO: shortcuts
    # TODO: flows
