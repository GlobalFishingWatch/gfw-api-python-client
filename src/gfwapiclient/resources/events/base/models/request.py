"""Global Fishing Watch (GFW) API Python Client - Events API Base Request Models."""

import datetime

from enum import Enum
from typing import List, Optional

from pydantic import Field

from gfwapiclient.base.models import GeoJson, Geometry, Region
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
    """Events API dataset.

    For more details about the Events API supported datasets, dataset versioning,
    and data caveats, refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/key-concepts#api-dataset

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#how-are-the-events-estimated

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/events

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats

    **Important:**

    We recommend using the `latest` dataset alias to ensure access
    to the latest data improvements. When requesting a dataset using
    the `latest` alias, the API returns the resolved, specific dataset
    version in the `x-datasets` response header. This allows callers
    to identify the exact dataset version used to generate the response.

    For reproducibility, callers may alternatively request a specific
    dataset version using its corresponding version tag.

    Attributes:
        ENCOUNTERS_EVENTS_LATEST (str):
            The latest version of the public global encounters events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#encounter-event

        ENCOUNTERS_EVENTS_V5_0 (str):
            Version 5.0 of the public global encounters events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#encounter-event

        ENCOUNTERS_EVENTS_V4_0 (str):
            Version 4.0 of the public global encounters events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#encounter-event

        GAPS_EVENTS_LATEST (str):
            The latest version of the public global gaps events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#ais-off-event-aka-gap

        GAPS_EVENTS_V5_0 (str):
            Version 5.0 of the public global gaps events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#ais-off-event-aka-gap

        GAPS_EVENTS_V4_0 (str):
            Version 4.0 of the public global gaps events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#ais-off-event-aka-gap

        FISHING_EVENTS_LATEST (str):
            The latest version of the public global fishing events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#apparent-fishing-events

        FISHING_EVENTS_V5_0 (str):
            Version 5.0 of the public global fishing events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#apparent-fishing-events

        FISHING_EVENTS_V4_0 (str):
            Version 4.0 of the public global fishing events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#apparent-fishing-events

        LOITERING_EVENTS_LATEST (str):
            The latest version of the public global loitering events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#loitering-event

        LOITERING_EVENTS_V5_0 (str):
            Version 5.0 of the public global loitering events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#loitering-event

        LOITERING_EVENTS_V4_0 (str):
            Version 4.0 of the public global loitering events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#loitering-event

        PORT_VISITS_EVENTS_LATEST (str):
            The latest version of the public global port visits events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#port-visit-events

        PORT_VISITS_EVENTS_V5_0 (str):
            Version 5.0 of the public global port visits events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#port-visit-events

        PORT_VISITS_EVENTS_V4_0 (str):
            Version 4.0 of the public global port visits events dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#port-visit-events
    """

    ENCOUNTERS_EVENTS_LATEST = "public-global-encounters-events:latest"
    ENCOUNTERS_EVENTS_V5_0 = "public-global-encounters-events:v5.0"
    ENCOUNTERS_EVENTS_V4_0 = "public-global-encounters-events:v4.0"

    GAPS_EVENTS_LATEST = "public-global-gaps-events:latest"
    GAPS_EVENTS_V5_0 = "public-global-gaps-events:v5.0"
    GAPS_EVENTS_V4_0 = "public-global-gaps-events:v4.0"

    FISHING_EVENTS_LATEST = "public-global-fishing-events:latest"
    FISHING_EVENTS_V5_0 = "public-global-fishing-events:v5.0"
    FISHING_EVENTS_V4_0 = "public-global-fishing-events:v4.0"

    LOITERING_EVENTS_LATEST = "public-global-loitering-events:latest"
    LOITERING_EVENTS_V5_0 = "public-global-loitering-events:v5.0"
    LOITERING_EVENTS_V4_0 = "public-global-loitering-events:v4.0"

    PORT_VISITS_EVENTS_LATEST = "public-global-port-visits-events:latest"
    PORT_VISITS_EVENTS_V5_0 = "public-global-port-visits-events:v5.0"
    PORT_VISITS_EVENTS_V4_0 = "public-global-port-visits-events:v4.0"


class EventGeometry(GeoJson):
    """GeoJSON-like region where the events occur.

    Represents a GeoJSON-compatible area of interest used for filtering event data.

    For more details on the Events API supported geojson/geometries, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#events-post-body-parameters
    """

    pass


class EventRegion(Region):
    """Region where the events occur.

    Represents a predefined area of interest used for filtering events data.

    For more details on the Events API supported regions, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#events-post-body-parameters

    See: https://globalfishingwatch.org/our-apis/documentation#regions
    """

    pass


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

        geometry (Optional[Geometry]):
            Region where the events occur (GeoJSON).

        region (Optional[EventRegion]):
            Region where the events occur (by dataset and ID).

        vessel_types (Optional[List[EventVesselType]]):
            Vessel types to filter by.
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
    geometry: Optional[Geometry] = Field(None)  # TODO: use GeoJson
    region: Optional[EventRegion] = Field(None)
    vessel_types: Optional[List[EventVesselType]] = Field(None)
