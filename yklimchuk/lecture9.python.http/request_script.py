# import requests
#
# #response = requests.get('http://localhost:5002/')
# #print(response.__dict__)
#
# # response = requests.get('http://localhost:5002/')
# # print(response.status_code)
# # print(response.json())
# # response2 = requests.get('http://localhost:5002/fail500')
# # print(response2.status_code)
# # print(response.json())
# # response3 = requests.get('http://localhost:5002/users')
# # print(response3.status_code)
# # print(response.json())
#
# response = requests.get( 'https://api.github.com/search/repositories',
#     params={'q': 'become-qa-auto'})
#
# json_response = response.json()

# import requests
# from requests.auth import HTTPBasicAuth

# response = requests.get(
#     'http://localhost:5002/basic_auth',
#     auth=HTTPBasicAuth('sergii', 'hello')
# )
#
# print(response.text)

# import requests
#
# response = requests.post(
#     'http://localhost:5002/login',
#     json={'username': 'test', 'password': 'test'}
#     )
#
# print(response.json())


import requests
from requests.auth import HTTPBasicAuth

response = requests.post(
    'http://localhost:5002/login',
    json={'username': 'test', 'password': 'test'}
    )

token = response.json()['access_token']
print(f"token: {token}\n")

print("sending not authoraized request")
response = requests.get(
    'http://localhost:5002/protected',
    )
print(response.text)

print("sending authoraized request")
response = requests.get(
    'http://localhost:5002/protected',
    headers={'Authorization': f"Bearer {token}"}
    )
print(response.text)