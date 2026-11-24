"""Global Fishing Watch (GFW) API Python Client - Download bulk Report (URL File) Response Models."""

from typing import Optional, Type

from pydantic import Field

from gfwapiclient.http.models import Result, ResultItem


__all__ = ["BulkReportFileItem", "BulkReportFileResult"]


class BulkReportFileItem(ResultItem):
    """Result item for the Download bulk Report (URL File) API endpoint.

    Represents signed URL to download the file (i.e., `"DATA"`, `"README"`,
    or `"GEOM"`) of the previously created bulk report.

    For more details on the Download bulk Report (URL File) API endpoint supported
    response bodies, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/download-file#download-bulk-report--response

    Attributes:
        url (Optional[str]):
            Signed URL to download the file.
    """

    url: Optional[str] = Field(None, alias="url")


class BulkReportFileResult(Result[BulkReportFileItem]):
    """Result for the Download bulk Report (URL File) API endpoint.

    For more details on the Download bulk Report (URL File) API endpoint supported
    response bodies, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/download-file#download-bulk-report--response

    Attributes:
        _result_item_class (Type[BulkReportFileItem]):
            The model used for individual result items.

        _data (BulkReportFileItem):
            The bulk report file item returned in the response.
    """

    _result_item_class: Type[BulkReportFileItem]
    _data: BulkReportFileItem

    def __init__(self, data: BulkReportFileItem) -> None:
        """Initializes a new `BulkReportFileResult`.

        Args:
            data (BulkReportFileItem):
                The bulk report file download details.
        """
        super().__init__(data=data)
