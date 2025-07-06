import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"

def test_add_success(client):
    response = client.get("/add?a=10&b=20")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["result"] == 30

def test_add_missing_params(client):
    response = client.get("/add?a=10")
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data

def test_greet(client):
    response = client.get("/greet/Laxman")
    assert response.status_code == 200
    assert response.data == b"Hello, Laxman!"

