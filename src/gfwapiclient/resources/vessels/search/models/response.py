"""Global Fishing Watch (GFW) API Python Client - Vessels Search API Response Models.

This module defines response models for the Vessels API's search vessels endpoint.
"""

from typing import List, Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.vessels.base.models.response import VesselItem


__all__ = ["VesselSearchItem", "VesselSearchResult"]


class VesselSearchItem(VesselItem):
    """Result item for the vessels search API endpoint.

    This class extends :class:`VesselItem` to provide a specialized result item
    for the vessel search endpoint.
    """

    pass


class VesselSearchResult(Result[VesselSearchItem]):
    """Result for the vessels search API endpoint.

    This class extends :class:`Result` to provide a specialized result container
    for the vessel search endpoint.
    """

    _result_item_class: Type[VesselSearchItem]
    _data: List[VesselSearchItem]

    def __init__(self, data: List[VesselSearchItem]) -> None:
        """Initializes a new `VesselSearchResult`.

        Args:
            data (List[VesselSearchItem]):
                The list of result items.
        """
        super().__init__(data=data)
