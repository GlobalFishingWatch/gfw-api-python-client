"""Global Fishing Watch (GFW) API Python Client - Get Vessels by IDs API EndPoint.

This module defines the endpoint for retrieving a list of vessels by IDs.
"""

from typing import Any, Dict, List, Union

from typing_extensions import override

from gfwapiclient.exceptions.validation import ResultValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import GetEndPoint
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.vessels.list.models.request import VesselListParams
from gfwapiclient.resources.vessels.list.models.response import (
    VesselListItem,
    VesselListResult,
)


__all__ = ["VesselListEndPoint"]


class VesselListEndPoint(
    GetEndPoint[VesselListParams, RequestBody, VesselListItem, VesselListResult],
):
    """Get list of vessels by IDs API endpoint.

    This endpoint retrieves a list of vessels based on the provided IDs and
    other request parameters.
    """

    def __init__(
        self,
        *,
        request_params: VesselListParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `VesselListEndPoint` API endpoint.

        Args:
            request_params (VesselListParams):
                The request parameters containing the vessel IDs.

            http_client (HTTPClient):
                The HTTP client used to make the API call.
        """
        super().__init__(
            path="vessels",
            request_params=request_params,
            result_item_class=VesselListItem,
            result_class=VesselListResult,
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
        suitable for the `VesselListResult` model.

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

        # Loop through "entries" list i.e [{"dataset": ..., ...}, ...]
        for vessel_entry in vessel_entries:
            # Append extracted dictionaries, if not empty
            if vessel_entry:
                transformed_data.append(dict(**vessel_entry))

        return transformed_data
