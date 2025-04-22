import smtplib
from email.mime.text import MIMEText
import os
from datetime import datetime

# Gmail SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
GMAIL_PASSWORD = os.environ.get("EMAIL_APP_PASSWORD")

def send_email():
    recipient = os.environ.get("EMAIL_RECIPIENT")
    subject = os.environ.get("EMAIL_SUBJECT", "Automated Email")
    body = os.environ.get("EMAIL_BODY", "This is your automated recurring email.")
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = GMAIL_USERNAME
    msg['To'] = recipient
    
    try:
        smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        smtp_server.send_message(msg)
        smtp_server.close()
        print(f"Email sent successfully at {datetime.now()}")
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False

if __name__ == "__main__":
    send_email()