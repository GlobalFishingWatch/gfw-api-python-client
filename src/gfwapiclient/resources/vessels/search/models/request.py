"""Global Fishing Watch (GFW) API Python Client - Vessels Search API Request Models.

This module defines request models for the Vessels API's search vessels endpoint.
"""

from enum import Enum
from typing import ClassVar, Final, List, Optional

from pydantic import Field

from gfwapiclient.resources.vessels.base.models.request import (
    VesselBaseParams,
    VesselDataset,
)


__all__ = ["VesselSearchParams"]


VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Search vessels request parameters validation failed."
)


class VesselSearchInclude(str, Enum):
    """Enumeration of extra information that can be included in a vessel search.

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


class VesselSearchParams(VesselBaseParams):
    """Request query parameters for the vessels search API endpoint.

    Attributes:
        since (Optional[str]):
            The token to send to get more results.

        limit (Optional[int]):
            Amount of search results to return. Defaults to 20.

        datasets (List[VesselDataset]):
            Datasets that will be used to search the vessel.

        query (Optional[str]):
            Free form query that allows you to search a vessel by sending some
            identifier.

        where (Optional[str]):
            Advanced query that allows you to search a vessel by sending several
            identifiers.

        includes (Optional[List[VesselSearchInclude]]):
            Whether to add extra information to the response.
    """

    indexed_fields: ClassVar[Optional[List[str]]] = [
        "datasets",
        "match-fields",
        "includes",
    ]

    since: Optional[str] = Field(None, serialization_alias="since")
    limit: Optional[int] = Field(20, le=50, serialization_alias="limit")
    datasets: List[VesselDataset] = Field(
        [VesselDataset.VESSEL_IDENTITY_LATEST], serialization_alias="datasets"
    )
    query: Optional[str] = Field(None, serialization_alias="query")
    where: Optional[str] = Field(None, serialization_alias="where")
    includes: Optional[List[VesselSearchInclude]] = Field(
        list(VesselSearchInclude), serialization_alias="includes"
    )
