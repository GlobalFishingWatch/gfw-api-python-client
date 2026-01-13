"""Global Fishing Watch (GFW) API Python Client - Regions API Response Models."""

from typing import List, Optional, Type

from pydantic import Field

from gfwapiclient.http.models import Result, ResultItem


__all__ = [
    "EEZRegionItem",
    "EEZRegionResult",
    "MPARegionItem",
    "MPARegionResult",
    "RFMORegionItem",
    "RFMORegionResult",
]


class EEZRegionItem(ResultItem):
    """Exclusive Economic Zone (EEZ) region item.

    Represents single EEZ region item returned by the EEZ regions API endpoint.

    Attributes:
        id (Optional[int]):
            Unique identifier for the EEZ region. Used in 4Wings, Events and
            Bulk Download API queries.

        label (Optional[str]):
            Human-readable name of the EEZ region.

        iso3 (Optional[str]):
            ISO 3166-1 alpha-3 country code (`null` for joint regimes and
            overlapping claims).

        iso_sov_1 (Optional[str]):
            Primary sovereignty ISO code.

        iso_sov_2 (Optional[str]):
            Secondary sovereignty ISO code (for joint regimes/overlapping claims).

        iso_sov_3 (Optional[str]):
            Tertiary sovereignty ISO code (for complex overlapping claims).

        territory_1 (Optional[str]):
            Territory name.

        dataset (str):
            Dataset name or ID. Used in 4Wings, Events and Bulk Download API queries.
    """

    id: Optional[int] = Field(None)
    label: Optional[str] = Field(None)
    iso3: Optional[str] = Field(None)
    iso_sov_1: Optional[str] = Field(None, alias="isoSov1")
    iso_sov_2: Optional[str] = Field(None, alias="isoSov2")
    iso_sov_3: Optional[str] = Field(None, alias="isoSov3")
    territory_1: Optional[str] = Field(None, alias="territory1")
    dataset: Optional[str] = Field("public-eez-areas")


class EEZRegionResult(Result[EEZRegionItem]):
    """Result for Exclusive Economic Zone (EEZ) regions API endpoint.

    Represents result (i.e., list of EEZ region items) returned by the EEZ regions
    API endpoint.

    For more details on the EEZ regions API endpoint supported response bodies,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#regions

    Attributes:
        _result_item_class (Type[EEZRegionItem]):
            The model used for individual result items.

        _data (EEZRegionItem):
            The EEZ region item returned in the response.
    """

    _result_item_class: Type[EEZRegionItem]
    _data: List[EEZRegionItem]

    def __init__(self, data: List[EEZRegionItem]) -> None:
        """Initializes a new `EEZRegionResult`.

        Args:
            data (List[EEZRegionItem]):
                The of list of EEZ region items.
        """
        super().__init__(data=data)


class MPARegionItem(ResultItem):
    """Marine Protected Area (MPA) region item.

    Represents single MPA region item returned by the MPA regions API endpoint.

    Attributes:
        id (Optional[str]):
            Unique identifier for the MPA region. Used in 4Wings, Events and
            Bulk Download API queries.

        label (Optional[str]):
            Name and designation of the Marine Protected Area.

        dataset (str):
            Dataset name or ID. Used in 4Wings, Events and Bulk Download API queries.
    """

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None)
    dataset: Optional[str] = Field("public-mpa-all")


class MPARegionResult(Result[MPARegionItem]):
    """Result for Marine Protected Area (MPA) regions API endpoint.

    Represents result (i.e., list of MPA region items) returned by the MPA regions
    API endpoint.

    For more details on the MPA regions API endpoint supported response bodies,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#regions

    Attributes:
        _result_item_class (Type[MPARegionItem]):
            The model used for individual result items.

        _data (MPARegionItem):
            The MPA region item returned in the response.
    """

    _result_item_class: Type[MPARegionItem]
    _data: List[MPARegionItem]

    def __init__(self, data: List[MPARegionItem]) -> None:
        """Initializes a new `MPARegionResult`.

        Args:
            data (List[MPARegionItem]):
                The of list of EEZ region items.
        """
        super().__init__(data=data)


class RFMORegionItem(ResultItem):
    """Regional Fisheries Management Organization (RFMO) region item.

    Represents single RFMO region item returned by the RFMO regions API endpoint.

    Attributes:
        id (Optional[str]):
            Unique identifier for the RFMO region (matches the abbreviation).
            Used in 4Wings, Events and Bulk Download API queries.

        label (Optional[str]):
            Standard abbreviation of the RFMO or fisheries body.

        id_ (Optional[str]):
            Duplicate identifier field (matches id and label).

        dataset (str):
            Dataset name or ID. Used in 4Wings, Events and Bulk Download API queries.
    """

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None)
    id_: Optional[str] = Field(None, alias="ID")
    dataset: Optional[str] = Field("public-rfmo")


class RFMORegionResult(Result[RFMORegionItem]):
    """Result for Regional Fisheries Management Organization (RFMO) regions API endpoint.

    Represents result (i.e., list of RFMO region items) returned by the RFMO regions
    API endpoint.

    For more details on the RFMO regions API endpoint supported response bodies,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#regions

    Attributes:
        _result_item_class (Type[RFMORegionItem]):
            The model used for individual result items.

        _data (RFMORegionItem):
            The RFMO region item returned in the response.
    """

    _result_item_class: Type[RFMORegionItem]
    _data: List[RFMORegionItem]

    def __init__(self, data: List[RFMORegionItem]) -> None:
        """Initializes a new `RFMORegionResult`.

        Args:
            data (List[RFMORegionItem]):
                The of list of EEZ region items.
        """
        super().__init__(data=data)
