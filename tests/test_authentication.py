import unittest
from authentication import load_users, authenticate_user

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.users_db = load_users()

    def test_authenticate_user_success(self):
        self.assertTrue(authenticate_user("user1", "password1", self.users_db))

    def test_authenticate_user_failure(self):
        self.assertFalse(authenticate_user("user1", "wrong_password", self.users_db))

if __name__ == "__main__":
    unittest.main()
