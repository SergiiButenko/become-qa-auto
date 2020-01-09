import pytest
from login import Login
from itemsAPI import ItemsAPI

header = {"Content-Type": "application/json"}
txt_header = {"Content-Type": "text/html"}
login = Login()
api = ItemsAPI()


def test_login_success():
    r = login.login_valid_user()
    assert r.status_code == api.status_codes['OK']
    assert r.headers['Content-Length'] == '579'
    assert r.headers['Content-Type'] == 'application/json'
    assert r.json()['access_token'] is not None


def test_bad_login():
    r = login.login_as("test1", "test")
    assert r.status_code == api.status_codes['UNAUTHORIZED']
    assert r.headers['Content-Type'] == 'application/json'
    assert r.json()['msg'] == "Bad username or password"


def test_login_without_body():
    r = login.login_without_body()
    assert r.status_code == api.status_codes['INTERNAL SERVER ERROR']


def test_login_txt_format():
    r = login.login_valid_user_in_format(txt_header)
    assert r.status_code == api.status_codes['INTERNAL SERVER ERROR']






