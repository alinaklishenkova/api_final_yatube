# API для Yatube

## Описание
REST API для социальной сети Yatube. Позволяет создавать посты, комментарии, группы и подписки на авторов.

## Установка

1. Клонируйте репозиторий:

    git clone [https://github.com/alinaklishenkova/api_final_yatube.git](https://github.com/alinaklishenkova/api_final_yatube.git)

    cd api_final_yatube


2. Создайте виртуальное окружение:

    python -m venv venv

    source venv/Scripts/activate


3. Установите зависимости:

    cd yatube_api

    pip install -r ../requirements.txt


4. Выполните миграции:

    python manage.py migrate


5. Создайте суперпользователя:

    python manage.py createsuperuser


6. Запустите сервер:

    python manage.py runserver


## Примеры запросов

Получение JWT-токена:
```
POST /api/v1/jwt/create/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```
Создание поста:
```
POST /api/v1/posts/
Content-Type: application/json
Authorization: Bearer <your_token>

{
    "text": "Текст поста",
    "group": 1
}
```
