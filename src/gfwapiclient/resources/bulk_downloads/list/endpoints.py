"""Global Fishing Watch (GFW) API Python Client - Get All Bulk Reports API endpoint."""

from typing import Any, Dict, List, Union

from typing_extensions import override

from gfwapiclient.exceptions.validation import ResultValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import GetEndPoint
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.bulk_downloads.list.models.request import (
    BulkReportListParams,
)
from gfwapiclient.resources.bulk_downloads.list.models.response import (
    BulkReportListItem,
    BulkReportListResult,
)


__all__ = ["BulkReportListEndPoint"]


class BulkReportListEndPoint(
    GetEndPoint[
        BulkReportListParams, RequestBody, BulkReportListItem, BulkReportListResult
    ],
):
    """Get All Bulk Reports API endpoint.

    This endpoint retrieves a list of metadata and status of the previously created
    bulk reports based on the provided request parameters.

    For more details on the Get All Bulk Reports API endpoint, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/get-bulk-report-users
    """

    def __init__(
        self,
        *,
        request_params: BulkReportListParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `BulkReportListEndPoint`.

        Args:
            request_params (BulkReportListParams):
                The request parameters.

            http_client (HTTPClient):
                The HTTP client used to make the API call.
        """
        super().__init__(
            path="bulk-reports",
            request_params=request_params,
            result_item_class=BulkReportListItem,
            result_class=BulkReportListResult,
            http_client=http_client,
        )

    @override
    def _transform_response_data(
        self,
        *,
        body: Union[List[Dict[str, Any]], Dict[str, Any]],
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Transform and reshape response body and yield data.

        This method transforms the raw response body from the API into a format
        suitable for the `BulkReportListResult` model.

        The expected response structure is: `{"entries": [{...}]}`.

        Args:
            body (Union[List[Dict[str, Any]], Dict[str, Any]]):
                The raw response body.

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]:
                The transformed response data.

        Raises:
            ResultValidationError:
                If the response body does not match the expected format.
        """
        # expected: {"entries": [{"key": ...}, ...], ...}
        if not isinstance(body, dict) or "entries" not in body:
            raise ResultValidationError(
                message="Expected a list of entries, but got an empty list.",
                body=body,
            )

        # Transforming and reshaping entries
        bulk_report_entries: List[Dict[str, Any]] = body.get("entries", [])
        transformed_data: List[Dict[str, Any]] = []

        # Loop through "entries" list i.e [{"key": ..., ...}, ...]
        for bulk_report_entry in bulk_report_entries:
            # Append extracted dictionaries, if not empty
            if bulk_report_entry:
                transformed_data.append(dict(**bulk_report_entry))

        return transformed_data
