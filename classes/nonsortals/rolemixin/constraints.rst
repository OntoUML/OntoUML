Constraints
-----------

**C1:** A «RoleMixin» is always abstract. Notice that abstract classes
are represented with an *italic* label.

.. container:: figure

   |RoleMixin application 3|

**C2:** A «RoleMixin» aggregate individuals that follow different
identity principles, therefore it may not have as ancestor the following
constructs: «Kind», «Quantity», «Collective», «Subkind», «Role»,
«Phase», «Relator», «Mode», «Quality».

**C3:** A «RoleMixin» is a anti-rigid construct, therefore it cannot
have as descendent any rigid or semi-rigid type, as: «Kind», «Quantity»,
«Collective», «Subkind», «Category», «Mixin», «Relator», «Mode»,
«Quality».

.. container:: figure

   |RoleMixin forbidden 1|

.. |RoleMixin application 3| image:: _images/ontouml_rolemixin-application-3.png
.. |RoleMixin forbidden 1| image:: _images/ontouml_rolemixin-forbidden-1.png
