.. _end:

end
===

«end» is a property stereotype. On each concrete individual in the extension of the owning class, the value is the instant at which that individual ceases to exist.

- For an endurant, it is the instant the endurant ceases to exist.
- For an event, it is the instant the event finishes occurring.
- For a situation, it is the instant the situation ceases to obtain.

An end point does not precede the corresponding begin point. Once acquired, it is immutable. A currently existing endurant has no end point yet, so an «end» attribute on an endurant class has lower-bound multiplicity zero. An attribute stereotyped with both :ref:`begin` and «end» represents individuals whose begin and end points coincide.

Examples are ``finalWhistle`` of Soccer Match, ``dateOfDeath`` of Person, and ``instant`` of an instantaneous Payment.

.. figure:: /specification-figures/end.svg
   :alt: An end attribute on an event
   :width: 60%
   :align: center

   A property categorized as «end».

Constraints
-----------

- The property is owned by a class of concrete individuals. ``restrictedTo`` is non-empty and excludes ``type`` and ``abstract``.
- The property is typed by a datatype that represents a temporal value space.
