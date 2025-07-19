from app import app
import pytest



def test_home():
    app.testing = True
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.data == b"Hello World!"