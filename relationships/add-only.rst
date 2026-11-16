.. _addOnly:

addOnly
=======

«addOnly» is a property stereotype. Values of an add-only property may be added at any time. Once added, a value is kept for as long as the owning object exists: it is not removed and it is not replaced.

Typical uses record history, such as the diagnoses received by a patient or the purchases made by a customer. If the association end ``purchases`` of Customer is «addOnly», new purchases may be linked to Maria at any time, and none of them can later be unlinked or substituted.

The stereotype is meaningful for multivalued properties and for optional single-valued properties (``0..1``). It is incompatible with read-only properties, which admit no additions. It restores the ``addOnly`` changeability of UML 1, which UML 2 dropped.

.. figure:: /specification-figures/add-only.svg
   :alt: An add-only association end recording purchases
   :width: 70%
   :align: center

   A property categorized as «addOnly».

.. figure:: /specification-figures/endurant-properties.svg
   :alt: Profile diagram of endurant property stereotypes
   :width: 40%
   :align: center

   Endurant property stereotypes.

Constraints
-----------

- The property is multivalued, or it is optional.
- The property is not read-only.

Temporal bounds of individuals use the event-module stereotypes :ref:`begin` and :ref:`end`, which can also decorate endurant attributes such as a date of birth.
