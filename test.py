import pytest
import requests
import app

from app import app as flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def app():
    yield flask_app


def test_hello_world(app, client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"
    #assert response.get_data(as_text=True) == 'Hello Stranger'


def test_wiki_search(app, client):
    response = client.get("/helloworld?name=AlfredNeumann")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"
    assert response.get_data(as_text=True) == 'Hello Alfred Neumann'
    response = client.get("/helloworld?name=AlfredENeumann")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"
    assert response.get_data(as_text=True) == "Hello Alfred E Neumann"
    response = client.get("/helloworld?name=ABC")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"
    assert response.get_data(as_text=True) == "Hello A B C"


