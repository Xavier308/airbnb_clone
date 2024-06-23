# app/api/review_api.py
from flask import Blueprint, request, jsonify
from app.services.review_service import ReviewService

review_blueprint = Blueprint('reviews', __name__)

@review_blueprint.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    try:
        review = ReviewService.create_review(place_id, request.json)
        return jsonify(review), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400 if 'not found' in str(e) else 409

@review_blueprint.route('/users/<user_id>/reviews', methods=['GET'])
def get_reviews_by_user(user_id):
    return jsonify(ReviewService.get_reviews_by_user(user_id)), 200

@review_blueprint.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    return jsonify(ReviewService.get_reviews_by_place(place_id)), 200

@review_blueprint.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = ReviewService.get_review_by_id(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review), 200

@review_blueprint.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    try:
        review = ReviewService.update_review(review_id, request.json)
        return jsonify(review), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404

@review_blueprint.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    try:
        ReviewService.delete_review(review_id)
        return '', 204
    except ValueError:
        return jsonify({'error': 'Review not found'}), 404
