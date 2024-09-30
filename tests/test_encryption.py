import unittest
from encryption import encrypt, decrypt

class TestEncryption(unittest.TestCase):

    def test_encryption_decryption(self):
        data = "Data sensitif"
        encrypted_data = encrypt(data)
        decrypted_data = decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

if __name__ == "__main__":
    unittest.main()
