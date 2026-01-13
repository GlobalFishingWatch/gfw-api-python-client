# Bulk Download API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/bulk-downloads-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access the [Bulk Download API](https://globalfishingwatch.org/our-apis/documentation#bulk-download-api), which is designed to support workflows that require bulk access to data, including integration with platforms and tools used by data engineers and researchers. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/bulk-downloads-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Datasets](https://globalfishingwatch.org/our-apis/documentation#api-dataset), [Data Caveats](https://globalfishingwatch.org/our-apis/documentation#data-caveat), [SAR (Synthetic-Aperture Radar) Data Caveats](https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats), and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Prerequisites

- Before using the `gfw-api-python-client`, ensure it is installed (see the [Getting Started](../getting-started) guide) and that you have obtained an API access token from the [Global Fishing Watch API portal](https://globalfishingwatch.org/our-apis/tokens).

## Getting Started

To interact with the Bulk Download endpoints, you first need to instantiate the `gfw.Client` and then access the `bulk_downloads` resource:

```python
import time
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

The `gfw_client.bulk_downloads` object provides methods to:

- Create bulk reports based on specific filters and spatial parameters.
- Monitor previously created bulk report generation status.
- Get signed URL to download previously created bulk report data, metadata and
  region geometry (in GeoJSON format) files.
- Query previously created bulk report data records in JSON format.

These methods return a `result` object, which offers convenient ways to access the data as Pydantic models using `.data()` or as pandas DataFrames using `.df()`.

> **Tip:** Use [IPython](https://ipython.readthedocs.io/en/stable/) or Python 3.11+ with `python -m asyncio` to run `gfw-api-python-client` code interactively, as these environments support executing `async` / `await` expressions directly in the console.

## Create a Bulk Report (`create_bulk_report`)

The `create_bulk_report()` method allows you create a bulk report based on specified filters and spatial parameters. The `name` parameter is mandatory. Please [learn more about create a bulk report here](https://globalfishingwatch.org/our-apis/documentation#create-a-bulk-report) and [check its data caveats here](https://globalfishingwatch.org/our-apis/documentation#data-caveat) and [here](https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats).

```python
timestamp = int(time.time() * 1000)
dataset = "public-fixed-infrastructure-data:latest"
region_dataset = "public-eez-areas"
region_id = "8466"  # Argentinian Exclusive Economic Zone
name = f"{dataset.split(':')[0]}_{region_dataset}__{region_id}_{timestamp}"

create_bulk_report_result = await gfw_client.bulk_downloads.create_bulk_report(
    name=name,
    dataset=dataset,
    region={
        "dataset": region_dataset,
        "id": region_id,
    },
    filters=["label = 'oil'", "label_confidence = 'high'"],
)
```

### Access Create a Bulk Report Result as Pydantic models

```python
create_bulk_report_data = create_bulk_report_result.data()
print((
    create_bulk_report_data.id,
    create_bulk_report_data.name,
    create_bulk_report_data.status,
    create_bulk_report_data.created_at,
))
```

**Output:**

```
('c5e32895-4374-41d2-8b2e-ac414ed6757f',
 'public-fixed-infrastructure-data_public-eez-areas__8466_1768085547174',
 'pending',
 datetime.datetime(2026, 1, 10, 22, 52, 30, 9000, tzinfo=TzInfo(0)))
```

### Access Create a Bulk Report Result as a DataFrame

```python
create_bulk_report_df = create_bulk_report_result.df()

print(create_bulk_report_df.info())
print(create_bulk_report_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 12 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   id          1 non-null      object
 1   name        1 non-null      object
 2   file_path   1 non-null      object
 3   format      1 non-null      object
 4   filters     1 non-null      object
 5   geom        1 non-null      object
 6   status      1 non-null      object
 7   owner_id    1 non-null      int64
 8   owner_type  1 non-null      object
 9   created_at  1 non-null      datetime64[ns, UTC]
 10  updated_at  1 non-null      datetime64[ns, UTC]
 11  file_size   0 non-null      object
dtypes: datetime64[ns, UTC](2), int64(1), object(9)
memory usage: 228.0+ bytes
```

## Get Bulk Report by ID (`get_bulk_report_by_id`)

The `get_bulk_report_by_id()` method allows you retrieves metadata and status of the previously created bulk report based on the provided bulk report ID. The `id` parameter is mandatory. Please [learn more about get bulk report by id report here](https://globalfishingwatch.org/our-apis/documentation#get-bulk-report-by-id) and [check its data caveats here](https://globalfishingwatch.org/our-apis/documentation#data-caveat) and [here](https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats).

> **Important:** We recommend to use this method to poll the status of previously created bulk report, if it takes **several minutes or hours** to generate until it status is `done` or `failed`.

```python
bulk_report_result = await gfw_client.bulk_downloads.get_bulk_report_by_id(
    id=create_bulk_report_data.id
)
```

### Access Get Bulk Report by ID Result as Pydantic models

```python
bulk_report_data = bulk_report_result.data()

print((
    create_bulk_report_data.id,
    create_bulk_report_data.name,
    create_bulk_report_data.status,
    create_bulk_report_data.created_at,
))
```

**Output:**

```
('c5e32895-4374-41d2-8b2e-ac414ed6757f',
 'public-fixed-infrastructure-data_public-eez-areas__8466_1768085547174',
 'pending',
 datetime.datetime(2026, 1, 10, 22, 52, 30, 9000, tzinfo=TzInfo(0)))
```

### Access Get Bulk Report by ID Result as a DataFrame

```python
bulk_report_df = bulk_report_result.df()

print(bulk_report_df.info())
print(bulk_report_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 12 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   id          1 non-null      object
 1   name        1 non-null      object
 2   file_path   1 non-null      object
 3   format      1 non-null      object
 4   filters     1 non-null      object
 5   geom        1 non-null      object
 6   status      1 non-null      object
 7   owner_id    1 non-null      int64
 8   owner_type  1 non-null      object
 9   created_at  1 non-null      datetime64[ns, UTC]
 10  updated_at  1 non-null      datetime64[ns, UTC]
 11  file_size   0 non-null      object
dtypes: datetime64[ns, UTC](2), int64(1), object(9)
memory usage: 228.0+ bytes
```

## Get All Bulk Reports Created by User or Application (`get_all_bulk_reports`)

The `get_all_bulk_reports()` method allows you retrieves a list of **metadata and status** of the previously created bulk reports based on specified pagination, sorting, and filtering criteria. Please [learn more about get all bulk reports created by user or application here](https://globalfishingwatch.org/our-apis/documentation#get-all-bulk-reports-by-user) and [check its data caveats here](https://globalfishingwatch.org/our-apis/documentation#data-caveat) and [here](https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats).

```python
bulk_reports_result = await gfw_client.bulk_downloads.get_all_bulk_reports(
    status="done",
)
```

### Access All Created Bulk Reports Result as Pydantic models

```python
bulk_reports_data = bulk_reports_result.data()
bulk_report_item = bulk_reports_data[-1]

print((
    bulk_report_item.id,
    bulk_report_item.name,
    bulk_report_item.status,
    bulk_report_item.created_at,
))
```

**Output:**

```
('0c0cada1-72dd-4fb0-bdf6-7fe8c7fdb1e3',
 'sar-fixed-infrastructure-data-20241207-region-1',
 'done',
 datetime.datetime(2025, 12, 7, 10, 3, 12, 371000, tzinfo=TzInfo(0)))
```

### Access All Created Bulk Reports Result as a DataFrame

```python
bulk_reports_df = bulk_reports_result.df()

print(bulk_reports_df.info())
print(bulk_reports_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 12 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   id          7 non-null      object
 1   name        7 non-null      object
 2   file_path   7 non-null      object
 3   format      7 non-null      object
 4   filters     7 non-null      object
 5   geom        4 non-null      object
 6   status      7 non-null      object
 7   owner_id    7 non-null      int64
 8   owner_type  7 non-null      object
 9   created_at  7 non-null      datetime64[ns, UTC]
 10  updated_at  7 non-null      datetime64[ns, UTC]
 11  file_size   7 non-null      float64
dtypes: datetime64[ns, UTC](2), float64(1), int64(1), object(8)
memory usage: 804.0+ bytes
```

## Get Bulk Report File Download URL (`get_bulk_report_file_download_url`)

The `get_bulk_report_file_download_url()` method allows you retrieves **signed URL** that points to a **downloadable file** hosted on Global Fishing Watch's cloud infrastructure to **download file(s)** (i.e., `"DATA"`, `"README"`, or `"GEOM"`) of the previously created bulk report. The `id` parameter is mandatory. Please [learn more about get bulk report file download url here](https://globalfishingwatch.org/our-apis/documentation#download-bulk-report-url-file) and [check its data caveats here](https://globalfishingwatch.org/our-apis/documentation#data-caveat) and [here](https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats).

```python
bulk_report_file_download_url_result = (
    await gfw_client.bulk_downloads.get_bulk_report_file_download_url(
        id=bulk_reports_data[0].id, file="DATA"
    )
)
```

### Access Get Bulk Report File Download URL Result as Pydantic models

```python
bulk_report_file_download_url_data = bulk_report_file_download_url_result.data()

print(bulk_report_file_download_url_data.url)
```

**Output:**

```
'https://storage.googleapis.com/gfw-api-bulk-pro-us-central1/705f2f9a-f695-43f1-a4bf-7746f3deb091/data.json.gz?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=api-bulk-pro%40gfw-production.iam.gserviceaccount.com%2F20260110%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260110T225232Z&X-Goog-Expires=60&X-Goog-SignedHeaders=host&X-Goog-Signature=481a4ff7244b7286f303b37bb7941c291a26d1e3502debdb7611b8cb2d5edf37bc7aa0287b15a11c2f69f72e88791da3f76873a2fd7d08f911691c35ee8e095b825615510de8256f8cd275211997141e026837e118d86e01c026c457dc1f47d43ff2cb07131c3d21e7908c847bf1e3d87cd4773f02e8e4512a7c15e93799de186b9ea004be50cd3e53292f01e9393595a81c42cc3686f65d280f4f16076759da4722c17c2a6a698393c919cdd083402421a1bbf425b618244b3a9b30e48b770a9dc7f9eed8e63af04f8e31f0b6723fdf76fa7262ded89e7a375fbaea3b031bf29db22b1961878facd79c92d633ab6aa2309c0ce3982104d9835058ecd829bee8'
```

### Access Get Bulk Report File Download URL Result as a DataFrame

```python
bulk_report_file_download_url_df = bulk_report_file_download_url_result.df()

print(bulk_report_file_download_url_df.info())
print(bulk_report_file_download_url_df.iloc[0]["url"])
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 1 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   url     1 non-null      object
dtypes: object(1)
memory usage: 140.0+ bytes
```

## Query Bulk Fixed Infrastructure Data Report (`query_bulk_fixed_infrastructure_data_report`)

The `query_bulk_fixed_infrastructure_data_report()` method allows you retrieves **data records** of a previously created **fixed infrastructure data** (i.e., `public-fixed-infrastructure-data:latest` dataset) bulk report data in JSON format based on specified pagination, sorting, and including criteria. The `id` parameter is mandatory. Please [learn more about query bulk fixed infrastructure data report in JSON format here](https://globalfishingwatch.org/our-apis/documentation#get-data-in-json-format) and [check its data caveats here](https://globalfishingwatch.org/our-apis/documentation#data-caveat) and [here](https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats).

```python
bulk_fixed_infrastructure_data_report_result = (
    await gfw_client.bulk_downloads.query_bulk_fixed_infrastructure_data_report(
        id=bulk_reports_data[0].id
    )
)
```

### Access Query Bulk Fixed Infrastructure Data Report Result as Pydantic models

```python
bulk_fixed_infrastructure_data_report_data = (
    bulk_fixed_infrastructure_data_report_result.data()
)

bulk_fixed_infrastructure_data_report_item = bulk_fixed_infrastructure_data_report_data[
    -1
]

print((
    bulk_fixed_infrastructure_data_report_item.structure_id,
    bulk_fixed_infrastructure_data_report_item.lat,
    bulk_fixed_infrastructure_data_report_item.lon,
    bulk_fixed_infrastructure_data_report_item.label,
    bulk_fixed_infrastructure_data_report_item.label_confidence,
))
```

**Output:**

```
('1051638', -53.0895574340617, -67.32289149541135, 'oil', 'high')
```

### Access Query Bulk Fixed Infrastructure Data Report Result as a DataFrame

```python
bulk_fixed_infrastructure_data_report_result_df = (
    bulk_fixed_infrastructure_data_report_result.df()
)

print(bulk_fixed_infrastructure_data_report_result_df.info())
print(bulk_fixed_infrastructure_data_report_result_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1238 entries, 0 to 1237
Data columns (total 9 columns):
 #   Column                Non-Null Count  Dtype
---  ------                --------------  -----
 0   detection_id          1237 non-null   object
 1   detection_date        1238 non-null   datetime64[ns]
 2   structure_id          1238 non-null   object
 3   lat                   1238 non-null   float64
 4   lon                   1238 non-null   float64
 5   structure_start_date  1238 non-null   datetime64[ns]
 6   structure_end_date    7 non-null      datetime64[ns]
 7   label                 1238 non-null   object
 8   label_confidence      1238 non-null   object
dtypes: datetime64[ns](3), float64(2), object(4)
memory usage: 87.2+ KB
```

## Next Steps

Explore the [Usage Guides](index) and [Workflow Guides](../workflow-guides/index) for other API resources to understand how you can combine the reporting and statistical capabilities of the 4Wings API with vessel information, event data, and more. Check out the following resources:

- [4Wings API](4wings-api)
- [Vessels API](vessels-api)
- [Events API](events-api)
- [Insights API](insights-api)
- [Datasets API](datasets-api)
- [Reference Data API](references-data-api)
