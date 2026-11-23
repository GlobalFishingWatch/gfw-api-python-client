"""Global Fishing Watch (GFW) API Python Client -  Get Bulk Report by ID Response Models."""

from typing import Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.bulk_downloads.base.models.response import BulkReportItem


__all__ = ["BulkReportDetailItem", "BulkReportDetailResult"]


class BulkReportDetailItem(BulkReportItem):
    """Result item for the Get Bulk Report by ID API endpoint.

    Represents metadata and status of the previously created bulk report.

    For more details on the Get Bulk Report by ID API endpoint supported
    response bodies, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/get-bulk-report-id#get-bulk-report-by-id---response-fields

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/create-bulk-report#bulk-report---response-fields

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/get-bulk-report-users#bulk-reports-get---response-fields
    """

    pass


class BulkReportDetailResult(Result[BulkReportDetailItem]):
    """Result for the Get Bulk Report by ID API endpoint.

    For more details on the Get Bulk Report by ID API endpoint supported
    response bodies, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/get-bulk-report-id-http-response

    Attributes:
        _result_item_class (Type[BulkReportDetailItem]):
            The model used for individual result items.

        _data (BulkReportDetailItem):
            The bulk report item returned in the response.
    """

    _result_item_class: Type[BulkReportDetailItem]
    _data: BulkReportDetailItem

    def __init__(self, data: BulkReportDetailItem) -> None:
        """Initializes a new `BulkReportDetailResult`.

        Args:
            data (BulkReportDetailItem):
                The bulk report details.
        """
        super().__init__(data=data)
