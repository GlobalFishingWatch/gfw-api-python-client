"""Global Fishing Watch (GFW) API Python Client - Bulk Download API Resource.

This module provides the `BulkDownloadResource` class, which allows to interact with
the Bulk Download API to:

- Create bulk reports based on specific filters and spatial parameters.
- Monitor previously created bulk report generation status.
- Get signed URL to download previously created bulk report data, metadata and
region geometry (in GeoJSON format) files.
- Query previously created bulk report data records in JSON format.

For detailed information about the Bulk Download API, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download

For more details on the Bulk Download data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#sar-fixed-infrastructure-data-caveats
"""

from gfwapiclient.resources.bulk_downloads.resources import BulkDownloadResource


__all__ = ["BulkDownloadResource"]
