Constraints
-----------

.. _mode-constraints-c1:
**C1:** Every «:ref:`mode`» must be (directly or indirectly) connected to an association end of at least one «:ref:`characterization`» relation.

.. container:: figure

   |Mode application 1|

.. _mode-constraints-c2:
**C2:** The multiplicity of the characterized end (opposite to the «:ref:`mode`») must be exactly one. Therefore, the following examples are forbidden.

.. container:: figure

   |Mode forbidden 3|

.. _mode-constraints-c3:
**C3:** A «:ref:`mode`» cannot have an :ref:`identity <identity>` provider («:ref:`kind`», «:ref:`collective`», «:ref:`quality`», «:ref:`relator`», «:ref:`mode`» and «:ref:`quantity`») as its direct or indirect super-type.

.. container:: figure

   |Mode forbidden 2|

.. _mode-constraints-c4:
**C4:** A «:ref:`mode`» cannot have types that inherit :ref:`identity <identity>` («:ref:`subkind`», «:ref:`role`» and «:ref:`phase`») as its direct or indirect super-type.

.. container:: figure

   |Mode forbidden 1|

.. _mode-constraints-c5:
**C5:** A «:ref:`mode`» cannot have types that aggregate individuals with :ref:`different identity principles <identity>` («:ref:`category`», «:ref:`rolemixin`», «:ref:`phasemixin`» and «:ref:`mixin`») as its direct or indirect subtypes.

.. _mode-constraints-c6:
**C6:** As a :ref:`rigid <rigidity>` type, a «:ref:`mode`» cannot have any :ref:`anti-rigid <rigidity>` type («:ref:`role`», «:ref:`rolemixin`», «:ref:`phase`» and «:ref:`phasemixin`») as its direct or indirect super-type.

.. |Mode application 1| image:: _images/ontouml_mode-application-1.png
.. |Mode forbidden 3| image:: _images/ontouml_mode-forbidden-3.png
.. |Mode forbidden 2| image:: _images/ontouml_mode-forbidden-2.png
.. |Mode forbidden 1| image:: _images/ontouml_mode-forbidden-1.png


