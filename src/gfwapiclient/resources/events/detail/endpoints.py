"""Global Fishing Watch (GFW) API Python Client - Event Detail API EndPoint."""

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
    GetEndPoint[
        EventDetailParams,
        RequestBody,
        EventDetailItem,
        EventDetailResult,
    ],
):
    """Get event by id API endpoint."""

    def __init__(
        self,
        event_id: str,
        request_params: EventDetailParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `EventDetailEndPoint` API endpoint."""
        super().__init__(
            path=f"events/{event_id}",
            request_params=request_params,
            result_item_class=EventDetailItem,
            result_class=EventDetailResult,
            http_client=http_client,
        )
