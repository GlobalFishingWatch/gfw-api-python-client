# Events API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/events-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access information about various activities of a vessel, including fishing activity, encounters, port visits, loitering, and gaps in AIS reporting. The [Events API](https://globalfishingwatch.org/our-apis/documentation#events-api) allows you to retrieve lists of events, get details for a specific event, and obtain statistics on event occurrences. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/events-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Datasets](https://globalfishingwatch.org/our-apis/documentation#api-dataset), [Events Data Caveats](https://globalfishingwatch.org/our-apis/documentation#how-are-the-events-estimated), and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Prerequisites

- Before using the `gfw-api-python-client`, ensure it is installed (see the [Getting Started](../getting-started) guide) and that you have obtained an API access token from the [Global Fishing Watch API portal](https://globalfishingwatch.org/our-apis/tokens).

## Getting Started

To interact with the Events endpoints, you first need to instantiate the `gfw.Client` and then access the `events` resource:

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

The `gfw_client.events` object provides methods to retrieve event data and statistics. Each of these methods returns a `result` object, which offers convenient ways to access the data as Pydantic models using `.data()` or as pandas DataFrames using `.df()`.

> **Tip:** Use [IPython](https://ipython.readthedocs.io/en/stable/) or Python 3.11+ with `python -m asyncio` to run `gfw-api-python-client` code interactively, as these environments support executing `async` / `await` expressions directly in the console.

## Retrieving All Events from Predefined Region (`get_all_events`)

The `get_all_events()` method allows you to retrieve a list of events based on specified criteria. The `datasets` parameter is mandatory.

> **Note:** See how to use the [Reference Data API - Usage Guides](https://globalfishingwatch.github.io/gfw-api-python-client/usage-guides/references-data-api.html) to obtain and filter predefined [**Regions of Interest (ROIs)**](https://globalfishingwatch.org/our-apis/documentation#regions), such as Exclusive Economic Zones (**EEZs**), Marine Protected Areas (**MPAs**), and Regional Fisheries Management Organizations (**RFMOs**).

```python
eez_rois_result = await gfw_client.references.get_eez_regions(iso3="CHN")
chn_eez_roi = eez_rois_result.data()[0]
print((chn_eez_roi.id, chn_eez_roi.dataset, chn_eez_roi.label, chn_eez_roi.iso3))
```

**Output:**

````
('8486', 'public-eez-areas', 'Chinese Exclusive Economic Zone', 'CHN')
``

```python
events_result = await gfw_client.events.get_all_events(
    datasets=["public-global-fishing-events:latest"],
    start_date="2017-01-01",
    end_date="2017-01-31",
    region=chn_eez_roi,
    limit=5,
)
````

### Access the list of event as Pydantic models

```python
events_data = events_result.data()
event = events_data[-1]
print((event.id, event.type, event.vessel.id))
```

**Output:**

```
('54e1b8739c8ef032f2384e866b56077b',
 'fishing',
 'de2fb30db-b118-8a4e-edac-3764639a0d9e')
```

### Access the events as a DataFrame

```python
events_df = events_result.df()
print(events_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 14 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   start         5 non-null      datetime64[us, UTC]
 1   end           5 non-null      datetime64[us, UTC]
 2   id            5 non-null      str
 3   type          5 non-null      str
 4   position      5 non-null      object
 5   regions       5 non-null      object
 6   bounding_box  5 non-null      object
 7   distances     5 non-null      object
 8   vessel        5 non-null      object
 9   encounter     0 non-null      object
 10  fishing       5 non-null      object
 11  gap           0 non-null      object
 12  loitering     0 non-null      object
 13  port_visit    0 non-null      object
dtypes: datetime64[us, UTC](2), object(10), str(2)
memory usage: 692.0+ bytes
```

## Retrieving All Events from Custom Region (`get_all_events`)

> **Note:** Custom region can either a path to a spatial file (e.g., GeoJSON, Shapefile, etc.), GeoJSON-like object (e.g., JSON string, dictionary, `geopandas.GeoDataFrame`, `shapely`, an object implementing `__geo_interface__` etc.) or `GeoJson` model instance. Spatial files are loaded using [geopandas.read_file](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html) and supported formats depend on a properly configured [geopandas/GDAL installation](https://geopandas.org/en/stable/getting_started/install.html#installing-with-pip).

```python
filename = "https://raw.githubusercontent.com/GlobalFishingWatch/gfw-api-python-client/refs/heads/develop/tests/fixtures/events/geometry/geometry.shp"

custom_roi_gdf = gpd.read_file(filename)
```

```python
custom_events_result = await gfw_client.events.get_all_events(
    datasets=["public-global-fishing-events:latest"],
    start_date="2017-01-01",
    end_date="2017-01-31",
    geometry=custom_roi_gdf,
    limit=5,
)
```

### Access the list of event as Pydantic models

```python
custom_events_data = custom_events_result.data()
custom_event = custom_events_data[-1]
print((custom_event.id, custom_event.type, custom_event.vessel.id))
```

**Output:**

```
('5c03609c64d96c6ca5bfaaca0e9d9b6c',
 'fishing',
 'c01e0a0d2-20d9-7cc6-e04e-449dae2fbd95')
```

### Access the events as a DataFrame

```python
custom_events_df = custom_events_result.df()
print(custom_events_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 14 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   start         5 non-null      datetime64[us, UTC]
 1   end           5 non-null      datetime64[us, UTC]
 2   id            5 non-null      str
 3   type          5 non-null      str
 4   position      5 non-null      object
 5   regions       5 non-null      object
 6   bounding_box  5 non-null      object
 7   distances     5 non-null      object
 8   vessel        5 non-null      object
 9   encounter     0 non-null      object
 10  fishing       5 non-null      object
 11  gap           0 non-null      object
 12  loitering     0 non-null      object
 13  port_visit    0 non-null      object
dtypes: datetime64[us, UTC](2), object(10), str(2)
memory usage: 692.0+ bytes
```

## Retrieving a Single Event by ID (`get_event_by_id`)

To retrieve details for a specific event, you need its `id` and the `dataset` it belongs to.

```python
event_result = await gfw_client.events.get_event_by_id(
    id="c2f0967e061f99a01793edac065de003",
    dataset="public-global-port-visits-events:latest",
)
```

### Access the event model as Pydantic model

```python
event = event_result.data()
print((event.id, event.type, event.vessel.id))
print(event.model_dump())
```

**Output:**

```
('c2f0967e061f99a01793edac065de003', 'port_visit', '8c7304226-6c71-edbe-0b63-c246734b3c01')
```

### Access the event as a DataFrame

```python
event_df = event_result.df()
print(event_df.info())
print(event_df[["id", "type"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 14 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   start         1 non-null      datetime64[ns, UTC]
 1   end           1 non-null      datetime64[ns, UTC]
 2   id            1 non-null      object
 3   type          1 non-null      object
 4   position      1 non-null      object
 5   regions       1 non-null      object
 6   bounding_box  1 non-null      object
 7   distances     1 non-null      object
 8   vessel        1 non-null      object
 9   encounter     0 non-null      object
 10  fishing       0 non-null      object
 11  gap           0 non-null      object
 12  loitering     0 non-null      object
 13  port_visit    1 non-null      object
dtypes: datetime64[ns, UTC](2), object(12)
memory usage: 244.0+ bytes
```

## ## Getting Event Statistics Worldwide (`get_events_stats`)

The `get_events_stats()` method allows you to retrieve statistics on event occurrences based on specified criteria and a time series interval.

```python
worldwide_event_stats_result = await gfw_client.events.get_events_stats(
    datasets=["public-global-encounters-events:latest"],
    encounter_types=["CARRIER-FISHING", "FISHING-CARRIER"],
    vessel_types=["CARRIER"],
    start_date="2018-01-01",
    end_date="2023-01-31",
    timeseries_interval="YEAR",
    flags=["RUS"],
    duration=60,
)
```

### Access the statistics as Pydantic models

```python
worldwide_event_stat = worldwide_event_stats_result.data()
print((
    worldwide_event_stat.num_events,
    worldwide_event_stat.num_flags,
    worldwide_event_stat.num_vessels,
))
```

**Output:**

```
(24819, 1, 194)
```

### Access the statistics as a DataFrame

```python
worldwide_event_stat_df = worldwide_event_stats_result.df()
print(worldwide_event_stat_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 5 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   num_events   1 non-null      int64
 1   num_flags    1 non-null      int64
 2   num_vessels  1 non-null      int64
 3   flags        1 non-null      object
 4   timeseries   1 non-null      object
dtypes: int64(3), object(2)
memory usage: 172.0+ bytes
```

## Getting Event Statistics from Predefined Region (`get_events_stats`)

> **Note:** See how to use the [Reference Data API - Usage Guides](https://globalfishingwatch.github.io/gfw-api-python-client/usage-guides/references-data-api.html) to obtain and filter predefined [**Regions of Interest (ROIs)**](https://globalfishingwatch.org/our-apis/documentation#regions), such as Exclusive Economic Zones (**EEZs**), Marine Protected Areas (**MPAs**), and Regional Fisheries Management Organizations (**RFMOs**).

```python
eez_rois_result = await gfw_client.references.get_eez_regions(iso3="SEN")
sen_eez_roi = eez_rois_result.data()[0]

print((sen_eez_roi.id, sen_eez_roi.dataset, sen_eez_roi.label, sen_eez_roi.iso3))
```

**Output:**

```
('8371', 'public-eez-areas', 'Senegalese Exclusive Economic Zone', 'SEN')
```

```python
predefined_event_stats_result = await gfw_client.events.get_events_stats(
    datasets=["public-global-port-visits-events:latest"],
    start_date="2018-01-01",
    end_date="2019-01-31",
    timeseries_interval="YEAR",
    region=sen_eez_roi,
    confidences=["3", "4"],
)
```

### Access the statistics as Pydantic models

```python
predefined_event_stat = predefined_event_stats_result.data()

print((
    predefined_event_stat.num_events,
    predefined_event_stat.num_flags,
    predefined_event_stat.num_vessels,
))
```

**Output:**

```
(4528, 75, 1464)
```

### Access the statistics as a DataFrame

```python
predefined_event_stat_df = predefined_event_stats_result.df()

print(predefined_event_stat_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 5 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   num_events   1 non-null      int64
 1   num_flags    1 non-null      int64
 2   num_vessels  1 non-null      int64
 3   flags        1 non-null      object
 4   timeseries   1 non-null      object
dtypes: int64(3), object(2)
memory usage: 172.0+ bytes
```

## Getting Event Statistics from Custom Region (`get_events_stats`)

> **Note:** Custom region can either a path to a spatial file (e.g., GeoJSON, Shapefile, etc.), GeoJSON-like object (e.g., JSON string, dictionary, `geopandas.GeoDataFrame`, `shapely`, an object implementing `__geo_interface__` etc.) or `GeoJson` model instance. Spatial files are loaded using [geopandas.read_file](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html) and supported formats depend on a properly configured [geopandas/GDAL installation](https://geopandas.org/en/stable/getting_started/install.html#installing-with-pip).

```python
filename = "https://raw.githubusercontent.com/GlobalFishingWatch/gfw-api-python-client/refs/heads/develop/tests/fixtures/events/geometry/geometry.shp"

custom_stats_roi_gdf = gpd.read_file(filename)
```

```python
custom_event_stats_result = await gfw_client.events.get_events_stats(
    datasets=["public-global-port-visits-events:latest"],
    start_date="2018-01-01",
    end_date="2019-01-31",
    timeseries_interval="YEAR",
    geometry=custom_stats_roi_gdf,
    confidences=["3", "4"],
)
```

### Access the statistics as Pydantic models

```python
custom_event_stat = custom_event_stats_result.data()

print((
    custom_event_stat.num_events,
    custom_event_stat.num_flags,
    custom_event_stat.num_vessels,
))
```

**Output:**

```
(301548, 162, 40996)
```

### Access the statistics as a DataFrame

```python
custom_event_stat_df = custom_event_stats_result.df()

print(custom_event_stat_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 5 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   num_events   1 non-null      int64
 1   num_flags    1 non-null      int64
 2   num_vessels  1 non-null      int64
 3   flags        1 non-null      object
 4   timeseries   1 non-null      object
dtypes: int64(3), object(2)
memory usage: 172.0+ bytes
```

## Data Caveat

Please be aware that the accuracy and completeness of the event data can vary. Refer to the Global Fishing Watch API documentation for any specific caveats related to the datasets you are using.

## Next Steps

Explore the [Usage Guides](index) and [Workflow Guides](../workflow-guides/index) for other API resources to understand how you can combine event data with information about vessels, and more. Check out the following resources:

- [4Wings API](4wings-api)
- [Vessels API](vessels-api)
- [Insights API](insights-api)
- [Datasets API](datasets-api)
- [Bulk Download API](bulk-downloads-api)
- [Reference Data API](references-data-api)
