'''Requests: Позволяет легко отправлять HTTP запросы и
получать ответы в различных форматах, включая JSON.
Это полезно для работы с API,
так как можно легко интегрировать внешние сервисы в приложения.'''
import requests

# Запрос данных с сайта
url = 'https://api.github.com'
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    data = response.json()  # Преобразуем ответ в JSON
    print("Ответ с сервера:")
    print(data)
else:
    print("Ошибка при запросе:", response.status_code)