"""Global Fishing Watch (GFW) API Python Client - Vessels Search API EndPoint."""

from typing import Any, Dict, List, Union, override

import pydantic

from pydantic_core import ErrorDetails

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import GetEndPoint
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.vessels.search.models.request import VesselSearchParams
from gfwapiclient.resources.vessels.search.models.response import (
    VesselSearchItem,
    VesselSearchResult,
)


__all__ = ["VesselSearchEndPoint"]


class VesselSearchEndPoint(
    GetEndPoint[
        VesselSearchParams,
        RequestBody,
        VesselSearchItem,
        VesselSearchResult,
    ],
):
    """Search vessels API endpoint."""

    def __init__(
        self,
        request_params: VesselSearchParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `VesselSearchEndPoint` API endpoint."""
        super().__init__(
            path="vessels/search",
            request_params=request_params,
            result_item_class=VesselSearchItem,
            result_class=VesselSearchResult,
            http_client=http_client,
        )

    @override
    def _transform_response_body(
        self,
        body: Union[List[Dict[str, Any]], Dict[str, Any]],
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Transform and reshape response body and yield data."""
        # expected: {entries: [{"key": [{}]}]}
        if not isinstance(body, dict) or "entries" not in body:
            # TODO: raise APIResponseDataError | APIResultItemValidationError | APIResultValidationError
            errors = [
                ErrorDetails(
                    type="value_error",
                    loc=("entries",),
                    msg="Expected a list of entries, but got an empty list.",
                    input=None,
                )
            ]
            raise pydantic.ValidationError(errors, VesselSearchResult)

        # TODO: update pagination options|params(since:str, limit:int)

        # Transforming and reshaping entries
        vessel_entries: List[Dict[str, Any]] = body.get("entries", [])
        transformed_data: List[Dict[str, Any]] = []

        # Loop through "entries" list i.e {"entries": [{"dataset": [{...}]}]}
        for vessel_entry in vessel_entries:
            # Append extracted dictionaries
            transformed_data.append(vessel_entry)

        return transformed_data
