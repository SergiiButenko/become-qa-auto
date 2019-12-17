# Задание2. Используя локально запущеный simple-app.py:
# 1. Авторизироваться пользователем tets с паролем test
# 2. Создать ресурс item
# 3. Прочитать ресурс item
# 4. Удалить ресурс item
import random
import requests

item_url = 'http://localhost:5002/item/'
user = f"Alex_{random.randint(0, 100)}"
# Тут не нужны formatted strings. Просто вызоа рандомизатора
password = f"{random.randint(0, 9999999)}"

# Get access token
# Не называй переменные get_bla - это к методам и функциям
get_token = requests.post(
    'http://localhost:5002/login',
    json={'username': 'test', 'password': 'test'}
)
token = {'Authorization': f"Bearer {get_token.json()['access_token']}"}

# Create resource
# Та же фигня со строками. просто передай переменные
create_response = requests.post(
    'http://localhost:5002/item', json={"login": f"{user}", "password": f"{password}"}, headers=token
)
# А если 200, а не 201 - это эррор или всетаки нет
if create_response.status_code == 201:
    print('POST Success with code 201!')
else:
    print(f'An error has occurred during POST request. {create_response.status_code}')
         
# Строки... не злоупотребляй 
item_id = f"{create_response.json()['id'] - 1}"

# Check if resource was created
get_created_item = requests.get(item_url + item_id, headers=token)
new_user = get_created_item.json()['items']['login']
new_pass = get_created_item.json()['items']['password']
if new_user == user and new_pass == password:
    print(f"GET Success with code {get_created_item.status_code}!\n"
          f"User '{new_user}' with password '{new_pass}' was created successfully.")
else:
    print(f"User '{user}' was not created with Status Code: {create_response.status_code}.")

# Remove resource
remove_response = requests.delete(item_url + item_id, headers=token)
if remove_response.status_code == 200:
    print('DELETE Success with code 200!')
else:
    print('An error has occurred during DELETE request.')

# Just double-check if item removed
is_item_removed = requests.get(item_url + item_id, headers=token)
if is_item_removed.status_code != '200' and remove_response.text == 'ok':
    print(f"User '{new_user}' has been successfully deleted.")
else:
    print(f"User '{new_user}' was not removed with Status Code:{remove_response.status_code} or something going wrong.")
