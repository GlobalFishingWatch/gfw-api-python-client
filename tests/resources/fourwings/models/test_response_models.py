"""Tests for `gfwapiclient.resources.fourwings.report.models.response`."""

from typing import Any, Dict, List, cast

from gfwapiclient.resources.fourwings.report.models.response import (
    FourWingsReportItem,
    FourWingsReportResult,
)


def test_fourwings_report_item_deserializes_all_fields(
    mock_raw_fourwings_report_item: Dict[str, Any],
) -> None:
    """Test that `FourWingsReportItem` deserializes all fields correctly."""
    vessel_insight_item: FourWingsReportItem = FourWingsReportItem(
        **mock_raw_fourwings_report_item
    )
    assert vessel_insight_item.date is not None
    assert vessel_insight_item.detections is not None
    assert vessel_insight_item.flag is not None
    assert vessel_insight_item.gear_type is not None
    assert vessel_insight_item.hours is not None
    assert vessel_insight_item.vessel_ids is not None
    assert vessel_insight_item.vessel_id is not None
    assert vessel_insight_item.vessel_type is not None
    assert vessel_insight_item.entry_timestamp is None
    assert vessel_insight_item.exit_timestamp is not None
    assert vessel_insight_item.first_transmission_date is not None
    assert vessel_insight_item.last_transmission_date is not None
    assert vessel_insight_item.imo is not None
    assert vessel_insight_item.mmsi is not None
    assert vessel_insight_item.call_sign is not None
    assert vessel_insight_item.dataset is not None
    assert vessel_insight_item.report_dataset is not None
    assert vessel_insight_item.ship_name is not None
    assert vessel_insight_item.lat is not None
    assert vessel_insight_item.lon is not None


def test_fourwings_report_result_deserializes_all_fields(
    mock_raw_fourwings_report_item: Dict[str, Any],
) -> None:
    """Test that `FourWingsReportResult` deserializes all fields correctly."""
    data: List[FourWingsReportItem] = [
        FourWingsReportItem(**mock_raw_fourwings_report_item)
    ]
    result = FourWingsReportResult(data=data)
    assert cast(List[FourWingsReportItem], result.data()) == data


def test_fourwings_report_result_vessel_ids_returns_correctly(
    mock_raw_fourwings_report_item: Dict[str, Any],
) -> None:
    """Test that `FourWingsReportResult` returns list of vessel ids correctly."""
    data: List[FourWingsReportItem] = [
        FourWingsReportItem(**mock_raw_fourwings_report_item)
    ]
    result = FourWingsReportResult(data=data)
    assert result.vessel_ids is not None
    assert isinstance(result.vessel_ids, list)
    assert len(result.vessel_ids) >= 1


def test_fourwings_report_result_first_transmission_dates_returns_correctly(
    mock_raw_fourwings_report_item: Dict[str, Any],
) -> None:
    """Test that `FourWingsReportResult` first transmission dates returns list of first transmission dates correctly."""
    data: List[FourWingsReportItem] = [
        FourWingsReportItem(**mock_raw_fourwings_report_item)
    ]
    result = FourWingsReportResult(data=data)
    assert result.first_transmission_dates is not None
    assert isinstance(result.first_transmission_dates, list)
    assert len(result.first_transmission_dates) >= 1


def test_fourwings_report_result_last_transmission_dates_returns_correctly(
    mock_raw_fourwings_report_item: Dict[str, Any],
) -> None:
    """Test that `FourWingsReportResult` last transmission dates to returns list of last transmission dates correctly."""
    data: List[FourWingsReportItem] = [
        FourWingsReportItem(**mock_raw_fourwings_report_item)
    ]
    result = FourWingsReportResult(data=data)
    assert result.last_transmission_dates is not None
    assert isinstance(result.last_transmission_dates, list)
    assert len(result.last_transmission_dates) >= 1
