import random
import smtplib
from email.mime.text import MIMEText

# Simulasi pengiriman kode MFA
def send_mfa_code(username):
    mfa_code = str(random.randint(100000, 999999))
    send_email(username, mfa_code)  # Kirim kode ke email
    return mfa_code

def send_email(to_email, mfa_code):
    """Mengirim kode MFA ke email pengguna."""
    msg = MIMEText(f"Kode MFA Anda adalah: {mfa_code}")
    msg['Subject'] = 'Kode MFA Anda'
    msg['From'] = 'smtptest@pwn0sec.com'
    msg['To'] = to_email

    # Mengirim email menggunakan SMTP
    with smtplib.SMTP('smtp.pwn0sec.com', 587) as server:
        server.starttls()
        server.login('smtptest@pwn0sec.com', 'your_password')
        server.send_message(msg)

def verify_mfa_code(expected_code, input_code):
    """Memverifikasi kode MFA."""
    return expected_code == input_code
