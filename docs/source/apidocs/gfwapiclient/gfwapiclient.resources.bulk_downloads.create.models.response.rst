:py:mod:`gfwapiclient.resources.bulk_downloads.create.models.response`
======================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.create.models.response

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportCreateItem <gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateItem
          :summary:
   * - :py:obj:`BulkReportCreateResult <gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.create.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.create.models.response.__all__
   :value: ['BulkReportCreateItem', 'BulkReportCreateResult']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.__all__

.. py:class:: BulkReportCreateItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateItem

   Bases: :py:obj:`gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateItem.__init__

.. py:class:: BulkReportCreateResult(data: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateItem)
   :canonical: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult._data
      :type: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateItem
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.create.models.response.BulkReportCreateResult._data
