"""Global Fishing Watch (GFW) API Python Client - Vessels List API Request Models."""

from typing import ClassVar, List, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.vessels.base.enums import (
    VesselDataset,
    VesselInclude,
    VesselMatchField,
    VesselRegistryInfoData,
)


__all__ = ["VesselListParams"]


class VesselListParams(RequestParams):
    """Request query parameters for get list of vessels filtered by ids API endpoint."""

    indexed_fields: ClassVar[Optional[List[str]]] = [
        "datasets",
        "includes",
        "match-fields",
        "ids",
        "vessel-groups",
    ]

    datasets: List[VesselDataset] = Field(
        [VesselDataset.VESSEL_IDENTITY_LATEST],
        serialization_alias="datasets",
        description="Datasets that will be used to search the vessel.",
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
    ids: List[str] = Field(
        ..., serialization_alias="ids", description="List of vessel ids."
    )
    vessel_groups: Optional[List[str]] = Field(
        None, serialization_alias="vessel-groups", description="List of vessel groups."
    )
