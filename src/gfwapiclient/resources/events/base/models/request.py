"""Global Fishing Watch (GFW) API Python Client - Events API Base Request Models."""

import datetime

from enum import Enum
from typing import Any, List, Optional

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models.request import RequestBody


__all__ = [
    "EventBaseBody",
    "EventConfidence",
    "EventDataset",
    "EventEncounterType",
    "EventGeometry",
    "EventRegion",
    "EventType",
    "EventVesselType",
]


class EventType(str, Enum):
    """Type of event."""

    ENCOUNTER = "ENCOUNTER"
    FISHING = "FISHING"
    GAP = "GAP"
    GAP_START = "GAP_START"
    LOITERING = "LOITERING"
    PORT = "PORT"
    PORT_VISIT = "PORT_VISIT"


class EventConfidence(str, Enum):
    """Confidence level of the event."""

    LOW = "2"
    MEDIUM = "3"
    HIGH = "4"


class EventEncounterType(str, Enum):
    """Type of encounter event."""

    CARRIER_FISHING = "CARRIER-FISHING"
    FISHING_CARRIER = "FISHING-CARRIER"
    FISHING_SUPPORT = "FISHING-SUPPORT"
    SUPPORT_FISHING = "SUPPORT-FISHING"
    FISHING_BUNKER = "FISHING-BUNKER"
    BUNKER_FISHING = "BUNKER-FISHING"
    FISHING_FISHING = "FISHING-FISHING"
    FISHING_TANKER = "FISHING-TANKER"
    TANKER_FISHING = "TANKER-FISHING"
    CARRIER_BUNKER = "CARRIER-BUNKER"
    BUNKER_CARRIER = "BUNKER-CARRIER"
    SUPPORT_BUNKER = "SUPPORT-BUNKER"
    BUNKER_SUPPORT = "BUNKER-SUPPORT"


class EventVesselType(str, Enum):
    """Type of vessel involved in the event."""

    BUNKER = "BUNKER"
    CARGO = "CARGO"
    DISCREPANCY = "DISCREPANCY"
    CARRIER = "CARRIER"
    FISHING = "FISHING"
    GEAR = "GEAR"
    OTHER = "OTHER"
    PASSENGER = "PASSENGER"
    SEISMIC_VESSEL = "SEISMIC_VESSEL"
    SUPPORT = "SUPPORT"


class EventDataset(str, Enum):
    """Dataset containing the events."""

    ENCOUNTERS_EVENTS_LATEST = "public-global-encounters-events:latest"
    FISHING_EVENTS_LATEST = "public-global-fishing-events:latest"
    GAPS_EVENTS_LATEST = "public-global-gaps-events:latest"
    LOITERING_EVENTS_LATEST = "public-global-loitering-events:latest"
    PORT_VISITS_EVENTS_LATEST = "public-global-port-visits-events:latest"


class EventGeometry(BaseModel):
    """GeoJSON-like region where the events occur.

    Attributes:
        type (str):
            The GeoJSON geometry type (e.g., "Polygon").

        coordinates (Any):
            The GeoJSON coordinates.
    """

    type: str = Field(...)
    coordinates: Any = Field(...)


class EventRegion(BaseModel):
    """Region where the events occur.

    Attributes:
        dataset (str):
            The dataset containing the region.

        id (str):
            The region ID.
    """

    dataset: str = Field(...)
    id: str = Field(...)


class EventBaseBody(RequestBody):
    """Base request body for retrieving all events and event statistics.

    Attributes:
        datasets (List[EventDataset]):
            Datasets to use for searching vessel events.

        vessels (Optional[List[str]]):
            List of vessel IDs to filter by.

        types (Optional[List[EventType]]):
            Event types to filter by.

        start_date (Optional[datetime.date]):
            Start date of the events (inclusive).

        end_date (Optional[datetime.date]):
            End date of the events (exclusive).

        confidences (Optional[List[EventConfidence]]):
            Confidence levels of the events.

        encounter_types (Optional[List[EventEncounterType]]):
            Encounter types to filter by.

        duration (Optional[int]):
            Minimum duration (in minutes) of the events.

        vessel_groups (Optional[List[str]]):
            IDs of the vessel groups to filter by.

        flags (Optional[List[str]]):
            Flags (in ISO3 format) of the vessels involved in the events.

        geometry (Optional[EventGeometry]):
            Region where the events occur (GeoJSON).

        region (Optional[EventRegion]):
            Region where the events occur (by dataset and ID).

        vessel_types (Optional[List[EventVesselType]]):
            Vessel types to filter by.

        gap_intentional_disabling (Optional[bool]):
            Whether to retrieve AIS off events (gaps) that were potentially intentional.
    """

    datasets: List[EventDataset] = Field(...)
    vessels: Optional[List[str]] = Field(None)
    types: Optional[List[EventType]] = Field(None)
    start_date: Optional[datetime.date] = Field(None)
    end_date: Optional[datetime.date] = Field(None)
    confidences: Optional[List[EventConfidence]] = Field(None)
    encounter_types: Optional[List[EventEncounterType]] = Field(None)
    duration: Optional[int] = Field(None)
    vessel_groups: Optional[List[str]] = Field(None)
    flags: Optional[List[str]] = Field(None)
    geometry: Optional[EventGeometry] = Field(None)
    region: Optional[EventRegion] = Field(None)
    vessel_types: Optional[List[EventVesselType]] = Field(None)
    gap_intentional_disabling: Optional[bool] = Field(None)
