# Yamdb-Final

[![Workflow status](https://github.com/gasimovv21/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](http://84.252.142.26)

## **Описание**


- Вы человек творческий? ✨
- Любите делиться своими мыслями? 🤔
- Книги ? Фильмы ? Музыка? 🤓
- Вы пришли прямо по адресу, теперь на просторах интернета есть проект API-Yamdb. 🥳
- API-Yamdb. Социальная сеть, в которой хранятся произведения (книги 📚, фильмы 📽️ или музыка 🎶) с возможностью оставить свой отзыв и делиться своими мыслями. 💥

### _**Инструкция по установке:**_

## Заполняем env файл:

# Указываем секретный ключ
```
SECRET_KEY = example(свой ключ, ниже способ как сгенерировать ключ. 🔻)
```
# Для генерации ключа в терминале выполняем: 
```
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
# Указываем, что работаем с postgresql
```
DB_ENGINE=django.db.backends.postgresql 
```
# Имя базы данных
```
DB_NAME=example (назовите свой)
```
# Логин для подключения к базе данных (назовите свой)
```
POSTGRES_USER=example
```
# Пароль для подключения к БД (установите свой)
```
POSTGRES_PASSWORD=postgres
```
# Название сервиса (контейнера)
```
DB_HOST=db
```
# Порт для подключения к БД 
```
DB_PORT=5432
```
### Перейти в директорию с файлом docker-compose и выполнить:
```
sudo docker-compose up -d --build
```
### Выполнить миграции внутри контейнера:
```
docker-compose exec web python manage.py migrate
```
```
docker-compose exec web python manage.py createsuperuser
```
```
docker-compose exec web python manage.py collectstatic --no-input
```
### Создайте дамп (резервную копию) базы:
```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

### После запуска приложение, автор советует ознакомиться с ReDoc чтобы было удобно воспользоваться сервисом API-Yamdb:

- _**ReDoc ℹ️ - http://localhost/redoc/**_

### _**Автор:**_

- _**Эльтун Гасимов 👨‍💻 - https://github.com/gasimovv21**_
