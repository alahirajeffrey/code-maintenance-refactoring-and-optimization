def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_list_users(client):
    response = client.get("/users/")

    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

    user = data[0]
    assert "id" in user
    assert "first_name" in user
    assert "last_name" in user


def test_get_user_by_id_success(client):
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.get_json() == {
        "id": 1,
        "first_name": "John",
        "last_name": "Shinggu",
    }


def test_get_user_by_id_not_found(client):
    response = client.get("/users/999")

    assert response.status_code == 404
