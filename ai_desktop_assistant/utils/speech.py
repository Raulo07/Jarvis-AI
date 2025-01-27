import pyttsx3
import speech_recognition as sr
import logging

# Set up text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def Speak(Audio):
    print(f": {Audio}")
    engine.say(Audio)
    engine.runAndWait()
    logging.info(f"Spoke: {Audio}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            query = r.recognize_google(audio, language='en-in')
            print(f"Your Command: {query}\n")
            logging.info(f"Recognized Command: {query}")
        except sr.UnknownValueError:
            Speak("Sorry, I did not understand that. Could you please repeat?")
            return "None"
        except sr.RequestError as e:
            Speak(f"Could not request results; {e}")
            return "None"
        return query.lower()
