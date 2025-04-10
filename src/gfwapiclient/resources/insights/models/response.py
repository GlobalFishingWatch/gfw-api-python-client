"""Global Fishing Watch (GFW) API Python Client - Vessels Insights API Response Models."""

import datetime

from typing import List, Optional, Type

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import Result, ResultItem


__all__ = ["VesselInsightItem", "VesselInsightResult"]


class Period(BaseModel):
    """Vessel insights period.

    Attributes:
        start_date (Optional[datetime.date], default=None):
            The start date of the period.

        end_date (Optional[datetime.date], default=None):
            The end date of the period.
    """

    start_date: Optional[datetime.date] = Field(None, alias="startDate")
    end_date: Optional[datetime.date] = Field(None, alias="endDate")


class PeriodicCounters(BaseModel):
    """Periodic counters.

    Attributes:
        events (Optional[int], default=None):
            The total number of events.

        events_gap_off (Optional[int], default=None):
            The number of events with AIS gaps.

        events_in_rfmo_without_known_authorization (Optional[int], default=None):
            The number of events in RFMOs without known authorization.

        events_in_no_take_mpas (Optional[int], default=None):
            The number of events in no-take MPAs.
    """

    events: Optional[int] = Field(None, alias="events")
    events_gap_off: Optional[int] = Field(None, alias="eventsGapOff")
    events_in_rfmo_without_known_authorization: Optional[int] = Field(
        None, alias="eventsInRFMOWithoutKnownAuthorization"
    )
    events_in_no_take_mpas: Optional[int] = Field(None, alias="eventsInNoTakeMPAs")


class Gap(BaseModel):
    """AIS off insights.

    Attributes:
        datasets ( Optional[List[str]], default=None):
            The datasets used for AIS off insights.

        historical_counters (Optional[PeriodicCounters], default=None):
            The historical counters for AIS off events.

        period_selected_counters (Optional[PeriodicCounters], default=None):
            The counters for AIS off events in the selected period.

        ais_off (Optional[List[str]], default=None):
            The list of AIS off event IDs.
    """

    datasets: Optional[List[str]] = Field(None, alias="datasets")
    historical_counters: Optional[PeriodicCounters] = Field(
        None, alias="historicalCounters"
    )
    period_selected_counters: Optional[PeriodicCounters] = Field(
        None, alias="periodSelectedCounters"
    )
    ais_off: Optional[List[str]] = Field(None, alias="aisOff")


class Coverage(BaseModel):
    """Coverage insights.

    Attributes:
        blocks (Optional[str], default=None):
            The number of blocks covered.

        blocks_with_positions (Optional[str], default=None):
            The number of blocks with positions.

        percentage (Optional[float], default=None):
            The percentage of coverage.
    """

    blocks: Optional[str] = Field(None, alias="blocks")
    blocks_with_positions: Optional[str] = Field(None, alias="blocksWithPositions")
    percentage: Optional[float] = Field(None, alias="percentage")


class ApparentFishing(BaseModel):
    """Apparent fishing insights.

    Attributes:
        datasets (Optional[List[str]], default=None):
            The datasets used for apparent fishing insights.

        historical_counters (Optional[PeriodicCounters], default=None):
            The historical counters for apparent fishing events.

        period_selected_counters (Optional[PeriodicCounters], default=None):
            The counters for apparent fishing events in the selected period.

        events_in_rfmo_without_known_authorization (Optional[List[str]], default=None):
            The list of apparent fishing event IDs in RFMOs without known authorization.

        events_in_no_take_mpas (Optional[List[str]], default=None):
            The list of apparent fishing event IDs in no-take MPAs.
    """

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


class IuuListPeriod(BaseModel):
    """IUU list period.

    Attributes:
        from_ (Optional[datetime.datetime], default=None):
            The start date of the period.

        to (Optional[datetime.datetime], default=None):
            The end date of the period.
    """

    from_: Optional[datetime.datetime] = Field(None, alias="from")
    to: Optional[datetime.datetime] = Field(None, alias="to")


class IuuVesselList(BaseModel):
    """IUU vessel list.

    Attributes:
        values_in_the_period (Optional[List[IuuListPeriod]], default=None):
            The values in the period.

        total_times_listed (Optional[int], default=None):
            The total times listed.

        total_times_listed_in_the_period (Optional[int], default=None):
            The total times listed in the period.
    """

    values_in_the_period: Optional[List[IuuListPeriod]] = Field(
        None, alias="valuesInThePeriod"
    )
    total_times_listed: Optional[int] = Field(None, alias="totalTimesListed")
    total_times_listed_in_the_period: Optional[int] = Field(
        None, alias="totalTimesListedInThePeriod"
    )


class VesselIdentity(BaseModel):
    """IUU (Illegal, Unreported, or Unregulated) insights.

    Attributes:
        datasets (Optional[List[str]], default=None):
            The datasets used for IUU insights.

        iuu_vessel_list (Optional[IuuVesselList], default=None):
            The IUU vessel list.
    """

    datasets: Optional[List[str]] = Field(None, alias="datasets")
    iuu_vessel_list: Optional[IuuVesselList] = Field(None, alias="iuuVesselList")


class VesselInsightItem(ResultItem):
    """Vessel insight item.

    Attributes:
        period (Optional[Period], default=None):
            The period of the insights.

        vessel_ids_without_identity (Optional[List[str]], default=None):
            The list of vessel IDs without identity.

        gap (Optional[Gap], default=None): The AIS off insights.

        coverage (Optional[Coverage], default=None):
            The coverage insights.

        apparent_fishing (Optional[ApparentFishing], default=None):
            The apparent fishing insights.

        vessel_identity (Optional[VesselIdentity], default=None):
            The IUU insights.
    """

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
        """Initializes a new `VesselInsightResult`.

        Args:
            data (VesselInsightItem):
                The vessel insight item data.
        """
        super().__init__(data=data)
