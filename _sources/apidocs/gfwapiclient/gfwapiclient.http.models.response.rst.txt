:py:mod:`gfwapiclient.http.models.response`
===========================================

.. py:module:: gfwapiclient.http.models.response

.. autodoc2-docstring:: gfwapiclient.http.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ResultItem <gfwapiclient.http.models.response.ResultItem>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.response.ResultItem
          :summary:
   * - :py:obj:`Result <gfwapiclient.http.models.response.Result>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.response.Result
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.http.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.response.__all__
          :summary:
   * - :py:obj:`_ResultItemT <gfwapiclient.http.models.response._ResultItemT>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.response._ResultItemT
          :summary:
   * - :py:obj:`_ResultT <gfwapiclient.http.models.response._ResultT>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.response._ResultT
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.http.models.response.__all__
   :value: ['Result', 'ResultItem', '_ResultItemT', '_ResultT']

   .. autodoc2-docstring:: gfwapiclient.http.models.response.__all__

.. py:class:: ResultItem(/, **data: typing.Any)
   :canonical: gfwapiclient.http.models.response.ResultItem

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.http.models.response.ResultItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.http.models.response.ResultItem.__init__

.. py:data:: _ResultItemT
   :canonical: gfwapiclient.http.models.response._ResultItemT
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: gfwapiclient.http.models.response._ResultItemT

.. py:class:: Result(*, data: typing.Union[typing.List[gfwapiclient.http.models.response._ResultItemT], gfwapiclient.http.models.response._ResultItemT])
   :canonical: gfwapiclient.http.models.response.Result

   Bases: :py:obj:`typing.Generic`\ [\ :py:obj:`gfwapiclient.http.models.response._ResultItemT`\ ]

   .. autodoc2-docstring:: gfwapiclient.http.models.response.Result

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.http.models.response.Result.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.http.models.response.Result._result_item_class
      :type: typing.Type[gfwapiclient.http.models.response._ResultItemT]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.http.models.response.Result._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.http.models.response.Result._data
      :type: typing.Union[typing.List[gfwapiclient.http.models.response._ResultItemT], gfwapiclient.http.models.response._ResultItemT]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.http.models.response.Result._data

   .. py:method:: data(**kwargs: typing.Any) -> typing.Union[typing.List[gfwapiclient.http.models.response._ResultItemT], gfwapiclient.http.models.response._ResultItemT]
      :canonical: gfwapiclient.http.models.response.Result.data

      .. autodoc2-docstring:: gfwapiclient.http.models.response.Result.data

   .. py:method:: df(*, include: typing.Optional[typing.Set[str]] = None, exclude: typing.Optional[typing.Set[str]] = None, **kwargs: typing.Any) -> typing.Union[pandas.DataFrame, geopandas.GeoDataFrame]
      :canonical: gfwapiclient.http.models.response.Result.df

      .. autodoc2-docstring:: gfwapiclient.http.models.response.Result.df

.. py:data:: _ResultT
   :canonical: gfwapiclient.http.models.response._ResultT
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: gfwapiclient.http.models.response._ResultT
