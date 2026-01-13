:py:mod:`gfwapiclient.resources.bulk_downloads.query.models.base.request`
=========================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.query.models.base.request

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportQueryParams <gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.query.models.base.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.__all__
          :summary:
   * - :py:obj:`BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.bulk_downloads.query.models.base.request.BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.request.__all__
   :value: ['BulkReportQueryParams']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.__all__

.. py:data:: BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.request.BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Query bulk report request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:class:: BulkReportQueryParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams

   Bases: :py:obj:`gfwapiclient.http.models.RequestParams`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.__init__

   .. py:attribute:: indexed_fields
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.indexed_fields
      :type: typing.ClassVar[typing.Optional[typing.List[str]]]
      :value: ['includes']

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.indexed_fields

   .. py:attribute:: limit
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.limit
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.limit

   .. py:attribute:: offset
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.offset
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.offset

   .. py:attribute:: sort
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.sort
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.sort

   .. py:attribute:: includes
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.includes
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.request.BulkReportQueryParams.includes
