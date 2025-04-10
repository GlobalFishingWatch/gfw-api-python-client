"""Tests for `gfwapiclient.exceptions.validation`."""

from typing import Final

import httpx
import pytest

from pydantic import Field
from pydantic_core import ValidationError

from gfwapiclient.base.models import BaseModel
from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.exceptions.validation import (
    MODEL_VALIDATION_ERROR_MESSAGE,
    REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    RESULT_ITEM_VALIDATION_ERROR_MESSAGE,
    ModelValidationError,
    RequestBodyValidationError,
    RequestParamsValidationError,
    ResultItemValidationError,
    ResultValidationError,
)


class SampleModel(BaseModel):
    """A sample model for testing `ModelValidationError` behavior."""

    start_date: str = Field(...)
    timeseries_interval: str = Field(...)


start_date: Final[str] = "2018-01-01"


# ModelValidationError


def test_model_validation_error_inheritance() -> None:
    """Test that `ModelValidationError` is a subclass of `GFWAPIClientError`."""
    assert issubclass(ModelValidationError, GFWAPIClientError)
    assert issubclass(ModelValidationError, Exception)


def test_model_validation_error_instance_with_message() -> None:
    """Test that `ModelValidationError` can be instantiated with a custom error message."""
    error = ModelValidationError(message="Validation error occurred.")
    assert isinstance(error, ModelValidationError)
    assert len(error.errors) == 0
    assert str(error) == "Validation error occurred."
    assert repr(error).startswith("ModelValidationError")
    assert "Validation error occurred." in repr(error)


def test_model_validation_error_instance_with_no_message() -> None:
    """Test that `ModelValidationError` can be instantiated with no custom error message."""
    error = ModelValidationError()
    assert isinstance(error, ModelValidationError)
    assert len(error.errors) == 0
    assert str(error) == MODEL_VALIDATION_ERROR_MESSAGE
    assert repr(error).startswith("ModelValidationError")
    assert MODEL_VALIDATION_ERROR_MESSAGE in repr(error)


def test_model_validation_error_instance_with_pydantic_error() -> None:
    """Test that `ModelValidationError` can be instantiated with `pydantic.ValidationError`."""
    with pytest.raises(ModelValidationError) as exc_info:
        try:
            SampleModel(start_date=start_date)  # type: ignore[call-arg]
        except ValidationError as exc:
            raise ModelValidationError(error=exc) from exc

    error = exc_info.value
    assert isinstance(error, ModelValidationError)
    assert isinstance(error.__cause__, ValidationError)
    assert len(error.errors) > 0

    assert MODEL_VALIDATION_ERROR_MESSAGE in str(error)
    assert "('timeseriesInterval',)" in str(error)
    assert "Field required" in str(error)
    assert "missing" in str(error)

    assert repr(error).startswith("ModelValidationError")
    assert MODEL_VALIDATION_ERROR_MESSAGE in repr(error)
    assert "('timeseriesInterval',)" in repr(error)
    assert "Field required" in repr(error)
    assert "missing" in repr(error)


def test_model_validation_error_instance_without_pydantic_error() -> None:
    """Test that `ModelValidationError` can be instantiated without `pydantic.ValidationError`."""
    error = ModelValidationError()
    assert isinstance(error, ModelValidationError)
    assert len(error.errors) == 0
    assert str(error) == MODEL_VALIDATION_ERROR_MESSAGE
    assert repr(error).startswith("ModelValidationError")


def test_model_validation_error_raises() -> None:
    """Test that `ModelValidationError` raises properly."""
    with pytest.raises(ModelValidationError, match="Model validation failed"):
        raise ModelValidationError()


# RequestParamsValidationError


def test_request_params_validation_error_inheritance() -> None:
    """Test that `RequestParamsValidationError` is a subclass of `ModelValidationError`."""
    assert issubclass(RequestParamsValidationError, ModelValidationError)
    assert issubclass(RequestParamsValidationError, GFWAPIClientError)
    assert issubclass(RequestParamsValidationError, Exception)


