# Пример базового микросервисного приложения Django + JS + Nginx (Docker) 
Этот репозиторий содержит минимальную, но рабочую структуру микросервисного приложения. 

Технологии:
- **Django** – бэкенд
- **JavaScript (Vanilla)** – фронтенд
- **Nginx** – для раздачи статики и маршрутизации между сервисами
- **Docker Compose** – для удобной локальной сборки и запуска
## Установка и запуск
```
docker-compose build
docker-compose up 
```
### Инициализация БД
```
Для инициализации БД
docker exec site_architecture-python-1 python3 manage.py migrate

Для загрузки базовых примеров БД
docker exec site_architecture-python-1 python3 manage.py loaddata db_dump.json
```
## Сайт будет доступен по адресу localhost:8080
