from base import BaseTemplate

class Endpoint(BaseTemplate):
    summary = "A template for WSGI applications"
    _template_dir = "templates/endpoint"
    required_templates = 'wsgi_package',