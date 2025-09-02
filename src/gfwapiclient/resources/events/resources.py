"""Global Fishing Watch (GFW) API Python Client - Events API Resource."""

import datetime

from typing import Any, Dict, List, Optional, Union

import pydantic

from gfwapiclient.exceptions.validation import (
    RequestBodyValidationError,
    RequestParamsValidationError,
)
from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.events.base.models.request import (
    EventConfidence,
    EventDataset,
    EventEncounterType,
    EventGeometry,
    EventRegion,
    EventType,
    EventVesselType,
)
from gfwapiclient.resources.events.detail.endpoints import EventDetailEndPoint
from gfwapiclient.resources.events.detail.models.request import (
    EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    EventDetailParams,
)
from gfwapiclient.resources.events.detail.models.response import EventDetailResult
from gfwapiclient.resources.events.list.endpoints import EventListEndPoint
from gfwapiclient.resources.events.list.models.request import (
    EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    EventListBody,
    EventListParams,
)
from gfwapiclient.resources.events.list.models.response import EventListResult
from gfwapiclient.resources.events.stats.endpoints import EventStatsEndPoint
from gfwapiclient.resources.events.stats.models.request import (
    EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    EventStatsBody,
    EventStatsInclude,
    EventStatsTimeSeriesInterval,
)
from gfwapiclient.resources.events.stats.models.response import EventStatsResult


__all__ = ["EventResource"]


