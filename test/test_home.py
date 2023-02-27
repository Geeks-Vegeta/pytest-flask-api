from app import app
import json


def test_home():
    response = app.test_client().get("/")
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200