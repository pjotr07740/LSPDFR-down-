import requests

class status():
    def get_status():
        r = requests.head("https://www.lcpdfr.com")
        return r.status_code