:py:mod:`gfwapiclient.resources.events.base.models.response`
============================================================

.. py:module:: gfwapiclient.resources.events.base.models.response

.. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventPosition <gfwapiclient.resources.events.base.models.response.EventPosition>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPosition
          :summary:
   * - :py:obj:`EventRegions <gfwapiclient.resources.events.base.models.response.EventRegions>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions
          :summary:
   * - :py:obj:`EventDistances <gfwapiclient.resources.events.base.models.response.EventDistances>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventDistances
          :summary:
   * - :py:obj:`EventVesselPublicAuthorization <gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization
          :summary:
   * - :py:obj:`EventVessel <gfwapiclient.resources.events.base.models.response.EventVessel>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVessel
          :summary:
   * - :py:obj:`EventEncounter <gfwapiclient.resources.events.base.models.response.EventEncounter>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter
          :summary:
   * - :py:obj:`EventFishing <gfwapiclient.resources.events.base.models.response.EventFishing>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventFishing
          :summary:
   * - :py:obj:`Gap <gfwapiclient.resources.events.base.models.response.Gap>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap
          :summary:
   * - :py:obj:`EventLoitering <gfwapiclient.resources.events.base.models.response.EventLoitering>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventLoitering
          :summary:
   * - :py:obj:`EventPortVisitAnchorage <gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage
          :summary:
   * - :py:obj:`EventPortVisit <gfwapiclient.resources.events.base.models.response.EventPortVisit>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisit
          :summary:
   * - :py:obj:`EventItem <gfwapiclient.resources.events.base.models.response.EventItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.base.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.base.models.response.__all__
   :value: ['EventItem']

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.__all__

.. py:class:: EventPosition(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventPosition

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPosition

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPosition.__init__

   .. py:attribute:: lat
      :canonical: gfwapiclient.resources.events.base.models.response.EventPosition.lat
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPosition.lat

   .. py:attribute:: lon
      :canonical: gfwapiclient.resources.events.base.models.response.EventPosition.lon
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPosition.lon

.. py:class:: EventRegions(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventRegions

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.__init__

   .. py:attribute:: mpa
      :canonical: gfwapiclient.resources.events.base.models.response.EventRegions.mpa
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.mpa

   .. py:attribute:: eez
      :canonical: gfwapiclient.resources.events.base.models.response.EventRegions.eez
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.eez

   .. py:attribute:: rfmo
      :canonical: gfwapiclient.resources.events.base.models.response.EventRegions.rfmo
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.rfmo

   .. py:attribute:: fao
      :canonical: gfwapiclient.resources.events.base.models.response.EventRegions.fao
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.fao

   .. py:attribute:: major_fao
      :canonical: gfwapiclient.resources.events.base.models.response.EventRegions.major_fao
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.major_fao

   .. py:attribute:: eez_12_nm
      :canonical: gfwapiclient.resources.events.base.models.response.EventRegions.eez_12_nm
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.eez_12_nm

   .. py:attribute:: high_seas
      :canonical: gfwapiclient.resources.events.base.models.response.EventRegions.high_seas
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.high_seas

   .. py:attribute:: mpa_no_take_partial
      :canonical: gfwapiclient.resources.events.base.models.response.EventRegions.mpa_no_take_partial
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.mpa_no_take_partial

   .. py:attribute:: mpa_no_take
      :canonical: gfwapiclient.resources.events.base.models.response.EventRegions.mpa_no_take
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventRegions.mpa_no_take

.. py:class:: EventDistances(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventDistances

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventDistances

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventDistances.__init__

   .. py:attribute:: start_distance_from_shore_km
      :canonical: gfwapiclient.resources.events.base.models.response.EventDistances.start_distance_from_shore_km
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventDistances.start_distance_from_shore_km

   .. py:attribute:: end_distance_from_shore_km
      :canonical: gfwapiclient.resources.events.base.models.response.EventDistances.end_distance_from_shore_km
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventDistances.end_distance_from_shore_km

   .. py:attribute:: start_distance_from_port_km
      :canonical: gfwapiclient.resources.events.base.models.response.EventDistances.start_distance_from_port_km
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventDistances.start_distance_from_port_km

   .. py:attribute:: end_distance_from_port_km
      :canonical: gfwapiclient.resources.events.base.models.response.EventDistances.end_distance_from_port_km
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventDistances.end_distance_from_port_km

.. py:class:: EventVesselPublicAuthorization(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization.__init__

   .. py:attribute:: has_publicly_listed_authorization
      :canonical: gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization.has_publicly_listed_authorization
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization.has_publicly_listed_authorization

   .. py:attribute:: rfmo
      :canonical: gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization.rfmo
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization.rfmo

.. py:class:: EventVessel(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventVessel

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVessel

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVessel.__init__

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.events.base.models.response.EventVessel.id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVessel.id

   .. py:attribute:: name
      :canonical: gfwapiclient.resources.events.base.models.response.EventVessel.name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVessel.name

   .. py:attribute:: ssvid
      :canonical: gfwapiclient.resources.events.base.models.response.EventVessel.ssvid
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVessel.ssvid

   .. py:attribute:: flag
      :canonical: gfwapiclient.resources.events.base.models.response.EventVessel.flag
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVessel.flag

   .. py:attribute:: type
      :canonical: gfwapiclient.resources.events.base.models.response.EventVessel.type
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVessel.type

   .. py:attribute:: public_authorizations
      :canonical: gfwapiclient.resources.events.base.models.response.EventVessel.public_authorizations
      :type: typing.Optional[typing.List[gfwapiclient.resources.events.base.models.response.EventVesselPublicAuthorization]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventVessel.public_authorizations

.. py:class:: EventEncounter(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventEncounter

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter.__init__

   .. py:attribute:: vessel
      :canonical: gfwapiclient.resources.events.base.models.response.EventEncounter.vessel
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventVessel]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter.vessel

   .. py:attribute:: median_distance_kilometers
      :canonical: gfwapiclient.resources.events.base.models.response.EventEncounter.median_distance_kilometers
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter.median_distance_kilometers

   .. py:attribute:: median_speed_knots
      :canonical: gfwapiclient.resources.events.base.models.response.EventEncounter.median_speed_knots
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter.median_speed_knots

   .. py:attribute:: type
      :canonical: gfwapiclient.resources.events.base.models.response.EventEncounter.type
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter.type

   .. py:attribute:: potential_risk
      :canonical: gfwapiclient.resources.events.base.models.response.EventEncounter.potential_risk
      :type: typing.Optional[bool]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter.potential_risk

   .. py:attribute:: main_vessel_public_authorization_status
      :canonical: gfwapiclient.resources.events.base.models.response.EventEncounter.main_vessel_public_authorization_status
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter.main_vessel_public_authorization_status

   .. py:attribute:: encountered_vessel_public_authorization_status
      :canonical: gfwapiclient.resources.events.base.models.response.EventEncounter.encountered_vessel_public_authorization_status
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventEncounter.encountered_vessel_public_authorization_status

.. py:class:: EventFishing(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventFishing

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventFishing

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventFishing.__init__

   .. py:attribute:: total_distance_km
      :canonical: gfwapiclient.resources.events.base.models.response.EventFishing.total_distance_km
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventFishing.total_distance_km

   .. py:attribute:: average_speed_knots
      :canonical: gfwapiclient.resources.events.base.models.response.EventFishing.average_speed_knots
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventFishing.average_speed_knots

   .. py:attribute:: average_duration_hours
      :canonical: gfwapiclient.resources.events.base.models.response.EventFishing.average_duration_hours
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventFishing.average_duration_hours

   .. py:attribute:: potential_risk
      :canonical: gfwapiclient.resources.events.base.models.response.EventFishing.potential_risk
      :type: typing.Optional[bool]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventFishing.potential_risk

   .. py:attribute:: vessel_public_authorization_status
      :canonical: gfwapiclient.resources.events.base.models.response.EventFishing.vessel_public_authorization_status
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventFishing.vessel_public_authorization_status

.. py:class:: Gap(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.Gap

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap.__init__

   .. py:attribute:: intentional_disabling
      :canonical: gfwapiclient.resources.events.base.models.response.Gap.intentional_disabling
      :type: typing.Optional[bool]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap.intentional_disabling

   .. py:attribute:: distance_km
      :canonical: gfwapiclient.resources.events.base.models.response.Gap.distance_km
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap.distance_km

   .. py:attribute:: duration_hours
      :canonical: gfwapiclient.resources.events.base.models.response.Gap.duration_hours
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap.duration_hours

   .. py:attribute:: implied_speed_knots
      :canonical: gfwapiclient.resources.events.base.models.response.Gap.implied_speed_knots
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap.implied_speed_knots

   .. py:attribute:: positions_12_hours_before_sat
      :canonical: gfwapiclient.resources.events.base.models.response.Gap.positions_12_hours_before_sat
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap.positions_12_hours_before_sat

   .. py:attribute:: positions_per_day_sat_reception
      :canonical: gfwapiclient.resources.events.base.models.response.Gap.positions_per_day_sat_reception
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap.positions_per_day_sat_reception

   .. py:attribute:: off_position
      :canonical: gfwapiclient.resources.events.base.models.response.Gap.off_position
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventPosition]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap.off_position

   .. py:attribute:: on_position
      :canonical: gfwapiclient.resources.events.base.models.response.Gap.on_position
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventPosition]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.Gap.on_position

.. py:class:: EventLoitering(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventLoitering

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventLoitering

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventLoitering.__init__

   .. py:attribute:: total_time_hours
      :canonical: gfwapiclient.resources.events.base.models.response.EventLoitering.total_time_hours
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventLoitering.total_time_hours

   .. py:attribute:: total_distance_km
      :canonical: gfwapiclient.resources.events.base.models.response.EventLoitering.total_distance_km
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventLoitering.total_distance_km

   .. py:attribute:: average_speed_knots
      :canonical: gfwapiclient.resources.events.base.models.response.EventLoitering.average_speed_knots
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventLoitering.average_speed_knots

   .. py:attribute:: average_distance_from_shore_km
      :canonical: gfwapiclient.resources.events.base.models.response.EventLoitering.average_distance_from_shore_km
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventLoitering.average_distance_from_shore_km

.. py:class:: EventPortVisitAnchorage(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.__init__

   .. py:attribute:: anchorage_id
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.anchorage_id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.anchorage_id

   .. py:attribute:: at_dock
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.at_dock
      :type: typing.Optional[bool]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.at_dock

   .. py:attribute:: distance_from_shore_km
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.distance_from_shore_km
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.distance_from_shore_km

   .. py:attribute:: flag
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.flag
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.flag

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.id

   .. py:attribute:: lat
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.lat
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.lat

   .. py:attribute:: lon
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.lon
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.lon

   .. py:attribute:: name
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.name

   .. py:attribute:: top_destination
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.top_destination
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage.top_destination

.. py:class:: EventPortVisit(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisit

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisit

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisit.__init__

   .. py:attribute:: visit_id
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisit.visit_id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisit.visit_id

   .. py:attribute:: confidence
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisit.confidence
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisit.confidence

   .. py:attribute:: duration_hrs
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisit.duration_hrs
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisit.duration_hrs

   .. py:attribute:: start_anchorage
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisit.start_anchorage
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisit.start_anchorage

   .. py:attribute:: intermediate_anchorage
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisit.intermediate_anchorage
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisit.intermediate_anchorage

   .. py:attribute:: end_anchorage
      :canonical: gfwapiclient.resources.events.base.models.response.EventPortVisit.end_anchorage
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventPortVisitAnchorage]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventPortVisit.end_anchorage

.. py:class:: EventItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.response.EventItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.__init__

   .. py:attribute:: start
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.start
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.start

   .. py:attribute:: end
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.end
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.end

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.id

   .. py:attribute:: type
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.type
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.type

   .. py:attribute:: position
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.position
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventPosition]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.position

   .. py:attribute:: regions
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.regions
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventRegions]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.regions

   .. py:attribute:: bounding_box
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.bounding_box
      :type: typing.Optional[typing.List[float]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.bounding_box

   .. py:attribute:: distances
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.distances
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventDistances]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.distances

   .. py:attribute:: vessel
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.vessel
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventVessel]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.vessel

   .. py:attribute:: encounter
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.encounter
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventEncounter]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.encounter

   .. py:attribute:: fishing
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.fishing
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventFishing]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.fishing

   .. py:attribute:: gap
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.gap
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.Gap]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.gap

   .. py:attribute:: loitering
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.loitering
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventLoitering]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.loitering

   .. py:attribute:: port_visit
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.port_visit
      :type: typing.Optional[gfwapiclient.resources.events.base.models.response.EventPortVisit]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.port_visit

   .. py:method:: empty_datetime_str_to_none(value: typing.Any) -> typing.Optional[typing.Any]
      :canonical: gfwapiclient.resources.events.base.models.response.EventItem.empty_datetime_str_to_none
      :classmethod:

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.response.EventItem.empty_datetime_str_to_none
