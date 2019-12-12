# Задание2. Используя локально запущеный simple-app.py: 
# 1. Авторизироваться пользователем tets с паролем test
# 2. Создать ресурс item
# 3. Прочитать ресурс item
# 4. Удалить ресурс item

import requests
response = requests.post(
    'http://localhost:5002/login',
    json={'username': 'test', 'password': 'test'}
    )

token = response.json()['access_token']
print(f"token: {token}\n")
print(response.text)

print("sending authoraized request to http://localhost:5002")
response1 = requests.get(
    'http://localhost:5002/protected',
    headers={'Authorization': f"Bearer {token}"}
    )
print(response1.text)