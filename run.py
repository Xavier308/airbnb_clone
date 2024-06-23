from flask import Flask, jsonify
import json
from instance.config import DevelopmentConfig
from app.services.country_city_service import CountryCityService


# Essential to render special characters (1)
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return super().default(obj)  # Call the base class method for other types

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.json_encoder = CustomJSONEncoder  # Set the custom encoder
    # Essential to render special characters (2)
    app.config['JSON_AS_ASCII'] = False  # Prevent Flask from escaping non-ASCII chars

    # Set up the application context before initializing countries
    with app.app_context():
        # Initialize country data
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

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])
