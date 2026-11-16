.. _historicalRoleMixin:

Historical role mixin
=====================

.. stereotype:: meta.yml

Definition
----------

A «historicalRoleMixin» is an anti-rigid non-sortal that classifies entities contingently in virtue of their participation in a past event.

It stands to :ref:`historicalRole` as :ref:`rolemixin` stands to :ref:`role`. The classification is grounded in a past event and kept once acquired, and the instances may follow different identity principles.

Disaster Casualty may classify the persons, buildings, and vehicles harmed in a natural disaster. Auctioned Item may classify the paintings, properties, and vehicles sold in an auction.

.. figure:: /specification-figures/historical-role-mixin.svg
   :alt: Disaster casualty as a historical role mixin
   :width: 85%
   :align: center

   A class categorized as «historicalRoleMixin».

A historical role mixin may specialize a category, mixin, role mixin, historical role mixin, or phase mixin. It may be specialized by a role, historical role, role mixin, or historical role mixin. It is an abstract class.

Connect it to the event type by :ref:`participation`, in the same way as a historical role.
