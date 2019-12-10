import requests
response = requests.get('http://localhost:5002/')
print(response.json())
