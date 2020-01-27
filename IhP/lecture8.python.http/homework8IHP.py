# Задание1. Разобрать код.
# 1. Ответить на вопрос: "Что тут происходит?"
#We are sending request to each http address and receiving answer for each request, in first case "Success" because
# we don't have errors after this request, than we have additional break line because of \n in print statement,
# in the second and third requests we have received raised for status http errors.

# 2 .Что такое raise_for_status()
#Raises stored HTTPError, if one occurred.

# 3. for цикл в питоне
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# 4. как добавить третий запрос на 'http://localhost:5002/basic_auth'
#It is just necessary to add 'http://localhost:5002/basic_auth' into the loop list

import requests
from requests.exceptions import HTTPError

for url in ['http://localhost:5002/', 'http://localhost:5002/fail500', 'http://localhost:5002/basic_auth']:
    try:
        print(f"\nSending GET request to {url}")
        response = requests.get(url)

        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
