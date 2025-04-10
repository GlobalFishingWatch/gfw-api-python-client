:py:mod:`gfwapiclient.exceptions.client`
========================================

.. py:module:: gfwapiclient.exceptions.client

.. autodoc2-docstring:: gfwapiclient.exceptions.client
   :allowtitles:

Module Contents
---------------

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.exceptions.client.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.client.__all__
          :summary:
   * - :py:obj:`BASE_URL_ERROR_MESSAGE <gfwapiclient.exceptions.client.BASE_URL_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.client.BASE_URL_ERROR_MESSAGE
          :summary:
   * - :py:obj:`ACCESS_TOKEN_ERROR_MESSAGE <gfwapiclient.exceptions.client.ACCESS_TOKEN_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.client.ACCESS_TOKEN_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.exceptions.client.__all__
   :value: ['AccessTokenError', 'BaseUrlError']

   .. autodoc2-docstring:: gfwapiclient.exceptions.client.__all__

.. py:data:: BASE_URL_ERROR_MESSAGE
   :canonical: gfwapiclient.exceptions.client.BASE_URL_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'The `base_url` must be provided either as an argument or set via the `GFW_API_BASE_URL` environment ...'

   .. autodoc2-docstring:: gfwapiclient.exceptions.client.BASE_URL_ERROR_MESSAGE

.. py:data:: ACCESS_TOKEN_ERROR_MESSAGE
   :canonical: gfwapiclient.exceptions.client.ACCESS_TOKEN_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'The `access_token` must be provided either as an argument or set via the `GFW_API_ACCESS_TOKEN` envi...'

   .. autodoc2-docstring:: gfwapiclient.exceptions.client.ACCESS_TOKEN_ERROR_MESSAGE

.. py:exception:: BaseUrlError()
   :canonical: gfwapiclient.exceptions.client.BaseUrlError

   Bases: :py:obj:`gfwapiclient.exceptions.base.GFWAPIClientError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.client.BaseUrlError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.client.BaseUrlError.__init__

.. py:exception:: AccessTokenError()
   :canonical: gfwapiclient.exceptions.client.AccessTokenError

   Bases: :py:obj:`gfwapiclient.exceptions.base.GFWAPIClientError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.client.AccessTokenError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.client.AccessTokenError.__init__
