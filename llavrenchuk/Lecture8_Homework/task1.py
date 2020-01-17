# Задание1. Разобрать код. 
# 1. Ответить на вопрос: "Что тут происходит?"
# 2 .Что такое raise_for_status()
# 3. for цикл в питоне
# 4. как добавить третий запрос на 'http://localhost:5002/basic_auth'
import requests 
from requests.exceptions import HTTPError 
from requests.auth import HTTPBasicAuth
 
for url in ['http://localhost:5002/', 'http://localhost:5002/fail500', 'http://localhost:5002/basic_auth']: 
    try: 
        print(f"\nSending GET request to {url}") 
        response = requests.get(url,auth=HTTPBasicAuth('sergii','hello')) 

        response.raise_for_status() 
        
    except HTTPError as http_err:  
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(f'Success! {response.text}')          
