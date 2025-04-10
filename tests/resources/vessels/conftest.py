"""Test configurations for `gfwapiclient.resources.vessels`."""

from typing import Any, Callable, Dict

import pytest


@pytest.fixture
def mock_raw_vessel_detail_request_params(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw vessel detail request params.

    Returns:
        Dict[str, Any]:
            Raw `VesselDetailParams` sample data.
    """
    raw_vessel_detail_request_params: Dict[str, Any] = load_json_fixture(
        "vessels/vessel_detail_request_params.json"
    )
    return raw_vessel_detail_request_params


@pytest.fixture
def mock_raw_vessel_list_request_params(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw vessel list request params.

    Returns:
        Dict[str, Any]:
            Raw `VesselListParams` sample data.
    """
    raw_vessel_list_request_params: Dict[str, Any] = load_json_fixture(
        "vessels/vessel_list_request_params.json"
    )
    return raw_vessel_list_request_params


@pytest.fixture
def mock_raw_vessel_search_request_params(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw vessel search request params.

    Returns:
        Dict[str, Any]:
            Raw `VesselSearchParams` sample data.
    """
    raw_vessel_detail_request_params: Dict[str, Any] = load_json_fixture(
        "vessels/vessel_search_request_params.json"
    )
    return raw_vessel_detail_request_params


@pytest.fixture
def mock_raw_vessel_detail_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw vessel detail item.

    Returns:
        Dict[str, Any]:
            Raw `VesselDetailItem` sample data.
    """
    raw_vessel_detail_item: Dict[str, Any] = load_json_fixture(
        "vessels/vessel_item.json"
    )
    return raw_vessel_detail_item


@pytest.fixture
def mock_raw_vessel_list_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw vessel list item.

    Returns:
        Dict[str, Any]:
            Raw `VesselListItem` sample data.
    """
    raw_vessel_list_item: Dict[str, Any] = load_json_fixture("vessels/vessel_item.json")
    return raw_vessel_list_item


@pytest.fixture
def mock_raw_vessel_search_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw vessel search item.

    Returns:
        Dict[str, Any]:
            Raw `VesselSearchItem` sample data.
    """
    raw_vessel_search_item: Dict[str, Any] = load_json_fixture(
        "vessels/vessel_item.json"
    )
    return raw_vessel_search_item
