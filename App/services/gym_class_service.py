from app.models.gym_class import GymClass
from app.repositories.gym_class_repository import GymClassRepository
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



class GymClassService(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.__repo = GymClassRepository()
    
    def find_all(self):
        return self.__repo.find_all()

    def find_by_id(self, id):
        return self.__repo.find_by_id(id)

    def create(self, class_data: dict) -> GymClass:
        gym_class = GymClass(**class_data)
        return self.__repo.create(gym_class)

    def update(self, id, class_data):
        return self.__repo.update(id, class_data)

    def delete(self, id):
        return self.__repo.delete(id)