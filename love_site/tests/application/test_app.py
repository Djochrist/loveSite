import pytest
from app import create_app
from app.config import Config


def test_app_creation():
    """Test application creation."""
    app = create_app(Config)
    assert app is not None
    assert app.config['TESTING'] is False  # Default


def test_app_creation_with_config():
    """Test creation with custom configuration."""
    class TestConfig:
        TESTING = True
        DEBUG = True

    app = create_app(TestConfig)
    assert app.config['TESTING'] is True
    assert app.config['DEBUG'] is True


def test_blueprints_registered():
    """Test that blueprints are registered."""
    app = create_app(Config)
    # Verify that the home blueprint is registered
    assert 'home' in [bp.name for bp in app.blueprints.values()]


def test_static_files():
    """Test access to static files."""
    app = create_app(Config)
    with app.test_client() as client:
        resp = client.get('/static/css/style.css')
        assert resp.status_code == 200
        assert b'--bg:' in resp.data  # Verify CSS content


def test_template_rendering():
    """Test template rendering."""
    app = create_app(Config)
    with app.test_client() as client:
        resp = client.get('/')
        assert resp.status_code == 200
        # Verify key elements
        assert b'Love Gift' in resp.data
        assert b'heart' in resp.data  # Heart overlay
