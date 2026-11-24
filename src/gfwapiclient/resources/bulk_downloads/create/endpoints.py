"""Global Fishing Watch (GFW) API Python Client - Create a Bulk Report API endpoint."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import PostEndPoint
from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.bulk_downloads.create.models.request import (
    BulkReportCreateBody,
)
from gfwapiclient.resources.bulk_downloads.create.models.response import (
    BulkReportCreateItem,
    BulkReportCreateResult,
)


__all__ = ["BulkReportCreateEndPoint"]


class BulkReportCreateEndPoint(
    PostEndPoint[
        RequestParams,
        BulkReportCreateBody,
        BulkReportCreateItem,
        BulkReportCreateResult,
    ]
):
    """Create a Bulk Report API endpoint.

    This endpoint is used to create bulk reports based on the provided request body.

    For more details on the Create a Bulk Report API endpoint, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/create-bulk-report
    """

    def __init__(
        self,
        *,
        request_body: BulkReportCreateBody,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `BulkReportCreateEndPoint`.

        Args:
            request_body (BulkReportCreateBody):
                The request body.

            http_client (HTTPClient):
                The HTTP client for making API requests.
        """
        super().__init__(
            path="bulk-reports",
            request_params=None,
            request_body=request_body,
            result_item_class=BulkReportCreateItem,
            result_class=BulkReportCreateResult,
            http_client=http_client,
        )
