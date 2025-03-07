"""Global Fishing Watch (GFW) API Python Client - Events API Base Request Models."""

from typing import Any

from gfwapiclient.base.models import BaseModel


__all__ = ["EventGeometry", "EventRegion"]


# TODO: use shapely.Geometry??? or base geometry
class EventGeometry(BaseModel):
    """GeoJSON-like region where the events happen."""

    type: str
    coordinates: Any
    # FIX: Should ideally be `List[List[List[float]]]` for MultiPolygon


# TODO: extend base Region
class EventRegion(BaseModel):
    """Region where the events happen."""

    dataset: str
    id: int
