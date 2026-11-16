"""Tests for `gfwapiclient.resources.fourwings.report.models.request`."""

from typing import Any, Dict

import pytest

from gfwapiclient.resources.fourwings.report.models.request import (
    FourWingsReportBody,
    FourWingsReportDataset,
    FourWingsReportParams,
)

from ....base.test_geojson_models import assert_valid_geojson


@pytest.mark.parametrize(
    "dataset,value",
    [
        (
            FourWingsReportDataset.FISHING_EFFORT_LATEST,
            "public-global-fishing-effort:latest",
        ),
        (
            FourWingsReportDataset.FISHING_EFFORT_V5_0,
            "public-global-fishing-effort:v5.0",
        ),
        (
            FourWingsReportDataset.FISHING_EFFORT_V4_0,
            "public-global-fishing-effort:v4.0",
        ),
        (
            FourWingsReportDataset.PRESENCE_LATEST,
            "public-global-presence:latest",
        ),
        (
            FourWingsReportDataset.PRESENCE_V5_0,
            "public-global-presence:v5.0",
        ),
        (
            FourWingsReportDataset.PRESENCE_V4_0,
            "public-global-presence:v4.0",
        ),
        (
            FourWingsReportDataset.SAR_PRESENCE_LATEST,
            "public-global-sar-presence:latest",
        ),
        (
            FourWingsReportDataset.SAR_PRESENCE_V5_0,
            "public-global-sar-presence:v5.0",
        ),
        (
            FourWingsReportDataset.SAR_PRESENCE_V4_0,
            "public-global-sar-presence:v4.0",
        ),
    ],
)
def test_fourwings_report_dataset_enum_correct_values(
    dataset: FourWingsReportDataset, value: str
) -> None:
    """Test that correct `FourWingsReportDataset` enum values can be instantiated."""
    dataset_instance = FourWingsReportDataset(value)
    assert dataset_instance == dataset


@pytest.mark.parametrize(
    "invalid_value",
    [
        "INVALID_DATASET",
        "",
    ],
)
def test_fourwings_report_dataset_enum_invalid_value_raises_value_error(
    invalid_value: str,
) -> None:
    """Test that invalid `FourWingsReportDataset` enum values raise a `ValueError`."""
    with pytest.raises(ValueError):
        FourWingsReportDataset(invalid_value)


def test_fourwings_report_request_body_serializes_all_fields(
    mock_raw_fourwings_report_request_body: Dict[str, Any],
) -> None:
    """Test that `FourWingsReportBody` serializes all fields correctly."""
    fourwings_report_request_body: FourWingsReportBody = FourWingsReportBody(
        **mock_raw_fourwings_report_request_body
    )
    assert fourwings_report_request_body.geojson is not None
    assert fourwings_report_request_body.region is not None
    assert_valid_geojson(fourwings_report_request_body.geojson)

    fourwings_report_request_json_body: Dict[str, Any] = (
        fourwings_report_request_body.to_json_body()
    )

    for attr_name in ["region"]:
        assert (
            fourwings_report_request_json_body[attr_name]
            == mock_raw_fourwings_report_request_body[attr_name]
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
    assert fourwings_report_request_params.distance_from_port_km is not None
    assert fourwings_report_request_params.to_query_params() is not None
