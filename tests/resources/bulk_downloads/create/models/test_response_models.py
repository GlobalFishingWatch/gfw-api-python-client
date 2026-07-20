"""Tests for `gfwapiclient.resources.bulk_downloads.create.models.response`."""

from typing import Any, Dict, cast

from gfwapiclient.resources.bulk_downloads.create.models.response import (
    BulkReportCreateItem,
    BulkReportCreateResult,
)


def test_bulk_report_create_item_deserializes_all_fields(
    mock_raw_bulk_report_item: Dict[str, Any],
) -> None:
    """Test that `BulkReportCreateItem` deserializes all fields correctly."""
    bulk_report_item: BulkReportCreateItem = BulkReportCreateItem(
        **mock_raw_bulk_report_item
    )
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


def test_bulk_report_create_result_deserializes_all_fields(
    mock_raw_bulk_report_item: Dict[str, Any],
) -> None:
    """Test that `BulkReportCreateResult` deserializes all fields correctly."""
    data: BulkReportCreateItem = BulkReportCreateItem(**mock_raw_bulk_report_item)
    result = BulkReportCreateResult(data=data)
    assert cast(BulkReportCreateItem, result.data()) == data
