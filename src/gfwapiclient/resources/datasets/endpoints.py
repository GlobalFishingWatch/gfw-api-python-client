"""Global Fishing Watch (GFW) API Python Client - Datasets API EndPoints."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints.get import GetEndPoint
from gfwapiclient.http.models import RequestBody, RequestParams
from gfwapiclient.resources.datasets.models.response import (
    SARFixedInfrastructureItem,
    SARFixedInfrastructureResult,
)


class SARFixedInfrastructureEndPoint(
    GetEndPoint[
        RequestParams,
        RequestBody,
        SARFixedInfrastructureItem,
        SARFixedInfrastructureResult,
    ]
):
    """Get SAR fixed infrastructure API endpoint.

    This endpoint retrieves SAR fixed infrastructure data based on the provided
    request parameters.
    """

    def __init__(
        self,
        *,
        z: int,
        x: int,
        y: int,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `SARFixedInfrastructureEndPoint` API endpoint.

        Args:
            z: (int):
                Zoom level (from 0 to 9 for SAR fixed infrastructure dataset).
                Example: `1`.

            x: (int):
                X index (lat) of the tile.
                Example: `0`.

            y: (int):
                Y index (lon) of the tile.
                Example: `1`.

            http_client (HTTPClient):
                The HTTP client for making API requests.
        """
        super().__init__(
            path=f"datasets/public-fixed-infrastructure-filtered:latest/context-layers/{z}/{x}/{y}",
            request_params=None,
            result_item_class=SARFixedInfrastructureItem,
            result_class=SARFixedInfrastructureResult,
            http_client=http_client,
        )
