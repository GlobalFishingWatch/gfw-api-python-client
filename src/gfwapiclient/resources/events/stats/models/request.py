"""Global Fishing Watch (GFW) API Python Client - Events Statistics API Request Models."""

from enum import Enum
from typing import Final, List, Optional

from pydantic import Field

from gfwapiclient.resources.events.base.models.request import EventBaseBody


__all__ = ["EventStatsBody"]

EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Get events statistics request body validation failed."
)


class EventStatsTimeSeriesInterval(str, Enum):
    """Granularity for time series event statistics."""

    HOUR = "HOUR"
    DAY = "DAY"
    MONTH = "MONTH"
    YEAR = "YEAR"


class EventStatsInclude(str, Enum):
    """Additional information to include in event statistics."""

    TOTAL_COUNT = "TOTAL_COUNT"
    TIME_SERIES = "TIME_SERIES"


class EventStatsBody(EventBaseBody):
    """Request body for retrieving event statistics.

    Attributes:
        timeseries_interval (Optional[EventStatsTimeSeriesInterval]):
            Granularity of the time series data.

        includes (Optional[List[EventStatsInclude]]):
            List of additional information to include in the response.
    """

    timeseries_interval: Optional[EventStatsTimeSeriesInterval] = Field(None)
    includes: Optional[List[EventStatsInclude]] = Field(None)
