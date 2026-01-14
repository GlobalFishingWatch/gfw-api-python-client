"""Tests for `gfwapiclient.resources.bulk_downloads.create.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.bulk_downloads.create.models.request import (
    BulkReportCreateBody,
)


def test_bulk_report_create_request_body_serializes_all_fields(
    mock_raw_bulk_report_create_request_body: Dict[str, Any],
) -> None:
    """Test that `BulkReportCreateBody` serializes all fields correctly."""
    bulk_report_create_request_body: BulkReportCreateBody = BulkReportCreateBody(
        **mock_raw_bulk_report_create_request_body
    )
    assert bulk_report_create_request_body.name is not None
    assert bulk_report_create_request_body.dataset is not None
    assert bulk_report_create_request_body.geojson is not None
    assert bulk_report_create_request_body.format is not None
    assert bulk_report_create_request_body.region is not None
    assert bulk_report_create_request_body.filters is not None

    expected_raw_bulk_report_create_request_body = {
        **mock_raw_bulk_report_create_request_body
    }
    expected_raw_bulk_report_create_request_body["region"]["id"] = str(
        mock_raw_bulk_report_create_request_body["region"]["id"]
    )
    assert (
        bulk_report_create_request_body.to_json_body()
        == expected_raw_bulk_report_create_request_body
    )
