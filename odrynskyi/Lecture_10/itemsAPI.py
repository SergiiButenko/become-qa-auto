import requests


class ItemsAPI:
    url = 'http://localhost:5002/items'

    status_codes = {'OK': 200,
                    'CREATED': 201,
                    'BAD REQUEST': 400,
                    'UNAUTHORIZED': 401,
                    'INTERNAL SERVER ERROR': 500}

    def __init__(self, url=url):
        self.url = url

    def post_item(self, item_data, token):
        return requests.post(self.url, json=item_data, headers=token)

    def get_item(self, item_id, token):
        return requests.get(self.url + item_id, headers=token)

    def delete_item(self, item_id, token):
        return requests.delete(self.url + item_id, headers=token)

    def get_all_items(self, token):
        return requests.get(self.url, headers=token)