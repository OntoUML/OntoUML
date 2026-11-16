Definition
----------

«:ref:`mediation`» is an :ref:`existential dependence <dependency>` whose instances connect a :ref:`relator` to an endurant the relator depends on. Mediations are non-functional inherence relations: non-reflexive, asymmetric, and anti-transitive. A relator mediates at least two distinct individuals.

Employment mediates Employee and Employer. Marriage mediates Spouse.

.. figure:: /specification-figures/mediation.svg
   :alt: An employment mediating an employee and an employer
   :width: 80%
   :align: center

   Associations categorized as «mediation».

Allowed ends
------------

- **Relator end.** A class restricted exactly to ``{relator}``: a relator, a sortal that specializes one, or a non-sortal explicitly restricted to relators.
- **Mediated end.** A class whose instances are endurants. ``restrictedTo`` is a non-empty subset of the endurant natures.

The :ref:`material` association between the mediated endurants is derived from the relator and these mediations.
