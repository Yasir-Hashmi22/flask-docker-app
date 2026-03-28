import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add(client):
    response = client.get('/add?a=2&b=3')
    data = response.get_json()
    assert data['result'] == 5.0

def test_subtract(client):
    response = client.get('/subtract?a=10&b=4')
    data = response.get_json()
    assert data['result'] == 6.0

def test_multiply(client):
    response = client.get('/multiply?a=3&b=4')
    data = response.get_json()
    assert data['result'] == 12.0