def test_request_params_validation_error_instance() -> None:
    """Test that `RequestParamsValidationError` can be instantiated."""
    error = RequestParamsValidationError()
    assert isinstance(error, RequestParamsValidationError)
    assert len(error.errors) == 0
    assert str(error) == REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
    assert repr(error).startswith("RequestParamsValidationError")
    assert REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE in repr(error)


# RequestBodyValidationError


def test_request_body_validation_error_inheritance() -> None:
    """Test that `RequestBodyValidationError` is a subclass of `ModelValidationError`."""
    assert issubclass(RequestBodyValidationError, ModelValidationError)
    assert issubclass(RequestBodyValidationError, GFWAPIClientError)
    assert issubclass(RequestBodyValidationError, Exception)


def test_request_body_validation_error_instance() -> None:
    """Test that `RequestBodyValidationError` can be instantiated."""
    error = RequestBodyValidationError()
    assert isinstance(error, RequestBodyValidationError)
    assert len(error.errors) == 0
    assert str(error) == REQUEST_BODY_VALIDATION_ERROR_MESSAGE
    assert repr(error).startswith("RequestBodyValidationError")
    assert REQUEST_BODY_VALIDATION_ERROR_MESSAGE in repr(error)


# ResultItemValidationError


def test_result_item_validation_error_inheritance() -> None:
    """Test that `ResultItemValidationError` is a subclass of `ModelValidationError`."""
    assert issubclass(ResultItemValidationError, ModelValidationError)
    assert issubclass(ResultItemValidationError, GFWAPIClientError)
    assert issubclass(ResultItemValidationError, Exception)


def test_result_item_validation_error_instance() -> None:
    """Test that `ResultItemValidationError` can be instantiated."""
    error = ResultItemValidationError()
    assert isinstance(error, ResultItemValidationError)
    assert len(error.errors) == 0
    assert str(error) == RESULT_ITEM_VALIDATION_ERROR_MESSAGE
    assert repr(error).startswith("ResultItemValidationError")
    assert RESULT_ITEM_VALIDATION_ERROR_MESSAGE in repr(error)


def test_result_item_validation_error_instance_with_httpx_response() -> None:
    """Test that `ResultItemValidationError` can be instantiated with `httpx.Response`."""
    response = httpx.Response(400, json={"error": "Bad Request", "statusCode": 400})
    body = {"data": "invalid"}

    error = ResultItemValidationError(response=response, body=body)
    assert isinstance(error, ResultItemValidationError)
    assert len(error.errors) == 0

    assert RESULT_ITEM_VALIDATION_ERROR_MESSAGE in str(error)
    assert "Bad Request" in str(error)

    assert repr(error).startswith("ResultItemValidationError")
    assert RESULT_ITEM_VALIDATION_ERROR_MESSAGE in repr(error)

    assert error.response == response
    assert error.body == body


# ResultValidationError


def test_result_validation_error_inheritance() -> None:
    """Test that `ResultValidationError` is a subclass of `ModelValidationError`."""
    assert issubclass(ResultValidationError, ModelValidationError)
    assert issubclass(ResultValidationError, GFWAPIClientError)
    assert issubclass(ResultValidationError, Exception)


def test_result_validation_error_instance() -> None:
    """Test that `ResultValidationError` can be instantiated."""
    message = "Result validation error occurred."
    error = ResultValidationError(message=message)
    assert isinstance(error, ResultValidationError)
    assert len(error.errors) == 0
    assert message in str(error)
    assert repr(error).startswith("ResultValidationError")
    assert message in repr(error)


def test_result_validation_error_instance_with_httpx_response() -> None:
    """Test that `ResultValidationError` can be instantiated with `httpx.Response`."""
    message = "Result validation error occurred."
    response = httpx.Response(400, json={"error": "Bad Request", "statusCode": 400})
    body = {"data": "invalid"}

    error = ResultValidationError(message=message, response=response, body=body)
    assert isinstance(error, ResultValidationError)
    assert len(error.errors) == 0

    assert message in str(error)
    assert "Bad Request" in str(error)

    assert repr(error).startswith("ResultValidationError")
    assert message in repr(error)

    assert error.response == response
    assert error.body == body
