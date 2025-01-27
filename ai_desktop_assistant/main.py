# main.py
from commands.email import SendEmail
from commands.music import Music
from commands.open_amazon import open_amazon
from commands.open_amazon_associates import open_amazon_associates
from commands.open_pinterest import open_pinterest
from commands.whatsapp import SendWhatsAppMessage
from commands.screenshot import screenshot
from commands.youtube import YoutubeAutomation
from commands.chrome_auto import ChromeAuto
from commands.object_detection import ObjectDetection
from commands.translation import Tran
from utils.speech import Speak, takecommand
from utils.web_scraping import Temp, get_location
from config.config import OPENAI_API_KEY
import openai
import logging

# Set up OpenAI API key
openai.api_key = OPENAI_API_KEY

# Set up logging
logging.basicConfig(filename='logs/jarvis.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def TaskExe():
    Speak("Hello Sir, I am Jarvis. How can I help you?")

    while True:
        query = takecommand().lower()

        if 'hello' in query:
            Speak("Hello Sir, I am Jarvis. How can I help you?")

        elif 'how are you' in query:
            Speak("I am fine, Sir! How can I assist you?")

        elif 'send email' in query:
            SendEmail()

        elif 'send a whatsapp message' in query:
            SendWhatsAppMessage()

        elif 'screenshot' in query:
            screenshot()

        elif 'youtube tool' in query:
            YoutubeAutomation()

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'object detection' in query:
            ObjectDetection()

        elif 'translate a sentence' in query:
            Tran()

        elif 'temperature' in query:
            Temp()

        elif 'location' in query:
            get_location()

        elif 'open_amazon' in query:
            open_amazon() 

        elif 'open_amazon_associates' in query:
            open_amazon_associates() 

        elif 'open_pinterest' in query:
            open_pinterest()

        elif 'you need a break' in query:
            Speak("Okay, Sir. Call me when you need anything!")
            break

        else:
            Speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    TaskExe()
