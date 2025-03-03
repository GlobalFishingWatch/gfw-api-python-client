"""Global Fishing Watch (GFW) API Python Client - Events API Resource."""

import datetime

from typing import Any, Dict, List, Optional

from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.events.models.request import EventDataset
from gfwapiclient.resources.events.stats.endpoints import EventStatsEndPoint
from gfwapiclient.resources.events.stats.models.request import (
    EventStatsBody,
    EventStatsTimeSeriesInterval,
)
from gfwapiclient.resources.events.stats.models.response import EventStatsResult


class EventResource(BaseResource):
    """Events data API resource."""

    async def aget_event_stats(
        self,
        datasets: List[EventDataset],
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        timeseries_interval: Optional[
            EventStatsTimeSeriesInterval
        ] = EventStatsTimeSeriesInterval.YEAR,
        duration: Optional[int] = 90,
        **kwargs: Dict[str, Any],
    ) -> EventStatsResult:
        """Asynchronously get events statistics data."""
        request_body = EventStatsBody(
            datasets=datasets,
            start_date=start_date,
            end_date=end_date,
            timeseries_interval=timeseries_interval,
            duration=duration,
        )  # type: ignore[call-arg]
        endpoint = EventStatsEndPoint(
            request_body=request_body,
            http_client=self._http_client,
        )
        result = await endpoint.arequest()
        return result

    def get_event_stats(
        self,
        datasets: List[EventDataset],
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        timeseries_interval: Optional[
            EventStatsTimeSeriesInterval
        ] = EventStatsTimeSeriesInterval.YEAR,
        duration: Optional[int] = 90,
        **kwargs: Dict[str, Any],
    ) -> EventStatsResult:
        """Synchronously get events statistics data."""
        request_body = EventStatsBody(
            datasets=datasets,
            start_date=start_date,
            end_date=end_date,
            timeseries_interval=timeseries_interval,
            duration=duration,
        )  # type: ignore[call-arg]
        endpoint = EventStatsEndPoint(
            request_body=request_body,
            http_client=self._http_client,
        )
        result = endpoint.request()
        return result
