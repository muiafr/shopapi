import os

from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()


def get_config():
    if os.getenv("DATABASE"):
        return os.environ["DATABASE"]

    return URL.create(
        "postgresql+psycopg",
        username=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
        host=os.environ["DATABASE_HOST"],
        port=int(os.getenv("DATABASE_PORT", "5432")),
        database=os.environ["DATABASE_NAME"],
    )