"""Global Fishing Watch (GFW) API Python Client - Vessels API Base Response Models.

This module defines base response models for the Vessels API, providing
common data structures for vessel-related information.
"""

import datetime

from typing import Any, Iterator, List, Optional, Type, TypeVar, Union

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import Result, ResultItem


__all__ = ["VesselItem", "VesselResult"]


class ExtraField(BaseModel):
    """Vessel registry extra information.

    Attributes:
        registry_source (Optional[str]):
            The source of the registry information.

        iuu_status (Optional[Any]):
            The IUU (Illegal, Unreported, Unregulated) status.

        has_compliance_info (Optional[Any]):
            Indicates if compliance information is available.

        images (Optional[Any]):
            Images associated with the vessel.

        operator (Optional[Any]):
            The operator of the vessel.

        built_year (Optional[Any]):
            The year the vessel was built.

        depth_m (Optional[Any]):
            The depth in meters.
    """

    registry_source: Optional[str] = Field(None, alias="registrySource")
    iuu_status: Optional[Any] = Field(None, alias="iuuStatus")
    has_compliance_info: Optional[Any] = Field(None, alias="hasComplianceInfo")
    images: Optional[Any] = Field(None, alias="images")
    operator: Optional[Any] = Field(None, alias="operator")
    built_year: Optional[Any] = Field(None, alias="builtYear")
    depth_m: Optional[Any] = Field(None, alias="depthM")


class RegistryInfo(BaseModel):
    """Vessel registry information.

    Attributes:
        id (Optional[str]):
            The registry ID.

        source_code (Optional[List[str]]):
            List of source codes.

        ssvid (Optional[str]):
            The Ship Static Voyage Identifier.

        flag (Optional[str]):
            The vessel's flag.

        ship_name (Optional[str]):
            The vessel's ship name.

        n_ship_name (Optional[str]):
            Normalized ship name.

        call_sign (Optional[str]):
            The vessel's call sign.

        imo (Optional[str]):
            The vessel's IMO number.

        latest_vessel_info (Optional[bool]):
            Indicates if it's the latest vessel info.

        transmission_date_from (Optional[datetime.datetime]):
            Transmission date from.

        transmission_date_to (Optional[datetime.datetime]):
            Transmission date to.

        gear_types (Optional[List[str]]):
            List of gear types.

        length_m (Optional[float]):
            Length in meters.

        tonnage_gt (Optional[float]):
            Tonnage in gross tons.

        vessel_info_reference (Optional[str]):
            Vessel info reference.

        extra_fields (Optional[List[ExtraField]]):
            List of extra fields.
    """

    id: Optional[str] = Field(None, alias="id")
    source_code: Optional[List[str]] = Field(None, alias="sourceCode")
    ssvid: Optional[str] = Field(None, alias="ssvid")
    flag: Optional[str] = Field(None, alias="flag")
    ship_name: Optional[str] = Field(None, alias="shipname")
    n_ship_name: Optional[str] = Field(None, alias="nShipname")
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
    """Vessel registry owner.

    Attributes:
        name (Optional[str]):
            The owner's name.

        flag (Optional[str]):
            The owner's flag.

        ssvid (Optional[str]):
            The Ship Static Voyage Identifier.

        source_code (Optional[List[str]]):
            List of source codes.

        date_from (Optional[datetime.datetime]):
           Date from.

        date_to (Optional[datetime.datetime]):
            Date to.
    """

    name: Optional[str] = Field(None, alias="name")
    flag: Optional[str] = Field(None, alias="flag")
    ssvid: Optional[str] = Field(None, alias="ssvid")
    source_code: Optional[List[str]] = Field(None, alias="sourceCode")
    date_from: Optional[datetime.datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime.datetime] = Field(None, alias="dateTo")


class RegistryPublicAuthorization(BaseModel):
    """Vessel registry public authorization.

    Attributes:
        date_from (Optional[datetime.datetime]):
            Date from.

        date_to (Optional[datetime.datetime]):
            Date to.

        ssvid (Optional[str]):
            The Ship Static Voyage Identifier.

        source_code (Optional[List[str]]):
            List of source codes.
    """

    date_from: Optional[datetime.datetime] = Field(None, alias="dateFrom")
    date_to: Optional[datetime.datetime] = Field(None, alias="dateTo")
    ssvid: Optional[str] = Field(None, alias="ssvid")
    source_code: Optional[List[str]] = Field(None, alias="sourceCode")


