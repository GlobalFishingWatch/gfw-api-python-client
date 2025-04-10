:py:mod:`gfwapiclient.resources.references.regions.models.response`
===================================================================

.. py:module:: gfwapiclient.resources.references.regions.models.response

.. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EEZRegionItem <gfwapiclient.resources.references.regions.models.response.EEZRegionItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionItem
          :summary:
   * - :py:obj:`EEZRegionResult <gfwapiclient.resources.references.regions.models.response.EEZRegionResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionResult
          :summary:
   * - :py:obj:`MPARegionItem <gfwapiclient.resources.references.regions.models.response.MPARegionItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionItem
          :summary:
   * - :py:obj:`MPARegionResult <gfwapiclient.resources.references.regions.models.response.MPARegionResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionResult
          :summary:
   * - :py:obj:`RFMORegionItem <gfwapiclient.resources.references.regions.models.response.RFMORegionItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionItem
          :summary:
   * - :py:obj:`RFMORegionResult <gfwapiclient.resources.references.regions.models.response.RFMORegionResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.references.regions.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.references.regions.models.response.__all__
   :value: ['EEZRegionItem', 'EEZRegionResult', 'MPARegionItem', 'MPARegionResult', 'RFMORegionItem', 'RFMORegi...

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.__all__

.. py:class:: EEZRegionItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.references.regions.models.response.EEZRegionItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionItem.__init__

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.references.regions.models.response.EEZRegionItem.id
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionItem.id

   .. py:attribute:: label
      :canonical: gfwapiclient.resources.references.regions.models.response.EEZRegionItem.label
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionItem.label

   .. py:attribute:: iso3
      :canonical: gfwapiclient.resources.references.regions.models.response.EEZRegionItem.iso3
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionItem.iso3

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.references.regions.models.response.EEZRegionItem.dataset
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionItem.dataset

.. py:class:: EEZRegionResult(data: typing.List[gfwapiclient.resources.references.regions.models.response.EEZRegionItem])
   :canonical: gfwapiclient.resources.references.regions.models.response.EEZRegionResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.references.regions.models.response.EEZRegionItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.references.regions.models.response.EEZRegionResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.references.regions.models.response.EEZRegionItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.references.regions.models.response.EEZRegionResult._data
      :type: typing.List[gfwapiclient.resources.references.regions.models.response.EEZRegionItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.EEZRegionResult._data

.. py:class:: MPARegionItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.references.regions.models.response.MPARegionItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionItem.__init__

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.references.regions.models.response.MPARegionItem.id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionItem.id

   .. py:attribute:: label
      :canonical: gfwapiclient.resources.references.regions.models.response.MPARegionItem.label
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionItem.label

   .. py:attribute:: name
      :canonical: gfwapiclient.resources.references.regions.models.response.MPARegionItem.name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionItem.name

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.references.regions.models.response.MPARegionItem.dataset
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionItem.dataset

.. py:class:: MPARegionResult(data: typing.List[gfwapiclient.resources.references.regions.models.response.MPARegionItem])
   :canonical: gfwapiclient.resources.references.regions.models.response.MPARegionResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.references.regions.models.response.MPARegionItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.references.regions.models.response.MPARegionResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.references.regions.models.response.MPARegionItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.references.regions.models.response.MPARegionResult._data
      :type: typing.List[gfwapiclient.resources.references.regions.models.response.MPARegionItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.MPARegionResult._data

.. py:class:: RFMORegionItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.references.regions.models.response.RFMORegionItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionItem.__init__

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.references.regions.models.response.RFMORegionItem.id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionItem.id

   .. py:attribute:: label
      :canonical: gfwapiclient.resources.references.regions.models.response.RFMORegionItem.label
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionItem.label

   .. py:attribute:: rfb
      :canonical: gfwapiclient.resources.references.regions.models.response.RFMORegionItem.rfb
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionItem.rfb

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.references.regions.models.response.RFMORegionItem.dataset
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionItem.dataset

.. py:class:: RFMORegionResult(data: typing.List[gfwapiclient.resources.references.regions.models.response.RFMORegionItem])
   :canonical: gfwapiclient.resources.references.regions.models.response.RFMORegionResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.references.regions.models.response.RFMORegionItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.references.regions.models.response.RFMORegionResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.references.regions.models.response.RFMORegionItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.references.regions.models.response.RFMORegionResult._data
      :type: typing.List[gfwapiclient.resources.references.regions.models.response.RFMORegionItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.references.regions.models.response.RFMORegionResult._data
