# Simple Airbnb Clone in Flask

This Flask application serves as a simple clone of Airbnb, providing a RESTful API for managing users, places, amenities, reviews, cities, and countries. It is built using Python and Flask, utilizing blueprints to organize routes and JSON files for data storage. The application offers a scalable architecture and is planned for future integration with a backend database.

## Features

- **User Management**: Create, update, delete, and retrieve user profiles.
- **Place Management**: Allows the addition, modification, deletion, and retrieval of place details.
- **Review Management**: Support for adding, updating, and deleting reviews, as well as fetching reviews for specific users or places.
- **Amenity Management**: Manage amenities that can be associated with places.
- **City Management**: Manage city details, allowing for the addition, update, and deletion of city information.
- **Country Retrieval**: Retrieve details of countries, supporting broader geographic functionalities.


## Author of this project
### **Xavier J. Cruz Santiago**

Feel free to contact me for any questions or feedback regarding this project.

## Local Setup

### To set up the project locally, follow these steps:

1. **Clone the repository:**
```bash
   git clone https://github.com/Xavier308/airbnb_clone.git
```
```bash
   cd your-repository-name
```
## Set up a virtual environment:


```bash
python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install dependencies:

```bash
pip install -r requirements.txt
```
### Initialize the application:

```bash
python run.py
```

## Structure of the APP - N tier Layer

```bash
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
```
## How to print this diagram in terminal

### Install tree dependency:
```bash
pip install tree
```
### Print the tree:
This command filter some directories and print the tree
```bash
tree -L 3 -I "__pycache__|myenv|__init__.py"
```
## Usage of the API
Here is how you can interact with the application:

### Create a user:
Send a POST request to /users with the user data in JSON format.

### Get a place:
Send a GET request to /places/<place_id> to retrieve details about a place.


## Future Plans
- Integration with a SQL or NoSQL database.
- Expansion of the API to include more complex functionalities.
- Enhancement of security features and implementation of OAuth for better security.