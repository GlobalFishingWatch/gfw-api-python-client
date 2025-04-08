"""Global Fishing Watch (GFW) API Python Client - Get Vessel by ID API Response Models.

This module defines response models for the Vessels API's get vessel by ID endpoint.
"""

from typing import Type

from gfwapiclient.http.models import Result
from gfwapiclient.resources.vessels.base.models.response import VesselItem


__all__ = ["VesselDetailItem", "VesselDetailResult"]


class VesselDetailItem(VesselItem):
    """Result item for the get vessel by ID API endpoint.

    This class extends :class:`VesselItem` to provide a specialized result item
    for the vessel detail endpoint.
    """

    pass


class VesselDetailResult(Result[VesselDetailItem]):
    """Result for the get vessel by ID API endpoint.

    This class extends :class:`Result` to provide a specialized result container
    for the vessel detail endpoint.
    """

    _result_item_class: Type[VesselDetailItem]
    _data: VesselDetailItem

    def __init__(self, data: VesselDetailItem) -> None:
        """Initializes a new `VesselDetailResult`.

        Args:
            data (VesselDetailItem):
                The data of the result.
        """
        super().__init__(data=data)
