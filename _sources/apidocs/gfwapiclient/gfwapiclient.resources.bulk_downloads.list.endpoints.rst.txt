:py:mod:`gfwapiclient.resources.bulk_downloads.list.endpoints`
==============================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.list.endpoints

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.endpoints
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportListEndPoint <gfwapiclient.resources.bulk_downloads.list.endpoints.BulkReportListEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.endpoints.BulkReportListEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.list.endpoints.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.endpoints.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.list.endpoints.__all__
   :value: ['BulkReportListEndPoint']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.endpoints.__all__

.. py:class:: BulkReportListEndPoint(*, request_params: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.bulk_downloads.list.endpoints.BulkReportListEndPoint

   Bases: :py:obj:`gfwapiclient.http.endpoints.GetEndPoint`\ [\ :py:obj:`gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams`\ , :py:obj:`gfwapiclient.http.models.RequestBody`\ , :py:obj:`gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem`\ , :py:obj:`gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.endpoints.BulkReportListEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.endpoints.BulkReportListEndPoint.__init__

   .. py:method:: _transform_response_data(*, body: typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]) -> typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]
      :canonical: gfwapiclient.resources.bulk_downloads.list.endpoints.BulkReportListEndPoint._transform_response_data

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.endpoints.BulkReportListEndPoint._transform_response_data
