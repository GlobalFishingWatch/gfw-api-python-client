"""Tests for `gfwapiclient.http.models.ResultItem` and `gfwapiclient.http.models.Result`."""

import datetime

from typing import Any, Dict, Final, Iterator, List, Optional, Type, cast

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


def test_result_filter_returns_only_items_matching_predicate(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` filter with a predicate returns a new `Result` containing only matched `ResultItem` objects."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**{**input, "confidence": 4})]
    result = SampleListResult(data=data)

    def predicate(item: SampleResultItem) -> bool:
        return item is not None and item.confidence is not None and item.confidence >= 4

    filtered_result: Result[SampleResultItem] = result.filter(predicate=predicate)
    filtered_data: List[SampleResultItem] = cast(
        List[SampleResultItem], filtered_result.data()
    )

    assert filtered_result is not result
    assert isinstance(filtered_result, SampleListResult)
    assert len(filtered_data) == 1
    assert filtered_data[-1].confidence == 4


def test_result_filter_returns_empty_result_when_no_items_match_predicate(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` filter with a predicate that matches no `ResultItem` objects returns a new empty `Result`."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**{**input, "confidence": 4})]
    result = SampleListResult(data=data)

    def predicate(item: SampleResultItem) -> bool:
        return item is not None and item.confidence is not None and item.confidence >= 5

    filtered_result: Result[SampleResultItem] = result.filter(predicate=predicate)
    filtered_data: List[SampleResultItem] = cast(
        List[SampleResultItem], filtered_result.data()
    )

    assert filtered_result is not result
    assert isinstance(filtered_result, SampleListResult)
    assert len(filtered_data) == 0
    assert filtered_data == []


def test_result_filter_without_predicate_returns_all_items(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` filter without a predicate returns new `Result` containing all `ResultItem` objects."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**{**input, "confidence": 4})]
    result = SampleListResult(data=data)

    filtered_result: Result[SampleResultItem] = result.filter()
    filtered_data: List[SampleResultItem] = cast(
        List[SampleResultItem], filtered_result.data()
    )

    assert filtered_result is not result
    assert isinstance(filtered_result, SampleListResult)
    assert len(filtered_data) == 2


def test_result_filter_works_with_single_result_item(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` filter works correctly with a single `ResultItem`."""
    input = {**mock_result_item}
    data = SampleResultItem(**input)
    result = SampleSingleResult(data=data)

    def predicate(item: SampleResultItem) -> bool:
        return item is not None and item.confidence is not None and item.confidence >= 3

    filtered_result: Result[SampleResultItem] = result.filter(predicate=predicate)
    filtered_data: List[SampleResultItem] = cast(
        List[SampleResultItem], filtered_result.data()
    )

    assert filtered_result is not result
    assert isinstance(filtered_result, SampleSingleResult)
    assert len(filtered_data) == 1
    assert filtered_data[-1].confidence == 3


def test_result_filter_works_with_empty_result_set() -> None:
    """Tests that `Result` filter works correctly with empty `ResultItem` objects."""
    result = SampleListResult(data=[])

    def predicate(item: SampleResultItem) -> bool:
        return item is not None and item.confidence is not None and item.confidence >= 3

    filtered_result: Result[SampleResultItem] = result.filter(predicate=predicate)
    filtered_data: List[SampleResultItem] = cast(
        List[SampleResultItem], filtered_result.data()
    )

    assert filtered_result is not result
    assert isinstance(filtered_result, SampleListResult)
    assert len(filtered_data) == 0
    assert filtered_data == []


@pytest.mark.parametrize(
    "invalid_predicate",
    [
        "invalid",
        123,
        object(),
        True,
        [],
        {},
    ],
)
def test_result_filter_invalid_predicate_returns_result_copy(
    mock_result_item: Dict[str, Any],
    invalid_predicate: Any,
) -> None:
    """Tests that `Result` filter with an invalid predicates returns shalslow copy of the `Result`."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**{**input, "confidence": 4})]
    result = SampleListResult(data=data)

    filtered_result: Result[SampleResultItem] = result.filter(
        predicate=invalid_predicate
    )
    filtered_data: List[SampleResultItem] = cast(
        List[SampleResultItem], filtered_result.data()
    )

    assert filtered_result is not result
    assert isinstance(filtered_result, SampleListResult)
    assert len(filtered_data) == 2


def test_result_find_returns_first_matching_item(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` find returns the first `ResultItem` matching the predicate."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**{**input, "confidence": 4})]
    result = SampleListResult(data=data)

    def predicate(item: SampleResultItem) -> bool:
        return item.confidence is not None and item.confidence >= 3

    found: Optional[SampleResultItem] = result.find(predicate=predicate)

    assert found is not None
    assert isinstance(found, SampleResultItem)
    assert found.confidence == 3


def test_result_find_returns_none_when_no_items_match_predicate(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` find returns `None` when no `ResultItem` matches the predicate."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**{**input, "confidence": 4})]
    result = SampleListResult(data=data)

    def predicate(item: SampleResultItem) -> bool:
        return item.confidence is not None and item.confidence >= 5

    found: Optional[SampleResultItem] = result.find(predicate=predicate)

    assert found is None


def test_result_find_returns_none_when_predicate_is_none(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` find returns `None` when predicate is not provided."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input)]
    result = SampleListResult(data=data)

    found: Optional[SampleResultItem] = result.find()

    assert found is None


def test_result_find_returns_none_for_empty_result_set() -> None:
    """Tests that `Result` find returns `None` when the result contains no items."""
    result = SampleListResult(data=[])

    def predicate(item: SampleResultItem) -> bool:
        return True

    found: Optional[SampleResultItem] = result.find(predicate=predicate)

    assert found is None


def test_result_find_works_with_single_result_item(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` find works correctly with a single `ResultItem`."""
    item = SampleResultItem(**mock_result_item)
    result = SampleSingleResult(data=item)

    def predicate(item: SampleResultItem) -> bool:
        return item.id == cast(str, mock_result_item["id"])

    found: Optional[SampleResultItem] = result.find(predicate=predicate)

    assert found is not None
    assert found is item


def test_result_find_returns_none_when_single_item_does_not_match(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` find returns `None` when the single `ResultItem` does not match."""
    item = SampleResultItem(**mock_result_item)
    result = SampleSingleResult(data=item)

    def predicate(_: SampleResultItem) -> bool:
        return False

    found: Optional[SampleResultItem] = result.find(predicate=predicate)

    assert found is None


@pytest.mark.parametrize(
    "invalid_predicate",
    ["invalid", 123, object(), True, [], {}],
)
def test_result_find_invalid_predicate_returns_none(
    mock_result_item: Dict[str, Any],
    invalid_predicate: Any,
) -> None:
    """Tests that `Result` find with an invalid predicates returns `None`."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input)]
    result = SampleListResult(data=data)

    found: Optional[SampleResultItem] = result.find(predicate=invalid_predicate)

    assert found is None


def test_result_map_transforms_all_result_items(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` map transforms correctly all `ResultItem`."""
    data = [
        SampleResultItem(**mock_result_item),
        SampleResultItem(**{**mock_result_item, "id": mock_result_item["id"] * 2}),
    ]

    result = SampleListResult(data=data)

    def to_ids(item: SampleResultItem) -> str:
        return item.id

    mapped_result: Iterator[str] = result.map(mapper=to_ids)

    assert mapped_result is not None
    assert isinstance(mapped_result, Iterator)

    mapped_result_list: List[str] = list(mapped_result)
    assert len(mapped_result_list) == 2
    assert mapped_result_list[0] == data[0].id
    assert mapped_result_list[1] == data[1].id


def test_result_map_transforms_single_result_item(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` map transforms correctly a single `ResultItem`."""
    item = SampleResultItem(**mock_result_item)

    result = SampleSingleResult(data=item)

    def to_ids(item: SampleResultItem) -> str:
        return item.id

    mapped_result: Iterator[str] = result.map(mapper=to_ids)

    assert mapped_result is not None
    assert isinstance(mapped_result, Iterator)

    mapped_result_list: List[str] = list(mapped_result)
    assert len(mapped_result_list) == 1
    assert mapped_result_list[0] == item.id


@pytest.mark.parametrize(
    "invalid_mapper",
    ["invalid", 123, object(), True, [], {}],
)
def test_result_map_raises_type_error_for_non_callable_mapper(
    mock_result_item: Dict[str, Any],
    invalid_mapper: Any,
) -> None:
    """Tests that `Result` raises a `TypeError` when `mapper` is not callable."""
    data = [SampleResultItem(**mock_result_item)]
    result = SampleListResult(data=data)

    with pytest.raises(TypeError):
        list(result.map(mapper=invalid_mapper))


def test_result_supports_iteration(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` support iteration by implementing `__iter__`."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**{**input, "confidence": 4})]
    result = SampleListResult(data=data)

    assert list(result) == data

    for item in result:
        assert item is not None
        assert isinstance(item, SampleResultItem)


def test_result_supports_iteration_with_single_result_item(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` support iteration with a single `ResultItem`."""
    input = {**mock_result_item}
    item = SampleResultItem(**input)
    result = SampleSingleResult(data=item)

    assert list(result) == [item]

    for item in result:
        assert item is not None
        assert isinstance(item, SampleResultItem)


def test_result_supports_len(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` support len by implementing `__len__`."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input), SampleResultItem(**{**input, "confidence": 4})]
    result = SampleListResult(data=data)

    assert len(result) == 2


def test_result_supports_len_with_single_result_item(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` support len with a single `ResultItem`."""
    input = {**mock_result_item}
    data = SampleResultItem(**input)
    result = SampleSingleResult(data=data)

    assert len(result) == 1


def test_result_supports_extending(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` support appending items by implementing `extend`."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input)]
    result = SampleListResult(data=data)

    assert len(result) == 1

    values = [SampleResultItem(**{**input, "confidence": 4})]
    result.extend(values=values)

    assert len(result) == 2


def test_result_supports_extending_from_other_result(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` support appending items from other `Result`."""
    input = {**mock_result_item}
    data = [SampleResultItem(**input)]
    result = SampleListResult(data=data)

    assert len(result) == 1

    values = SampleListResult(data=[SampleResultItem(**{**input, "confidence": 4})])
    result.extend(values=values)

    assert len(result) == 2


def test_result_does_not_support_extending_with_single_result_item(
    mock_result_item: Dict[str, Any],
) -> None:
    """Tests that `Result` does not support appending items by implementing `extend`."""
    input = {**mock_result_item}
    item = SampleResultItem(**input)
    result = SampleSingleResult(item)

    assert len(result) == 1

    values = [SampleResultItem(**{**input, "confidence": 4})]
    result.extend(values=values)

    assert len(result) == 1
