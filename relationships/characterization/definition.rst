Definition
----------

«:ref:`characterization`» is an :ref:`existential dependence <dependency>` whose instances connect a mode or quality to the endurant in which it inheres. The instances are inherence relations: non-reflexive, asymmetric, anti-transitive, and functional. Each aspect inheres in exactly one bearer and cannot migrate.

Weight characterizes Person. Color characterizes Car. A headache characterizes a person. A commitment characterizes an agent.

.. figure:: /specification-figures/characterization.svg
   :alt: Weight characterizing a person and color characterizing a car
   :width: 80%
   :align: center

   Associations categorized as «characterization».

Allowed ends
------------

- **Characterizing end.** A class whose instances are modes or qualities. ``restrictedTo`` is a non-empty subset of ``{intrinsic mode, extrinsic mode, quality}``.
- **Bearer end.** A class whose instances are concrete individuals. ``restrictedTo`` is a non-empty subset of the concrete individual natures.

The characterizing types are :ref:`quality`, :ref:`intrinsicMode`, and :ref:`extrinsicMode`. An extrinsic mode also has an :ref:`externalDependence` toward the entity it is about.
