# Задание1. Используя локально запущеный simple-app.py.
# Написать позитивные тесты для проверки: 
# 1. Пользователь test может авторизироваться с паролем test
# 2. Пользователь test может создать ресурс item - POST
# 3. Пользователь test может прочитать ресурс item - GET
# 4. Пользователь test может удалить ресурс item - DELETE

# Написать пару негативных тестов. 

import requests
import pytest

login_data = {"username": "test", "password": "test"}
item_data = "item_value"
status_codes = {'OK': 200, 'Created': 201, 'Bad Request': 400, 'Internal Server Error': 500}


@pytest.fixture(scope="session")
def get_response(credentials=login_data, data_=item_data):
    resp_login = requests.post('http://localhost:5002/login', json=credentials)
    access_token = {'Authorization': 'Bearer {}'.format(resp_login.json()['access_token'])}
    resp_create_item = requests.post('http://localhost:5002/item', headers=access_token, json=data_)
    item_id = resp_create_item.json()['id'] - 1
    resp_get_item = requests.get('http://localhost:5002/item/{}'.format(item_id), headers=access_token)
    resp_delete_item = requests.delete('http://localhost:5002/item/{}'.format(item_id), headers=access_token)
    resp_get_item_failed = requests.get('http://localhost:5002/item/{}'.format(resp_create_item.json()['id']),
                                        headers=access_token)
    resp_delete_item_failed = requests.delete('http://localhost:5002/item/{}'.format(resp_create_item.json()['id']),
                                              headers=access_token)
    return {
        'status_code_login': resp_login.status_code,
        'status_code_create_item': resp_create_item.status_code,
        'status_code_get_item': resp_get_item.status_code,
        'status_code_delete_item': resp_delete_item.status_code,
        'status_code_delete_item_failed': resp_delete_item_failed.status_code,
        'status_code_get_item_failed': resp_get_item_failed.status_code,
        'access_token': access_token
    }


def test_get_authorization(get_response):
    assert get_response['status_code_login'] == status_codes['OK']
    assert get_response['access_token'] is not None


def test_create_item(get_response):
    assert get_response['status_code_create_item'] == status_codes['Created']


def test_get_item_by_id(get_response):
    assert get_response['status_code_get_item'] == status_codes['OK']


def test_delete_item_by_id(get_response):
    assert get_response['status_code_delete_item'] == status_codes['OK']


def test_get_authorization_failed(get_response):
    assert get_response['status_code_get_item_failed'] == status_codes['Bad Request']


def test_delete_item_by_id_failed(get_response):
    assert get_response['status_code_delete_item_failed'] == status_codes['Internal Server Error']
