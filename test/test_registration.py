from app import app
import json


def test_user_existing_register():
    data={
        "name":"shreyas mohite",
        "email":"shreyas123@gmail.com",
        "password":"shreyas123",
        "confirm_password":"shreyas123"
    }
    response = app.test_client().post("/register", data=json.dumps(data),
                headers={"Content-Type": "application/json"})
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 404


def test_new_register():
    data={
        "name":"shreyas mohite",
        "email":"shreyas1123@gmail.com",
        "password":"shreyas123",
        "confirm_password":"shreyas123"
    }
    response = app.test_client().post("/register", data=json.dumps(data),
                headers={"Content-Type": "application/json"})
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 201


def test_login_new_user():
    global token
    data={
        "email":"shreyas1123@gmail.com",
        "password":"shreyas123"
    }
    response = app.test_client().post("/login", data=json.dumps(data),
                headers={"Content-Type": "application/json"})
    data = json.loads(response.data.decode("utf-8"))
    token = data['token']
    assert response.status_code == 200


def test_update_new_user():
    data={
        "name":"jhoncena",
    }
    response = app.test_client().put("/register", data=json.dumps(data),
                headers={"Content-Type": "application/json",
                         "Authorization":f'Bearer {token}'})
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200


def test_delete_new_user():
    response = app.test_client().delete("/register",
                headers={"Content-Type": "application/json",
                        "Authorization":f'Bearer {token}'})
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
