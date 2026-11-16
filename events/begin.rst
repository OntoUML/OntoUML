.. _begin:

begin
=====

«begin» is a property stereotype. On each concrete individual in the extension of the owning class, the value is the instant at which that individual begins to exist.

- For an endurant, it is the instant the endurant comes into existence.
- For an event, it is the instant the event starts to occur.
- For a situation, it is the instant the situation begins to obtain.

The datatype is chosen by the model and reflects the temporal granularity it needs. Begin points are immutable. When existence is instantaneous, as for a punctual event, one attribute may carry both «begin» and :ref:`end`.

Examples are ``kickOff`` of Soccer Match, ``dateOfBirth`` of Person, and ``instant`` of an instantaneous Payment.

.. figure:: /specification-figures/begin.svg
   :alt: A begin attribute on an event
   :width: 60%
   :align: center

   A property categorized as «begin».

.. figure:: /specification-figures/event-properties.svg
   :alt: Profile diagram of event property stereotypes
   :width: 40%
   :align: center

   Event property stereotypes.

Constraints
-----------

- The property is owned by a class of concrete individuals. ``restrictedTo`` is non-empty and excludes ``type`` and ``abstract``.
- The property is read-only.
- The property is typed by a datatype that represents a temporal value space.
