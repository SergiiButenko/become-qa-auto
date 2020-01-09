import pytest
import requests
from login import Login
from items import ItemData
from itemsAPI import ItemsAPI

login = Login()
item_data = ItemData()
api = ItemsAPI()


@pytest.fixture(scope='session')
def token():
    return login.get_token()


@pytest.fixture(scope='function')
def create_item(token):
    r = api.post_item(item_data.generate_new_item(), token)
    yield r
    item_id = '/' + str(r.json()['id'] - 1)
    api.delete_item(item_id, token)


@pytest.fixture()
def remove_item(token):
    r = api.post_item(item_data.generate_new_item(), token)
    yield r
    item_id = '/' + str(r.json()['id'] - 1)
    r = api.get_item(item_id, token)
    assert r.status_code == api.status_codes['BAD REQUEST']


def test_create_item(create_item):
    assert create_item.status_code == api.status_codes['CREATED']


def test_get_item_by_id(create_item, token):
    item_id = '/' + str(create_item.json()['id'] - 1)
    r = api.get_item(item_id, token)
    assert r.status_code == api.status_codes['OK']


def test_check_data_for_created_item(create_item, token):
    item_id = '/' + str(create_item.json()['id'] - 1)
    r = api.get_item(item_id, token)
    assert r.json()['items']['user'] == item_data.user
    assert r.json()['items']['job'] == item_data.job


def test_delete_item_by_id(remove_item, token):
    item_id = '/' + str(remove_item.json()['id'] - 1)
    r = api.delete_item(item_id, token)
    assert r.status_code == api.status_codes['OK']
    assert r.text == 'ok'
