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
    """Test GET / route displays messages directly."""
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Love Messages for Bae' in resp.data
    assert b'From Djochrist with love' in resp.data
    assert b'bae' in resp.data  # Verify hardcoded lover name
    assert b'Djochrist' in resp.data  # Verify hardcoded sender name
