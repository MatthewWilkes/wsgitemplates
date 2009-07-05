from base import BaseTemplate

class Middleware(BaseTemplate):
    summary = "A template for WSGI filters"
    _template_dir = "templates/middleware"
    required_templates = 'wsgi_package',