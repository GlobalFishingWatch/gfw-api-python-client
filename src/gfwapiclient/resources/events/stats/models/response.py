"""Global Fishing Watch (GFW) API Python Client - Events Statistics API Response Models."""

import datetime

from typing import List, Optional, Type

from pydantic import BaseModel, Field

from gfwapiclient.http.models import Result, ResultItem


__all__ = ["EventStatsItem", "EventStatsResult"]


class EventStatsTimeSeries(BaseModel):
    """Time series data for event statistics.

    Attributes:
        date (Optional[datetime.datetime]):
            Date and time of the data point.

        value (Optional[int]):
            Number of events at the given date and time.
    """

    date: Optional[datetime.datetime] = Field(None)
    value: Optional[int] = Field(None)


class EventStatsItem(ResultItem):
    """Event statistics result item.

    Attributes:
        num_events (Optional[int]):
            Total number of events.

        num_flags (Optional[int]):
            Number of distinct vessel flags.

        num_vessels (Optional[int]):
            Number of distinct vessels.

        flags (Optional[List[str]]):
            List of distinct vessel flags.

        timeseries (Optional[List[EventStatsTimeSeries]]):
            Time series data of event counts.
    """

    num_events: Optional[int] = Field(None, alias="numEvents")
    num_flags: Optional[int] = Field(None, alias="numFlags")
    num_vessels: Optional[int] = Field(None, alias="numVessels")
    flags: Optional[List[str]] = Field(None, alias="flags")
    timeseries: Optional[List[EventStatsTimeSeries]] = Field(None, alias="timeseries")


class EventStatsResult(Result[EventStatsItem]):
    """Result containing event statistics."""

    _result_item_class: Type[EventStatsItem]
    _data: EventStatsItem

    def __init__(self, data: EventStatsItem) -> None:
        """Initializes a new `EventStatsResult` instance.

        Args:
            data (EventStatsItem):
               The event statistics data.
        """
        super().__init__(data=data)
