Common questions
----------------

**Q1:** Can I define multiples dependencies for a «Role»?
**A1:** Yes,
there is no restriction in the number of dependencies one can define for
a «Role». However, think carefully before doing so. You might be adding
some unwanted instantiations to your ontology. This is an Ontological
Anti-Pattern, called Multiple Dependency (read more about it
`here <https://www.researchgate.net/publication/268220197_Ontology_Validation_for_Managers>`__)


**Q2:** Can a «Role» be used to specialize another «Role»?
**A2:** Yes,
there is no restriction regarding it. Again, take care when doing so.
Since the language only require at least one indirect dependency for a
«Role», you might forget to define additional dependencies for the
sub-types.
