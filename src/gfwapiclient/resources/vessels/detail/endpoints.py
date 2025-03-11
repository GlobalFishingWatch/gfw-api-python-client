"""Global Fishing Watch (GFW) API Python Client - Vessel Detail API EndPoint."""

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
    GetEndPoint[
        VesselDetailParams,
        RequestBody,
        VesselDetailItem,
        VesselDetailResult,
    ],
):
    """Get vessel by id API endpoint."""

    def __init__(
        self,
        vessel_id: str,
        request_params: VesselDetailParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `VesselDetailEndPoint` API endpoint."""
        super().__init__(
            path=f"vessels/{vessel_id}",
            request_params=request_params,
            result_item_class=VesselDetailItem,
            result_class=VesselDetailResult,
            http_client=http_client,
        )
