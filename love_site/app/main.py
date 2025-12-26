from . import create_app
from .config import Config, DevelopmentConfig, ProductionConfig
import os

# Determine which config to use
config_name = os.environ.get('FLASK_ENV', 'development')
config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': Config
}

config_class = config_map.get(config_name, Config)

# Create the application instance
app = create_app(config_class)

if __name__ == "__main__":
    # Start the server
    # Use `uv run python app/main.py` to run
    # Debug mode enabled only if configured
    debug_mode = app.config.get('DEBUG', False)
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)), debug=debug_mode)
