Constraints
-----------

**R1:** A «:ref:`phase`» must always have **exactly one identity provider**
(«:ref:`kind`», «:ref:`collective`», «:ref:`quantity`», «:ref:`relator`», «:ref:`mode`», «:ref:`quantity`») as an
ancestor (a direct or indirect super-type). Our examples above should be
modelled as:

.. container:: figure

   |Phase application 1|

**R2:** A «:ref:`phase`» must always be part of a partition (a generalization
set disjoint and complete). Modeling a «:ref:`phase`» as in example below is
forbidden:

.. container:: figure

   |Phase forbidden 2|

**R3:** A «:ref:`phase`» cannot be a direct subtype of a «:ref:`rolemixin`» or
«:ref:`category`».

.. container:: figure

   |Phase forbidden 3|

**R4:** A «:ref:`phase`» cannot be a super-type of a :ref:`rigid <rigidity>` type («:ref:`kind`»,
«:ref:`collective`», «:ref:`quantity`», «:ref:`relator`», «:ref:`mode`», «:ref:`quantity`», «:ref:`subkind`», «:ref:`category`»).

.. container:: figure

   |Phase forbidden 1|

**R4:** A «:ref:`phase`» cannot be a super-type of a mixin type («:ref:`category`»,
«:ref:`rolemixin`», «:ref:`mixin`»).

.. container:: figure

   |Phase forbidden 4|

.. |Phase application 1| image:: _images/ontouml_phase-application-1.png
.. |Phase forbidden 2| image:: _images/ontouml_phase-forbidden-2.png
.. |Phase forbidden 3| image:: _images/ontouml_phase-forbidden-3.png
.. |Phase forbidden 1| image:: _images/ontouml_phase-forbidden-1.png
.. |Phase forbidden 4| image:: _images/ontouml_phase-forbidden-4.png
