import requests
from requests.auth import HTTPBasicAuth

response = requests.post(
    'http://localhost:5002/login',
    json={'username': 'test', 'password': 'test'}
    )

token = response.json()['access_token']
print(f"token: {token}\n")

print("sending not authoraized request")
response = requests.get(
    'http://localhost:5002/protected',
    )
print(response.text)    

print("sending authoraized request")
response = requests.get(
    'http://localhost:5002/protected',
    headers={'Authorization': f"Bearer {token}"}
    )
print(response.text)    
