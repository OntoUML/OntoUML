.. _change:

Change
======

«change» is a :ref:`participation` whose instances connect an event to an endurant that changes because of the event: the endurant acquires or loses properties as a result.

Creation and termination mark the boundaries of an endurant's existence. A change presupposes that the endurant exists both before and after the event. The event marks a transition between states. That transition may be a change in attribute values, in the aspects that inhere in the endurant, or in the phases it instantiates. A promotion changes an employee, who thereafter instantiates Senior Employee.

A repainting changes the color of a car. A legislation amendment changes a piece of legislation. A medical treatment changes a patient.

.. figure:: /specification-figures/change.svg
   :alt: A repainting changing the color of a car
   :width: 80%
   :align: center

   Associations categorized as «change».

Allowed ends
------------

- **Event end.** A class restricted exactly to ``{event}``.
- **Changed end.** A class of endurants. ``restrictedTo`` is a non-empty subset of the endurant natures.
