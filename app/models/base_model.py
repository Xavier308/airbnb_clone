import uuid
from datetime import datetime
import json

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def update(self, **kwargs):
        """Updates attributes of the model."""
        self.updated_at = datetime.now()
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def from_dict(cls, data):
        """Creates an instance from a dictionary."""
        obj = cls()
        obj.__dict__.update(data)
        obj.created_at = datetime.fromisoformat(data['created_at'])
        obj.updated_at = datetime.fromisoformat(data['updated_at'])
        return obj
