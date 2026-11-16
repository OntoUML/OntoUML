.. _situation:

Situation
=========

.. stereotype:: meta.yml

Definition
----------

A «situation» is a :ref:`first-order ultimate sortal <ultimate-sortal>` whose instances are particular configurations of a part of reality, understood as a whole, in which entities stand in relations.

Situations trigger events, and events bring situations about. A situation activates the dispositions whose manifestation is an event. The occurrence of an event results in a new situation.

Hazardous Gas Concentration is a configuration in which the concentration of a flammable gas in an enclosed space exceeds a safety threshold, and it can trigger an explosion. Checkmate is a board configuration in which a king stands in an attacked position from which no legal move can remove it. Loan Default is a configuration in which a borrower has failed to meet a payment obligation by its due date, and it triggers events such as contract termination or collateral seizure. Quorum Met is a configuration in which the number of members present meets the minimum required for deliberation, and it enables voting.

.. figure:: /specification-figures/situation.svg
   :alt: Hazardous gas concentration and checkmate as situations
   :width: 90%
   :align: center

   Classes categorized as «situation».

A situation may specialize a :ref:`category` or a :ref:`mixin`. It may be specialized by a :ref:`subkind` or a :ref:`phase`.

``restrictedTo`` is exactly ``{situation}`` and ``order`` is 1.

The entities that stand in the configuration are connected by :ref:`presence`. The link to the event a situation activates is :ref:`triggering`. The link from an event to the situation it produces is :ref:`bringingAbout`.
