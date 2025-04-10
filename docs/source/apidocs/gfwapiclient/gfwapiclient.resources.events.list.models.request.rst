:py:mod:`gfwapiclient.resources.events.list.models.request`
===========================================================

.. py:module:: gfwapiclient.resources.events.list.models.request

.. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventListParams <gfwapiclient.resources.events.list.models.request.EventListParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EventListParams
          :summary:
   * - :py:obj:`EventListBody <gfwapiclient.resources.events.list.models.request.EventListBody>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EventListBody
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.list.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.__all__
          :summary:
   * - :py:obj:`EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.events.list.models.request.EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:
   * - :py:obj:`EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.events.list.models.request.EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.list.models.request.__all__
   :value: ['EventListBody', 'EventListParams']

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.__all__

.. py:data:: EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.events.list.models.request.EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Get All Events request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EVENT_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:data:: EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.events.list.models.request.EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Get All Events request body validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EVENT_LIST_REQUEST_BODY_VALIDATION_ERROR_MESSAGE

.. py:class:: EventListParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.list.models.request.EventListParams

   Bases: :py:obj:`gfwapiclient.http.models.RequestParams`

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EventListParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EventListParams.__init__

   .. py:attribute:: limit
      :canonical: gfwapiclient.resources.events.list.models.request.EventListParams.limit
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EventListParams.limit

   .. py:attribute:: offset
      :canonical: gfwapiclient.resources.events.list.models.request.EventListParams.offset
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EventListParams.offset

   .. py:attribute:: sort
      :canonical: gfwapiclient.resources.events.list.models.request.EventListParams.sort
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EventListParams.sort

.. py:class:: EventListBody(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.list.models.request.EventListBody

   Bases: :py:obj:`gfwapiclient.resources.events.base.models.request.EventBaseBody`

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EventListBody

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.models.request.EventListBody.__init__
