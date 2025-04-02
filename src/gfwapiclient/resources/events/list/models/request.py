"""Global Fishing Watch (GFW) API Python Client - Get All Events API Request Models."""

from typing import Final, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.events.base.models.request import EventBaseBody


__all__ = ["EventListBody", "EventListParams"]

EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Get All Events request parameters validation failed."
)

EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Get All Events request body validation failed."
)


class EventListParams(RequestParams):
    """Request query parameters for retrieving a list of events.

    Attributes:
        limit (Optional[int]):
            Maximum number of events to return.
            Defaults to `99999`.

        offset (Optional[int]):
            Number of events to skip before returning results.
            Used for pagination. Defaults to `0`.

        sort (Optional[str]):
            Property to sort the events by. Depends on the dataset.
    """

    limit: Optional[int] = Field(99999, ge=0)
    offset: Optional[int] = Field(0, ge=0)
    sort: Optional[str] = Field(None)


class EventListBody(EventBaseBody):
    """Request body for retrieving a list of events.

    This request body contains the filtering criteria for the events.
    """

    pass
