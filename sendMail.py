import smtplib
import keyring
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# keyring.set_password("gmail_app_password", "Newsletter Project", "tknv ojhm dxae mhaw")
def smtp_setting():
    port = 587
    mail_type = 'smtp.gmail.com'

    server = smtplib.SMTP(mail_type, port)
    server.set_debuglevel(True)

    server.starttls()

    password = keyring.get_password("gmail_service", "moneymaster1232@gmail.com")
    password = keyring.get_password("gmail_app_password", "Newsletter Project")
    server.login("moneymaster1232@gmail.com", password)

    return server

# def send_email(server, ):
#     pass