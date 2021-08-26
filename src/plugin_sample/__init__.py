from flask import Blueprint
from src.plugin_sample import views

plugin_bp = Blueprint('plugin_sample', __name__, url_prefix='')

# Register Views
plugin_bp.add_url_rule('/', view_func=views.home, methods=('GET', 'POST',))
