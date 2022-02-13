import requests


url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
headers = {'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='}

username = 'devnetuser'
password = 'Cisco123!'

# Standard approach
# response = requests.request('GET', url=url, headers=headers)

# alternate with auth argument - it does base-64 conversion for you
response = requests.request('GET', url=url, auth=(username, password))

print(response.status_code)
# print(response.headers)