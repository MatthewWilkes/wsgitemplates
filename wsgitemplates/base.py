import os

from paste.script import templates

class BaseTemplate(templates.Template):
    """A basetemplate for creating WSGI applications"""
    
    use_cheetah = True
    
    def run(self, command, output_dir, vars):
        output_dir = os.path.join(*([vars['egg'], 'src'] + vars['segs']))
        self.pre(command, output_dir, vars)
        self.write_files(command, output_dir, vars)
        self.post(command, output_dir, vars)

    def post(self, *args, **kargs):
        templates.Template.post(self, *args, **kargs)

    def getEntrypoints(self, vars):
        return "[%s]\n%s = %s:%s" % (self.entrypoint_type,
                                     vars['entrypoint_name'],
                                     vars['egg'],
                                     vars['entrypoint_name'].title()+'Factory')
