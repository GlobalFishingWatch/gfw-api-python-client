"""Global Fishing Watch (GFW) API Python Client - Get one by Event ID API Response Models."""

from typing import Type

from gfwapiclient.resources.events.base.models.response import EventItem, EventResult


__all__ = ["EventDetailItem", "EventDetailResult"]


class EventDetailItem(EventItem):
    """Result item for retrieving an event by its ID."""

    pass


class EventDetailResult(EventResult[EventDetailItem]):
    """Result containing the details of a single event."""

    _result_item_class: Type[EventDetailItem]
    _data: EventDetailItem

    def __init__(self, data: EventDetailItem) -> None:
        """Initializes a new `EventDetailResult` instance.

        Args:
            data (EventDetailItem):
                The event details.
        """
        super().__init__(data=data)
