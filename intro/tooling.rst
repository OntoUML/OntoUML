.. _tooling:

Tooling
=======

OntoUML models can be drawn in a UML tool that supports the profile. The same models can be written as text with **Tonto**, a textual ontology language developed by the `NEMO Ontology and Conceptual Modeling Research Group <https://nemo.inf.ufes.br>`__ at the Federal University of Espírito Santo, in cooperation with the Semantics, Cybersecurity and Services group at the University of Twente.

Tonto puts the UFO distinctions used by OntoUML directly in the syntax: kinds, roles, relators, events, and the relations between them. A model is a plain ``.tonto`` file. Editor support adds completion, validation, refactoring, and version-control friendly text. The same textual form is intended for people and for LLM-based agents: explicit structure, checkable rules, and fast feedback. The name is a backronym for *textual ontologies*.

Three tools share that language.

`Tonto <https://github.com/nemo-ufes/tonto>`__
   The language, a VS Code extension, and a command-line tool. Install `tonto from the Visual Studio Marketplace <https://marketplace.visualstudio.com/items?itemName=nemo-ufes.tonto-vscode>`__ (VS Code 1.95 or later) and run **Tonto: Get Started**. The extension checks the model as you type, explains problems, and offers repairs when a rule determines the edit. Completion proposes admissible stereotypes and declaration shapes. **Tonto: Insert Modeling Pattern...** inserts a checked example for roles and their relators, phase partitions, parthood, constitution, causation, and multi-level modeling. An optional ``tonto.antiPatterns`` setting adds the :ref:`anti-pattern <anti-patterns>` catalogue as advisory diagnostics.

   Ontologies can grow from one file into packages, refer to other packages with ``use``, and import a published ontology by URL. **Tonto: Export to gUFO...** writes a gUFO-aligned OWL/Turtle file. The command-line package ``tonto-language`` (Node.js 22 or later) exposes the same checks, the language guide, and the export. **Tonto: Set Up Codex and Claude in Workspace** configures an MCP server and project instructions so an agent in the editor can use the guide, the validator, the patterns, and the export.

`Tonto Visualizer <https://github.com/nemo-ufes/tonto-visualizer>`__
   An OntoUML diagram beside the text, in VS Code (`marketplace extension <https://marketplace.visualstudio.com/items?itemName=nemo-ufes.tonto-visualizer>`__). It draws the model as you type and keeps elements where you drag them when the text changes. The picture is produced locally: stereotypes, attributes, generalizations, generalization sets, relations, cardinalities, and whole-part diamonds. Ontology manifests with bundles appear as package diagrams. Named views can be saved and reopened. The diagram edits the view, and the ``.tonto`` file remains the model. A command-line ``tonto-view`` can write the diagram as SVG.

`Tonto Playground <https://nemo-ufes.github.io/tonto-playground/>`__
   The same language and the same diagram in the browser (`source <https://github.com/nemo-ufes/tonto-playground>`__). One ``.tonto`` file is edited on the left and drawn on the right. There is no account and no server. The model stays on the page unless you share a link, and a shared link carries the model in the URL fragment. The editor runs Tonto's language server in a web worker, so completion, hover, problems, quick fixes, rename, and formatting match the VS Code extension. You can start from the pattern catalog, download the ``.tonto`` file, or export SVG, PNG, or a ``.tontoview`` arrangement that the VS Code visualizer opens. The playground edits a single file. Multi-file ontologies belong in VS Code.

A short model of people and employment, in Tonto::

   /// People and their employment.
   ontology people

   /// A person, in the everyday sense.
   kind Person

   /// A person employed by an organization.
   role Employee specializes Person

   /// An organization of people.
   kind Organization

   /// An organization that employs people.
   role Employer specializes Organization

   /// The employment binding an employee and an organization.
   relator Employment {
       @mediation [1..*] -- [1] (const) Employee
       @mediation [1..*] -- [1] (const) Employer
   }

   @material relation Employee [1..*] -- worksFor -- [1..*] Employer derivedFrom Employment

``kind`` gives Person and Organization their own identity. Employee and Employer apply while an employment holds. Each employment mediates one employee and one employer. ``worksFor`` is the material relation derived from that relator. A ``///`` comment immediately above a declaration is its domain documentation.

The original Tonto design is by Matheus Lenke Coutinho and João Paulo A. Almeida. The current repositories reimplement the language, the checks, and the diagram, and they acknowledge Giancarlo Guizzardi, Tiago Prince Sales, Claudenir M. Fonseca, and the contributors to OntoUML.
