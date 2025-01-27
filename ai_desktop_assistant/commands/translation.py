from googletrans import Translator
from utils.speech import Speak, takecommand

def Tran():
    Speak("Tell me the sentence you want to translate.")
    sentence = takecommand()
    Speak("Which language do you want to translate to?")
    language = takecommand()
    
    translator = Translator()
    try:
        translation = translator.translate(sentence, dest=language)
        Speak(f"The translation is: {translation.text}")
    except Exception as e:
        Speak(f"An error occurred while translating: {str(e)}")
