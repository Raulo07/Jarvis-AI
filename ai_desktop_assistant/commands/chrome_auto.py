from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.speech import Speak, takecommand

def ChromeAuto():
    Speak("Tell me the website you want to open.")
    website = takecommand()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"https://{website}.com")
    Speak(f"{website} is now open.")
