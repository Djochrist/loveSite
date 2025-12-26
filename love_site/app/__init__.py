from flask import Flask
# from flask_wtf.csrf import CSRFProtect
from .routes.home import home_bp


def create_app(config_object=None):
    """
    Create and configure the Flask application.

    Args:
        config_object: Optional configuration object.

    Returns:
        Flask app: Configured Flask application instance.
    """
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Minimal configuration (extensible)
    if config_object:
        app.config.from_object(config_object)

    # Initialize CSRF protection
    # csrf = CSRFProtect(app)

    # Register blueprints
    app.register_blueprint(home_bp)

    return app
