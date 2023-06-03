# A working example of an 'basic' authentication implementation

# Cisco DNA Center uses Basic Auth

from email.mime import base
import base64

username = 'devnetuser'
password = 'Cisco123!'
url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1'

def basic_auth(username, password):
    """Returns a base-64 encoded string of the username and password"""
    return str(base64.b64encode(f'{username}:{password}'.encode('utf-8')), 'utf-8')

print(basic_auth(username, password))