:py:mod:`gfwapiclient.resources.vessels.base.models.request`
============================================================

.. py:module:: gfwapiclient.resources.vessels.base.models.request

.. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselDataset <gfwapiclient.resources.vessels.base.models.request.VesselDataset>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselDataset
          :summary:
   * - :py:obj:`VesselRegistryInfoData <gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData
          :summary:
   * - :py:obj:`VesselInclude <gfwapiclient.resources.vessels.base.models.request.VesselInclude>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselInclude
          :summary:
   * - :py:obj:`VesselMatchField <gfwapiclient.resources.vessels.base.models.request.VesselMatchField>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselMatchField
          :summary:
   * - :py:obj:`VesselBaseParams <gfwapiclient.resources.vessels.base.models.request.VesselBaseParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseParams
          :summary:
   * - :py:obj:`VesselBaseDetailParams <gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.base.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.base.models.request.__all__
   :value: ['VesselBaseDetailParams', 'VesselBaseParams', 'VesselDataset', 'VesselInclude', 'VesselMatchField',...

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.__all__

.. py:class:: VesselDataset()
   :canonical: gfwapiclient.resources.vessels.base.models.request.VesselDataset

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselDataset

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselDataset.__init__

   .. py:attribute:: VESSEL_IDENTITY_LATEST
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselDataset.VESSEL_IDENTITY_LATEST
      :value: 'public-global-vessel-identity:latest'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselDataset.VESSEL_IDENTITY_LATEST

.. py:class:: VesselRegistryInfoData()
   :canonical: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData.__init__

   .. py:attribute:: NONE
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData.NONE
      :value: 'NONE'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData.NONE

   .. py:attribute:: DELTA
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData.DELTA
      :value: 'DELTA'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData.DELTA

   .. py:attribute:: ALL
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData.ALL
      :value: 'ALL'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData.ALL

.. py:class:: VesselInclude()
   :canonical: gfwapiclient.resources.vessels.base.models.request.VesselInclude

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselInclude

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselInclude.__init__

   .. py:attribute:: POTENTIAL_RELATED_SELF_REPORTED_INFO
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselInclude.POTENTIAL_RELATED_SELF_REPORTED_INFO
      :value: 'POTENTIAL_RELATED_SELF_REPORTED_INFO'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselInclude.POTENTIAL_RELATED_SELF_REPORTED_INFO

.. py:class:: VesselMatchField()
   :canonical: gfwapiclient.resources.vessels.base.models.request.VesselMatchField

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselMatchField

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselMatchField.__init__

   .. py:attribute:: SEVERAL_FIELDS
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselMatchField.SEVERAL_FIELDS
      :value: 'SEVERAL_FIELDS'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselMatchField.SEVERAL_FIELDS

   .. py:attribute:: NO_MATCH
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselMatchField.NO_MATCH
      :value: 'NO_MATCH'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselMatchField.NO_MATCH

   .. py:attribute:: ALL
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselMatchField.ALL
      :value: 'ALL'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselMatchField.ALL

.. py:class:: VesselBaseParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.request.VesselBaseParams

   Bases: :py:obj:`gfwapiclient.http.models.request.RequestParams`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseParams.__init__

   .. py:attribute:: match_fields
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselBaseParams.match_fields
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselMatchField]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseParams.match_fields

   .. py:attribute:: binary
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselBaseParams.binary
      :type: typing.Optional[bool]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseParams.binary

.. py:class:: VesselBaseDetailParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams

   Bases: :py:obj:`gfwapiclient.resources.vessels.base.models.request.VesselBaseParams`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams.__init__

   .. py:attribute:: registries_info_data
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams.registries_info_data
      :type: typing.Optional[gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams.registries_info_data

   .. py:attribute:: includes
      :canonical: gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams.includes
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselInclude]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams.includes
