from fastapi import FastAPI

from src.api.main import router as health_router
from src.database.database import engine, Base
from src.models.users.users_table import Users
from src.models.products.products_table import Products

app = FastAPI()

app.include_router(health_router)

Base.metadata.create_all(bind=engine)