"""Tests for `gfwapiclient.exceptions.http`."""

from typing import Type

import httpx
import pytest

from gfwapiclient.exceptions.base import GFWAPIClientError
from gfwapiclient.exceptions.http import (
    API_CONNECTION_ERROR_MESSAGE,
    API_TIMEOUT_ERROR_MESSAGE,
    APIConnectionError,
    APIError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadGatewayError,
    BadRequestError,
    ConflictError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    RequestTimeoutError,
    ServiceUnavailableError,
    UnprocessableEntityError,
)


@pytest.fixture
def mock_request(mock_base_url: str) -> httpx.Request:
    """Fixture for creating an HTTP request."""
    return httpx.Request("GET", mock_base_url + "/http-errors")


@pytest.fixture
def mock_response(mock_request: httpx.Request) -> httpx.Response:
    """Fixture for creating an HTTP response."""
    return httpx.Response(
        400,
        json={"error": "Bad Request", "statusCode": 400},
        request=mock_request,
    )


def test_api_error_inheritance() -> None:
    """Test that `APIError` is a subclass of `GFWAPIClientError`."""
    assert issubclass(APIError, GFWAPIClientError)
    assert issubclass(APIError, Exception)


def test_api_error_instance(mock_request: httpx.Request) -> None:
    """Test that `APIError` can be instantiated."""
    message = "Bad Request"
    body = {"data": "invalid"}

    error = APIError(message=message, request=mock_request, body=body)
    assert isinstance(error, APIError)
    assert error.message == message
    assert error.request == mock_request
    assert error.body == body
    assert "Bad Request" in str(error)
    assert repr(error).startswith("APIError")


def test_api_status_error_inheritance() -> None:
    """Test that `APIStatusError` is a subclass of `APIError`."""
    assert issubclass(APIStatusError, APIError)
    assert issubclass(APIStatusError, GFWAPIClientError)
    assert issubclass(APIStatusError, Exception)


def test_api_status_error_instance(mock_response: httpx.Response) -> None:
    """Test that `APIStatusError` can be instantiated."""
    message = "Bad Request"
    body = {"data": "invalid"}

    error = APIStatusError(message=message, response=mock_response, body=body)
    assert isinstance(error, APIStatusError)
    assert isinstance(error, APIError)
    assert error.message == message
    assert error.request == mock_response.request
    assert error.body == body
    assert error.response == mock_response
    assert error.status_code == mock_response.status_code
    assert "Bad Request" in str(error)
    assert repr(error).startswith("APIStatusError")


def test_api_connection_error_inheritance() -> None:
    """Test that `APIConnectionError` is a subclass of `APIError`."""
    assert issubclass(APIConnectionError, APIError)
    assert issubclass(APIConnectionError, GFWAPIClientError)
    assert issubclass(APIConnectionError, Exception)


def test_api_connection_error_instance(mock_request: httpx.Request) -> None:
    """Test that `APIConnectionError` can be instantiated."""
    error = APIConnectionError(request=mock_request)
    assert isinstance(error, APIError)
    assert error.message == API_CONNECTION_ERROR_MESSAGE
    assert error.request == mock_request
    assert API_CONNECTION_ERROR_MESSAGE in str(error)
    assert repr(error).startswith("APIConnectionError")


def test_api_timeout_error_inheritance() -> None:
    """Test that `APITimeoutError` is a subclass of `APIError`."""
    assert issubclass(APITimeoutError, APIConnectionError)
    assert issubclass(APITimeoutError, APIError)
    assert issubclass(APIConnectionError, GFWAPIClientError)
    assert issubclass(APIConnectionError, Exception)


def test_api_timeout_error_instance(mock_request: httpx.Request) -> None:
    """Test that `APITimeoutError` can be instantiated."""
    error = APITimeoutError(request=mock_request)
    assert isinstance(error, APIError)
    assert error.message == API_TIMEOUT_ERROR_MESSAGE
    assert error.request == mock_request
    assert API_TIMEOUT_ERROR_MESSAGE in str(error)
    assert repr(error).startswith("APITimeoutError")


@pytest.mark.parametrize(
    "error_class, error_status_code, error_message",
    [
        (BadRequestError, 400, "400 Bad Request"),
        (AuthenticationError, 401, "401 Authentication Error"),
        (PermissionDeniedError, 403, "403 Permission Denied Error"),
        (NotFoundError, 404, "404 Not Found Error"),
        (RequestTimeoutError, 408, "408 Request Timeout Error"),
        (ConflictError, 409, "409 Conflict Error"),
        (UnprocessableEntityError, 422, "422 Unprocessable Entity Error"),
        (RateLimitError, 429, "429 Too Many Requests"),
        (InternalServerError, 500, "500 Internal Server Error"),
        (BadGatewayError, 502, "502 Bad Gateway Error"),
        (ServiceUnavailableError, 503, "503 Service Unavailable Error"),
        (GatewayTimeoutError, 504, "504 Gateway Timeout Error"),
    ],
)
def test_http_status_error_instances(
    error_class: Type[APIStatusError],
    error_status_code: int,
    error_message: str,
    mock_request: httpx.Request,
) -> None:
    """Test that `APIStatusError` can be instantiated."""
    assert issubclass(error_class, APIStatusError)
    assert issubclass(error_class, APIError)
    assert issubclass(error_class, Exception)

    response = httpx.Response(error_status_code, request=mock_request)
    error = error_class(message=error_message, response=response)

    assert isinstance(error, error_class)
    assert error.status_code == error_status_code
    assert str(error) == error_message
    assert repr(error).startswith(error_class.__name__)
