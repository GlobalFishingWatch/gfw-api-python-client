"""Global Fishing Watch (GFW) API Python Client - Get Vessels by IDs API Request Models.

This module defines request models for the Vessels API's get vessels by IDs endpoint.
"""

from typing import ClassVar, Final, List, Optional

from pydantic import Field

from gfwapiclient.resources.vessels.base.models.request import (
    VesselBaseDetailParams,
    VesselDataset,
)


__all__ = ["VesselListParams"]


VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Get vesselS by IDs request parameters validation failed."
)


class VesselListParams(VesselBaseDetailParams):
    """Request query parameters for get list of vessels filtered by ids API endpoint."""

    """Request query parameters for the get list of vessels filtered by IDs API endpoint.

    Attributes:
        datasets (List[VesselDataset]):
            Datasets that will be used to search the vessels.

        ids (List[str]):
            List of vessel IDs.

        vessel_groups (Optional[List[str]]):
            List of vessel groups.
    """

    indexed_fields: ClassVar[Optional[List[str]]] = [
        "datasets",
        "includes",
        "match-fields",
        "ids",
        "vessel-groups",
    ]

    datasets: List[VesselDataset] = Field(
        [VesselDataset.VESSEL_IDENTITY_LATEST], serialization_alias="datasets"
    )
    ids: List[str] = Field(..., serialization_alias="ids")
    vessel_groups: Optional[List[str]] = Field(
        None, serialization_alias="vessel-groups"
    )
