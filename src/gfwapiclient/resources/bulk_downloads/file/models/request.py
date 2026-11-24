"""Global Fishing Watch (GFW) API Python Client - Download bulk Report (URL File) Request Models."""

from typing import Final, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.bulk_downloads.base.models.request import BulkReportFileType


__all__ = ["BulkReportFileParams"]


BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Get bulk report file download URL request parameters validation failed."
)


class BulkReportFileParams(RequestParams):
    """Request query parameters for Download bulk Report (URL File) API endpoint.

    Represents request query parameters to obtain signed URL to download the file
    (i.e., `"DATA"`, `"README"`, or `"GEOM"`) of the previously created bulk report.

    For more details on the Download bulk Report (URL File) API endpoint supported
    request parameters, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/download-file#parameters-query

    Attributes:
        file (Optional[BulkReportFileType]):
            Type of bulk report file (i.e., `"DATA"`, `"README"`, or `"GEOM"`).
    """

    file: Optional[BulkReportFileType] = Field(BulkReportFileType.DATA, alias="file")
