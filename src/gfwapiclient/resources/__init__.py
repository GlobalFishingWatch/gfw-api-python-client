"""Global Fishing Watch (GFW) API Python Client - Resources."""

from gfwapiclient.resources.fourwings import FourWingsResource
from gfwapiclient.resources.insights import InsightResource
from gfwapiclient.resources.references import ReferenceResource
from gfwapiclient.resources.vessels.resources import VesselResource


__all__ = [
    "FourWingsResource",
    "InsightResource",
    "ReferenceResource",
    "VesselResource",
]
