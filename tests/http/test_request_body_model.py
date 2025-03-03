"""Tests for `gfwapiclient.http.models.RequestBody`."""

from typing import List, Optional

from pydantic import Field

from gfwapiclient.http.models import RequestBody


class SampleRequestBody(RequestBody):
    """A sample model for testing `RequestBody` behavior."""

    datasets: Optional[List[str]] = Field(None)
    start_date: Optional[str] = Field(None, serialization_alias="startDate")
    end_date: Optional[str] = Field(None, serialization_alias="endDate")
    confidences: Optional[List[int]] = Field(None)


def test_empty_request_body() -> None:
    """Test that an empty `RequestBody` instance returns an empty dictionary."""
    params = SampleRequestBody()  # type: ignore[call-arg]
    assert params.to_json_body() == {}


def test_request_body_serialization() -> None:
    """Test that `RequestBody` serializes correctly."""
    datasets = ["public-global-fishing-effort:latest"]
    start_date = "2022-05-01"
    end_date = "2022-12-01"
    confidences = [3, 4]

    params = SampleRequestBody(
        datasets=datasets,
        start_date=start_date,
        end_date=end_date,
        confidences=confidences,
    )

    formatted = params.to_json_body()
    expected = {
        "datasets": datasets,
        "startDate": start_date,
        "endDate": end_date,
        "confidences": confidences,
    }

    assert formatted == expected


def test_request_body_excludes_none_values() -> None:
    """Test that `RequestBody` excludes fields with `None` values by default."""
    datasets = ["public-global-fishing-effort:latest"]
    start_date = "2022-05-01"
    end_date = "2022-12-01"
    confidences = None

    params = SampleRequestBody(
        datasets=datasets,
        start_date=start_date,
        end_date=end_date,
        confidences=confidences,
    )

    formatted = params.to_json_body()
    expected = {
        "datasets": datasets,
        "startDate": start_date,
        "endDate": end_date,
    }

    assert formatted == expected


def test_request_body_includes_none_when_explicitly_allowed() -> None:
    """Test that `RequestBody` includes `None` values when `exclude_none=False`."""
    params = SampleRequestBody(datasets=None)  # type: ignore[call-arg]
    formatted = params.to_json_body(exclude_none=False)

    expected = {
        "datasets": None,
        "startDate": None,
        "endDate": None,
        "confidences": None,
    }

    assert formatted == expected
