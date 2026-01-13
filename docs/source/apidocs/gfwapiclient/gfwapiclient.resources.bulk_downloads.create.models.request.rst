:py:mod:`gfwapiclient.resources.bulk_downloads.create.models.request`
=====================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.create.models.request

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportCreateBody <gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.create.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.__all__
          :summary:
   * - :py:obj:`BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.bulk_downloads.create.models.request.BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.create.models.request.__all__
   :value: ['BulkReportCreateBody']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.__all__

.. py:data:: BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.bulk_downloads.create.models.request.BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Create bulk report request body validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE

.. py:class:: BulkReportCreateBody(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody

   Bases: :py:obj:`gfwapiclient.http.models.RequestBody`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.__init__

   .. py:attribute:: name
      :canonical: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.name

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.dataset
      :type: typing.Optional[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.dataset

   .. py:attribute:: geojson
      :canonical: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.geojson
      :type: typing.Optional[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.geojson

   .. py:attribute:: format
      :canonical: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.format
      :type: typing.Optional[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.format

   .. py:attribute:: region
      :canonical: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.region
      :type: typing.Optional[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.region

   .. py:attribute:: filters
      :canonical: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.filters
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.request.BulkReportCreateBody.filters
