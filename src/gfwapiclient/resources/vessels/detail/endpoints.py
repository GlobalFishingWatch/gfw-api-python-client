"""Global Fishing Watch (GFW) API Python Client - Get Vessel by ID API EndPoint.

This module defines the endpoint for retrieving vessel details by ID.
"""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import GetEndPoint
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.vessels.detail.models.request import VesselDetailParams
from gfwapiclient.resources.vessels.detail.models.response import (
    VesselDetailItem,
    VesselDetailResult,
)


__all__ = ["VesselDetailEndPoint"]


class VesselDetailEndPoint(
    GetEndPoint[VesselDetailParams, RequestBody, VesselDetailItem, VesselDetailResult],
):
    """Get vessel by ID API endpoint.

    This endpoint retrieves vessel details by ID and
    other provided request parameters.
    """

    def __init__(
        self,
        *,
        vessel_id: str,
        request_params: VesselDetailParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `VesselDetailEndPoint` API endpoint.

        Args:
            vessel_id (str):
                The ID of the vessel to retrieve.

            request_params (VesselDetailParams):
                The request parameters for the API call.

            http_client (HTTPClient):
                The HTTP client used to make the API call.
        """
        super().__init__(
            path=f"vessels/{vessel_id}",
            request_params=request_params,
            result_item_class=VesselDetailItem,
            result_class=VesselDetailResult,
            http_client=http_client,
        )
