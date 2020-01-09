# Задание2. Используя локально запущеный simple-app.py: 
# 1. Авторизироваться пользователем tets с паролем test
# 2. Создать ресурс item
# 3. Прочитать ресурс item
# 4. Удалить ресурс item

import requests

r = requests.post('http://localhost:5002/', auth = {'username': 'test', 'password': 'test'})
