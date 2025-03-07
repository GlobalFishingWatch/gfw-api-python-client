"""Global Fishing Watch (GFW) API Python Client - Events API Base Response Models."""

import datetime

from typing import Any, List, Optional

from pydantic import Field, field_validator

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import ResultItem


__all__ = ["EventItem"]


class EventPosition(BaseModel):
    """Event position."""

    lat: Optional[float] = Field(None, alias="lat")
    lon: Optional[float] = Field(None, alias="lon")


class EventRegions(BaseModel):
    """Event regions."""

    mpa: Optional[List[str]] = Field([], alias="mpa")
    eez: Optional[List[str]] = Field([], alias="eez")
    rfmo: Optional[List[str]] = Field([], alias="rfmo")
    fao: Optional[List[str]] = Field([], alias="fao")
    major_fao: Optional[List[str]] = Field([], alias="majorFao")
    eez_12_nm: Optional[List[str]] = Field([], alias="eez12Nm")
    high_seas: Optional[List[str]] = Field([], alias="highSeas")
    mpa_no_take_partial: Optional[List[str]] = Field([], alias="mpaNoTakePartial")
    mpa_no_take: Optional[List[str]] = Field([], alias="mpaNoTake")


class EventDistances(BaseModel):
    """Event distances."""

    start_distance_from_shore_km: Optional[float] = Field(
        None, alias="startDistanceFromShoreKm"
    )
    end_distance_from_shore_km: Optional[float] = Field(
        None, alias="endDistanceFromShoreKm"
    )
    start_distance_from_port_km: Optional[float] = Field(
        None, alias="startDistanceFromPortKm"
    )
    end_distance_from_port_km: Optional[float] = Field(
        None, alias="endDistanceFromPortKm"
    )


class EventVesselPublicAuthorization(BaseModel):
    """Event vessel public authorization."""

    has_publicly_listed_authorization: Optional[str] = Field(
        None, alias="hasPubliclyListedAuthorization"
    )
    rfmo: Optional[str] = Field(None, alias="rfmo")


class EventVessel(BaseModel):
    """Event vessel."""

    id: Optional[str] = Field(None, alias="id")
    name: Optional[str] = Field(None, alias="name")
    ssvid: Optional[str] = Field(None, alias="ssvid")
    flag: Optional[str] = Field(None, alias="flag")
    type: Optional[str] = Field(None, alias="type")
    public_authorizations: Optional[List[EventVesselPublicAuthorization]] = Field(
        [], alias="publicAuthorizations"
    )


class EventEncounter(BaseModel):
    """Event encounter."""

    vessel: Optional[EventVessel] = Field(None, alias="vessel")
    median_distance_kilometers: Optional[float] = Field(
        None, alias="medianDistanceKilometers"
    )
    median_speed_knots: Optional[float] = Field(None, alias="medianSpeedKnots")
    type: Optional[str] = Field(None, alias="type")
    potential_risk: Optional[bool] = Field(None, alias="potentialRisk")
    main_vessel_public_authorization_status: Optional[str] = Field(
        None, alias="mainVesselPublicAuthorizationStatus"
    )
    encountered_vessel_public_authorization_status: Optional[str] = Field(
        None, alias="encounteredVesselPublicAuthorizationStatus"
    )


class EventFishing(BaseModel):
    """Event fishing."""

    total_distance_km: Optional[float] = Field(None, alias="totalDistanceKm")
    average_speed_knots: Optional[float] = Field(None, alias="averageSpeedKnots")
    average_duration_hours: Optional[float] = Field(None, alias="averageDurationHours")
    potential_risk: Optional[bool] = Field(None, alias="potentialRisk")
    vessel_public_authorization_status: Optional[str] = Field(
        None, alias="vesselPublicAuthorizationStatus"
    )


class Gap(BaseModel):
    """Event gap."""

    intentional_disabling: Optional[bool] = Field(None, alias="intentionalDisabling")
    distance_km: Optional[str] = Field(None, alias="distanceKm")
    duration_hours: Optional[float] = Field(None, alias="durationHours")
    implied_speed_knots: Optional[str] = Field(None, alias="impliedSpeedKnots")
    positions_12_hours_before_sat: Optional[str] = Field(
        None, alias="positions12HoursBeforeSat"
    )
    positions_per_day_sat_reception: Optional[float] = Field(
        None, alias="positionsPerDaySatReception"
    )
    off_position: Optional[EventPosition] = Field(None, alias="offPosition")
    on_position: Optional[EventPosition] = Field(None, alias="onPosition")


class EventLoitering(BaseModel):
    """Event loitering."""

    total_time_hours: Optional[float] = Field(None, alias="totalTimeHours")
    total_distance_km: Optional[float] = Field(None, alias="totalDistanceKm")
    average_speed_knots: Optional[float] = Field(None, alias="averageSpeedKnots")
    average_distance_from_shore_km: Optional[float] = Field(
        None, alias="averageDistanceFromShoreKm"
    )


class EventPortVisitAnchorage(BaseModel):
    """Event port visit anchorage."""

    anchorage_id: Optional[str] = Field(None, alias="anchorageId")
    at_dock: Optional[bool] = Field(None, alias="atDock")
    distance_from_shore_km: Optional[float] = Field(None, alias="distanceFromShoreKm")
    flag: Optional[str] = Field(None, alias="flag")
    id: Optional[str] = Field(None, alias="id")
    lat: Optional[float] = Field(None, alias="lat")
    lon: Optional[float] = Field(None, alias="lon")
    name: Optional[str] = Field(None, alias="name")
    top_destination: Optional[str] = Field(None, alias="topDestination")


class EventPortVisit(BaseModel):
    """Event port visit."""

    visit_id: Optional[str] = Field(None, alias="visitId")
    confidence: Optional[str] = Field(None, alias="confidence")
    duration_hrs: Optional[float] = Field(None, alias="durationHrs")
    start_anchorage: Optional[EventPortVisitAnchorage] = Field(
        None, alias="startAnchorage"
    )
    intermediate_anchorage: Optional[EventPortVisitAnchorage] = Field(
        None, alias="intermediateAnchorage"
    )
    end_anchorage: Optional[EventPortVisitAnchorage] = Field(None, alias="endAnchorage")


class EventItem(ResultItem):
    """Event item."""

    start: Optional[datetime.datetime] = Field(None, alias="start")
    end: Optional[datetime.datetime] = Field(None, alias="end")
    id: Optional[str] = Field(None, alias="id")
    type: Optional[str] = Field(None, alias="type")
    position: Optional[EventPosition] = Field(None, alias="position")
    regions: Optional[EventRegions] = Field(None, alias="regions")
    bounding_box: Optional[List[float]] = Field(None, alias="boundingBox")
    distances: Optional[EventDistances] = Field(None, alias="distances")
    vessel: Optional[EventVessel] = Field(None, alias="vessel")
    encounter: Optional[EventEncounter] = Field(None, alias="encounter")
    fishing: Optional[EventFishing] = Field(None, alias="fishing")
    gap: Optional[Gap] = Field(None, alias="gap")
    loitering: Optional[EventLoitering] = Field(None, alias="loitering")
    port_visit: Optional[EventPortVisit] = Field(None, alias="portVisit")

    @field_validator(
        "start",
        "end",
        mode="before",
    )
    @classmethod
    def empty_datetime_str_to_none(cls, value: Any) -> Optional[Any]:
        """Convert any empty datetime string to `None`."""
        if isinstance(value, str) and value.strip() == "":
            return None
        return value
