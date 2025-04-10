:py:mod:`gfwapiclient.resources.vessels.base.models.response`
=============================================================

.. py:module:: gfwapiclient.resources.vessels.base.models.response

.. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ExtraField <gfwapiclient.resources.vessels.base.models.response.ExtraField>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField
          :summary:
   * - :py:obj:`RegistryInfo <gfwapiclient.resources.vessels.base.models.response.RegistryInfo>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo
          :summary:
   * - :py:obj:`RegistryOwner <gfwapiclient.resources.vessels.base.models.response.RegistryOwner>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryOwner
          :summary:
   * - :py:obj:`RegistryPublicAuthorization <gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization
          :summary:
   * - :py:obj:`GearType <gfwapiclient.resources.vessels.base.models.response.GearType>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.GearType
          :summary:
   * - :py:obj:`ShipType <gfwapiclient.resources.vessels.base.models.response.ShipType>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ShipType
          :summary:
   * - :py:obj:`CombinedSourceInfo <gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo
          :summary:
   * - :py:obj:`SelfReportedInfo <gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo
          :summary:
   * - :py:obj:`VesselItem <gfwapiclient.resources.vessels.base.models.response.VesselItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.base.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.base.models.response.__all__
   :value: ['VesselItem']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.__all__

.. py:class:: ExtraField(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.response.ExtraField

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField.__init__

   .. py:attribute:: registry_source
      :canonical: gfwapiclient.resources.vessels.base.models.response.ExtraField.registry_source
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField.registry_source

   .. py:attribute:: iuu_status
      :canonical: gfwapiclient.resources.vessels.base.models.response.ExtraField.iuu_status
      :type: typing.Optional[typing.Any]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField.iuu_status

   .. py:attribute:: has_compliance_info
      :canonical: gfwapiclient.resources.vessels.base.models.response.ExtraField.has_compliance_info
      :type: typing.Optional[typing.Any]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField.has_compliance_info

   .. py:attribute:: images
      :canonical: gfwapiclient.resources.vessels.base.models.response.ExtraField.images
      :type: typing.Optional[typing.Any]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField.images

   .. py:attribute:: operator
      :canonical: gfwapiclient.resources.vessels.base.models.response.ExtraField.operator
      :type: typing.Optional[typing.Any]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField.operator

   .. py:attribute:: built_year
      :canonical: gfwapiclient.resources.vessels.base.models.response.ExtraField.built_year
      :type: typing.Optional[typing.Any]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField.built_year

   .. py:attribute:: depth_m
      :canonical: gfwapiclient.resources.vessels.base.models.response.ExtraField.depth_m
      :type: typing.Optional[typing.Any]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ExtraField.depth_m

.. py:class:: RegistryInfo(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.__init__

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.id

   .. py:attribute:: source_code
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.source_code
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.source_code

   .. py:attribute:: ssvid
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.ssvid
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.ssvid

   .. py:attribute:: flag
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.flag
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.flag

   .. py:attribute:: ship_name
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.ship_name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.ship_name

   .. py:attribute:: n_ship_name
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.n_ship_name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.n_ship_name

   .. py:attribute:: call_sign
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.call_sign
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.call_sign

   .. py:attribute:: imo
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.imo
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.imo

   .. py:attribute:: latest_vessel_info
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.latest_vessel_info
      :type: typing.Optional[bool]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.latest_vessel_info

   .. py:attribute:: transmission_date_from
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.transmission_date_from
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.transmission_date_from

   .. py:attribute:: transmission_date_to
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.transmission_date_to
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.transmission_date_to

   .. py:attribute:: gear_types
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.gear_types
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.gear_types

   .. py:attribute:: length_m
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.length_m
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.length_m

   .. py:attribute:: tonnage_gt
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.tonnage_gt
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.tonnage_gt

   .. py:attribute:: vessel_info_reference
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.vessel_info_reference
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.vessel_info_reference

   .. py:attribute:: extra_fields
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.extra_fields
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.response.ExtraField]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryInfo.extra_fields

.. py:class:: RegistryOwner(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryOwner

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryOwner

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.__init__

   .. py:attribute:: name
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.name

   .. py:attribute:: flag
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.flag
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.flag

   .. py:attribute:: ssvid
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.ssvid
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.ssvid

   .. py:attribute:: source_code
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.source_code
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.source_code

   .. py:attribute:: date_from
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.date_from
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.date_from

   .. py:attribute:: date_to
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.date_to
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryOwner.date_to

.. py:class:: RegistryPublicAuthorization(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization.__init__

   .. py:attribute:: date_from
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization.date_from
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization.date_from

   .. py:attribute:: date_to
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization.date_to
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization.date_to

   .. py:attribute:: ssvid
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization.ssvid
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization.ssvid

   .. py:attribute:: source_code
      :canonical: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization.source_code
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization.source_code

.. py:class:: GearType(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.response.GearType

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.GearType

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.GearType.__init__

   .. py:attribute:: name
      :canonical: gfwapiclient.resources.vessels.base.models.response.GearType.name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.GearType.name

   .. py:attribute:: source
      :canonical: gfwapiclient.resources.vessels.base.models.response.GearType.source
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.GearType.source

   .. py:attribute:: year_from
      :canonical: gfwapiclient.resources.vessels.base.models.response.GearType.year_from
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.GearType.year_from

   .. py:attribute:: year_to
      :canonical: gfwapiclient.resources.vessels.base.models.response.GearType.year_to
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.GearType.year_to

.. py:class:: ShipType(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.response.ShipType

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ShipType

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ShipType.__init__

   .. py:attribute:: name
      :canonical: gfwapiclient.resources.vessels.base.models.response.ShipType.name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ShipType.name

   .. py:attribute:: source
      :canonical: gfwapiclient.resources.vessels.base.models.response.ShipType.source
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ShipType.source

   .. py:attribute:: year_from
      :canonical: gfwapiclient.resources.vessels.base.models.response.ShipType.year_from
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ShipType.year_from

   .. py:attribute:: year_to
      :canonical: gfwapiclient.resources.vessels.base.models.response.ShipType.year_to
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.ShipType.year_to

.. py:class:: CombinedSourceInfo(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo.__init__

   .. py:attribute:: vessel_id
      :canonical: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo.vessel_id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo.vessel_id

   .. py:attribute:: gear_types
      :canonical: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo.gear_types
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.response.GearType]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo.gear_types

   .. py:attribute:: ship_types
      :canonical: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo.ship_types
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.response.ShipType]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo.ship_types

.. py:class:: SelfReportedInfo(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.__init__

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.id

   .. py:attribute:: ssvid
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.ssvid
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.ssvid

   .. py:attribute:: ship_name
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.ship_name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.ship_name

   .. py:attribute:: n_ship_name
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.n_ship_name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.n_ship_name

   .. py:attribute:: flag
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.flag
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.flag

   .. py:attribute:: call_sign
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.call_sign
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.call_sign

   .. py:attribute:: imo
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.imo
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.imo

   .. py:attribute:: messages_counter
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.messages_counter
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.messages_counter

   .. py:attribute:: positions_counter
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.positions_counter
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.positions_counter

   .. py:attribute:: source_code
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.source_code
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.source_code

   .. py:attribute:: match_fields
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.match_fields
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.match_fields

   .. py:attribute:: transmission_date_from
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.transmission_date_from
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.transmission_date_from

   .. py:attribute:: transmission_date_to
      :canonical: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.transmission_date_to
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo.transmission_date_to

.. py:class:: VesselItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.base.models.response.VesselItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem.__init__

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.vessels.base.models.response.VesselItem.dataset
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem.dataset

   .. py:attribute:: registry_info_total_records
      :canonical: gfwapiclient.resources.vessels.base.models.response.VesselItem.registry_info_total_records
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem.registry_info_total_records

   .. py:attribute:: registry_info
      :canonical: gfwapiclient.resources.vessels.base.models.response.VesselItem.registry_info
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.response.RegistryInfo]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem.registry_info

   .. py:attribute:: registry_owners
      :canonical: gfwapiclient.resources.vessels.base.models.response.VesselItem.registry_owners
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.response.RegistryOwner]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem.registry_owners

   .. py:attribute:: registry_public_authorizations
      :canonical: gfwapiclient.resources.vessels.base.models.response.VesselItem.registry_public_authorizations
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.response.RegistryPublicAuthorization]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem.registry_public_authorizations

   .. py:attribute:: combined_sources_info
      :canonical: gfwapiclient.resources.vessels.base.models.response.VesselItem.combined_sources_info
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.response.CombinedSourceInfo]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem.combined_sources_info

   .. py:attribute:: self_reported_info
      :canonical: gfwapiclient.resources.vessels.base.models.response.VesselItem.self_reported_info
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.response.SelfReportedInfo]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.base.models.response.VesselItem.self_reported_info
