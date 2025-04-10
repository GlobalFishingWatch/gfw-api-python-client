:py:mod:`gfwapiclient.exceptions.base`
======================================

.. py:module:: gfwapiclient.exceptions.base

.. autodoc2-docstring:: gfwapiclient.exceptions.base
   :allowtitles:

Module Contents
---------------

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.exceptions.base.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.base.__all__
          :summary:
   * - :py:obj:`GFW_API_CLIENT_ERROR_MESSAGE <gfwapiclient.exceptions.base.GFW_API_CLIENT_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.base.GFW_API_CLIENT_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.exceptions.base.__all__
   :value: ['GFWAPIClientError']

   .. autodoc2-docstring:: gfwapiclient.exceptions.base.__all__

.. py:data:: GFW_API_CLIENT_ERROR_MESSAGE
   :canonical: gfwapiclient.exceptions.base.GFW_API_CLIENT_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'An error occurred.'

   .. autodoc2-docstring:: gfwapiclient.exceptions.base.GFW_API_CLIENT_ERROR_MESSAGE

.. py:exception:: GFWAPIClientError(message: typing.Optional[str] = None)
   :canonical: gfwapiclient.exceptions.base.GFWAPIClientError

   Bases: :py:obj:`Exception`

   .. autodoc2-docstring:: gfwapiclient.exceptions.base.GFWAPIClientError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.base.GFWAPIClientError.__init__

   .. py:method:: __str__() -> str
      :canonical: gfwapiclient.exceptions.base.GFWAPIClientError.__str__

      .. autodoc2-docstring:: gfwapiclient.exceptions.base.GFWAPIClientError.__str__

   .. py:method:: __repr__() -> str
      :canonical: gfwapiclient.exceptions.base.GFWAPIClientError.__repr__

      .. autodoc2-docstring:: gfwapiclient.exceptions.base.GFWAPIClientError.__repr__
