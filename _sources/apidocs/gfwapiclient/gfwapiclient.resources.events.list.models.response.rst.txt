:py:mod:`gfwapiclient.resources.events.list.models.response`
============================================================

.. py:module:: gfwapiclient.resources.events.list.models.response

.. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventListItem <gfwapiclient.resources.events.list.models.response.EventListItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.EventListItem
          :summary:
   * - :py:obj:`EventListResult <gfwapiclient.resources.events.list.models.response.EventListResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.EventListResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.list.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.list.models.response.__all__
   :value: ['EventListItem', 'EventListResult']

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.__all__

.. py:class:: EventListItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.list.models.response.EventListItem

   Bases: :py:obj:`gfwapiclient.resources.events.base.models.response.EventItem`

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.EventListItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.EventListItem.__init__

.. py:class:: EventListResult(data: typing.List[gfwapiclient.resources.events.list.models.response.EventListItem])
   :canonical: gfwapiclient.resources.events.list.models.response.EventListResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.events.list.models.response.EventListItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.EventListResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.EventListResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.events.list.models.response.EventListResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.events.list.models.response.EventListItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.EventListResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.events.list.models.response.EventListResult._data
      :type: typing.List[gfwapiclient.resources.events.list.models.response.EventListItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.response.EventListResult._data
