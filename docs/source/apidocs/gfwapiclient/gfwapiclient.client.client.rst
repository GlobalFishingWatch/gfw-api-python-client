:py:mod:`gfwapiclient.client.client`
====================================

.. py:module:: gfwapiclient.client.client

.. autodoc2-docstring:: gfwapiclient.client.client
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Client <gfwapiclient.client.client.Client>`
     - .. autodoc2-docstring:: gfwapiclient.client.client.Client
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.client.client.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.client.client.__all__
          :summary:
   * - :py:obj:`GFW_API_BASE_URL <gfwapiclient.client.client.GFW_API_BASE_URL>`
     - .. autodoc2-docstring:: gfwapiclient.client.client.GFW_API_BASE_URL
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.client.client.__all__
   :value: ['Client']

   .. autodoc2-docstring:: gfwapiclient.client.client.__all__

.. py:data:: GFW_API_BASE_URL
   :canonical: gfwapiclient.client.client.GFW_API_BASE_URL
   :type: typing.Final[str]
   :value: 'https://gateway.api.globalfishingwatch.org/v3/'

   .. autodoc2-docstring:: gfwapiclient.client.client.GFW_API_BASE_URL

.. py:class:: Client(*, access_token: typing.Optional[str] = None, base_url: typing.Optional[str] = None, follow_redirects: typing.Optional[bool] = True, timeout: typing.Optional[float] = 60.0, connect_timeout: typing.Optional[float] = 5.0, max_connections: typing.Optional[int] = 100, max_keepalive_connections: typing.Optional[int] = 20, max_redirects: typing.Optional[int] = 2, **kwargs: typing.Any)
   :canonical: gfwapiclient.client.client.Client

   .. autodoc2-docstring:: gfwapiclient.client.client.Client

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.client.client.Client.__init__

   .. py:attribute:: _fourwings
      :canonical: gfwapiclient.client.client.Client._fourwings
      :type: gfwapiclient.resources.FourWingsResource
      :value: None

      .. autodoc2-docstring:: gfwapiclient.client.client.Client._fourwings

   .. py:attribute:: _vessels
      :canonical: gfwapiclient.client.client.Client._vessels
      :type: gfwapiclient.resources.VesselResource
      :value: None

      .. autodoc2-docstring:: gfwapiclient.client.client.Client._vessels

   .. py:attribute:: _events
      :canonical: gfwapiclient.client.client.Client._events
      :type: gfwapiclient.resources.EventResource
      :value: None

      .. autodoc2-docstring:: gfwapiclient.client.client.Client._events

   .. py:attribute:: _insights
      :canonical: gfwapiclient.client.client.Client._insights
      :type: gfwapiclient.resources.InsightResource
      :value: None

      .. autodoc2-docstring:: gfwapiclient.client.client.Client._insights

   .. py:attribute:: _datasets
      :canonical: gfwapiclient.client.client.Client._datasets
      :type: gfwapiclient.resources.DatasetResource
      :value: None

      .. autodoc2-docstring:: gfwapiclient.client.client.Client._datasets

   .. py:attribute:: _references
      :canonical: gfwapiclient.client.client.Client._references
      :type: gfwapiclient.resources.ReferenceResource
      :value: None

      .. autodoc2-docstring:: gfwapiclient.client.client.Client._references

   .. py:property:: fourwings
      :canonical: gfwapiclient.client.client.Client.fourwings
      :type: gfwapiclient.resources.FourWingsResource

      .. autodoc2-docstring:: gfwapiclient.client.client.Client.fourwings

   .. py:property:: vessels
      :canonical: gfwapiclient.client.client.Client.vessels
      :type: gfwapiclient.resources.VesselResource

      .. autodoc2-docstring:: gfwapiclient.client.client.Client.vessels

   .. py:property:: events
      :canonical: gfwapiclient.client.client.Client.events
      :type: gfwapiclient.resources.EventResource

      .. autodoc2-docstring:: gfwapiclient.client.client.Client.events

   .. py:property:: insights
      :canonical: gfwapiclient.client.client.Client.insights
      :type: gfwapiclient.resources.InsightResource

      .. autodoc2-docstring:: gfwapiclient.client.client.Client.insights

   .. py:property:: datasets
      :canonical: gfwapiclient.client.client.Client.datasets
      :type: gfwapiclient.resources.DatasetResource

      .. autodoc2-docstring:: gfwapiclient.client.client.Client.datasets

   .. py:property:: references
      :canonical: gfwapiclient.client.client.Client.references
      :type: gfwapiclient.resources.ReferenceResource

      .. autodoc2-docstring:: gfwapiclient.client.client.Client.references
