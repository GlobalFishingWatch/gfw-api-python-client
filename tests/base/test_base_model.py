"""Tests for `gfwapiclient.base.models.BaseModel`."""

from enum import Enum
from typing import Any, Dict, Final, Optional

import pytest

from pydantic import Field, ValidationError

from gfwapiclient.base.models import BaseModel


class SampleEnum(str, Enum):
    """A sample enum for testing `BaseModel` behavior."""

    START_ASC = "+start"
    START_DESC = "-start"


class SampleModel(BaseModel):
    """A sample model for testing `BaseModel` behavior."""

    start_date: str = Field(...)
    timeseries_interval: str = Field(...)
    sort: Optional[SampleEnum] = Field(SampleEnum.START_ASC)


class SampleNestedModel(BaseModel):
    """A sample nested model for testing `BaseModel` behavior."""

    id: str = Field(...)
    nested: SampleModel = Field(...)


start_date: Final[str] = "2018-01-01"
timeseries_interval: Final[str] = "YEAR"
sort: Final[str] = "+start"
duration: Final[int] = 60
id: Final[str] = "3ca9b73aee21fbf278a636709e0f8f03"


def test_base_model_serialization_snake_case_to_camel_case() -> None:
    """Tests that `BaseModel` serializes snake_case attributes to camelCase."""
    input = {"start_date": start_date, "timeseries_interval": timeseries_interval}
    expected = {
        "startDate": start_date,
        "timeseriesInterval": timeseries_interval,
        "sort": sort,
    }

    model = SampleModel(**input)  # type: ignore[arg-type]
    output = model.model_dump(by_alias=True)

    assert output == expected


def test_base_model_deserialization_camel_case_to_snake_case() -> None:
    """Tests that `BaseModel` deserializes camelCase input into snake_case attributes."""
    input = {
        "startDate": start_date,
        "timeseriesInterval": timeseries_interval,
        "sort": sort,
    }

    model = SampleModel(**input)  # type: ignore[arg-type]

    assert model.start_date == start_date
    assert model.timeseries_interval == timeseries_interval
    assert model.sort == SampleEnum.START_ASC


def test_base_model_allows_extra_fields() -> None:
    """Tests that `BaseModel` allows extra fields without raising errors."""
    input = {
        "startDate": start_date,
        "timeseriesInterval": timeseries_interval,
        "sort": sort,
        "duration": duration,
    }

    model = SampleModel(**input)  # type: ignore[arg-type]

    assert model.start_date == start_date
    assert model.timeseries_interval == timeseries_interval
    assert model.sort == SampleEnum.START_ASC
    assert model.model_dump()["duration"] == duration


def test_base_model_trims_whitespace_from_string_fields() -> None:
    """Tests that `BaseModel` automatically trims whitespace from string attributes."""
    input = {
        "startDate": f"  {start_date}  ",
        "timeseriesInterval": f"  {timeseries_interval} ",
    }

    model = SampleModel(**input)  # type: ignore[arg-type]

    assert model.start_date == start_date
    assert model.timeseries_interval == timeseries_interval
    assert model.sort == SampleEnum.START_ASC


def test_base_model_uses_default_enum_value_when_optional_field_is_missing() -> None:
    """Tests that `BaseModel` uses the default enum value when an optional enum field is missing."""
    input = {"startDate": start_date, "timeseriesInterval": timeseries_interval}

    model = SampleModel(**input)  # type: ignore[arg-type]

    assert model.start_date == start_date
    assert model.timeseries_interval == timeseries_interval
    assert model.sort == SampleEnum.START_ASC


def test_base_model_supports_nested_models() -> None:
    """Tests that `BaseModel` works correctly when nested."""
    input = {
        "id": id,
        "nested": {
            "start_date": start_date,
            "timeseries_interval": timeseries_interval,
            "sort": sort,
        },
    }
    expected = {
        "id": id,
        "nested": {
            "startDate": start_date,
            "timeseriesInterval": timeseries_interval,
            "sort": sort,
        },
    }

    model = SampleNestedModel(**input)  # type: ignore[arg-type]
    output = model.model_dump(by_alias=True)

    assert model.id == id
    assert model.nested.start_date == start_date
    assert model.nested.timeseries_interval == timeseries_interval
    assert model.nested.sort == SampleEnum.START_ASC
    assert output == expected


def test_base_model_raises_validation_error_when_required_fields_are_missing() -> None:
    """Tests that `BaseModel` raises a `ValidationError` when required fields are missing."""
    with pytest.raises(ValidationError):
        SampleModel(timeseries_interval=timeseries_interval)  # type: ignore[call-arg]


def test_base_model_raises_validation_error_when_enum_field_has_invalid_value() -> None:
    """Tests that `BaseModel` raises a `ValidationError` when an enum field has an invalid value."""
    with pytest.raises(ValidationError):
        SampleModel(
            start_date=start_date,
            timeseries_interval=timeseries_interval,
            sort="UNKNOWN",  # type: ignore[arg-type]
        )


@pytest.mark.parametrize(
    "invalid_data",
    [
        {"startDate": None, "timeseriesInterval": timeseries_interval, "sort": sort},
        {"startDate": start_date, "timeseriesInterval": None, "sort": sort},
        {
            "startDate": start_date,
            "timeseriesInterval": timeseries_interval,
            "sort": "UNKNOWN",
        },
        {"startDate": None, "timeseriesInterval": None, "sort": "UNKNOWN"},
    ],
)
def test_base_model_raises_validation_error_on_invalid_input_data(
    invalid_data: Dict[str, Any],
) -> None:
    """Tests that `BaseModel` raises a `ValidationError` on invalid input data."""
    with pytest.raises(ValidationError):
        SampleModel(**invalid_data)


def test_base_model_raises_validation_error_on_invalid_nested_model_fields() -> None:
    """Tests that `BaseModel` raises a `ValidationError` when nested model fields are invalid."""
    with pytest.raises(ValidationError):
        SampleNestedModel(
            id=id,
            nested=SampleModel(timeseries_interval=timeseries_interval),  # type: ignore[call-arg]
        )
