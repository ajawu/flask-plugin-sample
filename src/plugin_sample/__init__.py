from flask import Blueprint
from src.plugin_sample import views

plugin_bp = Blueprint('plugin_sample', __name__, url_prefix='/', template_folder='templates', static_folder='static',
                      static_url_path='assets')

# Register Views
plugin_bp.add_url_rule('/', view_func=views.home, methods=('GET', 'POST',))
plugin_bp.add_url_rule('/todo/create/', view_func=views.create_todo_api, methods=('POST',))
plugin_bp.add_url_rule('/todo/<string:pk>', view_func=views.retrieve_todo_api, methods=('GET',))
plugin_bp.add_url_rule('/todo/list/', view_func=views.list_todo_api, methods=('GET',))
plugin_bp.add_url_rule('/todo/<string:pk>/delete', view_func=views.delete_todo_api, methods=('DELETE',))
plugin_bp.add_url_rule('/todo/<string:pk>/update', view_func=views.update_todo_api, methods=('PATCH',))
