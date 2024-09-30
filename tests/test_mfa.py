import unittest
from mfa import send_mfa_code, verify_mfa_code

class TestMFA(unittest.TestCase):

    def test_verify_mfa_code(self):
        mfa_code = send_mfa_code("user1@example.com")
        self.assertTrue(verify_mfa_code(mfa_code, mfa_code))

if __name__ == "__main__":
    unittest.main()
