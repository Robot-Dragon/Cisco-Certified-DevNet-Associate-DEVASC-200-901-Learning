# A working example of an API token authentication implementation

# Continuing from the example of basic_auth, the request using this returns a token

import requests
import base64
import json

username = 'devnetuser'
password = 'Cisco123!'
url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'

def basic_auth(username, password):
    """Returns a base-64 encoded string of the username and password"""
    return str(base64.b64encode(f'{username}:{password}'.encode('utf-8')), 'utf-8')

auth = basic_auth(username=username, password=password)

headers = {'Content-Type': 'application/json', 'Authorization':f'Basic {auth}'}
response = requests.post(url=url, headers=headers, verify=False)

print(response.status_code)
token = json.loads(response.content.decode())['Token']

