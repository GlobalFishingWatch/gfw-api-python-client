"""Global Fishing Watch (GFW) API Python Client - Resources."""

from gfwapiclient.resources.datasets import DatasetResource
from gfwapiclient.resources.events import EventResource
from gfwapiclient.resources.fourwings import FourWingsResource
from gfwapiclient.resources.insights import InsightResource
from gfwapiclient.resources.references import ReferenceResource
from gfwapiclient.resources.vessels import VesselResource


__all__ = [
    "DatasetResource",
    "EventResource",
    "FourWingsResource",
    "InsightResource",
    "ReferenceResource",
    "VesselResource",
]
