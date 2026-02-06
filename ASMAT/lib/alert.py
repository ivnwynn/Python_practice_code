import smtplib
from email.mime.text import MIMEText
import logging 

def send_email_alert(subject, body, config):
    sender_email = config['email']['sender_email']
    receiver_email = config['email']['receiver_email']
    password = config['email']['password']
    smtp_server = config['email']['smtp_server']
    smtp_port = config['email']['smtp_port']

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL(smtp_server, int(smtp_port))as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        logging.info("Email send successfully")#Login Success
    except Exception as e:
        logging.error(f"Error sending email: {e}")#Login Error