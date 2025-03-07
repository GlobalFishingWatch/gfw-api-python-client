"""Global Fishing Watch (GFW) API Python Client - Events List API Response Models."""

from typing import List, Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.events.base.response import EventItem


__all__ = ["EventListItem", "EventListResult"]


class EventListItem(EventItem):
    """Result item for get all events API endpoint."""

    pass


class EventListResult(Result[EventListItem]):
    """Result for get all events API endpoint."""

    _result_item_class: Type[EventListItem]
    _data: List[EventListItem]

    def __init__(self, data: List[EventListItem]) -> None:
        """Initializes a new `EventListResult`."""
        self._data = data
