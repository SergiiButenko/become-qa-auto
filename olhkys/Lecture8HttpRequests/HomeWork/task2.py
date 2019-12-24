# Задание2. Используя локально запущеный simple-app.py:
# 1. Авторизироваться пользователем tets с паролем test
import requests
from requests.exceptions import HTTPError

userName = 'test'
userPass = 'test'
keyUserName = 'username'
keyUserPass = 'password'
keyLogin = 'login'
accessToken = 'access_token'
url_login = 'http://localhost:5002/login'
url_protected = 'http://localhost:5002/protected'


response = requests.post(url_login, json={keyUserName: userName, keyUserPass: userPass})
token = response.json()[accessToken]
response = requests.get(url_protected, headers={'Authorization': f"Bearer {token}"})
print(response.status_code)


# 2. Создать ресурс item - POST
keyItemName = 'name'
itemName ='newItem'
url_item = 'http://localhost:5002/item'
itemIdToDelete = 1
try:
    responseCreate = requests.post(url_item, json={keyItemName: itemName}, headers={'Authorization': f"Bearer {token}"})
    responseCreate.raise_for_status()
except HTTPError as http_err:
    #not autorizied for ex.
    print(f'HTTP error occurred: {http_err}')
else:
    print('Created successfully.')

    itemIdToDelete = responseCreate.json()['id']
    print(responseCreate.json()['id'])


# 3. Прочитать ресурс item - GET
try:
    responseRead = requests.get(url_item, json={keyItemName: itemName}, headers={'Authorization': f"Bearer {token}"})
    responseRead.raise_for_status()
except HTTPError as http_err:
    #not autorizied for ex.
    print(f'HTTP error occurred: {http_err}')
else:
    print(responseRead.text)



# 4. Удалить ресурс item - DELETE
try:
    responseDel = requests.delete(f'{url_item}/?{itemIdToDelete}',  headers={'Authorization': f"Bearer {token}"})

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
else:
    print(responseDel.status_code)