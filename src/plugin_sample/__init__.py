from flask import Blueprint
from src.plugin_sample import views

plugin_bp = Blueprint('plugin_sample', __name__, url_prefix='/', template_folder='templates',
                      static_folder='static/build', static_url_path='static')

# Register Views
plugin_bp.add_url_rule('/', view_func=views.home, methods=('GET', 'POST',))
plugin_bp.add_url_rule('/sidebar', view_func=views.sidebar_api, methods=('GET',))
plugin_bp.add_url_rule('/activate', view_func=views.activate_api, methods=('GET',))
