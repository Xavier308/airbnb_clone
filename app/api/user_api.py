# app/api/user_api.py
from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

# Defines a blueprint for all user-related API endpoints.
user_blueprint = Blueprint('users', __name__)

# API endpoint for creating a new user.
# It handles requests to "/users" and "/users/" using POST method.
@user_blueprint.route('/users', methods=['POST'], strict_slashes=False)
@user_blueprint.route('/users/', methods=['POST'], strict_slashes=False)
def create_user():
    try:
        # Extracts user data from request, creates a user,
        # and returns the new user data.
        user = UserService.create_user(request.json)
        return jsonify(user), 201
    except ValueError as e:
        # Returns an error response if there's an issue, such as an invalid email.
        return jsonify({'error': str(e)}), 400 if 'Invalid email' in str(e) else 409

# API endpoint to retrieve all users.
# It handles GET requests to both "/users" and "/users/".
@user_blueprint.route('/users', methods=['GET'], strict_slashes=False)
@user_blueprint.route('/users/', methods=['GET'], strict_slashes=False)
def get_users():
    # Returns a list of all users.
    return jsonify(UserService.get_all_users()), 200

# API endpoint to retrieve a specific user by their user_id.
@user_blueprint.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.find_user(user_id)
    if not user:
        # Finds the user; if not found, returns an error.
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200
# API endpoint to update a user's information.
@user_blueprint.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        # Updates the user data for the specified user_id with 
        # the provided JSON data.
        user = UserService.update_user(user_id, request.json)
        return jsonify(user), 200
    except ValueError as e:
        # If the user cannot be found, returns a 404 error.
        return jsonify({'error': str(e)}), 404

# API endpoint to delete a user.
@user_blueprint.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Deletes the user with the specified user_id.
        UserService.delete_user(user_id)
        return '', 204
    except ValueError:
        # If the user cannot be found, returns a 404 error.
        return jsonify({'error': 'User not found'}), 404

# How to consume this api in Postman
'''
{
  "email": "developer@spacex.com", # Valid & unique email
  "first_name": "Yu",              # At least 2 Characters
  "last_name": "Li",               # At least 2 characters
  "password": "1123"               # At least 4 characters
}

# How to consume this api with curl


'''
