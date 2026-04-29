"""Global Fishing Watch (GFW) API Python Client - Get Vessels Insights API Request Models."""

import datetime

from enum import Enum
from typing import Final, List

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.vessels.base.models.request import VesselDataset


__all__ = ["VesselInsightBody", "VesselInsightDatasetVessel", "VesselInsightInclude"]


VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Vessel insights request body validation failed."
)


class VesselInsightInclude(str, Enum):
    """Enumeration of vessel insight types.

    This enum defines the possible values for the `includes` parameter in the
    vessel insights request, specifying the types of insights to retrieve.

    Attributes:
        COVERAGE (str):
            Insights related to AIS coverage.

        FISHING (str):
            Insights related to fishing activity.

        GAP (str):
            Insights related to AIS gaps.

        VESSEL_IDENTITY_FLAG_CHANGES (str):
            Insights related to vessels flag changes.

        VESSEL_IDENTITY_IUU_VESSEL_LIST (str):
            Insights related to vessels listed in IUU lists.

        VESSEL_IDENTITY_MOU_LIST (str):
            Insights related to vessels listed in MOU lists.
    """

    COVERAGE = "COVERAGE"
    FISHING = "FISHING"
    GAP = "GAP"
    VESSEL_IDENTITY_FLAG_CHANGES = "VESSEL-IDENTITY-FLAG-CHANGES"
    VESSEL_IDENTITY_IUU_VESSEL_LIST = "VESSEL-IDENTITY-IUU-VESSEL-LIST"
    VESSEL_IDENTITY_MOU_LIST = "VESSEL-IDENTITY-MOU-LIST"


class VesselInsightDatasetVessel(BaseModel):
    """Dataset and Vessel ID to use to get vessel insights.

    This model represents the structure for identifying a vessel in the
    vessel insights request.

    Attributes:
        dataset_id (VesselDataset):
           The dataset identifier. Default to `VesselDataset.VESSEL_IDENTITY_LATEST`.

        vessel_id (str):
            The vessel identifier.
    """

    dataset_id: VesselDataset = Field(
        VesselDataset.VESSEL_IDENTITY_LATEST, alias="datasetId"
    )
    vessel_id: str = Field(..., alias="vesselId")


class VesselInsightBody(RequestBody):
    """Vessel insight request body.

    Represents includes, start_date, end_date, vessels etc. parameters
    for retrieving vessel insights.

    For more details on the Get Vessels Insights API endpoint supported request body,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#insights-by-vessels-body

    Attributes:
        includes (List[VesselInsightInclude]):
            List of requested insights. Default to `[VesselInsightInclude.FISHING]`.

        start_date (datetime.date):
            Start date of the request.

        end_date (datetime.date):
            End date of the request.

        vessels (List[VesselInsightDatasetVessel]):
            List of Dataset and Vessel ID to use to get vessel insights.
    """

    includes: List[VesselInsightInclude] = Field(
        [VesselInsightInclude.FISHING], alias="includes"
    )
    start_date: datetime.date = Field(..., alias="startDate")
    end_date: datetime.date = Field(..., alias="endDate")
    vessels: List[VesselInsightDatasetVessel] = Field(..., alias="vessels")
