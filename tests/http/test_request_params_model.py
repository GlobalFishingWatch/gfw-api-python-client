"""Tests for `gfwapiclient.http.models.RequestParams`."""

from typing import ClassVar, List, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestParams


class SampleRequestParams(RequestParams):
    """A sample model for testing `RequestParams` behavior."""

    indexed_fields: ClassVar[Optional[List[str]]] = ["datasets"]
    comma_separated_fields: ClassVar[Optional[List[str]]] = ["fields", "date-range"]

    datasets: Optional[List[str]] = Field(None)
    fields: Optional[List[str]] = Field(None)
    date_range: Optional[List[str]] = Field(None, serialization_alias="date-range")
    start_date: Optional[str] = Field(None, serialization_alias="start-date")
    confidences: Optional[List[int]] = Field(None)
    limit: Optional[int] = Field(None)


def test_empty_query_params() -> None:
    """Test that an empty `RequestParams` instance returns an empty dictionary."""
    params = SampleRequestParams()  # type: ignore[call-arg]
    assert params.to_query_params() == {}


def test_indexed_fields_serialization() -> None:
    """Test that indexed fields are serialized correctly."""
    datasets = ["public-global-fishing-effort:latest"]
    params = SampleRequestParams(datasets=datasets)  # type: ignore[call-arg]

    formatted = params.to_query_params()
    expected = {"datasets[0]": datasets[0]}

    assert formatted == expected


def test_comma_separated_fields_serialization() -> None:
    """Test that comma-separated fields are serialized correctly."""
    fields = ["FLAGS", "VESSEL-IDS", "ACTIVITY-HOURS"]
    date_range = ["2022-05-01", "2022-12-01"]
    params = SampleRequestParams(fields=fields, date_range=date_range)  # type: ignore[call-arg]

    formatted = params.to_query_params()
    expected = {
        "fields": ",".join(fields),
        "date-range": ",".join(date_range),
    }

    assert formatted == expected


def test_indexed_and_comma_separated_fields_serialization() -> None:
    """Test that indexed and comma-separated fields are handled correctly together."""
    datasets = ["public-global-fishing-effort:latest"]
    fields = ["FLAGS", "VESSEL-IDS", "ACTIVITY-HOURS"]
    date_range = ["2022-05-01", "2022-12-01"]

    params = SampleRequestParams(
        datasets=datasets,
        fields=fields,
        date_range=date_range,
    )  # type: ignore[call-arg]

    formatted = params.to_query_params()
    expected = {
        "datasets[0]": datasets[0],
        "fields": ",".join(fields),
        "date-range": ",".join(date_range),
    }

    assert formatted == expected


def test_mixed_field_serialization() -> None:
    """Test that a mix of indexed, comma-separated, and regular fields are serialized correctly."""
    datasets = ["public-global-fishing-effort:latest"]
    fields = ["FLAGS", "VESSEL-IDS", "ACTIVITY-HOURS"]
    date_range = ["2022-05-01", "2022-12-01"]
    start_date = "2022-05-01"
    confidences = [3, 4]
    limit = 10

    params = SampleRequestParams(
        datasets=datasets,
        fields=fields,
        date_range=date_range,
        start_date=start_date,
        confidences=confidences,
        limit=limit,
    )

    formatted = params.to_query_params()
    expected = {
        "datasets[0]": datasets[0],
        "fields": ",".join(fields),
        "date-range": ",".join(date_range),
        "start-date": start_date,
        "confidences": confidences,
        "limit": limit,
    }

    assert formatted == expected
