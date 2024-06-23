from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, host_id, name, description, number_of_rooms, number_of_bathrooms, max_guests, price_per_night, latitude, longitude, city_id, amenity_ids=[]):
        super().__init__()
        self.host_id = host_id
        self.name = name
        self.description = description
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.amenity_ids = amenity_ids

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'host_id': self.host_id,
            'name': self.name,
            'description': self.description,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'max_guests': self.max_guests,
            'price_per_night': self.price_per_night,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'city_id': self.city_id,
            'amenity_ids': self.amenity_ids
        })
        return data

'''
# JSON example for POST in postman
# Remember to use a valid city_id
{
  "host_id": "233333",
  "name": "Maison Blue",
  "description": "A beautiful place by the sea.",
  "address": "369 Ocean View Drive",
  "number_of_rooms": 3,
  "number_of_bathrooms": 1,
  "max_guests": 6,
  "price_per_night": 150,
  "latitude": 18.4655,
  "longitude": -66.1057,
  "city_id": "c4d9240d-6d99-487f-9421-ef6a22a85197",
  "amenity_ids": []
}
'''