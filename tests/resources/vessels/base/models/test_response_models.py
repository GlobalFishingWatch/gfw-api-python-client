"""Tests for `gfwapiclient.resources.vessels.base.models.response`."""

from typing import Any, Dict, Iterator, List

import pytest

from gfwapiclient.resources.vessels.base.models.response import (
    SelfReportedInfo,
    VesselItem,
    VesselResult,
)


def test_vessel_item_iter_matched_self_reported_infos_yields_correctly(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselItem` iter matched self reported infos yields correctly."""
    vessel_item: VesselItem = VesselItem(**mock_raw_vessel_list_item)
    matched_self_reported_info: Iterator[SelfReportedInfo] = (
        vessel_item._iter_matched_self_reported_infos()
    )
    assert matched_self_reported_info is not None
    assert isinstance(matched_self_reported_info, Iterator)
    assert len(list(matched_self_reported_info)) >= 1


@pytest.mark.parametrize(
    "update",
    [
        {"registryInfoTotalRecords": None},
        {"registryInfoTotalRecords": 0},
        {"selfReportedInfo": None},
        {"selfReportedInfo": []},
    ],
)
def test_vessel_item_iter_matched_self_reported_infos_does_not_yields_when_registry_or_self_report_info_missing(
    mock_raw_vessel_list_item: Dict[str, Any],
    update: Dict[str, Any],
) -> None:
    """Test that `VesselItem`  iter matched self reported infos does not yields when registry or self reported info missing."""
    mocked_raw_vessel_list_item: Dict[str, Any] = {**mock_raw_vessel_list_item}
    for k, v in update.items():
        mocked_raw_vessel_list_item[k] = v

    vessel_item: VesselItem = VesselItem(**mocked_raw_vessel_list_item)
    matched_self_reported_info: Iterator[SelfReportedInfo] = (
        vessel_item._iter_matched_self_reported_infos()
    )

    assert matched_self_reported_info is not None
    assert isinstance(matched_self_reported_info, Iterator)
    assert len(list(matched_self_reported_info)) == 0


def test_vessel_result_vessel_ids_returns_correctly(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselResult` returns list of vessel ids correctly."""
    data: List[VesselItem] = [VesselItem(**mock_raw_vessel_list_item)]
    result = VesselResult(data=data)
    assert result.vessel_ids is not None
    assert isinstance(result.vessel_ids, list)
    assert len(result.vessel_ids) >= 1


@pytest.mark.parametrize(
    "update",
    [
        {"registryInfoTotalRecords": None},
        {"registryInfoTotalRecords": 0},
        {"selfReportedInfo": None},
        {"selfReportedInfo": []},
        {"selfReportedInfo": [{"id": None}]},
        {"selfReportedInfo": [{"id": ""}]},
        {"selfReportedInfo": [{"id": " "}]},
    ],
)
def test_vessel_item_vessel_ids_returns_empty_list_when_registry_or_self_report_info_missing(
    mock_raw_vessel_list_item: Dict[str, Any],
    update: Dict[str, Any],
) -> None:
    """Test that `VesselItem` vessel ids returns empty list when registry or self reported info missing."""
    mocked_raw_vessel_list_item: Dict[str, Any] = {**mock_raw_vessel_list_item}
    for k, v in update.items():
        mocked_raw_vessel_list_item[k] = v

    data: List[VesselItem] = [VesselItem(**mocked_raw_vessel_list_item)]
    result = VesselResult(data=data)
    assert result.vessel_ids is not None
    assert isinstance(result.vessel_ids, list)
    assert len(result.vessel_ids) == 0


def test_vessel_result_transmission_dates_from_returns_correctly(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselResult` transmission dates from returns list of transmission start dates correctly."""
    data: List[VesselItem] = [VesselItem(**mock_raw_vessel_list_item)]
    result = VesselResult(data=data)
    assert result.transmission_dates_from is not None
    assert isinstance(result.transmission_dates_from, list)
    assert len(result.transmission_dates_from) >= 1


@pytest.mark.parametrize(
    "update",
    [
        {"registryInfoTotalRecords": None},
        {"registryInfoTotalRecords": 0},
        {"selfReportedInfo": None},
        {"selfReportedInfo": []},
        {"selfReportedInfo": [{"transmissionDateFrom": None}]},
    ],
)
def test_vessel_item_vessel_transmission_dates_from_returns_empty_list_when_registry_or_self_report_info_missing(
    mock_raw_vessel_list_item: Dict[str, Any],
    update: Dict[str, Any],
) -> None:
    """Test that `VesselItem` transmission dates from returns empty list when registry or self reported info missing."""
    mocked_raw_vessel_list_item: Dict[str, Any] = {**mock_raw_vessel_list_item}
    for k, v in update.items():
        mocked_raw_vessel_list_item[k] = v

    data: List[VesselItem] = [VesselItem(**mocked_raw_vessel_list_item)]
    result = VesselResult(data=data)
    assert result.transmission_dates_from is not None
    assert isinstance(result.transmission_dates_from, list)
    assert len(result.transmission_dates_from) == 0


def test_vessel_result_transmission_dates_to_returns_correctly(
    mock_raw_vessel_list_item: Dict[str, Any],
) -> None:
    """Test that `VesselResult` transmission dates to returns list of transmission end dates correctly."""
    data: List[VesselItem] = [VesselItem(**mock_raw_vessel_list_item)]
    result = VesselResult(data=data)
    assert result.transmission_dates_to is not None
    assert isinstance(result.transmission_dates_to, list)
    assert len(result.transmission_dates_to) >= 1


@pytest.mark.parametrize(
    "update",
    [
        {"registryInfoTotalRecords": None},
        {"registryInfoTotalRecords": 0},
        {"selfReportedInfo": None},
        {"selfReportedInfo": []},
        {"selfReportedInfo": [{"transmissionDateTo": None}]},
    ],
)
def test_vessel_item_vessel_transmission_dates_to_returns_empty_list_when_registry_or_self_report_info_missing(
    mock_raw_vessel_list_item: Dict[str, Any],
    update: Dict[str, Any],
) -> None:
    """Test that `VesselItem` transmission dates to returns empty list when registry or self reported info missing."""
    mocked_raw_vessel_list_item: Dict[str, Any] = {**mock_raw_vessel_list_item}
    for k, v in update.items():
        mocked_raw_vessel_list_item[k] = v

    data: List[VesselItem] = [VesselItem(**mocked_raw_vessel_list_item)]
    result = VesselResult(data=data)
    assert result.transmission_dates_to is not None
    assert isinstance(result.transmission_dates_to, list)
    assert len(result.transmission_dates_to) == 0
