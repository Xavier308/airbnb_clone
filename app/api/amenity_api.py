# app/api/amenity_api.py
from flask import Blueprint, request, jsonify
from app.services.amenity_service import AmenityService

amenity_blueprint = Blueprint('amenities', __name__)

@amenity_blueprint.route('/amenities', methods=['POST'], strict_slashes=False)
@amenity_blueprint.route('/amenities/', methods=['POST'], strict_slashes=False)
def create_amenity():
    try:
        amenity = AmenityService.create_amenity(request.json)
        return jsonify(amenity), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400 if 'Duplicate' in str(e) else 409

@amenity_blueprint.route('/amenities', methods=['GET'], strict_slashes=False)
@amenity_blueprint.route('/amenities/', methods=['GET'], strict_slashes=False)
def get_amenities():
    return jsonify(AmenityService.get_all_amenities()), 200

@amenity_blueprint.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = AmenityService.get_amenity_by_id(amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity), 200

@amenity_blueprint.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    try:
        amenity = AmenityService.update_amenity(amenity_id, request.json)
        return jsonify(amenity), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@amenity_blueprint.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    try:
        AmenityService.delete_amenity(amenity_id)
        return '', 204
    except ValueError:
        return jsonify({'error': 'Amenity not found'}), 404
