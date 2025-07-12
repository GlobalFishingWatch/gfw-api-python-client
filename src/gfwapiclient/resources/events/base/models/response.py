"""Global Fishing Watch (GFW) API Python Client - Events API Base Response Models."""

import datetime

from typing import Any, List, Optional

from pydantic import Field, field_validator

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import ResultItem


__all__ = ["EventItem"]


class EventPosition(BaseModel):
    """Position of the event.

    Attributes:
        lat (Optional[float]):
            Latitude of the event.

        lon (Optional[float]):
            Longitude of the event.
    """

    lat: Optional[float] = Field(None, alias="lat")
    lon: Optional[float] = Field(None, alias="lon")


class EventRegions(BaseModel):
    """Regions associated with the event.

    Attributes:
        mpa (Optional[List[str]]):
            Marine Protected Areas.

        eez (Optional[List[str]]):
            Exclusive Economic Zones.

        rfmo (Optional[List[str]]):
            Regional Fisheries Management Organizations.

        fao (Optional[List[str]]):
            Food and Agriculture Organization areas.

        major_fao (Optional[List[str]]):
            Major FAO areas.

        eez_12_nm (Optional[List[str]]):
            12 nautical mile Exclusive Economic Zones.

        high_seas (Optional[List[str]]):
            High seas areas.

        mpa_no_take_partial (Optional[List[str]]):
            Partially no-take Marine Protected Areas.

        mpa_no_take (Optional[List[str]]):
            Fully no-take Marine Protected Areas.
    """

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
    """Distances related to the event.

    Attributes:
        start_distance_from_shore_km (Optional[float]):
            Start distance from shore in kilometers.

        end_distance_from_shore_km (Optional[float]):
            End distance from shore in kilometers.

        start_distance_from_port_km (Optional[float]):
            Start distance from port in kilometers.

        end_distance_from_port_km (Optional[float]):
            End distance from port in kilometers.
    """

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
    """Public authorization details of the vessel involved in the event.

    Attributes:
        has_publicly_listed_authorization (Optional[str]):
            Whether the vessel has publicly listed authorization.

        rfmo (Optional[str]):
            Regional Fisheries Management Organization.
    """

    has_publicly_listed_authorization: Optional[str] = Field(
        None, alias="hasPubliclyListedAuthorization"
    )
    rfmo: Optional[str] = Field(None, alias="rfmo")


class EventVessel(BaseModel):
    """Vessel involved in the event.

    Attributes:
        id (Optional[str]):
            Vessel ID.

        name (Optional[str]):
            Vessel name.

        ssvid (Optional[str]):
            Vessel SSVID.

        flag (Optional[str]):
            Vessel flag.

        type (Optional[str]):
            Vessel type.

        public_authorizations (Optional[List[EventVesselPublicAuthorization]]):
            Public authorization details.
    """

    id: Optional[str] = Field(None, alias="id")
    name: Optional[str] = Field(
        None,
        alias="name",
    )
    ssvid: Optional[str] = Field(None, alias="ssvid")
    flag: Optional[str] = Field(None, alias="flag")
    type: Optional[str] = Field(None, alias="type")
    public_authorizations: Optional[List[EventVesselPublicAuthorization]] = Field(
        [], alias="publicAuthorizations"
    )


class EventEncounter(BaseModel):
    """Encounter event details.

    Attributes:
        vessel (Optional[EventVessel]):
            Encountered vessel details.

        median_distance_kilometers (Optional[float]):
            Median distance in kilometers.

        median_speed_knots (Optional[float]):
            Median speed in knots.

        type (Optional[str]):
            Encounter type.

        potential_risk (Optional[bool]):
            Potential risk indicator.

        main_vessel_public_authorization_status (Optional[str]):
            Public authorization status of the main vessel.

        encountered_vessel_public_authorization_status (Optional[str]):
            Public authorization status of the encountered vessel.
    """

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
    """Fishing event details.

    Attributes:
        total_distance_km (Optional[float]):
            Total distance in kilometers.

        average_speed_knots (Optional[float]):
            Average speed in knots.

        average_duration_hours (Optional[float]):
            Average duration in hours.

        potential_risk (Optional[bool]):
            Potential risk indicator.

        vessel_public_authorization_status (Optional[str]):
            Public authorization status of the vessel.
    """

    total_distance_km: Optional[float] = Field(None, alias="totalDistanceKm")
    average_speed_knots: Optional[float] = Field(None, alias="averageSpeedKnots")
    average_duration_hours: Optional[float] = Field(None, alias="averageDurationHours")
    potential_risk: Optional[bool] = Field(None, alias="potentialRisk")
    vessel_public_authorization_status: Optional[str] = Field(
        None, alias="vesselPublicAuthorizationStatus"
    )


