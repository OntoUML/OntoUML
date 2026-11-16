Definition
----------

A «:ref:`rolemixin`» is an anti-rigid non-sortal that classifies entities contingently, in virtue of a relational condition. It is the non-sortal counterpart of :ref:`role`: the classification is relational and temporary, and the instances need not share an identity principle.

Customer may classify persons and organizations in the scope of a purchase or a service. Insured Item may classify cars, houses, and artworks in the scope of an insurance contract. Competitor may classify persons, teams, horses, or dogs in the scope of a competition.

.. figure:: /specification-figures/role-mixin.svg
   :alt: Customer as a role mixin over persons and organizations
   :width: 80%
   :align: center

   A class categorized as «roleMixin».

Two familiar shapes remain useful:

- Define the role mixin by the sortal roles that specialize it, such as Personal Customer and Corporate Customer.
- Or let the role mixin specialize a category, such as Customer specializing Agent. The two shapes are semantically aligned. The second is the more compact one.

A role mixin may specialize a category, mixin, role mixin, historical role mixin, or phase mixin. It may be specialized by a role, historical role, role mixin, or historical role mixin. It is an abstract class.
