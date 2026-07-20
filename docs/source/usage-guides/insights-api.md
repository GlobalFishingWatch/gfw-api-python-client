# Insights API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/insights-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access aggregated insights about vessel activities. Currently, the [Insights API](https://globalfishingwatch.org/our-apis/documentation#insights-api) focuses on providing summaries related to specific vessels over a defined time range. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/insights-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Apparent fishing detected in no-take MPAs](https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-detected-in-no-take-mpas), [Apparent fishing event detected outside known authorized areas](https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-event-detected-outside-known-authorized-areas), [Coverage](https://globalfishingwatch.org/our-apis/documentation#insights-api-coverage), [AIS off event (aka GAP)](https://globalfishingwatch.org/our-apis/documentation#insights-api-ais-off-event-aka-gap), and [RFMO IUU vessel list](https://globalfishingwatch.org/our-apis/documentation#insights-api-rfmo-iuu-vessel-list) Data Caveats — it is critical to avoid misinterpreting the insights. You can find the [Datasets](https://globalfishingwatch.org/our-apis/documentation#api-dataset), and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Prerequisites

- Before using the `gfw-api-python-client`, ensure it is installed (see the [Getting Started](../getting-started) guide) and that you have obtained an API access token from the [Global Fishing Watch API portal](https://globalfishingwatch.org/our-apis/tokens).

- You will need a valid `Vessel ID` to retrieve insights for a specific vessel. You can obtain these IDs using the [Vessels API](vessels-api).

## Getting Started

To interact with the Insights endpoints, you first need to instantiate the `gfw.Client` and then access the `insights` resource:

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

The `gfw_client.insights` object provides methods for retrieving insights data for specified vessels. Each of these methods returns a `result` object, which offers convenient ways to access the data as Pydantic models using `.data()` or as pandas DataFrames using `.df()`.

> **Tip:** Use [IPython](https://ipython.readthedocs.io/en/stable/) or Python 3.11+ with `python -m asyncio` to run `gfw-api-python-client` code interactively, as these environments support executing `async` / `await` expressions directly in the console.

## Getting Insights by Vessel (`get_vessel_insights`)

The `get_vessel_insights()` method allows you to retrieve aggregated insights for a specific vessel within a given time range.

**Important:** `start_date` must be on or after `January 1, 2020`. [Insights](https://globalfishingwatch.org/our-apis/documentation#insights-api) are available from `January 1, 2020` onwards.

```python
insights_result = await gfw_client.insights.get_vessel_insights(
    includes=["FISHING"],
    start_date="2020-01-01",
    end_date="2025-03-03",
    vessels=[
        "785101812-2127-e5d2-e8bf-7152c5259f5f",
    ],
)
```

### Access the insights data as Pydantic model

```python
insights = insights_result.data()
print(
    (
        insights.period.start_date,
        insights.period.end_date,
        insights.apparent_fishing.period_selected_counters.events,
    )
)
print(insights.model_dump())
```

**Output:**

```
(datetime.date(2020, 1, 1), datetime.date(2025, 3, 3), 2829)
```

### Access the insights data as a DataFrame

```python
insights_df = insights_result.df()
print(insights_df.info())
print(insights_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   period                       1 non-null      object
 1   vessel_ids_without_identity  0 non-null      object
 2   gap                          0 non-null      object
 3   coverage                     0 non-null      object
 4   apparent_fishing             1 non-null      object
 5   vessel_identity              0 non-null      object
dtypes: object(6)
memory usage: 180.0+ bytes
```

## Getting Apparent Fishing-related Insights (`FISHING`)

```python
fishing_insights_result = await gfw_client.insights.get_vessel_insights(
    includes=["FISHING"],
    start_date="2020-01-01",
    end_date="2025-03-03",
    vessels=[
        "785101812-2127-e5d2-e8bf-7152c5259f5f",
        "2339c52c3-3a84-1603-f968-d8890f23e1ed",
        "2d26aa452-2d4f-4cae-2ec4-377f85e88dcb",
    ],
)
```

```python
fishing_insights_df = fishing_insights_result.df()
print(fishing_insights_df)
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   period                       1 non-null      object
 1   vessel_ids_without_identity  0 non-null      object
 2   gap                          0 non-null      object
 3   coverage                     0 non-null      object
 4   apparent_fishing             1 non-null      object
 5   vessel_identity              0 non-null      object
dtypes: object(6)
memory usage: 180.0+ bytes
```

## Getting AIS off/disabling Insights (`GAP`)

```python
gap_insights_result = await gfw_client.insights.get_vessel_insights(
    includes=["GAP"],
    start_date="2020-01-01",
    end_date="2025-03-03",
    vessels=[
        "785101812-2127-e5d2-e8bf-7152c5259f5f",
        "2339c52c3-3a84-1603-f968-d8890f23e1ed",
        "2d26aa452-2d4f-4cae-2ec4-377f85e88dcb",
    ],
)
```

```python
gap_insights_df = gap_insights_result.df()
print(gap_insights_df)
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   period                       1 non-null      object
 1   vessel_ids_without_identity  0 non-null      object
 2   gap                          1 non-null      object
 3   coverage                     0 non-null      object
 4   apparent_fishing             0 non-null      object
 5   vessel_identity              0 non-null      object
dtypes: object(6)
memory usage: 180.0+ bytes
```

## Getting AIS Coverage Metrics Insights (`COVERAGE`)

```python
coverage_insights_result = await gfw_client.insights.get_vessel_insights(
    includes=["COVERAGE"],
    start_date="2020-01-01",
    end_date="2025-03-03",
    vessels=[
        "2339c52c3-3a84-1603-f968-d8890f23e1ed",
    ],
)
```

```python
coverage_insights_df = coverage_insights_result.df()
print(coverage_insights_df)
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   period                       1 non-null      object
 1   vessel_ids_without_identity  0 non-null      object
 2   gap                          0 non-null      object
 3   coverage                     1 non-null      object
 4   apparent_fishing             0 non-null      object
 5   vessel_identity              0 non-null      object
dtypes: object(6)
memory usage: 180.0+ bytes
```

## Getting Being Listed in IUU (Illegal,Unreported, and Unregulated) Insights (`VESSEL-IDENTITY-IUU-VESSEL-LIST`)

```python
iuu_insights_result = await gfw_client.insights.get_vessel_insights(
    includes=["VESSEL-IDENTITY-IUU-VESSEL-LIST"],
    start_date="2020-01-01",
    end_date="2025-03-03",
    vessels=[
        "2d26aa452-2d4f-4cae-2ec4-377f85e88dcb",
    ],
)
```

```python
iuu_insights_df = iuu_insights_result.df()
print(iuu_insights_df)
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   period                       1 non-null      object
 1   vessel_ids_without_identity  0 non-null      object
 2   gap                          0 non-null      object
 3   coverage                     0 non-null      object
 4   apparent_fishing             0 non-null      object
 5   vessel_identity              1 non-null      object
dtypes: object(6)
memory usage: 180.0+ bytes
```

## Getting Flag Changes Insights (`VESSEL-IDENTITY-FLAG-CHANGES`)

> **Note:** In order to enable this insight for your API access token (`GFW_API_ACCESS_TOKEN`), please contact apis@globalfishingwatch.org. In your message, please specify the email address used to generate the [API tokens](https://globalfishingwatch.org/our-apis/tokens) (i.e., the email address associated with your [Global Fishing Watch account](https://globalfishingwatch.org/our-apis/tokens/signup)).

```python
flag_changes_insights_result = await gfw_client.insights.get_vessel_insights(
    includes=["VESSEL-IDENTITY-FLAG-CHANGES"],
    start_date="2020-01-01",
    end_date="2025-03-03",
    vessels=[
        "2d26aa452-2d4f-4cae-2ec4-377f85e88dcb",
    ],
)
```

```python
flag_changes_insights_df = flag_changes_insights_result.df()
print(flag_changes_insights_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   period                       1 non-null      object
 1   vessel_ids_without_identity  0 non-null      object
 2   gap                          0 non-null      object
 3   coverage                     0 non-null      object
 4   apparent_fishing             0 non-null      object
 5   vessel_identity              1 non-null      object
dtypes: object(6)
memory usage: 180.0+ bytes
```

## Getting Flag State Presence under Tokyo/Paris MOU black or grey Lists Insights (`VESSEL-IDENTITY-MOU-LIST`)

> **Note:** In order to enable this insight for your API access token (`GFW_API_ACCESS_TOKEN`), please contact apis@globalfishingwatch.org. In your message, please specify the email address used to generate the [API tokens](https://globalfishingwatch.org/our-apis/tokens) (i.e., the email address associated with your [Global Fishing Watch account](https://globalfishingwatch.org/our-apis/tokens/signup)).

```python
mou_insights_result = await gfw_client.insights.get_vessel_insights(
    includes=["VESSEL-IDENTITY-MOU-LIST"],
    start_date="2020-01-01",
    end_date="2025-03-03",
    vessels=[
        "785101812-2127-e5d2-e8bf-7152c5259f5f",
    ],
)
```

```python
mou_insights_df = mou_insights_result.df()
print(mou_insights_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   period                       1 non-null      object
 1   vessel_ids_without_identity  0 non-null      object
 2   gap                          0 non-null      object
 3   coverage                     0 non-null      object
 4   apparent_fishing             0 non-null      object
 5   vessel_identity              1 non-null      object
dtypes: object(6)
memory usage: 180.0+ bytes
```

## Getting Multiple Insights for Multiple Vessels

> **Note:** In order to enable `VESSEL-IDENTITY-FLAG-CHANGES` and `VESSEL-IDENTITY-MOU-LIST` insights for your API access token (`GFW_API_ACCESS_TOKEN`), please contact apis@globalfishingwatch.org. In your message, please specify the email address used to generate the [API tokens](https://globalfishingwatch.org/our-apis/tokens) (i.e., the email address associated with your [Global Fishing Watch account](https://globalfishingwatch.org/our-apis/tokens/signup)).

```python
all_insights_result = await gfw_client.insights.get_vessel_insights(
    includes=[
        "FISHING",
        "GAP",
        "VESSEL-IDENTITY-IUU-VESSEL-LIST",
        "COVERAGE",
        "VESSEL-IDENTITY-FLAG-CHANGES",
        "VESSEL-IDENTITY-MOU-LIST",
    ],
    start_date="2020-01-01",
    end_date="2025-03-03",
    vessels=[
        "785101812-2127-e5d2-e8bf-7152c5259f5f",
        "2339c52c3-3a84-1603-f968-d8890f23e1ed",
        "2d26aa452-2d4f-4cae-2ec4-377f85e88dcb",
    ],
)
```

```python
all_insights_df = all_insights_result.df()
print(all_insights_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   period                       1 non-null      object
 1   vessel_ids_without_identity  0 non-null      object
 2   gap                          1 non-null      object
 3   coverage                     1 non-null      object
 4   apparent_fishing             1 non-null      object
 5   vessel_identity              1 non-null      object
dtypes: object(6)
memory usage: 180.0+ bytes
```

## Next Steps

Explore the [Usage Guides](index) and [Workflow Guides](../workflow-guides/index) for other API resources to understand how you can combine vessel insights with event data, vessel details, and more. Check out the following resources:

- [4Wings API](4wings-api)
- [Vessels API](vessels-api)
- [Events API](events-api)
- [Datasets API](datasets-api)
- [Bulk Download API](bulk-downloads-api)
- [Reference Data API](references-data-api)
