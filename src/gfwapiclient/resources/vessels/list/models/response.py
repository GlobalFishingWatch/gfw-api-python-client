"""Global Fishing Watch (GFW) API Python Client - Vessels List API Response Models."""

from typing import List, Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.vessels.base.response import VesselItem


__all__ = ["VesselListItem", "VesselListResult"]


class VesselListItem(VesselItem):
    """Result item for get list of vessels filtered by ids API endpoint."""

    pass


class VesselListResult(Result[VesselListItem]):
    """Result for get list of vessels filtered by ids API endpoint."""

    _result_item_class: Type[VesselListItem]
    _data: List[VesselListItem]

    def __init__(self, data: List[VesselListItem]) -> None:
        """Initializes a new `VesselListResult`."""
        self._data = data
