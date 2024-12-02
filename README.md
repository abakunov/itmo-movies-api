# ITMO Movies API

ITMO Movies API — это RESTful API для управления списком фильмов. Проект создан с использованием Django и Django REST Framework, работает с PostgreSQL в Docker-контейнере.

---

## Функционал

1. **Фильмы:**
   - Получение списка фильмов (`GET /api/movies/`)
   - Получение информации о фильме по ID (`GET /api/movies/<id>/`)
   - Добавление нового фильма (`POST /api/movies/`)
   - Обновление информации о фильме (`PATCH /api/movies/<id>/`)
   - Удаление фильма (`DELETE /api/movies/<id>/`)

2. **Директора:**
   - Все фильмы связаны с режиссерами.
   - Режиссеры хранятся в отдельной таблице.

3. **Валидация данных:**
   - Год выпуска фильма: от 1900 до 2100.
   - Рейтинг фильма: от 0 до 10.
   - Все поля обязательны для заполнения.

---

## Как запустить проект

### Требования
- Установленный Docker и Docker Compose.

### Шаги для запуска

1. **Клонировать репозиторий**:
   ```bash
   git clone <URL-репозитория>
   cd ITMO-MOVIES-API
   ```
2. **Собрать и запустить контейнеры**:
   ```bash
   docker-compose up --build
   ```
3. **API будет доступно по адресу**:
   ```bash
   http://127.0.0.1:8000/api/
   ```
4. **Админка доступна по адресу**:
   ```bash
   http://127.0.0.1:8000/admin
   ```
Логин и пароль для администратора можно настроить с помощью команды:
   ```bash
    docker-compose exec web python manage.py createsuperuser
   ```

## Структура проекта
- **movies/api** — обработка запросов (views, serializers).
- **movies/core** — модели данных, фикстуры для начальных данных.
- **Dockerfile** — описание контейнера для запуска приложения.
- **docker-compose.yml** — настройка Docker-контейнеров (Django и PostgreSQL).

### Фикстуры
Проект автоматически загружает тестовые данные:

- **Режиссеры**: core/fixtures/directors.json
- **Фильмы**: core/fixtures/movies.json

## Подтверждение работы
![telegram-cloud-photo-size-2-5364334365552797325-y](https://github.com/user-attachments/assets/6c2e8a18-5904-4b13-96d5-c77e9335b65b)
![telegram-cloud-photo-size-2-5364334365552797327-y](https://github.com/user-attachments/assets/1c0125c8-73ca-4ad0-8199-57252a2a9a02)
![telegram-cloud-photo-size-2-5364334365552797331-y](https://github.com/user-attachments/assets/16621b5d-7f43-4953-874e-c7918718b779)
![telegram-cloud-photo-size-2-5364334365552797334-y](https://github.com/user-attachments/assets/c5eef29c-12cb-4ff9-b9af-64b63cc70d66)

