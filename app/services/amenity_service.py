# app/services/amenity_service.py
import uuid
from datetime import datetime
from app.persistence.data_manager import save_data, load_data

#amenities = load_data('amenities')

class AmenityService:
    @staticmethod
    def validate_amenity_name(name):
        if not name or len(name.strip()) == 0:
            raise ValueError("Amenity name cannot be empty")
        if len(name) < 3:  # Assuming you want at least 3 characters in the name
            raise ValueError("Amenity name must be at least 3 characters long")

    @staticmethod
    def get_all_amenities():
        amenities = load_data('amenities')
        return amenities

    @staticmethod
    def get_amenity_by_id(amenity_id):
        amenities = load_data('amenities')
        return next((amenity for amenity in amenities if amenity['id'] == amenity_id), None)

    @staticmethod
    def create_amenity(data):
        AmenityService.validate_amenity_name(data['name'])

        amenities = load_data('amenities')
        if any(amenity['name'] == data['name'] for amenity in amenities):
            raise ValueError("Amenity name must be unique")
        
        amenity = {
            'id': str(uuid.uuid4()),
            'name': data['name'],
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        amenities.append(amenity)
        save_data('amenities', amenities)
        return amenity

    @staticmethod
    def update_amenity(amenity_id, data):
        AmenityService.validate_amenity_name(data['name'])

        amenities = load_data('amenities')
        amenity = next((a for a in amenities if a['id'] == amenity_id), None)
        if amenity is None:
            raise ValueError("Amenity not found")

        if any(other_amenity['name'] == data['name'] and other_amenity['id'] != amenity_id for other_amenity in amenities):
            raise ValueError("Amenity name must be unique")

        # Explicitly set each field you want to update
        amenity['name'] = data.get('name', amenity['name'])
        amenity['updated_at'] = datetime.now().isoformat()

        # Save the entire amenities list back to the JSON file
        save_data('amenities', amenities)
        return amenity

    @staticmethod
    def delete_amenity(amenity_id):
        amenities = load_data('amenities')
        original_length = len(amenities)
        amenities[:] = [amenity for amenity in amenities if amenity['id'] != amenity_id]
        if len(amenities) == original_length:
            raise ValueError("Amenity not found")
        save_data('amenities', amenities)
        return True
