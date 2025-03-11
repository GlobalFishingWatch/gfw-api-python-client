"""Global Fishing Watch (GFW) API Python Client - Vessel Detail API Request Models."""

from typing import ClassVar, List, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.vessels.base.enums import (
    VesselDataset,
    VesselInclude,
    VesselMatchField,
    VesselRegistryInfoData,
)


__all__ = ["VesselDetailParams"]


class VesselDetailParams(RequestParams):
    """Request query parameters for get vessel by id API endpoint."""

    indexed_fields: ClassVar[Optional[List[str]]] = [
        "includes",
        "match-fields",
    ]

    dataset: VesselDataset = Field(
        VesselDataset.VESSEL_IDENTITY_LATEST,
        serialization_alias="dataset",
        description="Dataset that will be used to search the vessel.",
    )
    registries_info_data: Optional[VesselRegistryInfoData] = Field(
        VesselRegistryInfoData.NONE,
        serialization_alias="registries-info-data",
        description="Registry info data criteria.",
    )
    includes: Optional[List[VesselInclude]] = Field(
        [VesselInclude.POTENTIAL_RELATED_SELF_REPORTED_INFO],
        serialization_alias="includes",
        description="Whether to add extra information to the response.",
    )
    binary: Optional[bool] = Field(
        False,
        serialization_alias="binary",
        description="Whether response should be in binary format (proto buffer) or not.",
    )
    match_fields: Optional[List[VesselMatchField]] = Field(
        [VesselMatchField.ALL],
        serialization_alias="match-fields",
        description="Filter by matchFields levels criteria.",
    )
