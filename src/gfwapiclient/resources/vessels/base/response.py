"""Global Fishing Watch (GFW) API Python Client - Vessels API Base Response Models."""

import datetime

from typing import List, Optional

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import ResultItem


__all__ = ["VesselItem"]


class ExtraField(BaseModel):
    """Vessel registry extra information."""

    registry_source: Optional[str] = Field(None, alias="registrySource")
    iuu_status: Optional[str] = Field(None, alias="iuuStatus")
    has_compliance_info: Optional[str] = Field(None, alias="hasComplianceInfo")
    images: Optional[List[str]] = Field(None, alias="images")  # TODO: verify or use Any
    operator: Optional[str] = Field(None, alias="operator")
    # built_year: Optional[int] = Field(None, alias="builtYear")
    # depth_m: Optional[float] = Field(None, alias="depthM")


class RegistryInfo(BaseModel):
    """Vessel registry information."""

    id: Optional[str] = Field(None, alias="id")
    source_code: Optional[List[str]] = Field(None, alias="sourceCode")
    ssvid: Optional[str] = Field(None, alias="ssvid")
    flag: Optional[str] = Field(None, alias="flag")
    ship_name: Optional[str] = Field(None, alias="shipname")
    n_ship_name: Optional[str] = Field(
        None, alias="nShipname", description="Normalized ship name"
    )
    call_sign: Optional[str] = Field(None, alias="callsign")
    imo: Optional[str] = Field(None, alias="imo")
    latest_vessel_info: Optional[bool] = Field(None, alias="latestVesselInfo")
    transmission_date_from: Optional[datetime.datetime] = Field(
        None, alias="transmissionDateFrom"
    )
    transmission_date_to: Optional[datetime.datetime] = Field(
        None, alias="transmissionDateTo"
    )
    gear_types: Optional[List[str]] = Field(None, alias="geartypes")
    length_m: Optional[float] = Field(None, alias="lengthM")
    tonnage_gt: Optional[float] = Field(None, alias="tonnageGt")
    vessel_info_reference: Optional[str] = Field(None, alias="vesselInfoReference")
    extra_fields: Optional[List[ExtraField]] = Field(None, alias="extraFields")


class RegistryOwner(BaseModel):
    """Vessel registry owner."""

    name: Optional[str] = Field(None, alias="name")
    flag: Optional[str] = Field(None, alias="flag")
    ssvid: Optional[str] = Field(None, alias="ssvid")
    source_code: Optional[List[str]] = Field(None, alias="sourceCode")
    date_from: Optional[datetime.datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime.datetime] = Field(None, alias="dateTo")


class RegistryPublicAuthorization(BaseModel):
    """Vessel registry public authorization."""

    date_from: Optional[datetime.datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime.datetime] = Field(None, alias="dateTo")
    ssvid: Optional[str] = Field(None, alias="ssvid")
    source_code: Optional[List[str]] = Field(None, alias="sourceCode")


class GearType(BaseModel):
    """Vessel combined source gear type."""

    name: Optional[str] = Field(None, alias="name")
    source: Optional[str] = Field(None, alias="source")
    year_from: Optional[int] = Field(None, alias="yearFrom")
    year_to: Optional[int] = Field(None, alias="yearTo")


class ShipType(BaseModel):
    """Vessel combined source ship type."""

    name: Optional[str] = Field(None, alias="name")
    source: Optional[str] = Field(None, alias="source")
    year_from: Optional[int] = Field(None, alias="yearFrom")
    year_to: Optional[int] = Field(None, alias="yearTo")


class CombinedSourceInfo(BaseModel):
    """Vessel combined source information."""

    vessel_id: Optional[str] = Field(None, alias="vesselId")
    gear_types: Optional[List[GearType]] = Field(None, alias="geartypes")
    ship_types: Optional[List[ShipType]] = Field(None, alias="shiptypes")


class SelfReportedInfo(BaseModel):
    """Vessel self reported information."""

    id: Optional[str] = Field(None, alias="id")
    ssvid: Optional[str] = Field(None, alias="ssvid")
    ship_name: Optional[str] = Field(None, alias="shipname")
    n_ship_name: Optional[str] = Field(None, alias="nShipname")
    flag: Optional[str] = Field(None, alias="flag")
    call_sign: Optional[str] = Field(None, alias="callsign")
    imo: Optional[str] = Field(None, alias="imo")
    messages_counter: Optional[int] = Field(None, alias="messagesCounter")
    positions_counter: Optional[int] = Field(None, alias="positionsCounter")
    source_code: Optional[List[str]] = Field(None, alias="sourceCode")
    match_fields: Optional[str] = Field(None, alias="matchFields")
    transmission_date_from: Optional[datetime.datetime] = Field(
        None, alias="transmissionDateFrom"
    )
    transmission_date_to: Optional[datetime.datetime] = Field(
        None, alias="transmissionDateTo"
    )


class VesselItem(ResultItem):
    """Vessels API result item."""

    dataset: Optional[str] = Field(None, alias="dataset")
    registry_info_total_records: Optional[int] = Field(
        None, alias="registryInfoTotalRecords"
    )
    registry_info: Optional[List[RegistryInfo]] = Field(None, alias="registryInfo")
    registry_owners: Optional[List[RegistryOwner]] = Field(None, alias="registryOwners")
    registry_public_authorizations: Optional[List[RegistryPublicAuthorization]] = Field(
        None, alias="registryPublicAuthorizations"
    )
    combined_sources_info: Optional[List[CombinedSourceInfo]] = Field(
        None, alias="combinedSourcesInfo"
    )
    self_reported_info: Optional[List[SelfReportedInfo]] = Field(
        None, alias="selfReportedInfo"
    )
