from love_site.app import create_app
from love_site.app.config import Config

app = create_app(Config)
# Ensure SECRET_KEY is set for Flask-WTF CSRF
app.config['SECRET_KEY'] = app.config.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['WTF_CSRF_SECRET_KEY'] = app.config.get('WTF_CSRF_SECRET_KEY', app.config['SECRET_KEY'])
