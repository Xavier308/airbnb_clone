from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, place_id, user_id, rating, comment):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'place_id': self.place_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'comment': self.comment
        })
        return data
