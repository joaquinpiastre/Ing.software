import unittest
from app import create_app
from app.services.gym_class_service import GymClassService

class TestGymClass(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.service = GymClassService()

    def test_get_class(self):
        response = self.client.get('/find_class/1')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()