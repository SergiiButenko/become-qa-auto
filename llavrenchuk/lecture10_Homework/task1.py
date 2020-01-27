# Задание1. Используя локально запущеный simple-app.py.
# Написать позитивные тесты для проверки: 
# 1. Пользователь test может авторизироваться с паролем test
# 2. Пользователь test может создать ресурс item - POST
# 3. Пользователь test может прочитать ресурс item - GET
# 4. Пользователь test может удалить ресурс item - DELETE

# Написать пару негативных тестов. 

import requests


def test_login():
    result = requests.post('http://localhost:5002/login', json={'username': 'test', 'password': 'test'})
    assert 200 == result.status_code
