Definition
----------

A «:ref:`category`» is a rigid non-sortal. It captures essential properties shared by entities that follow different identity principles. Physical Object may classify persons, cars, and buildings. Legal Relationship may classify marriages, employments, and contracts. Economic Event may classify purchases, payments, and deliveries.

Categories are abstract classes. They are often introduced while refactoring a model. If Person and Animal both have a weight, a category such as Physical Object can own that quality, and Person and Animal specialize it.

.. figure:: /specification-figures/category-example.svg
   :alt: Physical Object as a category generalized by person, car, and building
   :width: 85%
   :align: center

   A class categorized as «category».

A category may specialize a category or a mixin. It may be specialized by any endurant, event, situation, or higher-order stereotype in the profile, including other categories, mixins, and the anti-rigid non-sortals. It cannot specialize a sortal, and it cannot specialize an anti-rigid type. See :ref:`class-taxonomy`.
