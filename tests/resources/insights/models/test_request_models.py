"""Tests for `gfwapiclient.resources.insights.models.request`."""

from typing import Any, Dict, Union

import pytest

from gfwapiclient.resources.insights.models.request import VesselInsightBody
from gfwapiclient.resources.vessels.base.models.request import VesselDataset


def test_vessel_insight_request_body_serializes_all_fields(
    mock_raw_vessel_insight_request_body: Dict[str, Any],
) -> None:
    """Test that `VesselInsightBody` serializes all fields correctly."""
    vessel_insight_body: VesselInsightBody = VesselInsightBody(
        **mock_raw_vessel_insight_request_body
    )
    assert vessel_insight_body.includes is not None
    assert vessel_insight_body.start_date is not None
    assert vessel_insight_body.end_date is not None
    assert vessel_insight_body.vessels is not None

    for vessel in vessel_insight_body.vessels:
        assert vessel.dataset_id is not None

    assert vessel_insight_body.to_json_body() == mock_raw_vessel_insight_request_body


def test_vessel_insight_request_body_serializes_none_vessels_dataset_id_with_default(
    mock_raw_vessel_insight_request_body: Dict[str, Any],
) -> None:
    """Test that `VesselInsightBody` serializes vessels with no dataset id using default dataset id."""
    raw_vessel_insight_request_body: Dict[str, Any] = {
        **mock_raw_vessel_insight_request_body
    }
    raw_vessel_insight_request_body["vessels"] = [
        {**vessel, "dataset_id": None}
        for vessel in raw_vessel_insight_request_body["vessels"]
    ]

    vessel_insight_body: VesselInsightBody = VesselInsightBody(
        **raw_vessel_insight_request_body
    )
    assert vessel_insight_body.includes is not None
    assert vessel_insight_body.start_date is not None
    assert vessel_insight_body.end_date is not None
    assert vessel_insight_body.vessels is not None

    for vessel in vessel_insight_body.vessels:
        assert vessel.dataset_id is not None
        assert vessel.dataset_id == VesselDataset.VESSEL_IDENTITY_LATEST

    assert vessel_insight_body.to_json_body() == mock_raw_vessel_insight_request_body


@pytest.mark.parametrize(
    "dataset_id",
    [
        VesselDataset.VESSEL_IDENTITY_LATEST,
        VesselDataset.VESSEL_IDENTITY_V5_0,
        VesselDataset.VESSEL_IDENTITY_V4_0,
    ],
)
def test_vessel_insight_request_body_serializes_all_vessels_dataset_id_values(
    mock_raw_vessel_insight_request_body: Dict[str, Any],
    dataset_id: Union[str, VesselDataset],
) -> None:
    """Test that `VesselInsightBody` serializes all vessels dataset id values correctly."""
    raw_vessel_insight_request_body: Dict[str, Any] = {
        **mock_raw_vessel_insight_request_body
    }
    raw_vessel_insight_request_body["vessels"] = [
        {**vessel, "datasetId": dataset_id}
        for vessel in raw_vessel_insight_request_body["vessels"]
    ]

    vessel_insight_body: VesselInsightBody = VesselInsightBody(
        **raw_vessel_insight_request_body
    )
    assert vessel_insight_body.includes is not None
    assert vessel_insight_body.start_date is not None
    assert vessel_insight_body.end_date is not None
    assert vessel_insight_body.vessels is not None

    for vessel in vessel_insight_body.vessels:
        assert vessel.dataset_id is not None
        assert vessel.dataset_id == dataset_id

    assert vessel_insight_body.to_json_body() == raw_vessel_insight_request_body
