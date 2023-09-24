#!/usr/bin/env python3

import requests

URL = "https://edutech-main.onrender.com/admins"

request = requests.get(URL)
if request.status_code == 200:
    print('Request successfully sent')
else:
    print(f'An error occured when sending request: {request.status_code} => {request.text}')
