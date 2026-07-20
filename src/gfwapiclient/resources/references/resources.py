"""Global Fishing Watch (GFW) API Python Client - References Data API Resource."""

import re

from typing import Any, Callable, Dict, List, Optional, Pattern, Union, cast

from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.references.regions.endpoints import (
    EEZRegionEndPoint,
    MPARegionEndPoint,
    RFMORegionEndPoint,
)
from gfwapiclient.resources.references.regions.models.response import (
    EEZRegionItem,
    EEZRegionResult,
    MPARegionItem,
    MPARegionResult,
    RFMORegionItem,
    RFMORegionResult,
)


__all__ = ["ReferenceResource"]


class ReferenceResource(BaseResource):
    """References data API resource.

    This resource provides methods to interact with the Reference Data API,
    specifically to:

    - Retrieves a list of Exclusive Economic Zone (EEZ) regions.
    - Retrieves a list of Marine Protected Area (MPA) regions.
    - Retrieves a list of Regional Fisheries Management Organization (RFMO) regions.

    For detailed information about the Reference Data API, please refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#reference-data

    See: https://globalfishingwatch.org/our-apis/documentation#regions

    For more details on the Reference Data API data caveats, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definition

    See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition

    See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

    See: https://globalfishingwatch.org/our-apis/documentation#how-does-gfw-calculate-that-an-event-has-a-publicly-listed-authorization

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-rfmo-iuu-vessel-list

    See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definitions

    See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition-2
    """

    async def get_eez_regions(
        self,
        *,
        id: Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]] = None,
        label: Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]] = None,
        iso3: Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]] = None,
        iso_sov_1: Optional[
            Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ] = None,
        iso_sov_2: Optional[
            Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ] = None,
        iso_sov_3: Optional[
            Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ] = None,
        territory_1: Optional[
            Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ] = None,
        predicate: Optional[Callable[[EEZRegionItem], bool]] = None,
        **kwargs: Any,
    ) -> EEZRegionResult:
        """Get available Exclusive Economic Zone (EEZ) regions data.

        Retrieves a list of Exclusive Economic Zone (EEZ) regions.

        For detailed information about the EEZ regions API endpoint, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#regions

        For more details on the EEZ regions data caveats, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definition

        See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

        See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definitions

        Args:
            id (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the unique identifier (id). Defaults to `None`.
                Example: `id="8371"`.

            label (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the label (name). Defaults to `None`.
                Example: `label="Senegalese"`.

            iso3 (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the ISO 3166-1 alpha-3 country code.
                Defaults to `None`.
                Example: `iso3="SEN"`.

            iso_sov_1 (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the primary sovereignty ISO code.
                Defaults to `None`.

            iso_sov_2 (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the secondary sovereignty ISO code.
                Defaults to `None`.

            iso_sov_3 (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the tertiary sovereignty ISO code.
                Defaults to `None`.

            territory_1 (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the territory name. Defaults to `None`.
                Example: `territory_1="Senegal"`.

            predicate (Optional[Callable[[EEZRegionItem], bool]], default=None):
                An optional callable that accepts a `EEZRegionItem` instance and
                returns `True` if it should be included.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments to pass to the EEZ region endpoint's request.

        Returns:
            EEZRegionResult:
                The result containing the list of EEZ regions data items.

        Raises:
            GFWAPIClientError:
                If the API request fails.
        """
        endpoint: EEZRegionEndPoint = EEZRegionEndPoint(http_client=self._http_client)
        result: EEZRegionResult = await endpoint.request(**kwargs)

        # Filter result by field filters
        item_filters: Dict[
            str, Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ] = {
            k: v
            for k, v in {
                "id": id,
                "iso3": iso3,
                "label": label,
                "iso_sov_1": iso_sov_1,
                "iso_sov_2": iso_sov_2,
                "iso_sov_3": iso_sov_3,
                "territory_1": territory_1,
            }.items()
            if v
        }
        field_filters_predicate: Callable[[EEZRegionItem], bool] = (
            self._build_field_filters_predicate(item_filters=item_filters)
        )
        result = cast(EEZRegionResult, result.filter(predicate=field_filters_predicate))

        # Filter result by custom predicate
        if predicate and callable(predicate):
            result = cast(EEZRegionResult, result.filter(predicate=predicate))

        return result

    async def get_mpa_regions(
        self,
        *,
        id: Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]] = None,
        label: Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]] = None,
        predicate: Optional[Callable[[MPARegionItem], bool]] = None,
        **kwargs: Any,
    ) -> MPARegionResult:
        """Get available Marine Protected Area (MPA) regions data.

        Retrieves a list of Marine Protected Area (MPA) regions.

        For detailed information about the MPA regions API endpoint, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#regions

        For more details on the MPA regions data caveats, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition

        See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

        See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition-2

        Args:
            id (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the unique identifier (id). Defaults to `None`.
                Example: `id="555745302"`.

            label (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the label (name). Defaults to `None`.
                Example: `label="Dorsal de Nasca"`.

            predicate (Optional[Callable[[MPARegionItem], bool]], default=None):
                An optional callable that accepts a `MPARegionItem` instance and
                returns `True` if it should be included.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments to pass to the MPA region endpoint's request.

        Returns:
            MPARegionResult:
                The result containing the list of MPA regions data items.

        Raises:
            GFWAPIClientError:
                If the API request fails.
        """
        endpoint: MPARegionEndPoint = MPARegionEndPoint(http_client=self._http_client)
        result: MPARegionResult = await endpoint.request(**kwargs)

        # Filter result by field filters
        item_filters: Dict[
            str, Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ] = {k: v for k, v in {"id": id, "label": label}.items() if v}
        field_filters_predicate: Callable[[MPARegionItem], bool] = (
            self._build_field_filters_predicate(item_filters=item_filters)
        )
        result = cast(MPARegionResult, result.filter(predicate=field_filters_predicate))

        # Filter result by custom predicate
        if predicate and callable(predicate):
            result = cast(MPARegionResult, result.filter(predicate=predicate))

        return result

    async def get_rfmo_regions(
        self,
        *,
        id: Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]] = None,
        label: Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]] = None,
        predicate: Optional[Callable[[RFMORegionItem], bool]] = None,
        **kwargs: Any,
    ) -> RFMORegionResult:
        """Get available Regional Fisheries Management Organization (RFMO) regions data.

        Retrieves a list of Regional Fisheries Management Organization (RFMO) regions.

        For detailed information about the RFMO regions API endpoint, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#regions

        For more details on the RFMO regions data caveats, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

        See: https://globalfishingwatch.org/our-apis/documentation#how-does-gfw-calculate-that-an-event-has-a-publicly-listed-authorization

        See: https://globalfishingwatch.org/our-apis/documentation#insights-api-rfmo-iuu-vessel-list

        Args:
            id (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the unique identifier (id). Defaults to `None`.
                Example: `id="ICCAT"`.

            label (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]], default=None):
                Filter(s) to apply to the label (name). Defaults to `None`.
                Example: `label="ICCAT"`.

            predicate (Optional[Callable[[RFMORegionItem], bool]], default=None):
                An optional callable that accepts a `RFMORegionItem` instance and
                returns `True` if it should be included.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments to pass to the RFMO region endpoint's request.

        Returns:
            RFMORegionResult:
                The result containing the list of RFMO regions data items.

        Raises:
            GFWAPIClientError:
                If the API request fails.
        """
        endpoint: RFMORegionEndPoint = RFMORegionEndPoint(http_client=self._http_client)
        result: RFMORegionResult = await endpoint.request(**kwargs)

        # Filter result by field filters
        item_filters: Dict[
            str, Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ] = {k: v for k, v in {"id": id, "label": label}.items() if v}
        field_filters_predicate: Callable[[RFMORegionItem], bool] = (
            self._build_field_filters_predicate(item_filters=item_filters)
        )
        result = cast(
            RFMORegionResult, result.filter(predicate=field_filters_predicate)
        )

        # Filter result by custom predicate
        if predicate and callable(predicate):
            result = cast(RFMORegionResult, result.filter(predicate=predicate))

        return result

    def _build_field_filters_predicate(
        self,
        *,
        item_filters: Dict[
            str, Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ],
    ) -> Callable[[Union[EEZRegionItem, MPARegionItem, RFMORegionItem]], bool]:
        """Build a predicate that filters region items by field values.

        All provided field filters must match (logical AND).

        Args:
            item_filters (Dict[str, Union[str, Pattern[str], List[str], List[Pattern[str]]]]):
                Mapping of item field names to filter values.

        Returns:
            Callable[[Union[EEZRegionItem, MPARegionItem, RFMORegionItem]], bool]:
                Predicate suitable to filter region `ResultItem` by fields.
        """

        def predicate(
            item: Union[EEZRegionItem, MPARegionItem, RFMORegionItem],
        ) -> bool:
            return all(
                self._match_field_filters(
                    field_value=cast(Optional[str], getattr(item, field_name, None)),
                    field_filters=field_filters,
                )
                for field_name, field_filters in item_filters.items()
            )

        return predicate

    def _match_field_filters(
        self,
        *,
        field_value: Optional[str] = None,
        field_filters: Optional[
            Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ] = None,
    ) -> bool:
        """Check whether a field value matches any of the provided field filters.

        Matching is case-insensitive and regex-based.

        Args:
            field_value (Optional[str]):
                Field value to be matched.

            field_filters (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]]):
                Field filters to match against field value.

        Returns:
            bool:
                `True` if any field filter matches the field value, otherwise `False`.
        """
        if not field_value or not field_filters:
            return False

        _field_filters: List[Pattern[str]] = self._normalize_field_filter(
            field_filter=field_filters
        )

        return any(
            True if field_filter.search(field_value) else False
            for field_filter in _field_filters
        )

    def _normalize_field_filter(
        self,
        *,
        field_filter: Optional[
            Union[str, Pattern[str], List[str], List[Pattern[str]]]
        ] = None,
    ) -> List[Pattern[str]]:
        """Normalize field filter into a list of compiled regex patterns.

        - Strings are stripped and compiled as case-insensitive regex.
        - Regex patterns are preserved.
        - Empty or invalid values are discarded.

        Args:
            field_filter (Optional[Union[str, Pattern[str], List[str], List[Pattern[str]]]]):
                Raw field filter(s).

        Returns:
            List[Pattern[str]]:
                Normalized list of field filter(s).
        """
        if not field_filter:
            return []

        # Normalize field filter to list
        field_filters: List[Union[str, Pattern[str]]] = (
            [*field_filter] if isinstance(field_filter, list) else [field_filter]
        )
        field_filters = [
            v.strip() if isinstance(v, str) else v for v in field_filters if v
        ]
        field_filters = [
            v for v in field_filters if v and isinstance(v, (str, re.Pattern))
        ]

        # Normalize field filter to list of compiled regex patterns
        _field_filters: List[Pattern[str]] = [
            re.compile(v, re.I) if isinstance(v, str) else v for v in field_filters
        ]
        return _field_filters
