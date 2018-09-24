Constraints
-----------

**R1:** A «Subkind» must **always** have exactly one identity provider
(«Kind», «Collective», «Quantity», «Relator», «Mode», «Quantity») as an
ancestor (a direct or indirect super-type). Therefore, our examples in
the first figure should be modelled as:

.. container:: figure

   |Subkind application 1|

**R2:** Because it is a rigid type, a «Subkind» cannot have an
anti-rigid type («Role», «Phase», «RoleMixin») as an ancestor.
Therefore, the following fragments would not be allowed:

.. container:: figure

   |Subkind forbidden 1|

**R3:** Since every instance of a «Subkind» follows the same identity
principle, a «Subkind» cannot have an mixin type («Category», «Mixin»,
«RoleMixin») as a descendant, i.e., a direct or indirect subtype.
Fragments like the ones below are not allowed:

.. container:: figure

   |Subkind forbidden 2|

.. |Subkind application 1| image:: _images/ontouml_subkind-application-1.png
.. |Subkind forbidden 1| image:: _images/ontouml_subkind-forbidden-2.png
.. |Subkind forbidden 2| image:: _images/ontouml_subkind-forbidden-3.png
