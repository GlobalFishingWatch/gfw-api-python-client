"""Global Fishing Watch (GFW) API Python Client - Events List API Request Models."""

import datetime

from typing import List, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestBody, RequestParams
from gfwapiclient.resources.events.base.enums import (
    EventConfidence,
    EventDataset,
    EventEncounterType,
    EventType,
    EventVesselType,
)
from gfwapiclient.resources.events.base.request import EventGeometry, EventRegion


__all__ = ["EventListParams", "RequestBody"]


class EventListParams(RequestParams):
    """Request query parameters for get all events API endpoint."""

    # TODO: default, max limit
    limit: Optional[int] = Field(
        99999,
        description="Amount of search results to return.",
    )
    offset: Optional[int] = Field(
        0,
        description="Offset into the search results, used for pagination.",
    )
    sort: Optional[str] = Field(
        None,
        description="Property used to sort, depends on the dataset.",
    )


# TODO: extend EventBody
class EventListBody(RequestBody):
    """Request body for get all events API endpoint."""

    # TODO: default???
    datasets: List[EventDataset] = Field(
        ...,
        serialization_alias="datasets",
        description="Datasets that will be used to search the vessel events.",
    )
    vessels: Optional[List[str]] = Field(
        None,
        serialization_alias="vessels",
        description="List of vessel ids to be used.",
    )
    types: Optional[List[EventType]] = Field(None, description="Event types.")
    start_date: Optional[datetime.date] = Field(
        None, description="Start date of the event (inclusive)."
    )
    end_date: Optional[datetime.date] = Field(
        None, description="End date of the event (exclusive)."
    )
    confidences: Optional[List[EventConfidence]] = Field(
        None,
        description="Event confidence level.",
    )
    encounter_types: Optional[List[EventEncounterType]] = Field(
        None, description="Encounter types."
    )
    duration: Optional[int] = Field(
        90,
        description="Minimum duration (greater than or equal to), in minutes, of the event.",
    )
    vessel_groups: Optional[List[str]] = Field(
        None, description="Ids of the vessel groups."
    )
    flags: Optional[List[str]] = Field(
        None, description="Flags of the vessels involved in the events, in ISO3."
    )
    geometry: Optional[EventGeometry] = Field(
        None, description="Region where the events happen."
    )
    region: Optional[EventRegion] = Field(
        None, description="Region where the events happen."
    )
    vessel_types: Optional[List[EventVesselType]] = Field(
        None, description="Vessel types."
    )
