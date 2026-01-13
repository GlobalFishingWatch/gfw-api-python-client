:py:mod:`gfwapiclient.resources.bulk_downloads.resources`
=========================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.resources

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkDownloadResource <gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.resources.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.resources.__all__
   :value: ['BulkDownloadResource']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.__all__

.. py:class:: BulkDownloadResource(*, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource

   Bases: :py:obj:`gfwapiclient.http.resources.BaseResource`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.__init__

   .. py:method:: create_bulk_report(*, name: str, dataset: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset, str]] = None, geojson: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry, typing.Dict[str, typing.Any]]] = None, format: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat, str]] = None, region: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion, typing.Dict[str, typing.Any]]] = None, filters: typing.Optional[typing.List[str]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult
      :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.create_bulk_report
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.create_bulk_report

   .. py:method:: get_bulk_report_by_id(*, id: str, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult
      :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.get_bulk_report_by_id
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.get_bulk_report_by_id

   .. py:method:: get_all_bulk_reports(*, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None, sort: typing.Optional[str] = None, status: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus, str]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult
      :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.get_all_bulk_reports
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.get_all_bulk_reports

   .. py:method:: get_bulk_report_file_download_url(*, id: str, file: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType, str]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult
      :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.get_bulk_report_file_download_url
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.get_bulk_report_file_download_url

   .. py:method:: query_bulk_fixed_infrastructure_data_report(*, id: str, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None, sort: typing.Optional[str] = None, includes: typing.Optional[typing.List[str]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult
      :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.query_bulk_fixed_infrastructure_data_report
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource.query_bulk_fixed_infrastructure_data_report

   .. py:method:: _prepare_create_bulk_report_request_body(*, name: str, dataset: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset, str]] = None, geojson: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry, typing.Dict[str, typing.Any]]] = None, format: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat, str]] = None, region: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion, typing.Dict[str, typing.Any]]] = None, filters: typing.Optional[typing.List[str]] = None) -> gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody
      :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource._prepare_create_bulk_report_request_body

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource._prepare_create_bulk_report_request_body

   .. py:method:: _prepare_get_all_bulk_report_params(*, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None, sort: typing.Optional[str] = None, status: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus, str]] = None) -> gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams
      :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource._prepare_get_all_bulk_report_params

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource._prepare_get_all_bulk_report_params

   .. py:method:: _prepare_get_bulk_report_file_download_url_params(*, file: typing.Optional[typing.Union[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType, str]] = None) -> gfwapiclient.resources.bulk_downloads.file.models.request.BulkReportFileParams
      :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource._prepare_get_bulk_report_file_download_url_params

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource._prepare_get_bulk_report_file_download_url_params

   .. py:method:: _prepare_query_bulk_report_params(*, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None, sort: typing.Optional[str] = None, includes: typing.Optional[typing.List[str]] = None) -> gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams
      :canonical: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource._prepare_query_bulk_report_params

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.resources.BulkDownloadResource._prepare_query_bulk_report_params
