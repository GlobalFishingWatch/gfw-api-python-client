"""Global Fishing Watch (GFW) API Python Client - HTTP Models."""

import json

from typing import (
    Any,
    ClassVar,
    Dict,
    Generic,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

from gfwapiclient.base.models import BaseModel


__all__ = ["RequestBody", "RequestParams", "Result", "ResultItem"]


class RequestParams(BaseModel):
    """Base model for handling HTTP query parameters.

    This model serialize query parameters into different formats,
    including indexed lists (e.g., `field[0]=value1`),
    comma-separated lists (e.g., `field=value1,value2`), etc.

    Attributes:
        indexed_fields (ClassVar[Optional[List[str]]]):
            A list of field names that should be serialized as indexed list parameters
            (e.g., `field[0]=value1`, `field[1]=value2`).

        comma_separated_fields (ClassVar[Optional[List[str]]]):
            A list of field names that should be serialized as comma-separated parameters
            (e.g., `field=value1,value2,value3`).
    """

    indexed_fields: ClassVar[Optional[List[str]]] = None
    comma_separated_fields: ClassVar[Optional[List[str]]] = None

    def to_query_params(self, **kwargs: Any) -> Dict[str, Any]:
        """Convert a `RequestParams` instance to a dictionary suitable for HTTP query parameters.

        Args:
            **kwargs (Any):
                Additional arguments passed to Pydantic's `model_dump` method.

        Returns:
            Dict[str, Any]:
                A dictionary representing query parameters.
        """
        kwargs.setdefault("exclude_none", True)
        kwargs.setdefault("by_alias", True)

        base_params: Dict[str, Any] = self.model_dump(**kwargs)
        formatted_params: Dict[str, Any] = {}

        for key, value in base_params.items():
            if isinstance(value, list):
                if self.indexed_fields and key in self.indexed_fields:
                    # Format as indexed list (e.g., "key[0]=value1", "key[1]=value2")
                    for idx, item in enumerate(value):
                        formatted_params[f"{key}[{idx}]"] = item
                elif self.comma_separated_fields and key in self.comma_separated_fields:
                    # Format as comma-separated string (e.g., "key=value1,value2,value3")
                    formatted_params[key] = ",".join(value)
                else:
                    # Default list behavior (e.g., "key=value1&key=value2")
                    formatted_params[key] = value
            else:
                formatted_params[key] = value

        return formatted_params


_RequestParamsT = TypeVar("_RequestParamsT", bound=RequestParams)


class RequestBody(BaseModel):
    """Base model for handling HTTP request bodies.

    This model serialize request bodies into JSON format,
    ensuring proper handling of null values and field aliases.
    """

    def to_json_body(self, **kwargs: Any) -> Dict[str, Any]:
        """Convert a `RequestBody` instance to a JSON-compatible dictionary.

        Args:
            **kwargs (Any):
                Additional arguments passed to Pydantic's `model_dump` method.

        Returns:
            Dict[str, Any]:
                A dictionary representing the JSON body of the HTTP request.
        """
        kwargs.setdefault("exclude_none", True)
        kwargs.setdefault("by_alias", True)

        # FIX: self.model_dump(**kwargs)
        # FIX: from pydantic_core import to_jsonable_python
        base_json_body: str = self.model_dump_json(**kwargs)
        formatted_json_body: Dict[str, Any] = json.loads(base_json_body)
        return formatted_json_body


_RequestBodyT = TypeVar("_RequestBodyT", bound=RequestBody)


class ResultItem(BaseModel):
    """Base model for handling HTTP response data."""

    pass


_ResultItemT = TypeVar("_ResultItemT", bound=ResultItem)


class Result(Generic[_ResultItemT]):
    """Base model for representing API response result."""

    _result_item_class: Type[_ResultItemT]
    _data: Union[List[_ResultItemT], _ResultItemT]

    def __init__(self, data: Union[List[_ResultItemT], _ResultItemT]) -> None:
        """Initializes a new `Result`."""
        self._data = data

    @property
    def data(
        self, **kwargs: Optional[Dict[str, Any]]
    ) -> Union[List[_ResultItemT], _ResultItemT]:
        """Returns result data."""
        return self._data


_ResultT = TypeVar("_ResultT", bound=Result[Any])  # TODO: fix typing
