# 4Wings API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/4wings-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access the 4Wings API, which is designed for generating reports and statistics on activities within specified regions. This API is particularly useful for creating data visualizations related to fishing effort and other vessel activities. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/4wings-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Data Caveats](https://globalfishingwatch.org/our-apis/documentation#data-caveat) and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Prerequisites

- You have installed the `gfw-api-python-client`. Refer to the [Getting Started](../getting-started) guide for installation instructions.

## Getting Started

To interact with the 4Wings endpoints, you first need to instantiate the `gfw.Client` and then access the `fourwings` resource:

```python
import os

import gfwapiclient as gfw


access_token = os.environ.get(
    "GFW_API_ACCESS_TOKEN",
    "<OR_PASTE_YOUR_GFW_API_ACCESS_TOKEN_HERE>",
)

gfw_client = gfw.Client(
    access_token=access_token,
)
```

The `gfw_client.fourwings` object provides methods to generate reports, retrieve the last generated report, and get global fishing effort statistics. These methods return a `result` object, which offers convenient ways to access the data as Pydantic models using `.data()` or as pandas DataFrames using `.df()`.

## Creating a Fishing Effort Report (`create_fishing_effort_report`)

Generates **AIS (Automatic Identification System) apparent fishing effort** reports to visualize fishing activity. [Please check the data caveats here](https://globalfishingwatch.org/our-apis/documentation#apparent-fishing-effort).

```python
fishing_effort_report_result = await gfw_client.fourwings.create_fishing_effort_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="GEARTYPE",
    start_date="2022-01-01",
    end_date="2022-05-01",
    region={
        "dataset": "public-eez-areas",
        "id": "5690",
    },
)
```

### Access the report data as Pydantic models

```python
fishing_effort_report_data = fishing_effort_report_result.data()

fishing_effort_report_item = fishing_effort_report_data[-1]

print((
    fishing_effort_report_item.date,
    fishing_effort_report_item.gear_type,
    fishing_effort_report_item.hours,
    fishing_effort_report_item.vessel_ids,
    fishing_effort_report_item.lat,
    fishing_effort_report_item.lon,
))
```

**Output:**

```
('2022-04', 'fishing', 2.705, 1, 52.0, 155.2)
```

### Access the report data as a DataFrame

```python
fishing_effort_report_df = fishing_effort_report_result.df()

print(fishing_effort_report_df.info())
print(fishing_effort_report_df[["date", "gear_type", "hours", "vessel_ids", "lat", "lon"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 41916 entries, 0 to 41915
Data columns (total 20 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   date                     41916 non-null  object
 1   detections               0 non-null      object
 2   flag                     0 non-null      object
 3   gear_type                41916 non-null  object
 4   hours                    41916 non-null  float64
 5   vessel_ids               41916 non-null  int64
 6   vessel_id                0 non-null      object
 7   vessel_type              0 non-null      object
 8   entry_timestamp          0 non-null      object
 9   exit_timestamp           0 non-null      object
 10  first_transmission_date  0 non-null      object
 11  last_transmission_date   0 non-null      object
 12  imo                      0 non-null      object
 13  mmsi                     0 non-null      object
 14  call_sign                0 non-null      object
 15  dataset                  0 non-null      object
 16  report_dataset           41916 non-null  object
 17  ship_name                0 non-null      object
 18  lat                      41916 non-null  float64
 19  lon                      41916 non-null  float64
dtypes: float64(3), int64(1), object(16)
memory usage: 6.4+ MB
```

## Creating an AIS Presence Report (`create_ais_presence_report`)

Generates **AIS (Automatic Identification System) vessel presence** reports to visualize movement patterns of any vessel type. [Please check the data caveats here](https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence-caveats).

> **Disclaimer:** AIS vessel presence is one of the largest datasets available. To prevent timeouts and ensure optimal performance, keep requests manageable: prefer simple, small regions and shorter time ranges (e.g., a few days).

```python
ais_presence_report_result = await gfw_client.fourwings.create_ais_presence_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="GEARTYPE",
    start_date="2022-01-01",
    end_date="2022-05-01",
    region={
        "dataset": "public-eez-areas",
        "id": "5690",
    },
)
```

### Access the report data as Pydantic models

```python
ais_presence_report_data = ais_presence_report_result.data()

ais_presence_report_item = ais_presence_report_data[-1]

print((
    ais_presence_report_item.date,
    ais_presence_report_item.hours,
    ais_presence_report_item.vessel_ids,
    ais_presence_report_item.lat,
    ais_presence_report_item.lon,
))
```

**Output:**

```
('2022-04', 9.0, 8, 50.4, 160.7)
```

### Access the report data as a DataFrame

```python
ais_presence_report_df = ais_presence_report_result.df()

print(ais_presence_report_df.info())
print(ais_presence_report_df[["date", "hours", "vessel_ids", "lat", "lon"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 144227 entries, 0 to 144226
Data columns (total 20 columns):
 #   Column                   Non-Null Count   Dtype
---  ------                   --------------   -----
 0   date                     144227 non-null  object
 1   detections               0 non-null       object
 2   flag                     0 non-null       object
 3   gear_type                144227 non-null  object
 4   hours                    144227 non-null  float64
 5   vessel_ids               144227 non-null  int64
 6   vessel_id                0 non-null       object
 7   vessel_type              0 non-null       object
 8   entry_timestamp          0 non-null       object
 9   exit_timestamp           0 non-null       object
 10  first_transmission_date  0 non-null       object
 11  last_transmission_date   0 non-null       object
 12  imo                      0 non-null       object
 13  mmsi                     0 non-null       object
 14  call_sign                0 non-null       object
 15  dataset                  0 non-null       object
 16  report_dataset           144227 non-null  object
 17  ship_name                0 non-null       object
 18  lat                      144227 non-null  float64
 19  lon                      144227 non-null  float64
dtypes: float64(3), int64(1), object(16)
memory usage: 22.0+ MB
```

## Creating a SAR Presence Report (`create_sar_presence_report`)

Generates **SAR (Synthetic-Aperture Radar) vessel detections** reports to identify vessels detected via radar, including non-broadcasting (possible `"dark"`) vessels. [Please check the data caveats here](https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections-data-caveats).

```python
sar_presence_report_result = await gfw_client.fourwings.create_sar_presence_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="GEARTYPE",
    start_date="2022-01-01",
    end_date="2022-05-01",
    region={
        "dataset": "public-eez-areas",
        "id": "5690",
    },
)
```

### Access the report data as Pydantic models

```python
sar_presence_report_data = sar_presence_report_result.data()

sar_presence_report_item = sar_presence_report_data[-1]

print((
    sar_presence_report_item.date,
    sar_presence_report_item.detections,
    sar_presence_report_item.vessel_ids,
    sar_presence_report_item.lat,
    sar_presence_report_item.lon,
))
```

**Output:**

```
('2022-04', 1, 1, 46.6, 142.6)
```

### Access the report data as a DataFrame

```python
sar_presence_report_df = sar_presence_report_result.df()

print(sar_presence_report_df.info())
print(sar_presence_report_df[["date", "detections", "vessel_ids", "lat", "lon"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3300 entries, 0 to 3299
Data columns (total 20 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   date                     3300 non-null   object
 1   detections               3300 non-null   int64
 2   flag                     0 non-null      object
 3   gear_type                3300 non-null   object
 4   hours                    0 non-null      object
 5   vessel_ids               3300 non-null   int64
 6   vessel_id                0 non-null      object
 7   vessel_type              0 non-null      object
 8   entry_timestamp          0 non-null      object
 9   exit_timestamp           0 non-null      object
 10  first_transmission_date  0 non-null      object
 11  last_transmission_date   0 non-null      object
 12  imo                      0 non-null      object
 13  mmsi                     0 non-null      object
 14  call_sign                0 non-null      object
 15  dataset                  0 non-null      object
 16  report_dataset           3300 non-null   object
 17  ship_name                0 non-null      object
 18  lat                      3300 non-null   float64
 19  lon                      3300 non-null   float64
dtypes: float64(2), int64(2), object(16)
memory usage: 515.8+ KB
```

## Creating a Report (`create_report`)

Generates a report for any [supported datasets](https://globalfishingwatch.org/our-apis/documentation#supported-datasets), using fully customizable parameters. [Please check the data caveats here](https://globalfishingwatch.org/our-apis/documentation#data-caveat).

```python
report_result = await gfw_client.fourwings.create_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="GEARTYPE",
    datasets=["public-global-fishing-effort:latest"],
    start_date="2022-01-01",
    end_date="2022-05-01",
    region={
        "dataset": "public-eez-areas",
        "id": "5690",
    },
)
```

### Access the report data as Pydantic models

```python
report_data = report_result.data()

report_item = report_data[-1]

print((
    report_item.date,
    report_item.gear_type,
    report_item.hours,
    report_item.vessel_ids,
    report_item.lat,
    report_item.lon,
))
print(report_item.model_dump())
```

**Output:**

```
('2022-04', 'fishing', 2.705, 1, 52.0, 155.2)
```

### Access the report data as a DataFrame

```python
report_df = report_result.df()

print(report_df.info())
print(report_df[["date", "hours", "lat", "lon"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 41916 entries, 0 to 41915
Data columns (total 20 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   date                     41916 non-null  object
 1   detections               0 non-null      object
 2   flag                     0 non-null      object
 3   gear_type                41916 non-null  object
 4   hours                    41916 non-null  float64
 5   vessel_ids               41916 non-null  int64
 6   vessel_id                0 non-null      object
 7   vessel_type              0 non-null      object
 8   entry_timestamp          0 non-null      object
 9   exit_timestamp           0 non-null      object
 10  first_transmission_date  0 non-null      object
 11  last_transmission_date   0 non-null      object
 12  imo                      0 non-null      object
 13  mmsi                     0 non-null      object
 14  call_sign                0 non-null      object
 15  dataset                  0 non-null      object
 16  report_dataset           41916 non-null  object
 17  ship_name                0 non-null      object
 18  lat                      41916 non-null  float64
 19  lon                      41916 non-null  float64
dtypes: float64(3), int64(1), object(16)
memory usage: 6.4+ MB
```

## Reference Data

The 4Wings API often requires specifying geographic regions. You can use the [Reference Data API](references-data-api) to retrieve the `dataset` and `id` of various regions (e.g., EEZs, MPAs, RFMOs) that can then be used in the `create_report()` method.

## Next Steps

Explore the [Usage Guides](index) for other API resources to understand how you can combine the reporting and statistical capabilities of the 4Wings API with vessel information, event data, and more. Check out the following resources:

- [Vessels API](vessels-api)
- [Events API](events-api)
- [Insights API](insights-api)
- [Datasets API](datasets-api)
- [Reference Data API](references-data-api)
