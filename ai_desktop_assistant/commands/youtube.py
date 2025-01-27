import pywhatkit as kit
from utils.speech import Speak, takecommand

def YoutubeAutomation():
    Speak("What do you want to search on YouTube?")
    search_query = takecommand()
    Speak(f"Searching {search_query} on YouTube")
    kit.playonyt(search_query)
