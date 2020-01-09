import requests


class Login:
    valid_login_data = {"username": "test", "password": "test"}
    login_url = 'http://localhost:5002/login'

    def __init__(self, url=login_url, credentials=valid_login_data):
        self.credentials = credentials
        self.url = url

    def login_valid_user(self):
        return requests.post(self.url, json=self.credentials)

    def login_as(self, username, password):
        login_cred = {"username": username, "password": password}
        return requests.post(self.url, json=login_cred)

    def login_without_body(self):
        r = requests.post(self.url)
        return r

    def login_valid_user_in_format(self, headers):
        return requests.post(self.url, json=self.credentials, headers=headers)

    def get_token(self):
        token = self.login_valid_user().json()['access_token']
        return {'Authorization': f"Bearer {token}"}