class EventResource(BaseResource):
    """Resource for interacting with the Events API.

    This resource provides methods for retrieving event data, including lists of
    events, individual events by ID, and event statistics.
    """

    async def get_all_events(
        self,
        *,
        datasets: Union[List[EventDataset], List[str]],
        vessels: Optional[List[str]] = None,
        types: Optional[Union[List[EventType], List[str]]] = None,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
        confidences: Optional[Union[List[EventConfidence], List[str]]] = None,
        encounter_types: Optional[Union[List[EventEncounterType], List[str]]] = None,
        duration: Optional[int] = None,
        vessel_types: Optional[Union[List[EventVesselType], List[str]]] = None,
        vessel_groups: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
        geometry: Optional[Union[EventGeometry, Dict[str, Any]]] = None,
        region: Optional[Union[EventRegion, Dict[str, Any]]] = None,
        gap_intentional_disabling: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        **kwargs: Dict[str, Any],
    ) -> EventListResult:
        """Get All Events.

        Retrieves a list of events based on specified criteria.

        Args:
            datasets (Union[List[EventDataset], List[str]]):
                Datasets to search for events.
                Allowed values: `["public-global-encounters-events:latest", "public-global-fishing-events:latest",
                "public-global-gaps-events:latest", "public-global-loitering-events:latest",
                "public-global-port-visits-events:latest"]`.
                Example: `["public-global-fishing-events:latest", "public-global-encounters-events:latest"]`.

            vessels (Optional[List[str]], default=None):
                List of vessel IDs to filter events. Defaults to `None`.
                Example: `["55d38c0ee-e0d7-cb32-ac9c-8b3680d213b3"]`.

            types (Optional[Union[List[EventType], List[str]]], default=None):
                List of event types to filter events. Defaults to `None`.
                Allowed values: `["ENCOUNTER", "PORT_VISIT", "FISHING", "CARRIER_OPERATIONS", "LOITERING"]`.
                Example: `["FISHING", "ENCOUNTER"]`.

            start_date (Optional[Union[datetime.date, str]], default=None):
                Start date for event filtering. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2017, 1, 1)` or `"2017-01-01"`.

            end_date (Optional[Union[datetime.date, str]], default=None):
                End date for event filtering. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2017, 1, 31)` or `"2017-01-31"`.

            confidences (Optional[Union[List[EventConfidence], List[str]]], default=None):
                List of event confidence levels to filter events. Defaults to `None`.
                Allowed values: `["2", "3", "4"]`.
                Example: `["3", "4"]`.

            encounter_types (Optional[Union[List[EventEncounterType], List[str]]], default=None):
                List of encounter types to filter events. Defaults to `None`.
                Allowed values: `["CARRIER-FISHING", "FISHING-CARRIER", "FISHING-SUPPORT",
                "SUPPORT-FISHING", "FISHING-BUNKER", "BUNKER-FISHING", "FISHING-FISHING",
                "FISHING-TANKER", "TANKER-FISHING", "CARRIER-BUNKER", "BUNKER-CARRIER",
                "SUPPORT-BUNKER", "BUNKER-SUPPORT"]`.
                Example: `["CARRIER-FISHING", "FISHING-CARRIER"]`.

            duration (Optional[int], default=None):
                Duration to filter events (in minutes). Defaults to `None`.
                Example: `60`.

            vessel_types (Optional[Union[List[EventVesselType], List[str]]], default=None):
                List of vessel types to filter events. Defaults to `None`.
                Allowed values: `["BUNKER", "CARGO", "DISCREPANCY", "CARRIER", "FISHING",
                "GEAR", "OTHER", "PASSENGER", "SEISMIC_VESSEL", "SUPPORT"]`.
                Example: `["FISHING", "CARGO"]`.

            vessel_groups (Optional[List[str]], default=None):
                List of vessel groups to filter events. Defaults to `None`.
                Example: `["my-vessel-group"]`.

            flags (Optional[List[str]], default=None):
                List of vessel flags to filter events. Defaults to `None`.
                Example: `["USA", "CAN"]`.

            geometry (Optional[Union[EventGeometry, Dict[str, Any]]], default=None):
                Geometry to filter events. Defaults to `None`.
                Example: `{"type": "Polygon", "coordinates": [...]}`.

            region (Optional[Union[EventRegion, Dict[str, Any]]], default=None):
                Region to filter events. Defaults to `None`.
                Example: `{"dataset": "public-eez-areas", "id": "5690"}`.

            gap_intentional_disabling (Optional[bool], default=None):
                Filter events based on intentional disabling of gap. Defaults to `None`.

            limit (Optional[int], default=99999):
                Maximum number of events to return. Defaults to `99999`.
                Example: `100`.

            offset (Optional[int], default=0):
                Number of events to skip before returning results. Defaults to `0`.
                Example: `100`.

            sort (Optional[str], default=None):
                Property to sort the events by. Defaults to `None`.
                Example: `"-start"`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            EventListResult:
                The result containing the list of events.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.

            RequestBodyValidationError:
                If the request body is invalid.
        """
        request_params: EventListParams = self._prepare_get_all_events_request_params(
            limit=limit,
            offset=offset,
            sort=sort,
        )

        request_body: EventListBody = self._prepare_get_all_events_request_body(
            datasets=datasets,
            vessels=vessels,
            types=types,
            start_date=start_date,
            end_date=end_date,
            confidences=confidences,
            encounter_types=encounter_types,
            duration=duration,
            vessel_types=vessel_types,
            vessel_groups=vessel_groups,
            flags=flags,
            geometry=geometry,
            region=region,
            gap_intentional_disabling=gap_intentional_disabling,
        )

        endpoint: EventListEndPoint = EventListEndPoint(
            request_params=request_params,
            request_body=request_body,
            http_client=self._http_client,
        )

        result: EventListResult = await endpoint.request(**kwargs)
        return result

    async def get_event_by_id(
        self,
        *,
        id: str,
        dataset: Union[EventDataset, str],
        **kwargs: Dict[str, Any],
    ) -> EventDetailResult:
        """Get one by Event ID.

        Retrieves a single event by its ID.

        Args:
            id (str):
                The ID of the event to retrieve.
                Example: `"3ca9b73aee21fbf278a636709e0f8f03"`.

            dataset (Union[EventDataset, str]):
                The dataset to search for the event in.
                Allowed values: `["public-global-encounters-events:latest", "public-global-fishing-events:latest",
                "public-global-gaps-events:latest", "public-global-loitering-events:latest",
                "public-global-port-visits-events:latest"]`.
                Example: `"public-global-fishing-events:latest"`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            EventDetailResult:
                The result containing the event details.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.
        """
        request_params: EventDetailParams = (
            self._prepare_get_event_by_id_request_params(dataset=dataset)
        )

        endpoint: EventDetailEndPoint = EventDetailEndPoint(
            event_id=id,
            request_params=request_params,
            http_client=self._http_client,
        )

        result: EventDetailResult = await endpoint.request(**kwargs)
        return result

    async def get_events_stats(
        self,
        *,
        datasets: Union[List[EventDataset], List[str]],
        timeseries_interval: Union[EventStatsTimeSeriesInterval, str],
        vessels: Optional[List[str]] = None,
        types: Optional[Union[List[EventType], List[str]]] = None,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
        confidences: Optional[Union[List[EventConfidence], List[str]]] = None,
        encounter_types: Optional[Union[List[EventEncounterType], List[str]]] = None,
        duration: Optional[int] = None,
        vessel_types: Optional[Union[List[EventVesselType], List[str]]] = None,
        vessel_groups: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
        geometry: Optional[Union[EventGeometry, Dict[str, Any]]] = None,
        region: Optional[Union[EventRegion, Dict[str, Any]]] = None,
        gap_intentional_disabling: Optional[bool] = None,
        includes: Optional[Union[List[EventStatsInclude], List[str]]] = None,
        **kwargs: Dict[str, Any],
    ) -> EventStatsResult:
        """Get events statistics worldwide or for a specific region.

        Args:
            datasets (Union[List[EventDataset], List[str]]):
                Datasets to search for statistics.
                Allowed values: `["public-global-encounters-events:latest", "public-global-fishing-events:latest",
                "public-global-gaps-events:latest", "public-global-loitering-events:latest",
                "public-global-port-visits-events:latest"]`.
                Example: `["public-global-fishing-events:latest", "public-global-encounters-events:latest"]`.

            timeseries_interval (Union[EventStatsTimeSeriesInterval, str]):
                Time series granularity for statistics.
                Allowed values: `["HOUR", "DAY", "MONTH", "YEAR"]`.
                Example: `"DAY"`.

            vessels (Optional[List[str]], default=None):
                List of vessel IDs to filter statistics. Defaults to `None`.
                Example: `["55d38c0ee-e0d7-cb32-ac9c-8b3680d213b3"]`.

            types (Optional[Union[List[EventType], List[str]]], default=None):
                List of event types to filter statistics. Defaults to `None`.
                Allowed values: `["ENCOUNTER", "PORT_VISIT", "FISHING", "CARRIER_OPERATIONS", "LOITERING"]`.
                Example: `["FISHING", "ENCOUNTER"]`.

            start_date (Optional[Union[datetime.date, str]], default=None):
                Start date for event filtering. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2023, 1, 31)` or `"2023-01-31"`.

            end_date (Optional[Union[datetime.date, str]], default=None):
                End date for event filtering. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2023, 12, 31)` or `"2023-12-31"`.

            confidences (Optional[Union[List[EventConfidence], List[str]]], default=None):
                List of event confidence levels to filter statistics. Defaults to `None`.
                Allowed values: `["2", "3", "4"]`.
                Example: `["3", "4"]`.

            encounter_types (Optional[Union[List[EventEncounterType], List[str]]], default=None):
                List of encounter types to filter statistics. Defaults to `None`.
                Allowed values: `["CARRIER-FISHING", "FISHING-CARRIER", "FISHING-SUPPORT",
                "SUPPORT-FISHING", "FISHING-BUNKER", "BUNKER-FISHING", "FISHING-FISHING",
                "FISHING-TANKER", "TANKER-FISHING", "CARRIER-BUNKER", "BUNKER-CARRIER",
                "SUPPORT-BUNKER", "BUNKER-SUPPORT"]`.
                Example: `["CARRIER-FISHING", "FISHING-CARRIER"]`.

            duration (Optional[int], default=None):
                Duration to filter statistics (in minutes). Defaults to `None`.
                Example: `60`.

            vessel_types (Optional[Union[List[EventVesselType], List[str]]], default=None):
                List of vessel types to filter statistics. Defaults to `None`.
                Allowed values: `["BUNKER", "CARGO", "DISCREPANCY", "CARRIER", "FISHING",
                "GEAR", "OTHER", "PASSENGER", "SEISMIC_VESSEL", "SUPPORT"]`.
                Example: `["FISHING", "CARGO"]`.

            vessel_groups (Optional[List[str]], default=None):
                List of vessel groups to filter statistics. Defaults to `None`.
                Example: `["my-vessel-group"]`.

            flags (Optional[List[str]], default=None):
                List of vessel flags to filter statistics. Defaults to `None`.
                Example: `["USA", "CAN"]`.

            geometry (Optional[Union[EventGeometry, Dict[str, Any]]], default=None):
                Geometry to filter statistics. Defaults to `None`.
                Example: `{"type": "Polygon", "coordinates": [...]}`.

            region (Optional[Union[EventRegion, Dict[str, Any]]], default=None):
                Region to filter statistics. Defaults to `None`.
                Example: `{"dataset": "public-eez-areas", "id": "5690"}`.

            gap_intentional_disabling (Optional[bool], default=None):
                Filter statistics based on intentional disabling of gap. Defaults to `None`.

            includes (Optional[Union[List[EventStatsInclude], List[str]]], default=None):
                List of additional information to include in the statistics. Defaults to `None`.
                Allowed values: `["TOTAL_COUNT", "TIME_SERIES"]`.
                Example: `["TOTAL_COUNT", "TIME_SERIES"]`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            EventStatsResult:
                The result containing the event statistics.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestBodyValidationError:
                If the request body is invalid.
        """
        request_body: EventStatsBody = self._prepare_get_events_stats_request_body(
            datasets=datasets,
            timeseries_interval=timeseries_interval,
            vessels=vessels,
            types=types,
            start_date=start_date,
            end_date=end_date,
            confidences=confidences,
            encounter_types=encounter_types,
            duration=duration,
            vessel_types=vessel_types,
            vessel_groups=vessel_groups,
            flags=flags,
            geometry=geometry,
            region=region,
            gap_intentional_disabling=gap_intentional_disabling,
            includes=includes,
        )

        endpoint: EventStatsEndPoint = EventStatsEndPoint(
            request_body=request_body,
            http_client=self._http_client,
        )

        result = await endpoint.request(**kwargs)
        return result

    def _prepare_get_all_events_request_params(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
    ) -> EventListParams:
        """Prepares and returns the request parameters for the get all events endpoint."""
        try:
            _request_params: Dict[str, Any] = {
                "limit": limit or 99999,
                "offset": offset or 0,
                "sort": sort,
            }
            request_params: EventListParams = EventListParams(**_request_params)
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params

    def _prepare_get_all_events_request_body(
        self,
        *,
        datasets: Union[List[EventDataset], List[str]],
        vessels: Optional[List[str]] = None,
        types: Optional[Union[List[EventType], List[str]]] = None,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
        confidences: Optional[Union[List[EventConfidence], List[str]]] = None,
        encounter_types: Optional[Union[List[EventEncounterType], List[str]]] = None,
        duration: Optional[int] = None,
        vessel_types: Optional[Union[List[EventVesselType], List[str]]] = None,
        vessel_groups: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
        geometry: Optional[Union[EventGeometry, Dict[str, Any]]] = None,
        region: Optional[Union[EventRegion, Dict[str, Any]]] = None,
        gap_intentional_disabling: Optional[bool] = None,
    ) -> EventListBody:
        """Prepares and returns the request body for the get all events endpoint."""
        try:
            _request_body: Dict[str, Any] = {
                "datasets": datasets,
                "vessels": vessels,
                "types": types,
                "start_date": start_date,
                "end_date": end_date,
                "confidences": confidences,
                "encounter_types": encounter_types,
                "duration": duration,
                "vessel_types": vessel_types,
                "vessel_groups": vessel_groups,
                "flags": flags,
                "geometry": geometry,
                "region": region,
                "gap_intentional_disabling": gap_intentional_disabling,
            }
            request_body: EventListBody = EventListBody(**_request_body)
        except pydantic.ValidationError as exc:
            raise RequestBodyValidationError(
                message=EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_body

    def _prepare_get_event_by_id_request_params(
        self,
        *,
        dataset: Union[EventDataset, str],
    ) -> EventDetailParams:
        """Prepares and returns the request parameters for the get event by ID endpoint."""
        try:
            _request_params: Dict[str, Any] = {"dataset": dataset}
            request_params: EventDetailParams = EventDetailParams(**_request_params)
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params

    def _prepare_get_events_stats_request_body(
        self,
        *,
        datasets: Union[List[EventDataset], List[str]],
        timeseries_interval: Union[EventStatsTimeSeriesInterval, str],
        vessels: Optional[List[str]] = None,
        types: Optional[Union[List[EventType], List[str]]] = None,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
        confidences: Optional[Union[List[EventConfidence], List[str]]] = None,
        encounter_types: Optional[Union[List[EventEncounterType], List[str]]] = None,
        duration: Optional[int] = None,
        vessel_types: Optional[Union[List[EventVesselType], List[str]]] = None,
        vessel_groups: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
        geometry: Optional[Union[EventGeometry, Dict[str, Any]]] = None,
        region: Optional[Union[EventRegion, Dict[str, Any]]] = None,
        gap_intentional_disabling: Optional[bool] = None,
        includes: Optional[Union[List[EventStatsInclude], List[str]]] = None,
    ) -> EventStatsBody:
        """Prepares and returns the request body for the get events statistics endpoint."""
        try:
            _request_body: Dict[str, Any] = {
                "datasets": datasets,
                "timeseries_interval": timeseries_interval,
                "vessels": vessels,
                "types": types,
                "start_date": start_date,
                "end_date": end_date,
                "confidences": confidences,
                "encounter_types": encounter_types,
                "duration": duration,
                "vessel_types": vessel_types,
                "vessel_groups": vessel_groups,
                "flags": flags,
                "geometry": geometry,
                "region": region,
                "gap_intentional_disabling": gap_intentional_disabling,
                "includes": includes,
            }
            request_body: EventStatsBody = EventStatsBody(**_request_body)
        except pydantic.ValidationError as exc:
            raise RequestBodyValidationError(
                message=EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_body
