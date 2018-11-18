import os
import datarum
from datetime import datetime

__version__ = '1.0.1'
__version_full__ = __version__

def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context['insegel_version'] = __version_full__

# Returns a Wending string representation of the current date
# See https://github.com/Autophagy/datarum
# Requires html_last_updated_fmt = '%d %b %Y'
def date_to_wending(date_string):
    dt = datetime.strptime(date_string, '%d %b %Y')
    return datarum.from_date(dt).strftime('{daeg} {month} {gere}')

def add_jinja_filters(app):
    app.builder.templates.environment.filters['wending'] = date_to_wending

def setup(app):
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, 'add_html_theme'):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme('insegel', theme_path)
    app.connect('html-page-context', update_context)
    app.connect('builder-inited', add_jinja_filters)
    return {'version': '0.3.0',
            'parallel_read_safe': True}
