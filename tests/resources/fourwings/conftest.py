"""Test configurations for `gfwapiclient.resources.fourwings`."""

from typing import Any, Callable, Dict

import pytest


@pytest.fixture
def mock_raw_fourwings_report_request_params(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw four wings report request params.

    Returns:
        Dict[str, Any]:
            Raw `FourWingsReportParams` sample data.
    """
    raw_fourwings_report_request_params: Dict[str, Any] = load_json_fixture(
        "fourwings/fourwings_report_request_params.json"
    )
    return raw_fourwings_report_request_params


@pytest.fixture
def mock_raw_fourwings_report_request_body(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw four wings report request body.

    Returns:
        Dict[str, Any]:
            Raw `FourWingsReportBody` sample data.
    """
    raw_fourwings_report_request_body: Dict[str, Any] = load_json_fixture(
        "fourwings/fourwings_report_request_body.json"
    )
    return raw_fourwings_report_request_body


@pytest.fixture
def mock_raw_fourwings_report_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw four wings report item.

    Returns:
        Dict[str, Any]:
            Raw `FourWingsReportItem` sample data.
    """
    raw_four_wings_report_item: Dict[str, Any] = load_json_fixture(
        "fourwings/fourwings_report_item.json"
    )
    return raw_four_wings_report_item
