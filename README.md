# RIP

Для запуска бэкенда нужно сделать несколько шагов:

1. Собрать и запустить докер-контейнер с настроенной MySQL
    1.1 Зайти в папку MySQL

    ```
    cd MySQL
    ```

    1.2 Запустить сборку докер-образа

    ```
    docker compose build
    ```

    1.3 Запустить докер-контейнер

    ```
    docker compose up -d
    ```

2. Запуск бэкенда
    2.0 Вернуться в папку RIP
    ```
    cd ..
    ```

    2.1 Установить библиотеки для работы бэкенда
    ```
    pip install -r requirements.txt
    ```

    2.2 Провести миграции (создать таблицы в БД)
    ```
    python3 manage.py migrate
    ```

    2.3 Запустить сервер
    ```
    python3 manage.py runserver 0.0.0.0:8000
    ```

    2.4 В отдельном терминале запустить скрипт создания начальных записей
    ```
    cd create_test_data
    python3 run.py
    ```



Бэкенд состоит из одного эндпоинта: /api/v1/execute

Он принимает 4 типа запросов: GET, POST, PATCH, DELETE

JSON запрос для GET ничего не принимает


Пример JSON запроса для POST (все поля кроме image обязательны для заполнения, пример работы с image в папке create_test_data, в поле gender может быть только M или F, в поле kind - Dog или Cat):
```
{
    "title": "Пупсик",
    "description": "Милый пупсик",
    "kind": "Dog",
    "breed": "пуп",
    "age": 1,
    "gender": "M",
    "location": "Москва",
    "price": 16000
}
```

Пример JSON запроса для PATCH (id обязателен для заполнения + нужен параметр, который будет меняться):
```
{
    "id": 7,
    "price": 1000
}
```

Пример JSON запроса для DELETE (id - обязательный и единственный ключ):
```
{
    "id": 7
}
```


## Авторизация:
1. Получаем токены JWT (POST /api/token/)
Пример запроса:
```
{
    "username": "vasya",
    "password": "1"
}
```

Формат ответа:
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5c..."
}
```

2. Для получения доступа к страницам с обязательной авторизацией требуется в Headers положить ключ: значение
ключ: Authorization
значение: Bearer ...(тут access token)

пример: "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

3. Для обновления токена нужно использовать refresh токен (POST /api/token/refresh/)
Формат запроса:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
```
Формат ответа:
```
{
    "access": "eyJhbGciOiJIUz...",
    "refresh": "eyJhbGciOiJIUzI1NiIsIn..."
}
```


## Для обычного пользователя
1. Авторизируемся

2. Получаем одноразовый uuid для подключения к вебсокету (GET /api/ws_token/)
*для выполнения операции нужно авторизоваться

Формат ответа:
```
{
    "uuid": "0e4b4018-f2f4-49e4-8bb3-0e5845e58455"
}
```


3. Получаем id комнаты к которой можно подключиться (GET /api/v1/support_chat)
*для выполнения операции нужно авторизоваться

Формат ответа:
```
{
    "room_name": 2
}
```

4. Подключаемся к вебсокету
```
ws://localhost:8000/ws/chat/id_комнаты/?uuid=...
```

## Для сотрудника техподдержки
1. Авторизуемся

2. Получаем одноразовый uuid для подключения к вебсокету (GET /api/ws_token/)
*для выполнения операции нужно авторизоваться

Формат ответа:
```
{
    "uuid": "0e4b4018-f2f4-49e4-8bb3-0e5845e58455"
}
```

3. Получаем список комнат, доступных для подключения (GET /api/v1/chats_list)
*для выполнения операции нужно авторизоваться

Формат ответа:
```
{
    "chats": [
        {
            "chat_name": "2",
            "support_read": true
        }
    ]
}
```

4. Подключаемся к вебсокету
```
ws://localhost:8000/ws/chat/id_комнаты/?uuid=...
```