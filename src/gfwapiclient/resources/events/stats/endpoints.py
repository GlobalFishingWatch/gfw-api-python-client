"""Global Fishing Watch (GFW) API Python Client - Event Stats API EndPoints."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import PostEndPoint
from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.events.stats.models.request import EventStatsBody
from gfwapiclient.resources.events.stats.models.response import (
    EventStatsItem,
    EventStatsResult,
)


__all__ = ["EventStatsEndPoint"]


class EventStatsEndPoint(
    PostEndPoint[RequestParams, EventStatsBody, EventStatsItem, EventStatsResult],
):
    """Get Event Stats API endpoint."""

    def __init__(
        self,
        request_body: EventStatsBody,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `EventStatsEndPoint` API endpoint."""
        super().__init__(
            path="events/stats",
            request_params=None,
            request_body=request_body,
            result_item_class=EventStatsItem,
            result_class=EventStatsResult,
            http_client=http_client,
        )
