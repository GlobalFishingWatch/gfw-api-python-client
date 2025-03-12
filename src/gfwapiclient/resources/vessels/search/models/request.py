"""Global Fishing Watch (GFW) API Python Client - Vessels Search API Request Models."""

from enum import Enum
from typing import ClassVar, List, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.vessels.base.enums import (
    VesselDataset,
    VesselMatchField,
)


__all__ = ["VesselSearchParams"]


class VesselSearchInclude(str, Enum):
    """Extra information that can be included in a vessel search.

    Attributes:
        OWNERSHIP (str):
            Includes vessel ownership details.

        AUTHORIZATIONS (str):
            Includes vessel authorization details.

        MATCH_CRITERIA (str):
            Includes criteria used for matching vessels.
    """

    OWNERSHIP = "OWNERSHIP"
    AUTHORIZATIONS = "AUTHORIZATIONS"
    MATCH_CRITERIA = "MATCH_CRITERIA"


class VesselSearchParams(RequestParams):
    """Request query parameters for vessels search API endpoint."""

    indexed_fields: ClassVar[Optional[List[str]]] = [
        "datasets",
        "match-fields",
        "includes",
    ]

    since: Optional[str] = Field(
        None,
        serialization_alias="since",
        description="The token to send to get more results.",
    )
    limit: Optional[int] = Field(
        20,
        serialization_alias="limit",
        description="Amount of search results to return.",
    )
    datasets: List[VesselDataset] = Field(
        [VesselDataset.VESSEL_IDENTITY_LATEST],
        serialization_alias="datasets",
        description="Datasets that will be used to search the vessel.",
    )
    query: Optional[str] = Field(
        None,
        serialization_alias="query",
        description="Free form query that allows you to search a vessel by sending some identifier.",
    )
    where: Optional[str] = Field(
        None,
        serialization_alias="where",
        description="Advanced query that allows you to search a vessel by sending several identifiers.",
    )
    match_fields: Optional[List[VesselMatchField]] = Field(
        [VesselMatchField.ALL],
        serialization_alias="match-fields",
        description="Filter by matchFields levels criteria.",
    )
    includes: Optional[List[VesselSearchInclude]] = Field(
        list(VesselSearchInclude),
        serialization_alias="includes",
        description="Whether to add extra information to the response.",
    )
    binary: Optional[bool] = Field(
        False,
        serialization_alias="binary",
        description="Whether response should be in binary format (proto buffer) or not.",
    )
