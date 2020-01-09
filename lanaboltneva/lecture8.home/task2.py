# Задание2. Используя локально запущеный simple-app.py: 
# 1. Авторизироваться пользователем tets с паролем test
# 2. Создать ресурс item - POST
# 3. Прочитать ресурс item - GET
# 4. Удалить ресурс item - DELETE

import requests
from requests.auth import HTTPBasicAuth

# 1. Авторизироваться пользователем tets с паролем test

response = requests.post(
    'http://localhost:5002/login',
    json={'username': 'test', 'password': 'test'}
    )

token = response.json()['access_token']

print(f"\n1. Sending authorization request to http://localhost:5002/login:") 
print(f"TOKEN: {token}\n")

# 2. Создать ресурс item - POST

HEADERS = {'Authorization': 'Bearer {}'.format(token)}

response_create_item = requests.post('http://localhost:5002/items', headers = HEADERS, 
 json={'0': 'become-q22a-auto'})
created_item_id = response_create_item.json()['id'] - 1

print(f"\n2. Sending POST request to http://localhost:5002/items")

# 3. Прочитать ресурс item - GET

response_read_item = requests.get('http://localhost:5002/items/{}'.format(created_item_id), headers = HEADERS)
json_response = response_read_item.json()
item = json_response['items']

print(f"\n3. Sending GET request to http://localhost:5002/items/item_id:")
print(item)

# 4. Удалить ресурс item - DELETE

response_delete_item = requests.delete('http://localhost:5002/items/{}'.format(created_item_id), headers = HEADERS)

print(f"\n4. Sending DELETE request to http://localhost:5002/items/item_id:")