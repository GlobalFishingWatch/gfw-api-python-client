"""Global Fishing Watch (GFW) API Python Client - Vessels Search API EndPoint.

This module defines the endpoint for searching vessels.
"""

from typing import Any, Dict, List, Union

from typing_extensions import override

from gfwapiclient.exceptions.validation import ResultValidationError
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
    GetEndPoint[VesselSearchParams, RequestBody, VesselSearchItem, VesselSearchResult],
):
    """Search vessels API endpoint.

    This endpoint searches for vessels based on the provided search request parameters.
    """

    def __init__(
        self,
        *,
        request_params: VesselSearchParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `VesselSearchEndPoint` API endpoint.

        Args:
            request_params (VesselSearchParams):
                The search parameters for the API call.

            http_client (HTTPClient):
                The HTTP client used to make the API call.
        """
        super().__init__(
            path="vessels/search",
            request_params=request_params,
            result_item_class=VesselSearchItem,
            result_class=VesselSearchResult,
            http_client=http_client,
        )

    @override
    def _transform_response_data(
        self,
        *,
        body: Union[List[Dict[str, Any]], Dict[str, Any]],
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Transform and reshape response body and yield data.

        This method transforms the raw response body from the API into a format
        suitable for the `VesselSearchResult` model.

        The expected response structure is: `{"entries": [{...}]}`.

        Args:
            body (Union[List[Dict[str, Any]], Dict[str, Any]]):
                The raw response body.

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]:
                The transformed response data.

        Raises:
            ResultValidationError:
                If the response body does not match the expected format.
        """
        # expected: {entries: [{"key": [{}]}]}
        if not isinstance(body, dict) or "entries" not in body:
            raise ResultValidationError(
                message="Expected a list of entries, but got an empty list.",
                body=body,
            )

        # Transforming and reshaping entries
        vessel_entries: List[Dict[str, Any]] = body.get("entries", [])
        transformed_data: List[Dict[str, Any]] = []

        # Loop through "entries" list i.e {"entries": [{"dataset": [{...}]}]}
        for vessel_entry in vessel_entries:
            # Append extracted dictionaries, if not empty
            if vessel_entry:
                transformed_data.append(dict(**vessel_entry))

        return transformed_data
