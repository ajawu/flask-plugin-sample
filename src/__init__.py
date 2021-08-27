from flask import Flask, jsonify
from marshmallow import ValidationError


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize plugins

    with app.app_context():

        # Register Blueprints
        from src.plugin_sample import plugin_bp
        app.register_blueprint(plugin_bp)

        # Error Handlers
        @app.errorhandler(ValidationError)
        def handle_marshmallow_validation_errors(err):
            return {'error': err.messages, 'data': err.valid_data}, 400

        return app
