import requests


class BaseAPI:
    url = 'http://localhost:5002/items'

    status_codes = {'OK': 200,
                    'CREATED': 201,
                    'BAD REQUEST': 400,
                    'UNAUTHORIZED': 401,
                    'INTERNAL SERVER ERROR': 500}

    def __init__(self, url=url):
        self.url = url
        self.api_provider = 

    def post(self, url, data, token):
        return requests.post(self.url, json=item_data, headers=token)

    def get(self, item_id, token):
        return requests.get(self.url + item_id, headers=token)

    def delete(self, item_id, token):
        return requests.delete(self.url + item_id, headers=token)

    def put(self):
        pass