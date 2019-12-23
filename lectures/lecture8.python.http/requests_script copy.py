import requests

response = requests.get('http://localhost:5002/')
print(response.status_code)
print(response.json())
print(response.headers)
print(requests.post('https://httpbin.org/post', json={'key':'value'}).json())