class GearType(BaseModel):
    """Vessel combined source gear type.

    Attributes:
        name (Optional[str]):
            The gear type name.

        source (Optional[str]):
            The source of the gear type information.

        year_from (Optional[int]):
            Year from.

        year_to (Optional[int]):
            Year to.
    """

    name: Optional[str] = Field(None, alias="name")
    source: Optional[str] = Field(None, alias="source")
    year_from: Optional[int] = Field(None, alias="yearFrom")
    year_to: Optional[int] = Field(None, alias="yearTo")


class ShipType(BaseModel):
    """Vessel combined source ship type.

    Attributes:
        name (Optional[str]):
            The ship type name.

        source (Optional[str]):
            The source of the ship type information.

        year_from (Optional[int]):
            Year from.

        year_to (Optional[int]):
            Year to.
    """

    name: Optional[str] = Field(None, alias="name")
    source: Optional[str] = Field(None, alias="source")
    year_from: Optional[int] = Field(None, alias="yearFrom")
    year_to: Optional[int] = Field(None, alias="yearTo")


class CombinedSourceInfo(BaseModel):
    """Vessel combined source information.

    Attributes:
        vessel_id (Optional[str]):
            The vessel ID.

        gear_types (Optional[List[GearType]]):
            List of gear types.

        ship_types (Optional[List[ShipType]]):
            List of ship types.
    """

    vessel_id: Optional[str] = Field(None, alias="vesselId")
    gear_types: Optional[List[GearType]] = Field(None, alias="geartypes")
    ship_types: Optional[List[ShipType]] = Field(None, alias="shiptypes")


class SelfReportedInfo(BaseModel):
    """Vessel self reported information.

    Attributes:
        id (Optional[str]):
            The self-reported information ID.

        ssvid (Optional[str]):
            The Ship Static Voyage Identifier.

        ship_name (Optional[str]):
            The vessel's ship name.

        n_ship_name (Optional[str]):
            Normalized ship name.

        flag (Optional[str]):
            The vessel's flag.

        call_sign (Optional[str]):
            The vessel's call sign.

        imo (Optional[str]):
            The vessel's IMO number.

        messages_counter (Optional[int]):
            Messages counter.

        positions_counter (Optional[int]):
            Positions counter.

        source_code (Optional[List[str]]):
            List of source codes.

        match_fields (Optional[str]):
            Matched fields.

        transmission_date_from (Optional[datetime.datetime]):
            Transmission date from (start).

        transmission_date_to (Optional[datetime.datetime]):
            Transmission date to (end).
    """

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
    """Vessels API result item.

    Attributes:
        dataset (Optional[str]):
            The dataset used.

        registry_info_total_records (Optional[int]):
            Total registry info records.

        registry_info (Optional[List[RegistryInfo]]):
            List of registry information.

        registry_owners (Optional[List[RegistryOwner]]):
            List of registry owners.

        registry_public_authorizations (Optional[List[RegistryPublicAuthorization]]):
            List of registry public authorizations.

        combined_sources_info (Optional[List[CombinedSourceInfo]]):
            List of combined source information.

        self_reported_info (Optional[List[SelfReportedInfo]]):
            List of self-reported information.
    """

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

    def _iter_matched_self_reported_infos(self) -> Iterator[SelfReportedInfo]:
        """Yields matched AIS self-reported vessel information.

        **Note:**  A vessel is considered matched when it includes both `registry_info`
        and `self_reported_info` (AIS), as this indicates a successful match between
        registry data and AIS information.

        See how the Vessel API is used in the Vessel Viewer
        here: https://globalfishingwatch.org/our-apis/assets/2024_Vessel_Viewer_and_APIs_behind_It.pdf

        Yields:
            SelfReportedInfo:
                Valid matched AIS self-reported vessel information.
        """
        if (
            self.registry_info_total_records
            and self.registry_info_total_records >= 1
            and self.self_reported_info
        ):
            yield from self.self_reported_info


