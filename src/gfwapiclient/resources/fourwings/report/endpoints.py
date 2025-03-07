"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API EndPoint."""

from typing import Any, Dict, List, Union, override

import pydantic

from pydantic_core import ErrorDetails

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


class FourWingsReportEndPoint(
    PostEndPoint[
        FourWingsReportParams,
        FourWingsReportBody,
        FourWingsReportItem,
        FourWingsReportResult,
    ],
):
    """Get 4Wings Report API endpoint."""

    def __init__(
        self,
        request_params: FourWingsReportParams,
        request_body: FourWingsReportBody,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `FourWingsReportEndPoint` API endpoint."""
        super().__init__(
            path="4wings/report",
            request_params=request_params,
            request_body=request_body,
            result_item_class=FourWingsReportItem,
            result_class=FourWingsReportResult,
            http_client=http_client,
        )

    @override
    def _transform_response_body(
        self,
        body: Union[List[Dict[str, Any]], Dict[str, Any]],
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Transform and reshape response body and yield data."""
        # expected: {entries: [{"key": [{}]}]}
        if not isinstance(body, dict) or "entries" not in body:
            # TODO: raise APIResponseDataError | APIResultItemValidationError
            errors = [
                ErrorDetails(
                    type="value_error",
                    loc=("entries",),
                    msg="Expected a list of entries, but got an empty list.",
                    input=None,
                )
            ]
            raise pydantic.ValidationError(errors, FourWingsReportResult)

        # TODO: update pagination options|params

        # Transforming and reshaping entries
        report_entries: List[Dict[str, Any]] = body.get("entries", [])
        transformed_data: List[Dict[str, Any]] = []

        # Loop through "entries" list i.e {"entries": [{"dataset": [{...}]}]}
        for report_entry in report_entries:
            # Loop through each dataset "entries" list i.e {"dataset": [{...}]}
            for report_dataset, report_dataset_entries in report_entry.items():
                # Extract actual report item data i.e [{...}]
                for report_dataset_entry in report_dataset_entries or []:
                    # Reshape
                    _report_dataset_entry = {
                        "report_dataset": report_dataset,
                        **report_dataset_entry,
                    }
                    # Append extracted dictionaries
                    transformed_data.append(_report_dataset_entry)

        return transformed_data
