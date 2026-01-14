"""Tests for `gfwapiclient.resources.bulk_downloads.base.models.request`."""

from typing import Any, Dict

import pytest

from pydantic import ValidationError

from gfwapiclient.resources.bulk_downloads.base.models.request import (
    BulkReportDataset,
    BulkReportFileType,
    BulkReportFormat,
    BulkReportGeometry,
    BulkReportRegion,
)

from ...conftest import geometry, region_dataset, region_id


@pytest.mark.parametrize(
    "dataset,value",
    [
        (
            BulkReportDataset.FIXED_INFRASTRUCTURE_DATA_LATEST,
            "public-fixed-infrastructure-data:latest",
        ),
    ],
)
def test_bulk_report_dataset_enum_correct_values(
    dataset: BulkReportDataset, value: str
) -> None:
    """Test that correct `BulkReportDataset` enum values can be instantiated."""
    dataset_instance = BulkReportDataset(value)
    assert dataset_instance == dataset


@pytest.mark.parametrize(
    "invalid_value",
    ["INVALID_DATASET", ""],
)
def test_bulk_report_dataset_enum_invalid_value_raises_value_error(
    invalid_value: str,
) -> None:
    """Test that invalid `BulkReportDataset` enum values raise a `ValueError`."""
    with pytest.raises(ValueError):
        BulkReportDataset(invalid_value)


@pytest.mark.parametrize(
    "format,value",
    [
        (BulkReportFormat.CSV, "CSV"),
        (BulkReportFormat.JSON, "JSON"),
    ],
)
def test_bulk_report_format_enum_correct_values(
    format: BulkReportFormat, value: str
) -> None:
    """Test that correct `BulkReportFormat` enum values can be instantiated."""
    format_instance = BulkReportFormat(value)
    assert format_instance == format


@pytest.mark.parametrize(
    "invalid_value",
    ["INVALID_FORMAT", ""],
)
def test_bulk_report_format_enum_invalid_value_raises_value_error(
    invalid_value: str,
) -> None:
    """Test that invalid `BulkReportFormat` enum values raise a `ValueError`."""
    with pytest.raises(ValueError):
        BulkReportFormat(invalid_value)


@pytest.mark.parametrize(
    "file_type,value",
    [
        (BulkReportFileType.DATA, "DATA"),
        (BulkReportFileType.README, "README"),
        (BulkReportFileType.GEOM, "GEOM"),
    ],
)
def test_bulk_report_file_type_enum_correct_values(
    file_type: BulkReportFileType, value: str
) -> None:
    """Test that correct `BulkReportFileType` enum values can be instantiated."""
    file_type_instance = BulkReportFileType(value)
    assert file_type_instance == file_type


@pytest.mark.parametrize(
    "invalid_value",
    ["INVALID_FILE_TYPE", ""],
)
def test_bulk_report_file_type_enum_invalid_value_raises_value_error(
    invalid_value: str,
) -> None:
    """Test that invalid `BulkReportFileType` enum values raise a `ValueError`."""
    with pytest.raises(ValueError):
        BulkReportFileType(invalid_value)


def test_bulk_report_geometry_serializes_all_fields() -> None:
    """Test that `BulkReportGeometry` serializes all required fields correctly."""
    geom: BulkReportGeometry = BulkReportGeometry(**geometry)
    assert geom.type == "Polygon"
    assert geom.coordinates == geometry.get("coordinates")


@pytest.mark.parametrize(
    "invalid_input",
    [
        {},  # missing required fields
        {"type": "Polygon"},  # missing coordinates
        {"coordinates": [[[0, 0]]]},  # missing type
    ],
)
def test_bulk_report_geometry_invalid_inputs_raise_validation_erro(
    invalid_input: Dict[str, Any],
) -> None:
    """Test that invalid `BulkReportGeometry` inputs raise a `ValidationError`."""
    with pytest.raises(ValidationError):
        BulkReportGeometry(**invalid_input)


def test_bulk_report_region_serializes_all_fields() -> None:
    """Test that `BulkReportRegion` serializes all required fields correctly."""
    region: BulkReportRegion = BulkReportRegion(dataset=region_dataset, id=region_id)  # type: ignore[arg-type]
    assert str(region.dataset) == region_dataset
    assert region.id == str(region_id)


def test_bulk_report_region_optional_fields_default_to_none() -> None:
    """Test that `BulkReportRegion` sets missing optional fields to `None`."""
    region: BulkReportRegion = BulkReportRegion()  # type: ignore[call-arg]
    assert region.dataset is None
    assert region.id is None
