# Задание2. Используя локально запущеный simple-app.py: 
# 1. Авторизироваться пользователем tets с паролем test
# 2. Создать ресурс item - POST
# 3. Прочитать ресурс item - GET
# 4. Удалить ресурс item - DELETE
import requests

data = {
    "username": "test",
    "password": "test"
}

print("Authorize user")
response = requests.post('http://localhost:5002/login', json=data)
print('Status code is: {}'.format(response.status_code))
access_token = {'Authorization': 'Bearer {}'.format(response.json()['access_token'])}

print("Create resource")
response = requests.post('http://localhost:5002/item', headers=access_token)
print('Status code is: {}'.format(response.status_code))

item_id = response.json()['id'] - 1

# не смог взять ресурс - Not exist, так как при создании ресурса получаю {"items": [null, null, null]}
# в функции получения -> if item is None: abort(400, 'Not exist')

# response = requests.get('http://localhost:5002/item/{}'.format(item_id), headers=access_token)
# print('Status code is: {}'.format(response.status_code))
# print(response.text)

print("Delete resource")
response = requests.delete('http://localhost:5002/item/{}'.format(item_id), headers=access_token)
print('Status code is: {}'.format(response.status_code))

print("Read all resource")
response = requests.get('http://localhost:5002/item', headers=access_token)
print('Status code is: {}'.format(response.status_code))
print(response.text)
