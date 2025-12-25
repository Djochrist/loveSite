import pytest
from app import create_app
from app.config import Config


def test_app_creation():
    """Test de la création de l'application."""
    app = create_app(Config)
    assert app is not None
    assert app.config['TESTING'] is False  # Par défaut


def test_app_creation_with_config():
    """Test création avec configuration personnalisée."""
    class TestConfig:
        TESTING = True
        DEBUG = True

    app = create_app(TestConfig)
    assert app.config['TESTING'] is True
    assert app.config['DEBUG'] is True


def test_blueprints_registered():
    """Test que les blueprints sont enregistrés."""
    app = create_app(Config)
    # Vérifier que le blueprint home est enregistré
    assert 'home' in [bp.name for bp in app.blueprints.values()]


def test_static_files():
    """Test accès aux fichiers statiques."""
    app = create_app(Config)
    with app.test_client() as client:
        resp = client.get('/static/css/style.css')
        assert resp.status_code == 200
        assert b'--bg:' in resp.data  # Vérifier contenu CSS


def test_template_rendering():
    """Test rendu des templates."""
    app = create_app(Config)
    with app.test_client() as client:
        resp = client.get('/')
        assert resp.status_code == 200
        # Vérifier éléments clés
        assert b'Cadeau d\'amour' in resp.data
        assert b'heart' in resp.data  # Overlay hearts
