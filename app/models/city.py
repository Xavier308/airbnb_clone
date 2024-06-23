from app.models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country_code):
        super().__init__()
        self.name = name
        self.country_code = country_code

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'country_code': self.country_code
        })
        return data
