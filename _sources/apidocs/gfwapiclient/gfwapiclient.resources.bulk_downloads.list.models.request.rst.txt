:py:mod:`gfwapiclient.resources.bulk_downloads.list.models.request`
===================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.list.models.request

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportListParams <gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.list.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.__all__
          :summary:
   * - :py:obj:`BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.bulk_downloads.list.models.request.BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.list.models.request.__all__
   :value: ['BulkReportListParams']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.__all__

.. py:data:: BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.bulk_downloads.list.models.request.BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Get bulk reports request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:class:: BulkReportListParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams

   Bases: :py:obj:`gfwapiclient.http.models.RequestParams`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams.__init__

   .. py:attribute:: limit
      :canonical: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams.limit
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams.limit

   .. py:attribute:: offset
      :canonical: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams.offset
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams.offset

   .. py:attribute:: sort
      :canonical: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams.sort
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams.sort

   .. py:attribute:: status
      :canonical: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams.status
      :type: typing.Optional[gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.request.BulkReportListParams.status
