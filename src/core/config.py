import os
from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()


def get_config():
    database_url = os.getenv("DATABASE")
    if database_url:
        return database_url

    try:
        return URL.create(
            drivername="postgresql+psycopg",
            username=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST", "localhost"),
            database=os.getenv("DATABASE_NAME"),
            port=int(os.getenv("DATABASE_PORT", "5432")),
        )
    except (TypeError, ValueError) as e:
        raise RuntimeError(f"Invalid database configuration: {e}") from e