class Gap(BaseModel):
    """Gap event details.

    Attributes:
        intentional_disabling (Optional[bool]):
            Whether the gap was due to intentional disabling.

        distance_km (Optional[str]):
            Distance in kilometers.

        duration_hours (Optional[float]):
            Duration in hours.

        implied_speed_knots (Optional[str]):
            Implied speed in knots.

        positions_12_hours_before_sat (Optional[str]):
            Positions 12 hours before satellite detection.

        positions_per_day_sat_reception (Optional[float]):
            Positions per day of satellite reception.

        off_position (Optional[EventPosition]):
            Position where the gap started.

        on_position (Optional[EventPosition]):
            Position where the gap ended.
    """

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
    """Loitering event details.

    Attributes:
        total_time_hours (Optional[float]):
            Total time in hours.

        total_distance_km (Optional[float]):
            Total distance in kilometers.

        average_speed_knots (Optional[float]):
            Average speed in knots.

        average_distance_from_shore_km (Optional[float]):
            Average distance from shore in kilometers.
    """

    total_time_hours: Optional[float] = Field(None, alias="totalTimeHours")
    total_distance_km: Optional[float] = Field(None, alias="totalDistanceKm")
    average_speed_knots: Optional[float] = Field(None, alias="averageSpeedKnots")
    average_distance_from_shore_km: Optional[float] = Field(
        None, alias="averageDistanceFromShoreKm"
    )


class EventPortVisitAnchorage(BaseModel):
    """Port visit anchorage details.

    Attributes:
        anchorage_id (Optional[str]):
            Anchorage ID.

        at_dock (Optional[bool]):
            Whether the vessel was at dock.

        distance_from_shore_km (Optional[float]):
            Distance from shore in kilometers.

        flag (Optional[str]):
            Flag of the anchorage.

        id (Optional[str]):
            Anchorage ID.

        lat (Optional[float]):
            Latitude of the anchorage.

        lon (Optional[float]):
            Longitude of the anchorage.

        name (Optional[str]):
            Name of the anchorage.

        top_destination (Optional[str]):
            Top destination from the anchorage.
    """

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
    """Port visit event details.

    Attributes:
        visit_id (Optional[str]):
            Port visit ID.

        confidence (Optional[str]):
            Confidence level of the port visit.

        duration_hrs (Optional[float]):
            Duration of the port visit in hours.

        start_anchorage (Optional[EventPortVisitAnchorage]):
            Start anchorage details.

        intermediate_anchorage (Optional[EventPortVisitAnchorage]):
            Intermediate anchorage details.

        end_anchorage (Optional[EventPortVisitAnchorage]):
            End anchorage details.
    """

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
    """Event item details.

    Attributes:
        start (Optional[datetime.datetime]):
            Start time of the event.

        end (Optional[datetime.datetime]):
            End time of the event.

        id (Optional[str]):
            Event ID.

        type (Optional[str]):
            Event type.

        position (Optional[EventPosition]):
            Position of the event.

        regions (Optional[EventRegions]):
            Regions associated with the event.

        bounding_box (Optional[List[float]]):
            Bounding box of the event.

        distances (Optional[EventDistances]):
            Distances related to the event.

        vessel (Optional[EventVessel]):
            Vessel involved in the event.

        encounter (Optional[EventEncounter]):
            Encounter event details.

        fishing (Optional[EventFishing]):
            Fishing event details.

        gap (Optional[Gap]):
            Gap event details.

        loitering (Optional[EventLoitering]):
            Loitering event details.

        port_visit (Optional[EventPortVisit]):
            Port visit event details.
    """

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

    @field_validator("start", "end", mode="before")
    @classmethod
    def empty_datetime_str_to_none(cls, value: Any) -> Optional[Any]:
        """Convert any empty datetime string to `None`.

        Args:
            value (Any): The value to validate.

        Returns:
            Optional[Any]:
                The validated value, or `None` if it was an empty string.
        """
        if isinstance(value, str) and value.strip() == "":
            return None
        return value
