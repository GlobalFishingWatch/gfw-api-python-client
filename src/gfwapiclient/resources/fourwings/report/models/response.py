"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API Response Models."""

import datetime

from typing import Any, List, Optional, Type

from pydantic import Field, field_validator

from gfwapiclient.http.models import Result, ResultItem


__all__ = ["FourWingsReportItem", "FourWingsReportResult"]


class FourWingsReportItem(ResultItem):
    """4Wings report entry.

    Represents a single entry in the 4Wings report result.

    Attributes:
        date (Optional[str]):
            The date of the report entry.

        detections (Optional[int]):
            The number of detections.

        flag (Optional[str]):
            The vessel's flag.

        gear_type (Optional[str]):
            The vessel's gear type.

        hours (Optional[float]):
            The number of hours.

        vessel_ids (Optional[int]):
            The number of vessel IDs.

        vessel_id (Optional[str]):
            The vessel ID.

        vessel_type (Optional[str]):
            The vessel type.

        entry_timestamp (Optional[datetime.datetime]):
            The entry timestamp.

        exit_timestamp (Optional[datetime.datetime]):
            The exit timestamp.

        first_transmission_date (Optional[datetime.datetime]):
            The first transmission date.

        last_transmission_date (Optional[datetime.datetime]):
            The last transmission date.

        imo (Optional[str]):
            The IMO number.

        mmsi (Optional[str]):
            The MMSI number.

        call_sign (Optional[str]):
            The call sign.

        dataset (Optional[str]):
            The dataset.

        report_dataset (Optional[str]):
            The dataset used to create the report.

        ship_name (Optional[str]):
            The ship name.

        lat (Optional[float]):
            The latitude.

        lon (Optional[float]):
            The longitude.
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
                The validated datetime or None.
        """
        if isinstance(value, str) and value.strip() == "":
            return None
        return value


class FourWingsReportResult(Result[FourWingsReportItem]):
    """Result for 4Wings Report API endpoint.

    Represents the result of the 4Wings Report API endpoint.
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
