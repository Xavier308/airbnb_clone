from app.models.base_model import BaseModel
from datetime import datetime

class Country(BaseModel):
    def __init__(self, code, name):
        super().__init__()
        self.id = code  # Override the UUID with ISO code
        self.name = name

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'code': self.id,  # Using self.id as the code here
            'name': self.name
        })
        return data

    @classmethod
    def from_dict(cls, data):
        """Recreates a Country instance from a dictionary."""
        obj = cls(data['code'], data['name'])
        obj.created_at = datetime.fromisoformat(data['created_at'])
        obj.updated_at = datetime.fromisoformat(data['updated_at'])
        return obj
