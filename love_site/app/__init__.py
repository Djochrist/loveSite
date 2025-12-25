from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .routes.home import home_bp


def create_app(config_object=None):
    """
    Crée et configure l'application Flask.

    Args:
        config_object: Objet de configuration optionnel.

    Returns:
        Flask app: Instance configurée de l'application.
    """
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Configuration minimale (extensible)
    if config_object:
        app.config.from_object(config_object)

    # Initialisation de la protection CSRF
    csrf = CSRFProtect(app)

    # Enregistrement des blueprints
    app.register_blueprint(home_bp)

    return app
