import pyautogui
from datetime import datetime
from utils.speech import Speak
from config.config import SCREENSHOT_PATH
import os

def screenshot():
    Speak("Taking screenshot...")
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(SCREENSHOT_PATH, f"screenshot_{current_time}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    Speak(f"Screenshot saved at {screenshot_path}")
