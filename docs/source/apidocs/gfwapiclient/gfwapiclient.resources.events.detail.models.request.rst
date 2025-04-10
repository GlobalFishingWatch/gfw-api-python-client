:py:mod:`gfwapiclient.resources.events.detail.models.request`
=============================================================

.. py:module:: gfwapiclient.resources.events.detail.models.request

.. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventDetailParams <gfwapiclient.resources.events.detail.models.request.EventDetailParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.request.EventDetailParams
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.detail.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.request.__all__
          :summary:
   * - :py:obj:`EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.events.detail.models.request.EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.request.EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.detail.models.request.__all__
   :value: ['EventDetailParams']

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.request.__all__

.. py:data:: EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.events.detail.models.request.EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Get one by Event ID request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.request.EVENT_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:class:: EventDetailParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.detail.models.request.EventDetailParams

   Bases: :py:obj:`gfwapiclient.http.models.RequestParams`

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.request.EventDetailParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.request.EventDetailParams.__init__

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.events.detail.models.request.EventDetailParams.dataset
      :type: gfwapiclient.resources.events.base.models.request.EventDataset
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.detail.models.request.EventDetailParams.dataset
