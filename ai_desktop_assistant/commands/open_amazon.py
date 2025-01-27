import webbrowser
import logging

def open_amazon():
    url = "https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=14195205567205925572&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9303142&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1"
    try:
        webbrowser.open(url)
        logging.info("Opened Amazon")
    except Exception as e:
        logging.error(f"Error opening Amazon: {str(e)}")
