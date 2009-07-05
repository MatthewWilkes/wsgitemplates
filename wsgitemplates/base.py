from paste.script import templates

class BaseTemplate(templates.Template):
    """A basetemplate for creating WSGI applications"""

    def run(self, command, output_dir, vars):
        templates.Template.run(self, command, output_dir, vars)

    def post(self, *args, **kargs):
        templates.Template.post(self, *args, **kargs)

