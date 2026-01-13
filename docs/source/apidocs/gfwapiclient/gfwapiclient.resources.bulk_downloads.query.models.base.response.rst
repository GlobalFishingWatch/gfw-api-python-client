:py:mod:`gfwapiclient.resources.bulk_downloads.query.models.base.response`
==========================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.query.models.base.response

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportQueryItem <gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryItem
          :summary:
   * - :py:obj:`BulkReportQueryResult <gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.query.models.base.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.__all__
          :summary:
   * - :py:obj:`_BulkReportQueryItemT <gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT
          :summary:
   * - :py:obj:`_BulkReportQueryResultT <gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryResultT>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryResultT
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.response.__all__
   :value: ['BulkReportQueryItem', 'BulkReportQueryResult', '_BulkReportQueryItemT', '_BulkReportQueryResultT']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.__all__

.. py:class:: BulkReportQueryItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryItem.__init__

.. py:data:: _BulkReportQueryItemT
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT

.. py:class:: BulkReportQueryResult(data: typing.List[gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT])
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult._data
      :type: typing.List[gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryItemT]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult._data

.. py:data:: _BulkReportQueryResultT
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryResultT
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.base.response._BulkReportQueryResultT
