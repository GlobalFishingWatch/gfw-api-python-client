"""Global Fishing Watch (GFW) API Python Client - Vessels Insights Request Models."""

import datetime

from enum import Enum
from typing import List

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import RequestBody


__all__ = ["VesselInsightBody"]


class VesselInsightInclude(str, Enum):
    """Vessel insight types."""

    FISHING = "FISHING"
    GAP = "GAP"
    COVERAGE = "COVERAGE"
    VESSEL_IDENTITY_IUU_VESSEL_LIST = "VESSEL-IDENTITY-IUU-VESSEL-LIST"


class VesselInsightIdBody(BaseModel):
    """Dataset and Vessel ID to use to get vessel insights."""

    dataset_id: str = Field(..., description="Dataset identifier.")
    vessel_id: str = Field(..., description="Vessel identifier.")


class VesselInsightBody(RequestBody):
    """Vessel insight request body."""

    includes: List[VesselInsightInclude] = Field(
        [VesselInsightInclude.FISHING],
        description="List of requested insights.",
    )
    start_date: datetime.date = Field(..., description="Start date of the request")
    end_date: datetime.date = Field(..., description="End date of the request")
    vessels: List[VesselInsightIdBody] = Field(
        ...,
        description="List of Dataset and Vessel ID to use to get vessel insights.",
    )
