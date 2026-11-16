Definition
----------

A «:ref:`mixin`» is a semi-rigid non-sortal. It captures properties that are essential to some of its instances and accidental to others. It is the only stereotype with that modal profile. Like a :ref:`category`, a :ref:`rolemixin`, and a :ref:`phasemixin`, a mixin classifies individuals that may follow different identity principles.

Musical Artist may classify bands essentially, and classify persons contingently while they are musicians. Legal Instrument may classify contracts essentially, and classify letters, declarations, or records contingently when they acquire legal force.

The same pattern appears in refactoring. Suppose the model already has Car and Jewellery. Luxury Good is essential to every jewel and accidental to a car, because a car is a luxury good only while its value stays above a threshold. Luxury Good is a mixin.

.. figure:: /specification-figures/mixin-example.svg
   :alt: Musical Artist as a mixin over bands and persons
   :width: 85%
   :align: center

   A class categorized as «mixin».

A mixin may specialize a category or a mixin. It may be specialized by the same range of stereotypes as a category. It cannot specialize an anti-rigid type, and its ontological natures include endurant natures. See :ref:`rigidity` and :ref:`class-taxonomy`.
