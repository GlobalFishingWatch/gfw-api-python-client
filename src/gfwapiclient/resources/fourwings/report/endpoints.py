"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API EndPoint."""

from typing import Any, Dict, List, Union

from typing_extensions import override

from gfwapiclient.exceptions.validation import ResultValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import PostEndPoint
from gfwapiclient.resources.fourwings.report.models.request import (
    FourWingsReportBody,
    FourWingsReportParams,
)
from gfwapiclient.resources.fourwings.report.models.response import (
    FourWingsReportItem,
    FourWingsReportResult,
)


__all__ = ["FourWingsReportEndPoint"]


class FourWingsReportEndPoint(
    PostEndPoint[
        FourWingsReportParams,
        FourWingsReportBody,
        FourWingsReportItem,
        FourWingsReportResult,
    ]
):
    """Create 4Wings Report API endpoint.

    This endpoint is used to generate reports from the 4Wings API.
    It supports both query parameters and request bodies for flexible report generation.
    """

    def __init__(
        self,
        *,
        request_params: FourWingsReportParams,
        request_body: FourWingsReportBody,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `FourWingsReportEndPoint` API endpoint.

        Args:
            request_params (FourWingsReportParams):
                The request query parameters.

            request_body (FourWingsReportBody):
                The request body.

            http_client (HTTPClient):
                The HTTP client.
        """
        super().__init__(
            path="4wings/report",
            request_params=request_params,
            request_body=request_body,
            result_item_class=FourWingsReportItem,
            result_class=FourWingsReportResult,
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
        suitable for the `FourWingsReportResult` model.

        The expected response structure is: `{"entries": [{"dataset": [{...}]}]}`.

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
        # expected: {entries: [{"key": [{}]}]}
        if not isinstance(body, dict) or "entries" not in body:
            raise ResultValidationError(
                message="Expected a list of entries, but got an empty list.",
                body=body,
            )

        # Transforming and reshaping entries
        report_entries: List[Dict[str, Any]] = body.get("entries", [])
        transformed_data: List[Dict[str, Any]] = []

        # Loop through "entries" list i.e {"entries": [{"dataset": [{...}]}]}
        for report_entry in report_entries:
            # Loop through each dataset "entries" list i.e {"dataset": [{...}]}
            for report_dataset, report_dataset_entries in report_entry.items():
                # Extract actual report item data i.e [{...}]}
                for report_dataset_entry in report_dataset_entries or []:
                    # Reshape
                    _report_dataset_entry = {
                        "report_dataset": report_dataset,
                        **report_dataset_entry,
                    }
                    # Append extracted report dataset entry dictionaries
                    transformed_data.append(_report_dataset_entry)

        return transformed_data
