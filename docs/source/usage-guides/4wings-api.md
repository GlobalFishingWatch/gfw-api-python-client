# 4Wings API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/4wings-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access the [4Wings API](https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api), which is designed for generating reports and statistics on activities within specified regions. This API is particularly useful for creating data visualizations related to fishing effort and other vessel activities. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/4wings-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Datasets](https://globalfishingwatch.org/our-apis/documentation#api-dataset), [AIS Apparent Fishing Effort Data Caveats](https://globalfishingwatch.org/our-apis/documentation#apparent-fishing-effort), [AIS Vessel Presence Data Caveats](https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence-caveats), [SAR Vessel Detections Data Caveats](https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections-data-caveats), and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Prerequisites

- Before using the `gfw-api-python-client`, ensure it is installed (see the [Getting Started](../getting-started) guide) and that you have obtained an API access token from the [Global Fishing Watch API portal](https://globalfishingwatch.org/our-apis/tokens).

## Getting Started

To interact with the 4Wings endpoints, you first need to instantiate the `gfw.Client` and then access the `fourwings` resource:

```python
import os

import geopandas as gpd

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

> **Tip:** Use [IPython](https://ipython.readthedocs.io/en/stable/) or Python 3.11+ with `python -m asyncio` to run `gfw-api-python-client` code interactively, as these environments support executing `async` / `await` expressions directly in the console.

## Creating a Fishing Effort Report (`create_fishing_effort_report`)

Generates **AIS (Automatic Identification System) apparent fishing effort** reports to visualize fishing activity. Please [learn more about apparent fishing effort here](https://globalfishingwatch.org/our-apis/documentation#ais-apparent-fishing-effort) and [check its data caveats here](https://globalfishingwatch.org/our-apis/documentation#apparent-fishing-effort).

**Note:** See how to use the [Reference Data API - Usage Guides](https://globalfishingwatch.github.io/gfw-api-python-client/usage-guides/references-data-api.html) to obtain and filter predefined [**Regions of Interest (ROIs)**](https://globalfishingwatch.org/our-apis/documentation#regions), such as Exclusive Economic Zones (**EEZs**), Marine Protected Areas (**MPAs**), and Regional Fisheries Management Organizations (**RFMOs**).

```python
eez_rois_result = await gfw_client.references.get_eez_regions(iso3="RUS")
rus_eez_roi = eez_rois_result.data()[0]

print((rus_eez_roi.id, rus_eez_roi.dataset, rus_eez_roi.label, rus_eez_roi.iso3))
```

**Output:**

```
('5690', 'public-eez-areas', 'Russian Exclusive Economic Zone', 'RUS')
```

```python
fishing_effort_report_result = await gfw_client.fourwings.create_fishing_effort_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="FLAG",
    start_date="2022-01-01",
    end_date="2022-05-01",
    region=rus_eez_roi,
)
```

### Access the report data as Pydantic models

```python
fishing_effort_report_data = fishing_effort_report_result.data()

fishing_effort_report_item = fishing_effort_report_data[-1]

print((
    fishing_effort_report_item.date,
    fishing_effort_report_item.flag,
    fishing_effort_report_item.hours,
    fishing_effort_report_item.vessel_ids,
    fishing_effort_report_item.lat,
    fishing_effort_report_item.lon,
))
```

**Output:**

```
('2022-03', 'RUS', 7.109166666666667, 3, 75.8, 44.0)
```

### Access the report data as a DataFrame

```python
fishing_effort_report_df = fishing_effort_report_result.df()

