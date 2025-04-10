:py:mod:`gfwapiclient.http.endpoints.base`
==========================================

.. py:module:: gfwapiclient.http.endpoints.base

.. autodoc2-docstring:: gfwapiclient.http.endpoints.base
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BaseEndPoint <gfwapiclient.http.endpoints.base.BaseEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.http.endpoints.base.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.__all__
          :summary:
   * - :py:obj:`log <gfwapiclient.http.endpoints.base.log>`
     - .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.log
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.http.endpoints.base.__all__
   :value: ['BaseEndPoint']

   .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.__all__

.. py:data:: log
   :canonical: gfwapiclient.http.endpoints.base.log
   :type: logging.Logger
   :value: 'getLogger(...)'

   .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.log

.. py:class:: BaseEndPoint(*, method: http.HTTPMethod, path: str, request_params: typing.Optional[gfwapiclient.http.models.request._RequestParamsT], request_body: typing.Optional[gfwapiclient.http.models.request._RequestBodyT], result_item_class: typing.Type[gfwapiclient.http.models.response._ResultItemT], result_class: typing.Type[gfwapiclient.http.models.response._ResultT], http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint

   Bases: :py:obj:`gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint`\ [\ :py:obj:`gfwapiclient.http.models.request._RequestParamsT`\ , :py:obj:`gfwapiclient.http.models.request._RequestBodyT`\ , :py:obj:`gfwapiclient.http.models.response._ResultItemT`\ , :py:obj:`gfwapiclient.http.models.response._ResultT`\ ]

   .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint.__init__

   .. py:method:: request(**kwargs: typing.Any) -> gfwapiclient.http.models.response._ResultT
      :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint.request
      :async:

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint.request

   .. py:method:: _request(**kwargs: typing.Any) -> gfwapiclient.http.models.response._ResultT
      :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint._request
      :async:

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint._request

   .. py:method:: _process_response_data(*, response: httpx.Response) -> gfwapiclient.http.models.response._ResultT
      :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint._process_response_data

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint._process_response_data

   .. py:method:: _parse_response_data(*, response: httpx.Response) -> typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]
      :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint._parse_response_data

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint._parse_response_data

   .. py:method:: _transform_response_data(*, body: typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]) -> typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]
      :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint._transform_response_data

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint._transform_response_data

   .. py:method:: _cast_response_data(*, body: typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]], response: httpx.Response) -> typing.Union[typing.List[gfwapiclient.http.models.response._ResultItemT], gfwapiclient.http.models.response._ResultItemT]
      :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint._cast_response_data

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint._cast_response_data

   .. py:method:: _build_api_result(*, data: typing.Union[typing.List[gfwapiclient.http.models.response._ResultItemT], gfwapiclient.http.models.response._ResultItemT]) -> gfwapiclient.http.models.response._ResultT
      :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint._build_api_result

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint._build_api_result

   .. py:method:: _process_api_status_error(*, response: httpx.Response) -> gfwapiclient.exceptions.http.APIStatusError
      :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint._process_api_status_error

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint._process_api_status_error

   .. py:method:: _cast_api_status_error(*, error_message: str, body: typing.Any, response: httpx.Response) -> gfwapiclient.exceptions.http.APIStatusError
      :canonical: gfwapiclient.http.endpoints.base.BaseEndPoint._cast_api_status_error

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.base.BaseEndPoint._cast_api_status_error
