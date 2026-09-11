Constraints
-----------

.. _quality-constraints-c1:
**C1:** A «:ref:`quality`» must always be connected, through a «:ref:`characterization`» to another type.

.. container:: figure

   |Quality application 1|

.. _quality-constraints-c2:
**C2:** The multiplicity of the characterized end (opposite to the quality) must be exactly one. Therefore, the following examples are forbidden.

.. container:: figure

   |Quality forbidden 1|

.. _quality-constraints-c3:
**C3:** A «:ref:`quality`» cannot have an :ref:`identity <identity>` provider («:ref:`kind`», «:ref:`collective`», «:ref:`quality`», «:ref:`relator`», «:ref:`mode`» and «:ref:`quantity`») as its direct or indirect super-type.

.. container:: figure

   |Quality forbidden 2|

.. _quality-constraints-c4:
**C4:** A «:ref:`quality`» cannot have types that inherit :ref:`identity <identity>` («:ref:`subkind`», «:ref:`role`» and «:ref:`phase`») as its direct or indirect super-type.

.. container:: figure

   |Quality forbidden 3|

.. _quality-constraints-c5:
**C5:** A «:ref:`quality`» cannot have types that aggregate individuals with :ref:`different identity principles <identity>` («:ref:`category`», «:ref:`rolemixin`», «:ref:`phasemixin`» and «:ref:`mixin`») as its direct or indirect subtypes.

.. _quality-constraints-c6:
**C6:** As a :ref:`rigid <rigidity>` type, a «:ref:`quality`» cannot have any :ref:`anti-rigid <rigidity>` type («:ref:`role`», «:ref:`rolemixin`», «:ref:`phase`» and «:ref:`phasemixin`») as its direct or indirect super-type.



.. |Quality application 1| image:: _images/ontouml_quality-application-1.png
.. |Quality forbidden 1| image:: _images/ontouml_quality-forbidden-1.png
.. |Quality forbidden 2| image:: _images/ontouml_quality-forbidden-2.png
.. |Quality forbidden 3| image:: _images/ontouml_quality-forbidden-3.png


