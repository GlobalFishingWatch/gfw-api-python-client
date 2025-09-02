"""Global Fishing Watch (GFW) API Python Client - Datasets API Resource."""

from typing import Any, Dict, Optional, Union

import pydantic

from geojson_pydantic.geometries import Geometry

from gfwapiclient.exceptions.validation import RequestParamsValidationError
from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.datasets.endpoints import SARFixedInfrastructureEndPoint
from gfwapiclient.resources.datasets.models.request import (
    SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    SARFixedInfrastructureParams,
)
from gfwapiclient.resources.datasets.models.response import SARFixedInfrastructureResult


__all__ = ["DatasetResource"]


class DatasetResource(BaseResource):
    """Datasets data API resource.

    This resource provides methods to interact with the datasets data API endpoints.
    """

    async def get_sar_fixed_infrastructure(
        self,
        *,
        z: Optional[int] = None,
        x: Optional[int] = None,
        y: Optional[int] = None,
        geometry: Optional[Union[Geometry, Dict[str, Any]]] = None,
        **kwargs: Dict[str, Any],
    ) -> SARFixedInfrastructureResult:
        """Get SAR (Synthetic-aperture radar) fixed infrastructure data.

        This method fetches SAR fixed infrastructure data, potentially filtered
        by a geographic geometry. If `z`, `x`, and `y` are not provided but
        `geometry` is, the tile containing the geometry's bounding box will be
        used.

        Args:
            z: (Optional[int], default=None):
                Zoom level (from 0 to 9 for SAR fixed infrastructure dataset). Defaults to `None`.
                Example: `1`.

            x: (Optional[int], default=None):
                X index (lat) of the tile. Defaults to `None`.
                Example: `0`.

            y: (Optional[int], default=None):
                Y index (lon) of the tile. Defaults to `None`.
                Example: `1`.

            geometry (Optional[Union[Geometry, Dict[str, Any]]], default=None):
                Geometry used to filter SAR fixed infrastructure. Defaults to `None`.
                Example: `{"type": "Polygon", "coordinates": [...]}`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            SARFixedInfrastructureResult:
                The result containing the SAR fixed infrastructure details.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.
        """
        request_params: SARFixedInfrastructureParams = (
            self._prepare_get_sar_fixed_infrastructure_request_params(
                z=z,
                x=x,
                y=y,
                geometry=geometry,
            )
        )

        endpoint: SARFixedInfrastructureEndPoint = SARFixedInfrastructureEndPoint(
            z=request_params.z,
            x=request_params.x,
            y=request_params.y,
            http_client=self._http_client,
        )

        result: SARFixedInfrastructureResult = await endpoint.request(**kwargs)
        return result

    def _prepare_get_sar_fixed_infrastructure_request_params(
        self,
        *,
        z: Optional[int] = None,
        x: Optional[int] = None,
        y: Optional[int] = None,
        geometry: Optional[Union[Geometry, Dict[str, Any]]] = None,
    ) -> SARFixedInfrastructureParams:
        """Prepares and returns the request parameters for the get sar fixed infrastructure endpoint."""
        try:
            _request_params: Dict[str, Any] = {
                "z": z,
                "x": x,
                "y": y,
                "geometry": geometry,
            }
            request_params: SARFixedInfrastructureParams = (
                SARFixedInfrastructureParams.from_tile_or_geometry(**_request_params)
            )
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params