print(fishing_effort_report_df.info())
print(fishing_effort_report_df[["date", "flag", "hours", "vessel_ids", "lat", "lon"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32271 entries, 0 to 32270
Data columns (total 20 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   date                     32271 non-null  object
 1   detections               0 non-null      object
 2   flag                     32271 non-null  object
 3   gear_type                0 non-null      object
 4   hours                    32271 non-null  float64
 5   vessel_ids               32271 non-null  int64
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
 16  report_dataset           32271 non-null  object
 17  ship_name                0 non-null      object
 18  lat                      32271 non-null  float64
 19  lon                      32271 non-null  float64
dtypes: float64(3), int64(1), object(16)
memory usage: 4.9+ MB
```

## Creating an AIS Presence Report (`create_ais_presence_report`)

Generates **AIS (Automatic Identification System) vessel presence** reports to visualize movement patterns of any vessel type. Please [learn more about AIS vessel presence here](https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence) and [check its data caveats here](https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence-caveats).

> **Disclaimer:** AIS vessel presence is one of the largest datasets available. To prevent timeouts and ensure optimal performance, keep requests manageable: prefer simple, small regions and shorter time ranges (e.g., a few days).

**Note:** See how to use the [Reference Data API - Usage Guides](https://globalfishingwatch.github.io/gfw-api-python-client/usage-guides/references-data-api.html) to obtain and filter predefined [**Regions of Interest (ROIs)**](https://globalfishingwatch.org/our-apis/documentation#regions), such as Exclusive Economic Zones (**EEZs**), Marine Protected Areas (**MPAs**), and Regional Fisheries Management Organizations (**RFMOs**).

```python
eez_rois_result = await gfw_client.references.get_eez_regions(iso3="RUS")
rus_eez_roi = eez_rois_result.data()[0]

print((rus_eez_roi.id, rus_eez_roi.dataset, rus_eez_roi.label, rus_eez_roi.iso3))
```

**Output:**

```
('5690', 'public-eez-areas', 'Russian Exclusive Economic Zone', 'RUS')
```

```python
ais_presence_report_result = await gfw_client.fourwings.create_ais_presence_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="FLAG",
    start_date="2022-01-01",
    end_date="2022-05-01",
    region=rus_eez_roi,
)
```

### Access the report data as Pydantic models

```python
ais_presence_report_data = ais_presence_report_result.data()

ais_presence_report_item = ais_presence_report_data[-1]

print((
    ais_presence_report_item.date,
    ais_presence_report_item.flag,
    ais_presence_report_item.hours,
    ais_presence_report_item.vessel_ids,
    ais_presence_report_item.lat,
    ais_presence_report_item.lon,
))
```

**Output:**

```
('2022-03', 'RUS', 1.0, 1, 52.1, 153.2)
```

### Access the report data as a DataFrame

```python
ais_presence_report_df = ais_presence_report_result.df()

print(ais_presence_report_df.info())
print(ais_presence_report_df[["date", "flag", "hours", "vessel_ids", "lat", "lon"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 274333 entries, 0 to 274332
Data columns (total 20 columns):
 #   Column                   Non-Null Count   Dtype
---  ------                   --------------   -----
 0   date                     274333 non-null  object
 1   detections               0 non-null       object
 2   flag                     274333 non-null  object
 3   gear_type                0 non-null       object
 4   hours                    274333 non-null  float64
 5   vessel_ids               274333 non-null  int64
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
 16  report_dataset           274333 non-null  object
 17  ship_name                0 non-null       object
 18  lat                      274333 non-null  float64
 19  lon                      274333 non-null  float64
dtypes: float64(3), int64(1), object(16)
memory usage: 41.9+ MB
```

## Creating a SAR Vessel Detections Report (`create_sar_presence_report`)

Generates **SAR (Synthetic-Aperture Radar) vessel detections** reports to identify vessels detected via radar, including non-broadcasting (possible `"dark"`) vessels. Please [learn more about SAR vessel detections here](https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections) and [check its data caveats here](https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections-data-caveats).

> **Important:** **AIS vessel presence** shows where vessels **reported their positions** via the **Automatic Identification System (AIS)**. **SAR vessel detection** shows where **Synthetic Aperture Radar (SAR) satellites detected** vessels on the ocean surface, even if they **weren't transmitting AIS**.

**Note:** See how to use the [Reference Data API - Usage Guides](https://globalfishingwatch.github.io/gfw-api-python-client/usage-guides/references-data-api.html) to obtain and filter predefined [**Regions of Interest (ROIs)**](https://globalfishingwatch.org/our-apis/documentation#regions), such as Exclusive Economic Zones (**EEZs**), Marine Protected Areas (**MPAs**), and Regional Fisheries Management Organizations (**RFMOs**).

```python
eez_rois_result = await gfw_client.references.get_eez_regions(iso3="RUS")
rus_eez_roi = eez_rois_result.data()[0]

print((rus_eez_roi.id, rus_eez_roi.dataset, rus_eez_roi.label, rus_eez_roi.iso3))
```

**Output:**

```
('5690', 'public-eez-areas', 'Russian Exclusive Economic Zone', 'RUS')
```

```python
sar_presence_report_result = await gfw_client.fourwings.create_sar_presence_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="GEARTYPE",
    start_date="2022-01-01",
    end_date="2022-05-01",
    region=rus_eez_roi,
)
```

### Access the report data as Pydantic models

```python
sar_presence_report_data = sar_presence_report_result.data()

sar_presence_report_item = sar_presence_report_data[-1]

print((
    sar_presence_report_item.date,
    sar_presence_report_item.flag,
    sar_presence_report_item.detections,
    sar_presence_report_item.vessel_ids,
    sar_presence_report_item.lat,
    sar_presence_report_item.lon,
))
```

**Output:**

```
('2022-04', '', 1, 1, 46.6, 142.6)
```

### Access the report data as a DataFrame

```python
sar_presence_report_df = sar_presence_report_result.df()

print(sar_presence_report_df.info())
print(sar_presence_report_df[["date", "flag", "detections", "vessel_ids", "lat", "lon"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3995 entries, 0 to 3994
Data columns (total 20 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   date                     3995 non-null   object
 1   detections               3995 non-null   int64
 2   flag                     3995 non-null   object
 3   gear_type                0 non-null      object
 4   hours                    0 non-null      object
 5   vessel_ids               3995 non-null   int64
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
 16  report_dataset           3995 non-null   object
 17  ship_name                0 non-null      object
 18  lat                      3995 non-null   float64
 19  lon                      3995 non-null   float64
dtypes: float64(2), int64(2), object(16)
memory usage: 624.3+ KB
```

## Creating a Generic Report from Predefined Region (`create_report`)

Generates a report for any [supported datasets](https://globalfishingwatch.org/our-apis/documentation#supported-datasets), using fully customizable parameters. [Please check the data caveats here](https://globalfishingwatch.org/our-apis/documentation#data-caveat).

> **Note:** AIS vessel presence (i.e., `"public-global-sar-presence:latest"` dataset) does **not** support `"GEARTYPE"` or `"FLAGANDGEARTYPE"` as `group_by` criteria.

**Note:** See how to use the [Reference Data API - Usage Guides](https://globalfishingwatch.github.io/gfw-api-python-client/usage-guides/references-data-api.html) to obtain and filter predefined [**Regions of Interest (ROIs)**](https://globalfishingwatch.org/our-apis/documentation#regions), such as Exclusive Economic Zones (**EEZs**), Marine Protected Areas (**MPAs**), and Regional Fisheries Management Organizations (**RFMOs**).

```python
eez_rois_result = await gfw_client.references.get_eez_regions(iso3="RUS")
rus_eez_roi = eez_rois_result.data()[0]

print((rus_eez_roi.id, rus_eez_roi.dataset, rus_eez_roi.label, rus_eez_roi.iso3))
```

**Output:**

```
('5690', 'public-eez-areas', 'Russian Exclusive Economic Zone', 'RUS')
```

```python
predefined_report_result = await gfw_client.fourwings.create_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="FLAG",
    datasets=[
        "public-global-fishing-effort:latest",
        "public-global-sar-presence:latest",
        "public-global-presence:latest",
    ],
    start_date="2022-01-01",
    end_date="2022-05-01",
    region=rus_eez_roi,
)
```

### Access the report data as Pydantic models

```python
predefined_report_data = predefined_report_result.data()

predefined_report_item = predefined_report_data[-1]

print((
    predefined_report_item.date,
    predefined_report_item.flag,
    predefined_report_item.hours,
    predefined_report_item.vessel_ids,
    predefined_report_item.lat,
    predefined_report_item.lon,
))
```

**Output:**

```
('2022-03', 'RUS', 1.0, 1, 52.1, 153.2)
```

### Access the report data as a DataFrame

```python
predefined_report_df = predefined_report_result.df()

print(predefined_report_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 310599 entries, 0 to 310598
Data columns (total 20 columns):
 #   Column                   Non-Null Count   Dtype
---  ------                   --------------   -----
 0   date                     310599 non-null  str
 1   detections               3995 non-null    float64
 2   flag                     310599 non-null  str
 3   gear_type                0 non-null       object
 4   hours                    306604 non-null  float64
 5   vessel_ids               310599 non-null  int64
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
 16  report_dataset           310599 non-null  str
 17  ship_name                0 non-null       object
 18  lat                      310599 non-null  float64
 19  lon                      310599 non-null  float64
dtypes: float64(4), int64(1), object(12), str(3)
memory usage: 47.4+ MB
```

## Creating a Generic Report from Custom Region (`create_report`)

Generates a report for any [supported datasets](https://globalfishingwatch.org/our-apis/documentation#supported-datasets), using fully customizable parameters. [Please check the data caveats here](https://globalfishingwatch.org/our-apis/documentation#data-caveat).

> **Note:** AIS vessel presence (i.e., `"public-global-sar-presence:latest"` dataset) does **not** support `"GEARTYPE"` or `"FLAGANDGEARTYPE"` as `group_by` criteria.

> **Note:** Custom region can either a path to a spatial file (e.g., GeoJSON, Shapefile, etc.), GeoJSON-like object (e.g., JSON string, dictionary, `geopandas.GeoDataFrame`, `shapely`, an object implementing `__geo_interface__` etc.) or `GeoJson` model instance. Spatial files are loaded using [geopandas.read_file](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html) and supported formats depend on a properly configured [geopandas/GDAL installation](https://geopandas.org/en/stable/getting_started/install.html#installing-with-pip).

```python
filename = "https://raw.githubusercontent.com/GlobalFishingWatch/gfw-api-python-client/refs/heads/develop/tests/fixtures/fourwings/geojson/geojson.shp"

custom_roi_gdf = gpd.read_file(filename)
```

```python
custom_report_result = await gfw_client.fourwings.create_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="FLAG",
    datasets=[
        "public-global-fishing-effort:latest",
        "public-global-sar-presence:latest",
        "public-global-presence:latest",
    ],
    start_date="2022-01-01",
    end_date="2022-05-01",
    geojson=custom_roi_gdf,
)
```

### Access the report data as Pydantic models

```python
custom_report_data = custom_report_result.data()

custom_report_item = custom_report_data[-1]

print((
    custom_report_item.date,
    custom_report_item.flag,
    custom_report_item.hours,
    custom_report_item.vessel_ids,
    custom_report_item.lat,
    custom_report_item.lon,
))
```

**Output:**

```
('2022-01', 'NOR', 1.0, 1, -25.9, -76.3)
```

### Access the report data as a DataFrame

```python
custom_report_df = custom_report_result.df()

print(custom_report_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 6740 entries, 0 to 6739
Data columns (total 20 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   date                     6740 non-null   str
 1   detections               0 non-null      object
 2   flag                     6740 non-null   str
 3   gear_type                0 non-null      object
 4   hours                    6740 non-null   float64
 5   vessel_ids               6740 non-null   int64
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
 16  report_dataset           6740 non-null   str
 17  ship_name                0 non-null      object
 18  lat                      6740 non-null   float64
 19  lon                      6740 non-null   float64
dtypes: float64(3), int64(1), object(13), str(3)
memory usage: 1.0+ MB
```

## Reference Data

The 4Wings API often requires specifying geographic regions. You can use the [Reference Data API](references-data-api) to retrieve the `dataset` and `id` of various regions (e.g., EEZs, MPAs, RFMOs) that can then be used in the `create_report()` method.

## Next Steps

Explore the [Usage Guides](index) and [Workflow Guides](../workflow-guides/index) for other API resources to understand how you can combine the reporting and statistical capabilities of the 4Wings API with vessel information, event data, and more. Check out the following resources:

- [Vessels API](vessels-api)
- [Events API](events-api)
- [Insights API](insights-api)
- [Datasets API](datasets-api)
- [Bulk Download API](bulk-downloads-api)
- [Reference Data API](references-data-api)
