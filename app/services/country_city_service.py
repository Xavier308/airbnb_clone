# country_city_service.py
import uuid
from datetime import datetime
from app.persistence.data_manager import save_data, load_data


class CountryCityService:
    @staticmethod
    def validate_string(input_string, min_len=2):
        """Validate that the string is not empty and meets the minimum length requirement."""
        return input_string and len(input_string) >= min_len

    @staticmethod
    def initialize_countries():
        countries = load_data('countries')
        if not countries:  # Check if the countries data is empty
            countries = [
                {"code": "US", "name": "United States"},
                {"code": "CA", "name": "Canada"},
                {"code": "GB", "name": "United Kingdom"},
                {"code": "AU", "name": "Australia"},
                {"code": "PR", "name": "Puerto Rico"},
                {"code": "DO", "name": "Dominican Republic"},
                {"code": "CO", "name": "Colombia"},
                {"code": "MX", "name": "Mexico"}
            ]
            save_data('countries', countries)

    @staticmethod
    def get_all_countries():
        countries = load_data('countries')
        return countries

    @staticmethod
    def get_country_by_code(code):
        countries = load_data('countries')
        return next((country for country in countries if country['code'] == code), None)

    @staticmethod
    def get_cities_by_country_code(country_code):
        cities = load_data('cities')
        return [city for city in cities if city['country_code'] == country_code]

    @staticmethod
    def get_all_cities():
        cities = load_data('cities')
        return cities

    @staticmethod
    def get_city_by_id(city_id):
        cities = load_data('cities')
        return next((city for city in cities if city['id'] == city_id), None)

    @staticmethod
    def create_city(data):
        cities = load_data('cities')
        if not CountryCityService.get_country_by_code(data['country_code']):
            raise ValueError("Invalid country code")
        if not CountryCityService.validate_string(data['name']):
            raise ValueError("City name must be at least 2 characters long")
        if any(city['name'] == data['name'] and city['country_code'] == data['country_code'] for city in cities):
            raise ValueError("City name must be unique within the same country")

        city = {
            'id': str(uuid.uuid4()),
            'name': data['name'],
            'country_code': data['country_code'],
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        cities.append(city)
        save_data('cities', cities)
        return city

    @staticmethod
    def update_city(city_id, data):
        cities = load_data('cities')
        city = next((c for c in cities if c['id'] == city_id), None)
        if city is None:
            raise ValueError("City not found")
        if not CountryCityService.validate_string(data.get('name', city['name'])):
            raise ValueError("City name must be at least 2 characters long")
        if any(other_city['name'] == data['name'] and other_city['country_code'] == data['country_code'] and other_city['id'] != city_id for other_city in cities):
            raise ValueError("City name must be unique within the same country")

        # Directly assign values to fields
        city['name'] = data.get('name', city['name'])
        city['updated_at'] = datetime.now().isoformat()

        # Save the entire list of cities back to the JSON file
        save_data('cities', cities)
        return city

    @staticmethod
    def delete_city(city_id):
        cities = load_data('cities')
        original_length = len(cities)
        cities[:] = [city for city in cities if city['id'] != city_id]
        if len(cities) == original_length:
            raise ValueError("City not found")
        save_data('cities', cities)
        return True
