Constraints
-----------

.. _collective-constraints-c1:
**C1:** A «:ref:`collective`» cannot have an :ref:`identity <identity>` provider («:ref:`kind`», «:ref:`collective`», «:ref:`quantity`», «:ref:`relator`», «:ref:`mode`» and «:ref:`quantity`») as its direct or indirect super-type.

.. container:: figure

   |Collective forbidden 1|

.. _collective-constraints-c2:
**C2:** A «:ref:`collective`» cannot have types that inherit :ref:`identity <identity>`  («:ref:`subkind`», «:ref:`role`» and «:ref:`phase`») as its direct or indirect super-types.

.. container:: figure

   |Collective forbidden 2|

.. _collective-constraints-c3:
**C3:** A «:ref:`collective`» cannot have types that aggregate individuals with :ref:`different identity principles <identity>` («:ref:`category`», «:ref:`rolemixin`» and «:ref:`mixin`») as its direct or indirect subtypes.

.. container:: figure

   |Collective forbidden 3|

.. _collective-constraints-c4:
**C4:** As a :ref:`rigid <rigidity>` type, a «:ref:`collective`» cannot have any :ref:`anti-rigid <rigidity>` type («:ref:`role`», «:ref:`rolemixin`» and «:ref:`phase`») as its direct or indirect super-type.

.. container:: figure

   |Collective forbidden 4|

.. |Collective forbidden 1| image:: _images/ontouml_collective-forbidden-1.png
.. |Collective forbidden 2| image:: _images/ontouml_collective-forbidden-2.png
.. |Collective forbidden 3| image:: _images/ontouml_collective-forbidden-3.png
.. |Collective forbidden 4| image:: _images/ontouml_collective-forbidden-4.png
