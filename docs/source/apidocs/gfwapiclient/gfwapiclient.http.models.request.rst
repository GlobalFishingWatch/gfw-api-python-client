:py:mod:`gfwapiclient.http.models.request`
==========================================

.. py:module:: gfwapiclient.http.models.request

.. autodoc2-docstring:: gfwapiclient.http.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`RequestParams <gfwapiclient.http.models.request.RequestParams>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestParams
          :summary:
   * - :py:obj:`RequestBody <gfwapiclient.http.models.request.RequestBody>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestBody
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.http.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.request.__all__
          :summary:
   * - :py:obj:`_RequestParamsT <gfwapiclient.http.models.request._RequestParamsT>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.request._RequestParamsT
          :summary:
   * - :py:obj:`_RequestBodyT <gfwapiclient.http.models.request._RequestBodyT>`
     - .. autodoc2-docstring:: gfwapiclient.http.models.request._RequestBodyT
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.http.models.request.__all__
   :value: ['RequestBody', 'RequestParams', '_RequestBodyT', '_RequestParamsT']

   .. autodoc2-docstring:: gfwapiclient.http.models.request.__all__

.. py:class:: RequestParams(/, **data: typing.Any)
   :canonical: gfwapiclient.http.models.request.RequestParams

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestParams.__init__

   .. py:attribute:: indexed_fields
      :canonical: gfwapiclient.http.models.request.RequestParams.indexed_fields
      :type: typing.ClassVar[typing.Optional[typing.List[str]]]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestParams.indexed_fields

   .. py:attribute:: comma_separated_fields
      :canonical: gfwapiclient.http.models.request.RequestParams.comma_separated_fields
      :type: typing.ClassVar[typing.Optional[typing.List[str]]]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestParams.comma_separated_fields

   .. py:method:: to_query_params(**kwargs: typing.Any) -> typing.Dict[str, typing.Any]
      :canonical: gfwapiclient.http.models.request.RequestParams.to_query_params

      .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestParams.to_query_params

.. py:data:: _RequestParamsT
   :canonical: gfwapiclient.http.models.request._RequestParamsT
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: gfwapiclient.http.models.request._RequestParamsT

.. py:class:: RequestBody(/, **data: typing.Any)
   :canonical: gfwapiclient.http.models.request.RequestBody

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestBody

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestBody.__init__

   .. py:method:: to_json_body(**kwargs: typing.Any) -> typing.Dict[str, typing.Any]
      :canonical: gfwapiclient.http.models.request.RequestBody.to_json_body

      .. autodoc2-docstring:: gfwapiclient.http.models.request.RequestBody.to_json_body

.. py:data:: _RequestBodyT
   :canonical: gfwapiclient.http.models.request._RequestBodyT
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: gfwapiclient.http.models.request._RequestBodyT
