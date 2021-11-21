Common questions
----------------

.. _role-faq-q1:
**Q1:** Can I define multiples :ref:`dependencies <dependency>` for a «:ref:`role`»?

.. _role-faq-a1:
**A1:** Yes,
there is no restriction in the number of :ref:`dependencies <dependency>` one can define for
a «:ref:`role`». However, think carefully before doing so. You might be adding
some unwanted instantiations to your ontology. This is an Ontological
Anti-Pattern, called Multiple Dependency (read more about it
`here <https://www.researchgate.net/publication/268220197_Ontology_Validation_for_Managers>`__)


.. _role-faq-q2:
**Q2:** Can a «:ref:`role`» be used to specialize another «:ref:`role`»?

.. _role-faq-a2:
**A2:** Yes,
there is no restriction regarding it. Again, take care when doing so.
Since the language only require at least one :ref:`indirect dependency <dependency>` for a
«:ref:`role`», you might forget to define additional :ref:`dependencies <dependency>` for the
sub-types.
