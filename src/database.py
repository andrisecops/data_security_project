import pandas as pd

def load_users():
    """Memuat pengguna dari file CSV."""
    return pd.read_csv("data/users.csv", index_col=0).to_dict(orient="index")
