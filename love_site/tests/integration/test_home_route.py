import pytest
from app import create_app
from app.config import Config


@pytest.fixture
def client():
    """Fixture pour le client de test Flask."""
    app = create_app(Config)
    app.testing = True
    with app.test_client() as client:
        yield client


def test_index_get(client):
    """Test de la route GET /."""
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Un petit cadeau romantique' in resp.data


def test_index_post_with_data(client):
    """Test de la route POST / avec données de personnalisation."""
    data = {
        'lover_name': 'Marie',
        'sender_name': 'Pierre'
    }
    resp = client.post('/', data=data)
    assert resp.status_code == 200
    assert b'Messages d\'amour pour toi' in resp.data
    assert b'Marie' in resp.data  # Vérifier que le nom est personnalisé


def test_index_post_empty_lover(client):
    """Test POST avec lover vide."""
    data = {
        'lover_name': '',
        'sender_name': 'Pierre'
    }
    resp = client.post('/', data=data)
    assert resp.status_code == 200
    assert b'mon amour' in resp.data  # Valeur par défaut


def test_index_post_default_sender(client):
    """Test POST avec sender vide (devrait utiliser défaut)."""
    data = {
        'lover_name': 'Marie',
        'sender_name': ''
    }
    resp = client.post('/', data=data)
    assert resp.status_code == 200
    assert b'Djochrist' in resp.data  # Valeur par défaut


def test_index_post_no_data(client):
    """Test POST sans données."""
    resp = client.post('/')
    assert resp.status_code == 200
    # Devrait afficher le formulaire
    assert b'Un petit cadeau romantique' in resp.data
