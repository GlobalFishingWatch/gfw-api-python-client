"""Global Fishing Watch (GFW) API Python Client - Vessels Insights Response Models."""

import datetime

from typing import Any, Dict, List, Optional, Type

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import Result, ResultItem


__all__ = ["VesselInsightItem", "VesselInsightResult"]


class Period(BaseModel):
    """Vessel insights period."""

    start_date: Optional[datetime.date] = Field(None, alias="startDate")
    end_date: Optional[datetime.date] = Field(None, alias="endDate")


class PeriodicCounters(BaseModel):
    """Periodic counters."""

    events: Optional[int] = Field(None)
    events_gap_off: Optional[int] = Field(None, alias="eventsGapOff")
    events_in_rfmo_without_known_authorization: Optional[int] = Field(
        None, alias="eventsInRFMOWithoutKnownAuthorization"
    )
    events_in_no_take_mpas: Optional[int] = Field(None, alias="eventsInNoTakeMPAs")


class Gap(BaseModel):
    """AIS off insights."""

    datasets: Optional[List[str]] = Field(None, alias="datasets")
    historical_counters: Optional[PeriodicCounters] = Field(
        None, alias="historicalCounters"
    )
    period_selected_counters: Optional[PeriodicCounters] = Field(
        None, alias="periodSelectedCounters"
    )
    ais_off: Optional[List[str]] = Field(None, alias="aisOff")


class Coverage(BaseModel):
    """Coverage insights."""

    blocks: Optional[int] = Field(None, alias="blocks")
    blocks_with_positions: Optional[int] = Field(None, alias="blocksWithPositions")
    percentage: Optional[float] = Field(None, alias="percentage")
    # TODO: historical coverage


class ApparentFishing(BaseModel):
    """Apparent fishing insights."""

    datasets: Optional[List[str]] = Field(None, alias="datasets")
    historical_counters: Optional[PeriodicCounters] = Field(
        None, alias="historicalCounters"
    )
    period_selected_counters: Optional[PeriodicCounters] = Field(
        None, alias="periodSelectedCounters"
    )
    events_in_rfmo_without_known_authorization: Optional[List[str]] = Field(
        None, alias="eventsInRfmoWithoutKnownAuthorization"
    )
    events_in_no_take_mpas: Optional[List[str]] = Field(
        None, alias="eventsInNoTakeMpas"
    )


class IuuVesselList(BaseModel):
    """IUU vessel list."""

    values_in_the_period: Optional[List[Dict[str, Any]]] = Field(
        None, alias="valuesInThePeriod"
    )  # TODO: model
    total_times_listed: Optional[int] = Field(None, alias="totalTimesListed")
    total_times_listed_in_the_period: Optional[int] = Field(
        None, alias="totalTimesListedInThePeriod"
    )


class VesselIdentity(BaseModel):
    """IUU (Illegal, Unreported, or Unregulated) insights."""

    datasets: Optional[List[str]] = Field(None, alias="datasets")
    iuu_vessel_list: Optional[IuuVesselList] = Field(None, alias="iuuVesselList")


class VesselInsightItem(ResultItem):
    """Vessel Insights."""

    period: Optional[Period] = Field(None, alias="period")
    vessel_ids_without_identity: Optional[List[str]] = Field(
        None, alias="vesselIdsWithoutIdentity"
    )
    gap: Optional[Gap] = Field(None, alias="gap")
    coverage: Optional[Coverage] = Field(None, alias="coverage")
    apparent_fishing: Optional[ApparentFishing] = Field(None, alias="apparentFishing")
    vessel_identity: Optional[VesselIdentity] = Field(None, alias="vesselIdentity")


class VesselInsightResult(Result[VesselInsightItem]):
    """Result for Vessel Insights API endpoint."""

    _result_item_class: Type[VesselInsightItem]
    _data: VesselInsightItem

    def __init__(self, data: VesselInsightItem) -> None:
        """Initializes a new `VesselInsightResult`."""
        self._data = data
