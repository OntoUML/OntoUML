.. _bringingAbout:

Bringing about
==============

«bringingAbout» connects an event to a situation that, as an effect of the event, begins to obtain at the instant the event ends.

As with :ref:`triggering`, the situation an event brings about is maximal: it embodies all the effects of the occurrence. A bringing-about association may connect an event type to a situation type that captures only the domain-relevant effects. Each such situation is an improper part of that maximal situation.

A gas leak brings about a hazardous gas concentration, which may in turn trigger an explosion. A final loan payment brings about a settled debt. A checkmating move brings about a checkmate.

.. figure:: /specification-figures/bringing-about.svg
   :alt: A gas leak bringing about a hazardous gas concentration
   :width: 80%
   :align: center

   Associations categorized as «bringingAbout».

Allowed ends
------------

- **Event end.** A class restricted exactly to ``{event}``.
- **Situation end.** A class restricted exactly to ``{situation}``.

Chains of bringing about and triggering are causal chains, and they ground :ref:`historicalDependence` between events.
