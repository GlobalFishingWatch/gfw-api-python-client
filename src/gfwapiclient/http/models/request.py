"""Global Fishing Watch (GFW) API Python Client - HTTP Request Models."""

from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    TypeVar,
)

from pydantic_core import to_jsonable_python

from gfwapiclient.base.models import BaseModel


__all__ = ["RequestBody", "RequestParams", "_RequestBodyT", "_RequestParamsT"]


class RequestParams(BaseModel):
    """Base model for handling HTTP query parameters.

    This model serializes query parameters into different formats,
    including indexed lists (e.g., `field[0]=value1`),
    comma-separated lists (e.g., `field=value1,value2`), etc.

    Attributes:
        indexed_fields (ClassVar[Optional[List[str]]]):
            A list of field aliases that should be serialized as indexed list parameters
            (e.g., `field[0]=value1`, `field[1]=value2`).

        comma_separated_fields (ClassVar[Optional[List[str]]]):
            A list of field aliases that should be serialized as comma-separated parameters
            (e.g., `field=value1,value2,value3`).
    """

    indexed_fields: ClassVar[Optional[List[str]]] = None
    comma_separated_fields: ClassVar[Optional[List[str]]] = None

    def to_query_params(self, **kwargs: Any) -> Dict[str, Any]:
        """Convert a `RequestParams` instance to a dictionary-compactible HTTP query parameters.

        This method serializes the model's fields according to the specified formats
        (indexed, comma-separated, or standard) and returns a dictionary that can be used
        as query parameters in an HTTP request.

        Args:
            **kwargs (Any):
                Additional arguments passed to the `model_dump` method to customize
                the serialization process.

        Returns:
            Dict[str, Any]:
                A dictionary representing HTTP query parameters.
        """
        # Ensure default kwargs for `model_dump` are set.
        kwargs.setdefault("exclude_none", True)
        kwargs.setdefault("by_alias", True)

        # Serialize the model into a dictionary.
        base_params: Dict[str, Any] = self.model_dump(**kwargs)

        # Ensure the dictionary is JSON-serializable.
        base_json_params: Dict[str, Any] = to_jsonable_python(dict(**base_params))

        formatted_params: Dict[str, Any] = {}
        for param_key, param_value in base_json_params.items():
            if isinstance(param_value, list):
                # Serialize field as indexed list query param (e.g., "param_key[0]=value1", "param_key[1]=value2")
                if self.indexed_fields and param_key in self.indexed_fields:
                    for idx, item in enumerate(param_value):
                        formatted_params[f"{param_key}[{idx}]"] = item
                # Serialize as comma-separated string query param (e.g., "param_key=value1,value2,value3")
                elif (
                    self.comma_separated_fields
                    and param_key in self.comma_separated_fields
                ):
                    formatted_params[param_key] = ",".join(param_value)
                # Serialize as standard list query param (e.g., "param_key=value1&param_key=value2")
                else:
                    formatted_params[param_key] = param_value
            else:
                # Serialize non-list values as-is.
                formatted_params[param_key] = param_value

        return formatted_params


_RequestParamsT = TypeVar("_RequestParamsT", bound=RequestParams)


class RequestBody(BaseModel):
    """Base model for handling HTTP request bodies.

    This model serializes request bodies into a JSON-compatible dictionary,
    ensuring proper handling of null values and field aliases.
    """

    def to_json_body(self, **kwargs: Any) -> Dict[str, Any]:
        """Converts the `RequestBody` instance to a JSON-compatible HTTP request body.

        This method serializes the model's fields into a dictionary suitable for
        use as the JSON body of an HTTP request. It handles options to customize
        the serialization process.

        Args:
            **kwargs (Any):
                Additional arguments passed to the `model_dump` method to customize
                the serialization process.

        Returns:
            Dict[str, Any]:
                A dictionary representing the JSON body of the HTTP request.
        """
        # Ensure default kwargs for `model_dump` are set.
        kwargs.setdefault("exclude_none", True)
        kwargs.setdefault("by_alias", True)

        # Serialize the model into a dictionary.
        base_json_body: Dict[str, Any] = self.model_dump(**kwargs)

        # Ensure the dictionary is JSON-serializable.
        formatted_json_body: Dict[str, Any] = to_jsonable_python(dict(**base_json_body))

        return formatted_json_body


_RequestBodyT = TypeVar("_RequestBodyT", bound=RequestBody)
