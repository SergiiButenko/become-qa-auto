# Задание1. Разобрать код. 
# 1. Ответить на вопрос: "Что тут происходит?"
# 2 .Что такое raise_for_status() 
# 3. for цикл в питоне
# 4. как добавить третий запрос на 'http://localhost:5002/basic_auth'
import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth


# sending hhtp requests one by one in cycle 
for url in ['http://localhost:5002/', 'http://localhost:5002/fail500', 

# uncomment below to: 1) without authorization catch 401 error
#'http://localhost:5002/basic_auth'
]: 

# try to send request  
    try:

# if 200ok  print 'Success!' message#
        print(f"\nSending GET request to {url}") 
        response = requests.get(url)

# 2) with authorization 
        responseWithToken = requests.get('http://localhost:5002/basic_auth', 
        auth = HTTPBasicAuth('sergii', 'hello'))

         
# method raises an exception if a request is unsuccessful (with http errors)
        response.raise_for_status()

# 2) with authorization
        responseWithToken.raise_for_status()

# if catch HTTP errors (400+, 500+) print error code and description
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

# if catch any exception errors print error text
    except Exception as err:
        print(f'Other error occurred: {err}')

    else:
        print('Success!')

# 2) with authorization
        print(f"\nSending GET request to http://localhost:5002/basic_auth:\n" + responseWithToken.text)
        