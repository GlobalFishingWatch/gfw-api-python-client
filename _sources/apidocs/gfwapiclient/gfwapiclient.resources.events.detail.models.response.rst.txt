:py:mod:`gfwapiclient.resources.events.detail.models.response`
==============================================================

.. py:module:: gfwapiclient.resources.events.detail.models.response

.. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventDetailItem <gfwapiclient.resources.events.detail.models.response.EventDetailItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.EventDetailItem
          :summary:
   * - :py:obj:`EventDetailResult <gfwapiclient.resources.events.detail.models.response.EventDetailResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.EventDetailResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.detail.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.detail.models.response.__all__
   :value: ['EventDetailItem', 'EventDetailResult']

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.__all__

.. py:class:: EventDetailItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.detail.models.response.EventDetailItem

   Bases: :py:obj:`gfwapiclient.resources.events.base.models.response.EventItem`

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.EventDetailItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.EventDetailItem.__init__

.. py:class:: EventDetailResult(data: gfwapiclient.resources.events.detail.models.response.EventDetailItem)
   :canonical: gfwapiclient.resources.events.detail.models.response.EventDetailResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.events.detail.models.response.EventDetailItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.EventDetailResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.EventDetailResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.events.detail.models.response.EventDetailResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.events.detail.models.response.EventDetailItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.EventDetailResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.events.detail.models.response.EventDetailResult._data
      :type: gfwapiclient.resources.events.detail.models.response.EventDetailItem
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.response.EventDetailResult._data
