import os
from utils.speech import Speak, takecommand

def Music():
    Speak("Tell me the name of the song!")
    music_name = takecommand()

    if 'dekha ek khwab' in music_name.lower():
        os.startfile('C:\\Users\\shubh\\Music\\Dekha Ek Khwab Song.mp3')
    elif 'chala jata hoon' in music_name.lower():
        os.startfile('C:\\Users\\shubh\\Music\\Chala Jata Hoon.mp3')
    else:
        Speak("I could not find the song. Please make sure the file path is correct.")
