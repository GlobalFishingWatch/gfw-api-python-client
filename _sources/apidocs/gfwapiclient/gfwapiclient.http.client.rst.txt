:py:mod:`gfwapiclient.http.client`
==================================

.. py:module:: gfwapiclient.http.client

.. autodoc2-docstring:: gfwapiclient.http.client
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`HTTPClient <gfwapiclient.http.client.HTTPClient>`
     - .. autodoc2-docstring:: gfwapiclient.http.client.HTTPClient
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.http.client.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.http.client.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.http.client.__all__
   :value: ['HTTPClient']

   .. autodoc2-docstring:: gfwapiclient.http.client.__all__

.. py:class:: HTTPClient(*, base_url: typing.Optional[typing.Union[str, httpx.URL]] = None, access_token: typing.Optional[str] = None, follow_redirects: typing.Optional[bool] = True, timeout: typing.Optional[float] = 60.0, connect_timeout: typing.Optional[float] = 5.0, max_connections: typing.Optional[int] = 100, max_keepalive_connections: typing.Optional[int] = 20, max_redirects: typing.Optional[int] = 2, **kwargs: typing.Any)
   :canonical: gfwapiclient.http.client.HTTPClient

   Bases: :py:obj:`httpx.AsyncClient`

   .. autodoc2-docstring:: gfwapiclient.http.client.HTTPClient

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.http.client.HTTPClient.__init__

   .. py:property:: user_agent
      :canonical: gfwapiclient.http.client.HTTPClient.user_agent
      :type: str

      .. autodoc2-docstring:: gfwapiclient.http.client.HTTPClient.user_agent

   .. py:property:: auth_headers
      :canonical: gfwapiclient.http.client.HTTPClient.auth_headers
      :type: typing.Dict[str, str]

      .. autodoc2-docstring:: gfwapiclient.http.client.HTTPClient.auth_headers

   .. py:property:: default_headers
      :canonical: gfwapiclient.http.client.HTTPClient.default_headers
      :type: typing.Dict[str, str]

      .. autodoc2-docstring:: gfwapiclient.http.client.HTTPClient.default_headers

   .. py:method:: __aenter__() -> typing.Self
      :canonical: gfwapiclient.http.client.HTTPClient.__aenter__
      :async:

      .. autodoc2-docstring:: gfwapiclient.http.client.HTTPClient.__aenter__

   .. py:method:: __aexit__(exc_type: typing.Optional[typing.Type[BaseException]] = None, exc_value: typing.Optional[BaseException] = None, traceback: typing.Optional[types.TracebackType] = None) -> None
      :canonical: gfwapiclient.http.client.HTTPClient.__aexit__
      :async:

      .. autodoc2-docstring:: gfwapiclient.http.client.HTTPClient.__aexit__
