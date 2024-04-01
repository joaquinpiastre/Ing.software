from app.models.gym_class import GymClass
from abc import ABC, abstractmethod
from app import db

class Create(ABC):
    
    @abstractmethod
    def create(self, entity: db.Model):
        db.session.add(entity)
        db.session.commit()
        return entity
    
class Read(ABC):
    
    @abstractmethod
    def find_all(self):
        return db.session.query(self.model).all()
    
    @abstractmethod
    def find_by_id(self, id: int):
        return db.session.query(self.model).filter(self.model.id == id).one_or_none()
    
class Update(ABC):
    
    @abstractmethod
    def update(self, id, **kwargs):
        entity = self.find_by_id(id)
        for key, value in kwargs.items():
            if hasattr(entity, key):
                setattr(entity, key, value)
        db.session.commit()
        return entity
    
class Delete(ABC):
    
    def delete(self, id):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()



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