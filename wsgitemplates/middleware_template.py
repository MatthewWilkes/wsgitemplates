from paste.script.templates import var
import os

from base import BaseTemplate

class Middleware(BaseTemplate):
    summary = "A template for WSGI filters"
    _template_dir = "templates/middleware"
    required_templates = 'wsgi_package',

    vars = [
        var('entrypointname', 'The name of the middleware filter being created.' 
                              ' (lowercase letters only, no special chars)'),
        ]

    
    def run(self, command, output_dir, vars):
        output_dir = os.path.join(*([vars['egg'], 'src'] + vars['segs']))
        self.pre(command, output_dir, vars)
        self.write_files(command, output_dir, vars)
        self.post(command, output_dir, vars)
