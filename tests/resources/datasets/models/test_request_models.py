"""Tests for `gfwapiclient.resources.datasets.models.request`."""

from typing import Any, Dict

import pytest

from pydantic import ValidationError

from gfwapiclient.resources.datasets.models.request import SARFixedInfrastructureParams

from ..conftest import geometry, x, y, z


def test_datasets_sar_fixed_infrastructure_request_params_from_zxy() -> None:
    """Test that `SARFixedInfrastructureParams` can be created from zoom, x, and y tile coordinates."""
    mock_sar_fixed_infrastructure_request_params: Dict[str, Any] = {
        "z": z,
        "x": x,
        "y": y,
    }
    sar_fixed_infrastructure_request_params: SARFixedInfrastructureParams = (
        SARFixedInfrastructureParams(**mock_sar_fixed_infrastructure_request_params)
    )
    assert sar_fixed_infrastructure_request_params.z == z
    assert sar_fixed_infrastructure_request_params.x == x
    assert sar_fixed_infrastructure_request_params.y == y
    assert sar_fixed_infrastructure_request_params.geometry is None


def test_datasets_sar_fixed_infrastructure_request_params_from_geometry() -> None:
    """Test that `SARFixedInfrastructureParams` can be created from a geometry."""
    mock_sar_fixed_infrastructure_request_params: Dict[str, Any] = {
        "geometry": geometry
    }
    sar_fixed_infrastructure_request_params: SARFixedInfrastructureParams = (
        SARFixedInfrastructureParams.from_tile_or_geometry(
            **mock_sar_fixed_infrastructure_request_params
        )
    )
    assert sar_fixed_infrastructure_request_params.z == z
    assert sar_fixed_infrastructure_request_params.x == x
    assert sar_fixed_infrastructure_request_params.y == y
    assert sar_fixed_infrastructure_request_params.geometry is not None


def test_datasets_sar_fixed_infrastructure_request_params_raises_when_fields_are_missing() -> (
    None
):
    """Tests that `SARFixedInfrastructureParams` raises a `ValidationError` when required fields are missing."""
    with pytest.raises(ValidationError):
        SARFixedInfrastructureParams(**{})  # all None


def test_datasets_sar_fixed_infrastructure_request_params_from_tile_or_geometry_raises_when_fields_are_missing() -> (
    None
):
    """Tests that `SARFixedInfrastructureParams.from_tile_or_geometry` raises a `ValidationError` when required fields are missing."""
    with pytest.raises(ValidationError):
        SARFixedInfrastructureParams.from_tile_or_geometry(**{})  # all None
