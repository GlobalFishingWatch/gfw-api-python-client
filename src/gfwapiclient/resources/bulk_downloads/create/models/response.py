"""Global Fishing Watch (GFW) API Python Client - Create a Bulk Report Response Models."""

from typing import Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.bulk_downloads.base.models.response import BulkReportItem


__all__ = ["BulkReportCreateItem", "BulkReportCreateResult"]


class BulkReportCreateItem(BulkReportItem):
    """Result item for the Create a Bulk Report API endpoint.

    Represents metadata and status of the created bulk report.

    For more details on the Create a Bulk Report API endpoint supported
    response bodies, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/create-bulk-report#bulk-report---response-fields

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/get-bulk-report-users#bulk-reports-get---response-fields
    """

    pass


class BulkReportCreateResult(Result[BulkReportCreateItem]):
    """Result for the Create a Bulk Report API endpoint.

    For more details on the Create a Bulk Report API endpoint supported
    response bodies, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/create-bulk-report#bulk-report---response-fields

    Attributes:
        _result_item_class (Type[BulkReportFileItem]):
            The model used for individual result items.

        _data (BulkReportCreateItem):
            The bulk report item returned in the response.
    """

    _result_item_class: Type[BulkReportCreateItem]
    _data: BulkReportCreateItem

    def __init__(self, data: BulkReportCreateItem) -> None:
        """Initializes a new `BulkReportCreateResult`.

        Args:
            data (BulkReportCreateItem):
                The created bulk report details.
        """
        super().__init__(data=data)
