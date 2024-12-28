import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("najam135@gmail.com")
    password = os.getenv("PASSWORD")

    receiver = "najam135@gmail.com"
    context = ssl.create_default_context()
    # ssl library used to create secure context for eg pwd

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)