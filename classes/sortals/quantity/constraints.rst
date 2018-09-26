Constraints
-----------

**C1:** A «:ref:`quantity`» cannot have an :ref:`identity provider <identity>` («:ref:`kind`», «:ref:`collective`», «:ref:`quantity`», «:ref:`relator`», «:ref:`mode`» and «:ref:`quantity`») as its direct or indirect super-type.

.. container:: figure

   |Quantity forbidden 1|

**C2:** A «:ref:`quantity`» cannot have types that inherit :ref:`identity <identity>` («:ref:`subkind`», «:ref:`role`» and «:ref:`phase`») as its direct or indirect super-types.

.. container:: figure

   |Quantity forbidden 2|

**C3:** A «:ref:`quantity`» cannot have types that aggregate individuals with different :ref:`identity principles <identity>` («:ref:`category`», «:ref:`rolemixin`» and «:ref:`mixin`») as its direct or indirect subtypes.

.. container:: figure

   |Quantity forbidden 3|

**C4:** As a :ref:`rigid <rigidity>` type, a «:ref:`quantity`» cannot have any :ref:`anti-rigid <rigidity>` type («:ref:`role`», «:ref:`rolemixin`» and «:ref:`phase`») as its direct or indirect super-type.

.. container:: figure

   |Quantity forbidden 4|

.. |Quantity forbidden 1| image:: _images/ontouml_quantity-forbidden-1.png
.. |Quantity forbidden 2| image:: _images/ontouml_quantity-forbidden-2.png
.. |Quantity forbidden 3| image:: _images/ontouml_quantity-forbidden-4.png
.. |Quantity forbidden 4| image:: _images/ontouml_quantity-forbidden-3.png
