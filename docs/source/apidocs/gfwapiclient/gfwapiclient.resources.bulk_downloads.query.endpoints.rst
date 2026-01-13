:py:mod:`gfwapiclient.resources.bulk_downloads.query.endpoints`
===============================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.query.endpoints

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportQueryEndPoint <gfwapiclient.resources.bulk_downloads.query.endpoints.BulkReportQueryEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkReportQueryEndPoint
          :summary:
   * - :py:obj:`BulkFixedInfrastructureDataQueryEndPoint <gfwapiclient.resources.bulk_downloads.query.endpoints.BulkFixedInfrastructureDataQueryEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkFixedInfrastructureDataQueryEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.query.endpoints.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.query.endpoints.__all__
   :value: ['BulkFixedInfrastructureDataQueryEndPoint', 'BulkReportQueryEndPoint']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints.__all__

.. py:class:: BulkReportQueryEndPoint(*, bulk_report_id: str, request_params: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams, result_item_class: typing.Type[gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT], result_class: typing.Type[gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryResultT], http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkReportQueryEndPoint

   Bases: :py:obj:`gfwapiclient.http.endpoints.GetEndPoint`\ [\ :py:obj:`gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams`\ , :py:obj:`gfwapiclient.http.models.RequestBody`\ , :py:obj:`gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT`\ , :py:obj:`gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryResultT`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkReportQueryEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkReportQueryEndPoint.__init__

   .. py:method:: _transform_response_data(*, body: typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]) -> typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]
      :canonical: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkReportQueryEndPoint._transform_response_data

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkReportQueryEndPoint._transform_response_data

.. py:class:: BulkFixedInfrastructureDataQueryEndPoint(*, bulk_report_id: str, request_params: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkFixedInfrastructureDataQueryEndPoint

   Bases: :py:obj:`gfwapiclient.resources.bulk_downloads.query.endpoints.BulkReportQueryEndPoint`\ [\ :py:obj:`gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem`\ , :py:obj:`gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkFixedInfrastructureDataQueryEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.endpoints.BulkFixedInfrastructureDataQueryEndPoint.__init__
