"""Tests for `gfwapiclient.resources.bulk_downloads.list.models.response`."""

from typing import Any, Dict, List, cast

from gfwapiclient.resources.bulk_downloads.list.models.response import (
    BulkReportListItem,
    BulkReportListResult,
)


def test_bulk_report_list_item_deserializes_all_fields(
    mock_raw_bulk_report_item: Dict[str, Any],
) -> None:
    """Test that `BulkReportListItem` deserializes all fields correctly."""
    bulk_report_list_item: BulkReportListItem = BulkReportListItem(
        **mock_raw_bulk_report_item
    )
    assert bulk_report_list_item.id is not None
    assert bulk_report_list_item.dataset is not None
    assert bulk_report_list_item.name is not None
    assert bulk_report_list_item.file_path is not None
    assert bulk_report_list_item.format is not None
    assert bulk_report_list_item.filters is not None
    assert bulk_report_list_item.geom is not None
    assert bulk_report_list_item.status is not None
    assert bulk_report_list_item.owner_id is not None
    assert bulk_report_list_item.owner_type is not None
    assert bulk_report_list_item.created_at is not None
    assert bulk_report_list_item.updated_at is not None
    assert bulk_report_list_item.file_size is not None


def test_bulk_report_list_result_deserializes_all_fields(
    mock_raw_bulk_report_item: Dict[str, Any],
) -> None:
    """Test that `BulkReportListResult` deserializes all fields correctly."""
    data: List[BulkReportListItem] = [BulkReportListItem(**mock_raw_bulk_report_item)]
    result = BulkReportListResult(data=data)
    assert cast(List[BulkReportListItem], result.data()) == data
