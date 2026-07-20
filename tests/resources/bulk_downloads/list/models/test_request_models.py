"""Tests for `gfwapiclient.resources.bulk_downloads.list.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.bulk_downloads.list.models.request import (
    BulkReportListParams,
)


def test_bulk_report_list_request_params_serializes_all_fields(
    mock_raw_bulk_report_list_request_params: Dict[str, Any],
) -> None:
    """Test that `BulkReportListParams` serializes all fields correctly."""
    bulk_report_list_request_params: BulkReportListParams = BulkReportListParams(
        **mock_raw_bulk_report_list_request_params
    )
    assert bulk_report_list_request_params.limit is not None
    assert bulk_report_list_request_params.offset is not None
    assert bulk_report_list_request_params.sort is not None
    assert bulk_report_list_request_params.status is not None
    assert bulk_report_list_request_params.dataset is not None
    assert bulk_report_list_request_params.to_query_params() is not None
