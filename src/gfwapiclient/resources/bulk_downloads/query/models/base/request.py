"""Global Fishing Watch (GFW) API Python Client - Query Bulk Report Base Request Models."""

from typing import ClassVar, Final, List, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestParams


__all__ = ["BulkReportQueryParams"]


BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Query bulk report request parameters validation failed."
)


class BulkReportQueryParams(RequestParams):
    """Request query parameters for Query Bulk Report API endpoint.

    Represents pagination, sorting, filtering parameters etc. for querying previously
    created bulk report data.

    For more details on the Query Bulk Report API endpoint supported request parameters,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/query-bulk-report

    Attributes:
        limit (Optional[int]):
            Maximum number of bulk report records to return.
            Defaults to `99999`.

        offset (Optional[int]):
            Number of bulk report records to skip before returning results.
            Used for pagination. Defaults to `0`.

        sort (Optional[str]):
            Property to sort the bulk report records by (e.g.
            `"-structure_start_date"`).

        includes (Optional[List[str]]):
            List of bulk report record fields to include in the result.
    """

    indexed_fields: ClassVar[Optional[List[str]]] = ["includes"]

    limit: Optional[int] = Field(99999, ge=0, alias="limit")
    offset: Optional[int] = Field(0, ge=0, alias="offset")
    sort: Optional[str] = Field(None, alias="sort")
    includes: Optional[List[str]] = Field(None, alias="includes")
