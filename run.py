from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
import json
from instance.config import DevelopmentConfig
from app.services.country_city_service import CountryCityService

# Initialize SQLAlchemy
db = SQLAlchemy()


# Essential to render special characters (1)
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return super().default(obj)  # Call the base class method for other types

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.json_encoder = CustomJSONEncoder  # Set the custom encoder
    app.config['JSON_AS_ASCII'] = False  # Prevent Flask from escaping non-ASCII chars

    # Initialize SQLAlchemy
    db = SQLAlchemy(app)  # Make sure 'db' is used throughout your application for SQLAlchemy operations

    # Set up the application context before initializing anything that requires the app context
    with app.app_context():
        from app.services.country_city_service import CountryCityService
        CountryCityService.initialize_countries()

    # Importing Blueprints
    from app.api.user_api import user_blueprint
    from app.api.place_api import place_blueprint
    from app.api.country_city_api import country_city_blueprint
    from app.api.review_api import review_blueprint
    from app.api.amenity_api import amenity_blueprint

    # Registering Blueprints without any URL prefixes
    app.register_blueprint(user_blueprint, url_prefix='')
    app.register_blueprint(place_blueprint, url_prefix='')
    app.register_blueprint(country_city_blueprint, url_prefix='')
    app.register_blueprint(review_blueprint, url_prefix='')
    app.register_blueprint(amenity_blueprint, url_prefix='')

    # This is for the render in localhost
    @app.route('/')
    def home():
        return "Welcome to the Flask API. Use the specific API endpoints to interact."
    
    # Essential to render special characters (3)
    @app.after_request
    def apply_utf8_encoding(response):
        if response.mimetype == 'application/json':
            response.set_data(json.dumps(response.get_json(), ensure_ascii=False, indent=2))
            response.mimetype = 'application/json; charset=utf-8'
        return response

    return app

# This is for activated it from command line
# It is not necessary in production - Comment it**
if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])
