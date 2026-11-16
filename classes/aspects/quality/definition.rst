Definition
----------

A «:ref:`quality`» is a :ref:`first-order ultimate sortal <ultimate-sortal>` whose instances are aspects that inhere in a bearer and are measurable by projection into a quality structure.

A quality structure is the value space for qualities of a given type. OntoUML represents it with a datatype or an enumeration. An object's color may be projected into an HSV space, an RGB space, or an enumeration such as red, green, and blue. A body's temperature may be projected into Celsius, Fahrenheit, or Kelvin. The color of a particular rose remains the same quality when its value changes from red to brown. See :ref:`endurants`.

.. figure:: /specification-figures/quality.svg
   :alt: Weight and color as qualities of a bearer
   :width: 75%
   :align: center

   A class categorized as «quality».

The inherence in the bearer is a :ref:`characterization`. Comparisons such as *heavier than* and *taller than* are :ref:`comparative` associations derived from these qualities. The earlier «structuration» stereotype is not part of the current profile. Structure the quality by typing it, or by typing the value it projects into, with a datatype or enumeration.

Modelers often group qualities by how the value is obtained:

- **Perceivable** qualities can be measured with an instrument, such as weight, height, color, and speed.
- **Non-perceivable** qualities are still projected into a value space, such as an amount of currency assigned as a price.
- **Nominal** qualities pick out a value used as a label, such as a name, an ISBN, or a card number.

A quality may specialize a :ref:`category` or a :ref:`mixin`. It may be specialized by a :ref:`subkind`, :ref:`role`, :ref:`historicalRole`, or :ref:`phase`.

``restrictedTo`` is exactly ``{quality}`` and ``order`` is 1.
