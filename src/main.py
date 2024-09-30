from encryption import encrypt, decrypt
from authentication import authenticate_user
from logger import Logger
from mfa import send_mfa_code, verify_mfa_code
from database import load_users

def main():
    logger = Logger("activity.log")
    users_db = load_users()

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if authenticate_user(username, password, users_db):
        logger.log(f"Pengguna {username} berhasil diautentikasi.")
        
        # Mengirim kode MFA
        mfa_code = send_mfa_code(username)
        mfa_input = input("Masukkan kode MFA yang telah dikirim: ")
        
        if verify_mfa_code(mfa_code, mfa_input):
            logger.log(f"MFA berhasil untuk pengguna {username}.")
            
            # Enkripsi dan dekripsi data
            data = "Data sensitif yang perlu dilindungi."
            encrypted_data = encrypt(data)
            logger.log(f"Data terenkripsi: {encrypted_data}")
            
            decrypted_data = decrypt(encrypted_data)
            logger.log(f"Data terdekripsi: {decrypted_data}")
        else:
            logger.log(f"Verifikasi MFA gagal untuk pengguna {username}.")
    else:
        logger.log(f"Autentikasi gagal untuk pengguna {username}.")

if __name__ == "__main__":
    main()
