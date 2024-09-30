import unittest
from database import load_users

class TestDatabase(unittest.TestCase):

    def test_load_users(self):
        users_db = load_users()
        self.assertIn("user1", users_db)

if __name__ == "__main__":
    unittest.main()
