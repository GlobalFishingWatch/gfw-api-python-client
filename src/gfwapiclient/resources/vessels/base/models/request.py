"""Global Fishing Watch (GFW) API Python Client - Vessels API Base Request Models.

This module defines base request models for the Vessels API, providing
common parameters and enumerations for various vessel-related endpoints.
"""

from enum import Enum
from typing import List, Optional

from pydantic import Field

from gfwapiclient.http.models.request import RequestParams


__all__ = [
    "VesselBaseDetailParams",
    "VesselBaseParams",
    "VesselDataset",
    "VesselInclude",
    "VesselMatchField",
    "VesselRegistryInfoData",
]


class VesselDataset(str, Enum):
    """Enumeration of available vessel datasets.

    Attributes:
        VESSEL_IDENTITY_LATEST (str):
            The latest version of the public global vessel identity dataset.
    """

    VESSEL_IDENTITY_LATEST = "public-global-vessel-identity:latest"


class VesselRegistryInfoData(str, Enum):
    """Enumeration of registry information data options.

    Attributes:
        NONE (str):
            Do not include registry information data.

        DELTA (str):
            Include only changes in registry information data.

        ALL (str):
            Include all registry information data.
    """

    NONE = "NONE"
    DELTA = "DELTA"
    ALL = "ALL"


class VesselInclude(str, Enum):
    """Enumeration of extra information to include in vessel details.

    Attributes:
        POTENTIAL_RELATED_SELF_REPORTED_INFO (str):
            Include potential related self-reported information.
    """

    POTENTIAL_RELATED_SELF_REPORTED_INFO = "POTENTIAL_RELATED_SELF_REPORTED_INFO"


class VesselMatchField(str, Enum):
    """Enumeration of match field options for vessel search.

    Attributes:
        SEVERAL_FIELDS (str):
            Match on several fields.

        NO_MATCH (str):
            Do not match on any fields.

        ALL (str):
            Match on all available fields.
    """

    SEVERAL_FIELDS = "SEVERAL_FIELDS"
    NO_MATCH = "NO_MATCH"
    ALL = "ALL"


class VesselBaseParams(RequestParams):
    """Base request query parameters for all Vessels API endpoints.

    Provides common parameters applicable to various vessel-related endpoints.

    Attributes:
        match_fields (Optional[List[VesselMatchField]]):
            Filter by match fields levels criteria.

        binary (Optional[bool]):
            Whether response should be in binary format (proto buffer) or not.
    """

    match_fields: Optional[List[VesselMatchField]] = Field(
        None, serialization_alias="match-fields"
    )
    binary: Optional[bool] = Field(False, serialization_alias="binary")


class VesselBaseDetailParams(VesselBaseParams):
    """Base request query parameters for get vessels by IDs and get vessel by ID API endpoints.

    Provides common parameters for retrieving vessel details.

    Attributes:
        registries_info_data (Optional[VesselRegistryInfoData]):
            Registry info data criteria.

        includes (Optional[List[VesselInclude]]):
            Whether to add extra information to the response.
    """

    registries_info_data: Optional[VesselRegistryInfoData] = Field(
        VesselRegistryInfoData.NONE, serialization_alias="registries-info-data"
    )
    includes: Optional[List[VesselInclude]] = Field(
        [VesselInclude.POTENTIAL_RELATED_SELF_REPORTED_INFO],
        serialization_alias="includes",
    )
