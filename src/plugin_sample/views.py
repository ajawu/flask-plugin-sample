import json
from datetime import datetime

from flask import request, jsonify
from .schema import TodoSchema


pk = 0
database = {}


def home():
    # Validate input with marshmallow
    if request.method == 'POST':
        schema = TodoSchema().load(request.data)
    return 'Hello World'


def create_todo_api():
    global pk
    if request.method == 'POST':
        todo = json.loads(request.data.decode())
        read_only_fields = {
            "id": pk+1,
            "created_at": str(datetime.now())
        }
        todo.update(read_only_fields)
        database[str(pk+1)] = todo
        pk = pk + 1
        schema = TodoSchema().load(database.get(str(pk)))
        return jsonify(schema)
    return jsonify({"error": "bad request"}), 400


def retrieve_todo_api(pk=None):
    if pk and pk in list(database.keys()):
        schema = TodoSchema().load(database.get(str(pk)))
        if schema:
            return jsonify(schema)
    return jsonify({"error": "not found"}), 404


def list_todo_api():
    schema = TodoSchema(many=True).load(database.get(str(pk)))
    return jsonify(schema)


def delete_todo_api(pk):
    if pk and pk in list(database.keys()):
        del database[str(pk)]
        return jsonify({}), 204
    return jsonify({"error": "not found"}), 404


def update_todo_api(pk):
    if pk and pk in list(database.keys()):
        todo = json.loads(request.data.decode())
        database[str(pk)].update(todo)
        schema = schema = TodoSchema().load(database.get(str(pk)))
        return jsonify(schema)
    return jsonify({"error": "not found"}), 404
