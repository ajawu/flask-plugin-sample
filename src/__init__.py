from flask import Flask


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize plugins

    with app.app_context():

        # Register Blueprints
        from src.plugin_sample import plugin_bp
        app.register_blueprint(plugin_bp)

        return app
