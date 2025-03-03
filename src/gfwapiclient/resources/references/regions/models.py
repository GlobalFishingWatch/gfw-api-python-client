"""Global Fishing Watch (GFW) API Python Client - Region Models."""

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
    """Exclusive Economic Zone (EEZ) region."""

    id: Optional[int] = Field(None, title="ID", description="Region id.")
    label: Optional[str] = Field(None, title="Label", description="Region label.")
    iso3: Optional[str] = Field(None, title="ISO3", description="ISO3 country code.")
    dataset: Optional[str] = Field(
        "public-eez-areas",
        title="Dataset",
        description="Dataset name or id.",
    )


class EEZRegionResult(Result[EEZRegionItem]):
    """Result for Exclusive Economic Zone (EEZ) regions API endpoint."""

    _result_item_class: Type[EEZRegionItem]
    _data: List[EEZRegionItem]

    def __init__(self, data: List[EEZRegionItem]) -> None:
        """Initializes a new `EEZRegionItem`."""
        self._data = data


class MPARegionItem(ResultItem):
    """Marine Protected Area (MPA) region."""

    id: Optional[str] = Field(None, title="ID", description="Region id.")
    label: Optional[str] = Field(None, title="Label", description="Region label.")
    name: Optional[str] = Field(
        None, title="Name", description="Region name.", validation_alias="NAME"
    )
    dataset: Optional[str] = Field(
        "public-mpa-all",
        title="Dataset",
        description="Dataset name or id.",
    )


class MPARegionResult(Result[MPARegionItem]):
    """Result for Marine Protected Area (MPA) regions API endpoint."""

    _result_item_class: Type[MPARegionItem]
    _data: List[MPARegionItem]

    def __init__(self, data: List[MPARegionItem]) -> None:
        """Initializes a new `MPARegionResult`."""
        self._data = data


class RFMORegionItem(ResultItem):
    """Regional Fisheries Management Organization (RFMO) region."""

    id: Optional[str] = Field(None, title="ID", description="Region id.")
    label: Optional[str] = Field(None, title="Label", description="Region label.")
    rfb: Optional[str] = Field(
        None, title="Name", description="Region RFB.", validation_alias="RFB"
    )
    dataset: Optional[str] = Field(
        "public-rfmo",
        title="Dataset",
        description="Dataset name or id.",
    )


class RFMORegionResult(Result[RFMORegionItem]):
    """Result for Regional Fisheries Management Organization (RFMO) regions API endpoint."""

    _result_item_class: Type[RFMORegionItem]
    _data: List[RFMORegionItem]

    def __init__(self, data: List[RFMORegionItem]) -> None:
        """Initializes a new `RFMORegionResult`."""
        self._data = data
