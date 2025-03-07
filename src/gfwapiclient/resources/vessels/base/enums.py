"""Global Fishing Watch (GFW) API Python Client - Vessels API Base Enum Models."""

from enum import Enum


__all__ = [
    "VesselDataset",
    "VesselInclude",
    "VesselMatchField",
    "VesselRegistryInfoData",
]


class VesselDataset(str, Enum):
    """Vessels API dataset."""

    VESSEL_IDENTITY_LATEST = "public-global-vessel-identity:latest"
    # TODO: add missing


class VesselRegistryInfoData(str, Enum):
    """Vessels API registries info data."""

    NONE = "NONE"
    DELTA = "DELTA"
    ALL = "ALL"


class VesselInclude(str, Enum):
    """Vessels API extra information include."""

    POTENTIAL_RELATED_SELF_REPORTED_INFO = "POTENTIAL_RELATED_SELF_REPORTED_INFO"


class VesselMatchField(str, Enum):
    """Vessels API match field."""

    SEVERAL_FIELDS = "SEVERAL_FIELDS"
    NO_MATCH = "NO_MATCH"
    ALL = "ALL"
