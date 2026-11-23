"""Global Fishing Watch (GFW) API Python Client - Query Bulk Report API endpoints."""

from typing import Any, Dict, List, Type, Union

from typing_extensions import override

from gfwapiclient.exceptions.validation import ResultValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import GetEndPoint
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.bulk_downloads.query.models.base.request import (
    BulkReportQueryParams,
)
from gfwapiclient.resources.bulk_downloads.query.models.base.response import (
    _BulkReportQueryItemT,
    _BulkReportQueryResultT,
)
from gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response import (
    BulkFixedInfrastructureDataQueryItem,
    BulkFixedInfrastructureDataQueryResult,
)


__all__ = ["BulkFixedInfrastructureDataQueryEndPoint", "BulkReportQueryEndPoint"]


class BulkReportQueryEndPoint(
    GetEndPoint[
        BulkReportQueryParams,
        RequestBody,
        _BulkReportQueryItemT,
        _BulkReportQueryResultT,
    ],
):
    """Query Bulk Report API endpoint.

    This endpoint query the previously created bulk report data in JSON format
    based on the provided request parameters.

    For more details on the Query Bulk Report API endpoint, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/query-bulk-report
    """

    def __init__(
        self,
        *,
        bulk_report_id: str,
        request_params: BulkReportQueryParams,
        result_item_class: Type[_BulkReportQueryItemT],
        result_class: Type[_BulkReportQueryResultT],
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `BulkReportQueryEndPoint`.

        Args:
            bulk_report_id (str):
                Unique identifier (ID) of the bulk report.

            request_params (BulkReportQueryParams):
                The request parameters.

            result_item_class (Type[_BulkReportQueryItemT]):
                Pydantic model for the expected response item.

            result_class (Type[_BulkReportQueryResultT]):
                Pydantic model for the expected response result.

            http_client (HTTPClient):
                The HTTP client used to make the API call.
        """
        super().__init__(
            path=f"bulk-reports/{bulk_report_id}/query",
            request_params=request_params,
            result_item_class=result_item_class,
            result_class=result_class,
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
        suitable for the `BulkReportQueryResult` model.

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
        bulk_report_data_entries: List[Dict[str, Any]] = body.get("entries", [])
        transformed_data: List[Dict[str, Any]] = []

        # Loop through "entries" list i.e [{"key": ..., ...}, ...]
        for bulk_report_data_entry in bulk_report_data_entries:
            # Append extracted dictionaries, if not empty
            if bulk_report_data_entry:
                transformed_data.append(dict(**bulk_report_data_entry))

        return transformed_data


class BulkFixedInfrastructureDataQueryEndPoint(
    BulkReportQueryEndPoint[
        BulkFixedInfrastructureDataQueryItem,
        BulkFixedInfrastructureDataQueryResult,
    ],
):
    """Query Bulk fixed infrastructure data API endpoint.

    This endpoint query the previously created fixed infrastructure data (i.e.,
    `public-fixed-infrastructure-data:latest` dataset) bulk report data in JSON format
    based on the provided request parameters.

    For more details on the Query Bulk Report API endpoint, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/query-bulk-report
    """

    def __init__(
        self,
        *,
        bulk_report_id: str,
        request_params: BulkReportQueryParams,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `BulkFixedInfrastructureDataQueryEndPoint`.

        Args:
            bulk_report_id (str):
                Unique identifier (ID) of the bulk report.

            request_params (BulkReportQueryParams):
                The request parameters.

            http_client (HTTPClient):
                The HTTP client used to make the API call.
        """
        super().__init__(
            bulk_report_id=bulk_report_id,
            request_params=request_params,
            result_item_class=BulkFixedInfrastructureDataQueryItem,
            result_class=BulkFixedInfrastructureDataQueryResult,
            http_client=http_client,
        )
