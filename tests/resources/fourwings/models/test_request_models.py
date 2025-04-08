"""Tests for `gfwapiclient.resources.fourwings.report.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.fourwings.report.models.request import (
    FourWingsReportBody,
    FourWingsReportParams,
)


def test_fourwings_report_request_body_serializes_all_fields(
    mock_raw_fourwings_report_request_body: Dict[str, Any],
) -> None:
    """Test that `FourWingsReportBody` serializes all fields correctly."""
    fourwings_report_request_body: FourWingsReportBody = FourWingsReportBody(
        **mock_raw_fourwings_report_request_body
    )
    assert fourwings_report_request_body.geojson is not None
    assert fourwings_report_request_body.region is not None
    assert (
        fourwings_report_request_body.to_json_body()
        == mock_raw_fourwings_report_request_body
    )


def test_fourwings_report_request_params_serializes_all_fields(
    mock_raw_fourwings_report_request_params: Dict[str, Any],
) -> None:
    """Test that `FourWingsReportParams` serializes all fields correctly."""
    fourwings_report_request_params: FourWingsReportParams = FourWingsReportParams(
        **mock_raw_fourwings_report_request_params
    )
    assert fourwings_report_request_params.spatial_resolution is not None
    assert fourwings_report_request_params.format is not None
    assert fourwings_report_request_params.group_by is not None
    assert fourwings_report_request_params.temporal_resolution is not None
    assert fourwings_report_request_params.datasets is not None
    assert fourwings_report_request_params.filters is not None
    assert fourwings_report_request_params.date_range is not None
    assert fourwings_report_request_params.spatial_aggregation is not None
    assert fourwings_report_request_params.to_query_params() is not None
