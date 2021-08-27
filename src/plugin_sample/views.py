from flask import request, jsonify, render_template, url_for

database = {}


def home():
    return render_template('index.html')


def install_api():
    data = {
        "name": "Sample Plugin",
        "description": "Simple proof of concept plugin in flask",
        "sidebar_url": url_for('plugin_sample.sidebar_api', _external=True),
        "install_url": url_for('plugin_sample.install_api', _external=True),
        "template_url": url_for('plugin_sample.home', _external=True)
    }
    return jsonify(data), 200


def sidebar_api():
    data = {
        "icon": "Hello World",
        "text": "Channel name"
    }
    return jsonify(data), 200
