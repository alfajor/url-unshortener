import requests
from time import sleep
from urllib.parse import urlparse

# Accept URL string, parse and return original

def url_handler(short_url, **kwargs):
    alert = kwargs.get('alert', None)

    input_url = ''
    while input_url == '':
        try:
            parsed_url = urlparse(short_url)
            parsed_url.scheme == 'http'
            
            try:
                input_url = requests.get(short_url).url
                return input_url
            
                break 
            except requests.exceptions.ConnectionError as e:
                return 'Connection refused. Please try again.'
                time.sleep(5)

                continue

        except ValueError:
            return alert