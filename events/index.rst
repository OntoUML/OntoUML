.. _events:

Events
======

Events are individuals that unfold in time. This section specifies the class, association, and property stereotypes for them. The ontological reading is in :ref:`events-theory`.

Historical semantics
--------------------

Events exist only in the past. A reference to a future event is a belief that an event of some type will happen, or a commitment to bring an event of some type about.

Events are also existentially dependent. They are manifestations of potentialities of endurants, and they are changes happening to specific endurants. A song manifests someone's capacity to sing. A flight manifests a capacity to fly. An electric current manifests a conductor's disposition to conduct. Singing is a set of changes in vocal cords. Moving is a series of changes in location.

Whenever a particular event instantiates a type in the model, that event is in the past, and the entities it depends on exist in that same past. A model that uses these stereotypes is interpreted with a historical, growing-block view of time: the relevant past continues to exist as new events and their participants are added.

.. figure:: /specification-figures/event-classes.svg
   :alt: Profile diagram of the event class stereotypes
   :width: 100%
   :align: center

   Event class stereotypes.

.. figure:: /specification-figures/event-associations.svg
   :alt: Profile diagram of the event association stereotypes
   :width: 100%
   :align: center

   Event association stereotypes.

.. toctree::
   :maxdepth: 1
   :caption: Classes:

   event/index
   historical-role/index
   historical-role-mixin/index

.. toctree::
   :maxdepth: 1
   :caption: Associations:

   historical-dependence
   participation
   creation
   termination
   manifestation
   change
   structural
   temporal
   participational

.. toctree::
   :maxdepth: 1
   :caption: Properties:

   begin
   end
