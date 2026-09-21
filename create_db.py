from sqlalchemy import create_engine, text
from src.core.config import get_config

# get_config() возвращает URL из отдельных параметров .env
url = get_config()
db_name = url.database

admin_engine = create_engine(
    url.set(database="postgres"),
    isolation_level="AUTOCOMMIT",
)

with admin_engine.connect() as connection:
    exists = connection.execute(
        text("SELECT 1 FROM pg_database WHERE datname = :name"),
        {"name": db_name},
    ).scalar()

    if not exists:
        quoted_name = connection.dialect.identifier_preparer.quote_identifier(
            db_name
        )
        connection.execute(text(f"CREATE DATABASE {quoted_name}"))

admin_engine.dispose()