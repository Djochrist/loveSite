from love_site.app import create_app
from love_site.app.config import Config

# Create the application instance
app = create_app(Config)

if __name__ == "__main__":
    # Start the server
    # Use `uv run python app/main.py` to run
    # Debug mode enabled only if configured
    debug_mode = app.config.get('DEBUG', False)
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
