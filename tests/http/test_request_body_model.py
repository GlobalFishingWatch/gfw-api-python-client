"""Tests for `gfwapiclient.http.models.RequestBody`."""

import datetime

from enum import Enum
from typing import Any, Dict, Final, List, Optional

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import RequestBody


class SampleRequestBodyEnum(str, Enum):
    """A sample enum for testing `RequestBody` behavior."""

    MONTH = "MONTH"
    YEAR = "YEAR"


class SampleSubRequestBody(BaseModel):
    """A sample sub-request (inner) body for testing `RequestBody` behavior."""

    type: str
    coordinates: Any


class SampleRequestBody(RequestBody):
    """A sample model for testing `RequestBody` behavior."""

    datasets: Optional[List[str]] = Field(None)
    start_date: Optional[datetime.date] = Field(None, serialization_alias="startDate")
    confidences: Optional[List[int]] = Field(None)
    geometry: Optional[SampleSubRequestBody] = Field(None)
    duration: Optional[int] = Field(None)
    gap_intentional_disabling: Optional[bool] = Field(
        None, serialization_alias="gapIntentionalDisabling"
    )
    time_series_interval: Optional[SampleRequestBodyEnum] = Field(
        None, serialization_alias="timeseriesInterval"
    )


datasets: Final[List[str]] = [
    "public-global-vessel-identity:latest",
    "public-global-fishing-events:latest",
]
start_date: Final[datetime.date] = datetime.date.fromisoformat("2022-05-01")
confidences: Final[List[int]] = [3, 4]
geometry: Final[Dict[str, Any]] = {
    "type": "Polygon",
    "coordinates": [
        [
            [120.36621093749999, 26.725986812271756],
            [122.36572265625, 26.725986812271756],
            [122.36572265625, 28.323724553546015],
            [120.36621093749999, 28.323724553546015],
            [120.36621093749999, 26.725986812271756],
        ]
    ],
}
duration: Final[int] = 60
gap_intentional_disabling: Final[bool] = True
time_series_interval: Final[SampleRequestBodyEnum] = SampleRequestBodyEnum.YEAR


def test_request_body_empty_instance_serialization() -> None:
    """Tests that `RequestBody` serializes empty instance to empty dictionary."""
    model = SampleRequestBody()  # type: ignore[call-arg]
    output = model.to_json_body()
    assert output == {}


def test_request_body_all_fields_serialization() -> None:
    """Tests that `RequestBody` serializes all fields correctly."""
    input = {
        "datasets": datasets,
        "start_date": start_date,
        "confidences": confidences,
        "geometry": geometry,
        "duration": duration,
        "gap_intentional_disabling": gap_intentional_disabling,
        "time_series_interval": time_series_interval,
    }
    expected = {
        "datasets": datasets,
        "startDate": start_date.isoformat(),
        "confidences": confidences,
        "geometry": geometry,
        "duration": duration,
        "gapIntentionalDisabling": gap_intentional_disabling,
        "timeseriesInterval": time_series_interval.value,
    }

    model = SampleRequestBody(**input)  # type: ignore[arg-type]
    output = model.to_json_body()

    assert output == expected


def test_request_body_serialization_excludes_none_values() -> None:
    """Tests that `RequestBody` excludes fields with `None` values by default."""
    input = {"datasets": datasets, "start_date": start_date, "confidences": None}
    expected = {
        "datasets": datasets,
        "startDate": start_date.isoformat(),
    }

    model = SampleRequestBody(**input)  # type: ignore[arg-type]
    output = model.to_json_body()

    assert output == expected


def test_request_body_serialization_includes_none_values_when_explicitly_allowed() -> (
    None
):
    """Test that `RequestBody` includes `None` values when `exclude_none=False`."""
    input = {"datasets": datasets}
    expected = {
        "datasets": datasets,
        "startDate": None,
        "confidences": None,
        "geometry": None,
        "duration": None,
        "gapIntentionalDisabling": None,
        "timeseriesInterval": None,
    }

    model = SampleRequestBody(**input)  # type: ignore[arg-type]
    output = model.to_json_body(exclude_none=False)

    assert output == expected
