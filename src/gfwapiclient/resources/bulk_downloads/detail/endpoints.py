"""Global Fishing Watch (GFW) API Python Client - Get Bulk Report by ID API endpoint."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import GetEndPoint
from gfwapiclient.http.models import RequestBody, RequestParams
from gfwapiclient.resources.bulk_downloads.detail.models.response import (
    BulkReportDetailItem,
    BulkReportDetailResult,
)


__all__ = ["BulkReportDetailEndPoint"]


class BulkReportDetailEndPoint(
    GetEndPoint[
        RequestParams, RequestBody, BulkReportDetailItem, BulkReportDetailResult
    ],
):
    """Get Bulk Report by ID API endpoint.

    This endpoint retrieves metadata and status of the previously created bulk report
    based on the provided bulk report ID.

    For more details on the Get Bulk Report by ID API endpoint, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/get-bulk-report-id

    For more details on the Get Bulk Report by ID data caveats, please refer
    to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#sar-fixed-infrastructure-data-caveats
    """

    def __init__(
        self,
        *,
        bulk_report_id: str,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `BulkReportDetailEndPoint`.

        Args:
            bulk_report_id (str):
                Unique identifier (ID) of the bulk report.

            http_client (HTTPClient):
                The HTTP client used to make the API call.
        """
        super().__init__(
            path=f"bulk-reports/{bulk_report_id}",
            request_params=None,
            result_item_class=BulkReportDetailItem,
            result_class=BulkReportDetailResult,
            http_client=http_client,
        )
