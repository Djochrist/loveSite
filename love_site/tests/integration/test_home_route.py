import pytest
from app import create_app
from app.config import Config


@pytest.fixture
def client():
    """Fixture for Flask test client."""
    app = create_app(Config)
    app.testing = True
    with app.test_client() as client:
        yield client


def test_index_get(client):
    """Test GET / route."""
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'A small romantic gift' in resp.data


def test_index_post_with_data(client):
    """Test POST / route with personalization data."""
    data = {
        'lover_name': 'Marie',
        'sender_name': 'Pierre'
    }
    resp = client.post('/', data=data)
    assert resp.status_code == 200
    assert b'Love messages for you' in resp.data
    assert b'Marie' in resp.data  # Verify name is personalized


def test_index_post_empty_lover(client):
    """Test POST with empty lover."""
    data = {
        'lover_name': '',
        'sender_name': 'Pierre'
    }
    resp = client.post('/', data=data)
    assert resp.status_code == 200
    assert b'my love' in resp.data  # Default value


def test_index_post_default_sender(client):
    """Test POST with empty sender (should use default)."""
    data = {
        'lover_name': 'Marie',
        'sender_name': ''
    }
    resp = client.post('/', data=data)
    assert resp.status_code == 200
    assert b'Djochrist' in resp.data  # Default value


def test_index_post_no_data(client):
    """Test POST without data."""
    resp = client.post('/')
    assert resp.status_code == 200
    # Should display the form
    assert b'A small romantic gift' in resp.data
