import json

from flask.testing import FlaskClient
from sqlalchemy import select

from app.extensions import db
from app.models import User


def test_health_check(client: FlaskClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_create_user(client: FlaskClient, db: db) -> None:
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

    stmt = select(User).where(User.email == "test@example.com")
    user: User | None = db.session.execute(stmt).scalar_one_or_none()
    assert user is not None
    assert user.name == "Test User"


def test_get_users(client: FlaskClient, db: db) -> None:
    user1 = User(name="User 1", email="user1@example.com")
    user2 = User(name="User 2", email="user2@example.com")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json) == 2


def test_get_user(client: FlaskClient, db: db) -> None:
    user = User(name="Test User", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json.get("name") == "Test User"
    assert response.json.get("email") == "test@example.com"


def test_update_user(client: FlaskClient, db: db) -> None:
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

    stmt = select(User).where(User.id == user.id)
    updated_user = db.session.execute(stmt).scalar_one()
    assert updated_user.name == "New Name"
    assert updated_user.email == "new@example.com"


def test_delete_user(client: FlaskClient, db: db) -> None:
    user = User(name="Test User", email="test@example.com")
    db.session.add(user)
    db.session.commit()

    response = client.delete(f"/users/{user.id}")
    assert response.status_code == 200

    stmt = select(User).where(User.id == user.id)
    deleted_user = db.session.execute(stmt).scalar_one_or_none()
    assert deleted_user is None
