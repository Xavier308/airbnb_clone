# app/api/place_api.py
from flask import Blueprint, request, jsonify
from app.services.place_service import PlaceService

place_blueprint = Blueprint('places', __name__)

@place_blueprint.route('/places', methods=['POST'], strict_slashes=False)
@place_blueprint.route('/places/', methods=['POST'], strict_slashes=False)
def create_place():
    try:
        place = PlaceService.create_place(request.json)
        return jsonify(place), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400 if 'City not found' in str(e) or 'Amenities not found' in str(e) else 409

@place_blueprint.route('/places', methods=['GET'], strict_slashes=False)
@place_blueprint.route('/places/', methods=['GET'], strict_slashes=False)
def get_places():
    return jsonify(PlaceService.get_all_places()), 200

@place_blueprint.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = PlaceService.get_place_by_id(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place), 200

@place_blueprint.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    try:
        place = PlaceService.update_place(place_id, request.json)
        return jsonify(place), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@place_blueprint.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    try:
        PlaceService.delete_place(place_id)
        return '', 204
    except ValueError:
        return jsonify({'error': 'Place not found'}), 404
