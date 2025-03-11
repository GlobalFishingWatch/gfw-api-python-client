"""Global Fishing Watch (GFW) API Python Client - Events API Resource."""

import datetime

from typing import Any, Dict, List, Optional

from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.events.base.enums import (
    EventConfidence,
    EventDataset,
    EventEncounterType,
    EventType,
    EventVesselType,
)
from gfwapiclient.resources.events.base.request import EventGeometry, EventRegion
from gfwapiclient.resources.events.detail.endpoints import EventDetailEndPoint
from gfwapiclient.resources.events.detail.models.request import EventDetailParams
from gfwapiclient.resources.events.detail.models.response import EventDetailResult
from gfwapiclient.resources.events.list.endpoints import EventListEndPoint
from gfwapiclient.resources.events.list.models.request import (
    EventListBody,
    EventListParams,
)
from gfwapiclient.resources.events.list.models.response import EventListResult
from gfwapiclient.resources.events.stats.endpoints import EventStatsEndPoint
from gfwapiclient.resources.events.stats.models.request import (
    EventStatsBody,
    EventStatsTimeSeriesInterval,
)
from gfwapiclient.resources.events.stats.models.response import EventStatsResult


__all__ = ["EventResource"]


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

    async def aget_events(
        self,
        # body
        datasets: List[EventDataset],
        vessels: Optional[List[str]] = None,
        types: Optional[List[EventType]] = None,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        confidences: Optional[List[EventConfidence]] = None,
        encounter_types: Optional[List[EventEncounterType]] = None,
        duration: Optional[int] = 90,
        vessel_groups: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
        geometry: Optional[EventGeometry] = None,
        region: Optional[EventRegion] = None,
        vessel_types: Optional[List[EventVesselType]] = None,
        # params
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        **kwargs: Dict[str, Any],
    ) -> EventListResult:
        """Asynchronously get list events."""
        endpoint = self._make_event_list_endpoint(
            # body
            datasets=datasets,
            vessels=vessels,
            types=types,
            start_date=start_date,
            end_date=end_date,
            confidences=confidences,
            encounter_types=encounter_types,
            duration=duration,
            vessel_groups=vessel_groups,
            flags=flags,
            geometry=geometry,
            region=region,
            vessel_types=vessel_types,
            # params
            limit=limit,
            offset=offset,
            sort=sort,
            **kwargs,
        )
        result = await endpoint.arequest()
        return result

    def get_events(
        self,
        # body
        datasets: List[EventDataset],
        vessels: Optional[List[str]] = None,
        types: Optional[List[EventType]] = None,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        confidences: Optional[List[EventConfidence]] = None,
        encounter_types: Optional[List[EventEncounterType]] = None,
        duration: Optional[int] = 90,
        vessel_groups: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
        geometry: Optional[EventGeometry] = None,
        region: Optional[EventRegion] = None,
        vessel_types: Optional[List[EventVesselType]] = None,
        # params
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        **kwargs: Dict[str, Any],
    ) -> EventListResult:
        """Synchronously get list events."""
        endpoint = self._make_event_list_endpoint(
            # body
            datasets=datasets,
            vessels=vessels,
            types=types,
            start_date=start_date,
            end_date=end_date,
            confidences=confidences,
            encounter_types=encounter_types,
            duration=duration,
            vessel_groups=vessel_groups,
            flags=flags,
            geometry=geometry,
            region=region,
            vessel_types=vessel_types,
            # params
            limit=limit,
            offset=offset,
            sort=sort,
            **kwargs,
        )
        result = endpoint.request()
        return result

    async def aget_event(
        self,
        id: str,
        dataset: EventDataset,
        **kwargs: Dict[str, Any],
    ) -> EventDetailResult:
        """Asynchronously get event by id."""
        endpoint = self._make_event_detail_endpoint(
            id=id,
            dataset=dataset,
            **kwargs,
        )
        result = await endpoint.arequest()
        return result

    def get_event(
        self,
        id: str,
        dataset: EventDataset,
        **kwargs: Dict[str, Any],
    ) -> EventDetailResult:
        """Synchronously get event by id."""
        endpoint = self._make_event_detail_endpoint(
            id=id,
            dataset=dataset,
            **kwargs,
        )
        result = endpoint.request()
        return result

    def _make_event_list_endpoint(
        self,
        # body
        datasets: List[EventDataset],
        vessels: Optional[List[str]] = None,
        types: Optional[List[EventType]] = None,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        confidences: Optional[List[EventConfidence]] = None,
        encounter_types: Optional[List[EventEncounterType]] = None,
        duration: Optional[int] = 90,
        vessel_groups: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
        geometry: Optional[EventGeometry] = None,
        region: Optional[EventRegion] = None,
        vessel_types: Optional[List[EventVesselType]] = None,
        # params
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        **kwargs: Dict[str, Any],
    ) -> EventListEndPoint:
        """Initializes a new `EventListEndPoint` API endpoint."""
        request_params = EventListParams(
            limit=limit,
            offset=offset,
            sort=sort,
        )

        request_body = EventListBody(
            datasets=datasets,
            vessels=vessels,
            types=types,
            start_date=start_date,
            end_date=end_date,
            confidences=confidences,
            encounter_types=encounter_types,
            duration=duration,
            vessel_groups=vessel_groups,
            flags=flags,
            geometry=geometry,
            region=region,
            vessel_types=vessel_types,
        )

        endpoint = EventListEndPoint(
            request_params=request_params,
            request_body=request_body,
            http_client=self._http_client,
        )

        return endpoint

    def _make_event_detail_endpoint(
        self,
        id: str,
        dataset: EventDataset,
        **kwargs: Dict[str, Any],
    ) -> EventDetailEndPoint:
        """Initializes a new `EventDetailEndPoint` API endpoint."""
        request_params = EventDetailParams(
            dataset=dataset,
            # raw=False,
        )

        endpoint = EventDetailEndPoint(
            event_id=id,
            request_params=request_params,
            http_client=self._http_client,
        )

        return endpoint
