Constraints
-----------

**R1:** A «Role» must always have **exactly one identity provider**
(«Kind», «Collective», «Quantity», «Relator», «Mode», «Quantity») as an
ancestor (a direct or indirect super-type). To model our list of roles
presented above, we should given them identity providers:

.. container:: figure

   |Role application 1|

**R2:** Every «Role» must be connected, directly or indirectly, to a
«mediation» relation, since it is a relationally dependent construct.
Continuing our example above, we should do the following:

.. container:: figure

   |Role application 2|

Remember that you can't defined a relational dependency with a minimum
cardinality of zero. Therefore, the fragment below is wrong!

.. container:: figure

   |Role forbidden 1|

**R3:** A «Role» cannot be a supertype of a rigid type («Kind»,
«Subkind», «Collective», «Quantity», «Relator», «Category»).

.. container:: figure

   |Role forbidden 2|

**R4:** A «Role» cannot be a supertype of a mixin types («Category»,
«RoleMixin», «Mixin»).

.. container:: figure

   |Role forbidden 3|

.. |Role application 1| image:: _images/ontouml_role-application-1.png
.. |Role application 2| image:: _images/ontouml_role-application-2.png
.. |Role forbidden 1| image:: _images/ontouml_role-forbidden-1.png
.. |Role forbidden 2| image:: _images/ontouml_role-forbidden-2.png
.. |Role forbidden 3| image:: _images/ontouml_role-forbidden-3.png
