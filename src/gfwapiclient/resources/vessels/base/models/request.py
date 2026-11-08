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
    """Vessel API (identity) dataset.

    For more details about the Vessel API supported datasets, dataset versioning,
    and data caveats, refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/key-concepts#api-dataset

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/vessels

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
        VESSEL_IDENTITY_LATEST (str):
            The latest version of the public global vessel identity dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#vessel-api---vessel-identity-information

        VESSEL_IDENTITY_V5_0 (str):
            Version 5.0 of the public global vessel identity dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#vessel-api---vessel-identity-information

        VESSEL_IDENTITY_V4_0 (str):
            Version 4.0 of the public global vessel identity dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#vessel-api---vessel-identity-information
    """

    VESSEL_IDENTITY_LATEST = "public-global-vessel-identity:latest"
    VESSEL_IDENTITY_V5_0 = "public-global-vessel-identity:v5.0"
    VESSEL_IDENTITY_V4_0 = "public-global-vessel-identity:v4.0"


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
            Include potential related self-reported vessel information.

            This include provides related `vessel ids` identified through
            matching with vessel registry records. It represents Global Fishing Watch's
            best estimate for linking AIS (self-reported) vessel positions to Vessel
            Identity information derived from public registries.

            See how the Vessel API is used in the Vessel Viewer
            here: https://globalfishingwatch.org/our-apis/assets/2024_Vessel_Viewer_and_APIs_behind_It.pdf

            For more details on the Vessels API data caveats, please refer to the
            official Global Fishing Watch API documentation
            here: https://globalfishingwatch.org/our-apis/documentation#vessel-api-vessel-identity-information
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
