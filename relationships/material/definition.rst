Definition
----------

«:ref:`material`» connects two or more endurants in virtue of an extrinsic aspect: a relator, or an extrinsic mode. *rents*, *isFriendOf*, *trusts*, and *loves* are material relations. The relata instantiate the relation exactly when the truthmaker exists.

.. figure:: /specification-figures/material.svg
   :alt: A rents association derived from a rental agreement
   :width: 85%
   :align: center

   Associations categorized as «material».

Every end is a class of endurants. ``restrictedTo`` is a non-empty subset of the endurant natures.

The association is derived from its truthmaker.

- For a relation with two or more independent relata, the truthmaker is a :ref:`relator` connected to each relatum by :ref:`mediation`. *rents* is derived from Rental Agreement, which mediates the renter and the rented object.
- For a one-sided relation, the truthmaker is an :ref:`extrinsicMode` connected to one relatum by :ref:`characterization` and to the other by :ref:`externalDependence`. *trusts* is derived from Trust, which inheres in the trusting agent and externally depends on the trusted entity.

The derivation is a UML :ref:`derivation` dependency. Cardinality on the material association is the cardinality obtained by collapsing the paths through the truthmaker. Several material relations can be derived from one relator. Employments, enrollments, and marriages are the usual cases. See :ref:`relations-theory` and the :ref:`relator pattern <relator-pattern>`.
