"""Global Fishing Watch (GFW) API Python Client - Get Vessels by IDs API Response Models.

This module defines response models for the Vessels API's get vessels by IDs endpoint.
"""

from typing import List, Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.vessels.base.models.response import VesselItem


__all__ = ["VesselListItem", "VesselListResult"]


class VesselListItem(VesselItem):
    """Result item for the get vessels by IDs API endpoint.

    This class extends :class:`VesselItem` to provide a specialized result item
    for the vessel list endpoint.
    """

    pass


class VesselListResult(Result[VesselListItem]):
    """Result for the get vessels by IDs API endpoint.

    This class extends :class:`Result` to provide a specialized result container
    for the vessel list endpoint.
    """

    _result_item_class: Type[VesselListItem]
    _data: List[VesselListItem]

    def __init__(self, data: List[VesselListItem]) -> None:
        """Initializes a new `VesselListResult`.

        Args:
            data (List[VesselListItem]):
                The list of result items.
        """
        super().__init__(data=data)
