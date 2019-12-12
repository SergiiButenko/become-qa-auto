import requests
""" 
#response = requests.get('http://localhost:5002/')
#print(response.__dict__)
#print(response.status_code)

#response2 = requests.get('http://localhost:5002/fail500')
#print(response2.status_code)

#response3 = requests.get('http://localhost:5002/users')
#print(response3.status_code)

#print(response.json())
"""

""" 
# Поиск местонахождения для запросов на GitHub
response = requests.get(
   'https://api.github.com/search/repositories',
   params={'q': 'become-qa-auto'},
)
# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+
"""

"""  
response = requests.post(
   'http://localhost:5002/',
   json={'serbut': 'value'},)
json_response = response.json()
print(f'Responce: {json_response}')
"""

"""

import requests
from requests.auth import HTTPBasicAuth

response = requests.get(
   'http://localhost:5002/basic_auth',
   auth=HTTPBasicAuth('sergii', 'hello')
)
print(response.text)
"""

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