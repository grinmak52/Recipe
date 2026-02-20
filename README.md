## Recipe — pet‑project для портфолио

**Recipe** — учебный проект про рецепты, сделанный в двух вариантах:

- **`django_app/`** — классическое веб‑приложение на Django (SSR: шаблоны, формы, авторизация).
- **`fastapi_app/`** — отдельный REST API на FastAPI (версионирование `/api/v1`, async SQLAlchemy).

Проект показывает умение собрать **полный цикл CRUD**, работу с **БД**, **валидацией**, **маршрутизацией**, а также разделение кода на слои (routes/schemas/crud/dependencies).

---

## Стек

- **Язык**: Python (в `pyproject.toml` указано `>=3.14`)
- **Backend (SSR)**: Django
- **Backend (API)**: FastAPI, Uvicorn
- **База данных**: PostgreSQL
- **ORM**:
  - Django ORM (в Django-части)
  - SQLAlchemy 2 (async) + `asyncpg` (в FastAPI-части)
- **Валидация/схемы**: Pydantic
- **Конфиги**: `pydantic-settings` (переменные окружения для FastAPI)
- **Утилиты**: slugify / `python-slugify`, Pillow (изображения)
- **Управление зависимостями**: Poetry (`pyproject.toml`, `poetry.lock`)

---

## Что умеет проект

- **Рецепты**: создание, просмотр, редактирование, удаление
- **Аккаунты (Django)**: регистрация, вход, профиль и обновление профиля
- **API (FastAPI)**: CRUD для рецептов по `/api/v1/recipes`
- **Авторизация (FastAPI)**: JWT Bearer-токен для определения `author_id`

---

## Структура репозитория

```text
.
├─ django_app/                 # Django-проект (UI + server-side rendering)
│  ├─ manage.py                # Точка входа Django CLI
│  ├─ config/                  # settings/urls/asgi/wsgi
│  ├─ accounts/                # регистрация/логин/профиль (views/forms/urls/models)
│  ├─ recipes/                 # рецепты (views/forms/urls/models + migrations)
│  ├─ templates/               # шаблоны: base + accounts + recipes
│  └─ static/                  # статика (CSS)
│
├─ fastapi_app/                # FastAPI-приложение (REST API)
│  ├─ main.py                  # создание app и подключение роутеров
│  ├─ api_v1/                  # роутинг API v1
│  │  └─ recipes/              # routes + crud + schemas + dependencies
│  └─ core/                    # конфиг и модели БД
│     ├─ config.py             # api_v1_prefix, DB_URL, DB_ECHO
│     └─ models/               # SQLAlchemy модели + db_helper (engine/session)
│
├─ pyproject.toml              # зависимости/настройки Poetry
└─ poetry.lock
```

---

## Ключевые файлы и папки

### Django (`django_app/`)

- **Маршрутизация**: `django_app/config/urls.py` (подключает `recipes` и `accounts`)
- **Настройки**: `django_app/config/settings.py` (PostgreSQL, static/media, installed apps)
- **Шаблоны**: `django_app/templates/`
- **Статика**: `django_app/static/`

### FastAPI (`fastapi_app/`)

- **Точка входа**: `fastapi_app/main.py` (префикс берётся из `settings.api_v1_prefix`, по умолчанию `/api/v1`)
- **Роуты v1**: `fastapi_app/api_v1/`
- **Auth**: `POST /api/v1/auth/token` (dev-only) и JWT-проверка токена
- **Рецепты**: `fastapi_app/api_v1/recipes/` (`views.py`, `schemas.py`, `crud.py`, `dependencies.py`)
- **База/сессии**: `fastapi_app/core/models/db_helper.py`
- **Настройки**: `fastapi_app/core/config.py` (например, `DB_URL`)
 - **Безопасность**: `fastapi_app/core/security.py` (создание/проверка JWT)

---

## Запуск (локально)

Сконфигурируйте переменные окружения:

```bash
copy .env.example .env
```

Далее откройте `.env` и задайте реальные значения (например, доступ к PostgreSQL).

Установка зависимостей:

```bash
poetry install
```

### Django

```bash
poetry run python django_app/manage.py migrate
poetry run python django_app/manage.py runserver
```

### FastAPI

```bash
poetry run uvicorn fastapi_app.main:app --reload --host 127.0.0.1 --port 8001
```

#### Получить токен (для демо)

Dev-only эндпоинт, чтобы удобно тестировать API:

```bash
curl -X POST http://127.0.0.1:8001/api/v1/auth/token -H "Content-Type: application/json" -d "{\"user_id\": 1}"
```

Дальше используйте токен в запросах:

```bash
curl http://127.0.0.1:8001/api/v1/recipes/ -H "Authorization: Bearer <TOKEN>"
```

---

## Переменные окружения

Основные параметры находятся в `.env`:

- **Django**
  - `DJANGO_SECRET_KEY`
  - `DJANGO_DEBUG`
  - `DJANGO_ALLOWED_HOSTS`
  - `DJANGO_DB_ENGINE`, `DJANGO_DB_NAME`, `DJANGO_DB_USER`, `DJANGO_DB_PASSWORD`, `DJANGO_DB_HOST`, `DJANGO_DB_PORT`
- **FastAPI**
  - `API_V1_PREFIX`
  - `DB_URL`
  - `DB_ECHO`
  - `JWT_SECRET`, `JWT_ALGORITHM`, `JWT_EXPIRES_MINUTES`

