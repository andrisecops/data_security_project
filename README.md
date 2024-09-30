# Proyek Data Security 🚀

## Deskripsi
Selamat datang di proyek **Data Security**! 🔒 Proyek ini dibuat untuk melindungi data-data sensitif dan memastikan keamanan siber yang lebih canggih. Dengan fitur-fitur keren seperti enkripsi data, autentikasi pengguna, dan autentikasi multi-faktor (MFA), kamu bisa tenang deh karena data kamu aman banget! Hanya pengguna yang terautentikasi yang bisa mengakses informasi penting ini. Yuk, kita jaga data kita bersama-sama!

## Cara Instalasi

1. **Clone Repo Ini**  
   Pertama-tama, clone repo ini ke komputer kamu:
```bash
   git clone https://github.com/pwnosec/data_security_project.git
   cd data_security_project
```
2. **Instal Dependensi**
   Instal semua dependensi yang diperlukan dengan pip:
```
pip install -r requirements.txt
```
3. **Siapkan Data Pengguna**
Edit file `data/users.csv` dengan username dan password yang di-hash. Gunakan bcrypt untuk meng-hash password, seperti contoh di bawah ini:
```
import bcrypt

password = "password1"
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
print(hashed.decode())
```
## Cara Penggunaan
1. **Jalankan Proyek**
  Setelah semua siap, kamu bisa menjalankan proyek dengan perintah berikut:
```
python src/main.py
```
2. **Jalankan Pengujian**
  Untuk menjalankan pengujian, gunakan perintah berikut:
```
python -m unittest tests/test_encryption.py
python -m unittest tests/test_authentication.py
python -m unittest tests/test_logger.py
python -m unittest tests/test_mfa.py
python -m unittest tests/test_database.py
```

### Kontribusi
Kalau kamu mau ikut berkontribusi di proyek ini, silakan buka issue atau pull request! Semua kontribusi sangat dihargai. Semangat!

&copy; [@pwnosec](https://github.com/pwnosec) / [@pwnlaboratory](https://github.com/pwnlaboratory) / [@pwnacademy](https://academy.pwn0sec.com)
