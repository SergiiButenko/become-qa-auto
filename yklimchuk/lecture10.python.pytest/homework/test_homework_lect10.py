#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from requests.auth import HTTPBasicAuth
import pytest


user_credentials = {"username": "test", "password": "test"}
item_data = "item_value"
status_codes = {'OK': 200, 'Created': 201, 'Bad Request': 400 }


@pytest.fixture(scope = 'session')
def user_authorization(user_credentials=user_credentials):
    resp_login = requests.post('http://localhost:5002/login', json=user_credentials)
    access_token = {'Authorization': 'Bearer {}'.format(resp_login.json()['access_token'])}

    return {
        'login_response': resp_login,
        'access_token': access_token
    }

@pytest.fixture(scope = 'function')
def create_item_response(user_authorization, item_data = item_data):
    response_create_item = requests.post('http://localhost:5002/items',
    headers = user_authorization['access_token'],
    json = item_data)

    created_item_id = response_create_item.json()['id'] - 1

    return {
        'response_create_item': response_create_item,
        'created_item_id': created_item_id
    }


def test_user_authorization(user_authorization):
    authorization_response_status = user_authorization['login_response'].status_code
    
    assert authorization_response_status == status_codes['OK']

def test_to_create_item(create_item_response):
    item_response = create_item_response['response_create_item'].status_code

    assert  item_response == status_codes['Created']

def test_read_item(user_authorization, create_item_response):
    create_response_item = requests.get('http://localhost:5002/items/{}'.format(create_item_response['created_item_id']),
     headers = user_authorization['access_token'])

    json_response = create_response_item.json()
    item_data = json_response['items']

    assert create_response_item.status_code == status_codes['OK']
    assert item_data == item_data

def test_delete_item(user_authorization, create_item_response):
    response_delete_item = requests.delete('http://localhost:5002/items/{}'.format(create_item_response['created_item_id']),
     headers = user_authorization['access_token'])

    assert response_delete_item.status_code == status_codes['OK']

def test_receiving_400_error_respons_if_read_nonexistent_item(user_authorization, create_item_response):
    response_nonexistent_item = requests.get('http://localhost:5002/items/{}'.format(create_item_response['created_item_id'] + 1),
     headers = user_authorization['access_token'])

    assert response_nonexistent_item.status_code == status_codes['Bad Request']
