import bcrypt
import pandas as pd

def load_users():
    """Memuat pengguna dari file CSV."""
    return pd.read_csv("data/users.csv", index_col=0).to_dict(orient="index")

def authenticate_user(username, password, users_db):
    """Mengautentikasi pengguna dengan username dan password."""
    if username in users_db:
        hashed_password = users_db[username]["password"].encode()
        return bcrypt.checkpw(password.encode(), hashed_password)
    return False
