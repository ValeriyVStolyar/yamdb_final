# yamdb_final

yamdb_final
<!-- 
### Краткое описание проекта

API к сайту отзывов к художекственным произведениям.

## Технологии

- Python 3.7
- Django 2.2
- Djangorestframework 3.12

## Запуск проекта в dev-режиме

- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Примените миграции БД:
```
python3 manage.py migrate
```
- При необходимости импортируйте тестовые данные в БД:
```
python3 manage.py uploadcsv
```
- Запустите проект:
```
python3 manage.py runserver
```

## Примеры запросов

```
GET http://localhost:8000/api/v1/titles/ HTTP/1.1
Content-Type: application/json
Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciO......

{
  "count": 32,
  "next": "http://127.0.0.1:8000/api/v1/titles/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Побег из Шоушенка",
      "year": 1994,
      "rating": 10.0,
      "description": null,
      "genre": [
        {
          "name": "Драма",
          "slug": "drama"
        }
      ],
      "category": {
        "name": "Фильм",
        "slug": "movie"
      }
    },
    {
      "id": 2,
      "name": "Крестный отец",
      "year": 1972,
      "rating": 4.666666666666667,
      "description": null,
      "genre": [
        {
          "name": "Драма",
          "slug": "drama"
        }
      ],
      "category": {
        "name": "Фильм",
        "slug": "movie"
      }
    },
    {
      "id": 3,
      "name": "12 разгневанных мужчин",
      "year": 1957,
      "rating": 7.5,
      "description": null,
      "genre": [
        {
          "name": "Драма",
          "slug": "drama"
        }
      ],
      "category": {
        "name": "Фильм",
        "slug": "movie"
      }
    },
    ...
  ]
}
```
```
GET http://localhost:8000/api/v1/titles/1/reviews/ HTTP/1.1
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciO......

{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "text": "Ставлю десять звёзд!\n...Эти голоса были чище и светлее тех, о которых мечтали в этом сером, убогом месте. Как будто две птички влетели и своими голосами развеяли стены наших клеток, и на короткий миг каждый человек в Шоушенке почувствовал себя свободным.",
      "author": "bingobongo",
      "score": 10,
      "pub_date": "2022-05-19T10:10:20.166481Z"
    },
    {
      "id": 2,
      "text": "Не привыкай\n«Эти стены имеют одно свойство: сначала ты их ненавидишь, потом привыкаешь, а потом не можешь без них жить»",
      "author": "capt_obvious",
      "score": 10,
      "pub_date": "2022-05-19T10:10:20.181440Z"
    }
  ]
}
```

## Документация

http://localhost:8000/redoc/

## Авторы

Alexander aka R6DJO, Tatyana aka tachanka595 and Valery aka ValeriyVStolyar

### Описание команд для запуска приложения в контейнерах

Клонируем директорию yamdb_final из удаленного репозитория на github.com, в которой создаем служебный файл .env с переменными окружения.

Из файла приложения выполняем команду docker-compose up -d

### Шаблон наполнения env-файла

DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД

### Описание команды для заполнения базы данными

По адресу http://localhost/admin/ авторизуемся как админ и заполняем базу данных. -->
