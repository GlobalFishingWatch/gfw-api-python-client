"""Test configurations for `gfwapiclient.http.endpoints`."""

import datetime

from enum import Enum
from typing import Any, ClassVar, Dict, Final, List, Optional, Type

import pytest

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models.request import RequestBody, RequestParams
from gfwapiclient.http.models.response import Result, ResultItem


class MockRequestParamsEnum(str, Enum):
    """A sample enum for testing `RequestParams` and HTTP endpoints behavior."""

    START_ASC = "+start"
    START_DESC = "-start"


class MockRequestParams(RequestParams):
    """A sample model for testing `RequestParams` and HTTP endpoints behavior."""

    indexed_fields: ClassVar[Optional[List[str]]] = ["datasets"]
    comma_separated_fields: ClassVar[Optional[List[str]]] = ["fields"]

    datasets: Optional[List[str]] = Field(None)
    fields: Optional[List[str]] = Field(None)
    start_date: Optional[datetime.date] = Field(None, serialization_alias="start-date")
    confidences: Optional[List[int]] = Field(None)
    limit: Optional[int] = Field(None)
    gap_intentional_disabling: Optional[bool] = Field(
        None, serialization_alias="gap-intentional-disabling"
    )
    sort: Optional[MockRequestParamsEnum] = Field(None)


class MockRequestBodyEnum(str, Enum):
    """A sample enum for testing `RequestBody` and HTTP endpoints behavior."""

    MONTH = "MONTH"
    YEAR = "YEAR"


class MockSubRequestBody(BaseModel):
    """A sample sub-request (inner) body for testing `RequestBody` and HTTP endpoints behavior."""

    type: str
    coordinates: Any


class MockRequestBody(RequestBody):
    """A sample model for testing `RequestBody` and HTTP endpoints behavior."""

    datasets: Optional[List[str]] = Field(None)
    start_date: Optional[datetime.date] = Field(None, serialization_alias="startDate")
    confidences: Optional[List[int]] = Field(None)
    geometry: Optional[MockSubRequestBody] = Field(None)
    duration: Optional[int] = Field(None)
    gap_intentional_disabling: Optional[bool] = Field(
        None, serialization_alias="gapIntentionalDisabling"
    )
    time_series_interval: Optional[MockRequestBodyEnum] = Field(
        None, serialization_alias="timeseriesInterval"
    )


class MockResultItem(ResultItem):
    """A sample model for testing `ResultItem` and HTTP endpoints behavior."""

    id: str = Field(...)
    flags: Optional[List[str]] = Field(None)
    start: Optional[datetime.datetime] = Field(None, alias="start")
    end: Optional[datetime.date] = Field(None, alias="end")
    lat: Optional[float] = Field(None)
    lon: Optional[float] = Field(None)
    bounding_box: Optional[List[float]] = Field(None, alias="boundingBox")
    confidence: Optional[int] = Field(None)
    confidences: Optional[List[int]] = Field(None)
    intentional_disabling: Optional[bool] = Field(None, alias="intentionalDisabling")


class MockListResult(Result[MockResultItem]):
    """A sample model for testing `Result` with a list of items and HTTP endpoints behavior."""

    _result_item_class: Type[MockResultItem]
    _data: List[MockResultItem]

    def __init__(self, data: List[MockResultItem]) -> None:
        """Initialize a new `MockListResult`."""
        super().__init__(data=data)


class MockSingleResult(Result[MockResultItem]):
    """A sample model for testing `Result` with a single item and HTTP endpoints behavior."""

    _result_item_class: Type[MockResultItem]
    _data: MockResultItem

    def __init__(self, data: MockResultItem) -> None:
        """Initialize a new `MockSingleResult`."""
        super().__init__(data=data)


datasets: Final[List[str]] = [
    "public-global-vessel-identity:latest",
    "public-global-fishing-events:latest",
]
fields: Final[List[str]] = ["FLAGS", "VESSEL-IDS", "ACTIVITY-HOURS"]
start_date: Final[datetime.date] = datetime.date.fromisoformat("2022-05-01")
confidences: Final[List[int]] = [3, 4]
limit: Final[int] = 10
gap_intentional_disabling: Final[bool] = True
sort: Final[MockRequestParamsEnum] = MockRequestParamsEnum.START_ASC
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
time_series_interval: Final[MockRequestBodyEnum] = MockRequestBodyEnum.YEAR

id: Final[str] = "0c0574a6c02b90a69e1e552cb8864d26"
flags: Final[List[str]] = ["ESP", "FRA"]
start: Final[str] = "2016-12-30T03:50:00.000Z"
end: Final[str] = "2016-12-30"
lat: Final[float] = 27.4111
lon: Final[float] = 121.3678
bounding_box: Final[List[float]] = [
    121.36782959633199,
    27.411060935796353,
    121.36782959633199,
    27.411060935796353,
]
confidence: Final[int] = 3
intentional_disabling: Final[bool] = True


@pytest.fixture
def mock_request_params() -> MockRequestParams:
    """Fixture for mock request parameters.

    Returns:
        MockRequestParams:
            An instance of `MockRequestParams` with sample data.
    """
    request_params: Dict[str, Any] = {
        "datasets": datasets,
        "fields": fields,
        "start_date": start_date,
        "confidences": confidences,
        "limit": limit,
        "gap_intentional_disabling": gap_intentional_disabling,
        "sort": sort,
    }
    return MockRequestParams(**request_params)


@pytest.fixture
def mock_request_body() -> MockRequestBody:
    """Fixture for mock request body.

    Returns:
        MockRequestBody:
            An instance of `MockRequestBody` with sample data.
    """
    request_body: Dict[str, Any] = {
        "datasets": datasets,
        "start_date": start_date,
        "confidences": confidences,
        "geometry": MockSubRequestBody(**geometry),
        "duration": duration,
        "gap_intentional_disabling": gap_intentional_disabling,
        "time_series_interval": time_series_interval,
    }
    return MockRequestBody(**request_body)


@pytest.fixture
def mock_raw_result_item() -> Dict[str, Any]:
    """Fixture for mock raw response result item.

    Returns:
        Dict[str, Any]:
            Raw `MockResultItem` sample data.
    """
    raw_result_item: Dict[str, Any] = {
        "id": id,
        "flags": flags,
        "start": start,
        "end": end,
        "lat": lat,
        "lon": lon,
        "boundingBox": bounding_box,
        "confidence": confidence,
        "confidences": confidences,
        "intentionalDisabling": intentional_disabling,
    }
    return raw_result_item


@pytest.fixture
def mock_result_item(mock_raw_result_item: Dict[str, Any]) -> MockResultItem:
    """Fixture for mock response result item.

    Returns:
        MockResultItem:
            An instance of `MockResultItem` with sample data.
    """
    return MockResultItem(**mock_raw_result_item)


@pytest.fixture
def mock_list_result(mock_result_item: MockResultItem) -> MockListResult:
    """Fixture for mock response result with a list of items.

    Returns:
        MockListResult:
            An instance of `MockListResult` with a list containing a `MockResultItem`.
    """
    return MockListResult(data=[mock_result_item])


@pytest.fixture
def mock_single_result(mock_result_item: MockResultItem) -> MockSingleResult:
    """Fixture for mock response result with a single item.

    Returns:
        MockSingleResult:
            An instance of `MockSingleResult` containing a `MockResultItem`.
    """
    return MockSingleResult(data=mock_result_item)
