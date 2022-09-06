Constraints
-----------

.. _category-constraints-c1:
**C1:** A «:ref:`category`» is always abstract. Notice that abstract classes are represented with an *italic* label.

.. container:: figure

   |Category application 1|

.. _category-constraints-c2:
**C2:** A «:ref:`category`» aggregate individuals that follow :ref:`different identity principles <identity>`, therefore it may not have as ancestor the following constructs: «:ref:`kind`», «:ref:`quantity`», «:ref:`collective`», «:ref:`subkind`», «:ref:`role`», «:ref:`phase`», «:ref:`relator`», «:ref:`mode`», «:ref:`quality`».

.. container:: figure

   |Category forbidden 1|

.. _category-constraints-c3:
**C3:** A «:ref:`category`» is a :ref:`rigid <rigidity>` construct, therefore it cannot have as ancestor an :ref:`anti-rigid <rigidity>` type, as: «:ref:`role`», «:ref:`rolemixin`», «:ref:`phase`».

.. container:: figure

   |Category forbidden 2|

.. |Category application 1| image:: _images/ontouml_category-application-1.png
.. |Category forbidden 1| image:: _images/ontouml_category-forbidden-1.png
.. |Category forbidden 2| image:: _images/ontouml_category-forbidden-3.png
