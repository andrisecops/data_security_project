from cryptography.fernet import Fernet

# Menghasilkan kunci untuk enkripsi
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(data):
    """Enkripsi data yang diberikan."""
    return cipher.encrypt(data.encode())

def decrypt(encrypted_data):
    """Dekripsi data terenkripsi yang diberikan."""
    return cipher.decrypt(encrypted_data).decode()
