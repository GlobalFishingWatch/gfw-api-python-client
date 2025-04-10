"""Tests for `gfwapiclient.http.models.ResultItem` and `gfwapiclient.http.models.Result`."""

import datetime

from typing import Any, Dict, Final, List, Optional, Type, cast

import pandas as pd
import pytest

from pydantic import Field, ValidationError

from gfwapiclient.http.models.response import Result, ResultItem


class SampleResultItem(ResultItem):
    """A sample model for testing `ResultItem` behavior."""

    id: str = Field(...)
    flags: Optional[List[str]] = Field(None)
    start_date: Optional[datetime.datetime] = Field(None, alias="startDate")
    end_date: Optional[datetime.date] = Field(None, alias="endDate")
    lat: Optional[float] = Field(None)
    lon: Optional[float] = Field(None)
    bounding_box: Optional[List[float]] = Field(None, alias="boundingBox")
    confidence: Optional[int] = Field(None)
    confidences: Optional[List[int]] = Field(None)
    intentional_disabling: Optional[bool] = Field(None, alias="intentionalDisabling")


class SampleSingleResult(Result[SampleResultItem]):
    """A sample model for testing `Result` behavior with single item."""

    _result_item_class: Type[SampleResultItem]
    _data: SampleResultItem

    def __init__(self, data: SampleResultItem) -> None:
        """Initializes `SampleSingleResult`."""
        super().__init__(data=data)


class SampleListResult(Result[SampleResultItem]):
    """A sample model for testing `Result` behavior with list of items."""

    _result_item_class: Type[SampleResultItem]
    _data: List[SampleResultItem]

    def __init__(self, data: List[SampleResultItem]) -> None:
        """Initializes `SampleResult`."""
        super().__init__(data=data)


id: Final[str] = "0c0574a6c02b90a69e1e552cb8864d26"
flags: Final[List[str]] = ["ESP", "FRA"]
start_date: Final[str] = "2016-12-30T03:50:00.000Z"
end_date: Final[str] = "2016-12-30"
lat: Final[float] = 27.4111
lon: Final[float] = 121.3678
bounding_box: Final[List[float]] = [
    121.36782959633199,
    27.411060935796353,
    121.36782959633199,
    27.411060935796353,
]
confidence: Final[int] = 3
confidences: Final[List[int]] = [3, 4]
intentional_disabling: Final[bool] = True


@pytest.fixture
def mock_result_item() -> Dict[str, Any]:
    """Fixture for a raw `ResultItem` dictionary."""
    return {
        "id": id,
        "flags": flags,
        "startDate": start_date,
        "endDate": end_date,
        "lat": lat,
        "lon": lon,
        "boundingBox": bounding_box,
        "confidence": confidence,
        "confidences": confidences,
        "intentionalDisabling": intentional_disabling,
    }


def test_result_item_deserialization_all_fields(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `ResultItem` deserializes all fields correctly."""
    model = SampleResultItem(**mock_result_item)

    assert model.id == id
    assert model.flags == flags
    assert model.start_date == datetime.datetime.fromisoformat(start_date)
    assert model.end_date == datetime.date.fromisoformat(end_date)
    assert model.lat == lat
    assert model.lon == lon
    assert model.bounding_box == bounding_box
    assert model.confidence == confidence
    assert model.confidences == confidences
    assert model.intentional_disabling == intentional_disabling


def test_result_item_raises_validation_error_when_required_fields_are_missing() -> None:
    """Tests that `ResultItem` raises a `ValidationError` when required fields are missing."""
    with pytest.raises(ValidationError):
        SampleResultItem(flags=flags)  # type: ignore[call-arg]


def test_result_initialization_with_single_result_item(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` initializes with single `ResultItem`."""
    data = SampleResultItem(**mock_result_item)

    result = SampleSingleResult(data=data)
    output: SampleResultItem = cast(SampleResultItem, result.data())

    assert output == data
    assert isinstance(output, SampleResultItem)
    assert output.id == id


def test_result_initialization_with_result_item_list(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` initializes with list of `ResultItem`."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**input)]

    result = SampleListResult(data=data)
    output: List[SampleResultItem] = cast(List[SampleResultItem], result.data())

    assert output == data
    assert isinstance(output, list)
    assert len(output) == 2
    assert output[-1].id == id


def test_result_initialization_with_empty_result_item_list() -> None:
    """Tests that `Result` initializes with empty `ResultItem` list."""
    result = SampleListResult(data=[])
    output: List[SampleResultItem] = cast(List[SampleResultItem], result.data())

    assert isinstance(output, list)
    assert len(output) == 0


def test_result_dataframe_conversion_with_single_result_item(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` converts single `ResultItem` to `DataFrame`."""
    data = SampleResultItem(**mock_result_item)

    result = SampleSingleResult(data=data)
    output: pd.DataFrame = cast(pd.DataFrame, result.df())

    assert isinstance(output, pd.DataFrame)
    assert len(output) == 1
    assert list(output.columns) == list(dict(data).keys())


def test_result_dataframe_conversion_with_result_item_list(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` converts list of `ResultItem` to `DataFrame`."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**input)]

    result = SampleListResult(data=data)
    output: pd.DataFrame = cast(pd.DataFrame, result.df())

    assert isinstance(output, pd.DataFrame)
    assert len(output) == 2
    assert list(output.columns) == list(dict(data[-1]).keys())


def test_result_dataframe_conversion_include(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` converts list of `ResultItem` to `DataFrame` including only specified fields."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**input)]

    result = SampleListResult(data=data)
    output: pd.DataFrame = cast(pd.DataFrame, result.df(include={"id", "flags"}))

    assert isinstance(output, pd.DataFrame)
    assert len(output) == 2
    assert list(output.columns) == ["id", "flags"]


def test_result_dataframe_conversion_exclude(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` converts list of `ResultItem` to `DataFrame` excluding specified fields."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**input)]

    result = SampleListResult(data=data)
    output: pd.DataFrame = cast(pd.DataFrame, result.df(exclude={"id", "flags"}))

    assert isinstance(output, pd.DataFrame)
    assert len(output) == 2
    assert "id" not in list(output.columns)
    assert "flags" not in list(output.columns)
