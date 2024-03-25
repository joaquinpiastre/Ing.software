import unittest
from App import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()