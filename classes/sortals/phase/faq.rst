Common questions
----------------

.. _phase-faq-q1:
**Q1:** Do I have to represent the intrinsic property which is affecting the instantiation of the phase?

.. _phase-faq-a1:
**A1:** No, OntoUML does not require you to do that. However, whenever it is possible, you should represent everything needed to define the phase. On one hand, if you want to represent the Living and Deceased phases of a Person, it is ok. On the other hand, if representing Adult and Child, your model would be a lot more precise if you include the age property on your model and the OCL constraint defining the instantiation of the two phases.


.. _phase-faq-q2:
**Q2:** Can I define phases using modes?

.. _phase-faq-a2:
**A2:** Yes. The fragment below is an example of how to do that.

.. container:: figure

   |Phase application 3|

.. |Phase application 3| image:: _images/ontouml_phase-application-3.png