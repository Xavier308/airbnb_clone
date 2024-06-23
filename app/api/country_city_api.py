# country_city_api.py
from flask import Blueprint, request, jsonify
from app.services.country_city_service import CountryCityService

country_city_blueprint = Blueprint('country_city', __name__)

@country_city_blueprint.route('/countries', methods=['GET'], strict_slashes=False)
@country_city_blueprint.route('/countries/', methods=['GET'], strict_slashes=False)
def get_countries():
    return jsonify(CountryCityService.get_all_countries()), 200

@country_city_blueprint.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = CountryCityService.get_country_by_code(country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country), 200

@country_city_blueprint.route('/countries/<country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    cities = CountryCityService.get_cities_by_country_code(country_code)
    return jsonify(cities), 200

@country_city_blueprint.route('/cities', methods=['POST'], strict_slashes=False)
@country_city_blueprint.route('/cities/', methods=['POST'], strict_slashes=False)
def create_city():
    try:
        city = CountryCityService.create_city(request.json)
        return jsonify(city), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400 if 'Invalid country code' in str(e) else 409

@country_city_blueprint.route('/cities', methods=['GET'], strict_slashes=False)
@country_city_blueprint.route('/cities/', methods=['GET'], strict_slashes=False)
def get_cities():
    return jsonify(CountryCityService.get_all_cities()), 200

@country_city_blueprint.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    city = CountryCityService.get_city_by_id(city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city), 200

@country_city_blueprint.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    try:
        city = CountryCityService.update_city(city_id, request.json)
        return jsonify(city), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@country_city_blueprint.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    try:
        CountryCityService.delete_city(city_id)
        return '', 204
    except ValueError:
        return jsonify({'error': 'City not found'}), 404
