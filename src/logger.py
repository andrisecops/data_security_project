import logging

class Logger:
    def __init__(self, filename):
        logging.basicConfig(filename=filename, level=logging.INFO)
    
    def log(self, message):
        logging.info(message)
        print(message)  # Menampilkan pesan log di konsol
