from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app import db
from dataclasses import dataclass

@dataclass
class GymClass(db.Model):
    __tablename__ = 'gym_classes'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    gym_name = db.Column('gym_name', db.String)
    instructor_id = db.Column('instructor_id', db.Integer, ForeignKey('instructors.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'gym_name': self.gym_name,
            'instructor_id': self.instructor_id
        }