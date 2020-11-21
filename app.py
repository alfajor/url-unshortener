#!/usr/bin/env python3

import os
from flask import Flask, request, render_template
from url import url_handler

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key = os.environ.get('SECRET_KEY')

if __name__ == '__main__':
    app.run()

@app.route('/', methods=['GET'])
def index():
    client_url = request.args.get('url')
    
    prompt = ''
    if not client_url:
        prompt = 'Enter a URL to shorten:'

    result = ''
    if request.args.get('query') == 'true':
        error = '* Please enter a valid full URL. i.e http://example.com'
        result = url_handler(str(client_url), alert=error)

    return render_template('index.html', result=result, prompt=prompt)

