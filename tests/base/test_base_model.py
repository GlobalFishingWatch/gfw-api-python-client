"""Tests for `gfwapiclient.base.models.BaseModel`."""

import pytest

from pydantic import ValidationError

from gfwapiclient.base.models import BaseModel


class SampleModel(BaseModel):
    """A sample model for testing BaseModel behavior."""

    start_date: str
    timeseries_interval: str


def test_serialization_snake_to_camel() -> None:
    """Test that BaseModel serializes snake_case attributes to camelCase."""
    model = SampleModel(start_date="2018-01-01", timeseries_interval="YEAR")
    output = {"startDate": "2018-01-01", "timeseriesInterval": "YEAR"}

    assert model.model_dump(by_alias=True) == output


def test_deserialization_camel_to_snake() -> None:
    """Test that BaseModel deserializes camelCase input into snake_case attributes."""
    input = {"startDate": "2018-01-01", "timeseriesInterval": "YEAR"}
    model = SampleModel(**input)

    assert model.start_date == "2018-01-01"
    assert model.timeseries_interval == "YEAR"


def test_extra_fields_are_allowed() -> None:
    """Test that BaseModel allows extra fields without raising errors."""
    input = {
        "startDate": "2018-01-01",
        "timeseriesInterval": "YEAR",
        "duration": "60",
    }
    model = SampleModel(**input)

    assert model.start_date == "2018-01-01"
    assert model.timeseries_interval == "YEAR"
    assert model.model_dump()["duration"] == "60"


def test_whitespace_is_trimmed() -> None:
    """Test that BaseModel automatically trims leading and trailing whitespace in string fields."""
    model = SampleModel(start_date="  2018-01-01  ", timeseries_interval="  YEAR ")

    assert model.start_date == "2018-01-01"
    assert model.timeseries_interval == "YEAR"


def test_missing_required_fields_raises_error() -> None:
    """Test that BaseModel raises a ValidationError when required fields are missing."""
    with pytest.raises(ValidationError):
        SampleModel(timeseries_interval="YEAR")  # type: ignore[call-arg]
