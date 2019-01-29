from docutils import nodes
from docutils.parsers.rst import Directive


class LimitationDirective(Directive):
    
    #define the parameters the directive expects
    required_arguments = 0
    optional_arguments = 0

    #A boolean, indicating if the final argument may contain whitespace
    final_argument_whitespace = True
    option_spec = {}
    has_content = True

    def run(self):
        # Raise an error if the directive does not have contents.
        self.assert_has_content()
        text = '\n'.join(self.content)
        # Create the limitation node, to be populated by `nested_parse`.
        limitation_node = nodes.paragraph(rawsource=text)
        # Parse the directive contents.
        self.state.nested_parse(self.content, self.content_offset, limitation_node)
        return [limitation_node]

class Limitation(LimitationDirective):
    pass

def setup(app):
    app.add_directive("limitation", LimitationDirective)
