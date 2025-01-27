import webbrowser
import logging

def open_amazon_associates():
    url = "https://affiliate-program.amazon.in/home"
    try:
        webbrowser.open(url)
        logging.info("Opened Amazon Associates")
    except Exception as e:
        logging.error(f"Error opening Amazon Associates: {str(e)}")
