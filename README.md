# Shop API

Начальный каркас API магазина на FastAPI и SQLAlchemy с PostgreSQL.
Проверено на Python 3.13. Бизнес-логика и модели пока не реализованы.

## Установка и запуск

Из корня проекта:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Если `.env` ещё нет, скопируйте `.env.example` в `.env`.
Заполните параметры своей базы PostgreSQL; пароль не храните в Git.
База и пользователь должны быть созданы отдельно.

```sh
python -m uvicorn main:app --reload
```

- Документация: http://127.0.0.1:8000/docs
- Проверка работы API: http://127.0.0.1:8000/health

`/health` проверяет только работу API, без подключения к базе.
`--reload` предназначен для разработки.

## Настройки базы

`.env` загружается из корня проекта. Переменные окружения имеют приоритет.
`DATABASE` позволяет задать полный URL SQLAlchemy вместо отдельных параметров.
Для PostgreSQL с установленным драйвером используйте `postgresql+psycopg://...`.
Если URL собирается из отдельных параметров, обязательны `DATABASE_USER`,
`DATABASE_PASSWORD`, `DATABASE_HOST` и `DATABASE_NAME`.
`DATABASE_PORT` по умолчанию равен `5432`; допустимы значения от 1 до 65535.

## Структура

- `main.py` — точка входа для сервера.
- `src/api/main.py` — создание FastAPI и подключение будущих маршрутов.
- `src/core/config.py` — чтение и проверка настроек базы.
- `src/database/database.py` — engine, сессии и базовый класс моделей.
- `src/routes/` — будущие маршруты API.
- `src/models/`, `src/schemas/`, `src/services/` — модели, схемы и бизнес-логика.

Сессия `get_db()` закрывается после запроса. Изменения данных необходимо
подтверждать явно через `commit()` в коде операции.
