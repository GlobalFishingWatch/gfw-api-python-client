"""Global Fishing Watch (GFW) API Python Client - Events Statistics Request Models."""

import datetime

from enum import Enum
from typing import Any, List, Optional

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.events.models.request import (
    EventConfidence,
    EventDataset,
    EventEncounterType,
    EventType,
    EventVesselType,
)


__all__ = ["EventStatsBody"]


class EventStatsTimeSeriesInterval(str, Enum):
    """Event statistics time series granularity."""

    HOUR = "HOUR"
    DAY = "DAY"
    MONTH = "MONTH"
    YEAR = "YEAR"


class EventStatsInclude(str, Enum):
    """Event statistics include."""

    TOTAL_COUNT = "TOTAL_COUNT"
    TIME_SERIES = "TIME_SERIES"


# TODO: use shapely.Geometry???
class Geometry(BaseModel):
    """Model for GeoJSON-like geometry input."""

    type: str
    coordinates: Any
    # FIX: Should ideally be `List[List[List[float]]]` for MultiPolygon


# TODO: import from Region
class Region(BaseModel):
    """Model for defining a region by dataset and ID."""

    dataset: str
    id: int


class EventStatsBody(RequestBody):
    """Event statistics request body."""

    datasets: List[EventDataset] = Field(
        ..., description="List of datasets to be used."
    )
    vessels: Optional[List[str]] = Field(
        None, description="List of vessel ids to be used."
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
    geometry: Optional[Geometry] = Field(
        None, description="Region where the events happen."
    )
    region: Optional[Region] = Field(
        None, description="Region where the events happen."
    )
    timeseries_interval: Optional[EventStatsTimeSeriesInterval] = Field(
        EventStatsTimeSeriesInterval.YEAR, description="Time series granularity."
    )
    includes: Optional[List[EventStatsInclude]] = Field(
        None, description="Allows to include additional information."
    )
    vessel_types: Optional[List[EventVesselType]] = Field(
        None, description="Vessel types."
    )
