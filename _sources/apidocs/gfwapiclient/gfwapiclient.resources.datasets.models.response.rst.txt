:py:mod:`gfwapiclient.resources.datasets.models.response`
=========================================================

.. py:module:: gfwapiclient.resources.datasets.models.response

.. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SARFixedInfrastructureItem <gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem
          :summary:
   * - :py:obj:`SARFixedInfrastructureResult <gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.datasets.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.datasets.models.response.__all__
   :value: ['SARFixedInfrastructureItem', 'SARFixedInfrastructureResult']

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.__all__

.. py:class:: SARFixedInfrastructureItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem

   Bases: :py:obj:`gfwapiclient.http.models.response.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.__init__

   .. py:attribute:: structure_id
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.structure_id
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.structure_id

   .. py:attribute:: lat
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.lat
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.lat

   .. py:attribute:: lon
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.lon
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.lon

   .. py:attribute:: label
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.label
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.label

   .. py:attribute:: structure_start_date
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.structure_start_date
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.structure_start_date

   .. py:attribute:: structure_end_date
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.structure_end_date
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.structure_end_date

   .. py:attribute:: label_confidence
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.label_confidence
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.label_confidence

   .. py:method:: epoch_to_utc_datetime_or_none(value: typing.Any) -> typing.Optional[typing.Any]
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.epoch_to_utc_datetime_or_none
      :classmethod:

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem.epoch_to_utc_datetime_or_none

.. py:class:: SARFixedInfrastructureResult(data: typing.List[gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem])
   :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult

   Bases: :py:obj:`gfwapiclient.http.models.response.Result`\ [\ :py:obj:`gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult._data
      :type: typing.List[gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult._data
