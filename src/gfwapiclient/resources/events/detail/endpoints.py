"""Global Fishing Watch (GFW) API Python Client - Get one by Event ID API Endpoint."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import GetEndPoint
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.events.detail.models.request import EventDetailParams
from gfwapiclient.resources.events.detail.models.response import (
    EventDetailItem,
    EventDetailResult,
)


__all__ = ["EventDetailEndPoint"]


class EventDetailEndPoint(
    GetEndPoint[EventDetailParams, RequestBody, EventDetailItem, EventDetailResult]
):
    """Get one by Event ID API endpoint.

    This endpoint allows you to retrieve detailed information about a specific
    event using its unique ID.
    """

    def __init__(
        self,
        *,
        event_id: str,
        request_params: EventDetailParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `EventDetailEndPoint` API endpoint.

        Args:
            event_id (str):
                The ID of the event to retrieve.

            request_params (EventDetailParams):
                The request parameters.

            http_client (HTTPClient):
                The HTTP client.
        """
        super().__init__(
            path=f"events/{event_id}",
            request_params=request_params,
            result_item_class=EventDetailItem,
            result_class=EventDetailResult,
            http_client=http_client,
        )
