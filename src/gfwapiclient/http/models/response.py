"""Global Fishing Watch (GFW) API Python Client - HTTP Response Models."""

from typing import (
    Any,
    Generic,
    List,
    Optional,
    Set,
    Type,
    TypeVar,
    Union,
)

import geopandas as gpd
import pandas as pd

from gfwapiclient.base.models import BaseModel


__all__ = ["Result", "ResultItem", "_ResultItemT", "_ResultT"]


class ResultItem(BaseModel):
    """Base model for handling individual data items within API endpoint responses.

    This model serves as a base for defining the structure of individual data items
    returned by API endpoints. It extends `BaseModel` to leverage Pydantic's data
    validation and serialization capabilities, ensuring that response data is
    correctly parsed and represented as Python objects.

    Specific API response item models should inherit from this class and define
    their own fields to match the structure of the data they represent.
    """

    pass


_ResultItemT = TypeVar("_ResultItemT", bound=ResultItem)


class Result(Generic[_ResultItemT]):
    """Base model for representing API endpoint response results.

    This model encapsulates the response data from an API endpoint, which can
    be either a single `ResultItem` or a list of `ResultItem` instances. It
    provides methods to access the data in Pydantic model format or convert
    it to a pandas `DataFrame` or `GeoDataFrame`.

    Specific API endpoints should inherit from this class to define their own
    `Result` model, and specifying the `ResultItem` type.
    """

    _result_item_class: Type[_ResultItemT]
    _data: Union[List[_ResultItemT], _ResultItemT]

    def __init__(self, *, data: Union[List[_ResultItemT], _ResultItemT]) -> None:
        """Initializes a new `Result` instance.

        Args:
            data (Union[List[_ResultItemT], _ResultItemT]):
                The response data from the API endpoint, which can be either a single
                `ResultItem` or a list of `ResultItem` instances.
        """
        self._data = data

    def data(
        self,
        **kwargs: Any,
    ) -> Union[List[_ResultItemT], _ResultItemT]:
        """Returns the API endpoint result data in Pydantic model format.

        This method provides direct access to the underlying data, which can be
        either a single `ResultItem` instance or a list of `ResultItem` instances.

        Args:
            **kwargs (Any):
                Additional arguments passed to the `model_dump` method to customize
                the serialization process.

        Returns:
            Union[List[_ResultItemT], _ResultItemT]:
                The API endpoint result data, either a single `ResultItem` or a list of `ResultItem`.
        """
        _items: Union[List[_ResultItemT], _ResultItemT] = (
            [*self._data] if isinstance(self._data, list) else self._data
        )
        return _items

    def df(
        self,
        *,
        include: Optional[Set[str]] = None,
        exclude: Optional[Set[str]] = None,
        **kwargs: Any,
    ) -> Union[pd.DataFrame, gpd.GeoDataFrame]:
        """Returns the API endpoint result as a `DataFrame` or `GeoDataFrame`.

        This method converts the response data into a `DataFrame` or `GeoDataFrame`,
        allowing for easy data manipulation and analysis.

        Args:
            include (Optional[Set[str]]):
                A set of field names to include in the DataFrame.
                If `None`, all fields are included.

            exclude (Optional[Set[str]]):
                A set of field names to exclude from the DataFrame.
                If `None`, no fields are excluded.

            **kwargs (Any):
                Additional keyword arguments to pass to `DataFrame` or `GeoDataFrame` constructor.

        Returns:
            Union[pd.DataFrame, gpd.GeoDataFrame]:
                A `DataFrame` representing the API endpoint result. If the result items
                contain geospatial data, a `GeoDataFrame` may be returned.
        """
        items: List[_ResultItemT] = (
            [*self._data] if isinstance(self._data, list) else [self._data]
        )
        df = pd.DataFrame(
            [item.model_dump(include=include, exclude=exclude) for item in items],
            **kwargs,
        )
        return df


_ResultT = TypeVar("_ResultT", bound=Result[Any])
