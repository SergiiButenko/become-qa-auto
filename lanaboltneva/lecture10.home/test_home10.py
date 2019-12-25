# Задание1. Используя локально запущеный simple-app.py.
# Написать позитивные тесты для проверки: 
# 1. Пользователь test может авторизироваться с паролем test
# 2. Пользователь test может создать ресурс item - POST
# 3. Пользователь test может прочитать ресурс item - GET
# 4. Пользователь test может удалить ресурс item - DELETE
# Написать пару негативных тестов. 


import requests
from requests.auth import HTTPBasicAuth
import pytest


user_test_credentials = {"username": "test", "password": "test"}
user_with_invalid_credentials = {"username": "teuust", "password": "yruufu"}
expected_item_data = {'0': 'become-qa-auto'}
expected_status_codes = {'OK': 200, 'Created': 201, 'Bad Request': 400, 'Unauthorized': 401}


@pytest.fixture(scope = 'session')
def user_authorization(user_credentials = user_test_credentials):
    response = requests.post(
    'http://localhost:5002/login',
    json = user_credentials
    )

    token = {'Authorization': 'Bearer {}'.format(response.json()['access_token'])}

    return {
        'authorization_response': response,
        'login_token' : token
    }

@pytest.fixture(scope = 'function')
def create_item_response(user_authorization, item_data = expected_item_data):  
    response_create_item = requests.post('http://localhost:5002/items',
    headers = user_authorization['login_token'], 
    json = item_data)

    created_item_id = response_create_item.json()['id'] - 1

    return {
        'response_create_item' : response_create_item,
        'created_item_id' : created_item_id
    }


# 1. Пользователь test может авторизироваться с паролем test
def test_verify_that_user_is_able_to_authorize_with_his_password(user_authorization):
    actual_authorization_response_status_code = user_authorization['authorization_response'].status_code
    
    assert actual_authorization_response_status_code == expected_status_codes['OK']
    
# 2. Пользователь test может создать ресурс item - POST
def test_verify_that_user_is_able_to_create_item_via_POST_request(create_item_response):
    actual_post_item_response_status_code = create_item_response['response_create_item'].status_code
    
    assert  actual_post_item_response_status_code == expected_status_codes['Created']

# 3. Пользователь test может прочитать ресурс item - GET
def test_verify_that_user_is_able_to_read_item_via_GET_request(user_authorization, create_item_response):
    actual_get_response_item = requests.get('http://localhost:5002/items/{}'.format(create_item_response['created_item_id']),
     headers = user_authorization['login_token'])
    
    json_response = actual_get_response_item.json()
    actual_item_data = json_response['items']
    
    assert actual_get_response_item.status_code == expected_status_codes['OK']
    assert actual_item_data == expected_item_data   

# 4. Пользователь test может удалить ресурс item - DELETE
def test_verify_that_user_is_able_to_delete_item_via_DELETE_request(user_authorization, create_item_response):
    actual_response_delete_item = requests.delete('http://localhost:5002/items/{}'.format(create_item_response['created_item_id']),
     headers = user_authorization['login_token'])
     
    assert actual_response_delete_item.status_code == expected_status_codes['OK']

# 5. Негативная проверка: проверить, что пользователь test НЕ может авторезироваться с невалидным паролем
def test_verify_that_user_receives_401_error_if_logins_with_invalid_password(user_credentials = user_with_invalid_credentials):
    actual_not_authorized_response = requests.post('http://localhost:5002/login', json = user_credentials)

    assert actual_not_authorized_response.status_code == expected_status_codes['Unauthorized']

# 6. Негативная проверка: проверить, что пользователь test НЕ может прочитать несуществующий ресурс item
def test_verify_that_user_receives_400_error_if_tries_to_read_nonexistent_item_via_GET_request(user_authorization, create_item_response):
    actual_get_response_nonexistent_item = requests.get('http://localhost:5002/items/{}'.format(create_item_response['created_item_id'] + 1),
     headers = user_authorization['login_token'])
    
    assert actual_get_response_nonexistent_item.status_code == expected_status_codes['Bad Request']