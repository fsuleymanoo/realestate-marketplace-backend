from flask import Blueprint, request, jsonify
from app.utils.validators import is_valid_email, is_valid_username, is_valid_password
from app.services.auth_service import AuthService


auth_bp =Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if 'email' not in data or not data.get('email'):
        return jsonify({"error": "email property cannot be empty or missing"}), 400
    
    if not is_valid_email(data.get('email')):
        return jsonify({"error": f"Invalid email format {data.get('email')}"}), 400
    
    if 'username' not in data or not data.get('username'):
        return jsonify({"error": "username property cannot be empty or missing"}), 400
    
    if not is_valid_username(data.get('username')):
        return jsonify({"error": f"Invalid username format {data.get('username')}"}), 400
    
    if 'password' not in data or not data.get('password'):
        return jsonify({"error": "password property cannot be empty or missing"}), 400
    
    if not is_valid_password(data.get('password')):
        return jsonify({"error": f"Invalid password format {data.get('password')}"}), 400
    
    try:
        user = AuthService.register(**data)
        return jsonify({"message": "User successfully created!", "user": user.serialize()})
    except ValueError as e:
        return jsonify({"error": "Registration failed", "message": str(e)}), 400
    


  