"""Tests for `gfwapiclient.http.models.RequestParams`."""

import datetime

from enum import Enum
from typing import ClassVar, Final, List, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestParams


class SampleRequestParamsEnum(str, Enum):
    """A sample enum for testing `RequestParams` behavior."""

    START_ASC = "+start"
    START_DESC = "-start"


class SampleRequestParams(RequestParams):
    """A sample model for testing `RequestParams` behavior."""

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
    sort: Optional[SampleRequestParamsEnum] = Field(None)


datasets: Final[List[str]] = [
    "public-global-vessel-identity:latest",
    "public-global-fishing-events:latest",
]
fields: Final[List[str]] = ["FLAGS", "VESSEL-IDS", "ACTIVITY-HOURS"]
start_date: Final[datetime.date] = datetime.date.fromisoformat("2022-05-01")
confidences: Final[List[int]] = [3, 4]
limit: Final[int] = 10
gap_intentional_disabling: Final[bool] = True
sort: Final[SampleRequestParamsEnum] = SampleRequestParamsEnum.START_ASC


def test_request_params_empty_instance_serialization() -> None:
    """Tests that `RequestParams` serializes empty instance to empty dictionary."""
    model = SampleRequestParams()  # type: ignore[call-arg]
    output = model.to_query_params()
    assert output == {}


def test_request_params_indexed_fields_serialization() -> None:
    """Test that `RequestParams` serializes indexed fields correctly."""
    input = {"datasets": datasets}
    expected = {"datasets[0]": datasets[0], "datasets[1]": datasets[1]}

    model = SampleRequestParams(**input)  # type: ignore[arg-type]
    output = model.to_query_params()

    assert output == expected


def test_request_params_comma_separated_fields_serialization() -> None:
    """Test that `RequestParams` serializes comma-separated fields correctly."""
    input = {"fields": fields}
    expected = {"fields": ",".join(fields)}

    model = SampleRequestParams(**input)  # type: ignore[arg-type]
    output = model.to_query_params()

    assert output == expected


def test_request_params_indexed_and_comma_separated_fields_serialization() -> None:
    """Test that `RequestParams` serializes indexed and comma-separated fields correctly."""
    input = {"datasets": datasets, "fields": fields}
    expected = {
        "datasets[0]": datasets[0],
        "datasets[1]": datasets[1],
        "fields": ",".join(fields),
    }

    model = SampleRequestParams(**input)  # type: ignore[arg-type]
    output = model.to_query_params()

    assert output == expected


def test_request_params_other_list_fields_serialization() -> None:
    """Test that `RequestParams` serializes other list fields (not indexed or comma-separated) correctly."""
    input = {"confidences": confidences}
    expected = {"confidences": confidences}

    model = SampleRequestParams(**input)  # type: ignore[arg-type]
    output = model.to_query_params()

    assert output == expected


def test_request_params_mixed_field_serialization() -> None:
    """Test that `RequestParams` serializes indexed, comma-separated, and regular fields correctly."""
    input = {
        "datasets": datasets,
        "fields": fields,
        "start_date": start_date,
        "confidences": confidences,
        "limit": limit,
        "gap_intentional_disabling": gap_intentional_disabling,
        "sort": sort,
    }
    expected = {
        "datasets[0]": datasets[0],
        "datasets[1]": datasets[1],
        "fields": ",".join(fields),
        "start-date": start_date.isoformat(),
        "confidences": confidences,
        "limit": limit,
        "gap-intentional-disabling": gap_intentional_disabling,
        "sort": sort.value,
    }

    model = SampleRequestParams(**input)  # type: ignore[arg-type]
    output = model.to_query_params()

    assert output == expected
