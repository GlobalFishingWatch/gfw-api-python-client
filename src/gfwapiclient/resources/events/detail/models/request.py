"""Global Fishing Watch (GFW) API Python Client - Get one by Event ID API Request Models."""

from typing import Final

from pydantic import Field

from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.events.base.models.request import EventDataset


__all__ = ["EventDetailParams"]

EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Get one by Event ID request parameters validation failed."
)


class EventDetailParams(RequestParams):
    """Request query parameters for retrieving an event by its ID.

    Attributes:
        dataset (EventDataset):
            Dataset to search for the event.

        raw (Optional[bool]):
            Whether to return the raw content of the event without parsing. Defaults to `False`.
    """

    dataset: EventDataset = Field(...)
