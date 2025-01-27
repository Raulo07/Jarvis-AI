import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.speech import Speak, takecommand
from config.config import EMAIL
import logging

def SendEmail():
    Speak("Whom do you want to send the email to?")
    recipient = takecommand()
    Speak("What is the subject of the email?")
    subject = takecommand()
    Speak("What is the message of the email?")
    message_body = takecommand()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL['address'], EMAIL['password'])

        msg = MIMEMultipart()
        msg['From'] = EMAIL['address']
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message_body, 'plain'))

        server.sendmail(EMAIL['address'], recipient, msg.as_string())
        server.quit()

        Speak("Your email has been sent successfully!")
        logging.info(f"Email sent to {recipient} with subject '{subject}'")

    except Exception as e:
        Speak(f"An error occurred while sending the email: {str(e)}")
        logging.error(f"Error sending email: {str(e)}")
