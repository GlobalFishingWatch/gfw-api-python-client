"""Global Fishing Watch (GFW) API Python Client - Get Vessels Insights API Endpoint."""

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

    For detailed information about the Get Vessels Insights API endpoint, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#insights-by-vessels

    See: https://globalfishingwatch.org/our-apis/documentation#insights-by-vessels-body

    For more details on the Get Vessels Insights data caveats, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-detected-in-no-take-mpas

    See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-that-an-api-dataset-is-in-prototype-stage

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-event-detected-outside-known-authorized-areas

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-coverage

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-rfmo-iuu-vessel-list
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
