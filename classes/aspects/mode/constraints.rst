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
**C3:** Modes cannot have as ancestors the following types: «:ref:`kind`», «:ref:`quantity`», «:ref:`collective`», «:ref:`subkind`», «:ref:`role`», «:ref:`rolemixin`», «:ref:`phase`», «:ref:`relator`», «:ref:`quality`», «:ref:`mode`».

.. container:: figure

   |Mode forbidden 2|

.. _mode-constraints-c4:
**C4:** Modes cannot have as descendants the following types: «:ref:`kind`», «:ref:`quantity`», «:ref:`collective`», «:ref:`rolemixin`», «:ref:`category`», «:ref:`mixin`», «:ref:`relator`», «:ref:`quality`», «:ref:`mode`».

.. container:: figure

   |Mode forbidden 1|


.. |Mode application 1| image:: _images/ontouml_mode-application-1.png
.. |Mode forbidden 3| image:: _images/ontouml_mode-forbidden-3.png
.. |Mode forbidden 2| image:: _images/ontouml_mode-forbidden-2.png
.. |Mode forbidden 1| image:: _images/ontouml_mode-forbidden-1.png
