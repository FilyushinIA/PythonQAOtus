# PythonQAOtus
Курс Python QA Engineer (OTUS)

Тестирование API
Цель: Тестирование API сервиса с помощью Python используя библиотеки pytest, requests, json.
Тестирование каждого api оформить в отдельном тестовом модуле.

1. Тестирование REST сервиса https://dog.ceo/dog-api/ (test_dogs.py)

2. Тестирование REST сервиса https://www.openbrewerydb.org/(test_breweries.py)

3. Тестирование REST сервиса https://jsonplaceholder.typicode.com/ (test_json_holder.py)

4. Реализация тестовой функции, принимающей 2 параметра (test_url_status/test_url_status,py):
url - должно быть значение по умолчанию https://ya.ru
status_code - значение по умолчанию 200
Проверка по переданному урлу статус ответа
Пример запуска pytest test_module.py --url=https://mail.ru --status_code=200
