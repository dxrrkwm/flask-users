from flask import Blueprint, jsonify, request, Response

from app.extensions import db
from app.models import User
from app.schemas import UserSchema


user_bp = Blueprint("user", __name__, url_prefix="/users")
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_bp.route("", methods=["GET"])
def get_users() -> tuple[Response, int]:
    users: list[User] = User.query.all()
    result: list[dict] = users_schema.dump(users)
    return jsonify(result), 200


@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int) -> tuple[Response, int]:
    user: User = User.query.get_or_404(user_id)
    result: dict = user_schema.dump(user)
    return jsonify(result), 200


@user_bp.route("", methods=["POST"])
def create_user() -> tuple[Response, int]:
    try:
        user: User = user_schema.load(request.json)

        existing_user: User | None = User.query.filter_by(email=user.email).first()
        if existing_user:
            return jsonify({"message": "Email already registered"}), 409

        db.session.add(user)
        db.session.commit()

        result: dict = user_schema.dump(user)
        return jsonify(result), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id: int) -> tuple[Response, int]:
    try:
        user: User = User.query.get_or_404(user_id)

        data: dict = request.json

        if "email" in data and data["email"] != user.email:
            existing_user: User | None = User.query.filter_by(email=data["email"]).first()
            if existing_user:
                return jsonify({"message": "Email already registered"}), 409

        if "name" in data:
            user.name = data["name"]
        if "email" in data:
            user.email = data["email"]

        db.session.commit()

        result: dict = user_schema.dump(user)
        return jsonify(result), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400


@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int) -> tuple[Response, int]:
    try:
        user: User = User.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "User deleted successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 400
