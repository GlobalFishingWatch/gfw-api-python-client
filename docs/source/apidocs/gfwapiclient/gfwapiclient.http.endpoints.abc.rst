:py:mod:`gfwapiclient.http.endpoints.abc`
=========================================

.. py:module:: gfwapiclient.http.endpoints.abc

.. autodoc2-docstring:: gfwapiclient.http.endpoints.abc
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AbstractBaseEndPoint <gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.http.endpoints.abc.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.http.endpoints.abc.__all__
   :value: ['AbstractBaseEndPoint']

   .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.__all__

.. py:class:: AbstractBaseEndPoint(*, method: http.HTTPMethod, path: str, request_params: typing.Optional[gfwapiclient.http.models.request._RequestParamsT], request_body: typing.Optional[gfwapiclient.http.models.request._RequestBodyT], result_item_class: typing.Type[gfwapiclient.http.models.response._ResultItemT], result_class: typing.Type[gfwapiclient.http.models.response._ResultT], http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint

   Bases: :py:obj:`abc.ABC`, :py:obj:`typing.Generic`\ [\ :py:obj:`gfwapiclient.http.models.request._RequestParamsT`\ , :py:obj:`gfwapiclient.http.models.request._RequestBodyT`\ , :py:obj:`gfwapiclient.http.models.response._ResultItemT`\ , :py:obj:`gfwapiclient.http.models.response._ResultT`\ ]

   .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint.__init__

   .. py:attribute:: _request_params_class
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._request_params_class
      :type: typing.Type[gfwapiclient.http.models.request._RequestParamsT]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._request_params_class

   .. py:attribute:: _request_body_class
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._request_body_class
      :type: typing.Type[gfwapiclient.http.models.request._RequestBodyT]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._request_body_class

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._result_item_class
      :type: typing.Type[gfwapiclient.http.models.response._ResultItemT]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._result_item_class

   .. py:attribute:: _result_class
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._result_class
      :type: typing.Type[gfwapiclient.http.models.response._ResultT]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._result_class

   .. py:property:: headers
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint.headers
      :type: typing.Dict[str, str]

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint.headers

   .. py:method:: _prepare_request_method() -> str
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_method

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_method

   .. py:method:: _prepare_request_path() -> str
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_path

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_path

   .. py:method:: _prepare_request_url() -> httpx.URL
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_url

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_url

   .. py:method:: _prepare_request_headers() -> httpx.Headers
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_headers

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_headers

   .. py:method:: _prepare_request_query_params() -> typing.Optional[httpx.QueryParams]
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_query_params

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_query_params

   .. py:method:: _prepare_request_json_body() -> typing.Optional[typing.Dict[str, typing.Any]]
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_json_body

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._prepare_request_json_body

   .. py:method:: _build_request() -> httpx.Request
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._build_request

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint._build_request

   .. py:method:: request(**kwargs: typing.Any) -> gfwapiclient.http.models.response._ResultT
      :canonical: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint.request
      :abstractmethod:
      :async:

      .. autodoc2-docstring:: gfwapiclient.http.endpoints.abc.AbstractBaseEndPoint.request
