.. _presence:

Presence
========

«presence» connects a situation to an entity that stands in a relation exemplified in that situation. The situation comprehends that entity as part of the configuration.

A hazardous gas concentration is present with the portion of flammable gas whose concentration exceeds the safety threshold. A checkmate is present with the king that stands in an attacked position from which no legal move can remove it. A loan default is present with the loan whose payment obligation was missed. A quorum is present with each assembly member who counts toward the minimum required for deliberation.

.. figure:: /specification-figures/presence.svg
   :alt: A checkmate situation present with a king
   :width: 80%
   :align: center

   Associations categorized as «presence».

Allowed ends
------------

- **Situation end.** A class restricted exactly to ``{situation}``.
- **Entity end.** Any class. The entity present in the situation may be an endurant, an event, another situation, or a type, according to what the configuration comprehends.
