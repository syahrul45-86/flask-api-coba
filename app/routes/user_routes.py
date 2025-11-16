from flask import Blueprint, request, jsonify
from app.controllers.user_controller import UserController

user_bp = Blueprint("user_bp", __name__)

@user_bp.get("/")
def get_all_users():
    return jsonify(UserController.get_all())

@user_bp.get("/<int:id>")
def get_user(id):
    user = UserController.get_by_id(id)
    return jsonify(user) if user else ({"error": "User not found"}, 404)

@user_bp.post("/")
def create_user():
    return jsonify(UserController.create(request.json)), 201

@user_bp.put("/<int:id>")
def update_user(id):
    result = UserController.update(id, request.json)
    return jsonify(result) if result else ({"error": "User not found"}, 404)

@user_bp.delete("/<int:id>")
def delete_user(id):
    result = UserController.delete(id)
    return jsonify({"message": "deleted"}) if result else ({"error": "User not found"}, 404)
