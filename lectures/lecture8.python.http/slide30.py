import requests
from requests.auth import HTTPBasicAuth

response = requests.post(
    'http://localhost:5002/basic_auth',
    auth=HTTPBasicAuth('sergii', 'hello')
)

print(response.text)