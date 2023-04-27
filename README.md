### Проект yatube_api: Описание

Проект создан в учебных целях, с помощью этого приложения 
вы можете создавать посты, оставлять комментарии к интересным вам 
постам, а так же подписываться на интересных вам авторов. 
Приложение создано с помощью фрэимворка Django Rest Framework

#### При необходимости, можете развернуть приложение у себя локально

Первое что вам нужно, это 
клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/fazletdinov/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

#### Здесь покажем основные endpoint, с которыми вы можете взаимодействовать
Для создания пользователя
```
http://127.0.0.1:8000/api/v1/users/
```
Для получения jwt токена
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
Для обновления jwt токена
```
http://127.0.0.1:8000/api/v1/jwt/refresh/
```
Для CRUD операций с постами, читать посты могут все, 
а добавлять, удалять, обновлять могут лишь авторизованные
пользователи
```
http://127.0.0.1:8000/api/v1/posts/
```
Для CRUD операций с комментариями,
читать могут все, но оставлять комментарии, редактировать их
и удалять могут лишь авторизованные пользователи
```
127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
Группы может добавлять лишь администратор
через админ панель,
остальные могут только читать
```
http://127.0.0.1:8000/api/v1/groups/
```
Подписыватться можете на любого, кроме самого себя,
соответственно доступно лишь авторизованным пользователям
```
http://127.0.0.1:8000/api/v1/follow/
```