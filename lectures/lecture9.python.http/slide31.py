import requests
from requests.auth import HTTPBasicAuth

response = requests.post(
    'http://localhost:5002/login',
    json={'username': 'test', 'password': 'test'}
    )

print(response.json())