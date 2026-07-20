"""Tests for `gfwapiclient.resources.bulk_downloads.base.models.response`."""

from typing import Any, Dict

import pytest

from gfwapiclient.resources.bulk_downloads.base.models.response import (
    BulkReportGeography,
    BulkReportItem,
    BulkReportStatus,
)

from ...conftest import region_dataset, region_id


@pytest.mark.parametrize(
    "status,value",
    [
        (BulkReportStatus.PENDING, "pending"),
        (BulkReportStatus.PROCESSING, "processing"),
        (BulkReportStatus.DONE, "done"),
        (BulkReportStatus.FAILED, "failed"),
    ],
)
def test_bulk_report_status_enum_correct_values(
    status: BulkReportStatus, value: str
) -> None:
    """Test that correct `BulkReportStatus` enum values can be instantiated."""
    status_instance = BulkReportStatus(value)
    assert status_instance == status


@pytest.mark.parametrize(
    "invalid_value",
    ["invalid", ""],
)
def test_bulk_report_status_enum_invalid_value_raises_value_error(
    invalid_value: str,
) -> None:
    """Test that invalid `BulkReportStatus` enum values raise a `ValueError`."""
    with pytest.raises(ValueError):
        BulkReportStatus(invalid_value)


def test_bulk_report_geography_deserializes_all_fields() -> None:
    """Test that `BulkReportGeography` deserializes all fields correctly."""
    input: Dict[str, Any] = {
        "type": "dataset",
        "dataset": region_dataset,
        "id": region_id,
    }
    geo: BulkReportGeography = BulkReportGeography(**input)
    assert geo.type == "dataset"
    assert geo.dataset == region_dataset
    assert geo.id == region_id


def test_bulk_report_geography_deserializes_optional_fields_to_none() -> None:
    """Test that `BulkReportGeography` sets missing optional fields to `None`."""
    geo: BulkReportGeography = BulkReportGeography()  # type: ignore[call-arg]
    assert geo.type is None
    assert geo.dataset is None
    assert geo.id is None


def test_bulk_report_item_deserializes_all_fields(
    mock_raw_bulk_report_item: Dict[str, Any],
) -> None:
    """Test that `BulkReportItem` deserializes all fields correctly."""
    bulk_report_item: BulkReportItem = BulkReportItem(**mock_raw_bulk_report_item)
    assert bulk_report_item.id is not None
    assert bulk_report_item.dataset is not None
    assert bulk_report_item.name is not None
    assert bulk_report_item.file_path is not None
    assert bulk_report_item.format is not None
    assert bulk_report_item.filters is not None
    assert bulk_report_item.geom is not None
    assert bulk_report_item.status is not None
    assert bulk_report_item.owner_id is not None
    assert bulk_report_item.owner_type is not None
    assert bulk_report_item.created_at is not None
    assert bulk_report_item.updated_at is not None
    assert bulk_report_item.file_size is not None


def test_bulk_report_item_deserializes_optional_fields_to_none() -> None:
    """Test that `BulkReportItem` sets missing optional fields to `None`."""
    bulk_report_item: BulkReportItem = BulkReportItem()  # type: ignore[call-arg]
    assert bulk_report_item.id is None
    assert bulk_report_item.dataset is None
    assert bulk_report_item.name is None
    assert bulk_report_item.file_path is None
    assert bulk_report_item.format is None
    assert bulk_report_item.filters is None
    assert bulk_report_item.geom is None
    assert bulk_report_item.status is None
    assert bulk_report_item.owner_id is None
    assert bulk_report_item.owner_type is None
    assert bulk_report_item.created_at is None
    assert bulk_report_item.updated_at is None
    assert bulk_report_item.file_size is None


@pytest.mark.parametrize(
    "empty_datetime_field",
    ["", "   "],
)
def test_bulk_report_item_deserializes_empty_datetime_strings_to_none(
    mock_raw_bulk_report_item: Dict[str, Any], empty_datetime_field: str
) -> None:
    """Test that `BulkReportItem` empty strings for datetime fields (`createdAt`, `updatedAt`) are converted to `None`."""
    raw_bulk_report_item: Dict[str, Any] = {
        **mock_raw_bulk_report_item,
        "createdAt": empty_datetime_field,
        "updatedAt": empty_datetime_field,
    }
    report_item: BulkReportItem = BulkReportItem(**raw_bulk_report_item)
    assert report_item.created_at is None
    assert report_item.updated_at is None
