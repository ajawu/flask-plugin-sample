import json
from datetime import datetime
from uuid import uuid4

from flask import request, jsonify, render_template
from .schema import TodoSchema

database = {}


def home():
    return render_template('')


def create_todo_api():
    schema = TodoSchema().load(request.get_json())
    database[str(uuid4().hex)] = schema
    print(database)
    return jsonify(schema)


def retrieve_todo_api(pk=None):
    try:
        return jsonify(database[pk]), 200
    except KeyError:
        return jsonify({"error": "not found"}), 404


def list_todo_api():
    schema = TodoSchema(many=True).load(database.values())
    return jsonify(schema)


def delete_todo_api(pk):
    try:
        del database[str(pk)]
        return jsonify({}), 204
    except KeyError:
        return jsonify({"error": "not found"}), 404


def update_todo_api(pk):
    try:
        schema = TodoSchema().load(request.get_json())
        database[pk] = schema
        return jsonify(schema)
    except KeyError:
        return jsonify({"error": "not found"}), 404
