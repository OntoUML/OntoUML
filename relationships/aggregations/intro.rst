Part-Whole
==========

UML distinguishes between aggregation and composition only. OntoUML
distinguishes among

-  sharing

   -  shared part (white ◊)
   -  exclusive part (black ♦)

-  multiplicity of relationship

   -  mandatory part with respect to the whole
   -  mandatory whole w.r.t. the part
   -  mandatory non-rigid type (e.g. role, phase, mixin)

OntoUML also distinguishes among various types of wholes and their parts

-  functional whole
   (and `ComponentOf </ufo/wiki/part-whole-relation/componentof/>`__
   relation)
-  collective
   (and `SubCollectionOf </ufo/wiki/part-whole-relation/subcollectionof/>`__
   and \ `MemberOf </ufo/wiki/part-whole-relation/memberof/>`__
   relations)
-  quantity (and
   `Containment </ufo/wiki/part-whole-relation/containment/>`__
   and \ `SubQuantityOf </ufo/wiki/part-whole-relation/subquantityof/>`__
   relations)

.. _example:

Examples
========

**EX1:** [caption id="attachment_615" align="alignnone"
width="650"]\ |image0| Part-Whole Relations[/caption] **EX2:** [caption
id="attachment_621" align="alignnone" width="360"]\ |image1| Example of
shared part[/caption] Notice that maximum multiplicity of the whole is >
1. **EX3:** [caption id="attachment_624" align="alignnone"
width="350"]\ |image2| Exclusive Part[/caption] Notice that maximum
multiplicity of the whole is = 1. **EX4:** [caption id="attachment_628"
align="alignnone" width="350"]\ |image3| Optional Part[/caption]
Optional part w.r.t. the rigid whole. The whole doesn´t necessarily need
any part. **EX5:** [caption id="attachment_630" align="alignnone"
width="350"]\ |image4| Mandatory Part[/caption] Mandatory part w.r.t.
the rigid whole. The whole does need a part, instances of the part may
mute. **EX6:** [caption id="attachment_632" align="alignnone"
width="350"]\ |image5| Essential Part[/caption] Essential part w.r.t.
the rigid whole. The whole does need a part, instances mustn´t mute.
**EX7:** [caption id="attachment_632" align="alignnone"
width="350"]\ |image6| Optional Whole[/caption] Optional rigid whole
w.r.t. the part. The part may exist alone, even without the whole.
**EX8:** [caption id="attachment_635" align="alignnone"
width="350"]\ |image7| Mandatory Whole[/caption] Mandatory rigid whole
w.r.t. the part. The part must belong to some whole, instances of the
whole may mute. **EX9:** [caption id="attachment_636" align="alignnone"
width="350"]\ |image8| Inseparable Part[/caption] Inseparable part of
the rigid whole. The part must belong to the same whole, instances of
the whole mustn´t mute. **EX10:** [caption id="attachment_638"
align="alignnone" width="360"]\ |image9| Immutable Part[/caption]
Immutable part of the antirigid whole. Whenever the whole exists in the
particular role or phase, its parts must be still the same instances --
they cannot not mute. Compare to *{essential}*. **EX11:** [caption
id="attachment_639" align="alignnone" width="470"]\ |image10| Immutable
Whole[/caption] Immutable whole w.r.t. the antirigid part. Whenever the
part exists in the particular role or phase, its wholes must be still
the same instances -- they cannot not mute. Instances of the whole may
mute only as the part changes it´s role or phase.  

.. container:: figure

   **References:**

GUIZZARDI, Giancarlo. *Ontological Foundations for Structural Conceptual
Models.* Enschede: CTIT, Telematica Instituut, 2005. GUIZZARDI,
Giancarlo. *Introduction to Ontological Engineering.* [presentation]
Prague: Prague University of Economics, 2011.

.. |image0| image:: _images/partWholeRelations.png
.. |image1| image:: _images/sharedPart.png
.. |image2| image:: _images/exclusivePart.png
.. |image3| image:: _images/optionalPart.png
.. |image4| image:: _images/mandatoryPart.png
.. |image5| image:: _images/essentialPart.png
.. |image6| image:: _images/essentialPart.png
.. |image7| image:: _images/mandatoryWhole.png
.. |image8| image:: _images/nonseparablePart.png
.. |image9| image:: _images/immutablePart.png
.. |image10| image:: _images/immutable_whole.png
