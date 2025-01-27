import requests
from bs4 import BeautifulSoup
from utils.speech import Speak

def Temp():
    search = "current temperature in your_location"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    Speak(f"The current temperature is {temp}")

def get_location():
    ip_info = requests.get('https://ipinfo.io').json()
    location = ip_info['city']
    Speak(f"You are currently in {location}")
