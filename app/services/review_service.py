# app/services/review_service.py
import uuid
from datetime import datetime
from app.persistence.data_manager import save_data, load_data
from app.services.user_service import UserService
from app.services.place_service import PlaceService


class ReviewService:
    @staticmethod
    def validate_review_data(data):
        if not data.get('comment') or len(data['comment'].strip()) < 3:
            raise ValueError("Comment must be at least 3 characters long")
        if data.get('rating') < 1 or data.get('rating') > 5:
            raise ValueError("Rating must be between 1 and 5")

    @staticmethod
    def get_reviews_by_user(user_id):
        reviews = load_data('reviews')
        return [review for review in reviews if review['user_id'] == user_id]

    @staticmethod
    def get_reviews_by_place(place_id):
        reviews = load_data('reviews')
        return [review for review in reviews if review['place_id'] == place_id]

    @staticmethod
    def get_review_by_id(review_id):
        reviews = load_data('reviews')
        return next((review for review in reviews if review['id'] == review_id), None)

    @staticmethod
    def create_review(place_id, data):
        ReviewService.validate_review_data(data)

        reviews = load_data('reviews')
        if not PlaceService.get_place_by_id(place_id):
            raise ValueError("Place not found")
        if not UserService.find_user(data['user_id']):  # Use find_user instead of get_user_by_id
            raise ValueError("User not found")
        if data['rating'] < 1 or data['rating'] > 5:
            raise ValueError("Rating must be between 1 and 5")
        if any(review['user_id'] == data['user_id'] and review['place_id'] == place_id for review in reviews):
            raise ValueError("User has already reviewed this place")

        review = {
            'id': str(uuid.uuid4()),
            'place_id': place_id,
            'user_id': data['user_id'],
            'rating': data['rating'],
            'comment': data['comment'],
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        reviews.append(review)
        save_data('reviews', reviews)
        return review

    @staticmethod
    def update_review(review_id, data):
        ReviewService.validate_review_data(data)

        reviews = load_data('reviews')
        review = next((r for r in reviews if r['id'] == review_id), None)
        if review is None:
            raise ValueError("Review not found")

        # Directly assign updated values to the review
        review['rating'] = data.get('rating', review['rating'])
        review['comment'] = data.get('comment', review['comment'])
        review['updated_at'] = datetime.now().isoformat()

        # Save the entire list of reviews back to the JSON file to ensure persistence
        save_data('reviews', reviews)
        return review

    @staticmethod
    def delete_review(review_id):
        reviews = load_data('reviews')
        original_length = len(reviews)
        reviews[:] = [review for review in reviews if review['id'] != review_id]
        if len(reviews) == original_length:
            raise ValueError("Review not found")
        save_data('reviews', reviews)
        return True
