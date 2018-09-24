Constraints
-----------

**C1:** A Quality must always be connected, through a characterization
to another type.

.. container:: figure

   |Quality application 1|

**C2:** The multiplicity of the characterized end (opposite to the
quality) must be exactly one. Therefore, the following examples are
forbidden.

.. container:: figure

   |Quality forbidden 1|

**C3:** Qualtities cannot have as ancestors the following types: «Kind»,
«Quantiy», «Collective», «Subkind», «Role», «RoleMixin», «Phase»,
«Relator», «Mode».

.. container:: figure

   |Quality forbidden 2|

**C4:** Qualtities cannot have as descendants the following types:
«Kind», «Quantiy», «Collective», «RoleMixin», «Category», «Mixin»,
«Relator», «Mode».

.. container:: figure

   |Quality forbidden 3|


.. |Quality application 1| image:: _images/ontouml_quality-application-1.png
.. |Quality forbidden 1| image:: _images/ontouml_quality-forbidden-1.png
.. |Quality forbidden 2| image:: _images/ontouml_quality-forbidden-2.png
.. |Quality forbidden 3| image:: _images/ontouml_quality-forbidden-3.png
