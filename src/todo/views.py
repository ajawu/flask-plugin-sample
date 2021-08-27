from uuid import uuid4

from flask import request, jsonify, render_template, url_for
from .schema import TodoSchema

database = {}


def create_todo():
    schema = TodoSchema().load(request.get_json())
    database[str(uuid4().hex)] = schema
    return jsonify(schema)


def list_todo():
    return database


def retrieve_todo(pk=None):
    try:
        return jsonify(database[pk]), 200
    except KeyError:
        return jsonify({"error": "not found"}), 404


def delete_todo(pk=None):
    try:
        del database[str(pk)]
        return jsonify({"msg": "TODO item deleted"}), 204
    except KeyError:
        return jsonify({"error": "not found"}), 404


def update_todo(pk=None):
    if pk in database:
        schema = TodoSchema().load(request.get_json())
        database[pk] = schema
        return jsonify(schema)
    else:
        return jsonify({"error": "not found"}), 404
