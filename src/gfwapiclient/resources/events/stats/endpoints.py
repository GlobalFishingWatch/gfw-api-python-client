"""Global Fishing Watch (GFW) API Python Client - Events Statistics API Endpoints."""

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
    PostEndPoint[RequestParams, EventStatsBody, EventStatsItem, EventStatsResult]
):
    """Get Events Statistics API endpoint.

    This endpoint allows you to retrieve statistical information about events
    based on specified request body parameters.
    """

    def __init__(
        self,
        *,
        request_body: EventStatsBody,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `EventStatsEndPoint` API endpoint.

        Args:
            request_body (EventStatsBody):
                The request body containing the statistics parameters.

            http_client (HTTPClient):
                The HTTP client.
        """
        super().__init__(
            path="events/stats",
            request_params=None,
            request_body=request_body,
            result_item_class=EventStatsItem,
            result_class=EventStatsResult,
            http_client=http_client,
        )
