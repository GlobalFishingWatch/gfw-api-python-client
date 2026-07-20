"""Tests for `gfwapiclient.resources.bulk_downloads.detail.models.response`."""

from typing import Any, Dict, cast

from gfwapiclient.resources.bulk_downloads.detail.models.response import (
    BulkReportDetailItem,
    BulkReportDetailResult,
)


def test_bulk_report_detail_item_deserializes_all_fields(
    mock_raw_bulk_report_item: Dict[str, Any],
) -> None:
    """Test that `BulkReportDetailItem` deserializes all fields correctly."""
    bulk_report_item: BulkReportDetailItem = BulkReportDetailItem(
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


def test_bulk_report_detail_result_deserializes_all_fields(
    mock_raw_bulk_report_item: Dict[str, Any],
) -> None:
    """Test that `BulkReportDetailResult` deserializes all fields correctly."""
    data: BulkReportDetailItem = BulkReportDetailItem(**mock_raw_bulk_report_item)
    result = BulkReportDetailResult(data=data)
    assert cast(BulkReportDetailItem, result.data()) == data
