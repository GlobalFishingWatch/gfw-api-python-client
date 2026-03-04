"""Global Fishing Watch (GFW) API Python Client - HTTP Response Models."""

from typing import (
    Any,
    Callable,
    Generic,
    Iterator,
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
            list(self._data) if isinstance(self._data, list) else self._data
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
        df = pd.DataFrame(
            [
                item.model_dump(include=include, exclude=exclude)
                for item in self._iter_data()
            ],
            **kwargs,
        )
        return df

    def filter(
        self,
        *,
        predicate: Optional[Callable[[_ResultItemT], bool]] = None,
    ) -> "Result[_ResultItemT]":
        """Filters API endpoint result data using a predicate function.

        This method returns a new `Result` instance containing only those
        `ResultItem` objects for which `predicate(item)` evaluates to `True`.

        If `predicate` is `None`, a shallow copy of the result is returned,
        containing all `ResultItem` objects.

        Args:
            predicate (Optional[Callable[[_ResultItemT], bool]], default=None):
                An optional callable that accepts a `ResultItem` instance and
                returns `True` if it should be included.

        Returns:
            Result[_ResultItemT]:
                A new `Result` instance containing the filtered `ResultItem` objects.
        """
        if predicate is None or not callable(predicate):
            return self.__class__(data=list(self._iter_data()))

        filtered_items: List[_ResultItemT] = [
            item for item in self._iter_data() if predicate(item)
        ]
        return self.__class__(data=filtered_items)

    def find(
        self,
        *,
        predicate: Optional[Callable[[_ResultItemT], bool]] = None,
    ) -> Optional[_ResultItemT]:
        """Finds the first API endpoint result item matching a predicate.

        This method returns the first `ResultItem` for which
        `predicate(item)` evaluates to `True`.

        If `predicate` is `None`, or if no items match, `None` is returned.

        Args:
            predicate (Optional[Callable[[_ResultItemT], bool]], default=None):
                An optional callable that accepts a `ResultItem` instance and
                returns `True` for the desired item.

        Returns:
            Optional[_ResultItemT]:
                The first matching `ResultItem`, or `None` if no match is found.
        """
        if predicate is None or not callable(predicate):
            return None

        for item in self._iter_data():
            if predicate(item):
                return item

        return None

    def _iter_data(self) -> Iterator[_ResultItemT]:
        """Iterate lazily over API endpoint result data without copying.

        This internal helper provides a unified iteration interface over
        the underlying response data regardless of whether the result
        contains:

        - a single `ResultItem`
        - a list of `ResultItem`

        Yields:
            _ResultItemT:
                Individual `ResultItem` contained in API endpoint result data.

        Returns:
            Iterator[_ResultItemT]:
                An iterator over API endpoint result data.
        """
        if isinstance(self._data, list):
            yield from self._data
        else:
            yield self._data


_ResultT = TypeVar("_ResultT", bound=Result[Any])
