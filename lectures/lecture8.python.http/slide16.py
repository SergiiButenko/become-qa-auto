import requests
response = requests.get('http://localhost:5002/')
print(response.status_code)
response2 = requests.get('http://localhost:5002/fail500')
print(response2.status_code)
response3 = requests.get('http://localhost:5002/users')
print(response3.status_code)
