from flask import Blueprint, jsonify, abort

from app.dependencies.container import container

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/", methods=["GET"])
def list_users():
    user_service = container.user_service()
    return jsonify(user_service.list_users())


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user_service = container.user_service()
    user = user_service.get_user_by_id(user_id)

    if user is None:
        abort(404, description="User not found")

    return jsonify(user)
