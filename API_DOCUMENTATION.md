# API Documentation for Simple Airbnb-Clone in Flask
 **By Xavier J. Cruz**

## How to consume the API

## Table of Contents

- [User Endpoints](#user-endpoints)
- [Place Endpoints](#place-endpoints)
- [Country and City Enpoints](#country-and-city-endpoints)
- [Reviews Endpoints](#review-endpoints)
- [Amenity Endpoints](#amenity-endpoints)


## User Endpoints

### Create User
- URL: /users
- Method: POST
- Data Params:
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "password": "securePassword123"
}
```
- Success Response:
- Code: 201 CREATED
- **Content:**
```json
{
  "id": "uuid-generated-id",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```
- Error Response:
- Code: 400 BAD REQUEST
- Content: {"error": "Invalid email format"}
- Code: 409 CONFLICT
- Content: {"error": "Email must be unique"}

### Sample Call:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "password": "securePassword123"}' http://localhost:5000/users
```
## Get All Users

**URL:** `/users`

**Method:** `GET`

### Success Response:

- **Code:** 200 OK
- **Content:**
  ```json
  [
    {
      "id": "uuid",
      "first_name": "John",
      "last_name": "Doe",
      "email": "john@example.com",
      "created_at": "2024-01-01T12:00:00Z",
      "updated_at": "2024-01-01T12:00:00Z"
    },
    {...}
  ]

### Sample Call:
```bash
curl -X GET http://localhost:5000/users
```

Get User by ID
URL: /users/<user_id>
Method: GET
URL Params:
Required: user_id=[uuid]
Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "uuid",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```
Error Response:
Code: 404 NOT FOUND
Content: {"error": "User not found"}

### Sample Call:
```bash
curl -X GET http://localhost:5000/users/uuid
```

Update User
URL: /users/<user_id>
Method: PUT
URL Params:
Required: user_id=[uuid]

Data Params:
```json
{
  "first_name": "Jane",
  "last_name": "Doe"
}
```

Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "uuid",
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "john@example.com",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 404 NOT FOUND
Content: {"error": "User not found"}
Sample Call:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"first_name": "Jane", "last_name": "Doe"}' http://localhost:5000/users/uuid
```

Delete User

URL: /users/<user_id>
Method: DELETE
URL Params:
Required: user_id=[uuid]
Success Response:
Code: 204 NO CONTENT
Error Response:
Code: 404 NOT FOUND
Content: {"error": "User not found"}

### Sample Call:
```bash
curl -X DELETE http://localhost:5000/users/uuid
```

## Place Endpoints

Create Place
URL: /places
Method: POST

Data Params:
```json

{
  "name": "Lovely Studio",
  "description": "Spacious studio with great views",
  "address": "123 Beach Ave, Miami, FL",
  "city_id": "city-uuid",
  "latitude": 25.7617,
  "longitude": -80.1918,
  "host_id": "host-uuid",
  "number_of_rooms": 1,
  "number_of_bathrooms": 1,
  "price_per_night": 120,
  "max_guests": 2,
  "amenity_ids": ["amenity-uuid1", "amenity-uuid2"]
}
```

Success Response:
Code: 201 CREATED

- **Content:**
```json
{
  "id": "uuid",
  "name": "Lovely Studio",
  "description": "Spacious studio with great views",
  "address": "123 Beach Ave, Miami, FL",
  "city_id": "city-uuid",
  "latitude": 25.7617,
  "longitude": -80.1918,
  "host_id": "host-uuid",
  "number_of_rooms": 1,
  "number_of_bathrooms": 1,
  "price_per_night": 120,
  "max_guests": 2,
  "amenity_ids": ["amenity-uuid1", "amenity-uuid2"],
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 400 BAD REQUEST
Content: {"error": "City not found"} or {"error": "One or more amenities not found"}

### Sample Call:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Lovely Studio", "description": "Spacious studio with great views", "address": "123 Beach Ave, Miami, FL", 
"city_id": "city-uuid", "latitude": 25.7617, "longitude": -80.1918", "host_id": "host-uuid", "number_of_rooms": 1, "number_of_bathrooms": 1, "price_per_night": 120, "max_guests": 2, "amenity_ids": ["amenity-uuid1", "amenity-uuid2"]}' http://localhost:5000/places
```

Get All Places
URL: /places
Method: GET
Success Response:
Code: 200 OK

- **Content:**
```json

[
  {
    "id": "uuid",
    "name": "Lovely Studio",
    "description": "Spacious studio with great views",
    "address": "123 Beach Ave, Miami, FL",
    "city_id": "city-uuid",
    "latitude": 25.7617,
    "longitude": -80.1918,
    "host_id": "host-uuid",
    "number_of_rooms": 1,
    "number_of_bathrooms": 1,
    "price_per_night": 120,
    "max_guests": 2,
    "amenity_ids": ["amenity-uuid1", "amenity-uuid2"],
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  },
  // More places...
]
```

### Sample Call:
```bash
curl -X GET http://localhost:5000/places
```

Get Place by ID
URL: /places/<place_id>
Method: GET
URL Params:
Required: place_id=[uuid]
Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "uuid",
  "name": "Lovely Studio",
  "description": "Spacious studio with great views",
  "address": "123 Beach Ave, Miami, FL",
  "city_id": "city-uuid",
  "latitude": 25.7617,
  "longitude": -80.1918,
  "host_id": "host-uuid",
  "number_of_rooms": 1,
  "number_of_bathrooms": 1,
  "price_per_night": 120,
  "max_guests": 2,
  "amenity_ids": ["amenity-uuid1", "amenity-uuid2"],
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 404 NOT FOUND
Content: {"error": "Place not found"}

### Sample Call:
```bash
curl -X GET http://localhost:5000/places/uuid
```

Update Place
URL: /places/<place_id>
Method: PUT
URL Params:
Required: place_id=[uuid]

Data Params:
```json
{
  "name": "Updated Studio",
  "description": "Updated description",
  "address": "Updated Address, Miami, FL",
  "number_of_rooms": 2
}
```

Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "uuid",
  "name": "Updated Studio",
  "description": "Updated description",
  "address": "Updated Address, Miami, FL",
  "city_id": "city-uuid",
  "latitude": 25.7617,
  "longitude": -80.1918,
  "host_id": "host-uuid",
  "number_of_rooms": 2,
  "number_of_bathrooms": 1,
  "price_per_night": 120,
  "max_guests": 2,
  "amenity_ids": ["amenity-uuid1", "amenity-uuid2"],
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```
Error Response:
Code: 404 NOT FOUND
Content: {"error": "Place not found"}

### Sample Call:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Studio", "description": "Updated description", "address": "Updated Address, Miami, FL", "number_of_rooms": 2}' http://localhost:5000/places/uuid
```

Delete Place
URL: /places/<place_id>
Method: DELETE
URL Params:
Required: place_id=[uuid]
Success Response:
Code: 204 NO CONTENT
Error Response:
Code: 404 NOT FOUND
Content: {"error": "Place not found"}

### Sample Call:
```bash
curl -X DELETE http://localhost:5000/places/uuid
```

## Country and City Endpoints

Get All Countries
URL: /countries
Method: GET
Success Response:
Code: 200 OK

- **Content:**
```json
[
  {"code": "US", "name": "United States"},
  {"code": "CA", "name": "Canada"},
  // More countries...
]
```

### Sample Call:
```bash
curl -X GET http://localhost:5000/countries
```

Get Country by Code
URL: /countries/<country_code>
Method: GET
URL Params:
Required: country_code=[string]
Success Response:
Code: 200 OK

- **Content:**
```json
{
  "code": "US",
  "name": "United States"
}
```

Error Response:
Code: 404 NOT FOUND
Content: {"error": "Country not found"}

### Sample Call:
```bash
curl -X GET http://localhost:5000/countries/US
```

Get Cities by Country Code
URL: /countries/<country_code>/cities
Method: GET
URL Params:
Required: country_code=[string]
Success Response:
Code: 200 OK

- **Content:**
```json
[
  {"id": "city-uuid", "name": "Miami", "country_code": "US"},
  // More cities...
]
```

### Sample Call:
```bash
curl -X GET http://localhost:5000/countries/US/cities
```

Create City
URL: /cities
Method: POST

Data Params:
```json
{
  "name": "New City",
  "country_code": "US"
}
```

Success Response:
Code: 201 CREATED

- **Content:**
```json
{
  "id": "new-city-uuid",
  "name": "New City",
  "country_code": "US",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 400 BAD REQUEST
Content: {"error": "Invalid country code"} or {"error": "City name must be at least 2 characters long"}

### Sample Call:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "New City", "country_code": "US"}' http://localhost:5000/cities
```

Get All Cities
URL: /cities
Method: GET
Success Response:
Code: 200 OK

- **Content:**
```json
[
  {"id": "city-uuid", "name": "Miami", "country_code": "US"},
  // More cities...
]
```

### Sample Call:
```bash
curl -X GET http://localhost:5000/cities
```

Get City by ID
URL: /cities/<city_id>
Method: GET
URL Params:
Required: city_id=[uuid]
Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "city-uuid",
  "name": "Miami",
  "country_code": "US"
}
```

Error Response:
Code: 404 NOT FOUND
Content: {"error": "City not found"}

Sample Call:
```bash
curl -X GET http://localhost:5000/cities/city-uuid
```

Update City
URL: /cities/<city_id>
Method: PUT
URL Params:
Required: city_id=[uuid]

Data Params:
```json
{
  "name": "Updated City"
}
```

Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "city-uuid",
  "name": "Updated City",
  "country_code": "US",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 404 NOT FOUND
Content: {"error": "City not found"}

### Sample Call:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated City"}' http://localhost:5000/cities/city-uuid
```

Delete City
URL: /cities/<city_id>
Method: DELETE
URL Params:
Required: city_id=[uuid]
Success Response:
Code: 204 NO CONTENT
Error Response:
Code: 404 NOT FOUND
Content: {"error": "City not found"}

### Sample Call:
```bash
curl -X DELETE http://localhost:5000/cities/city-uuid
```

## Review Endpoints

Create Review for a Place
URL: /places/<place_id>/reviews
Method: POST
URL Params:
Required: place_id=[uuid]

Data Params:
```json
{
  "user_id": "user-uuid",
  "rating": 5,
  "comment": "Great place to stay!"
}
```

Success Response:
Code: 201 CREATED

- **Content:**
```json
{
  "id": "review-uuid",
  "place_id": "place-uuid",
  "user_id": "user-uuid",
  "rating": 5,
  "comment": "Great place to stay!",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 400 BAD REQUEST
Content: {"error": "User not found"} or {"error": "Place not found"}

Sample Call:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"user_id": "user-uuid", "rating": 5, "comment": "Great place to stay!"}' http://localhost:5000/places/place-uuid/reviews
```

Get Reviews by User
URL: /users/<user_id>/reviews
Method: GET
URL Params:
Required: user_id=[uuid]
Success Response:
Code: 200 OK

- **Content:**
```json
[
  {
    "id": "review-uuid",
    "place_id": "place-uuid",
    "user_id": "user-uuid",
    "rating": 5,
    "comment": "Loved this place!",
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  }
]
```

### Sample Call:
```bash
curl -X GET http://localhost:5000/users/user-uuid/reviews
```

Get Reviews by Place
URL: /places/<place_id>/reviews
Method: GET
URL Params:
Required: place_id=[uuid]
Success Response:
Code: 200 OK

- **Content:**
```json
[
  {
    "id": "review-uuid",
    "place_id": "place-uuid",
    "user_id": "user-uuid",
    "rating": 4,
    "comment": "Great views!",
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  }
]
```

### Sample Call:
```bash
curl -X GET http://localhost:5000/places/place-uuid/reviews
```

Get Review by ID
URL: /reviews/<review_id>
Method: GET
URL Params:
Required: review_id=[uuid]
Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "review-uuid",
  "place_id": "place-uuid",
  "user_id": "user-uuid",
  "rating": 5,
  "comment": "Fantastic place!",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 404 NOT FOUND
Content: {"error": "Review not found"}

### Sample Call:
```bash
curl -X GET http://localhost:5000/reviews/review-uuid
```
Update Review
URL: /reviews/<review_id>
Method: PUT
URL Params:
Required: review_id=[uuid]

Data Params:
```json
{
  "rating": 4,
  "comment": "Updated comment on this place."
}
```

Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "review-uuid",
  "place_id": "place-uuid",
  "user_id": "user-uuid",
  "rating": 4,
  "comment": "Updated comment on this place.",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 404 NOT FOUND
Content: {"error": "Review not found"}

### Sample Call:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"rating": 4, "comment": "Updated comment on this place."}' http://localhost:5000/reviews/review-uuid
```

Delete Review
URL: /reviews/<review_id>
Method: DELETE
URL Params:
Required: review_id=[uuid]
Success Response:
Code: 204 NO CONTENT
Error Response:
Code: 404 NOT FOUND
Content: {"error": "Review not found"}

### Sample Call:
```bash
curl -X DELETE http://localhost:5000/reviews/review-uuid
```

## Amenity Endpoints

Create Amenity
URL: /amenities
Method: POST

Data Params:
```json
{
  "name": "Swimming Pool"
}
```
Success Response:
Code: 201 CREATED

- **Content:**
```json
{
  "id": "uuid",
  "name": "Swimming Pool",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 400 BAD REQUEST
Content: {"error": "Amenity name must be unique"} or {"error": "Amenity name must be at least 3 characters long"}
Sample Call:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Swimming Pool"}' http://localhost:5000/amenities
```

Get All Amenities
URL: /amenities
Method: GET
Success Response:
Code: 200 OK

- **Content:**
```json
[
  {
    "id": "uuid",
    "name": "Swimming Pool",
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
  },
  // More amenities...
]
```

### Sample Call:
```bash
curl -X GET http://localhost:5000/amenities
```
Get Amenity by ID
URL: /amenities/<amenity_id>
Method: GET
URL Params:
Required: amenity_id=[uuid]
Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "uuid",
  "name": "Swimming Pool",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

Error Response:
Code: 404 NOT FOUND
Content: {"error": "Amenity not found"}

Sample Call:
```bash
curl -X GET http://localhost:5000/amenities/uuid
```
Update Amenity
URL: /amenities/<amenity_id>
Method: PUT
URL Params:
Required: amenity_id=[uuid]

Data Params:
```json
{
  "name": "Updated Swimming Pool"
}
```

Success Response:
Code: 200 OK

- **Content:**
```json
{
  "id": "uuid",
  "name": "Updated Swimming Pool",
  "updated_at": "2024-01-01T12:00:00Z"
}
```
Error Response:
Code: 404 NOT FOUND
Content: {"error": "Amenity not found"} or {"error": "Amenity name must be unique"}

### Sample Call:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Swimming Pool"}' http://localhost:5000/amenities/uuid
```

Delete Amenity
URL: /amenities/<amenity_id>
Method: DELETE
URL Params:
Required: amenity_id=[uuid]
Success Response:
Code: 204 NO CONTENT
Error Response:
Code: 404 NOT FOUND
Content: {"error": "Amenity not found"}

### Sample Call:
```bash
curl -X DELETE http://localhost:5000/amenities/uuid
```