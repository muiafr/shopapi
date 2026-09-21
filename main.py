from fastapi import FastAPI

from src.api.main import router as health_router
from src.database.database import engine, Base
from src.models.users.users_table import Users
from src.models.products.products_table import Products
from src.quiries.orm import Orm
from src.routes.users.users import router as users
from src.routes.products.products import router as products
app = FastAPI()


app.include_router(health_router)
app.include_router(users)
app.include_router(products)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
Orm.insert_user()

