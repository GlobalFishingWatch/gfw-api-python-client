"""Global Fishing Watch (GFW) API Python Client - Events API Base Enums."""

from enum import Enum


__all__ = [
    "EventConfidence",
    "EventDataset",
    "EventEncounterType",
    "EventType",
    "EventVesselType",
]


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

    # stats
    CARRIER_FISHING = "CARRIER-FISHING"
    FISHING_CARRIER = "FISHING-CARRIER"
    FISHING_SUPPORT = "FISHING-SUPPORT"
    SUPPORT_FISHING = "SUPPORT-FISHING"
    # list
    FISHING_BUNKER = "FISHING-BUNKER"
    BUNKER_FISHING = "BUNKER-FISHING"
    FISHING_FISHING = "FISHING-FISHING"
    FISHING_TANKER = "FISHING-TANKER"
    TANKER_FISHING = "TANKER-FISHING"
    CARRIER_BUNKER = "CARRIER-BUNKER"
    BUNKER_CARRIER = "BUNKER-CARRIER"
    SUPPORT_BUNKER = "SUPPORT-BUNKER"
    BUNKER_SUPPORT = "BUNKER-SUPPORT"
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

    # list
    OTHER_NON_FISHING = "OTHER_NON_FISHING"
    BUNKER_OR_TANKER = "BUNKER_OR_TANKER"
    # TODO: add missing


class EventDataset(str, Enum):
    """Event dataset."""

    ENCOUNTERS_EVENTS_LATEST = "public-global-encounters-events:latest"
    LOITERING_EVENTS_LATEST = "public-global-loitering-events:latest"
    FISHING_EVENTS_LATEST = "public-global-fishing-events:latest"
    PORT_VISITS_EVENTS_LATEST = "public-global-port-visits-events:latest"
    GAPS_EVENTS_LATEST = "public-global-gaps-events:latest"
    # TODO: add missing
