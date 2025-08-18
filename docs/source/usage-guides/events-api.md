# Events API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/events-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access information about various activities of a vessel, including fishing activity, encounters, port visits, loitering, and gaps in AIS reporting. The Events API allows you to retrieve lists of events, get details for a specific event, and obtain statistics on event occurrences. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/events-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Data Caveats](https://globalfishingwatch.org/our-apis/documentation#data-caveat) and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Prerequisites

- You have installed the `gfw-api-python-client`. Refer to the [Getting Started](../getting-started) guide for installation instructions.

## Getting Started

To interact with the Events endpoints, you first need to instantiate the `gfw.Client` and then access the `events` resource:

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

The `gfw_client.events` object provides methods to retrieve event data and statistics. Each of these methods returns a `result` object, which offers convenient ways to access the data as Pydantic models using `.data()` or as pandas DataFrames using `.df()`.

## Retrieving All Events (`get_all_events`)

The `get_all_events()` method allows you to retrieve a list of events based on specified criteria. The `datasets` parameter is mandatory.

```python
events_result = await gfw_client.events.get_all_events(
    datasets=["public-global-fishing-events:latest"],
    start_date="2020-10-01",
    end_date="2020-12-31",
    region={
        "dataset": "public-eez-areas",
        "id": "8371",
    },
    limit=1,
)
```

### Access the list of event as Pydantic models

```python
events_data = events_result.data()
event = events_data[-1]
print((event.id, event.type, event.vessel.id))
print(event.model_dump())
```

**Output:**

```
('a0f5848d1a83b7f0b4b8cda6873699ba', 'fishing', '9e01144bf-f383-e634-3178-ca7e34477f34')
```

### Access the events as a DataFrame

```python
events_df = events_result.df()
print(events_df.info())
print(events_df[["id", "type"]].head())
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
 10  fishing       1 non-null      object
 11  gap           0 non-null      object
 12  loitering     0 non-null      object
 13  port_visit    0 non-null      object
dtypes: datetime64[ns, UTC](2), object(12)
memory usage: 244.0+ bytes
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
('a0f5848d1a83b7f0b4b8cda6873699ba', 'fishing', '9e01144bf-f383-e634-3178-ca7e34477f34')
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
 10  fishing       1 non-null      object
 11  gap           0 non-null      object
 12  loitering     0 non-null      object
 13  port_visit    0 non-null      object
dtypes: datetime64[ns, UTC](2), object(12)
memory usage: 244.0+ bytes
```

## Getting Event Statistics (`get_events_stats`)

The `get_events_stats()` method allows you to retrieve statistics on event occurrences based on specified criteria and a time series interval.

```python
event_stats_result = await gfw_client.events.get_events_stats(
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
event_stat = event_stats_result.data()
print((event_stat.num_events, event_stat.num_flags, event_stat.num_vessels))
print(event_stat.model_dump())
```

**Output:**

```
(24786, 1, 194)
```

### Access the statistics as a DataFrame

```python
event_stat_df = event_stats_result.df()
print(event_stat_df.info())
print(event_stat_df[["num_events", "num_flags", "num_vessels"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
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

Explore the [Usage Guides](index) for other API resources to understand how you can combine event data with information about vessels, and more. Check out the following resources:

- [4Wings API](4wings-api)
- [Vessels API](vessels-api)
- [Insights API](insights-api)
- [Datasets API](datasets-api)
- [Reference Data API](references-data-api)
