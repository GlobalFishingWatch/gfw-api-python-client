:py:mod:`gfwapiclient.resources.bulk_downloads.file.models.request`
===================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.file.models.request

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportFileParams <gfwapiclient.resources.bulk_downloads.file.models.request.BulkReportFileParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.request.BulkReportFileParams
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.file.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.request.__all__
          :summary:
   * - :py:obj:`BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.bulk_downloads.file.models.request.BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.request.BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.file.models.request.__all__
   :value: ['BulkReportFileParams']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.request.__all__

.. py:data:: BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.bulk_downloads.file.models.request.BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Get bulk report file download URL request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.request.BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:class:: BulkReportFileParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.file.models.request.BulkReportFileParams

   Bases: :py:obj:`gfwapiclient.http.models.RequestParams`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.request.BulkReportFileParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.request.BulkReportFileParams.__init__

   .. py:attribute:: file
      :canonical: gfwapiclient.resources.bulk_downloads.file.models.request.BulkReportFileParams.file
      :type: typing.Optional[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.request.BulkReportFileParams.file
