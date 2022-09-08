# dfа_test

Находясь в папке с файлом `docker-compose.yml` выполнить в терминале:

    cp .env.example .env

	docker-compose up -d


## API:

 `/api/token/refresh` - Обновить jwt токен

 `/api/token` - Получить jwt токен

 `/swagger` - Сваггер со всеми юрлами

 `/gallery` - CRUD для галереи

 `/users` - Создание пользователя

 `/users/{id}` - Ретрив пользователя

