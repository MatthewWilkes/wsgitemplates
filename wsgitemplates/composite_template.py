from base import BaseTemplate

class Composite(BaseTemplate):
    summary = "A template for WSGI composites"
    _template_dir = "templates/composite"
    required_templates = 'wsgi_package',