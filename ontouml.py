from docutils import nodes
from docutils.parsers.rst import Directive, directives
import sphinx
import os
import yaml


def add_df_item(root, term, *contents):
    root += nodes.definition_list_item(
        '',
        nodes.term('', term),
        nodes.definition('', *contents)
    )


def yes_no(b):
    return 'yes' if b else 'no'


# TODO: make cross linking by default
def make_class_stereotype(data):
    x = nodes.definition_list()

    add_df_item(x, 'Category', nodes.paragraph(text=data['parent']))
    add_df_item(x, 'Provides identity', nodes.paragraph(text=yes_no(data['provides_identity'])))
    add_df_item(x, 'Identity principle', nodes.paragraph(text=data['identity_principle']))
    add_df_item(x, 'Rigidity', nodes.paragraph(text=data['rigidity']))
    add_df_item(x, 'Dependency', nodes.paragraph(text=data['dependency']))
    add_df_item(x, 'Allowed supertypes', nodes.paragraph(text=', '.join(data['supertypes'])))
    add_df_item(x, 'Allowed subtypes', nodes.paragraph(text=', '.join(data['subtypes'])))
    add_df_item(x, 'Forbidden associations', nodes.paragraph(text=', '.join(data['forbidden_associations'])))
    add_df_item(x, 'Abstract', nodes.paragraph(text=data['abstract']))
    return x


def make_relationship_stereotype(data):
    ... # TODO


def make_aggregation_stereotype(data):
    ... # TODO


class StereotypeDirective(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    has_content = True
    add_index = True

    def run(self):
        env = self.state.document.settings.env

        doc_folder = env.srcdir
        this_folder = os.path.split(os.path.relpath(self.state.document.current_source, doc_folder))[0]
        file = os.path.join(this_folder, self.arguments[0])

        try:
            with open(file) as f:
                data = yaml.load(f)
        except:
            # TODO: log error while reading file
            data = {}

        result = []
        if 'class_stereotype' in data:
            result.append(make_class_stereotype(data['class_stereotype']))
        elif 'relationship_stereotype' in data:
            result.append(make_relationship_stereotype(data['relationship_stereotype']))
        elif 'aggregation_stereotype' in data:
            result.append(make_aggregation_stereotype(data['aggregation_stereotype']))
        else:
            ...  # TODO: log problem
        return result


def setup(app):
    app.add_directive("stereotype", StereotypeDirective)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
