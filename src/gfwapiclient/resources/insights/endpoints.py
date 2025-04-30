"""Global Fishing Watch (GFW) API Python Client - Vessels Insights API EndPoints."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import PostEndPoint
from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.insights.models.request import (
    VesselInsightBody,
)
from gfwapiclient.resources.insights.models.response import (
    VesselInsightItem,
    VesselInsightResult,
)


class VesselInsightEndPoint(
    PostEndPoint[
        RequestParams, VesselInsightBody, VesselInsightItem, VesselInsightResult
    ]
):
    """Get Vessels Insights API endpoint.

    This endpoint retrieves insights for specified vessels based on the provided
    request parameters.
    """

    def __init__(
        self,
        *,
        request_body: VesselInsightBody,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `VesselInsightEndPoint` API endpoint.

        Args:
            request_body (VesselInsightBody):
                The request body containing vessel insight parameters.

            http_client (HTTPClient):
                The HTTP client for making API requests.
        """
        super().__init__(
            path="insights/vessels",
            request_params=None,
            request_body=request_body,
            result_item_class=VesselInsightItem,
            result_class=VesselInsightResult,
            http_client=http_client,
        )
