"""Global Fishing Watch (GFW) API Python Client - Vessel Detail API Response Models."""

from typing import Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.vessels.base.response import VesselItem


__all__ = ["VesselDetailItem", "VesselDetailResult"]


class VesselDetailItem(VesselItem):
    """Result item for get vessel by id API endpoint."""

    pass


class VesselDetailResult(Result[VesselDetailItem]):
    """Result for get vessel by id API endpoint."""

    _result_item_class: Type[VesselDetailItem]
    _data: VesselDetailItem

    def __init__(self, data: VesselDetailItem) -> None:
        """Initializes a new `VesselDetailResult`."""
        self._data = data
