"""Global Fishing Watch (GFW) API Python Client - Vessels Search API Response Models."""

from typing import List, Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.vessels.base.response import VesselItem


__all__ = ["VesselSearchItem", "VesselSearchResult"]


class VesselSearchItem(VesselItem):
    """Result item for vessels search API endpoint."""

    pass


class VesselSearchResult(Result[VesselSearchItem]):
    """Result for for vessels search API endpoint."""

    _result_item_class: Type[VesselSearchItem]
    _data: List[VesselSearchItem]

    def __init__(self, data: List[VesselSearchItem]) -> None:
        """Initializes a new `VesselSearchResult`."""
        self._data = data
