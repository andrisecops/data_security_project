import unittest
import os
from logger import Logger

class TestLogger(unittest.TestCase):

    def test_log_message(self):
        log_file = "test.log"
        logger = Logger(log_file)
        logger.log("Test log message")
        
        # Memeriksa apakah file log terbentuk
        self.assertTrue(os.path.exists(log_file))

        # Bersihkan setelah tes
        os.remove(log_file)

if __name__ == "__main__":
    unittest.main()
