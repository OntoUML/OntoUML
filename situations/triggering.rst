.. _triggering:

Triggering
==========

«triggering» connects a situation to an event that is the :ref:`manifestation` of dispositions activated by that situation.

Strictly speaking, the situation that triggers an event is the maximal situation satisfying every condition that is jointly necessary and sufficient for that activation. In a triggering association, the situation type may capture only the domain-relevant portion of those conditions. Each such situation is an improper part of the maximal situation that triggers the event.

A hazardous gas concentration triggers an explosion, which manifests the flammability of the gas. A loan default triggers a collateral seizure, which manifests the legal power the loan contract confers on the lender. A checkmate triggers the match ending, which manifests normative dispositions grounded in the rules of chess.

.. figure:: /specification-figures/triggering.svg
   :alt: A hazardous gas concentration triggering an explosion
   :width: 80%
   :align: center

   Associations categorized as «triggering».

Allowed ends
------------

- **Situation end.** A class restricted exactly to ``{situation}``.
- **Event end.** A class restricted exactly to ``{event}``.

Together with :ref:`bringingAbout`, triggering grounds causation between events. An event causes another when it brings about a situation that triggers the latter.
