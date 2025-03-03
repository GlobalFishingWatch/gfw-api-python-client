"""Global Fishing Watch (GFW) API Python Client -  Events Request Models."""

from enum import Enum


class EventType(str, Enum):
    """Event type."""

    PORT = "PORT"
    ENCOUNTER = "ENCOUNTER"
    LOITERING = "LOITERING"
    GAP = "GAP"
    PORT_VISIT = "PORT_VISIT"


class EventConfidence(int, Enum):
    """Event confidence."""

    LOW = 2
    MEDIUM = 3
    HIGH = 4


class EventEncounterType(str, Enum):
    """Event encounter type."""

    CARRIER_FISHING = "CARRIER-FISHING"
    FISHING_CARRIER = "FISHING-CARRIER"
    FISHING_SUPPORT = "FISHING-SUPPORT"
    SUPPORT_FISHING = "SUPPORT-FISHING"
    # TODO: add missing


class EventVesselType(str, Enum):
    """Event vessel type."""

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
    # TODO: add missing


class EventDataset(str, Enum):
    """Event dataset."""

    ENCOUNTERS_EVENTS_LATEST = "public-global-encounters-events:latest"
    LOITERING_EVENTS_LATEST = "public-global-loitering-events:latest"
    FISHING_EVENTS_LATEST = "public-global-fishing-events:latest"
    PORT_VISITS_EVENTS_LATEST = "public-global-port-visits-events:latest"
    GAPS_EVENTS_LATEST = "public-global-gaps-events:latest"
    # TODO: add missing
