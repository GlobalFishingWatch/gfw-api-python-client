"""Global Fishing Watch (GFW) API Python Client - Get All Bulk Reports Request Models."""

from typing import Final, Optional, Union

from pydantic import Field

from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.bulk_downloads.base.models.request import BulkReportDataset
from gfwapiclient.resources.bulk_downloads.base.models.response import BulkReportStatus


__all__ = ["BulkReportListParams"]


BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Get bulk reports request parameters validation failed."
)


class BulkReportListParams(RequestParams):
    """Request query parameters for Get All Bulk Reports API endpoint.

    Represents pagination, sorting, filtering parameters etc. for retrieving
    previously created bulk reports.

    For more details on the Get All Bulk Reports API endpoint supported
    request parameters, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#get-all-bulk-reports-by-user

    Attributes:
        limit (Optional[int]):
            Maximum number of bulk reports to return.
            Defaults to `99999`.

        offset (Optional[int]):
            Number of bulk reports to skip before returning results.
            Used for pagination. Defaults to `0`.

        sort (Optional[str]):
            Property to sort the bulk reports by (e.g., `"-createdAt"`).

        status (Optional[BulkReportStatus]):
            Current status of the bulk report generation process (e.g., `"done"` etc.).

        dataset (Optional[str]):
            The dataset used to create the bulk report (e.g.,
            `"public-fixed-infrastructure-data:latest"`,
            `"public-fixed-infrastructure-data:v1.1"` etc.).
    """

    limit: Optional[int] = Field(99999, ge=0, alias="limit")
    offset: Optional[int] = Field(0, ge=0, alias="offset")
    sort: Optional[str] = Field("-createdAt", alias="sort")
    status: Optional[BulkReportStatus] = Field(None, alias="status")
    dataset: Optional[Union[BulkReportDataset, str]] = Field(None, alias="dataset")
