"""Global Fishing Watch (GFW) API Python Client - Get Vessels Insights API Response Models."""

import datetime

from typing import Any, Dict, List, Optional, Type

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
        datasets (Optional[List[str]], default=None):
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


class PeriodicValue(BaseModel):
    """Periodic vessel value (i.e., `FLAG CHANGE`, `IUU`, `MOU` etc.).

    Attributes:
        from_ (Optional[datetime.datetime], default=None):
            The start date of the period.

        to (Optional[datetime.datetime], default=None):
            The end date of the period.

        value (Optional[Any], default=None):
            The value of the period.
    """

    from_: Optional[datetime.datetime] = Field(None, alias="from")
    to: Optional[datetime.datetime] = Field(None, alias="to")
    value: Optional[Any] = Field(None, alias="value")


class PeriodicValueList(BaseModel):
    """Periodic vessel value (i.e., `FLAG CHANGE`, `IUU`, `MOU` etc.) list.

    Attributes:
        values_in_the_period (Optional[List[PeriodicValue]], default=None):
            The values in the period.

        total_times_listed (Optional[int], default=None):
            The total times listed.

        total_times_listed_in_the_period (Optional[int], default=None):
            The total times listed in the period.
    """

    values_in_the_period: Optional[List[PeriodicValue]] = Field(
        None, alias="valuesInThePeriod"
    )
    total_times_listed: Optional[int] = Field(None, alias="totalTimesListed")
    total_times_listed_in_the_period: Optional[int] = Field(
        None, alias="totalTimesListedInThePeriod"
    )


class FlagsChanges(PeriodicValueList):
    """Periodic FLAG CHANGES list."""

    pass


class IuuVesselList(PeriodicValueList):
    """Periodic IUU vessel list."""

    pass


class MouList(PeriodicValueList):
    """Periodic MOU vessel list."""

    pass


class VesselIdentity(BaseModel):
    """FLAG CHANGES, IUU (Illegal, Unreported, or Unregulated), and MOU insights.

    Attributes:
        datasets (Optional[List[str]], default=None):
            The datasets used for IUU insights.

        flag_changes (Optional[FlagsChanges], default=None):
            The FLAG CHANGES list.

        iuu_vessel_list (Optional[IuuVesselList], default=None):
            The IUU vessel list.

        mou_list (Optional[Optional[Dict[str, MouList]]], default=None):
            The MOU vessel list.
    """

    datasets: Optional[List[str]] = Field(None, alias="datasets")
    flag_changes: Optional[FlagsChanges] = Field(None, alias="flagsChanges")
    iuu_vessel_list: Optional[IuuVesselList] = Field(None, alias="iuuVesselList")
    mou_list: Optional[Optional[Dict[str, MouList]]] = Field(None, alias="mouList")


class LongLineSetIndicator(BaseModel):
    """Longline set indicator.

    Represents the count and event IDs for a particular longline set
    indicator.

    Attributes:
        count (Optional[int], default=None):
            The number of longline set events represented by the indicator.

        entries (Optional[List[str]], default=None):
            The list of longline set event IDs represented by the indicator.
    """

    count: Optional[int] = Field(None, alias="count")
    entries: Optional[List[str]] = Field(None, alias="entries")


class ApparentLongLineSetEvents(BaseModel):
    """Apparent longline set events insights.

    Represents apparent longline set events and their day/night indicators.

    Attributes:
        datasets (Optional[List[str]], default=None):
            The datasets used for apparent longline set events insights.

        count (Optional[int], default=None):
            The total number of apparent longline set events.

        entirely_day (Optional[LongLineSetIndicator], default=None):
            Longline set events classified as entirely during the day.

        mostly_day (Optional[LongLineSetIndicator], default=None):
            Longline set events classified as mostly during the day.

        day_and_night (Optional[LongLineSetIndicator], default=None):
            Longline set events classified as occurring during both day and night.

        mostly_night (Optional[LongLineSetIndicator], default=None):
            Longline set events classified as mostly during the night.

        entirely_night (Optional[LongLineSetIndicator], default=None):
            Longline set events classified as entirely during the night.

        unclassified (Optional[LongLineSetIndicator], default=None):
            Longline set events without a day/night classification.
    """

    datasets: Optional[List[str]] = Field(None, alias="datasets")
    count: Optional[int] = Field(None, alias="count")
    entirely_day: Optional[LongLineSetIndicator] = Field(None, alias="entirelyDay")
    mostly_day: Optional[LongLineSetIndicator] = Field(None, alias="mostlyDay")
    day_and_night: Optional[LongLineSetIndicator] = Field(None, alias="dayAndNight")
    mostly_night: Optional[LongLineSetIndicator] = Field(None, alias="mostlyNight")
    entirely_night: Optional[LongLineSetIndicator] = Field(None, alias="entirelyNight")
    unclassified: Optional[LongLineSetIndicator] = Field(None, alias="unclassified")


class VesselInsightItem(ResultItem):
    """Vessel insight item.

    For more details on the Get Vessels Insights API endpoint supported
    response bodies, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/insights/insights-vessels

    Attributes:
        period (Optional[Period], default=None):
            The period of the insights.

        vessel_ids_without_identity (Optional[List[str]], default=None):
            The list of vessel IDs without identity.

        gap (Optional[Gap], default=None):
            The AIS off insights.

        coverage (Optional[Coverage], default=None):
            The coverage insights.

        apparent_fishing (Optional[ApparentFishing], default=None):
            The apparent fishing insights.

        vessel_identity (Optional[VesselIdentity], default=None):
            The FLAG CHANGES, IUU, and MOU insights.

        apparent_longline_set_events (Optional[ApparentLonglineSetEvents], default=None):
            The apparent longline set events insights.
    """

    period: Optional[Period] = Field(None, alias="period")
    vessel_ids_without_identity: Optional[List[str]] = Field(
        None, alias="vesselIdsWithoutIdentity"
    )
    gap: Optional[Gap] = Field(None, alias="gap")
    coverage: Optional[Coverage] = Field(None, alias="coverage")
    apparent_fishing: Optional[ApparentFishing] = Field(None, alias="apparentFishing")
    vessel_identity: Optional[VesselIdentity] = Field(None, alias="vesselIdentity")
    apparent_longline_set_events: Optional[ApparentLongLineSetEvents] = Field(
        None, alias="apparentLongLineSetEvents"
    )


class VesselInsightResult(Result[VesselInsightItem]):
    """Result for Vessel Insights API endpoint.

    For more details on the Get Vessels Insights API endpoint supported
    response bodies, please refer to the official Global Fishing Watch API
    documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/insights/insights-vessels

    Attributes:
        _result_item_class (Type[VesselInsightItem]):
            The model used for individual result items.

        _data (VesselInsightItem):
            The vessel insight item returned in the response.
    """

    _result_item_class: Type[VesselInsightItem]
    _data: VesselInsightItem

    def __init__(self, data: VesselInsightItem) -> None:
        """Initializes a new `VesselInsightResult`.

        Args:
            data (VesselInsightItem):
                The vessel insight data.
        """
        super().__init__(data=data)
