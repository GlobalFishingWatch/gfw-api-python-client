:py:mod:`gfwapiclient.exceptions.http`
======================================

.. py:module:: gfwapiclient.exceptions.http

.. autodoc2-docstring:: gfwapiclient.exceptions.http
   :allowtitles:

Module Contents
---------------

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.exceptions.http.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.http.__all__
          :summary:
   * - :py:obj:`API_CONNECTION_ERROR_MESSAGE <gfwapiclient.exceptions.http.API_CONNECTION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.http.API_CONNECTION_ERROR_MESSAGE
          :summary:
   * - :py:obj:`API_TIMEOUT_ERROR_MESSAGE <gfwapiclient.exceptions.http.API_TIMEOUT_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.http.API_TIMEOUT_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.exceptions.http.__all__
   :value: ['APIConnectionError', 'APIError', 'APIStatusError', 'APITimeoutError', 'AuthenticationError', 'BadG...

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.__all__

.. py:data:: API_CONNECTION_ERROR_MESSAGE
   :canonical: gfwapiclient.exceptions.http.API_CONNECTION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Connection error.'

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.API_CONNECTION_ERROR_MESSAGE

.. py:data:: API_TIMEOUT_ERROR_MESSAGE
   :canonical: gfwapiclient.exceptions.http.API_TIMEOUT_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Request timed out.'

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.API_TIMEOUT_ERROR_MESSAGE

.. py:exception:: APIError(message: str, request: httpx.Request, *, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.APIError

   Bases: :py:obj:`gfwapiclient.exceptions.base.GFWAPIClientError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIError.__init__

   .. py:attribute:: request
      :canonical: gfwapiclient.exceptions.http.APIError.request
      :type: httpx.Request
      :value: None

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIError.request

   .. py:attribute:: body
      :canonical: gfwapiclient.exceptions.http.APIError.body
      :type: typing.Optional[typing.Any]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIError.body

   .. py:method:: __str__() -> str
      :canonical: gfwapiclient.exceptions.http.APIError.__str__

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIError.__str__

   .. py:method:: __repr__() -> str
      :canonical: gfwapiclient.exceptions.http.APIError.__repr__

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIError.__repr__

.. py:exception:: APIStatusError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.APIStatusError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIStatusError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIStatusError.__init__

   .. py:attribute:: response
      :canonical: gfwapiclient.exceptions.http.APIStatusError.response
      :type: httpx.Response
      :value: None

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIStatusError.response

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.APIStatusError.status_code
      :type: int
      :value: None

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIStatusError.status_code

   .. py:method:: __repr__() -> str
      :canonical: gfwapiclient.exceptions.http.APIStatusError.__repr__

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIStatusError.__repr__

.. py:exception:: APIConnectionError(*, message: str = API_CONNECTION_ERROR_MESSAGE, request: httpx.Request)
   :canonical: gfwapiclient.exceptions.http.APIConnectionError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIConnectionError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.APIConnectionError.__init__

.. py:exception:: APITimeoutError(request: httpx.Request)
   :canonical: gfwapiclient.exceptions.http.APITimeoutError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIConnectionError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.APITimeoutError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.APITimeoutError.__init__

.. py:exception:: BadRequestError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.BadRequestError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.BadRequestError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.BadRequestError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.BadRequestError.status_code
      :type: typing.Literal[400]
      :value: 400

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.BadRequestError.status_code

.. py:exception:: AuthenticationError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.AuthenticationError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.AuthenticationError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.AuthenticationError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.AuthenticationError.status_code
      :type: typing.Literal[401]
      :value: 401

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.AuthenticationError.status_code

.. py:exception:: PermissionDeniedError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.PermissionDeniedError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.PermissionDeniedError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.PermissionDeniedError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.PermissionDeniedError.status_code
      :type: typing.Literal[403]
      :value: 403

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.PermissionDeniedError.status_code

.. py:exception:: NotFoundError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.NotFoundError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.NotFoundError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.NotFoundError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.NotFoundError.status_code
      :type: typing.Literal[404]
      :value: 404

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.NotFoundError.status_code

.. py:exception:: RequestTimeoutError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.RequestTimeoutError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.RequestTimeoutError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.RequestTimeoutError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.RequestTimeoutError.status_code
      :type: typing.Literal[408]
      :value: 408

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.RequestTimeoutError.status_code

.. py:exception:: ConflictError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.ConflictError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.ConflictError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.ConflictError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.ConflictError.status_code
      :type: typing.Literal[409]
      :value: 409

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.ConflictError.status_code

.. py:exception:: UnprocessableEntityError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.UnprocessableEntityError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.UnprocessableEntityError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.UnprocessableEntityError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.UnprocessableEntityError.status_code
      :type: typing.Literal[422]
      :value: 422

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.UnprocessableEntityError.status_code

.. py:exception:: RateLimitError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.RateLimitError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.RateLimitError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.RateLimitError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.RateLimitError.status_code
      :type: typing.Literal[429]
      :value: 429

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.RateLimitError.status_code

.. py:exception:: InternalServerError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.InternalServerError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.InternalServerError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.InternalServerError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.InternalServerError.status_code
      :type: typing.Literal[500]
      :value: 500

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.InternalServerError.status_code

.. py:exception:: BadGatewayError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.BadGatewayError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.BadGatewayError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.BadGatewayError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.BadGatewayError.status_code
      :type: typing.Literal[502]
      :value: 502

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.BadGatewayError.status_code

.. py:exception:: ServiceUnavailableError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.ServiceUnavailableError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.ServiceUnavailableError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.ServiceUnavailableError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.ServiceUnavailableError.status_code
      :type: typing.Literal[503]
      :value: 503

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.ServiceUnavailableError.status_code

.. py:exception:: GatewayTimeoutError(message: str, *, response: httpx.Response, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.http.GatewayTimeoutError

   Bases: :py:obj:`gfwapiclient.exceptions.http.APIStatusError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.GatewayTimeoutError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.http.GatewayTimeoutError.__init__

   .. py:attribute:: status_code
      :canonical: gfwapiclient.exceptions.http.GatewayTimeoutError.status_code
      :type: typing.Literal[504]
      :value: 504

      .. autodoc2-docstring:: gfwapiclient.exceptions.http.GatewayTimeoutError.status_code
