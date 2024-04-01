import unittest
from app import create_app
from app.models.gym_class import GymClass
from app.repositories.gym_class_repository import GymClassRepository

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.repo = GymClassRepository()

    def test_gym_class_in_database(self):
        # Create a new gym class
        new_class = GymClass(name="Yoga", instructor="John Doe", duration=60)
        self.repo.add(new_class)

        # Retrieve the gym class from the database
        retrieved_class = self.repo.get(new_class.id)

        # Check if the retrieved class is the same as the one we added
        self.assertEqual(retrieved_class.name, new_class.name)
        self.assertEqual(retrieved_class.instructor, new_class.instructor)
        self.assertEqual(retrieved_class.duration, new_class.duration)

if __name__ == "__main__":
    unittest.main()