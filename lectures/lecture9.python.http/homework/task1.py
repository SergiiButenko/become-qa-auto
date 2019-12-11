# Задание1. Разобрать код. 
# 1. Ответить на вопрос: "Что тут происходит?"
# 2 .Что такое raise_for_status()
# 3. for цикл в питоне
# 4. как добавить третий запрос на 'http://localhost:5002/basic_auth'
import requests # импортируем библиотеку requests
from requests.exceptions import HTTPError # из библиотеки requests.exceptions импортируем HTTPError
 
for url in ['http://localhost:5002/', 'http://localhost:5002/fail500','http://localhost:5002/basic_auth']: # в цикле перебираются урлы
    try: # обработка исключений. Здесь в блоке мы выполняем инструкцию, которая может породить исключение.
        print(f"\nSending GET request to {url}") # информационный вывод об отправке реквеста на итерируемый урл
        response = requests.get(url) # создается переменная с результатом вызова состояния

        response.raise_for_status() # вызов исключения, если запрос был неудачным.
        # HTTPError будет вызываться для определенных кодов состояния. Если код состояния указывает на успешный запрос, программа продолжит работу без возникновения этого исключения.
    except HTTPError as http_err:  # обработка исключений. Здесь в блоке мы перехватываем исключения.
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')          # если никаких исключений/ ошибок в итерируемой урле не возникло, выводится сообщение об успешном результате
