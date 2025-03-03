"""Global Fishing Watch (GFW) API Python Client - Events Statistics Response Models."""

import datetime

from typing import List, Optional, Type

from pydantic import BaseModel, Field

from gfwapiclient.http.models import Result, ResultItem


__all__ = ["EventStatsItem", "EventStatsResult"]


class EventStatsTimeSeries(BaseModel):
    """Events stats timeseries."""

    date: Optional[datetime.datetime] = Field(None, description="Date.")
    value: Optional[int] = Field(None, description="Number of events.")


class EventStatsItem(ResultItem):
    """Event statistics."""

    num_events: Optional[int] = Field(
        None, description="Number of events.", alias="numEvents"
    )
    num_flags: Optional[int] = Field(
        None, description="Number of distinct vessel flags.", alias="numFlags"
    )
    num_vessels: Optional[int] = Field(
        None, description="Number of distinct vessels.", alias="numVessels"
    )
    flags: Optional[List[str]] = Field(
        None, description="Distinct flags.", alias="flags"
    )
    timeseries: Optional[List[EventStatsTimeSeries]] = Field(
        None, description="Timeseries.", alias="timeseries"
    )


class EventStatsResult(Result[EventStatsItem]):
    """Result for Event Stats API endpoint."""

    _result_item_class: Type[EventStatsItem]
    _data: EventStatsItem

    def __init__(self, data: EventStatsItem) -> None:
        """Initializes a new `EventStatsResult`."""
        self._data = data
