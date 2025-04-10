:py:mod:`gfwapiclient.exceptions.validation`
============================================

.. py:module:: gfwapiclient.exceptions.validation

.. autodoc2-docstring:: gfwapiclient.exceptions.validation
   :allowtitles:

Module Contents
---------------

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.exceptions.validation.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.validation.__all__
          :summary:
   * - :py:obj:`MODEL_VALIDATION_ERROR_MESSAGE <gfwapiclient.exceptions.validation.MODEL_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.validation.MODEL_VALIDATION_ERROR_MESSAGE
          :summary:
   * - :py:obj:`REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.exceptions.validation.REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.validation.REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:
   * - :py:obj:`REQUEST_BODY_VALIDATION_ERROR_MESSAGE <gfwapiclient.exceptions.validation.REQUEST_BODY_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.validation.REQUEST_BODY_VALIDATION_ERROR_MESSAGE
          :summary:
   * - :py:obj:`RESULT_ITEM_VALIDATION_ERROR_MESSAGE <gfwapiclient.exceptions.validation.RESULT_ITEM_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.exceptions.validation.RESULT_ITEM_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.exceptions.validation.__all__
   :value: ['ModelValidationError', 'RequestBodyValidationError', 'RequestParamsValidationError', 'ResultItemVa...

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.__all__

.. py:data:: MODEL_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.exceptions.validation.MODEL_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Model validation failed.'

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.MODEL_VALIDATION_ERROR_MESSAGE

.. py:data:: REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.exceptions.validation.REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:data:: REQUEST_BODY_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.exceptions.validation.REQUEST_BODY_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Request body validation failed.'

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.REQUEST_BODY_VALIDATION_ERROR_MESSAGE

.. py:data:: RESULT_ITEM_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.exceptions.validation.RESULT_ITEM_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Result item validation failed.'

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.RESULT_ITEM_VALIDATION_ERROR_MESSAGE

.. py:exception:: ModelValidationError(*, message: typing.Optional[str] = None, error: typing.Optional[pydantic_core.ValidationError] = None)
   :canonical: gfwapiclient.exceptions.validation.ModelValidationError

   Bases: :py:obj:`gfwapiclient.exceptions.base.GFWAPIClientError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ModelValidationError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ModelValidationError.__init__

   .. py:attribute:: error
      :canonical: gfwapiclient.exceptions.validation.ModelValidationError.error
      :type: typing.Optional[pydantic_core.ValidationError]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ModelValidationError.error

   .. py:method:: __str__() -> str
      :canonical: gfwapiclient.exceptions.validation.ModelValidationError.__str__

      .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ModelValidationError.__str__

   .. py:method:: __repr__() -> str
      :canonical: gfwapiclient.exceptions.validation.ModelValidationError.__repr__

      .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ModelValidationError.__repr__

.. py:exception:: RequestParamsValidationError(*, message: typing.Optional[str] = None, error: typing.Optional[pydantic_core.ValidationError] = None)
   :canonical: gfwapiclient.exceptions.validation.RequestParamsValidationError

   Bases: :py:obj:`gfwapiclient.exceptions.validation.ModelValidationError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.RequestParamsValidationError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.RequestParamsValidationError.__init__

.. py:exception:: RequestBodyValidationError(*, message: typing.Optional[str] = None, error: typing.Optional[pydantic_core.ValidationError] = None)
   :canonical: gfwapiclient.exceptions.validation.RequestBodyValidationError

   Bases: :py:obj:`gfwapiclient.exceptions.validation.ModelValidationError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.RequestBodyValidationError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.RequestBodyValidationError.__init__

.. py:exception:: ResultItemValidationError(*, error: typing.Optional[pydantic_core.ValidationError] = None, response: typing.Optional[httpx.Response] = None, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.validation.ResultItemValidationError

   Bases: :py:obj:`gfwapiclient.exceptions.validation.ModelValidationError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultItemValidationError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultItemValidationError.__init__

   .. py:attribute:: response
      :canonical: gfwapiclient.exceptions.validation.ResultItemValidationError.response
      :type: typing.Optional[httpx.Response]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultItemValidationError.response

   .. py:attribute:: body
      :canonical: gfwapiclient.exceptions.validation.ResultItemValidationError.body
      :type: typing.Optional[typing.Any]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultItemValidationError.body

   .. py:method:: __str__() -> str
      :canonical: gfwapiclient.exceptions.validation.ResultItemValidationError.__str__

      .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultItemValidationError.__str__

   .. py:method:: __repr__() -> str
      :canonical: gfwapiclient.exceptions.validation.ResultItemValidationError.__repr__

      .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultItemValidationError.__repr__

.. py:exception:: ResultValidationError(*, message: typing.Optional[str] = None, error: typing.Optional[pydantic_core.ValidationError] = None, response: typing.Optional[httpx.Response] = None, body: typing.Optional[typing.Any] = None)
   :canonical: gfwapiclient.exceptions.validation.ResultValidationError

   Bases: :py:obj:`gfwapiclient.exceptions.validation.ModelValidationError`

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultValidationError

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultValidationError.__init__

   .. py:method:: __str__() -> str
      :canonical: gfwapiclient.exceptions.validation.ResultValidationError.__str__

      .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultValidationError.__str__

   .. py:method:: __repr__() -> str
      :canonical: gfwapiclient.exceptions.validation.ResultValidationError.__repr__

      .. autodoc2-docstring:: gfwapiclient.exceptions.validation.ResultValidationError.__repr__
