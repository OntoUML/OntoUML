Constraints
-----------

**C1:** Every «Mode» must be (directly or indirectly) connected to an
association end of at least one «characterization» relation.

.. container:: figure

   |Mode application 1|

**C2:** The multiplicity of the characterized end (opposite to the Mode)
must be exactly one. Therefore, the following examples are forbidden.

.. container:: figure

   |Mode forbidden 3|

**C3:** Modes cannot have as ancestors the following types: «Kind»,
«Quantiy», «Collective», «Subkind», «Role», «RoleMixin», «Phase»,
«Relator», «Quality».

.. container:: figure

   |Mode forbidden 2|

**C4:** Modes cannot have as descendants the following types: «Kind»,
«Quantity», «Collective», «RoleMixin», «Category», «Mixin», «Relator»,
«Quality».

.. container:: figure

   |Mode forbidden 1|


.. |Mode application 1| image:: _images/ontouml_mode-application-1.png
.. |Mode forbidden 3| image:: _images/ontouml_mode-forbidden-3.png
.. |Mode forbidden 2| image:: _images/ontouml_mode-forbidden-2.png
.. |Mode forbidden 1| image:: _images/ontouml_mode-forbidden-1.png
