"""Tests for `gfwapiclient.resources.vessels.list.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.vessels.list.models.request import VesselListParams


def test_vessel_list_request_params_serializes_all_fields(
    mock_raw_vessel_list_request_params: Dict[str, Any],
) -> None:
    """Test that `VesselListParams` serializes all fields correctly."""
    vessel_list_request_params: VesselListParams = VesselListParams(
        **mock_raw_vessel_list_request_params
    )
    assert vessel_list_request_params.binary is not None
    assert vessel_list_request_params.datasets is not None
    assert vessel_list_request_params.ids is not None
    assert vessel_list_request_params.includes is not None
    assert vessel_list_request_params.match_fields is not None
    assert vessel_list_request_params.registries_info_data is not None
    assert vessel_list_request_params.vessel_groups is not None
    assert vessel_list_request_params.to_query_params() is not None
