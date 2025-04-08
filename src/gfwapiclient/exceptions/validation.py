"""Global Fishing Watch (GFW) API Python Client - Validation Exceptions."""

from typing import Any, Final, Optional

import httpx

from pydantic_core import ValidationError

from gfwapiclient.exceptions.base import GFWAPIClientError


__all__ = [
    "ModelValidationError",
    "RequestBodyValidationError",
    "RequestParamsValidationError",
    "ResultItemValidationError",
    "ResultValidationError",
]

MODEL_VALIDATION_ERROR_MESSAGE: Final[str] = "Model validation failed."

REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Request parameters validation failed."
)

REQUEST_BODY_VALIDATION_ERROR_MESSAGE: Final[str] = "Request body validation failed."
RESULT_ITEM_VALIDATION_ERROR_MESSAGE: Final[str] = "Result item validation failed."


class ModelValidationError(GFWAPIClientError):
    """Base exception for Pydantic model validation errors.

    Attributes:
        message (str):
            The error message.

        errors (List[ErrorDetails]):
            A list of validation errors (if available).
    """

    error: Optional[ValidationError] = None

    def __init__(
        self,
        *,
        message: Optional[str] = None,
        error: Optional[ValidationError] = None,
    ) -> None:
        """Initialize a new `ModelValidationError` exception.

        Args:
            message (Optional[str], default=None):
                Error message describing the exception.

            error (Optional[pydantic.ValidationError], default=None):
                The `pydantic.ValidationError` instance with list of
                validation errors (if available).
        """
        super().__init__(message or MODEL_VALIDATION_ERROR_MESSAGE)
        self.errors = error.errors() if error else []

    def __str__(self) -> str:
        """Return a string representation of the error."""
        if self.errors:
            _errors: str = ",\n ".join(
                f"{_error['msg']}: [loc={_error['loc']}, type={_error['type']}, "
                f"input={_error['input']}]"
                for _error in self.errors
            )
            return f"{self.message} Errors:\n {_errors}"
        return self.message

    def __repr__(self) -> str:
        """Return the canonical string representation of the error."""
        return (
            f"{self.__class__.__name__}(message={self.message!r}, "
            f"errors={self.errors!r})"
        )


class RequestParamsValidationError(ModelValidationError):
    """Exception raised when `RequestParams` validation fails."""

    def __init__(
        self,
        *,
        message: Optional[str] = None,
        error: Optional[ValidationError] = None,
    ) -> None:
        """Initialize a new `RequestParamsValidationError` exception.

        Args:
            message (Optional[str], default=None):
                Error message describing the exception.

            error (Optional[pydantic.ValidationError], default=None):
                The `pydantic.ValidationError` instance with list of
                validation errors (if available).
        """
        _message: str = message or REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
        super().__init__(message=_message, error=error)


class RequestBodyValidationError(ModelValidationError):
    """Exception raised when `RequestBody` validation fails."""

    def __init__(
        self,
        *,
        message: Optional[str] = None,
        error: Optional[ValidationError] = None,
    ) -> None:
        """Initialize a new `RequestBodyValidationError` exception.

        Args:
            message (Optional[str], default=None):
                Error message describing the exception.

            error (Optional[pydantic.ValidationError], default=None):
                The `pydantic.ValidationError` instance with list of
                validation errors (if available).
        """
        _message: str = message or REQUEST_BODY_VALIDATION_ERROR_MESSAGE
        super().__init__(message=_message, error=error)


class ResultItemValidationError(ModelValidationError):
    """Raised when a `ResultItem` is invalid.

    Attributes:
        response (Optional[httpx.Response]):
            Associated HTTP response (if available).

        body (Optional[Any]):
            Associated HTTP response body content (if available).
    """

    response: Optional[httpx.Response] = None
    body: Optional[Any] = None

    def __init__(
        self,
        *,
        error: Optional[ValidationError] = None,
        response: Optional[httpx.Response] = None,
        body: Optional[Any] = None,
    ) -> None:
        """Initialize a new `ResultItemValidationError` exception.

        Args:
            error (Optional[pydantic.ValidationError], default=None):
                The `pydantic.ValidationError` instance with list of
                validation errors (if available).

            response (Optional[httpx.Response], default=None):
                The HTTP response received.

            body (Optional[Any], default=None):
                The HTTP response body content.
        """
        super().__init__(message=RESULT_ITEM_VALIDATION_ERROR_MESSAGE, error=error)
        self.response = response
        self.body = body

    def __str__(self) -> str:
        """Return a string representation of the error."""
        _message: str = super().__str__()
        if self.response:
            _message = f"{_message} \nResponse: {self.response.text}"
        return _message

    def __repr__(self) -> str:
        """Return the canonical string representation of the error."""
        return (
            f"{self.__class__.__name__}(message={self.message!r}, "
            f"errors={self.errors!r}, response={self.response!r}, "
            f"body={self.body!r})"
        )


class ResultValidationError(ModelValidationError):
    """Raised when a `Result` or received HTTP response is invalid.

    Attributes:
        response (Optional[httpx.Response]):
            Associated HTTP response (if available).

        body (Optional[Any]):
            Associated HTTP response body content (if available).
    """

    def __init__(
        self,
        *,
        message: Optional[str] = None,
        error: Optional[ValidationError] = None,
        response: Optional[httpx.Response] = None,
        body: Optional[Any] = None,
    ) -> None:
        """Initialize a new `ResultValidationError` exception.

        Args:
            message (Optional[str], default=None):
                Error message describing the exception.

            error (Optional[pydantic.ValidationError], default=None):
                The `pydantic.ValidationError` instance with list of
                validation errors (if available).

            response (Optional[httpx.Response], default=None):
                The HTTP response received.

            body (Optional[Any], default=None):
                The HTTP response body content.
        """
        # TODO: default _message = message or "Result validation error."
        super().__init__(message=message, error=error)
        self.response = response
        self.body = body

    def __str__(self) -> str:
        """Return a string representation of the error."""
        _message: str = super().__str__()
        if self.response:
            _message = f"{_message} \nResponse: {self.response.text}"
        return _message

    def __repr__(self) -> str:
        """Return the canonical string representation of the error."""
        return (
            f"{self.__class__.__name__}(message={self.message!r}, "
            f"errors={self.errors!r}, response={self.response!r}, "
            f"body={self.body!r})"
        )
