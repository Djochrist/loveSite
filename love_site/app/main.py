from love_site.app import create_app
from love_site.app.config import Config

# Création de l'instance de l'application
app = create_app(Config)

if __name__ == "__main__":
    # Lancement du serveur
    # Utilisez `uv run python app/main.py` pour lancer
    # Debug activé seulement si configuré
    debug_mode = app.config.get('DEBUG', False)
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
