.. _historicalRole:

Historical role
===============

.. stereotype:: meta.yml

Definition
----------

A «historicalRole» is an anti-rigid sortal that specializes a unique :ref:`ultimate sortal <ultimate-sortal>` and classifies entities contingently in virtue of their participation in an event.

An ordinary :ref:`role` applies only while a relational condition holds. A historical role is grounded in a past event and is retained once acquired. A person is a Hired Soccer Player, a role, only while employed by a club, and remains a Soccer Match Player, a historical role, after having played in a match. Composer classifies a person who has participated in an Act of Composition. Tested Code classifies code that has participated in a Test Execution.

.. figure:: /specification-figures/historical-role.svg
   :alt: Soccer match player as a historical role of person
   :width: 85%
   :align: center

   Classes categorized as «historicalRole».

A historical role may specialize a kind, collective, quantity, relator, intrinsic mode, extrinsic mode, quality, situation, type, subkind, role, historical role, phase, category, mixin, role mixin, or historical role mixin. It may be specialized by a role or a historical role. It cannot specialize an event type.

Constraints
-----------

A historical role is connected by a :ref:`participation` association to a class whose extension may include events, with minimum cardinality one at the event end. An instance of the historical role has participated in an event of that type.
