"""Tests for `gfwapiclient.resources.vessels.search.models.request`."""

from typing import Any, Dict

from gfwapiclient.resources.vessels.search.models.request import VesselSearchParams


def test_vessel_search_request_params_serializes_all_fields(
    mock_raw_vessel_search_request_params: Dict[str, Any],
) -> None:
    """Test that `VesselSearchParams` serializes all fields correctly."""
    vessel_search_request_params: VesselSearchParams = VesselSearchParams(
        **mock_raw_vessel_search_request_params
    )
    assert vessel_search_request_params.binary is not None
    assert vessel_search_request_params.datasets is not None
    assert vessel_search_request_params.includes is not None
    assert vessel_search_request_params.limit is not None
    assert vessel_search_request_params.match_fields is not None
    assert vessel_search_request_params.query is not None
    assert vessel_search_request_params.since is not None
    assert vessel_search_request_params.where is not None
    assert vessel_search_request_params.to_query_params() is not None
