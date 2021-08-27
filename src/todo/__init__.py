from flask import Blueprint
from src.todo import views

todo_bp = Blueprint('todo', __name__, url_prefix='/todo', template_folder='templates', static_folder='static',
                    static_url_path='assets')

todo_bp.add_url_rule('/create', view_func=views.create_todo, methods=('POST',))
todo_bp.add_url_rule('/<string:pk>', view_func=views.retrieve_todo, methods=('GET',))
todo_bp.add_url_rule('/list', view_func=views.list_todo, methods=('GET',))
todo_bp.add_url_rule('/<string:pk>/delete', view_func=views.delete_todo, methods=('DELETE',))
todo_bp.add_url_rule('/<string:pk>/update', view_func=views.update_todo, methods=('PATCH',))
