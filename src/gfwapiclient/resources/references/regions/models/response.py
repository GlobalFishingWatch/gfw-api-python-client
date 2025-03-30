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

    Attributes:
        id (Optional[int]):
            Region ID.

        label (Optional[str]):
            Region label.

        iso3 (Optional[str]):
            ISO3 country code.

        dataset (str):
            Dataset name or ID.
    """

    id: Optional[int] = Field(None)
    label: Optional[str] = Field(None)
    iso3: Optional[str] = Field(None)
    dataset: Optional[str] = Field("public-eez-areas")


class EEZRegionResult(Result[EEZRegionItem]):
    """Result for Exclusive Economic Zone (EEZ) regions API endpoint.

    This model represents the result returned by the EEZ regions API endpoint.
    See the API documentation for more details:
    https://globalfishingwatch.org/our-apis/documentation#regions
    """

    _result_item_class: Type[EEZRegionItem]
    _data: List[EEZRegionItem]

    def __init__(self, data: List[EEZRegionItem]) -> None:
        """Initializes a new `EEZRegionResult`.

        Args:
            data (List[EEZRegionItem]):
                A list of `EEZRegionItem` objects representing the EEZ regions.
        """
        super().__init__(data=data)


class MPARegionItem(ResultItem):
    """Marine Protected Area (MPA) region item.

    Attributes:
        id (Optional[str]):
            Region ID.

        label (Optional[str]):
            Region label.

        name (Optional[str]):
            Region name.

        dataset (str):
            Dataset name or ID.
    """

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None)
    name: Optional[str] = Field(None, validation_alias="NAME")
    dataset: Optional[str] = Field("public-mpa-all")


class MPARegionResult(Result[MPARegionItem]):
    """Result for Marine Protected Area (MPA) regions API endpoint.

    This model represents the result returned by the MPA regions API endpoint.
    See the API documentation for more details:
    https://globalfishingwatch.org/our-apis/documentation#regions
    """

    _result_item_class: Type[MPARegionItem]
    _data: List[MPARegionItem]

    def __init__(self, data: List[MPARegionItem]) -> None:
        """Initializes a new `MPARegionResult`.

        Args:
            data (List[MPARegionItem]):
                A list of `MPARegionItem` objects representing the MPA regions.
        """
        super().__init__(data=data)


class RFMORegionItem(ResultItem):
    """Regional Fisheries Management Organization (RFMO) region item.

    Attributes:
        id (Optional[str]):
            Region ID.

        label (Optional[str]):
            Region label.

        rfb (Optional[str]):
            Region RFB.

        dataset (str):
            Dataset name or ID.
    """

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None)
    rfb: Optional[str] = Field(None, title="RFB", validation_alias="RFB")
    dataset: Optional[str] = Field("public-rfmo")


class RFMORegionResult(Result[RFMORegionItem]):
    """Result for Regional Fisheries Management Organization (RFMO) regions API endpoint.

    This model represents the result returned by the RFMO regions API endpoint.
    See the API documentation for more details:
    https://globalfishingwatch.org/our-apis/documentation#regions
    """

    _result_item_class: Type[RFMORegionItem]
    _data: List[RFMORegionItem]

    def __init__(self, data: List[RFMORegionItem]) -> None:
        """Initializes a new `RFMORegionResult`.

        Args:
            data (List[RFMORegionItem]):
                A list of `RFMORegionItem` objects representing the RFMO regions.
        """
        super().__init__(data=data)
