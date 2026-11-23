"""Global Fishing Watch (GFW) API Python Client - Download bulk Report (URL File) API endpoint."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import GetEndPoint
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.bulk_downloads.file.models.request import (
    BulkReportFileParams,
)
from gfwapiclient.resources.bulk_downloads.file.models.response import (
    BulkReportFileItem,
    BulkReportFileResult,
)


__all__ = ["BulkReportFileEndPoint"]


class BulkReportFileEndPoint(
    GetEndPoint[
        BulkReportFileParams, RequestBody, BulkReportFileItem, BulkReportFileResult
    ],
):
    """Download bulk Report (URL File) API endpoint.

    This endpoint is used to retrieve signed URL to download file(s) (i.e., `"DATA"`,
    `"README"`, or `"GEOM"`) of the previously created bulk report.

    For more details on the Download bulk Report (URL File) API endpoint, please refer
    to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/download-file

    For more details on the Download bulk Report (URL File) data caveats, please refer
    to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#sar-fixed-infrastructure-data-caveats
    """

    def __init__(
        self,
        *,
        bulk_report_id: str,
        request_params: BulkReportFileParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `BulkReportFileEndPoint`.

        Args:
            bulk_report_id (str):
                Unique identifier (ID) of the bulk report.

            request_params (BulkReportFileParams):
                The request query parameters.

            http_client (HTTPClient):
                The HTTP client used to make the API call.
        """
        super().__init__(
            path=f"bulk-reports/{bulk_report_id}/download-file-url",
            request_params=request_params,
            result_item_class=BulkReportFileItem,
            result_class=BulkReportFileResult,
            http_client=http_client,
        )
