"""Global Fishing Watch (GFW) API Python Client - Get Vessel by ID API Request Models.

This module defines request models for the Vessels API's get vessel by ID endpoint.
"""

from typing import ClassVar, Final, List, Optional

from pydantic import Field

from gfwapiclient.resources.vessels.base.models.request import (
    VesselBaseDetailParams,
    VesselDataset,
)


__all__ = ["VesselDetailParams"]


VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Get vessel by ID request parameters validation failed."
)


class VesselDetailParams(VesselBaseDetailParams):
    """Request query parameters for the get vessel by ID API endpoint.

    Attributes:
        dataset (VesselDataset):
            Dataset that will be used to search the vessel.
    """

    indexed_fields: ClassVar[Optional[List[str]]] = [
        "includes",
        "match-fields",
    ]

    dataset: VesselDataset = Field(
        VesselDataset.VESSEL_IDENTITY_LATEST, serialization_alias="dataset"
    )
