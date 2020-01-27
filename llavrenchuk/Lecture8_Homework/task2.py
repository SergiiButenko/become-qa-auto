# Задание2. Используя локально запущеный simple-app.py: 
# 1. Авторизироваться пользователем tesе с паролем test
# 2. Создать ресурс item - POST
# 3. Прочитать ресурс item - GET
# 4. Удалить ресурс item - DELETE

import requests
response = requests.post(
    'http://localhost:5002/login',
    json={'username': 'test', 'password': 'test'}
    )

token = response.json()['access_token']
#print(f"token: {token}\n")
#print(response.text)

print("sending authoraized request to http://localhost:5002")
response1 = requests.get(
    'http://localhost:5002/protected',
    headers={'Authorization': f"Bearer {token}"}
    )
print(response1.text)

response2 = requests.post(
    'http://localhost:5002/',
    json={'key': 'item'})

response3 = requests.get(
    'http://localhost:5002/', params={'key': 'item'})
json_response3=response3.json()
print(f'Item is created: {json_response3}')

response4 = requests.delete(
    'http://localhost:5002/',
    json={'key': 'item'})