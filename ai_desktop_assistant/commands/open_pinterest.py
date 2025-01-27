import webbrowser
import logging

def open_pinterest():
    url = "https://in.pinterest.com/pin-creation-tool/"
    try:
        webbrowser.open(url)
        logging.info("Opened Pinterest")
    except Exception as e:
        logging.error(f"Error opening Pinterest: {str(e)}")
