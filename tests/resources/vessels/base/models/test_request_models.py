"""Tests for `gfwapiclient.resources.vessels.base.models.request`."""

import pytest

from gfwapiclient.resources.vessels.base.models.request import VesselDataset


@pytest.mark.parametrize(
    "dataset,value",
    [
        (
            VesselDataset.VESSEL_IDENTITY_LATEST,
            "public-global-vessel-identity:latest",
        ),
        (
            VesselDataset.VESSEL_IDENTITY_V5_0,
            "public-global-vessel-identity:v5.0",
        ),
        (
            VesselDataset.VESSEL_IDENTITY_V4_0,
            "public-global-vessel-identity:v4.0",
        ),
    ],
)
def test_vessel_dataset_enum_correct_values(dataset: VesselDataset, value: str) -> None:
    """Test that correct `VesselDataset` enum values can be instantiated."""
    dataset_instance = VesselDataset(value)
    assert dataset_instance == dataset


@pytest.mark.parametrize(
    "invalid_value",
    [
        "INVALID_DATASET",
        "",
    ],
)
def test_vessel_dataset_enum_invalid_value_raises_value_error(
    invalid_value: str,
) -> None:
    """Test that invalid `VesselDataset` enum values raise a `ValueError`."""
    with pytest.raises(ValueError):
        VesselDataset(invalid_value)
