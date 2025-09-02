"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API Endpoints.

This module defines the endpoints used for interacting with the 4Wings Report API.
It includes the `FourWingsReportEndPoint` class, which handles the construction
and execution of API requests to generate reports on AIS apparent fishing activity,
AIS vessel presence and SAR vessel detections.

For detailed information about the 4Wings Report API, refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#create-a-report-of-a-specified-region

See: https://globalfishingwatch.org/our-apis/documentation#report-url-parameters-for-both-post-and-get-requests

See: https://globalfishingwatch.org/our-apis/documentation#report-body-only-for-post-request

See: https://globalfishingwatch.org/our-apis/documentation#supported-datasets

See: https://globalfishingwatch.org/our-apis/documentation#api-dataset

For detailed information about the 4Wings data caveats, refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#apparent-fishing-effort

See: https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections-data-caveats

See: https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence-caveats
"""
