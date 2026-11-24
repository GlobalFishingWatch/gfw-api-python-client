"""Global Fishing Watch (GFW) API Python Client - Query Bulk Report Base Response Models."""

from typing import Any, List, Type, TypeVar

from gfwapiclient.http.models import Result, ResultItem


__all__ = [
    "BulkReportQueryItem",
    "BulkReportQueryResult",
    "_BulkReportQueryItemT",
    "_BulkReportQueryResultT",
]


class BulkReportQueryItem(ResultItem):
    """Result item for the Query Bulk Report API endpoint.

    Represents a data record of a previously created bulk report.

    For more details on the Query Bulk Report API endpoint supported response bodies,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/query-bulk-report
    """

    pass


_BulkReportQueryItemT = TypeVar("_BulkReportQueryItemT", bound=BulkReportQueryItem)


class BulkReportQueryResult(Result[_BulkReportQueryItemT]):
    """Result for the Query Bulk Report API endpoint.

    Represents data records of a previously created bulk report.

    For more details on the Query Bulk Report API endpoint supported response bodies,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/query-bulk-report

    Attributes:
        _result_item_class (Type[_BulkReportQueryItemT]):
            The model used for individual result items.

        _data (List[_BulkReportQueryItemT]):
            The bulk report data item returned in the response.
    """

    _result_item_class: Type[_BulkReportQueryItemT]
    _data: List[_BulkReportQueryItemT]

    def __init__(self, data: List[_BulkReportQueryItemT]) -> None:
        """Initializes a new `BulkReportQueryResult`.

        Args:
            data (List[_BulkReportQueryItemT]):
                The list of bulk report data items.
        """
        super().__init__(data=data)


_BulkReportQueryResultT = TypeVar(
    "_BulkReportQueryResultT", bound=BulkReportQueryResult[Any]
)
