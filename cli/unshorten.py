#!/usr/bin/env python3

import requests
from urllib.parse import urlparse

# Enter a shortened URL string and convert to original i.e https://tinyurl.com/y3z9jshq

print('Convert a shortened URL to the original \n')

while True:
    short_url = input('Enter a URL: ')

    try:
        parsed_url = urlparse(short_url)
        parsed_url.scheme == 'http'

        print(requests.get(short_url).url)
        break
    except ValueError:
        print('Enter a valid URL (http://example.com)')

