:py:mod:`gfwapiclient.resources.fourwings.resources`
====================================================

.. py:module:: gfwapiclient.resources.fourwings.resources

.. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`FourWingsResource <gfwapiclient.resources.fourwings.resources.FourWingsResource>`
     - .. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources.FourWingsResource
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.fourwings.resources.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.fourwings.resources.__all__
   :value: ['FourWingsResource']

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources.__all__

.. py:class:: FourWingsResource(*, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.fourwings.resources.FourWingsResource

   Bases: :py:obj:`gfwapiclient.http.resources.BaseResource`

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources.FourWingsResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources.FourWingsResource.__init__

   .. py:method:: create_report(*, spatial_resolution: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportSpatialResolution, str]] = None, group_by: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportGroupBy, str]] = None, temporal_resolution: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportTemporalResolution, str]] = None, datasets: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportDataset], typing.List[str]]] = None, filters: typing.Optional[typing.List[str]] = None, start_date: typing.Optional[typing.Union[datetime.date, str]] = None, end_date: typing.Optional[typing.Union[datetime.date, str]] = None, spatial_aggregation: typing.Optional[bool] = None, geojson: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsGeometry, typing.Dict[str, typing.Any]]] = None, region: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportRegion, typing.Dict[str, typing.Any]]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult
      :canonical: gfwapiclient.resources.fourwings.resources.FourWingsResource.create_report
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources.FourWingsResource.create_report

   .. py:method:: _prepare_create_report_request_body(*, geojson: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsGeometry, typing.Dict[str, typing.Any]]] = None, region: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportRegion, typing.Dict[str, typing.Any]]] = None) -> gfwapiclient.resources.fourwings.report.models.request.FourWingsReportBody
      :canonical: gfwapiclient.resources.fourwings.resources.FourWingsResource._prepare_create_report_request_body

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources.FourWingsResource._prepare_create_report_request_body

   .. py:method:: _prepare_create_report_request_params(*, spatial_resolution: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportSpatialResolution, str]] = None, group_by: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportGroupBy, str]] = None, temporal_resolution: typing.Optional[typing.Union[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportTemporalResolution, str]] = None, datasets: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.fourwings.report.models.request.FourWingsReportDataset], typing.List[str]]] = None, filters: typing.Optional[typing.List[str]] = None, start_date: typing.Optional[typing.Union[datetime.date, str]] = None, end_date: typing.Optional[typing.Union[datetime.date, str]] = None, spatial_aggregation: typing.Optional[bool] = None) -> gfwapiclient.resources.fourwings.report.models.request.FourWingsReportParams
      :canonical: gfwapiclient.resources.fourwings.resources.FourWingsResource._prepare_create_report_request_params

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources.FourWingsResource._prepare_create_report_request_params

   .. py:method:: _prepare_create_report_date_range_request_param(*, start_date: typing.Optional[typing.Union[datetime.date, str]] = None, end_date: typing.Optional[typing.Union[datetime.date, str]] = None) -> typing.Optional[str]
      :canonical: gfwapiclient.resources.fourwings.resources.FourWingsResource._prepare_create_report_date_range_request_param

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.resources.FourWingsResource._prepare_create_report_date_range_request_param
