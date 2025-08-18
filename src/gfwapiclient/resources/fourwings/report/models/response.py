"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API Response Models."""

import datetime

from typing import Any, List, Optional, Type

from pydantic import Field, field_validator

from gfwapiclient.http.models import Result, ResultItem


__all__ = ["FourWingsReportItem", "FourWingsReportResult"]


class FourWingsReportItem(ResultItem):
    """4Wings report entry.

    Represents a single entry in the 4Wings report result.
    Each entry captures multiple dimensions of vessel activity, identity,
    and detection using Automatic Identification System (AIS) or
    Synthetic Aperture Radar (SAR) data.

    For more details on the 4Wings API supported report response bodies,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#create-a-report-of-a-specified-region

    Attributes:
        date (Optional[str]):
            The date of the report entry (e.g. `"2022-01-13"`).

        detections (Optional[int]):
            The number of vessel detections (e.g. `12`).

        flag (Optional[str]):
            The vessel's country flag (e.g. `"ESP"`).

        gear_type (Optional[str]):
            The vessel's gear type (e.g. `"FISHING"`).

        hours (Optional[float]):
            The number of activity hours (e.g. `26.6`).

        vessel_ids (Optional[int]):
            The number of vessel identifiers (IDs) (e.g. `3`).

        vessel_id (Optional[str]):
            The vessel identifier (ID) (e.g `"e6154b2e7-7762-4889-fb46-976ec72875e1"`).

        vessel_type (Optional[str]):
            The vessel type (e.g `"FISHING"`).

        entry_timestamp (Optional[datetime.datetime]):
            The timestamp when the vessel entered the observation area in ISO-8601
            format (e.g `"2022-01-14T14:00:00Z"`).

        exit_timestamp (Optional[datetime.datetime]):
            The timestamp when the vessel exited the observation area in ISO-8601
            format (e.g `"2022-01-14T16:00:00Z"`).

        first_transmission_date (Optional[datetime.datetime]):
            The vessel's first AIS (Automatic Identification System) transmission
            date in ISO-8601 format (e.g `"2019-07-12T12:08:27Z"`).

        last_transmission_date (Optional[datetime.datetime]):
            The vessel's last AIS (Automatic Identification System) transmission
            date in ISO-8601 format (e.g `"2025-03-01T23:55:50Z"`).

        imo (Optional[str]):
            The vessel's IMO (International Maritime Organization) number (e.g `"8602866"`).

        mmsi (Optional[str]):
            The vessel's MMSI (Maritime Mobile Service Identity) number (e.g `"273453380"`).

        call_sign (Optional[str]):
            The vessel's call sign (e.g `"UBSS9"`).

        dataset (Optional[str]):
            The vessel information dataset (e.g `"public-global-vessel-identity:v3.0"`).

        report_dataset (Optional[str]):
            The dataset used to create the report (e.g `"public-global-fishing-effort:v3.0"`).

        ship_name (Optional[str]):
            The vessel's ship name (e.g `"ALSEY"`).

        lat (Optional[float]):
            The vessel's reported latitude (e.g `49.33`).

        lon (Optional[float]):
            The vessel's reported longitude (e.g `141.15`).
    """

    date: Optional[str] = Field(None, alias="date")
    detections: Optional[int] = Field(None, alias="detections")
    flag: Optional[str] = Field(None, alias="flag")
    gear_type: Optional[str] = Field(None, alias="geartype")
    hours: Optional[float] = Field(None, alias="hours")
    vessel_ids: Optional[int] = Field(None, alias="vesselIDs")
    vessel_id: Optional[str] = Field(None, alias="vesselId")
    vessel_type: Optional[str] = Field(None, alias="vesselType")
    entry_timestamp: Optional[datetime.datetime] = Field(None, alias="entryTimestamp")
    exit_timestamp: Optional[datetime.datetime] = Field(None, alias="exitTimestamp")
    first_transmission_date: Optional[datetime.datetime] = Field(
        None, alias="firstTransmissionDate"
    )
    last_transmission_date: Optional[datetime.datetime] = Field(
        None, alias="lastTransmissionDate"
    )
    imo: Optional[str] = Field(None, alias="imo")
    mmsi: Optional[str] = Field(None, alias="mmsi")
    call_sign: Optional[str] = Field(None, alias="callsign")
    dataset: Optional[str] = Field(None, alias="dataset")
    report_dataset: Optional[str] = Field(None, alias="report_dataset")
    ship_name: Optional[str] = Field(None, alias="shipName")
    lat: Optional[float] = Field(None, alias="lat")
    lon: Optional[float] = Field(None, alias="lon")

    @field_validator(
        "entry_timestamp",
        "exit_timestamp",
        "first_transmission_date",
        "last_transmission_date",
        mode="before",
    )
    @classmethod
    def empty_datetime_str_to_none(cls, value: Any) -> Optional[Any]:
        """Convert any empty datetime string to `None`.

        Args:
            value (Any):
                The value to validate.

        Returns:
            Optional[datetime.datetime]:
                The validated datetime object or `None` if input is empty.
        """
        if isinstance(value, str) and value.strip() == "":
            return None
        return value


class FourWingsReportResult(Result[FourWingsReportItem]):
    """Result for 4Wings Report API endpoint.

    Represents the result of the 4Wings Report API endpoint.

    Attributes:
        _result_item_class (Type[FourWingsReportItem]):
            The model used for individual result items.

        _data (List[FourWingsReportItem]):
            List of report items returned in the response.
    """

    _result_item_class: Type[FourWingsReportItem]
    _data: List[FourWingsReportItem]

    def __init__(self, data: List[FourWingsReportItem]) -> None:
        """Initializes a new `FourWingsReportResult`.

        Args:
            data (List[FourWingsReportItem]):
                The list of report items.
        """
        super().__init__(data=data)
