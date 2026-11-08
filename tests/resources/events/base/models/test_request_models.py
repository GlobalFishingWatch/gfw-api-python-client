"""Tests for `gfwapiclient.resources.events.base.models.request`."""

import pytest

from gfwapiclient.resources.events.base.models.request import (
    EventDataset,
)


@pytest.mark.parametrize(
    "dataset,value",
    [
        (
            EventDataset.ENCOUNTERS_EVENTS_LATEST,
            "public-global-encounters-events:latest",
        ),
        (
            EventDataset.ENCOUNTERS_EVENTS_V5_0,
            "public-global-encounters-events:v5.0",
        ),
        (
            EventDataset.ENCOUNTERS_EVENTS_V4_0,
            "public-global-encounters-events:v4.0",
        ),
        (
            EventDataset.GAPS_EVENTS_LATEST,
            "public-global-gaps-events:latest",
        ),
        (
            EventDataset.GAPS_EVENTS_V5_0,
            "public-global-gaps-events:v5.0",
        ),
        (
            EventDataset.GAPS_EVENTS_V4_0,
            "public-global-gaps-events:v4.0",
        ),
        (
            EventDataset.FISHING_EVENTS_LATEST,
            "public-global-fishing-events:latest",
        ),
        (
            EventDataset.FISHING_EVENTS_V5_0,
            "public-global-fishing-events:v5.0",
        ),
        (
            EventDataset.FISHING_EVENTS_V4_0,
            "public-global-fishing-events:v4.0",
        ),
        (
            EventDataset.LOITERING_EVENTS_LATEST,
            "public-global-loitering-events:latest",
        ),
        (
            EventDataset.LOITERING_EVENTS_V5_0,
            "public-global-loitering-events:v5.0",
        ),
        (
            EventDataset.LOITERING_EVENTS_V4_0,
            "public-global-loitering-events:v4.0",
        ),
        (
            EventDataset.PORT_VISITS_EVENTS_LATEST,
            "public-global-port-visits-events:latest",
        ),
        (
            EventDataset.PORT_VISITS_EVENTS_V5_0,
            "public-global-port-visits-events:v5.0",
        ),
        (
            EventDataset.PORT_VISITS_EVENTS_V4_0,
            "public-global-port-visits-events:v4.0",
        ),
    ],
)
def test_event_dataset_enum_correct_values(dataset: EventDataset, value: str) -> None:
    """Test that correct `EventDataset` enum values can be instantiated."""
    dataset_instance = EventDataset(value)
    assert dataset_instance == dataset


@pytest.mark.parametrize(
    "invalid_value",
    [
        "INVALID_DATASET",
        "",
    ],
)
def test_event_dataset_enum_invalid_value_raises_value_error(
    invalid_value: str,
) -> None:
    """Test that invalid `EventDataset` enum values raise a `ValueError`."""
    with pytest.raises(ValueError):
        EventDataset(invalid_value)
