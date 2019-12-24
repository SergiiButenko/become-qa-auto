import requests
 
# Поиск местонахождения для запросов на GitHub
response = requests.post(
    'http://localhost:5002/',
    json={'serbut': 'value'}
)
 
# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()
print(f'Response: {json_response}')  # Python 3.6+