_VesselItemT = TypeVar("_VesselItemT", bound=VesselItem)


class VesselResult(Result[_VesselItemT]):
    """Result for the Vessels API endpoints.

    This class extends :class:`Result` to provide a specialized result container
    for the Vessels API endpoints.
    """

    _result_item_class: Type[_VesselItemT]
    _data: Union[List[_VesselItemT], _VesselItemT]

    def __init__(self, *, data: Union[List[_VesselItemT], _VesselItemT]) -> None:
        """Initializes a new `VesselResult`.

        Args:
            data (Union[List[_VesselItemT], _VesselItemT]):
                The response data from the Vessels API endpoint, which can
                be either a single `ResultItem` or a list of `ResultItem` instances.
        """
        super().__init__(data=data)

    @property
    def vessel_ids(self) -> List[str]:
        """Returns matched AIS self-reported vessel identifiers (IDs).

        **Note:**  A vessel is considered matched when it includes both `registry_info`
        and `self_reported_info` (AIS), as this indicates a successful match between
        registry data and AIS information.

        See how the Vessel API is used in the Vessel Viewer
        here: https://globalfishingwatch.org/our-apis/assets/2024_Vessel_Viewer_and_APIs_behind_It.pdf

        Returns:
            List[str]:
                Valid list of matched AIS self-reported vessel identifier (ID).
        """

        def extract_vessel_ids(item: _VesselItemT) -> Iterator[Optional[str]]:
            for self_reported_info in item._iter_matched_self_reported_infos():
                yield self_reported_info.id

        mapped_vessel_ids: Iterator[Optional[str]] = self.flat_map(
            mapper=extract_vessel_ids
        )
        matched_vessel_ids: List[str] = list(
            {_vessel_id.strip() for _vessel_id in mapped_vessel_ids if _vessel_id}
        )

        return matched_vessel_ids

    @property
    def transmission_dates_from(self) -> List[datetime.date]:
        """Returns matched AIS transmission start dates.

        **Note:**  A vessel is considered matched when it includes both `registry_info`
        and `self_reported_info` (AIS), as this indicates a successful match between
        registry data and AIS information.

        See how the Vessel API is used in the Vessel Viewer
        here: https://globalfishingwatch.org/our-apis/assets/2024_Vessel_Viewer_and_APIs_behind_It.pdf

        Returns:
            List[str]:
                Valid list of matched AIS self-reported transmission date from.
        """

        def extract_transmission_date_from(
            item: _VesselItemT,
        ) -> Iterator[Optional[datetime.datetime]]:
            for self_reported_info in item._iter_matched_self_reported_infos():
                yield self_reported_info.transmission_date_from

        mapped_transmission_dates_from: Iterator[Optional[datetime.datetime]] = (
            self.flat_map(mapper=extract_transmission_date_from)
        )
        matched_transmission_dates_from: List[datetime.date] = list(
            {
                _transmission_date_from.date()
                for _transmission_date_from in mapped_transmission_dates_from
                if _transmission_date_from
            }
        )

        return matched_transmission_dates_from

    @property
    def transmission_dates_to(self) -> List[datetime.date]:
        """Returns matched AIS transmission end dates.

        **Note:**  A vessel is considered matched when it includes both `registry_info`
        and `self_reported_info` (AIS), as this indicates a successful match between
        registry data and AIS information.

        See how the Vessel API is used in the Vessel Viewer
        here: https://globalfishingwatch.org/our-apis/assets/2024_Vessel_Viewer_and_APIs_behind_It.pdf

        Returns:
            List[str]:
                Valid list of matched AIS self-reported transmission date to.
        """

        def extract_transmission_date_to(
            item: _VesselItemT,
        ) -> Iterator[Optional[datetime.datetime]]:
            for self_reported_info in item._iter_matched_self_reported_infos():
                yield self_reported_info.transmission_date_to

        mapped_transmission_dates_to: Iterator[Optional[datetime.datetime]] = (
            self.flat_map(mapper=extract_transmission_date_to)
        )
        matched_transmission_dates_to: List[datetime.date] = list(
            {
                _transmission_date_to.date()
                for _transmission_date_to in mapped_transmission_dates_to
                if _transmission_date_to
            }
        )

        return matched_transmission_dates_to
