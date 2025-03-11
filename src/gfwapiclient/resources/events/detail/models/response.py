"""Global Fishing Watch (GFW) API Python Client - Event Detail API Response Models."""

from typing import Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.events.base.response import EventItem


__all__ = ["EventDetailItem", "EventDetailResult"]


class EventDetailItem(EventItem):
    """Result item for get event by id API endpoint."""

    pass


class EventDetailResult(Result[EventDetailItem]):
    """Result for get event by id API endpoint."""

    _result_item_class: Type[EventDetailItem]
    _data: EventDetailItem

    def __init__(self, data: EventDetailItem) -> None:
        """Initializes a new `EventDetailResult`."""
        self._data = data
