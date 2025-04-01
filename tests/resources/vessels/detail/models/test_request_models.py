"""Tests for `gfwapiclient.resources.vessels.detail.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.vessels.detail.models.request import VesselDetailParams


def test_vessel_detail_request_params_serializes_all_fields(
    mock_raw_vessel_detail_request_params: Dict[str, Any],
) -> None:
    """Test that `VesselDetailParams` serializes all fields correctly."""
    vessel_detail_request_params: VesselDetailParams = VesselDetailParams(
        **mock_raw_vessel_detail_request_params
    )
    assert vessel_detail_request_params.binary is not None
    assert vessel_detail_request_params.dataset is not None
    assert vessel_detail_request_params.includes is not None
    assert vessel_detail_request_params.match_fields is not None
    assert vessel_detail_request_params.registries_info_data is not None
    assert vessel_detail_request_params.to_query_params() is not None
