"""Tests for `gfwapiclient.resources.bulk_downloads.create.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.bulk_downloads.create.models.request import (
    BulkReportCreateBody,
)

from .....base.test_geojson_models import assert_valid_geometry


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

    assert_valid_geometry(bulk_report_create_request_body.geojson)

    expected_raw_bulk_report_create_request_body = {
        **mock_raw_bulk_report_create_request_body
    }
    expected_raw_bulk_report_create_request_body["region"]["id"] = str(
        mock_raw_bulk_report_create_request_body["region"]["id"]
    )

    bulk_report_create_request_json_body: Dict[str, Any] = (
        bulk_report_create_request_body.to_json_body()
    )

    for attr_name in ["name", "dataset", "format", "region", "filters"]:
        assert (
            bulk_report_create_request_json_body[attr_name]
            == expected_raw_bulk_report_create_request_body[attr_name]
        )
