from app.models.gym_class import GymClass
from app.repositories.repository_base import Create, Read, Update, Delete
from app import db

class GymClassRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.model = GymClass
    
    def find_all(self):
        return super().find_all()
        
    def find_by_id(self, id) -> GymClass:
        return super().find_by_id(id)

    def create(self, class_data: GymClass) -> db.Model:
        return super().create(class_data)
    
    def update(self, class_data: dict, id: int) -> GymClass:
        return super().update(id, **class_data)

    def delete(self, id: int):
        return super().delete(id)