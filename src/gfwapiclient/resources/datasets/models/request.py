"""Global Fishing Watch (GFW) API Python Client - Datasets API Request Models."""

from typing import Final, Optional, Self, cast

import mercantile

from geojson_pydantic.geometries import Geometry
from pydantic import Field

from gfwapiclient.base.models import BaseModel


SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Get SAR fixed infrastructure request parameters validation failed."
)


class SARFixedInfrastructureParams(BaseModel):
    """Request parameters for retrieving SAR fixed infrastructure.

    This model is used to structure the path parameters required for the
    `/v3/datasets/sar-fixed-infrastructure/mvt/{z}/{x}/{y}.pbf` endpoint.

    Attributes:
        z (int):
            Zoom level for the tiles (from 0 to 9 for the SAR fixed
            infrastructure dataset). Example: 1.

        x (int):
            X index (column) of the tile.

        y (int):
            Y index (row) of the tile.

        geometry (Optional[Geometry]):
            Optional GeoJSON geometry to filter SAR fixed infrastructure.
            If provided and `z`, `x`, `y` are not specified, the tile
            containing the geometry's bounding box will be used to populate
            `z`, `x`, and `y`.
            Example: `{"type": "Polygon", "coordinates": [...]}`.
    """

    z: int = Field(...)
    x: int = Field(...)
    y: int = Field(...)
    geometry: Optional[Geometry] = Field(None)

    @classmethod
    def from_tile_or_geometry(
        cls,
        *,
        z: Optional[int] = None,
        x: Optional[int] = None,
        y: Optional[int] = None,
        geometry: Optional[Geometry] = None,
    ) -> Self:
        """Create an instance `SARFixedInfrastructureParams` from either tile coordinates or a GeoJSON geometry.

        If `z`, `x`, or `y` are missing and a `geometry` is provided, this
        calculates the bounding tile that encompasses the geometry
        and populates the missing `z`, `x`, and `y` values.

        Args:
            z (int):
                Zoom level for the tiles (from 0 to 9 for the SAR fixed
                infrastructure dataset). Example: 1.

            x (int):
                X index (column) of the tile.

            y (int):
                Y index (row) of the tile.

            geometry (Optional[Geometry]):
                Optional GeoJSON geometry to filter SAR fixed infrastructure.
                If provided and `z`, `x`, `y` are not specified, the tile
                containing the geometry's bounding box will be used to populate
                `z`, `x`, and `y`.
                Example: `{"type": "Polygon", "coordinates": [...]}`.

        Returns:
            SARFixedInfrastructureParams:
                A fully populated `SARFixedInfrastructureParams` instance.
        """
        if z is None or x is None or y is None:
            if geometry:
                bounds: mercantile.LngLatBbox = mercantile.geojson_bounds(geometry)
                tile: mercantile.Tile = mercantile.bounding_tile(
                    *bounds, truncate=False
                )
                z, x, y = tile.z, tile.x, tile.y
        return cls(z=cast(int, z), x=cast(int, x), y=cast(int, y), geometry=geometry)
