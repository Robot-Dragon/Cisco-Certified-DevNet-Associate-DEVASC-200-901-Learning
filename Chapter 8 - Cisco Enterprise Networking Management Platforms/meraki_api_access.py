import requests
from requests.api import head

url = 'https://api.meraki.com/api/v0/organizations'
api_key = ''

headers = {'X-Cisco-Meraki-API-Key':api_key}

response = requests.request(method='GET', url=url, headers=headers)

print(response.status_code)

print('OK!')