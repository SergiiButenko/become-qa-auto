import requests
from requests.auth import HTTPBasicAuth

response = requests.get(
    'http://localhost:5002/basic_auth',
    auth=HTTPBasicAuth('sergii', 'hello')
)

print(response.text)
