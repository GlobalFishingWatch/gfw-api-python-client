"""Global Fishing Watch (GFW) API Python Client - Vessels Insights API Request Models."""

import datetime

from enum import Enum
from typing import Final, List

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import RequestBody


__all__ = ["VesselInsightBody", "VesselInsightDatasetVessel", "VesselInsightInclude"]


VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Vessel insights request body validation failed."
)


class VesselInsightInclude(str, Enum):
    """Enumeration of vessel insight types.

    This enum defines the possible values for the `includes` parameter in the
    vessel insights request, specifying the types of insights to retrieve.

    Attributes:
        FISHING (str):
            Insights related to fishing activity.

        GAP (str):
            Insights related to AIS gaps.

        COVERAGE (str):
            Insights related to AIS coverage.

        VESSEL_IDENTITY_IUU_VESSEL_LIST (str):
            Insights related to vessels listed in IUU lists.
    """

    FISHING = "FISHING"
    GAP = "GAP"
    COVERAGE = "COVERAGE"
    VESSEL_IDENTITY_IUU_VESSEL_LIST = "VESSEL-IDENTITY-IUU-VESSEL-LIST"


class VesselInsightDatasetVessel(BaseModel):
    """Dataset and Vessel ID to use to get vessel insights.

    This model represents the structure for identifying a vessel in the
    vessel insights request.

    Attributes:
        dataset_id (str):
           The dataset identifier. Default to `"public-global-vessel-identity:latest"`.

        vessel_id:
            The vessel identifier.
    """

    dataset_id: str = Field(...)
    vessel_id: str = Field(...)


class VesselInsightBody(RequestBody):
    """Vessel insight request body.

    This model represents the request body for retrieving vessel insights.

    Attributes:
        includes (List[VesselInsightInclude]):
            List of requested insights. Default to `[VesselInsightInclude.FISHING]`.

        start_date (datetime.date):
            Start date of the request.

        end_date (datetime.date):
            End date of the request.

        vessels List[VesselInsightIdBody]:
            List of Dataset and Vessel ID to use to get vessel insights.
    """

    includes: List[VesselInsightInclude] = Field([VesselInsightInclude.FISHING])
    start_date: datetime.date = Field(...)
    end_date: datetime.date = Field(...)
    vessels: List[VesselInsightDatasetVessel] = Field(...)
