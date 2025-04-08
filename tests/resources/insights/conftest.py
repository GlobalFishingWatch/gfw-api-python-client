"""Test configurations for `gfwapiclient.resources.insights`."""

from typing import Any, Callable, Dict

import pytest


@pytest.fixture
def mock_raw_vessel_insight_request_body(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw vessel insight request body.

    Returns:
        Dict[str, Any]:
            Raw `VesselInsightBody` sample data.
    """
    raw_vessel_insight_request_body: Dict[str, Any] = load_json_fixture(
        "insights/vessel_insight_request_body.json"
    )
    return raw_vessel_insight_request_body


@pytest.fixture
def mock_raw_vessel_insight_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw vessel insight item.

    Returns:
        Dict[str, Any]:
            Raw `VesselInsightItem` sample data.
    """
    raw_vessel_insight_item: Dict[str, Any] = load_json_fixture(
        "insights/vessel_insight_item.json"
    )
    return raw_vessel_insight_item
