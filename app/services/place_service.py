# app/services/place_service.py
import uuid
from datetime import datetime
from app.persistence.data_manager import save_data, load_data
from app.services.amenity_service import AmenityService
from app.services.country_city_service import CountryCityService


class PlaceService:
    @staticmethod
    def validate_place_data(data, update=False):
        required_fields = ['name', 'description', 'address', 'latitude', 'longitude', 
                           'host_id', 'number_of_rooms', 'number_of_bathrooms', 
                           'price_per_night', 'max_guests']
        if not update:
            for field in required_fields:
                if not data.get(field):
                    raise ValueError(f"{field} cannot be empty")

        if len(data.get('name', '')) < 3:
            raise ValueError("Name must be at least 3 characters long")
        if len(data.get('description', '')) < 10 or len(data.get('address', '')) < 10:
            raise ValueError("Description and address must be at least 10 characters long")
        if data.get('price_per_night', 0) <= 0:
            raise ValueError("Price per night must be greater than zero")

    @staticmethod
    def get_all_places():
        places = load_data('places')
        return places

    @staticmethod
    def get_place_by_id(place_id):
        places = load_data('places')
        return next((place for place in places if place['id'] == place_id), None)

    @staticmethod
    def create_place(data):
        PlaceService.validate_place_data(data)

        places = load_data('places')
        if not CountryCityService.get_city_by_id(data['city_id']):
            raise ValueError("City not found")
        if any(not AmenityService.get_amenity_by_id(amenity_id) for amenity_id in data.get('amenity_ids', [])):
            raise ValueError("One or more amenities not found")

        place = {
            'id': str(uuid.uuid4()),
            'name': data['name'],
            'description': data['description'],
            'address': data['address'],
            'city_id': data['city_id'],
            'latitude': data['latitude'],
            'longitude': data['longitude'],
            'host_id': data['host_id'],
            'number_of_rooms': data['number_of_rooms'],
            'number_of_bathrooms': data['number_of_bathrooms'],
            'price_per_night': data['price_per_night'],
            'max_guests': data['max_guests'],
            'amenity_ids': data['amenity_ids'],
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        places.append(place)
        save_data('places', places)
        return place

    @staticmethod
    def update_place(place_id, data):
        PlaceService.validate_place_data(data, update=True)

        places = load_data('places')
        place = next((p for p in places if p['id'] == place_id), None)
        if place is None:
            raise ValueError("Place not found")

        # Directly assign values to each field to ensure updates are captured
        place['name'] = data.get('name', place['name'])
        place['description'] = data.get('description', place['description'])
        place['address'] = data.get('address', place['address'])
        place['latitude'] = data.get('latitude', place['latitude'])
        place['longitude'] = data.get('longitude', place['longitude'])
        place['number_of_rooms'] = data.get('number_of_rooms', place['number_of_rooms'])
        place['number_of_bathrooms'] = data.get('number_of_bathrooms', place['number_of_bathrooms'])
        place['price_per_night'] = data.get('price_per_night', place['price_per_night'])
        place['max_guests'] = data.get('max_guests', place['max_guests'])
        place['updated_at'] = datetime.now().isoformat()

        # Save the entire list of places back to the JSON file
        save_data('places', places)
        return place

    @staticmethod
    def delete_place(place_id):
        places = load_data('places')
        original_length = len(places)
        places[:] = [place for place in places if place['id'] != place_id]
        if len(places) == original_length:
            raise ValueError("Place not found")
        save_data('places', places)
        return True
