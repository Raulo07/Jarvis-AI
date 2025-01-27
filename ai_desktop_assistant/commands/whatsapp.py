import pywhatkit as kit
from utils.speech import Speak, takecommand
import logging

def SendWhatsAppMessage():
    Speak("Tell me the phone number to send the message to.")
    phone_number = takecommand()
    Speak("What is the message?")
    message = takecommand()
    
    try:
        kit.sendwhatmsg_instantly(phone_number, message, 15, True, 2)
        Speak("Message has been sent successfully!")
        logging.info(f"WhatsApp message sent to {phone_number}")
    except Exception as e:
        Speak(f"An error occurred while sending the message: {str(e)}")
        logging.error(f"Error sending WhatsApp message: {str(e)}")
