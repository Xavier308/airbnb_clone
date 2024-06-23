README


'''bash
tree -L 3 -I "__pycache__|myenv|__init__.py"
'''
## Structure of my app
'''bash
.
├── app
│   ├── api
│   │   ├── amenity_api.py
│   │   ├── country_city_api.py
│   │   ├── place_api.py
│   │   ├── review_api.py
│   │   └── user_api.py
│   ├── models
│   │   ├── amenity.py
│   │   ├── base_model.py
│   │   ├── city.py
│   │   ├── country.py
│   │   ├── place.py
│   │   ├── review.py
│   │   └── user.py
│   ├── persistence
│   │   └── data_manager.py
│   └── services
│       ├── amenity_service.py
│       ├── country_city_service.py
│       ├── place_service.py
│       ├── review_service.py
│       └── user_service.py
├── assets
├── instance
│   ├── config.py
│   └── json_data
│       ├── amenities.json
│       ├── cities.json
│       ├── countries.json
│       ├── places.json
│       ├── reviews.json
│       └── users.json
├── README.md
├── requirements.txt
├── run.py
└── tests
'''