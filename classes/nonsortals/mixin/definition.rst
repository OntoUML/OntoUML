Definition
----------

A **«Mixin»** is a semi-rigid type, i.e., it "behaves" as a rigid type
for some individuals and as an anti-rigid one for others (it's the only
stereotype with such feature in OntoUML). As the Category and the
RoleMixin, the Mixin meta-class characterizes individuals that follow
different identity principles. Here are some examples of types that
could be classified as Mixin:

.. container:: figure

   |Mixin examples|

As categories, mixins are commonly applied during a refactoring process,
in particular when we want to state that some properties are applied to
both rigid and anti-rigid types. For instance, let's consider that we
defined the following types in our model, Car and Jewellery, a general
concept for Ring, Necklace, etc. Now we want to define the type Luxury
Good. In our worldview, every jewellery is luxurious, but only cars that
are worth more than 30k dollars are. Since the value of a car changes
through the years, being a luxurious car is a temporary classification,
whilst being a jewellery is a permanent one. The type Luxury Good,
therefore, is semi-rigid or a Mixin.

.. container:: figure

   |Mixin application 1|

.. |Mixin examples| image:: _images/ontouml_mixin-examples.png
.. |Mixin application 1| image:: _images/ontouml_mixin-application-1.png
