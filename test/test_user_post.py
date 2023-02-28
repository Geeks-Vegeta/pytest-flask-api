from app import app
import json


def test_login_user():
    global token
    data={
        "email":"shreyas12@gmail.com",
        "password":"shreyas!123"
    }
    response = app.test_client().post("/login", data=json.dumps(data),
                headers={"Content-Type": "application/json"})
    data = json.loads(response.data.decode("utf-8"))
    token = data['token']
    assert response.status_code == 200


def test_add_post():
    data={
        "title": "hello bhai",
        "body": "hello"
    }
    response = app.test_client().post("/post", data=json.dumps(data),
                headers={"Content-Type": "application/json",
                         "Authorization":f'Bearer {token}'})
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 201


def test_update_post():
    data={
        "title": "hello shreyas",
        "body": "hello"
    }
    response = app.test_client().put("/post?title_name=hello bhai", data=json.dumps(data),
                headers={"Content-Type": "application/json",
                         "Authorization":f'Bearer {token}'})
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200


def test_delete_post():
    response = app.test_client().delete("/post?title_name=hello shreyas",
                headers={"Content-Type": "application/json",
                         "Authorization":f'Bearer {token}'})
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200