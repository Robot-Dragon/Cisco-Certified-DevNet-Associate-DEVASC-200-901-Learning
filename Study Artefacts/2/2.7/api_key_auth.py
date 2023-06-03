# A working example of an API key authentication implementation

# Cisco Meraki uses an API key

import requests

url = 'https://api.meraki.com/api/v1/organizations'
api_key = 'c2639037b0ec9ab6ff7038399172d1f2315fe1dd'

headers = {'X-Cisco-Meraki-API-Key': api_key}
response = requests.get(url=url, headers=headers)

print(response.content)
