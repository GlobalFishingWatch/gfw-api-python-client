"""Global Fishing Watch (GFW) API Python Client - Get All Events API Response Models."""

from typing import List, Type

from gfwapiclient.resources.events.base.models.response import EventItem, EventResult


__all__ = ["EventListItem", "EventListResult"]


class EventListItem(EventItem):
    """Result item for retrieving a list of events."""

    pass


class EventListResult(EventResult[EventListItem]):
    """Result containing a list of event items."""

    _result_item_class: Type[EventListItem]
    _data: List[EventListItem]

    def __init__(self, data: List[EventListItem]) -> None:
        """Initializes a new `EventListResult` instance.

        Args:
            data (List[EventListItem]):
                The list of event items.
        """
        super().__init__(data=data)
