from flask import request, jsonify, render_template
from .schema import SampleObjectSchema


pk = 0
database = {}


def home():
    # Validate input with marshmallow
    if request.method == 'POST':
        schema = SampleObjectSchema().load(request.data)
    return render_template('plugin/index.html')


def create_todo_api():
    global pk
    if request.method == 'POST':
        todo = request.data.decode()
        database[str(pk+1)] = todo
        pk = pk + 1
        return jsonify(todo)
    return jsonify({"error": "bad request"}), 400


def retrieve_todo_api(pk=None):
    if pk and pk in list(database.keys()):
        todo = database[str(pk)]
        if todo:
            return jsonify(todo)
    return jsonify({"error": "not found"}), 404


def list_todo_api():
    todos = database
    return jsonify(todos)


def delete_todo_api(pk):
    if pk and pk in list(database.keys()):
        del database[str(pk)]
        return jsonify({}), 204
    return jsonify({"error": "not found"}), 404
