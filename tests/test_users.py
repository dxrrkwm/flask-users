import json

from app.models import User


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_create_user(client, db):
    data = {
        "name": "Test User",
        "email": "test@example.com"
    }
    response = client.post(
        "/users",
        data=json.dumps(data),
        content_type="application/json"
    )
    assert response.status_code == 201

    assert response.json.get("name") == "Test User"
    assert response.json.get("email") == "test@example.com"
    assert "id" in response.json
    assert "created_at" in response.json

    user = User.query.filter_by(email="test@example.com").first()
    assert user is not None
    assert user.name == "Test User"


def test_get_users(client, db):
    user1 = User(name="User 1", email="user1@example.com")
    user2 = User(name="User 2", email="user2@example.com")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json) == 2


def test_get_user(client, db):
    user = User(name="Test User", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json.get("name") == "Test User"
    assert response.json.get("email") == "test@example.com"


def test_update_user(client, db):
    user = User(name="Old Name", email="old@example.com")
    db.session.add(user)
    db.session.commit()

    data = {
        "name": "New Name",
        "email": "new@example.com"
    }
    response = client.put(
        f"/users/{user.id}",
        data=json.dumps(data),
        content_type="application/json"
    )
    assert response.status_code == 200

    updated_user = User.query.get(user.id)
    assert updated_user.name == "New Name"
    assert updated_user.email == "new@example.com"


def test_delete_user(client, db):
    user = User(name="Test User", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    response = client.delete(f"/users/{user.id}")
    assert response.status_code == 200

    deleted_user = User.query.get(user.id)
    assert deleted_user is None
